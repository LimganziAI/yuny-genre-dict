#!/usr/bin/env python3
# YUNY Source Intake Packager
# Standard-library only. It prepares research/source files for upload to ChatGPT/YUNY
# as manifests, safe text samples, and upload-sized ZIP batches.
#
# Usage:
#   python yuny_source_intake_packager.py prepare ./my_sources --out ./yuny_intake --max-mb 450
#   python yuny_source_intake_packager.py prepare urls.txt ./local_folder --out ./yuny_intake
#
# urls.txt can contain one URL per line. Downloads are optional and run only on the user's machine.

from __future__ import annotations
import argparse, csv, datetime as _dt, hashlib, json, os, pathlib, shutil, sys, tarfile, urllib.request, zipfile

TEXT_EXTS = {'.txt','.md','.csv','.tsv','.json','.jsonl','.yaml','.yml','.py','.js','.html','.htm','.xml'}
ARCHIVE_EXTS = {'.zip','.tar','.gz','.tgz','.bz2','.xz'}
MAX_SAMPLE_BYTES = 200_000

def sha256_file(path: pathlib.Path, chunk: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        while True:
            b = f.read(chunk)
            if not b: break
            h.update(b)
    return h.hexdigest()

def is_url(s: str) -> bool:
    return s.startswith('http://') or s.startswith('https://')

def safe_name(s: str) -> str:
    keep = []
    for ch in s:
        if ch.isalnum() or ch in '._-()[] 한글abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            keep.append(ch)
        else:
            keep.append('_')
    return ''.join(keep)[:180] or 'source'

def download_url(url: str, raw_dir: pathlib.Path) -> pathlib.Path:
    name = safe_name(url.rstrip('/').split('/')[-1] or 'download')
    dst = raw_dir / name
    if dst.exists():
        stem, suffix = dst.stem, dst.suffix
        i = 2
        while (raw_dir / f"{stem}_{i}{suffix}").exists():
            i += 1
        dst = raw_dir / f"{stem}_{i}{suffix}"
    print(f"[download] {url} -> {dst}")
    with urllib.request.urlopen(url, timeout=60) as r, dst.open('wb') as f:
        shutil.copyfileobj(r, f)
    return dst

def load_sources(args) -> list[pathlib.Path]:
    raw_dir = pathlib.Path(args.out) / 'raw_sources'
    raw_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for item in args.inputs:
        p = pathlib.Path(item)
        if p.exists():
            if p.is_file() and p.suffix.lower() == '.txt':
                lines = p.read_text(encoding='utf-8', errors='ignore').splitlines()
                for line in lines:
                    line = line.strip()
                    if not line or line.startswith('#'): continue
                    if is_url(line):
                        paths.append(download_url(line, raw_dir))
                    else:
                        lp = pathlib.Path(line)
                        if lp.exists(): paths.append(lp)
            else:
                paths.append(p)
        elif is_url(item):
            paths.append(download_url(item, raw_dir))
        else:
            print(f"[warn] missing input ignored: {item}", file=sys.stderr)
    return paths

def iter_files(paths):
    for p in paths:
        p = pathlib.Path(p)
        if p.is_dir():
            for f in p.rglob('*'):
                if f.is_file():
                    yield f
        elif p.is_file():
            yield p

def extract_archive(path: pathlib.Path, extract_root: pathlib.Path):
    target = extract_root / safe_name(path.name)
    target.mkdir(parents=True, exist_ok=True)
    try:
        if path.suffix.lower() == '.zip':
            with zipfile.ZipFile(path) as z:
                z.extractall(target)
            return target, 'zip'
        if tarfile.is_tarfile(path):
            with tarfile.open(path) as t:
                t.extractall(target)
            return target, 'tar'
    except Exception as e:
        return None, f'extract_failed:{e}'
    return None, 'not_archive'

def sample_text_file(path: pathlib.Path, sample_dir: pathlib.Path, rel_label: str) -> str:
    try:
        data = path.read_bytes()[:MAX_SAMPLE_BYTES]
        text = data.decode('utf-8', errors='ignore')
        sample_name = safe_name(rel_label.replace(os.sep, '__')) + '.sample.txt'
        out = sample_dir / sample_name
        out.write_text(text, encoding='utf-8')
        return str(out.relative_to(sample_dir.parent))
    except Exception as e:
        return f'sample_failed:{e}'

def write_manifest(rows, out_dir: pathlib.Path):
    jsonl = out_dir / 'manifest.jsonl'
    with jsonl.open('w', encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    csvp = out_dir / 'manifest.csv'
    keys = ['path','kind','ext','size','sha256','source_root','sample','note']
    with csvp.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for r in rows:
            w.writerow({k:r.get(k,'') for k in keys})

def zip_under_limit(files: list[pathlib.Path], base_dir: pathlib.Path, upload_dir: pathlib.Path, max_bytes: int):
    upload_dir.mkdir(parents=True, exist_ok=True)
    batches = []
    current, current_size = [], 0
    for f in sorted(files, key=lambda x: str(x)):
        size = f.stat().st_size
        if size > max_bytes:
            # large single file: place alone and warn. User may need platform-level split/partial upload.
            if current:
                batches.append(current); current, current_size = [], 0
            batches.append([f])
            continue
        if current and current_size + size > max_bytes:
            batches.append(current); current, current_size = [], 0
        current.append(f); current_size += size
    if current: batches.append(current)
    zip_paths = []
    for i, batch in enumerate(batches, 1):
        zp = upload_dir / f'yuny_upload_batch_{i:03d}.zip'
        with zipfile.ZipFile(zp, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
            for f in batch:
                try:
                    z.write(f, f.relative_to(base_dir))
                except ValueError:
                    z.write(f, f.name)
        zip_paths.append(zp)
    return zip_paths

def make_report(out_dir: pathlib.Path, rows, zips):
    exts = {}
    total = 0
    for r in rows:
        exts[r['ext']] = exts.get(r['ext'], 0) + 1
        total += int(r['size'] or 0)
    report = out_dir / 'YUNY_SOURCE_INTAKE_REPORT.md'
    report.write_text(f"""# YUNY SOURCE INTAKE REPORT

Generated: {_dt.datetime.now().isoformat(timespec='seconds')}

## What this bundle is for
This bundle is for YUNY system/knowledge improvement. Source materials are used as craft evidence, gates, tests, and pattern ledgers. Protected sentences, lyrics, poems, or corpus lines must not be copied into generated lyrics.

## Counts
- files indexed: {len(rows)}
- total bytes: {total}
- upload batches: {len(zips)}

## Extension counts
{chr(10).join(f'- `{k or "<none>"}`: {v}' for k,v in sorted(exts.items()))}

## Upload advice
Upload:
1. `manifest.csv`
2. `manifest.jsonl`
3. `YUNY_SOURCE_INTAKE_REPORT.md`
4. relevant `samples/` files
5. original archives or `upload_batches/` if needed

If any source is too large for one upload, keep the original archive and upload its split parts together. YUNY can use the manifest first, then request only targeted files.
""", encoding='utf-8')

def cmd_prepare(args):
    out = pathlib.Path(args.out).resolve()
    raw_dir = out / 'raw_sources'
    extracted = out / 'extracted_archives'
    samples = out / 'samples'
    upload = out / 'upload_batches'
    for d in [raw_dir, extracted, samples, upload]:
        d.mkdir(parents=True, exist_ok=True)

    source_paths = load_sources(args)
    initial_files = list(iter_files(source_paths))
    rows = []
    extract_roots = []
    for f in initial_files:
        kind = 'file'
        note = ''
        ext = ''.join(f.suffixes[-2:]).lower() if f.name.endswith(('.tar.gz','.tar.bz2','.tar.xz')) else f.suffix.lower()
        if f.suffix.lower() == '.zip' or tarfile.is_tarfile(f):
            root, status = extract_archive(f, extracted)
            kind = 'archive'
            note = status
            if root: extract_roots.append(root)
        sample = ''
        if f.suffix.lower() in TEXT_EXTS:
            sample = sample_text_file(f, samples, f.name)
        try:
            rows.append({
                'path': str(f),
                'kind': kind,
                'ext': ext,
                'size': f.stat().st_size,
                'sha256': sha256_file(f),
                'source_root': '',
                'sample': sample,
                'note': note
            })
        except Exception as e:
            rows.append({'path': str(f), 'kind': kind, 'ext': ext, 'size': '', 'sha256': '', 'source_root': '', 'sample': sample, 'note': f'stat_failed:{e}'})

    for root in extract_roots:
        for f in root.rglob('*'):
            if not f.is_file(): continue
            sample = ''
            if f.suffix.lower() in TEXT_EXTS:
                sample = sample_text_file(f, samples, str(f.relative_to(root)))
            try:
                rows.append({
                    'path': str(f.relative_to(out)),
                    'kind': 'extracted',
                    'ext': f.suffix.lower(),
                    'size': f.stat().st_size,
                    'sha256': sha256_file(f),
                    'source_root': str(root.relative_to(out)),
                    'sample': sample,
                    'note': ''
                })
            except Exception as e:
                rows.append({'path': str(f), 'kind': 'extracted', 'ext': f.suffix.lower(), 'size': '', 'sha256': '', 'source_root': str(root), 'sample': sample, 'note': f'stat_failed:{e}'})

    write_manifest(rows, out)
    # Bundle manifest/samples first, not all raw archives by default.
    package_files = [out/'manifest.csv', out/'manifest.jsonl', out/'YUNY_SOURCE_INTAKE_REPORT.md'] if (out/'YUNY_SOURCE_INTAKE_REPORT.md').exists() else [out/'manifest.csv', out/'manifest.jsonl']
    package_files += [f for f in samples.rglob('*') if f.is_file()]
    max_bytes = int(float(args.max_mb) * 1024 * 1024)
    zips = zip_under_limit(package_files, out, upload, max_bytes)
    make_report(out, rows, zips)
    # rebuild batches including report
    for z in zips:
        z.unlink(missing_ok=True)
    package_files = [out/'manifest.csv', out/'manifest.jsonl', out/'YUNY_SOURCE_INTAKE_REPORT.md'] + [f for f in samples.rglob('*') if f.is_file()]
    zips = zip_under_limit(package_files, out, upload, max_bytes)
    print(f"[done] {out}")
    print(f"[manifest] {out/'manifest.csv'}")
    for z in zips:
        print(f"[batch] {z}")

def main():
    ap = argparse.ArgumentParser(description='Prepare source material for YUNY/ChatGPT upload.')
    sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('prepare')
    p.add_argument('inputs', nargs='+', help='files, folders, urls, or txt containing paths/urls')
    p.add_argument('--out', default='yuny_intake_out')
    p.add_argument('--max-mb', default='450')
    args = ap.parse_args()
    if args.cmd == 'prepare':
        cmd_prepare(args)

if __name__ == '__main__':
    main()
