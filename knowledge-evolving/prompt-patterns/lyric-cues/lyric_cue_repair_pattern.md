# Lyric Cue Repair Pattern

Use when the user reports weak 가사큐, singer confusion, cue labels being sung, rushed lyrics, poor duet separation, bad ending, or section collapse.

## First diagnosis

Classify the failure:

- structural tag failure;
- singer label failure;
- duet handoff failure;
- rushed lyric density;
- missing [Singing:] direction;
- over-tagging;
- section length drift;
- outro/end failure;
- language/pronunciation drift.

## Core rules

- Square brackets `[ ]` are for instructions and singer labels.
- Parentheses `( )` are only for audible ad-libs.
- Do not use parentheses for speaker labels.
- Use bar counts for important sections.
- Use one strong [Singing:] cue per section before adding microcues.
- Preserve useful stress marks, [Breath], [Held note], [Pause half bar], [Seamless handoff], [Outro], and [End].

## Speaker labels

Good:

```text
[Female Vocal 1]
[Female Vocal 2]
[Duet]
```

Bad:

```text
(Female Vocal 1)
(Vocal 2)
```

## Section cue skeleton

```text
[Verse 1 8]
[Female Vocal 1]
[Singing: breathy close-mic, relaxed phrasing, intimate lower register]
...

[Pre-Chorus 8]
[Female Vocal 2]
[Singing: building intensity, cadence tightening, brighter tone]
...

[Chorus 16]
[Duet]
[Singing: doubled hook, harmony +3rd entering bar 9, clear handoff]
...

[Bridge 8]
[Female Vocal 1]
[Singing: stripped whisper, slower delivery, breath audible]
...

[Final Chorus 16]
[Duet]
[Singing: full harmony stack, lead remains clear, ad-libs on line ends]
...

[Outro 4]
[Singing: last phrase thins to close-mic]
...
[End]
```

## Density repair

If lyrics rush:

- reduce syllables per line;
- split long lines;
- add [Pause half bar] before hook lines;
- avoid consonant clusters at high BPM;
- use shorter hook thesis;
- keep verse imagery concrete but not overloaded.

## Ending repair

If endings drift or continue randomly:

- add [Outro 4] or [Outro 8];
- repeat the hook fragment intentionally;
- use [Each repeat thinning out] when useful;
- add [Hard stop] or [Sudden Absolute Silence] only when stylistically right;
- end with [End].

## Case note

If the repair clearly works or fails, record a case. The useful lesson is usually about cue density, singer labels, line length, or ending control.
