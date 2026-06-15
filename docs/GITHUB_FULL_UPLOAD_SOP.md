# GitHub Full Upload SOP — CURRENT

Purpose: upload a full CURRENT repository tree, not a patch fragment.

Use the contents of:
```text
3_GITHUB_UPLOAD_STRUCTURE/yuny-suno-os-main/
```
as the repository root.

Required after upload:
- repo root has `README.md`
- `project-sync/PROJECT_INSTRUCTIONS.txt` exists and is under 8000 chars
- `project-sync/knowledge-20/` has exactly 20 markdown files
- `genre-dictionary/`, `knowledge-evolving/`, `lyric-craft/`, `production-engineering/`, `prompt-patterns/`, `suno-render-behavior/`, `cases/`, `tests/`, `operator-history/`, and `vocal-palette/` remain present
- legacy install docs are archive/reference only and must not be used as install source

Fail if only README, patches, or a partial folder set was uploaded.
