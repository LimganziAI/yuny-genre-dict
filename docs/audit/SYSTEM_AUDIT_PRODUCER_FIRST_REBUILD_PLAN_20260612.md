# SYSTEM AUDIT — Producer-First Rebuild Plan

## date
2026-06-12

## audit trigger
User critique after repeated Korean lyric failures. The system produced formal-looking Suno 8-field packages while failing basic Korean lyric sense, macro song flow, and producer-level judgment.

## diagnosis
The current system has too many downstream controls and too weak an upstream producer decision layer.

Existing materials already cover:
- routing
- staged lyric process
- cue rules
- CREATE/COVER fields
- exclude/sliders
- production quality stack
- Korean lyric prosody
- reference assimilation

But the runtime has been using these as if the job were to satisfy a checklist.

The actual job is:

```text
music production planning → lyric/composition/arrangement judgment → Suno execution package
```

The eight fields are delivery format, not the creative process itself.

## core failure
The model behaved like a compliance clerk:

```text
rules → counts → sections → cues → 8 fields → fake PASS
```

It must behave like a record producer / songwriter-director:

```text
song intent → reference function → macro arc → section jobs → lyric mode → draft → targeted repair → 8-axis Suno execution
```

## why the user should not be doing this work
The user may provide references, taste, examples, and rejection signals. The system must infer:
- what kind of song is being made
- where the listener should land emotionally
- which sections carry information
- which sections carry sound/hook
- what lyric mode each section needs
- which rules are relevant
- which rules would harm the song

The user should not be the first Korean sentence sanity filter.

## required architecture

### Layer 0 — Producer Intake
Resolve:
- record goal
- reference function
- target listener experience
- language/register
- genre lane
- vocal identity
- production world
- delivery format

### Layer 1 — Song Thesis
Create one sentence:

```text
This record works because ______.
```

No lyric drafting until this is clear.

### Layer 2 — Macro Arc
Define:
- Opening: listener landing
- Verse 1: observable situation
- Pre: pressure rise
- Chorus: memorable sentence/sound
- Verse 2: new information
- Bridge: defense break or reversal
- Final: meaning shift from first chorus
- Outro: residue

### Layer 3 — Section Jobs
For each section, decide:
- story function
- energy function
- lyric mode
- melody/topline function
- arrangement role

### Layer 4 — Lyric Mode Routing
Modes:
- narrative prose lyric
- phonetic hook / dance lyric
- hybrid pop lyric
- chant/post hook
- formal meter
- minimal image lyric

Do not apply one mode to all sections unless the song demands it.

### Layer 5 — Targeted Gates
Only use gates that fit the chosen song and section.

Examples:
- narrative verse: Korean prose sanity, adjacent-line handoff
- dance hook: phonetic hook cell sanity
- hybrid chorus: hook repeat dose, vowel landing
- final chorus: meaning shift
- cover prompt: preserve/substitute map

### Layer 6 — Suno Execution
Only after the song survives musically and lyrically:
- CREATE PROMPT
- LYRIC
- EXCLUDE
- SLIDERS
- COVER CREATE PROMPT
- COVER LYRIC
- COVER EXCLUDE
- COVER SLIDERS

## anti-patterns to remove
- uniform character-count trimming across all lyric modes
- PASS tables that do not quote and repair the worst lines
- object-bank line stuffing
- cue rules freezing broken lyrics
- treating 8-field output as proof of quality
- applying every available rule to every song
- making the user debug basic Korean sentence validity

## new acceptance tests needed
1. AT-KR-MACRO-ARC-SECTION-MODE
2. AT-KR-PHONETIC-HOOK-CELL-SANITY
3. AT-KR-HYBRID-SECTION-ROUTING
4. AT-SUNO-8FIELD-AS-DELIVERY-NOT-PROCESS
5. AT-REFERENCE-FUNCTION-ASSIMILATION

## patch targets
Builder runtime:
- instructions/current/00_INSTRUCTIONS_FULL_REPLACE_UNDER_8000.txt
- knowledge/current/05_lyric_dossier_and_5000_script_engine.md
- knowledge/current/06_korean_lyric_prosody_hook.md
- possibly 11_pd_arrangement_orchestration.md
- possibly 12_rhythm_harmony_melody_topline.md

Repo design/tests:
- docs/design/KR_LYRIC_MODE_ROUTING_AND_LENGTH_PRIORITY_20260612.md
- docs/design/KR_SONG_DIRECTOR_MACRO_ARC_RUNTIME_20260612.md
- tests/acceptance/AT-KR-PLAIN-SENTENCE-SANITY.md
- cases/failure/C-20260612-KR-BUS-SEARCH-LYRIC-GATE-FAIL.md

## release rule
Do not ship another Builder package until this plan is promoted into runtime and tested with at least:
- one narrative Korean lyric
- one phonetic/dance Korean hook
- one hybrid K-pop structure
- one user-provided lyric repair case

## status
Audit created. Awaiting runtime promotion patch.
