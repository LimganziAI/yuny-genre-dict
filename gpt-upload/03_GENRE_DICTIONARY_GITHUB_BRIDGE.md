# Genre Dictionary GitHub Bridge

Full genre dictionary is stored in GitHub repo upload folder:

`knowledge-evolving/genre-dictionary/`

Index files:

- `knowledge-evolving/genre-dictionary/index/GENRE_INDEX.md`
- `knowledge-evolving/genre-dictionary/index/genre_index.json`
- `knowledge-evolving/genre-dictionary/index/genre_index.csv`

Fullbody entries are under:

`knowledge-evolving/genre-dictionary/23_GENRE_FULLBODY/<category>/<slug>.md`

Total fullbody genre entries: 277

Use rule:

```text
exact slug
→ adjacent slug
→ fallback DNA
→ prompt encoding
→ case update if result teaches something
```

Do not upload the full genre dictionary into GPT Knowledge unless the builder has enough storage and retrieval remains stable. Prefer GitHub lookup for fullbody entries.
