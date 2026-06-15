# KR Lyric Mode Routing and Length Priority

## Problem
A Korean lyric failure showed that the system used one compression rule across different lyric types. This damages narrative Korean lyrics because natural sentence flow gets cut before meaning is secure.

The defect is mode confusion.

- Narrative lyrics need sentence logic, scene continuity, and speaker truth first.
- Phonetic dance hooks may prioritize vowel shape, repetition, and rhythmic cells.
- Hybrid pop lyrics often need prose-like verses and sound-first choruses.
- Formal meter should only be strict when the user or genre explicitly demands it.

## Core doctrine
Length is a result, not a target.

For Korean lyrics, line length or syllable count must not outrank:

1. Korean sentence validity
2. speaker truth
3. adjacent-line handoff
4. scene comprehension
5. genre-specific lyric mode
6. breath and singability
7. hook memorability
8. field limit compliance

Field limits are packaging constraints. They are not lyric-writing goals.

## Mode A: sentence-driven narrative lyric
Use for indie R&B, ballad, folk, singer-songwriter, story-driven city pop, emotional verse-heavy pop.

Priority:
- natural Korean first
- prose continuity before compression
- adjacent two-line pairs must survive as plain Korean prose
- particles, endings, and connective tissue may stay when they carry meaning
- line length may vary by section
- hook may be a complete sentence split across lines

Hard rule:
Do not cut Korean particles, endings, or connectors just to shorten the line when the cut damages meaning.

## Mode B: phonetic hook / dance lyric
Use for dance pop, performance chorus, chant refrain, rhythm-first earworm sections.

Priority:
- vowel landing
- consonant bounce
- repeat cell
- rhythmic latch
- singable fragments

Hard rule:
Fragments are allowed only when they are intentional musical cells, not broken narrative prose.

## Mode C: hybrid pop narrative plus hook cell
Use when verse and pre-chorus need story, but chorus or post-chorus needs sound-first repetition.

Priority:
- verse and pre-chorus: Mode A
- chorus and post-chorus: Mode B
- bridge and final: meaning shift returns

Hard rule:
Do not apply chorus compression rules to verses. Do not apply verse prose rules to chant hooks.

## Mode D: formal or metrical lyric
Use for deliberate fixed-meter writing, retro formalism, trot meter, or a user-declared pattern.

Priority:
- declared meter
- recurring rhythmic cell
- Korean naturalness inside the form

Hard rule:
Strict count only applies when the form is explicitly declared.

## Compression policy
- Compress after meaning survives, not before.
- For Mode A, remove redundant repeats, cue clutter, or extra sections before cutting Korean grammar.
- For Mode B, grammar may be lighter if the hook cell becomes stronger.
- For Mode C, apply the correct compression logic by section.
- For Mode D, count can be stricter, but sentence sanity still matters.

## Mandatory pre-write decision
Before Korean lyric drafting, determine:

```text
LYRIC MODE: A/B/C/D
WHY: genre + user goal + section function
COMPRESSION POLICY: prose-first / hook-cell-first / hybrid / formal-meter
LINE FLEX: high / medium / low
```

## Acceptance rule
If Mode A is selected, KR PLAIN SENTENCE SANITY must pass before cue pass or eight-field packaging.

If Mode B is selected, PHONETIC HOOK CELL SANITY must pass:
- clear vowel or consonant identity
- singable rhythm cell
- intentional fragments
- appropriate meaning load for the section

If Mode C is selected, both tests apply by section.

## Patch targets
- 05_lyric_dossier_and_5000_script_engine.md
- 06_korean_lyric_prosody_hook.md
- tests/acceptance/AT-KR-PLAIN-SENTENCE-SANITY.md
- future test: AT-KR-PHONETIC-HOOK-CELL-SANITY.md

## Status
Design doctrine added after user critique. Needs promotion into 05/06 Builder runtime before release.
