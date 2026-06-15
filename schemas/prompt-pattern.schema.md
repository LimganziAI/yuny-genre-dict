# prompt-pattern.schema.md — Reusable Prompt Pattern Schema

Lives in `knowledge-evolving/prompt-patterns/`. A pattern is a *promoted* technique — born from 3+ cases, never from theory alone.
Filename: `PP-NNN_short-slug.md`

```yaml
pattern_id: PP-NNN
name: # short, functional ("vocal-rescue stack", "era-anchor position-1")
applies_to: CREATE | COVER | LYRICS | EXCLUDE | SLIDERS
trigger: # when to reach for this
template: |
  # exact field text with {slots}
placement: # which field, which position zone
provenance: [C-..., C-..., C-...] # the cases that earned it
confidence: low | med | high
source_type: official | community | experiment
side_effects: # known costs (e.g., "suppresses vocal processing if paired with 'compressed' in EXCLUDE")
counter_indications: # genres/modes where this backfires
last_validated: YYYY-MM-DD + suno_model
```

Rules:
- `community`/`experiment` patterns MUST carry provenance+confidence — result quality over purity, but never disguise a hack as canon.
- Re-validate `high` confidence patterns after each Suno model update; downgrade if behavior shifted.
- A pattern contradicted by 2+ new cases → demote to `experiment`, note why.
