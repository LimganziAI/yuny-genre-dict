# VALIDATION — all_videos private taste overlay

## Input
- `all_videos.csv`
- Rows: 453
- Date range: 2025-09-06 → 2026-06-10

## Filtering
- Lyric-like rows: 440
- Manual-review / likely non-lyric rows: 13

Heuristic used:
- line count
- short-line ratio
- blank block structure
- metadata/promo penalty
- average line length

## Privacy
- Raw descriptions/lyrics are not included in generated overlay.
- Per-video ledger contains title, URL, tags, stats, and description hash only.
- This should live under `vault/operator-private/`, not Knowledge.

## Files generated
- `vault/operator-private/LYRIC_HISTORY_PRIVATE_PROFILE_FROM_ALL_VIDEOS.md`
- `vault/operator-private/LYRIC_HISTORY_EXPRESSION_LEDGER_FROM_ALL_VIDEOS.csv`
- `vault/operator-private/CHARACTER_TONE_PRIORS_FROM_ALL_VIDEOS.csv`
- `vault/operator-private/ALL_VIDEOS_PRIVATE_ANALYSIS_STATS.json`
- `lyric-craft/OPERATOR_LYRIC_HISTORY_ROUTER.md`
- `tests/acceptance/AT-OPERATOR-LYRIC-HISTORY-PRIVATE-ROUTE-v1.md`

## Key distillation
- Global taste leans toward object-driven emotion, weather/light/body/motion motifs, denial/excuse speech acts, character-first framing, bright surface with hidden pressure.
- Main risks: repeated motifs, abstract carriers, same endings, slogan-like chorus, character lore replacing present scene.

## Compatibility
- v4.2.1 remains the main lyric engine.
- This overlay must not bypass syllable grid, machine verification, infill repair, or Korean lyric sovereignty.
