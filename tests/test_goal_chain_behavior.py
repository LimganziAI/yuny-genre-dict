#!/usr/bin/env python3
from pathlib import Path
import re

def _find_install_root(start):
    for d in [start, *start.parents]:
        if (d/"1_PROJECT_INSTRUCTIONS").is_dir() and (d/"2_KNOWLEDGE_FILES").is_dir() and (d/"3_GITHUB_UPLOAD_STRUCTURE").is_dir():
            return d
    raise AssertionError("install root not found")

ROOT = _find_install_root(Path(__file__).resolve())
GH_BASE = ROOT/"3_GITHUB_UPLOAD_STRUCTURE"
GH = next((d for d in GH_BASE.iterdir() if d.is_dir() and (d/"tests").exists()), GH_BASE)

def read(p): return p.read_text(encoding="utf-8")

def test_universal_lyric_gate_is_not_character_only():
    instr = read(next((ROOT/"1_PROJECT_INSTRUCTIONS").glob("*.txt")))
    k05 = read(ROOT/"2_KNOWLEDGE_FILES"/"05_lyric_dossier_and_5000_script_engine.md")
    k06 = read(ROOT/"2_KNOWLEDGE_FILES"/"06_korean_lyric_prosody_hook.md")
    blob = (instr + "\n" + k05 + "\n" + k06).lower()
    for token in ["universal lyric", "speaker", "situation", "object bank", "thought spine", "hook"]:
        assert token in blob, f"missing universal lyric component: {token}"
    assert "character or not" in blob or "not character-only" in blob, "universal gate must not be character-only"
    for bad in ["ai summary", "generic uplift", "pretty concept list"]:
        assert bad in blob, f"missing anti-generic lyric failure class: {bad}"

def test_goal_chain_is_encoded_end_to_end():
    blob = "\n".join(read(p) for p in (ROOT/"2_KNOWLEDGE_FILES").glob("*.md")).lower()
    required = [
        "first executable draft",
        "create source sim",
        "cover final",
        "dual 5000-character runways",
        "cover final record preflight",
        "cue-prompt sync",
        "render_stage",
        "revision_entrypoint",
        "liked lyric",
        "quality stack",
        "audio influence",
    ]
    for token in required:
        assert token in blob, f"missing end-to-end chain token: {token}"

def test_behavioral_acceptance_matrix_exists_and_covers_user_goal():
    matrix = GH/"tests"/"acceptance"/"AT_CURRENT_GOAL_CHAIN_BEHAVIOR.md"
    assert matrix.exists(), "goal-chain acceptance matrix missing"
    text = read(matrix).lower()
    scenarios = [
        "universal korean lyric request",
        "first executable draft",
        "create render old",
        "cover render toy",
        "cue/prompt mismatch",
        "cover lyric blind copy",
        "post-render repair entrypoint",
    ]
    for scenario in scenarios:
        assert scenario in text, f"missing scenario: {scenario}"
    assert "generic summer words only" in text, "lyric-quality failure must be behaviorally catchable"
    assert "repair cover prompt" in text, "COVER repair owner must be explicit"

def test_package_shape_and_counts_after_goal_patch():
    instr = read(next((ROOT/"1_PROJECT_INSTRUCTIONS").glob("*.txt")))
    assert len(instr) < 8000, f"instructions too long: {len(instr)}"
    assert len(list((ROOT/"2_KNOWLEDGE_FILES").glob("*.md"))) == 20
    roots = sorted(p.name for p in ROOT.iterdir())
    assert roots == ["1_PROJECT_INSTRUCTIONS", "2_KNOWLEDGE_FILES", "3_GITHUB_UPLOAD_STRUCTURE"], roots
    # Cache files are removed during packaging; pytest may create __pycache__ while running.
