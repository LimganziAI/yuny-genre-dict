# Research Synthesis — AI Songwriting Workflow for YUNY Rebuild

## date
2026-06-12

## purpose
Convert external AI-songwriting workflow research into a practical YUNY runtime correction.

The user problem is not lack of materials. The problem is that the current runtime uses materials as rigid constraints instead of producer-level judgment inputs.

## sources consulted
- CoLyricist: workflow-aligned AI lyric support; key stages include Theme Setting, Ideation, Drafting Lyrics, Melody Fitting.
- Youling: AI-assisted lyrics creation with interactive generation, candidate selection, and revision modules instead of one-shot full text only.
- Amuse: human-AI collaborative songwriting with multimodal inspirations, turning images/text/audio into coherent musical suggestions while preserving songwriter agency.
- Lyric setting / prosody principle: lyrics must preserve natural language shape while aligning with rhythm and melody.
- Suno/Udio prompt analysis literature: AI music platforms are used through prompts, tags, and lyrics, but prompting strategies need musicological interpretation rather than tag dumping.

## applied lesson
YUNY should not start from output format.

Do not start with:

```text
8 fields → lyric sections → cue count → character count
```

Start with:

```text
Theme/record goal → ideation/reference function → macro song design → lyric drafting → melody/prosody fitting → Suno execution fields
```

## Producer-first runtime mapping

### 1. Theme / Record Goal
Resolve the song's reason to exist.

Output internally:
- song thesis
- emotional promise
- genre lane
- listener landing point

### 2. Ideation / Reference Function
Use references and user materials as function evidence.

Extract:
- lyric density
- section pressure
- hook role
- vocal posture
- arrangement movement
- repetition dose
- language fragmentation tolerance

Never copy reference lines.

### 3. Macro Song Design
Build the whole-song arc before lyric lines.

Define:
- opening image or action
- V1 observation
- pre pressure
- chorus memory object
- V2 disclosure
- bridge rupture/reversal
- final chorus shift
- outro residue

### 4. Lyric Drafting
Draft according to lyric mode by section.

Modes:
- sentence-driven narrative
- phonetic hook / dance
- hybrid pop
- chant/post-hook
- formal meter
- minimal image lyric

### 5. Melody / Prosody Fitting
Do not trim Korean grammar blindly.

Fit by:
- natural speech accent
- vowel landing
- open ending placement
- breath group
- section energy
- meaning stress

### 6. Revision / Candidate Repair
The model must surface weak lines before the user catches them.

For Korean narrative lyrics:
- worst 3 line-pairs
- prose rewrite
- lyric rewrite
- pass/fail

For hook-driven lyrics:
- phonetic cell test
- repeat fatigue test
- meaning load test

### 7. Suno Execution
Only after the song survives the producer/lyric/prosody layers, produce the 8 fields.

The fields are delivery, not the creative process.

## Runtime correction
YUNY must use a dynamic process:

```text
producer judgment first
select mode
select only relevant gates
repair highest broken layer
then package
```

Do not use every rule for every song.

## Immediate patch target
Promote this synthesis into:
- builder-runtime/instructions/current/00_INSTRUCTIONS_FULL_REPLACE_UNDER_8000.txt
- builder-runtime/knowledge/current/05_lyric_dossier_and_5000_script_engine.md
- builder-runtime/knowledge/current/06_korean_lyric_prosody_hook.md
- possibly card 11/12 for arrangement and topline connection

## Acceptance requirement
Before release ZIP, run four tests:
1. Korean sentence-driven narrative lyric
2. Korean phonetic/dance hook lyric
3. Korean hybrid verse+hook lyric
4. user-provided lyric repair case

## status
Research synthesis recorded. Runtime patch still required.
