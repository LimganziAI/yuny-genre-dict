# Patch V3 — Prompt Mining, Technical PD, Korean Lyric Integration

Date: 2026-06-13
Status: active patch candidate
Source materials: files(27) metadata linkage, user preferences, Hibiscus/Tatoo failure case, operator-history interview rounds.

## Goal
Upgrade YUNY runtime so it proactively uses machine-mined prompt materials, v5.5 gold prompt candidates, operator lyric/case memory, and technical Suno prompt engineering instead of drifting into short generic fields.

## User-confirmed preferences
- `MJ style 10%` may be used as groove/ad-lib/funk-pocket seasoning.
- Percentage ratios are useful for hybrid genres and cover transforms when they clarify dominance.
- User generally prefers technical prompting: BPM, key, progression, range, instrument articulation, vocal corridor, stereo/frequency quality language.
- For high-energy songs, technical quality control is welcome and often preferred.

## Runtime changes
1. Use files(27) as a prompt vocabulary mine, not a truth table.
2. Use v5.5 gold prompt candidates as listening targets and prompt-shape examples.
3. Treat machine create/final matches as candidate evidence only; user-confirmed cover workflow can override.
4. When prompts are short/generic, route as PROCESS + CREATE/COVER underbuild and rebuild from current lock.
5. Add percentage and MJ-style handling to genre/reference prompt construction.
6. Add Korean lyric corpus mining: extract method from user lyrics and professional examples, never copy lines.
7. Add PD autonomy: if engineering is missing, propose/fix BPM/key/range/harmony/instrument/quality gaps before final fields.

## Acceptance targets
- CREATE prompt contains bone and technical execution value, not vague genre labels.
- COVER prompt contains preserve/substitute/quality/final record logic.
- EXCLUDE contains actual failure classes only.
- Korean lyric work preserves speaker truth and user-style object logic while improving linecraft.
- Gold examples are promoted only after listening/user confirmation.
