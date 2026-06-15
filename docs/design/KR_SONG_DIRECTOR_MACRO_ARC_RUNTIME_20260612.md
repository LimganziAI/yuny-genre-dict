# KR Song Director Macro Arc Runtime

## Why this exists
A Korean lyric failure exposed a deeper system problem: the runtime over-managed local rules while failing the director-level job.

The user should not have to inspect every unnatural line, mode mismatch, and story break. The system must act as music director first, not checklist clerk.

## Core correction
Do not try to run every possible lyric rule on every song.

Before lyric drafting, make one director decision:

```text
WHAT KIND OF SONG IS THIS?
```

Then choose only the constraints that serve that song.

## Director hierarchy
Every Korean song request must follow this priority order:

1. song identity
2. listener experience
3. genre and reference function
4. macro energy arc
5. section function
6. lyric mode by section
7. speaker truth and Korean naturalness
8. hook design
9. breath and singability
10. field packaging

Local line-count, syllable trimming, cue count, and formal tables must never outrank the song identity.

## Macro arc before line craft
Before writing lyrics, build an internal macro arc:

```text
OPENING: where the listener lands
V1: what is observable
PRE: what pressure rises
CHORUS: what sentence or sound becomes memorable
V2: what new information changes the listener's understanding
BRIDGE: what defense breaks or flips
FINAL: what changes from the first chorus
OUTRO: what image, action, or sound remains
```

If this arc is weak, do not solve it by adding lyric devices. Fix the arc first.

## Section-specific lyric mode
Do not use one lyric mode for the whole song unless the song actually wants it.

A single song may contain:

- narrative verse
- pressure-building pre-chorus
- phonetic chorus
- chant post-chorus
- confession bridge
- widened final chorus

Each section receives its own mode:

```text
SECTION MODE: narrative / phonetic hook / hybrid / chant / formal / minimal image
```

## Reference assimilation
References are not decoration.

When the user provides songs, YouTube lyrics, or previous work, the system must infer:

- what kind of lyric density the user is aiming for
- whether the song is story-led or hook-led
- how much grammar can be fragmented
- where repetition is musical, not lazy
- how verses carry information
- how the chorus simplifies or explodes
- how the final chorus changes

Do not copy lines. Extract function.

## Anti-checklist rule
A checklist is allowed only after a director choice is made.

Bad order:

```text
rules → counts → sections → lyrics → fake PASS
```

Correct order:

```text
song judgment → macro arc → section modes → draft → targeted checks → repair
```

## Minimal sufficient process
Use the smallest process that protects the song.

- For narrative songs: use prose sanity and adjacent-line handoff.
- For dance hooks: use phonetic hook cell sanity.
- For hybrid pop: use section-specific tests.
- For formal meter: use count and meter checks.
- For user-provided locked lyrics: do not rewrite content unless approved.

## Energy arc doctrine
Energy is not only loudness.

Track:

- lyric information pressure
- melodic height
- rhythm density
- vocal openness
- instrumental entry and subtraction
- repetition dose
- listener comprehension load

A song can rise by revealing information, not only by adding bigger production.

## Repair rule
When a Korean lyric complaint says the lyric feels wrong, do not produce a fresh full package first.

First diagnose:

1. macro arc failure
2. lyric mode mismatch
3. sentence naturalness failure
4. hook function failure
5. section role failure
6. cue/packaging over-control

Then repair the highest broken layer.

## Trust rule
The user should not be asked to be the first Korean sentence sanity filter.

The system must identify its own worst lines before presenting a lyric as passed.

## Patch targets
- 05_lyric_dossier_and_5000_script_engine.md
- 06_korean_lyric_prosody_hook.md
- 11_pd_arrangement_orchestration.md
- 12_rhythm_harmony_melody_topline.md
- tests/acceptance/AT-KR-PLAIN-SENTENCE-SANITY.md
- future: AT-KR-MACRO-ARC-SECTION-MODE.md

## Status
Design doctrine added after user critique. Needs promotion into Builder runtime before release.
