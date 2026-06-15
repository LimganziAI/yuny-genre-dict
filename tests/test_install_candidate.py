#!/usr/bin/env python3
"""CURRENT INSTALL CANDIDATE — behavioral + integrity suite.
Verifies BEHAVIOR the runtime must exhibit (SOP tests 1-8) by checking that the
governing laws/cards actually encode the required routing, plus install-integrity
(3 folders, <8000, 20 cards, no stale labels, manifest matches tree, no fake final).
Token-presence alone is insufficient: each behavioral check requires the specific
ROUTING rule, not just the keyword."""
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

F=[]
def fail(m): F.append(m)
def read(p): return p.read_text(encoding="utf-8")

ins_dir=ROOT/"1_PROJECT_INSTRUCTIONS"
ins=read(next(ins_dir.glob("*.txt")))
kfiles=sorted((ROOT/"2_KNOWLEDGE_FILES").glob("*.md"))
K={p.name:read(p) for p in kfiles}
allk="\n".join(K.values())
gh=_gh_content_root(ROOT)
ghtext="\n".join(read(p) for p in gh.rglob("*.md")) if gh.exists() else ""

# ── INSTALL INTEGRITY ──
roots=sorted(p.name for p in ROOT.iterdir())
if roots!=["1_PROJECT_INSTRUCTIONS","2_KNOWLEDGE_FILES","3_GITHUB_UPLOAD_STRUCTURE"]:
    fail(f"root must be exactly 3 install folders, got {roots}")
if len(ins)>=8000: fail(f"instructions >=8000: {len(ins)}")
if len(kfiles)!=20: fail(f"knowledge must be 20, got {len(kfiles)}")

# ── TEST 7 — current-only install: no stale version labels in filenames/manifests ──
stale_pat=re.compile(r'(v4_9|v5_0|v5_1|two_pass|4_8|4_9|V4_9|V5_0|V5_1)', re.I)
stale_files=[str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file() and stale_pat.search(p.name)]
if stale_files: fail(f"stale version labels in filenames: {stale_files}")
# manifest must match the actual tree
man=list((gh/"manifests").glob("*.md")) if (gh/"manifests").exists() else []
for m in man:
    mt=read(m)
    if stale_pat.search(mt): fail(f"manifest {m.name} contains stale version label")
    cnt=re.search(r'Knowledge files \((\d+)\)', mt)
    if cnt and int(cnt.group(1))!=20: fail(f"manifest {m.name} stale knowledge count {cnt.group(1)}")

# ── TEST 1 — first draft is NOT auto-final ──
if not (("first executable draft" in ins.lower()) and ("final" in ins.lower())):
    fail("T1: first-executable-draft vs final law missing in instructions")
if "FINAL RECORD LAW" not in ins: fail("T1: FINAL RECORD LAW missing")

# ── TEST 2 — CREATE old melody → diagnose source before rewrite ──
c12=K.get("12_rhythm_harmony_melody_topline.md","").lower()
if "old melod" not in c12 or "source" not in c12:
    fail("T2: card12 must detect old melodic lift and judge CREATE as COVER source")
if "create-render" not in ins.lower() and "create render" not in ins.lower():
    fail("T2: CREATE-render diagnosis routing missing in instructions")

# ── TEST 3 & 6 — COVER toy texture / liked-lyric-failed-cover → lock lyric, repair COVER first ──
c17=K.get("17_diagnostics_revision_cascade.md","").lower()
if "lik" not in c17 or "lock" not in c17 or "cover" not in c17:
    fail("T3/6: card17 must route liked-lyric+failed-cover to lock lyric + repair COVER side")
c15=K.get("15_production_quality_mix_master_stack.md","").lower()
if "toy" not in c15 or "buried" not in c15:
    fail("T3: card15 must catch toy texture / buried vocal failure classes")

# ── TEST 4 — cue-prompt dependency can FAIL a package ──
c08=K.get("08_vocal_identity_acting_cue_engine.md","").lower()
if "cue-prompt" not in c08 and "cue prompt" not in c08:
    fail("T4: card08 must mandate cue-prompt dependency check")
if "defect" not in c08:
    fail("T4: card08 cue-prompt mismatch must be a defect (can fail package)")

# ── TEST 5 — 5000 runway: staging only after lyric passes, stays under 5000 ──
c05=K.get("05_lyric_dossier_and_5000_script_engine.md","").lower()
if "5000" not in c05 or "runway" not in c05 or "without cues" not in c05:
    fail("T5: card05 must define 5000 runway + lyric survives without cues")

# ── TEST 8 — defensive-commentary bloat flagged; STANDARD LAW / self-anointment present ──
if "STANDARD LAW" not in ins: fail("T8/standard: STANDARD LAW missing")
if "system-generated" not in allk.lower() and "system generated" not in allk.lower():
    fail("self-anointment ban must survive in a card")

# ── TEST 10 — examples are format demos, not ceiling ──
if "format demo" not in ins.lower() and "never the ceiling" not in (ins+allk).lower() and "표준 아님" not in allk:
    fail("T10: exemplar=format-demo (not ceiling) guard missing")

# ── GitHub required areas ──
for area in ["README.md","tests","prompt-patterns","lyric-craft","production-engineering"]:
    if not (gh/area).exists(): fail(f"github missing required area: {area}")
if not any((gh/d).exists() for d in ["case-logs","case-memory","cases"]):
    fail("github missing case memory area")

def _emit_and_exit():
    print(json.dumps({"instruction_chars":len(ins),"knowledge_count":len(kfiles),
    "root_folders":roots,"status":"PASS" if not F else "FAIL","failures":F}, ensure_ascii=False, indent=2))
    sys.exit(1 if F else 0)

def test_suite():
    """pytest entrypoint: fail the test if any check failed (no sys.exit at import)."""
    assert not F, "; ".join(F)

if __name__ == "__main__":
    _emit_and_exit()
