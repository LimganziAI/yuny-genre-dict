#!/usr/bin/env python3
# Nonverbatim NIKL dialogue/register probe.
# It never prints utterance text.

import argparse, json, re, zipfile
from pathlib import Path
from collections import Counter
from statistics import median

HANGUL = re.compile(r"[가-힣]")
ENG = re.compile(r"[A-Za-z]")
SMALL = ["그냥","뭐","좀","자꾸","괜히","막","진짜","아니","근데","그래서","그니까","약간","되게","뭔가","아무튼","일단","그런데","그러니까"]

def hlen(s): return len(HANGUL.findall(s or ""))

def ending(line):
    l = re.sub(r"[^\w가-힣]+$", "", str(line).strip())
    if not l: return "empty"
    if re.search(r"(까|니|냐|나요|래요|을까|ㄹ까|인가|지)$", l): return "question_open"
    if re.search(r"(야|이야|거야|꺼야|잖아|다고|라고|니까|거든|구나|네)$", l): return "direct_speech"
    if re.search(r"(어|아|해|돼|봐|줘|와|가)$", l): return "plain_open"
    if re.search(r"(고|서|는데|지만|면)$", l): return "connector_cut"
    if re.search(r"(요|어요|아요|해요|네요)$", l): return "polite"
    if re.search(r"(다|한다|였다|했다|된다|있다|없다)$", l): return "statement_da"
    return "other"

def iter_json(path):
    p = Path(path)
    if p.suffix.lower() == ".zip":
        with zipfile.ZipFile(p) as z:
            for n in z.namelist():
                if n.lower().endswith(".json"):
                    yield json.loads(z.read(n).decode("utf-8-sig", errors="replace"))
    elif p.is_dir():
        for child in p.rglob("*.json"):
            yield json.loads(child.read_text(encoding="utf-8-sig"))
    else:
        yield json.loads(p.read_text(encoding="utf-8-sig"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    lengths = []
    ends = Counter()
    smalls = Counter()
    relations = Counter()
    docs = 0
    utts = 0

    for obj in iter_json(args.input):
        for doc in obj.get("document", []):
            docs += 1
            setting = doc.get("metadata", {}).get("setting", {})
            if isinstance(setting, dict) and setting.get("relation"):
                relations[setting["relation"]] += 1
            for u in doc.get("utterance", []) or []:
                form = (u.get("form") or u.get("original_form") or "").strip()
                if not form: continue
                utts += 1
                lengths.append(hlen(form))
                ends[ending(form)] += 1
                for word in SMALL:
                    if word in form:
                        smalls[word] += 1

    sl = sorted(lengths)
    out = {
        "documents": docs,
        "utterances": utts,
        "utterance_length_p25_median_p75": [sl[int(len(sl)*.25)], median(sl), sl[int(len(sl)*.75)]] if sl else None,
        "ending_counts": dict(ends.most_common()),
        "small_words": dict(smalls.most_common()),
        "relations": dict(relations.most_common()),
        "note": "No utterance text is exported."
    }
    Path(args.output).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()
