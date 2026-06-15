# archive/claude-migration/

Traceability layer for the Claude→GPT migration. Read-only history — runtime never fetches from here.

Existing migration material in this repo:
- `../migration-v2.8/` — Claude YUNY v2.8 file set (29 .md/.txt) as migrated
- `../migration-selected/` — items hand-selected during the first GPT port

Mapping of the Claude 29-file system into the v2 rebuild:
- Master system instruction (8k compression line) → `gpt-builder/00_INSTRUCTIONS_UNDER_8000.txt`
- 07/14/15 lyric craft + 16 prosody + 17 theme/culture → cards 05/06/07 + `knowledge-evolving/lyric-expression-banks/`
- 12 vocal direction + 25 cue realization → card 08
- 28 Arrangement Director (P1-P20, producer library) → card 11 + fullbody-legacy/05
- 23a genre index + 277-entry dictionary → card 09 + `knowledge-evolving/genre-dictionary/`
- 22 K-pop deep dives + 99 vault → card 19 + `kpop-artist-dna/` + `vault/`
- Diagnostics/cascade → card 17 · Case loop/CHANGELOG discipline → cards 18/20

Rule: nothing here is patched. Corrections happen in live cards/knowledge; this layer only explains where things came from.
