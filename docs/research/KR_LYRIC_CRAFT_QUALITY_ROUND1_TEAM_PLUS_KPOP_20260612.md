# KR Lyric Craft Quality Round 1 — Team Corpus plus K-pop Corpus

## date
2026-06-12

## source material
- User team video title/description corpus: `videos_titles_lyrics.csv`
- K-pop lyric dataset zip: `Kpop-lyric-datasets-main.zip`
- K-pop analytics zip: `kpop-lyrics-analytics-main.zip`

Do not paste full lyrics from either corpus into public runtime docs. Use derived craft rules, reverse briefs, and acceptance tests.

## quantitative snapshot

### Team corpus
- total rows: 453
- Korean rows detected: 326
- median Korean line count: 45
- mean Korean line count: 45.6
- median Korean lyric/description length: 847 characters
- median average line length: 17.5 characters
- median repeat ratio: 0.103

### K-pop analytics corpus
- lyric rows read: 4458
- Korean-ish lyric rows: 4381
- all-era median line count: 37
- all-era median average line length: 12.4 characters
- all-era median repeat ratio: 0.300
- 2010+ median line count: 53
- 2010+ median average line length: 13.0 characters
- 2010+ median repeat ratio: 0.297

## interpretation
The team corpus is not simply weaker K-pop imitation. It has its own bias:

- longer average lyric lines
- lower repeat ratio
- stronger situation and character setup
- more spoken/scene-based writing
- hooks often work as character identity or situational refrain, not only phonetic repetition

Therefore the YUNY minimum bar should use the team corpus as the first baseline and K-pop as secondary calibration.

## what to learn from the team corpus

### 1. Situation is the engine
The stronger lyrics can be reverse-inferred into a concrete prompt situation. The song is not a collection of pretty nouns. It has a scene, a body, a social posture, and a small dramatic problem.

Acceptance cue:
A reviewer should be able to infer the situation from the lyric without reading the original user prompt.

### 2. Speaker posture is visible
Good team lyrics often have a speaker who is shy, defensive, childish, sarcastic, competent outside but anxious inside, jealous while pretending not to be, ritualistic, or performative.

Acceptance cue:
The speaker should be describable in one phrase before the second chorus.

### 3. Object bank belongs to behavior
Objects work when they are noticed, handled, avoided, lost, touched, checked, worn, opened, or heard by the speaker. Objects fail when they are inserted as decoration.

Acceptance cue:
Every important object must have an action or attention verb.

### 4. Hooks are identities
In the team corpus, hooks may be:
- a sentence contradiction
- a character slogan
- a repeated sound-cell
- a comic catchphrase
- a central image
- a bodily action

Acceptance cue:
The chorus must be nameable by function, not only by section label.

### 5. V2 must change the angle
The second verse should add a new object, setting, social angle, bodily admission, or cause. It should not simply continue V1 with the same pressure.

Acceptance cue:
A reviewer can say what V2 newly revealed.

### 6. Final shift is often small
The final does not need a huge plot twist. It can shift address, verb, object, harmony, vocal stance, arrangement, or the speaker's defense.

Acceptance cue:
The final repeat must justify itself.

### 7. Creative expression is scene-born
The strongest metaphor grows from the available situation: room, roof, running, orbit, heat, screen, kitchen, shoes, cards, breath, water, game, road, light, door, hand, timing.

Acceptance cue:
Metaphor should be traceable to scene material.

## what to learn from K-pop corpus

### 1. Repetition is a major engine
K-pop uses higher repeat ratios than the team corpus, especially in chorus/post-hook forms.

YUNY use:
Use K-pop repetition logic when the section wants a hook cell, chant, post-chorus, or dance function. Do not impose it on narrative verses.

### 2. Lines are often shorter
K-pop median line length is shorter than the team corpus. This supports hook singability but can damage narrative Korean if copied everywhere.

YUNY use:
Shorten by section function, not globally.

### 3. Mixed-language and vocable hooks are common in modern data
Modern K-pop tolerates English, vocables, and sound-driven fragments. This is useful for hook mode, but not proof that broken Korean narrative lines are acceptable.

YUNY use:
Separate phonetic hook mode from narrative Korean mode.

## YUNY lyric craft bar
Before a Korean lyric is accepted, it must pass these qualitative checks:

1. The situation is inferable.
2. The speaker posture is distinct.
3. Important objects are acted on or noticed.
4. The chorus has a function: confession, contradiction, slogan, sound-cell, action, or image.
5. V2 adds a real angle.
6. The final section shifts something.
7. Metaphor grows from scene material.
8. Korean line-pairs survive as speech when in narrative mode.
9. Hook repetition is intentional when in hook mode.
10. The lyric can be reverse-briefed into a plausible original prompt.

## application rule
For now, optimize Korean lyric craft first. Suno CREATE/COVER quality comes after the lyric and song thesis are viable.

## status
Round 1 analysis complete. Needs simulation logs and runtime promotion into 05/06 after representative tests.
