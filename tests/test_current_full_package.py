from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INSTALL_ROOT = ROOT.parents[1] if ROOT.parent.name == "3_GITHUB_UPLOAD_STRUCTURE" else ROOT

def read(p):
    return p.read_text(encoding="utf-8")

def assert_true(x, msg):
    if not x:
        raise AssertionError(msg)

def test_current_full_repo():
    assert_true((ROOT / "README.md").exists(), "repo README missing")
    assert_true((ROOT / "project-sync" / "PROJECT_INSTRUCTIONS.txt").exists(), "project-sync instructions missing")
    assert_true((ROOT / "project-sync" / "knowledge-20").exists(), "project-sync knowledge-20 missing")
    assert_true(len(list((ROOT / "project-sync" / "knowledge-20").glob("*.md"))) == 20, "project-sync knowledge count != 20")
    assert_true((ROOT / "knowledge-evolving").exists(), "knowledge-evolving missing")
    assert_true((ROOT / "knowledge-evolving" / "genre-dictionary").exists(), "genre dictionary missing")
    assert_true((ROOT / "lyric-craft").exists(), "lyric-craft missing")
    assert_true((ROOT / "production-engineering").exists(), "production-engineering missing")
    assert_true((ROOT / "prompt-patterns").exists(), "prompt-patterns missing")
    assert_true((ROOT / "tests").exists(), "tests missing")
    assert_true((ROOT / "cases").exists(), "cases missing")

def test_install_instruction_and_knowledge():
    instr = read(ROOT / "project-sync" / "PROJECT_INSTRUCTIONS.txt")
    assert_true(len(instr) < 8000, f"instructions too long: {len(instr)}")
    must = [
        "FIRST EXECUTABLE DRAFT",
        "INTERNAL PRODUCTION COUNCIL",
        "CREATE SOURCE SIM",
        "COVER PRE-FINAL SIM",
        "5000-RUNWAY LAW",
        "STANDARD LAW",
        "COVER is final record",
    ]
    for token in must:
        assert_true(token in instr, f"missing instruction token: {token}")

    names = sorted(p.name for p in (ROOT / "project-sync" / "knowledge-20").glob("*.md"))
    assert_true(len(names) == 20, "knowledge-20 not exactly 20")
    assert_true("10_reference_assimilation_functional_rebuild.md" in names, "functional reference file missing")
    assert_true("10_reference_assimilation_protected_expression_guard.md" not in names, "old protected filename remains in install mirror")

def test_no_patch_only_upload_shape():
    file_count = len([p for p in ROOT.rglob("*") if p.is_file()])
    assert_true(file_count > 500, f"repo tree too small; patch-only likely: {file_count}")
    assert_true((ROOT / "operator-history").exists(), "operator-history missing")
    assert_true((ROOT / "vocal-palette").exists(), "vocal-palette missing")
    assert_true((ROOT / "suno-render-behavior").exists(), "suno-render-behavior missing")

def test_behavioral_runtime_tokens():
    blob = "\n".join(read(p) for p in (ROOT / "project-sync" / "knowledge-20").glob("*.md"))
    required = [
        "render_stage",
        "revision_entrypoint",
        "cue-prompt sync",
        "Dual 5000-Character Runways",
        "COVER Final Record Preflight",
        "Toy Texture Risk Gate",
        "Anti-Old Melody Repair",
        "Multi-Role Production Council",
        "Behavior Tests Over Token Presence",
    ]
    for token in required:
        assert_true(token in blob, f"missing behavioral token: {token}")

if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"PASS {name}")
