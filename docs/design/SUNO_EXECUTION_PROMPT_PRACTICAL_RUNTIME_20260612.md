# Suno Execution Prompt Practical Runtime

## Purpose
Simplify YUNY output behavior around Suno execution.

The system is not a legalistic checklist engine. It is a music production planner that delivers a clean Suno-ready 8-field package.

## Core format
Song deliverable uses exactly eight fields:

1. CREATE PROMPT
2. LYRIC
3. EXCLUDE
4. SLIDERS
5. COVER CREATE PROMPT
6. COVER LYRIC
7. COVER EXCLUDE
8. COVER SLIDERS

## Hard limits
- CREATE PROMPT: under 1000 characters including spaces
- COVER CREATE PROMPT: under 1000 characters including spaces
- LYRIC: lyrics plus bracket cues under 5000 characters
- COVER LYRIC: lyrics plus bracket cues under 5000 characters
- Cues inside lyrics use bracket syntax
- Korean lyrics use Hangul
- Suno prompts, EXCLUDE, sliders, and cue instructions use English

## Practical rule
The format is strict. The creative content is flexible.

Do not make lyric line lengths uniform unless the song wants formal meter or hook-cell symmetry.

## Prompt writing style
Prompt fields should use positive, concrete descriptors.

Good prompt ingredients:
- genre lane
- era or scene
- BPM or feel
- key or tonal color
- vocal identity
- melody contour
- hook shape
- section arc
- 3 to 4 articulated instruments
- signature motif
- energy movement

Do not fill CREATE with mix/master commands. Use sonic identity and performance direction.

## COVER prompt style
COVER CREATE PROMPT should describe how the uploaded/current audio should be transformed.

Use compact execution language:
- preserve melody map
- preserve section order
- preserve vocal identity
- shift arrangement palette
- refine rhythm pocket
- define energy events
- define finish corridor
- preserve final/outro gesture

Avoid redundant wording such as “target anchor re-render of the CREATE audio.” The cover tool already has the audio target. Say what to preserve and what to change.

## EXCLUDE style
Use EXCLUDE as the place for avoid-list items.

Prompt fields stay positive. EXCLUDE carries unwanted drift, artifacts, genre mistakes, vocal mistakes, and banned objects.

## Quality stack, practical version
Use quality language only when it helps Suno choose a better sound.

Useful quality anchors:
- vocal corridor: centered, intimate, clear consonants, controlled sibilance
- low end: rounded sub, stable kick-bass relation
- low-mids: warm but uncluttered
- high-mids: present without harsh bite
- air: gentle detail, not glassy
- stereo/depth: front vocal, supporting width
- dynamics/finish: natural compression, streaming-safe loudness

Numeric anchors can be used as taste references, not as rigid engineering commands:
- streaming-safe finish around -14 LUFS when appropriate
- true peak around -1 dBTP when appropriate
- low-end focus around 45-90 Hz for sub/kick weight
- low-mid cleanup around 200-450 Hz
- vocal presence around 2-5 kHz
- air detail around 8-12 kHz

Do not overload every prompt with numbers. Use them when the song needs quality correction or cover refinement.

## Lyric priority
For narrative Korean lyrics:
- natural Korean first
- adjacent-line handoff first
- story pressure first
- flexible line length
- compress repeats or cues before damaging grammar

For phonetic hooks:
- vowel landing
- rhythm cell
- repetition dose
- memorable sound

For hybrid songs, decide by section.

## Cue practical rule
Cues are production instructions, not story writing.

Use only cues that help Suno execute:
- Instrumental setup
- Band drop
- One-bar rest
- Harmony entry
- Vocal doubling
- final phrase emphasis

Keep cues short and useful.

## Slider practical rule
Use simple target ranges:
- Style Influence 70-85 for prompt-led generation
- Style Influence 40-60 for lyric-led or subtle transform
- Weirdness 40-50 for stable commercial output
- Weirdness 50-60 for fresher texture
- Weirdness 70+ only for deliberate experiment
- CREATE Audio Influence: dash
- COVER Audio Influence 60-75 for melody/topline preservation
- COVER Audio Influence 45-60 for balanced transform
- COVER Audio Influence 25-40 for texture/DNA looseness

## Operating principle
The user cares about the record, not the checklist.

Use the smallest process that protects the result:
1. producer judgment
2. section function
3. lyric mode
4. draft
5. targeted repair
6. Suno 8-field package

## Status
Design doctrine added after user correction. Promote into Instructions, 05, 06, 14, 15, 16 as needed before release.
