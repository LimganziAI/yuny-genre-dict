# production-quality-hacks/

Result-first prompt techniques for audio quality — official documentation NOT required for entry. Community lore, experiments, and "shouldn't-work-but-does" phrasings live here, each with mandatory provenance + confidence (prompt-pattern.schema.md format).

Philosophy (master request §9): the goal is output quality, not theoretical purity. But honesty about evidence level is non-negotiable:
- `source_type: official` — documented Suno behavior
- `source_type: community` — multiple independent reports, link/quote the provenance
- `source_type: experiment` — our own cases only; cite case IDs

Canonical baseline stack lives in `../production-engineering/cover_quality_stack_runtime.md` (vocal bus warmth, artifact removal, breath texture, tube saturation, ±8 cent detune L15/R15, vocal corridor 500Hz-3kHz, de-ess 5-8kHz, mono sub 20-80Hz, kick/bass separation, ~80ms sidechain for dance, 200-400Hz mud carve, 2-5kHz smoothing, 8-14kHz air, depth/placement, tail control, transient punch, bus glue, tape sat, genre loudness targets). Hacks here EXTEND that stack; they never silently replace it.

Demotion: a hack contradicted by 2+ cases or broken by a model update → move to cases/experiments/ with a post-mortem note.
