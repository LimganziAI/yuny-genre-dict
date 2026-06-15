# Prompt Pattern — Suno Prompt Density and COVER Final Record

Date: 2026-06-13
Source case: Hibiscus / Tatoo concept-relock session
Status: pattern-candidate, high priority after one severe cross-layer case

## Trigger

Use when:
- user says the prompt/COVER feels lazy, short, generic, or underbuilt
- a concept has changed after listening feedback
- lyrics are mostly fixed but sound/vocal/prompt must be rebuilt
- COVER quality, vocal identity, or source-skin drift is the real failure
- user asks to use current Suno prompt practice with 1000-char prompt budget

## Problem

The assistant often emits a short field package too early. It summarizes the meeting instead of designing executable Suno fields. It also copies discarded discussion terms into EXCLUDE.

## CREATE density checklist

A serious CREATE prompt should spend budget on useful execution, not filler:

1. microgenre + scene + era/finish
2. BPM / feel / meter
3. key or tonal color
4. vocal range anchor: soprano, mezzo-soprano, alto, tenor, etc. when helpful
5. vocal natural-language acting: how it feels in the room
6. melody contour: narrow verse, lift, hook shape, peak behavior
7. 3-4 instruments with articulation and register
8. signature motif
9. section movement / energy arc
10. mix corridor if important

## COVER density checklist

A serious COVER prompt is the final record. It needs:

1. target function: refine/remaster or transform
2. preserve map: melody, lyric timing, section order, rests, final/outro gesture, vocal identity
3. do-not-change map when needed
4. substitution/refine map: drums, bass, harmonic bed, texture, vocal treatment, bridge/final event
5. vocal identity protection with range anchor and acting
6. timing/rest protection for quoted lines or cue events
7. full quality stack: vocal corridor, low end, low-mids, high-mids/air, stereo/depth, dynamics/finish
8. final/outro preservation

## Vocal range anchor practice

Use range labels when they stabilize the render:

- light lyric soprano: clearer high center, bright youth, less chest weight
- mezzo-soprano: balanced female pop center, stable lyric singing
- alto / low mezzo: darker, lower, heavier; risky if melody must not drop

Do not let range anchor rewrite melody. Pair it with melody lock when needed:
`preserve topline contour and chorus lift; change vocal color only.`

## Natural-language acting

Use natural language alongside technical descriptors:

- sings as if keeping the room quiet
- tossed aside, still pitched
- low-effort but centered
- cool deadpan, not emotionally inflated
- smiles without brightening the tone
- holds back the line instead of pushing it

## Cue pass

After lyric survives, add renderable cues between lines. Cues must command, not describe:

- [One-beat rest]
- [Two-beat rest: piano only]
- [Band softens]
- [Drums cut]
- [Harmony enters only on final phrase]
- [Instrumental Outro: motif fades]

Every serious narrative lyric should have breath architecture. Long blocks without a rest device cause lyric spill.

## EXCLUDE rule

EXCLUDE lists actual failure classes, not every discarded idea from the meeting.

Good EXCLUDE targets:
- wrong delivery: talk-singing, flat narration, rushed vocal
- vocal defects: buried lead, harsh sibilance, whisper-only vocal, robotic autotune
- mix defects: muddy low-mids, harsh cymbal fizz, mono collapse
- source-skin drag when actually relevant
- wrong-gender lead only if gender drift is likely or observed

Bad EXCLUDE targets:
- a genre mentioned in early brainstorming but abandoned
- obvious absences with no failure risk
- generic long negative spam that steals attention from real failures

## S10 gate

Before final fields:
- prompts under 1000 chars each
- lyric plus cues under 5000 chars
- CREATE Audio Influence is `—`
- COVER Audio Influence numeric
- fields match current concept, not old meeting history
- COVER is as engineered as CREATE
