# 2026-03 — Suno v5.5: Voices, Custom Models, My Taste

Release: 2026-03-26 (verified via web, 2026-06). Affects cards 03/08/16/20.

## What changed
- **Voices** (Personas renamed + expanded): reusable vocal identities; voice creation/cloning on Pro/Premier tiers. System impact: a locked Voice can replace part of the 5-element vocal identity text — but descriptor language is STILL required for posture/acting (Voice carries timbre, not performance).
- **Custom Models**: train on your own catalog — min 6 tracks, max 3 models per account. Impact: catalog-consistent projects (character songs) can pin a model; prompts then spend fewer chars on identity, more on arrangement.
- **My Taste**: personalization from your generation history. ⚠️ Known risk (operator-observed): can reinforce old-sounding outputs by learning from prior takes. For era-jump projects, consider disabling or expect stronger drift; EXCLUDE must counter inherited traits.
- **Studio** (per 2026-02 update): 12-stem separation, six-band EQ, Warp Markers — post-gen rescue is now viable for minor mix faults; reserve COVER for structural/genre work.

## Field-level consequences
- COVER quality stack unchanged (engine still responds to descriptor language).
- Slider semantics unchanged (W/S/A ranges per card 16).
- When a Voice is pinned: drop redundant timbre words from Position 1-2; KEEP register-behavior + attitude descriptors.

## Re-validation queue
Patterns marked `confidence: high` with `last_validated < 2026-03-26` → re-test per prompt-pattern.schema.md rule.
