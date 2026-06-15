# AT-04 — "장르는 바꾸되 멜로디는 살려" → Preserve/Substitution + AI 60-75

## Input
"이 곡 장르는 [target]으로 바꾸되 멜로디는 살려줘." (existing CREATE result assumed)

## Pass criteria
1. COVER SLIDERS: Audio Influence in 60-75 band, value justified by transform intensity (mode b genre-change).
2. COVER PROMPT contains EXPLICIT preserve map: melody contour, vocal topline, hook shape, key/tempo feel, section structure — named as preserved.
3. COVER PROMPT contains EXPLICIT substitution map: which instruments/textures/grooves are swapped for target-genre equivalents (e.g., acoustic kit → 909 + sidechain pad), in target-genre micro-anchor language.
4. Order follows genre-transform sequence: micro-anchor → preserve map → substitution map → vocal identity → section/energy events → quality stack → outro preservation.
5. ~30% overlap rule respected: COVER doesn't restate the full CREATE bone.

## Fail routing
AI <55 or >80 without reasoning → card 16 · preserve map implicit/missing → card 14 · macro genre as anchor → card 09.
