# INSTALL SOURCE — CURRENT (unambiguous)

The live ChatGPT Project install source is exactly:

- **Project Instructions** → `1_PROJECT_INSTRUCTIONS/PROJECT_INSTRUCTIONS.txt` (package root)
- **Knowledge** → all 20 `.md` in `2_KNOWLEDGE_FILES/` (package root)
- **GitHub** → upload/merge the FULL contents of `3_GITHUB_UPLOAD_STRUCTURE/yuny-suno-os-main/` into the repo root (not patch-only)

Repo mirror of the install source (kept in sync, byte-identical):
- `project-sync/PROJECT_INSTRUCTIONS.txt`
- `project-sync/PROJECT_INSTRUCTIONS_CURRENT.txt`
- `project-sync/knowledge/` (20 files)
- `project-sync/knowledge-20/` (20 files)

## Legacy / reference (NOT install source)
`archive/` (incl. `archive/fullbody-legacy/`, `archive/legacy-install-docs/`) and any file with a historical version label are **reference/craft material only**. The runtime never routes install through them. They are preserved on purpose — do not delete craft facts for old wording.

## Tests
Run from the package root or from `3_GITHUB_UPLOAD_STRUCTURE/yuny-suno-os-main/`:
```
python3 tests/test_current_full_package.py
python3 tests/test_install_candidate.py
python3 tests/test_register_standard_guard.py
# or: python3 -m pytest -q tests/
```
All resolve the install root robustly (no parents[N] brittleness) and verify behavior, not token presence. No false PASS.

This package is the source of truth. Live Project is not updated until the operator applies it. GitHub is not current unless the full tree above is uploaded to repo root.
