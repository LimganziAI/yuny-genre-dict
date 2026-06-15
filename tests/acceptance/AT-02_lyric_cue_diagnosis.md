# AT-02 — "가사큐가 부실해" → Diagnosis, NOT New Song

## Input
Prior 8-field output exists in conversation. User: "가사큐가 부실해."

## Pass criteria
1. NO new song. No regenerated 8-field block. (Hard fail if any new CREATE PROMPT appears.)
2. Response diagnoses the LYRIC field specifically: which sections lack cues, which [Singing:] lines are repetitive/over-stuffed (>7 modifiers), where breath/pause/dynamics marks are missing, whether speaker labels and hook emphasis exist.
3. Fix = rewritten LYRIC field ONLY (full field, not fragment), with per-section cue reinforcement: varied [Singing:] per section, breath placement, held notes, energy direction matching section arc.
4. References cue grammar rules (cards 05/08): RENDERS vs MARGINAL distinction respected — fixes use renderable cues (CAPS, vowel stretch, brackets, (BGV)) not wishful ones.
5. Other 7 fields untouched unless the diagnosis explicitly implicates them (then named + justified).

## Fail routing
New song emitted → card 01 mode gate · cues all identical across sections → card 08 · meta-talk without rewritten field → 제0원칙 output-first.
