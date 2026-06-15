# Import Audit and Role Allocation

Date: 2026-06-09

## Sources analyzed

| Source | Entries / files | Size |
|---|---:|---:|
| YUNY_v2.8_ChatGPT_migration.zip | 47 zip entries / 41 files | 1,786,386 bytes uncompressed |
| yuny-genre-dict-main.zip | 301 zip entries | 3,988,791 bytes uncompressed |
| Current GPT Builder md files | 20 files | 1,744,578 bytes |
| Final upload package | generated from all above | includes full repo + GPT Builder upload set |

## Preserved

- Current 20 GPT Knowledge files are preserved and patched in `knowledge-static/current-20/`.
- Claude migration source is preserved in `archive/migration-v2.8/`.
- 99 memory files are preserved in `vault/operator-private/`.
- K-pop artist deep dive is copied to `knowledge-evolving/kpop-artist-dna/`.
- Legacy reference, genre, response template, and diagnostic overflow are mapped to `knowledge-evolving/`.
- Full genre dictionary is copied to `knowledge-evolving/genre-dictionary/23_GENRE_FULLBODY/`.
- Genre index was regenerated: 277 fullbody genre entries.
- GPT paste-ready txt/md files are in `gpt-upload/` and `_GPT_BUILDER_UPLOAD/`.

## Role allocation

### Instructions
Use:
`gpt-upload/00_COPY_TO_GPT_INSTRUCTIONS_FINAL.txt`

### GPT Knowledge
Recommended strict 20-file upload set:
`_GPT_BUILDER_UPLOAD/knowledge-upload-set-20-files-recommended/`

Optional extra bridge:
`_GPT_BUILDER_UPLOAD/optional-extra-knowledge-bridge/00_GITHUB_BRIDGE_FOR_GPT_KNOWLEDGE.md`

### GitHub
Upload contents of:
`_GITHUB_REPO_UPLOAD/yuny-suno-os/`

### Large files
The full genre dictionary, archive, and 99 memory are intentionally in GitHub, not GPT Instructions.

## Manual upload note

This package is designed for manual GitHub upload. Upload the repo folder contents to the repo root.
