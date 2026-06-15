# genre-card.schema.md — Genre Dictionary Entry Schema

Lives in `knowledge-evolving/genre-dictionary/23_GENRE_FULLBODY/<category>/<slug>.md`. Index: `genre-dictionary/index/GENRE_INDEX.md`.

```yaml
slug: # kebab-case microgenre id
names: [primary, aliases, 한국어명]
parent: # macro genre (NEVER goes in Position 1 — microgenre does)
era_region_scene: # the anchor triple
bpm_range: # typical + feel notes
key_tonal_color: # common keys/modes, brightness
vocal_posture: # default vocal identity tendencies
core_instruments: # 3-6, with articulation hints
signature_motifs: # rhythmic/harmonic/textural fingerprints
production_traits: # mix-era markers (tape sat, gated reverb, sidechain pump...)
adjacent_slugs: # fallback ladder targets
suno_keywords: # field-ready descriptor phrases (positive only)
exclude_candidates: # known drift directions to block
reference_dna: # functional notes only — no protected expression
```

Lookup ladder: exact slug → adjacent slug → parent fallback DNA → prompt-encode from this schema's fields.
