# AT-KR-HYBRID-SECTION-ROUTING

## purpose
Check that hybrid Korean pop songs use different lyric and production logic by section.

## trigger
Use when a song combines story verse, rising pre-chorus, hook chorus, post-hook, rhythmic section, or final chorus change.

## required pre-draft map
```text
SONG THESIS:
MACRO ARC:
SECTION MAP:
- V1: job / lyric mode / energy / topline role
- PRE: job / lyric mode / energy / topline role
- CHORUS: job / lyric mode / energy / topline role
- POST: job / lyric mode / energy / topline role
- V2: job / lyric mode / energy / topline role
- BRIDGE: job / lyric mode / energy / topline role
- FINAL: job / lyric mode / energy / topline role
```

## pass criteria
- Verse Korean sentences remain natural.
- Chorus has clear hook identity.
- V2 adds information or changes angle.
- Final chorus changes meaning, defense, energy, or arrangement.
- Repetition dose is intentional by section.
- Cue and production events support the macro arc.
- The listener can state the song movement in one sentence.

## fail criteria
- Every section uses the same lyric logic.
- Verse becomes too compressed for its story job.
- Chorus loses hook identity.
- Bridge repeats without development.
- Final chorus is copied without shift.
- Production energy rises without lyric or emotional reason.
- Correct fields hide a weak song arc.

## required audit table
After plain draft:

| section | intended job | actual job | lyric mode fit | energy fit | decision |
|---|---|---|---|---|---|

## repair rule
Patch the highest broken layer:
1. song thesis
2. macro arc
3. section job
4. lyric mode
5. line language
6. cue or field packaging

## status
Active acceptance test candidate.
