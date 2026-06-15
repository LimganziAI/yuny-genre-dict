# TEAM VIDEO LYRIC CORPUS BASELINE — 20260612

## source
User-provided `videos_titles_lyrics.csv` containing YouTube video IDs, titles, URLs, published dates, and description text.

Do not paste full lyrics from this corpus into public examples. Use derived craft analysis, reverse briefs, and acceptance criteria.

## corpus snapshot
- total rows: 453
- rows with substantial lyric-like description: 430
- detected Korean rows: 322
- detected English rows: 94
- detected Japanese rows: 35
- unknown/other: 2
- publication range in detected Korean set: 2025-09-06 to 2026-06-06

## Korean lyric statistical baseline
From 322 detected Korean rows:

- average line count: 45.6
- median line count: 45
- average description length: 875.8 characters
- median description length: 845 characters
- average line length: 17.8 characters
- median average-line length: 17.4 characters
- average repeat ratio: 0.108

Interpretation:
- The team's practical lyric length is far below the 5000-character Suno limit.
- The limit is not the creative target.
- Most working lyrics are compact, sectional, and repeat-aware rather than uniformly trimmed.
- Good output should usually land around 35-60 lyric lines unless the song form demands otherwise.

## recurring craft traits

### 1. Situation-first writing
The better team lyrics usually begin from a concrete situation:
- evening alley and smell of grass
- slow morning in bed
- office competence versus domestic anxiety
- rooftop one-step confession
- running pace and mismatched breath
- jealous phone-check monologue
- orbit metaphor for unrequited love

The situation gives the lyric its object bank. Objects are not decorative inventory.

### 2. Character voice over generic poetry
Many songs work because the speaker has a social posture:
- shy but moving
- sarcastic and defensive
- competent outside but clumsy at home
- jealous while pretending not to be
- childish, direct, ritualistic, or performative

YUNY must infer the speaker posture before writing lines.

### 3. Hook as identity, not summary
Good hooks are often one of these:
- sentence hook: a repeatable contradiction or confession
- phonetic hook: short sound-cell with motion
- slogan hook: direct posture phrase
- image hook: one central metaphor repeated with slight change

Do not make the chorus a thesis explanation.

### 4. V2 adds angle
The stronger lyrics do not merely continue V1. V2 adds a new object, changed social angle, deeper cause, or body behavior.

### 5. Final shift is small but real
Final sections often change by stance, target, word, object, or energy rather than rewriting the whole song.

### 6. Metaphor grows from scene
The best metaphors come from available material: route, room, rooftop, running, kitchen, summer heat, orbit, water, cards, shoes, screen, breath. Detached pretty language is weaker.

### 7. Different modes by song
The corpus contains:
- narrative Korean pop/R&B/ballad lyrics
- chant and dance hooks
- character songs
- comedic spoken-monologue lyrics
- short-form teaser lyrics
- English action/parkour-style prompts
- Japanese seasonal pop lyrics

A single universal lyric rule cannot cover this corpus.

## minimum quality bar for YUNY
YUNY output should at least match the user's existing baseline:

1. A concrete situation can be reverse-inferred from the lyric.
2. Speaker posture is clear before the chorus.
3. Chorus has a repeatable identity.
4. V2 adds angle or information.
5. Final chorus or final section shifts something.
6. Korean adjacent line-pairs remain understandable.
7. Metaphor belongs to the scene.
8. The lyric does not sound like a rule-compressed translation.
9. CREATE and COVER prompts support the same song identity.
10. Suno formatting is correct without letting formatting dominate the record.

## reverse-engineering test method
For each team-video lyric:

1. Read title and description.
2. Infer the likely song situation.
3. Infer the speaker posture.
4. Infer genre lane and hook mode.
5. Infer section arc.
6. Draft a compact prompt that could have led to that lyric without copying it.
7. Test whether YUNY can generate a new lyric with comparable structure and emotional clarity.
8. Judge against baseline: situation, posture, hook, V2, final, Korean naturalness, metaphor source, Suno prompt practicality.

## release implication
No Builder replacement should be considered stable until YUNY can pass representative reverse-brief simulations from this corpus.
