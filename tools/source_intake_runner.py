#!/usr/bin/env python3
"""
YUNY source intake runner (V4.6)

Use:
  python source_intake_runner.py --manifest sources_manifest.json --out yuny_source_pack_out --chunk-mb 80

Manifest schema:
{
  "pack_name": "my_research_pack",
  "sources": [
    {
      "id": "poetry_notes_01",
      "type": "local_file",
      "path": "/path/to/file_or_folder",
      "category": "literature_poetry",
      "license_note": "owned / permitted / public-domain / research excerpt"
    },
    {
      "id": "public_dataset_readme",
      "type": "url",
      "url": "https://example.org/legal_public_readme.md",
      "category": "korean_corpus",
      "license_note": "public URL; user has permission"
    }
  ]
}

This script does not bypass paywalls, logins, DRM, or copyright restrictions.
It only packages files/URLs the operator is allowed to use.
"""
from __future__ import annotations
import argparse, json, os, shutil, zipfile, hashlib, urllib.request, pathlib, time, math

TEXT_EXTS = {".txt",".md",".csv",".json",".jsonl",".yaml",".yml",".tsv",".xml",".html",".htm",".py",".js",".css"}

def sha256_file(path: pathlib.Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def safe_name(s: str) -> str:
    return "".join(c if c.isalnum() or c in "._-" else "_" for c in s)[:120] or "source"

def copy_local(src: pathlib.Path, dest: pathlib.Path):
    if src.is_dir():
        shutil.copytree(src, dest, dirs_exist_ok=True)
    else:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)

def download_url(url: str, dest: pathlib.Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent":"YUNY-source-intake/4.6"})
    with urllib.request.urlopen(req, timeout=60) as r, dest.open("wb") as f:
        shutil.copyfileobj(r, f)

def zip_dir(src_dir: pathlib.Path, zip_path: pathlib.Path):
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in src_dir.rglob("*"):
            if p.is_file():
                z.write(p, p.relative_to(src_dir))

def split_zip_if_needed(zip_path: pathlib.Path, out_dir: pathlib.Path, chunk_mb: int):
    size = zip_path.stat().st_size
    limit = chunk_mb * 1024 * 1024
    if size <= limit:
        return [zip_path.name]
    parts=[]
    data = zip_path.read_bytes()
    for i in range(math.ceil(size/limit)):
        part = out_dir / f"{zip_path.stem}.part{i+1:02d}.bin"
        part.write_bytes(data[i*limit:(i+1)*limit])
        parts.append(part.name)
    return parts

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--out", default="yuny_source_pack_out")
    ap.add_argument("--chunk-mb", type=int, default=80)
    args=ap.parse_args()
    manifest_path=pathlib.Path(args.manifest)
    manifest=json.loads(manifest_path.read_text(encoding="utf-8"))
    out=pathlib.Path(args.out)
    raw=out/"raw_sources"
    if out.exists():
        shutil.rmtree(out)
    raw.mkdir(parents=True)

    index={"pack_name": manifest.get("pack_name","yuny_source_pack"), "created_at": time.strftime("%Y-%m-%d %H:%M:%S"), "sources":[]}
    for src in manifest.get("sources",[]):
        sid=safe_name(src.get("id","source"))
        cat=safe_name(src.get("category","uncategorized"))
        item_dir=raw/cat/sid
        item_dir.mkdir(parents=True, exist_ok=True)
        stype=src.get("type")
        if stype=="local_file":
            p=pathlib.Path(src["path"]).expanduser()
            copy_local(p, item_dir/p.name)
        elif stype=="url":
            url=src["url"]
            filename=safe_name(os.path.basename(url.split("?")[0]) or sid)
            download_url(url, item_dir/filename)
        else:
            raise ValueError(f"unknown source type: {stype}")
        files=[]
        for f in item_dir.rglob("*"):
            if f.is_file():
                files.append({"path": str(f.relative_to(raw)), "bytes": f.stat().st_size, "sha256": sha256_file(f)})
        index["sources"].append({
            "id": src.get("id"),
            "type": stype,
            "category": src.get("category"),
            "license_note": src.get("license_note",""),
            "files": files
        })

    (out/"SOURCE_INDEX.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    (out/"READ_ME_FOR_CHATGPT.md").write_text(
        "# YUNY Source Pack\n\nUpload the zip or parts to ChatGPT. The material is for function extraction, gates, tests, and patterns; not sentence copying.\n",
        encoding="utf-8"
    )
    zip_path=out/f"{safe_name(index['pack_name'])}.zip"
    zip_dir(out, zip_path)
    parts=split_zip_if_needed(zip_path, out, args.chunk_mb)
    print(json.dumps({"output_dir": str(out), "zip": zip_path.name, "upload_files": parts}, ensure_ascii=False, indent=2))

if __name__=="__main__":
    main()
