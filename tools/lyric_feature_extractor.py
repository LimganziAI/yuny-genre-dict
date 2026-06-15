#!/usr/bin/env python3
# Nonverbatim lyric structure extractor.
# It never prints source lyric lines.

import argparse, json, csv, re, zipfile
from pathlib import Path
from collections import Counter
from statistics import median, mean

HANGUL = re.compile(r"[가-힣]")
ENG = re.compile(r"[A-Za-z]")

def hlen(s): return len(HANGUL.findall(s or ""))

def ending(line):
    l = re.sub(r"\[[^\]]*\]|\([^\)]*\)", "", str(line))
    l = re.sub(r"[^\w가-힣]+$", "", l.strip())
    if not l: return "empty"
    if re.search(r"(까|니|냐|나요|래요|을까|ㄹ까|인가|지)$", l): return "question_open"
    if re.search(r"(야|이야|거야|꺼야|잖아|다고|라고|니까|거든|구나|네)$", l): return "direct_speech"
    if re.search(r"(어|아|해|돼|봐|줘|와|가)$", l): return "plain_open"
    if re.search(r"(다|한다|였다|했다|된다|있다|없다)$", l): return "statement_da"
    if re.search(r"(고|서|는데|지만|면)$", l): return "connector_cut"
    if re.search(r"(요|어요|아요|해요|네요)$", l): return "polite"
    if ENG.search(l[-1]): return "english_end"
    return "other"

def metrics_for_lines(lines):
    clean = [str(x).strip() for x in lines if str(x).strip()]
    if not clean: return None
    lengths = [hlen(x) for x in clean]
    hang = sum(lengths)
    eng = sum(len(ENG.findall(x)) for x in clean)
    return {
        "line_count": len(clean),
        "median_hangul_syllables": median(lengths),
        "avg_hangul_syllables": round(mean(lengths), 2),
        "short_line_ratio_le5": round(sum(1 for x in lengths if x <= 5)/len(lengths), 3),
        "long_line_ratio_ge15": round(sum(1 for x in lengths if x >= 15)/len(lengths), 3),
        "repeat_line_ratio": round((len(clean)-len(set(clean)))/len(clean), 3),
        "english_char_share": round(eng/max(1, eng+hang), 3),
        "ending_counts": dict(Counter(ending(x) for x in clean).most_common())
    }

def iter_files(path):
    p = Path(path)
    if p.is_dir():
        for child in p.rglob("*"):
            if child.suffix.lower() in [".json", ".jsonl", ".csv", ".txt"]:
                yield child.name, child.read_bytes()
    elif p.suffix.lower() == ".zip":
        with zipfile.ZipFile(p) as z:
            for n in z.namelist():
                if n.lower().endswith((".json",".jsonl",".csv",".txt")):
                    yield n, z.read(n)
    else:
        yield p.name, p.read_bytes()

def extract_lines_from_json(obj):
    if isinstance(obj, dict):
        if isinstance(obj.get("lyrics"), dict) and isinstance(obj["lyrics"].get("lines"), list):
            return obj["lyrics"]["lines"]
        for key in ["lyrics", "lyric", "가사", "text", "content"]:
            if isinstance(obj.get(key), str):
                return obj[key].splitlines()
        return []
    return []

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    aggregate = Counter()
    per_song = []
    for name, data in iter_files(args.input):
        try:
            text = data.decode("utf-8-sig", errors="replace")
            lines = []
            if name.lower().endswith(".json"):
                obj = json.loads(text)
                lines = extract_lines_from_json(obj)
            elif name.lower().endswith(".jsonl"):
                for row in text.splitlines():
                    if not row.strip(): continue
                    lines += extract_lines_from_json(json.loads(row))
            elif name.lower().endswith(".txt"):
                lines = text.splitlines()
            elif name.lower().endswith(".csv"):
                rows = csv.DictReader(text.splitlines())
                for r in rows:
                    for col in ["lyrics","lyric","가사","text","content"]:
                        if col in r and r[col]:
                            lines = r[col].splitlines()
                            break
                    if lines: break
            m = metrics_for_lines(lines)
            if m:
                per_song.append({"source": name, **m})
                aggregate.update(m["ending_counts"])
        except Exception:
            continue

    counts = [x["line_count"] for x in per_song]
    out = {
        "files_with_lyrics": len(per_song),
        "line_count_median": median(counts) if counts else None,
        "ending_counts_total": dict(aggregate.most_common()),
        "per_song_nonverbatim": per_song
    }
    Path(args.output).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()
