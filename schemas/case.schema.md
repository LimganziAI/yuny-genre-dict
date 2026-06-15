# case.schema.md — Case Record Schema (canonical)

Every result feedback worth keeping becomes one case file under `cases/{success|failure|experiments|neutral-observations}/`.
Filename: `C-YYYYMMDD-NN_short-slug.md`

```yaml
case_id: C-YYYYMMDD-NN
date: YYYY-MM-DD
mode: CREATE | COVER | ONE-SHOT | REPAIR
goal: # one line — what the operator wanted
input_summary: # request essence + key constraints (no full lyrics unless needed)
suno_model: # e.g., v5.5
sliders: # W/S/A values used (A = Audio Influence, COVER only)
what_worked: # specific, observable
what_failed: # specific, observable
failure_class: prompt-defect | suno-random | quality-stack | lyric-cue | drift | pairing | reference-miss | none
suspected_cause: # mechanism hypothesis, not vibes
fix_applied: # exact field/wording change
result_after_fix: # observed delta
reuse_tags: [genre, technique, language, ...]
promotion_status: case | pattern-candidate | promoted
privacy: public | vault
```

Rules:
- One generation = one case max. Don't merge sessions.
- `suno-random` requires 2+ regens with identical prompt before claiming.
- `privacy: vault` cases never cite operator personal data in public mirrors.
- 3+ cases sharing cause+fix → write a prompt-pattern card and set `promotion_status: pattern-candidate`.

(`case_schema.md` is the legacy filename; this file is canonical. Keep both pointing to the same spec.)
