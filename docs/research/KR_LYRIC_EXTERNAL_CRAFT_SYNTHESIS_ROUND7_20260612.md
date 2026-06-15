# KR LYRIC EXTERNAL CRAFT SYNTHESIS ROUND 7 — 20260612

## purpose
Add outside lyric-writing and literary-craft calibration to the Korean lyric runtime.

This material is not used for copying lines or imitating named writers. It becomes judging physics: what to hide, what to say plainly, when to omit the subject, when to make an image carry emotion, and how to avoid fixed AI phrasing.

## sources consulted
- Professional lyric-writing tradition around object writing, lyric form, metaphor, and prosody.
- Lyric setting / prosody materials: natural language rhythm must align with musical rhythm.
- Poetry analysis methods: identify speaker, situation, event, timing, place, and why the speaker speaks before subtle image reading.
- Metaphor theory: tenor, vehicle, and ground; metaphor works by transfer, not decorative naming.
- Current AI poetry evaluation research: LLM poems often follow form and theme but underperform humans in creativity, idiosyncrasy, emotional resonance, imagery, and literary devices.
- Team corpus: primary baseline for Korean lyric feel.
- K-pop lyric corpus: secondary calibration for hook, repetition, section pressure, and phonetic cells.

## distilled craft rules

### 1. Subject economy
Korean songs usually do not need repeated first-person subject markers. The singer is already the speaker.

Use explicit subject only when it changes contrast, blame, distance, or confession.

Fail signals:
- repeated `나는` begins lines without contrast
- subject is used to explain instead of letting action imply speaker
- chorus repeats first-person subject where omission would feel more lyrical

Repair:
- remove subject when verb/action already identifies the speaker
- move subject to a pressure point only
- replace `나는 X다` with object/action residue

### 2. Explanation line audit
Lines like `사실 X가 문제는 아니지` often feel like essay summary unless the speaker's voice is specifically self-argumentative.

Use only when:
- character voice is defensive or sarcastic
- the line is part of spoken self-correction
- surrounding lines are concrete enough to carry it

Otherwise replace with action evidence.

### 3. Metaphor distance control
Metaphor should not reveal the hidden meaning too quickly.

Levels:
- direct: clear statement, good for plain chorus or comic posture
- near: object action implies emotion, best for team-corpus narrative
- far: poetic/symbolic, good only when the mode declares it
- opaque: fails unless surreal/artful mode is locked

For team baseline, default = near metaphor.

### 4. Register ladder
Before writing, choose how close the voice is to speech:

- everyday spoken: rounded, familiar, fewer literary nouns
- lyrical spoken: plain sentence plus one image pressure
- literary image: fewer explanations, stronger object field
- symbolic/poetic: omission and image logic lead
- comic speech: direct, timing-based, catchphrase-friendly
- hip-hop adjacent: verb force, internal rhyme, attitude, but sung-mode guard if needed

Each section may move on the ladder, but the speaker must remain one person.

### 5. Cliche and homage gate
Cliche is not always banned. It can be used when the song wants shared cultural shorthand, parody, comfort, or genre familiarity.

Homage is allowed as method, not surface line borrowing:
- adopt indirect speech mechanism
- adopt small object focus
- adopt sentence rhythm or restraint
- adopt contrast between plain words and emotional implication

Do not copy famous lines, titles, or signature lyric content.

### 6. Moon-brightness lesson
The well-known `moon is beautiful` anecdote is useful as a craft model even when its historical attribution is debated.

Craft lesson:
- love can be expressed by pointing at a shared external object
- indirect speech works when the listener can infer the relation
- the object must be present in the scene and shared by the speaker/listener

YUNY rule:
Do not write `I love you` as a thesis when the scene can make a smaller object say it.

### 7. Team-corpus match
The user's team corpus usually prefers:
- scene-born metaphor
- object-action coupling
- lower repeat than general K-pop
- character posture
- small final shift
- readable Korean with some image pressure

YUNY should not force maximal poetry. It should decide how much plain speech the speaker needs.

## new acceptance checks
Add these before cue pass:

```text
SUBJECT ECONOMY:
- Did repeated first-person subjects earn their place?
- Can the line work better with implied speaker?

EXPLANATION AUDIT:
- Is this line explaining the meaning instead of letting action show it?
- If kept, is it character voice?

METAPHOR DISTANCE:
- direct / near / far / opaque
- Is that distance right for the section mode?

REGISTER LADDER:
- everyday / lyrical-spoken / literary-image / symbolic / comic / hip-hop-adjacent
- Is the section using the right register?

HOMAGE GATE:
- What method is borrowed?
- What surface content is avoided?
```

## revised laundromat diagnosis
Previous sample improved but still had two warning patterns:

1. Explicit self-explanation: `drying is not the problem`-type idea.
2. Overexposed metaphor: `I am the undried one`-type wording.

Better direction:
- let the extra coin, damp sleeve, stopped timer, unopened message, and warm fingertips carry the unfinished feeling
- avoid naming the metaphor too directly
- remove repeated first-person subjects unless a contrast needs them

## status
Round 7 synthesis complete. Promote subject economy, explanation audit, metaphor distance, register ladder, and homage gate into cards 05/06/20.
