# AT-TEAM-CORPUS-REVERSE-BRIEF

## purpose
Use the user's existing team video lyrics as a practical minimum quality baseline.

The test asks whether YUNY can reverse-infer the song situation, speaker posture, hook function, and section arc from existing team lyrics, then produce a new Suno-ready direction that could reach comparable craft quality without copying.

## source
User-provided `videos_titles_lyrics.csv`.

Do not quote full lyrics in test reports. Use derived analysis only.

## trigger
Use before Builder replacement release and when Korean lyric quality has regressed.

## scenario selection
Select representative examples from:

1. narrative Korean emotional pop/R&B
2. character-voice Korean lyric
3. hook/dance or chant lyric
4. comedic/spoken monologue lyric
5. metaphor-led Korean lyric
6. hybrid verse-plus-hook song
7. short-form teaser or special-format lyric

## required reverse brief
For each selected item, produce:

```text
TITLE:
LANGUAGE:
LIKELY SONG SITUATION:
SPEAKER POSTURE:
GENRE / ENERGY LANE:
LYRIC MODE BY SECTION:
HOOK FUNCTION:
V2 FUNCTION:
FINAL SHIFT:
OBJECT BANK:
WHAT PROMPT WOULD HAVE CREATED THIS QUALITY:
WHAT YUNY MUST NOT DO:
```

## generation test
After reverse brief, generate a new concept in the same craft lane, not a copy.

Check:
- situation is concrete
- speaker posture is clear
- chorus has identity
- V2 adds angle
- final shifts
- Korean is natural
- imagery grows from scene
- prompt is practical for Suno
- 8-field format is correct when requested

## pass criteria
YUNY passes only if a human can see how the new output belongs to the same craft standard as the team corpus while remaining original.

## fail criteria
- Reverse brief is generic.
- Prompt only lists genre tags.
- Lyric copies surface images from the source.
- Korean line flow regresses.
- Hook is weaker than the source lane.
- Final has no shift.
- CREATE/COVER mismatch the lyric identity.

## status
Active acceptance test candidate. Requires representative simulation logs.
