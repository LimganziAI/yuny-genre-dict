# COVER 2-Step Transform + Remaster Protocol

## Trigger
Use when COVER must both transform genre and repair finish/stereo, or when one COVER render comes out dated, mono, muddy, thin, buried, or weak.

## Rule
Do not force transform, stereo vocal, modern finish, shouts, and instrument substitution into one overloaded paragraph if the previous render failed. Split the logic.

## Step 1 — Genre Transform COVER
Goal: change Skin while protecting Bone.
Prompt order:
1. target microgenre anchor
2. preserve map: melody/topline, Korean lyric timing, section order, vocal identity, final/outro
3. substitution map: drums, bass, guitars/synths, hooks, instrumental break
4. section events
5. minimal quality line
Audio Influence:
- 55-62 if old/source skin followed the prior render
- 62-68 if melody drift risk is high

## Step 2 — Texture Refine / Remaster COVER
Goal: repair Finish without rewriting song.
Prompt order:
1. same genre refine / remaster anchor
2. preserve map: already transformed skin, melody, lyric timing, lead vocal identity
3. vocal corridor + stereo backing field
4. low-end/low-mid/high-mid/air/depth/dynamics stack
5. final/outro preservation
Audio Influence:
- 70-75 if transformed song is right but finish is bad
- 60-68 if finish repair still needs more texture replacement

## Defects
- New-song description instead of preserve/substitute.
- Quality stack only says "high quality".
- Oldness not named in EXCLUDE after oldness feedback.
- Lead vocal and gang shouts both stacked center.
- Audio Influence raised after old skin failure without explanation.
