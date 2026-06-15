# PATCH MANIFEST — Completion/COVER Quality Runtime (2026-06-13)

## Purpose
Fix the milk/cola session failure class:
- lyric quality improved but full process did not complete before 8-field delivery
- invalid sliders appeared
- COVER quality degraded, sounded dated, vocal collapsed mono/buried, shouts/cues under-rendered
- GitHub reference routes were not specific enough

## Replacement scope
Project:
- 1_PROJECT_INSTRUCTIONS/PROJECT_INSTRUCTIONS.txt

Knowledge:
- 03_create_cover_engine.md
- 04_suno_field_grammar_output_format.md
- 05_lyric_dossier_and_5000_script_engine.md
- 06_korean_lyric_prosody_hook.md
- 08_vocal_identity_acting_cue_engine.md
- 14_cover_transform_preserve_substitution.md
- 15_production_quality_mix_master_stack.md
- 16_exclude_and_slider_strategy.md
- 17_diagnostics_revision_cascade.md
- 20_installation_tests_update_policy.md

GitHub overwrite/add:
- prompt-patterns/create-cover/COVER_2STEP_TRANSFORM_REMASTER_PROTOCOL.md
- prompt-patterns/create-cover/COVER_VOCAL_STEREO_OLDNESS_REPAIR.md
- tests/acceptance/AT-20260613-MILK-COLA-FULL-PROCESS-COVER.md
- cases/failure/C-20260613-MILK-COLA-COVER-QUALITY-MONO-OLDNESS.md
- docs/research/SESSION_MILK_COLA_FAILURE_SYNTHESIS_20260613.md
- project-sync/PATCH_MANIFEST_20260613_COMPLETION_COVER_QUALITY.md

## Operating rule
A lyric pass is not a song pass. Final 8 fields ship only after lyric, CREATE, COVER, EXCLUDE, sliders, and counts pass S10.
