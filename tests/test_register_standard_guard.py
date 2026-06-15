#!/usr/bin/env python3
"""CURRENT behavioral guard — catches the regressions that token-presence tests miss:
(1) self-anointment ban present, (2) world craft axioms present, (3) register standards
present, (4) GitHub lyric-craft fullbody reachable by RAG, (5) no system-generated song
re-imported as a quality exemplar. These are the defects the operator actually hit."""
from pathlib import Path
import sys, json, re

def _find_install_root(start):
    """Walk upward until a directory contains all three install folders.
    Works from full-package root, from 3_GITHUB_UPLOAD_STRUCTURE/, and from
    3_GITHUB_UPLOAD_STRUCTURE/yuny-suno-os-main/tests/ alike. No false PASS:
    if the 3-folder root is genuinely absent, raise instead of silently passing."""
    for d in [start, *start.parents]:
        if (d/"1_PROJECT_INSTRUCTIONS").is_dir() and (d/"2_KNOWLEDGE_FILES").is_dir() and (d/"3_GITHUB_UPLOAD_STRUCTURE").is_dir():
            return d
    raise SystemExit("install root (3 folders) not found above " + str(start))

ROOT = _find_install_root(Path(__file__).resolve())

def _gh_content_root(root):
    """GitHub content may sit flat under 3_GITHUB_UPLOAD_STRUCTURE/ or nested under
    a single repo dir like yuny-suno-os-main/. Resolve to wherever the repo material
    actually lives (the dir that contains README.md + tests/)."""
    base = root/"3_GITHUB_UPLOAD_STRUCTURE"
    if (base/"README.md").exists() and (base/"tests").exists():
        return base
    subs = [d for d in base.iterdir() if d.is_dir() and (d/"README.md").exists() and (d/"tests").exists()]
    return subs[0] if subs else base
PKG = ROOT

failures=[]
def fail(m): failures.append(m)
def read(p): return p.read_text(encoding="utf-8")

instr=read(next((PKG/"1_PROJECT_INSTRUCTIONS").glob("*.txt")))
kfiles=sorted((PKG/"2_KNOWLEDGE_FILES").glob("*.md"))
ktext={p.name: read(p) for p in kfiles}
all_k="\n".join(ktext.values())
gh=_gh_content_root(ROOT)

# 1. self-anointment ban must live in BOTH instructions and a card (survives regen)
if "STANDARD LAW" not in instr: fail("instructions: STANDARD LAW missing")
if "no single song" not in instr.lower(): fail("instructions: self-anointment ban phrasing missing")
if "system generated" not in all_k.lower() and "system-generated" not in all_k.lower():
    fail("knowledge: self-anointment ban not restated in any card (regression risk)")

# 2. world craft axioms (character-first / lyric-as-sound / concrete-yet-open)
axioms=["character first","passing figure","lyric-as-sound"]
if not any(a in instr.lower() for a in axioms): fail("instructions: world craft axioms missing")
if "캐릭터" not in all_k and "character" not in all_k.lower(): fail("knowledge: character-first axiom missing")

# 3. register standards (5 named registers in card 06)
c06=ktext.get("06_korean_lyric_prosody_hook.md","")
reg_hits=sum(x in c06 for x in ["R1","R2","R3","R4","R5"])
if reg_hits<5: fail(f"card06: register standards incomplete ({reg_hits}/5)")
if "REGISTER STANDARDS" not in c06 and "레지스터" not in c06: fail("card06: REGISTER STANDARDS block missing")

# 4. GitHub lyric-craft fullbody must exist (RAG craft reference, previously absent)
need_gh=["lyric-craft/WORLD_LYRIC_CRAFT_STANDARDS.md",
         "lyric-craft/KOREAN_REGISTER_EXEMPLAR_BANK.md",
         "production-engineering/SELF_ANOINTMENT_AND_REGRESSION_GUARD.md"]
for rel in need_gh:
    if not (gh/rel).exists(): fail(f"github: missing {rel}")

# 5. exemplar bank must self-label as NOT the standard
bank=gh/"lyric-craft/KOREAN_REGISTER_EXEMPLAR_BANK.md"
if bank.exists():
    b=read(bank)
    if "표준 아님" not in b and "not the standard" not in b.lower() and "never the ceiling" not in b.lower():
        fail("exemplar bank: must declare it is not the quality standard")

# 6. knowledge exemplars labeled as format demos, not ceiling
if "format demo" not in instr.lower() and "format demonstration" not in all_k.lower() and "형식" not in all_k:
    fail("no 'exemplar = format demo, not ceiling' guard anywhere")

# 7. instruction length + count integrity
if len(instr)>=8000: fail(f"instructions exceed 8000: {len(instr)}")
if len(kfiles)!=20: fail(f"expected 20 knowledge files, got {len(kfiles)}")

def _emit_and_exit():
    print(json.dumps({"instruction_chars":len(instr),"knowledge_count":len(kfiles),
    "status":"PASS" if not failures else "FAIL","failures":failures}, ensure_ascii=False, indent=2))
    sys.exit(1 if failures else 0)

def test_suite():
    """pytest entrypoint: fail the test if any check failed (no sys.exit at import)."""
    assert not failures, "; ".join(failures)

if __name__ == "__main__":
    _emit_and_exit()
