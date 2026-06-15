# YUNY Suno OS — Update Workflow

## 1. Operating loop

```text
request
→ classify route
→ use stable GPT knowledge
→ fetch GitHub only when needed
→ produce output or diagnosis
→ receive feedback
→ record case if useful
→ promote repeated patterns
→ patch knowledge or runtime guide only when justified
```

## 2. Update types

### 2.1 Case update
Use for one concrete result.

Examples:
- A COVER prompt fixed buried vocals.
- A lyric cue caused singer labels to be sung aloud.
- A genre-transform failed because the preserve map was weak.
- A Korean lyric worked because the hook syllable density matched the BPM.

Location:

```text
cases/success/
cases/failure/
cases/neutral-observations/
```

### 2.2 Pattern update
Use when similar cases repeat.

Examples:
- Tech Para works better when built from Eurobeat + Hyper Techno + ParaPara motion cues.
- Duet separation improves when every section repeats speaker labels and uses [Seamless handoff].
- COVER quality improves when vocal corridor and substitution map appear before detailed mix polish.

Location:

```text
knowledge-evolving/prompt-patterns/
knowledge-evolving/reference-dna/
knowledge-evolving/genre-dictionary/
```

### 2.3 Knowledge patch
Use when a repeated pattern should become part of stable craft knowledge.

Location:

```text
knowledge-static/current-20/patches/
```

### 2.4 Runtime guide patch
Use only when a rule changes the whole GPT workflow.

Location:

```text
instructions/
```

## 3. Case recording trigger

Record or propose a case when:

- the user explicitly says the result worked or failed;
- a repeated failure is diagnosed;
- a new genre or artist DNA is used successfully;
- a new prompt pattern appears reusable;
- a lyric cue, exclude, or slider setting clearly affects the result;
- a production/engineering fix produces a useful lesson.

Do not record every ordinary output. Record lessons.

## 4. Case naming

Use readable filenames:

```text
YYYY-MM-DD_short-topic_success.md
YYYY-MM-DD_short-topic_failure.md
YYYY-MM-DD_short-topic_observation.md
```

Examples:

```text
2026-06-09_duet-labels-read-aloud_failure.md
2026-06-09_tech-para-eurobeat-hypertechno_pattern.md
2026-06-09_cover-vocal-corridor_success.md
```

## 5. Promotion review

A case can be promoted when it answers yes to at least two:

- Did the same issue appear more than once?
- Does the fix apply across genres?
- Does it improve output predictability?
- Does it prevent a costly Suno failure?
- Does it clarify CREATE vs COVER responsibility?
- Does it improve lyric cue rendering or final audio polish?

## 6. Changelog

Major updates should be noted in:

```text
changelog/CHANGELOG.md
```

Each entry should say:

```text
Date
Changed files
Why it changed
What behavior should improve
```
