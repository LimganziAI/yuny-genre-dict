# C-20260613 — Milk/Cola COVER Quality, Mono Vocal, Oldness

## Type
Failure case → system patch.

## Summary
The Korean lyric direction succeeded enough for user to keep nearly all lines, but final package execution failed around process completion and COVER quality. Reported problems: invalid sliders, weak CREATE/COVER role separation, COVER sounding dated, poor fidelity, mono/buried vocal, weak shouts/gang chorus, weak cue rendering.

## Root causes
1. S10 shipped before all cross-field gates were complete.
2. COVER attempted transform + finish + stereo repair in one dense prompt.
3. Quality stack existed but was not operationally prioritized enough.
4. Actual failed render classes were not fully moved into EXCLUDE.
5. Audio Influence was raised for preserve, possibly preserving unwanted source skin.

## Patch decisions
- Add Completion-first law to Project Instructions.
- Add explicit COVER quality law and lyric-lock repair route.
- Patch cards 03/04/08/14/15/16/17/20.
- Add 2-step COVER transform/remaster protocol.
- Add vocal stereo + oldness repair pattern.
- Add acceptance test.

## Operator rule
A lyric pass is not a record pass. After a strong lyric, continue producer/prompt/COVER/quality checks with equal seriousness.
