# AT-01 — Korean K-R&B Request → Full 8-Field Output

## Input (fixture FX-001)
"새벽 감성 K-R&B 한 곡. 보컬은 담백한데 후렴에서만 살짝 터지는 느낌. 가사는 이별 직후."

## Pass criteria
1. Output is EXACTLY 8 code-fenced fields in order: CREATE PROMPT / LYRIC / EXCLUDE / SLIDERS / COVER PROMPT / LYRIC / EXCLUDE / SLIDERS. No 9th block, no song content outside fences.
2. CREATE PROMPT = bone: microgenre (NOT "R&B" macro) + era/scene in first ~80 chars; BPM/feel; tonal color; vocal identity 5 elements; melody contour; hook shape; section arc; 3-4 core instruments; signature motif. 700-950 chars, measured count shown.
3. LYRIC field = performance script: section tags w/ bar counts, full Korean lyric, per-section [Singing:] cues (varied, ≤7 modifiers), breath/pause marks, hook emphasis, bridge turn, final-chorus evolution, [End]. Dossier compliance: no banned clichés, no abstract emotion words, 받침/vowel checked against BPM.
4. COVER PROMPT contains: micro-anchor, preserve map, substitution map, vocal identity preservation, section/energy events, full quality stack, outro preservation.
5. COVER SLIDERS include Audio Influence with a value (never "—").
6. Request nuances survive: "담백→후렴만 터짐" appears as dynamics direction in vocal identity + [Singing:] cues; "이별 직후" drives dossier scene/object bank.

## Fail routing
Missing cue script → card 05/08 · macro genre at Position 1 → card 04/09 · AI missing → card 16 · 9+ blocks → card 01.
