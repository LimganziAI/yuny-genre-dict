# AT-03 — "커버했더니 보컬이 묻혀" → Production-Aware Fix

## Input
COVER result feedback: "커버했더니 보컬이 묻혀."

## Pass criteria
1. Classified as production-aware failure (feedback.schema.md symptom_class: vocal-buried, layer: COVER-PROMPT/EXCLUDE/SLIDERS) — not lyric, not genre.
2. Fix touches the vocal-rescue set: vocal corridor 500Hz-3kHz protection, de-ess 5-8kHz, 200-400Hz mud carve, instrument L/R placement away from center vocal, vocal bus forward/warmth language.
3. Audio Influence re-set with reasoning (e.g., lower AI if source mix is fighting the new vocal treatment, or raise if vocal identity is being lost to transformation).
4. EXCLUDE checked for keyword-guard trap: words like "muddy/compressed" that can suppress vocal processing → replaced with positive Hz-language in COVER PROMPT instead.
5. Output = rewritten COVER PROMPT + COVER EXCLUDE + COVER SLIDERS (full fields). CREATE side untouched.

## Fail routing
Generic "make vocal louder" without stack terms → card 15 · AI left unchanged without justification → card 16 · blames Suno randomness without 2-regen evidence → card 17.
