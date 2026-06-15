# 12. PROMPT TEMPLATES — Copy-Paste Skeletons & Diagnostic Trees
# Version: 2.0 — YUNY Edition (Natural-Language Direction Integrated)
# Last Updated: 2026-05-06
# Engine Target: Suno v5 / v5.5
# Load Trigger: Whenever a prompt is being generated, when the operator
#               requests a quick template, or when iteration/diagnostics
#               are needed.
# Companion Files: 09_SUNO_ENGINE.md, 10_SUNO_LYRICS_TAGS.md,
#                  06_VOCAL_PRODUCTION.md, 11_PRODUCTION_DESIGN.md,
#                  13_REFERENCE_ANALYSIS.md, 14_PROSODY_AND_PHONETICS.md,
#                  15_NATURAL_LANGUAGE_DIRECTION.md,
#                  99_PERSONAL_OPTIONAL.md (§7 verified tips)

---

## SECTION 0. PURPOSE & v2.0 PHILOSOPHY SHIFT

This file is the operational toolkit. Every other file teaches principle;
this file delivers ready-to-deploy templates.

### v2.0 vs v1.x — The Core Shift

**v1.x approach (deprecated):**
Style Box = comma-separated descriptor list (400-600 chars typical)
Result = average-of-genre output, signature moments lost

**v2.6 approach (current):**
Style Box = natural-language scene paragraph, **Dense 700-950 (기본) /
Tight 250-350 (sketch·다양성 우선)** — CREATE/COVER 동일 분량 프레임:
- CREATE: Dense 700-950 chars (bone only — no production language;
  8항목 다 박으면 자연히 이 분량 / 638자 부실 = 누락, §2 CREATE Density)
- COVER: Dense 700-950 chars (full texture + Suno-hacking defaults)
- ONE-SHOT: 850-950 chars (compressed 통합)

CREATE paints the skeleton; COVER paints the body — *내용*이 다른 것이지
길이가 다른 게 아니다. They must NOT share more than 30% of descriptors
(09 § 3.5b). (구 "CREATE 400-700 / COVER 800-950 split"은 v2.6에서 폐기.)

Result = output that resembles "that song" rather than "songs of
that genre", with bone/texture cleanly separated for re-skinning.

The shift in practice:

| v1.x | v2.0 |
|---|---|
| "K-pop, 130 BPM, female vocal, breathy, polished, four-piece" | "Late-2020s K-indie crossover at 130 BPM, the kind that opens with finger-picked acoustic and lets the room ambience breathe before the drums arrive at bar 9. Female vocal C4-F5: breathy and conversational in Korean verses, airy crystal-clear on the English chorus hook, never crossing into belt..." |
| 95 characters | 380+ characters of usable direction |
| Engine improvises 80% | Engine renders 60-70% of specified moments |

### The Three Operating Modes

**Reference-First mode (default for YUNY):**
1. `13_REFERENCE_ANALYSIS.md` produces 9 craft variables + Signature
   Moments
2. `15_NATURAL_LANGUAGE_DIRECTION.md` provides the vocabulary
3. `12` (this file) wraps both into CREATE/COVER or ONE-SHOT format
4. `14_PROSODY_AND_PHONETICS.md` validates singability
5. `09_SUNO_ENGINE.md` § 11 final gate
6. Output

**Build-up mode (opt-in):**
Phase 0-Deep deliberation → Phase 1 theory grounding → Phase 2 (this
file) prompt construction. Same templates, different upstream.

**Quick-sketch mode:**
ONE-SHOT skeleton (§ 2) for sub-2-minute experimental tracks.

### Mandatory Suno Instruction Layer

Every prompt this file produces must include the following layer
(no exceptions):

- `[Singing: ...]` cue per section (Verse / Chorus / Bridge / Outro)
- `[Pronunciation: ...]` for foreign words, acronyms, homographs
- Vocal protection keywords in Style Box if range crosses F5 (female)
  or A4 (male falsetto)
- Signature Moment translations (from `13` § 4.2 + `15` § 3) embedded
  as Style Box natural-language sentences AND/OR Lyrics Box microcues
- `(count: NNN/1000)` annotation at end of Style Box
- Era anchor specificity (decade + region + scene, never bare
  "vintage" or "modern")
- Reference encoding: **direct artist names tried first** (per
  09 § 5.3b + system instruction C-1). Decomposed Signature is
  the fallback when Suno blocks/distorts. Song titles default
  to Decomposed (higher filter risk than artist names).

These are not decorations. They are how the song actually sounds in
Suno. Without them, the prompt is technically valid but sonically
unreliable.

---

## SECTION 1. UNIVERSAL CREATE/COVER PAIR SKELETON (v2.0)

This is the master template. All genre-specific recipes derive from it.

### 1.1 CREATE PROMPT Skeleton (v2.0)

```
--- CREATE PROMPT ---

[STYLE BOX] (count: NNN/1000)

<Genre anchor + tempo + key + core vocal in first 80 chars>
[Era anchor with scene specificity], <BPM> BPM, <key>.
<Female/Male/etc.> vocal range <low-high>: <2-3 timbre adjectives>
in <verse function>, <texture shift> on <chorus function>, never
crossing into <unwanted register>. <Language> with <accent if
relevant>.

<Scene paragraph: what arrives first, what verse texture is, how
chorus lifts, what bridge does. 200-300 chars of scene-painting
covering instrumentation core 3-5 instruments + section dynamics.>

Signature moments to render: (1) <moment 1 in natural language>,
(2) <moment 2>, (3) <moment 3 if applicable>.

<Vocal protection keywords if range crosses F5/A4 falsetto.>
Clear melody focus, structural clarity, organic dynamics — bone
prioritized over mix polish.

[LYRICS BOX]
[Intro 4]
(instrumental atmosphere)

[Verse 1 8]
[Singing: <texture>, <dynamics>, <phrasing>]
<lyric lines with inline microcues where Signature Moments occur>

[Pre-Chorus 4]
[Singing: <building cue>]
<lyric lines>

[Sudden Absolute Silence: 0.5 seconds full band cut]   ← if signature

[Chorus 8]
[Singing: <chorus delivery cue>]
[Doubled second phrase]                                 ← if signature
<lyric lines including title hook>

[Verse 2 8]
[Singing: <V2 variation cue>]
<lyric lines, slightly fuller texture than V1>

[Pre-Chorus 4]
[Singing: <re-build cue>]
<lyric lines>

[Chorus 8]
[Singing: <chorus delivery>]
[Doubled] [Harmony +3rd entering bar 5]
<lyric lines>

[Bridge 4-8]
[Singing: <departure cue — stripped, vulnerable, etc.>]
[Stripped to <whatever stays>]
<lyric lines, contrast in POV or imagery>

[Final Chorus 8]
[Singing: <climax cue>]
[Half-step modulation up] / [Doubled] / [Harmony +3rd +5th]
[Ad-libs on line ends]
<lyric lines>

[Outro 4]
[Singing: <fade cue>]
[Each repeat thinning out, vocal stays close-mic]
<closing fragment>
[End]

[EXCLUDE STYLES]
<3-6 anti-drift keywords: unwanted vocal traits, drift genres,
mix issues>

[NOTES]
CREATE goal: lock melody, vocal phrasing, structural clarity,
Signature Moments. Mix quality secondary — COVER will refine.
CREATE GUARDRAIL: Style Box Dense 700-950 chars (sketch 시 Tight
250-350). 700자 초과는 정상 bone 밀도이지 누설 아님 — 길이로 판정하지
말 것. No production processing, no frequency specs, no mix
character, no atmospheric texture. 판정은 길이가 아니라 내용으로:
words like "reverb", "compression", "stereo width", "saturation",
"LUFS" belong in COVER (내용 혼입 0%), move them.
```

### 1.2 COVER PROMPT Skeleton (v2.0)

```
--- COVER PROMPT ---

[STYLE BOX] (count: NNN/1000)

<Same genre + tempo + key as CREATE in first 80 chars>
[Era anchor maintained], <BPM> BPM, <key>.
<Decomposed Signature: producer/engineer lineage in 2-3
descriptive phrases, no direct names>

<Full instrumentation paragraph: 6-10 instruments with role
specificity. Where each sits in the frequency spectrum, how the
stereo image distributes, what the production character is.>

<Mix character paragraph: stereo width per section, dynamics
profile, EQ tilt, reverb character per section. Verse dry vs
chorus bloom mapping if applicable.>

<Atmospheric / texture seasoning: 2-3 mood adjectives + texture
details like vinyl crackle, room ambience, tape warmth.>

Signature moments preserved from CREATE: (1) <moment 1 with
production texture added>, (2) <moment 2 + texture>, (3)...

<LUFS target if genre-specific. Vocal corridor protection
keywords. Anti-drift keywords for tendencies.>

[LYRICS BOX]
(preserved from CREATE — no changes to lyric content or section
tags. May add atmospheric tags like [breathing] or [room tone]
where applicable.)

[EXCLUDE STYLES]
<3-6 keywords specifically targeting drift tendencies that may
have appeared in CREATE>

[NOTES]
COVER goal: re-skin CREATE take with full target genre identity
+ production texture. Vocal preserved by Cover Mode; Style Box
focuses on production architecture and Signature Moment texture.
```

### 1.3 Decision Logic — When to Use This Pair

Use CREATE/COVER pair when:
- Track is intended for release or serious use
- Vocal identity must be preserved across iterations
- Specific reference sound is required
- Production character is complex (hybrid genre, specific era,
  layered atmosphere)
- Signature Moments require both melodic locking (CREATE) and
  production texture (COVER)

Skip the pair (use ONE-SHOT § 2) when:
- Quick sketch under 2 minutes
- Single-take experiment
- Concept exploration phase, not production phase
- Operator explicitly requests one-shot

---

## SECTION 2. ONE-SHOT SKELETON (v2.0)

For quick sketches, single-take experiments, short tracks under 2:30.

```
--- ONE-SHOT PROMPT ---

[STYLE BOX] (count: NNN/1000)

<Position 0-80: Genre anchor + tempo + key + condensed vocal directive>
[Era anchor], <BPM> BPM, <key>.
<Gender> <voice type> vocal <range>: <2 timbre adj>, <delivery>,
<language>.

<Position 80-400: Scene paragraph — what arrives first, verse
texture, chorus lift, bridge departure. ~300 chars of specific
direction.>

<Position 400-700: Signature moments + section dynamics.
2-3 moments translated into natural language.>

<Position 700-900: Production / mix character + atmospheric
seasoning + vocal protection keywords if needed.>

<Position 900-950: Final accent — mood + LUFS + anti-drift.>

[Position 950-1000: SAFETY BUFFER — leave empty]

[LYRICS BOX]
[Intro 4]

[Verse 1 8]
[Singing: <delivery cue>]
<lyrics>

[Pre-Chorus 4]
<lyrics>

[Chorus 8]
[Doubled]
[Singing: <chorus cue>]
<lyrics with title hook>

[Verse 2 8]
<lyrics>

[Pre-Chorus 4]
<lyrics>

[Chorus 8]
[Doubled] [Harmony +3rd]
<lyrics>

[Bridge 4]
[Stripped back]
[Singing: <bridge cue>]
<lyrics>

[Final Chorus 8]
[Singing: <climax cue>]
[Ad-libs] [Doubled]
<lyrics>

[Outro 4]
[Fade out]
[End]

[EXCLUDE STYLES]
<3-6 anti-drift keywords>

[NOTES]
One-shot mode: vocal and production combined in single prompt.
Re-roll expected — generate 2-3 takes and pick best.
```

### 2.1 One-Shot Trade-offs

Disclose to operator when using ONE-SHOT:
- Higher chance of vocal-genre mismatch
- Less control over melody character
- More re-rolls likely
- Better for short tracks (≤2:30)

---

## SECTION 3. PERSONA-LOCKED WORKFLOW

For album work or multi-track series where vocal identity must stay
consistent.

### 3.1 Persona Build Step

```
--- PERSONA DESCRIPTION (saved in Suno Persona slot) ---

<Gender> <voice type> vocal, range <low-high>.
<Timbre signature in 2-3 sentences of natural language>:
<texture in verse register>, <texture in chorus register>,
<distinctive trait if any: light vibrato, breathy attacks,
slight rasp on belted peaks>.

<Language and accent>: <delivery default in natural language —
e.g., "conversational with subtle melismatic ornaments at
phrase ends, behind-beat phrasing throughout, slight breath
audible between phrases.">

<Reference era / scene if helpful for vocal identity:
"late-2010s indie female pop vocal lineage" or equivalent>.

(target 250-450 characters for Persona slot)
```

### 3.2 Per-Track Custom Prompt with Persona Active

```
--- TRACK PROMPT WITH PERSONA ACTIVE ---

[STYLE BOX] (count: NNN/1000)

<Persona handles vocal identity — Style Box focuses entirely
on music. Use the budget for scene + Signature Moments +
production texture.>

<Era anchor>, <BPM> BPM, <key>.

<Scene paragraph 250-300 chars>
<Section dynamics + Signature Moments 200-300 chars>
<Production / mix / atmospheric 200-300 chars>

[LYRICS BOX]
<full lyric structure with section tags + microcues>

[EXCLUDE STYLES]
<anti-drift keywords>

[NOTES]
Persona active for vocal identity consistency.
Style Box focuses purely on per-track musical direction.
```

### 3.3 When to Use Persona

- Album projects (5+ tracks needing same vocal identity)
- Series of related tracks
- Concept records with defined "singer" character
- After CREATE produces a vocal you want to lock for all future
  iterations

---

## SECTION 4. GENRE-SPECIFIC PROMPT RECIPES (v2.0)

Each recipe provides a CREATE-stage Style Box and a COVER-stage Style
Box, written in v2.0 natural-language style. Adjust BPM, key, vocal
range, and lyrical content per track.

### 4.1 Modern K-Pop (4th Generation Crossover)

**CREATE Style Box (~880 chars):**

```
Late-2020s K-pop crossing into K-indie bedroom feel, 130 BPM,
F major modulating to F# major in final chorus. Female group
vocals A3-E5: airy crystal-clear unison on verses, slight chest
mix on chorus hook, never belted — modern K-pop preserves
proximity over power. Korean lyrics with one English phrase
landing on the chorus melodic peak.

Verse arrangement is sparse and breathing: soft kit with brushed
snare, controlled sub-bass on the kick fundamental, sustained
warm pad underneath, single plucked acoustic carrying the
harmonic motion. Pre-chorus brings in a UK-garage-influenced
hi-hat skip without changing the kick pattern. Chorus opens with
a doubled lead vocal at slight detune (~10 cents), a layered
synth pluck doubling the topline at +octave, and a fuller pad
bed — but the density stays moderate, not wall-of-sound.

Signature moments to render: (1) chorus enters without crash or
riser — just begins, 4th-gen K-pop convention; (2) bridge drops
to vocal + sub-bass + sparse piano only, four bars; (3) final
chorus modulates a half-step up with full layered harmony stack
+3rd +5th. Wide stereo image, vocal centered.

[LYRICS BOX]
[Intro 4]
[Atmospheric Intro: pad and vocal hum, 4 bars]

[Verse 1 8]
[Singing: airy crystal clear, conversational, chest dominance lower register]
<lyrics in Korean>

[Pre-Chorus 4]
[Singing: tightening cadence, slight push on phrase ends]
<lyrics in Korean>

[Chorus 8]
[Singing: still light texture, slight push, no belt — proximity not power]
[Doubled +10 cent detune]
<lyrics in Korean with English hook on final phrase>

[Verse 2 8]
[Singing: same texture as V1, slightly fuller, +1dB presence]
<lyrics>

[Pre-Chorus 4]
<lyrics>

[Chorus 8]
[Doubled] [Harmony +3rd entering bar 5]
<lyrics>

[Bridge 4]
[Stripped to vocal + sub-bass + sparse piano]
[Singing: vulnerable, half-spoken, breath audible]
<lyrics>

[Final Chorus 8]
[Singing: chorus delivery + key change up half-step]
[Half-step modulation up to F# major]
[Doubled] [Harmony +3rd +5th]
[Ad-libs on line ends]
<lyrics>

[Outro 4]
[Singing: returning to intimate distance]
<closing fragment>
[End]

[EXCLUDE STYLES]
auto-tune heavy, EDM drop, big-room K-pop chorus belt, generic
idol backing, distorted guitar
```

**COVER Style Box (~920 chars):**

```
Late-2020s K-pop polished bedroom-indie crossover production,
130 BPM, F major, the kind associated with the post-NewJeans
4th-gen scene where indie warmth bleeds into idol craft.
Decomposed signature: warm analog-modeled mix character,
controlled but not crushed loudness, mid-forward presence with
air shelf at 10-12 kHz untouched, vocal corridor 500Hz-3kHz
protected.

Full arrangement: brushed kit panned narrow, controlled sub-bass
mono below 80Hz sidechained to kick at 80ms, plucked acoustic
guitar pair L40/R40, warm Juno-style pad bed sustained, layered
synth pluck on chorus L60/R60, doubled lead vocal centered with
+10 cent detune width.

Mix character: verses recorded dry close-mic with 8% wet plate
reverb, chorus blooms to 22% wet with room ambience added,
bridge strips to nearly dry with subtle hall tail, final chorus
returns to chorus reverb settings + half-step modulation
preserved with full layered harmony.

Atmospheric texture: subtle vinyl warmth on the master bus,
analog tape saturation +1dB on vocal bus, organic human breath
preserved between phrases. Wide stereo image with centered
vocal and bass core. Loudness target -10 LUFS modern K-pop
controlled.

[EXCLUDE STYLES]
auto-tune heavy, vocoder, festival EDM drop, generic idol
backing, distorted guitar, crowd cheering, stadium reverb
```

### 4.2 Indie Folk / Bedroom Pop

**CREATE Style Box (~860 chars):**

```
Late-2010s East Coast bedroom indie folk, 92 BPM, D major with
borrowed iv (Gm) appearing in the bridge. Female mezzo G3-D5:
breathy and conversational close-mic throughout, dropping to
near-whisper on intimate lines, never crossing into belt — the
emotional weight comes from flatness, not lift.

The track opens with finger-picked steel-string acoustic alone
for 4 bars, then voice arrives dry and forward. Verses sparse:
acoustic + soft brushed snare with rim cross-stick + walking
upright bass + sustained ambient pad barely audible underneath.
Pre-chorus adds a second acoustic at +octave for harmonic
density without volume increase. Chorus brings warm low-mid
upright bass forward and a doubled lead vocal at slight detune,
but no drums lift — the band stays at the same energy while the
vocal layering accumulates.

Signature moments to render: (1) verse 2 enters after a
half-second band silence, voice arrives dry close-mic alone
first; (2) bridge drops to acoustic + voice only, with
chromatic descending bass under a held vocal note; (3) outro
repeats the hook with each pass thinning out — final pass voice
+ single guitar.

[LYRICS BOX]
[Intro 4]
[Acoustic guitar fingerpicking, voice enters bar 5]

[Verse 1 8]
[Singing: breathy conversational close-mic, dry tone, no vibrato]
<lyrics in English>

[Pre-Chorus 4]
[Singing: same texture, +octave acoustic enters underneath]
<lyrics>

[Chorus 8]
[Singing: still light, doubled lead +12 cent detune second phrase]
[Doubled second phrase, no harmony stack]
<lyrics>

[Sudden Absolute Silence: 0.5 seconds full band cut]

[Verse 2 8]
[Singing: voice arrives alone first, band re-enters bar 3]
<lyrics, slightly more vulnerable register>

[Pre-Chorus 4]
<lyrics>

[Chorus 8]
[Doubled] [Light harmony +3rd entering bar 5]
<lyrics>

[Bridge 4]
[Stripped to acoustic + voice only]
[Singing: held note, vibrato emerging slow, breath release]
<lyrics with chromatic descending bass under>

[Final Chorus 8]
[Singing: warmest of the song, slight tear in tone]
[Doubled] [Harmony +3rd]
<lyrics>

[Outro 4]
[Each repeat thinning out, final pass voice + single guitar]
<closing fragment>
[Fade out]
[End]

[EXCLUDE STYLES]
electronic drums, auto-tune, EDM, polished radio-pop, aggressive
bass, festival sound, K-pop chorus belt
```

**COVER Style Box (~910 chars):**

```
Intimate late-2010s East Coast bedroom indie folk, 92 BPM, D
major. Decomposed signature: acoustic-forward production with
audible room sound, narrow-to-medium stereo image (60-75% width
in verses, expanding to 85% on chorus), mid-forward EQ tilt,
warm low-mid presence.

Full arrangement: finger-picked steel-string acoustic guitar
foreground centered, second acoustic at +octave entering
pre-chorus L40, brushed snare with rim cross-stick narrow
center, walking upright bass warm thump 80-200Hz mono, soft
analog pad 300-800Hz subdued L60/R60, muted shaker ghost
tambourine gentle.

Mix character: vocal dry close-mic with 12% wet plate reverb on
verses blooming to 25% on chorus — the room arrives only on the
hook. Bridge sparse with hall tail nearly silent. Final chorus
returns to chorus reverb settings, slight tape saturation on
master bus. Light analog tube warmth +1dB on vocal bus, no
aggressive compression.

Atmospheric texture: melancholic nostalgic, autumn evening
mood, slight tape saturation throughout. Loudness controlled
-12 LUFS open dynamics, no aggressive limiting, transients
preserved. Vinyl-warmth aesthetic.

[EXCLUDE STYLES]
electronic drums, auto-tune, EDM, polished radio-pop, aggressive
bass, festival sound, crowd cheering, generic K-pop production
```

### 4.3 Hip-Hop / Trap

**CREATE Style Box (~880 chars):**

```
Modern atmospheric trap, 140 BPM with half-time perception
(felt 70 BPM), F# minor static loop with dark melodic top.
Male tenor C3-G4: gritty confident melodic-rap delivery,
sung-rap on hook with subtle pitch correction, deadpan
conversational on verses, English with subtle regional
inflection.

Production foundation: deep 808 sub-bass sustained through
chord changes with slight pitch glide between root tones,
trap snare on beat 3 only with hard hit, off-grid hi-hat 16ths
with triplet rolls and 32nd skitters in transitions, sparse
dark melodic loop in upper register (piano or bell).
Verse arrangement leaves wide mid-range vacancy for vocal
forward presence.

Signature moments to render: (1) hook entry preceded by 0.3
seconds full band silence, vocal arrives in the gap; (2) verse
2 beat switch — kick pattern doubles for 8 bars then returns;
(3) bridge stops time, band hits on 1 only, vocal in the
silence between hits.

[LYRICS BOX]
[Intro 4]
[Hi-hat roll into beat]

[Verse 1 16]
[Singing: deadpan conversational rap, slight grain, no auto-tune]
[Trap ad-libs throughout: yuh, ay]
<lyrics>

[Sudden Absolute Silence: 0.3 seconds]

[Hook 8]
[Singing: melodic-rap hook, doubled with +5th harmony]
[Doubled]
<hook lyrics with title>

[Verse 2 16]
[Singing: slightly more melodic than V1, controlled rasp]
[Beat switch: kick pattern doubles for 8 bars]
<lyrics>

[Hook 8]
[Doubled] [Harmony +5th]
<hook lyrics>

[Bridge 8]
[Stop-time: band hits on 1 only]
[Singing: vocal in the silence between hits, slower delivery]
<lyrics>

[Hook 8]
[Singing: full melodic delivery, ad-libs throughout]
[Doubled] [Trap ad-libs]
<hook lyrics>

[Outro 4]
[Sub-bass sustains, hi-hat fades]
<closing>
[End]

[EXCLUDE STYLES]
acoustic guitar, country twang, orchestral strings, jazz
harmony, generic boom-bap, K-pop production
```

**COVER Style Box (~895 chars):**

```
Modern atmospheric trap production 2018-2022 Atlanta lineage,
140 BPM half-time perception, F# minor. Decomposed signature:
sub-bass-forward mix architecture, controlled mid-range
vacancy, vocal-forward presence with subtle auto-tune residue.

Full arrangement: deep 808 sub-bass mono below 60Hz with slight
pitch glide between tones, sidechain duck under kick at 80ms,
trap kick punchy 60-100Hz fundamental, snare hard hit on beat 3
with 1.5 second plate tail, hi-hat 16th triplet rolls panned
narrow center, sparse dark melodic loop in upper register
3-5kHz, doubled lead vocal centered with light auto-tune at
+5th harmony layer.

Mix character: vocal corridor 500Hz-3kHz protected forward,
sub-bass dominant 20-80Hz, mid-range carved 200-500Hz to leave
space, hi-hat 8-12kHz crisp, master loudness crushed -8 LUFS
modern trap competitive.

Atmospheric texture: moody nocturnal late-night urban mood,
hi-hat triplet rolls in transitions, beat switch sharp on
verse 2, stop-time bridge with reverb tails preserved.

[EXCLUDE STYLES]
acoustic guitar, country twang, orchestral strings, jazz
harmony, generic boom-bap, K-pop production, crowd cheering
```

### 4.4 Neo-Soul / Modern R&B

**CREATE Style Box (~870 chars):**

```
Modern neo-soul late-2010s alternative R&B lineage, 88 BPM with
drunken laid-back swing slightly behind grid, E minor with
extended chord palette (Em9, Am11, Bm7, Em9 rootless voicings).
Female alto F3-C5: smooth-warm melismatic delivery with breathy
attack, behind-the-beat conversational phrasing, slight vocal
fry on lower register, English with natural accent.

The track opens with Rhodes electric piano alone for 4 bars,
then fretless bass enters walking through chord tones, then
drums arrive on bar 9 with brushed live-feel humanization.
Verses sparse with vocal forward and dry close-mic. Chorus
brings stacked harmony vocals (+3rd, +5th, octave) on hook
entry, plate reverb blooms on lead vocal, but the band stays
at moderate density.

Signature moments to render: (1) chorus second phrase brings in
melismatic ad-lib runs underneath the lead; (2) bridge becomes
a vamp section — repeated 2-chord cycle for 8 bars with vocal
improvisation accumulating; (3) final chorus returns with
breath emphasis on belted notes, slight tear in tone.

[LYRICS BOX]
[Intro 8]
[Rhodes electric piano alone first 4 bars, bass enters bar 5,
drums enter bar 9]

[Verse 1 8]
[Singing: breathy intimate close-mic, melismatic phrase ends, behind-beat]
<lyrics in English>

[Pre-Chorus 4]
[Singing: rising intensity, melismatic ornaments developing]
<lyrics>

[Chorus 8]
[Singing: passionate melismatic, full-throated on belted notes]
[Harmony +3rd]
[Ad-libs underneath]
<chorus lyrics>

[Verse 2 8]
[Singing: slightly more confident, fuller chest mix]
<lyrics>

[Pre-Chorus 4]
<lyrics>

[Chorus 8]
[Stacked harmonies +3rd +5th +octave]
[Doubled lead]
<chorus lyrics>

[Bridge 8]
[Vamp section: repeated 2-chord cycle Em9-Am11]
[Singing: improvised ad-libs accumulating]
[Spoken: soft, occasional]
<lyrics>

[Final Chorus 8]
[Singing: warmest belt, slight tear, breath emphasis]
[Gospel choir backing]
[Ad-libs throughout]
<chorus lyrics>

[Outro 4]
[Singing: breathy fade]
[Fade out]
[End]

[EXCLUDE STYLES]
aggressive 808, EDM drop, auto-tune T-Pain style, country
accent, generic K-pop chorus belt
```

**COVER Style Box (~915 chars):**

```
Modern neo-soul late-2010s alternative R&B lineage, 88 BPM
drunken laid-back swing, E minor. Decomposed signature: warm
vintage tube production with analog character, fretless rounded
bass forward in low-mids, vintage Rhodes electric piano with
chorus modulation, live-feel drums with subtle swing and ghost
notes humanization.

Full arrangement: vintage Rhodes electric piano with light
chorus effect L30/R30, fretless bass walking warm 80-300Hz mono
forward, brushed kit with ghost-note snare slightly behind grid,
sparse percussion shaker rim, female alto lead vocal close-mic
with stacked harmony vocals +3rd +5th +octave on hook entry,
optional gospel choir backing on final chorus.

Mix character: warm low-mid forward presence with vocal-prominent
mids, plate reverb on lead vocal 25% wet on verses with subtle
room ambience on drums, vintage tape saturation on master bus,
medium stereo width vocal centered, slight tube saturation +1dB
on vocal bus. Loudness controlled -11 LUFS open natural dynamics.

Atmospheric texture: intimate sensual late-night studio mood,
vinyl warmth, analog tube character throughout. Brushed cymbal
swells into chorus, vamp section with vocal improvisation in
bridge.

[EXCLUDE STYLES]
aggressive 808, EDM drop, auto-tune T-Pain style, country accent,
generic K-pop chorus belt, crowd cheering, distorted guitar
```

### 4.5 Ballad (Pop / Cinematic)

**CREATE Style Box (~885 chars):**

```
Late-2010s film-anthem cinematic pop ballad lineage, 72 BPM,
G major with minor color through borrowed iv (Cm) in pre-chorus.
Female mezzo A3-F5: warm passionate vulnerable in verses
intimate close-mic, building toward emotional climax in
choruses with controlled chest belt and slight rasp on peak
notes, English natural accent with subtle vibrato on long
sustained notes.

Track architecture follows massive dynamic range from intimate
to climactic. Opening: grand piano alone for 8 bars with sustain
pedal, recorded with natural room ambience. Verse 1 adds vocal
dry close-mic with audible breath. Pre-chorus brings in
sustained orchestral strings entering soft. Chorus 1 layers
soft live kick + brushed snare with no hi-hat, doubled lead
vocal with subtle harmony +3rd. Bridge strips back to piano +
voice only.

Signature moments to render: (1) chorus 1 entry preceded by
strings climbing in dynamic underneath the held last pre-chorus
note; (2) bridge drops to piano + voice only with vulnerable
half-spoken delivery; (3) final chorus modulates a half-step up
with full string section + cymbal swell + ad-libs accumulating.

[LYRICS BOX]
[Intro 8]
[Grand piano alone, sustain pedal, natural room ambience]

[Verse 1 8]
[Singing: intimate vulnerable close-mic, audible breath, slight tremor]
<lyrics in English>

[Pre-Chorus 4]
[Singing: building toward chorus, strings entering underneath]
<lyrics>

[Chorus 8]
[Singing: passionate chest mix, controlled vibrato, slight rasp on peak]
[Doubled lead]
[Harmony +3rd entering bar 5]
<chorus lyrics with title>

[Verse 2 8]
[Singing: slightly more confident, fuller texture]
<lyrics>

[Pre-Chorus 4]
<lyrics>

[Chorus 8]
[Stacked harmonies +3rd +5th]
<chorus lyrics>

[Bridge 8]
[Stripped to piano + voice only]
[Singing: half-spoken vulnerable, slower delivery, breath audible]
<lyrics>

[Final Chorus 8]
[Half-step modulation up to G# major]
[Singing: full belt, controlled rasp, slight tear in tone]
[Full string section + cymbal swell]
[Ad-libs accumulating]
<chorus lyrics>

[Outro 4]
[Singing: returning to intimate, vocal contracts to dry]
[Fade out, piano sustains]
[End]

[EXCLUDE STYLES]
electronic drums, distorted guitar, auto-tune, modern compressed
loudness, EDM drop, generic K-pop production
```

**COVER Style Box (~925 chars):**

```
Late-2010s film-anthem cinematic pop ballad lineage, 72 BPM,
G major. Decomposed signature: grand piano foundation with
natural room recording, sustained orchestral string section,
massive dynamic range cinematic open dynamics, no aggressive
limiting.

Full arrangement: grand piano centered with sustain pedal and
natural hall ambience, sustained orchestral strings entering
pre-chorus L70/R70 wide, soft live kick with brushed snare on
chorus narrow center no hi-hat, female mezzo lead vocal
close-mic with subtle vibrato, doubled lead on chorus, harmony
+3rd on chorus 2, full harmony +3rd +5th on final chorus,
optional gospel choir entering final chorus.

Mix character: wide stereo string section with centered vocal
and piano core, warm hall reverb on vocal 35% wet on chorus,
plate reverb on piano 20% wet, vocal corridor 500Hz-3kHz
protected forward presence. Massive dynamic range from intimate
verse -18 LUFS to climactic final chorus -7 LUFS, cinematic
open dynamics, no aggressive limiting, transients preserved.

Atmospheric texture: yearning bittersweet golden-hour mood,
key change into final chorus with cymbal swell, slight tape
warmth +1dB on master, organic acoustic ambience preserved.

[EXCLUDE STYLES]
electronic drums, distorted guitar, auto-tune, modern compressed
loudness, EDM drop, generic K-pop production, crowd cheering
```

### 4.6 Synth-Pop / 80s Revival

**CREATE Style Box (~870 chars):**

```
Late-1980s synthwave revival meets 2020s indie-pop sensibility,
118 BPM, F minor with i-VI-III-VII Andalusian descent in chorus.
Male tenor D3-B4: dry detached delivery in verses with slight
chorus-effect on lead, layered chorus harmonies +octave +5th on
hook, English with smooth vowels, subtle vocoder doubling on
post-chorus.

Production foundation: pulsing 80s-style drum machine with
gated reverb snare on 2 and 4, sequenced 16th-note synth bass
arpeggiator following root motion, stacked Juno-style pad chords
sustaining underneath, neon lead synth doubling vocal at
+octave on chorus. Verse arrangement leaves space for vocal
forward presence.

Signature moments to render: (1) chorus entry with sidechain
pump audible on bass and pads against kick; (2) bridge breaks
into ambient synth pad solo for 4 bars before vocal returns;
(3) final chorus adds an octave-up vocoder layer on the hook
phrase only.

[LYRICS BOX]
[Intro 8]
[Synth arpeggiator + drum machine]

[Verse 1 8]
[Singing: dry detached, slight chorus-effect on lead, no vibrato]
<lyrics in English>

[Pre-Chorus 4]
[Singing: tightening, building harmonic density]
<lyrics>

[Chorus 8]
[Singing: layered chorus harmonies +octave +5th]
[Sidechain pump on bass and pads against kick]
<chorus lyrics with title>

[Verse 2 8]
<lyrics>

[Pre-Chorus 4]
<lyrics>

[Chorus 8]
[Stacked harmonies +octave +5th]
<chorus lyrics>

[Bridge 4]
[Ambient synth pad solo, no vocal first 4 bars]
[Singing: vocal returns half-spoken theatrical]
<lyrics>

[Final Chorus 8]
[Octave-up vocoder layer on hook phrase only]
[Stacked harmonies + vocoder doubling]
<chorus lyrics>

[Outro 8]
[Synth arpeggiator vamp, vocal fades]
[Fade out with gated reverb decay]
[End]

[EXCLUDE STYLES]
acoustic guitar, country twang, jazz harmony, lo-fi mud,
generic K-pop production, distorted metal guitar
```

**COVER Style Box (~890 chars):**

```
Late-1980s synthwave revival production with 2020s indie-pop
sensibility, 118 BPM, F minor. Decomposed signature: glossy
80s analog character meets modern controlled loudness, neon
synth foreground, gated drum reverb signature, sidechain pump
audible on chorus.

Full arrangement: pulsing LinnDrum-style drum machine kit with
gated reverb snare 2 and 4 wide L70/R70, sequenced 16th-note
synth bass arpeggiator centered mono below 100Hz, stacked
Juno-style pad chords sustaining L60/R60, neon lead synth
doubling vocal at +octave on chorus L40/R40, male tenor lead
vocal close-mic with subtle chorus-effect, doubled lead on
chorus with stacked harmonies +octave +5th.

Mix character: glossy 80s analog production with chorus-effect
on lead vocal, gated drum room cut hard, sidechain pump on bass
and pads against kick at 120ms creating audible breathing,
wide stereo synth layers with centered bass and kick, bright
sparkling top end. Loudness modern controlled -10 LUFS.

Atmospheric texture: neon nocturnal mood, glossy analog warmth,
analog tape saturation on master, gated reverb signature
maintained throughout sections.

[EXCLUDE STYLES]
acoustic guitar, country twang, jazz harmony, lo-fi mud,
generic K-pop production, distorted metal guitar, crowd cheering
```

### 4.7 City-Pop / J-Pop Throwback

**CREATE Style Box (~880 chars):**

```
Mid-1980s Tokyo city-pop scene revival, 116 BPM, A major with
jazz-influenced harmony (IVmaj7-V-iii-vi Royal Road progression).
Female mezzo G3-E5: bright clean polished timbre with melismatic
phrase ends and breath-stops for emphasis, joyful articulate
delivery, Japanese natural pronunciation with clear vowel
articulation.

Track opens with slap bass forward and clean Rhodes electric
piano with chorus modulation, then DX7-style FM synth pads
entering on bar 5, then live drums with light gated reverb on
snare arriving on bar 9. Brass horn section stabs accent chorus
and hook downbeats. Verse arrangement keeps slap bass and
Rhodes forward with vocal centered. Chorus brings doubled lead
+ harmony +3rd +5th, brass stabs on every other beat.

Signature moments to render: (1) instrumental break before
final chorus features sax solo over the chord progression;
(2) bridge drops slap bass for 4 bars leaving Rhodes + vocal +
soft drums; (3) final chorus adds an octave-up vocal stack on
hook phrase with brass stabs intensified.

[LYRICS BOX]
[Intro 8]
[Slap bass + Rhodes electric piano, drums enter bar 9]

[Verse 1 8]
[Singing: bright clean Japanese articulation, melismatic phrase ends]
<lyrics in Japanese>

[Pre-Chorus 4]
[Singing: building, breath-stops on phrase ends]
<lyrics>

[Chorus 8]
[Singing: joyful articulate, melismatic ornaments on hook]
[Doubled] [Harmony +3rd]
[Brass stabs on hook downbeats]
<chorus lyrics>

[Verse 2 8]
<lyrics>

[Pre-Chorus 4]
<lyrics>

[Chorus 8]
[Stacked harmonies +3rd +5th]
[Brass stabs intensified]
<chorus lyrics>

[Instrumental Break 8]
[Saxophone solo over chord progression]

[Bridge 4]
[Slap bass drops, Rhodes + vocal + soft drums]
[Singing: smoother delivery, slower phrasing]
<lyrics>

[Final Chorus 8]
[Octave-up vocal stack on hook phrase]
[Brass stabs intensified, full layered harmonies]
<chorus lyrics>

[Outro 4]
[Slap bass vamp, brass fade]
[Fade out]
[End]

[EXCLUDE STYLES]
lo-fi mud, modern trap drums, auto-tune T-Pain, EDM drop,
generic K-pop production
```

**COVER Style Box (~915 chars):**

```
Mid-1980s Tokyo urban-pop scene production, 116 BPM, A major
with jazz extensions. Decomposed signature: glossy 1980s analog
production with warm tape saturation, slap bass forward funk
articulation, clean Rhodes electric piano with chorus
modulation, bright high-end with vintage analog softness.

Full arrangement: slap bass syncopated 16th lines mono forward
80-400Hz, Rhodes electric piano with chorus effect L40/R40,
DX7-style FM synth pads sustained L60/R60, live kit with light
gated reverb on snare wide L80/R80, brass horn section trumpet
trombone sax stabs centered, female mezzo lead vocal centered
with stacked harmony +3rd +5th on chorus.

Mix character: warm 80s Tokyo studio analog character, slap bass
prominent forward, plate reverb on Rhodes 18% wet, hall reverb
on vocal 22% wet on chorus, glossy bright high-end 8-12kHz with
vintage analog softness, wide polished stereo image with
centered vocal and bass core. Loudness vintage controlled -12
LUFS open natural dynamics.

Atmospheric texture: nostalgic golden-hour summer Tokyo mood,
analog tape saturation +1dB on master, cymbal swells into
chorus, sax solo in instrumental break, no auto-tune.

[EXCLUDE STYLES]
lo-fi mud, modern trap drums, auto-tune T-Pain, EDM drop,
generic K-pop production, crowd cheering, distorted guitar
```

### 4.8 Lo-Fi / Bedroom / Chill

**CREATE Style Box (~860 chars):**

```
Mid-2010s SoundCloud-era lo-fi bedroom indie, 80 BPM, A minor
with simple ii-i-VI-VII loop. Androgynous vocal A3-D5: hushed
breathy intimate timbre, half-sung mumbled delivery, English
natural accent with audible room sound, no studio polish.

Track opens with sparse upright piano with damper noise audible
for 4 bars, then warm soft sub-bass enters underneath, then
minimal trip-hop beat with vinyl crackle texture on bar 9.
Verse arrangement is muffled lo-fi production with audible
noise floor — the imperfection is the aesthetic. Chorus stays
at similar density with vocal slightly more forward, no big
production lift.

Signature moments to render: (1) verse 2 starts with vinyl
crackle isolated for 1 bar then vocal returns; (2) bridge drops
beat entirely leaving piano + vocal + crackle only; (3) outro
loops the hook fragment with each pass adding more lo-fi noise
floor.

[LYRICS BOX]
[Intro 4]
[Sparse upright piano with damper noise, vinyl crackle]

[Verse 1 8]
[Singing: hushed breathy intimate, mumbled close-mic, audible room sound]
<lyrics in English>

[Pre-Chorus 4]
[Singing: same hushed texture, slightly more forward]
<lyrics>

[Chorus 8]
[Singing: still hushed, vocal slightly forward in mix]
<chorus lyrics>

[Verse 2 8]
[Vinyl crackle isolated 1 bar, vocal returns]
<lyrics>

[Pre-Chorus 4]
<lyrics>

[Chorus 8]
<chorus lyrics>

[Bridge 4]
[Beat drops, piano + vocal + crackle only]
[Singing: half-spoken whisper]
<lyrics>

[Final Chorus 8]
[Beat returns, vocal stays hushed]
<chorus lyrics>

[Outro 4]
[Hook fragment loops, lo-fi noise floor accumulates]
[Fade out with vinyl crackle continuing]
[End]

[EXCLUDE STYLES]
polished pop, EDM drop, aggressive bass, auto-tune heavy,
festival sound, generic K-pop chorus belt, distorted guitar
```

**COVER Style Box (~880 chars):**

```
Mid-2010s SoundCloud-era lo-fi bedroom indie production, 80
BPM, A minor. Decomposed signature: muffled lo-fi production
with audible noise floor, vinyl crackle texture continuous,
heavy tape saturation throughout, narrow stereo image.

Full arrangement: sparse upright piano with damper noise centered,
warm soft sub-bass mono below 80Hz subdued, minimal trip-hop
beat with vinyl crackle texture wide L70/R70, breathy
androgynous lead vocal close-mic with slight room sound centered,
no harmony layers — single tracked lead.

Mix character: narrow stereo image with vocal centered, mid-
forward warm EQ tilt, heavy tape saturation throughout master,
modest plate reverb on vocal 15% wet, soft compressed dynamics
with no aggressive limiting. Loudness deliberately under-mastered
-14 LUFS preserving lo-fi character.

Atmospheric texture: melancholic dreamy rainy afternoon mood,
vinyl crackle texture continuous throughout, soft fade outs,
imperfection-as-aesthetic intentional, room ambience preserved,
audible noise floor maintained.

[EXCLUDE STYLES]
polished pop, EDM drop, aggressive bass, auto-tune heavy,
festival sound, generic K-pop chorus belt, distorted guitar,
crowd cheering, stadium reverb
```

(Additional genre recipes 4.9-4.12 follow same v2.0 pattern. For
brevity, see `05_GENRE_LIBRARY.md` for genre conventions and
`13_REFERENCE_ANALYSIS.md` for case-by-case Signature Moment
extraction.)

---

## SECTION 5. ITERATION & REFINEMENT PROTOCOL

### 5.1 The Five-Iteration Cycle

```
ITERATION 1 — CREATE (3-4 takes)
   Goal: usable melody + vocal phrasing + Signature Moments rendered.
   Pick the best take. Save it.
   │
   ▼
ITERATION 2 — COVER from saved take (3-4 takes)
   Goal: re-skin with full target genre + production texture.
   Pick the best take. Save it.
   │
   ▼
ITERATION 3 — Refinement via Replace Section / Extend
   Goal: fix specific weak sections (e.g., bridge that lost
   Signature Moment).
   Use Suno's Replace Section feature or regenerate just that
   section.
   │
   ▼
ITERATION 4 — Persona Lock
   If vocal is right, save take as Persona for future tracks.
   │
   ▼
ITERATION 5 — Final Polish
   Crop, fade, trim. Optional: external mastering.
```

### 5.2 When to Re-Roll vs. When to Refine

**Re-roll the whole track when:**
- Vocal gender/range is wrong
- Genre identity completely misses
- Tempo is significantly off
- All Signature Moments lost

**Refine specific section when:**
- One section (usually bridge or outro) is weak
- One Signature Moment was lost but rest preserved
- Mix balance off in one section
- Vocal slip in one phrase
- Length wrong (too long: crop; too short: extend)

### 5.3 Common Iteration Tools

- **Crop**: trim length without regenerating
- **Fade Out**: clean ending without regeneration
- **Replace Section**: regenerate one section keeping the rest
- **Extend**: continue from any timestamp with new prompt input
- **Cover**: re-skin existing take in new style
- **Persona Save**: lock vocal identity for future tracks

---

## SECTION 6. DIAGNOSTIC DECISION TREE (v2.0)

When a generation goes wrong, follow this tree.

### 6.1 Vocal Issues

```
VOCAL ISSUE
   │
   ├── Wrong gender?
   │      → Move vocal directive to first 80 chars of Style Box.
   │      → Repeat at end. Re-generate.
   │
   ├── Wrong range / register?
   │      → Tighten range specification (e.g., "C4-F5" not "high range").
   │      → Add register cue ("chest voice" or "mixed voice").
   │      → Add register transition map (where voice changes register).
   │
   ├── Auto-tune / vocoder unwanted?
   │      → Check Style Box for "auto-tune" / "polished" — remove.
   │      → Add "no auto-tune residue" / "natural human breath" to
   │         Style Box.
   │      → Add "auto-tune, vocoder" to Exclude Styles.
   │
   ├── Wrong language / accent?
   │      → Add explicit language declaration in vocal directive.
   │      → Add `[Pronunciation: language]` cue in Lyrics Box at
   │         section start.
   │
   ├── Vocal too aggressive on intimate verse?
   │      → Style Box vocal cue too strong.
   │      → Add `[Singing: breathy, intimate]` tag in Lyrics for
   │         that section.
   │      → Specify register transition map (verse stays chest,
   │         not chorus mix).
   │
   ├── Vocal slip on one word?
   │      → Add pronunciation override:
   │         `[Pronunciation: word "PRO-noun-see-AY-shun"]`.
   │      → Or use Replace Section for that line.
   │
   └── Signature Moment vocal direction lost?
         → Direction may be too generic. Use specific microcue
            from `15` § 3.1.
         → Place microcue immediately after section tag.
```

### 6.2 Genre / Identity Issues

```
GENRE ISSUE
   │
   ├── Wrong primary genre?
   │      → Genre anchor buried past character 80. Move to position 1.
   │
   ├── Hybrid genre = only one genre showing?
   │      → Apply 70/30 ratio with zone assignment.
   │      → Specify "[Genre B] elements applied to [specific layer]".
   │
   ├── Sounds generic / dated?
   │      → No era anchor. Add "1980s Tokyo city-pop scene" or
   │         equivalent specific decade + region + scene.
   │      → Add 2-3 production characteristics from
   │         `11_PRODUCTION_DESIGN.md`.
   │
   ├── Sounds like genre average not "that song"?
   │      → No Signature Moments specified. Run `13` § 2.3
   │         Specific Moment Capture.
   │      → Add 3-5 moments to Style Box and Lyrics Box.
   │
   └── Drifting toward different genre?
         → Add unwanted genre to Exclude Styles field.
         → Strengthen primary genre anchor by repeating in
            Style Box position 0-30 AND position 800-900.
```

### 6.3 Structure Issues

```
STRUCTURE ISSUE
   │
   ├── Section length wrong?
   │      → Add bar count: `[Verse 1 8]` not `[Verse 1]`.
   │
   ├── Section ignored entirely?
   │      → Check section tag syntax. Use approved bracket form.
   │      → Ensure tag is on its own line.
   │      → Tag must be in Tier S/A reliable list (`10` § 0.3).
   │
   ├── Sections all sound the same energy?
   │      → Add `[Stripped back]` to verse, `[Doubled] [Harmony +3rd]`
   │         to chorus.
   │      → Specify density contrast in COVER prompt.
   │      → Use scene paragraph to map energy curve.
   │
   ├── Bridge feels random?
   │      → Add `[Bridge 4] [Stripped back] [Singing: vulnerable]`.
   │      → Or specify "key change" or "modulation" for clarity.
   │      → Add Signature Moment for bridge from `13`.
   │
   ├── Final chorus identity drift?
   │      → Add "throughout / maintained" keywords:
   │         "vogue ballroom architecture maintained throughout
   │          all sections, finger snap + clap preserved through
   │          outro".
   │
   └── Section transition abrupt?
         → Add transition cue at section boundary:
            `[Sudden Absolute Silence: 0.5 seconds]` or
            `[Cymbal swell into chorus]` or
            `[Half-bar dropout before chorus entry]`.
```

### 6.4 Production / Mix Issues

```
PRODUCTION ISSUE
   │
   ├── Mix sounds muddy?
   │      → Add "tight low-mids" or "carved low-mids 200-500Hz".
   │      → Add "muddy mix" to Exclude Styles.
   │
   ├── Vocal buried?
   │      → Add "vocal-forward mix, vocal corridor 500Hz-3kHz
   │         protected" to Style Box.
   │      → Add "vocal up-front presence" to mix character paragraph.
   │
   ├── Track feels small?
   │      → Add "wide stereo image" and "full production layers".
   │      → Specify era anchor for the right density expectations.
   │
   ├── Track feels harsh?
   │      → Add "smooth high-mids" and "refined treble".
   │
   ├── No dynamic excitement?
   │      → Specify different energy states per section in COVER.
   │      → Add "open dynamics" to counter Suno's default loudness.
   │      → Map verses at -3dB, choruses at reference, bridge at -5dB.
   │
   ├── Sounds dated when modern is wanted?
   │      → Update era anchor (specific decade + region + scene).
   │      → Add modern production keywords.
   │
   └── Stadium / crowd sound when not wanted?
         → Add "studio recording clean isolated" to Style Box.
         → Add "crowd cheering, live audience, stadium ambience"
            to Exclude Styles.
         → Avoid "stadium reverb" keyword (triggers crowd).
```

### 6.5 Length Issues

```
LENGTH ISSUE
   │
   ├── Track too long / repeats?
   │      → Use Crop tool to trim.
   │      → Or add explicit `[Outro 4] [Fade out]` at end of Lyrics.
   │
   ├── Track too short?
   │      → Use Extend tool with continuation prompt.
   │      → Or add more sections to Lyrics field and regenerate.
   │
   ├── Section too long?
   │      → Reduce bar count: `[Verse 1 4]` instead of `[Verse 1 8]`.
   │
   └── Track won't end?
         → Add `[End]` tag at the very end.
         → Or use Fade Out tool.
```

### 6.6 Signature Moment Loss (NEW in v2.0)

```
SIGNATURE MOMENT LOST
   │
   ├── Moment specified in Style Box but not rendered?
   │      → Move moment description to position 600-800 of Style Box
   │         (better front-weight than 800-950).
   │      → Add corresponding microcue in Lyrics Box at the relevant
   │         section.
   │      → Translate to specific instruction (see `15` § 3 table).
   │
   ├── Moment too abstract for engine?
   │      → Replace with concrete instruction:
   │         ❌ "bridge feels like floor drops"
   │         ✅ "bridge drops to vocal + sub-bass + sparse piano
   │             only, four bars"
   │
   ├── Moment competing with default genre behavior?
   │      → Add "throughout / maintained" keyword.
   │      → Add the conflicting default to Exclude Styles.
   │
   └── Multiple moments specified, only some rendered?
         → Reduce to 3 most important moments (engine handles 3-5).
         → Front-load most important moments (Style Box position
            600-800).
```

### 6.7 Token / Character Limit Issues

```
LIMIT ISSUE
   │
   ├── Style Box truncated?
   │      → Run compression protocol (`09_SUNO_ENGINE.md` § 8.2).
   │      → Cut to ≤ 950 chars.
   │      → Cut atmospheric mood adjectives first, never genre
   │         anchor or Signature Moments.
   │
   ├── Lyrics field truncated?
   │      → Cut to ≤ 4,800 chars.
   │      → Trim ad-libs, condense vocal direction tags.
   │
   └── Output ignores second half of prompt?
         → Confirm character count on both fields.
         → Front-load critical elements per `09_SUNO_ENGINE.md` § 9.
         → Move most important Signature Moments to position
            600-800 of Style Box.
```

---

## SECTION 7. THE MASTER WORKFLOW (v2.0 END-TO-END)

```
USER REQUEST
   │
   ▼
INPUT CLASSIFICATION
   │
   ├── Reference present (track / artist / sound description)?
   │      → REFERENCE-FIRST MODE
   │      → 13_REFERENCE_ANALYSIS.md protocol
   │           ├── Confidence Self-Check
   │           ├── Web Search if needed
   │           ├── Specific Moment Capture (3-5 moments)
   │           ├── 9 Craft Variables extracted
   │           └── 5-axis decomposition
   │      → 15_NATURAL_LANGUAGE_DIRECTION.md vocabulary applied
   │      → 12 (this file) wraps in CREATE/COVER or ONE-SHOT
   │      │
   │      ▼
   │   PROMPT CONSTRUCTION
   │
   └── Loose creative concept (no reference)?
          → BUILD-UP MODE
          → 01_OPERATING_RULES.md Phase 0 protocol
          → Phase 1 theory grounding
          → 12 (this file) wraps in CREATE/COVER
          │
          ▼
       PROMPT CONSTRUCTION
   │
   ▼
SELECT TEMPLATE
   │
   ├── Quick sketch? → ONE-SHOT (Section 2)
   │
   ├── Album / release? → CREATE/COVER PAIR (Section 1)
   │
   └── Multi-track series? → PERSONA WORKFLOW (Section 3)
   │
   ▼
GENRE RECIPE LOOKUP
   Pick from Section 4 (genre recipes) or build hybrid from
   Section 4 + `09_SUNO_ENGINE.md` § 6.
   │
   ▼
DRAFT LYRICS
   Apply `07_LYRIC_CRAFT_KOREAN.md` or `08_LYRIC_CRAFT_ENGLISH.md`.
   Apply tags from `10_SUNO_LYRICS_TAGS.md`.
   Apply microcues from `15_NATURAL_LANGUAGE_DIRECTION.md` § 7.
   │
   ▼
CONSTRUCT STYLE BOX (v2.6 Dense — 길이 동일, 내용만 다름)
   CREATE Style Box: Dense 700-950 chars (sketch 시 Tight 250-350).
   bone — genre, BPM, key, chord sketch, vocal 5-element, core
   instruments, melody char, structure cues. NO production/mix/
   atmosphere language (내용 혼입 0%). 700자 초과는 정상 밀도이지 누설 아님.
   COVER Style Box: Dense 700-950 chars (full texture — apply
   `09_SUNO_ENGINE.md` § 7 order template, vocal from
   `06_VOCAL_PRODUCTION.md`, production from `11_PRODUCTION_DESIGN.md`,
   scene-painting from `15` § 5, era anchor in first 200 chars,
   throughout-keywords for sections, Suno-hacking defaults from
   99_OPERATOR_VAULT Part F, anti-drift exclude.)
   Embed 3-5 Signature Moments from `13` § 4.2 (split: bone-level
   moments → CREATE, texture-level moments → COVER).
   Run 30% Rule check (09 § 3.5b) before delivery.
   │
   ▼
APPLY 99_OPERATOR_VAULT Part F VERIFIED TIPS (if 99 active)
   Cite which tips were applied:
   "(Applied: 99_OPERATOR_VAULT Part F.X, §7.Y)"
   │
   ▼
PRE-GENERATION GATE (10 checks)
   `09_SUNO_ENGINE.md` § 11.
   `14_PROSODY_AND_PHONETICS.md` § 5 prosody gate.
   │
   ▼
DELIVER PROMPT
   Format per `09_SUNO_ENGINE.md` § 12 with character count
   annotation `(count: NNN/1000)`.
   │
   ▼
USER GENERATES → REVIEW
   │
   ▼
ITERATE
   Apply Section 5 protocol.
   Use Section 6 diagnostic tree if issues.
   │
   ▼
LOCK
   Save best take as Persona.
   Crop, fade, finalize.
   │
   ▼
OPTIONAL: CASE LOG TO 99
   "이거 케이스로 로그할까?" → Generate add-block for 99_OPERATOR_VAULT Part G.
   Discover new Suno tip? → Propose add to 99_OPERATOR_VAULT Part F.
   │
   ▼
DELIVERED FINAL TRACK
```

---

## SECTION 8. QUICK-FILL OPERATOR CHECKLIST

When the operator wants a fast-turnaround prompt, fill these blanks
and the system generates:

```
1. Reference (track / artist / description) OR concept: ___________
2. Target genre (primary): ___________
3. Sub-style or era: ___________
4. Tempo (BPM): ___________
5. Key / mode: ___________
6. Vocal gender: ___________
7. Vocal voice type / range: ___________
8. Vocal language / accent: ___________
9. Vocal timbre (3 adjectives): ___________
10. Mood / atmosphere: ___________
11. Reference era / scene (no artist names): ___________
12. Special instruments to include: ___________
13. Signature moments to render (3-5): ___________
14. Things to exclude: ___________
15. Workflow: [One-Shot / CREATE-COVER / Persona]: ___________
16. Track length target: ___________
```

System ingests these answers, runs `13` if reference present,
selects appropriate Section 4 recipe (or builds hybrid), constructs
lyric draft, applies `15` direction, and delivers formatted prompt
with character count annotation.

---

## SECTION 9. REFERENCES

- HookGenius — copy-paste recipes by genre, 2026 prompt guide
- musci.io — 100+ Suno prompt examples
- naqashmunir21/awesome-suno-prompts (GitHub) — community prompts
- JackRighteous — best prompts guide and iteration workflow
- r/SunoAI — workflow deep-dives, v5.5 master prompt threads
- Suno official blog — Covers, Personas, Extend documentation
- roo.beehiiv.com — Suno AI Prompt Guide 2026 character limits
- openmusicprompt.com — 500+ verified metatags

---

## SECTION 10. RELATED FILES

- `09_SUNO_ENGINE.md` — engine rules, character limits, mode logic.
- `10_SUNO_LYRICS_TAGS.md` — bracket tag library.
- `06_VOCAL_PRODUCTION.md` — full vocal directive system.
- `11_PRODUCTION_DESIGN.md` — production architecture for COVER.
- `05_GENRE_LIBRARY.md` — per-genre theory backing recipes here.
- `01_OPERATING_RULES.md` — overall workflow and gate enforcement.
- `00_ROUTER.md` — file routing map.
- `13_REFERENCE_ANALYSIS.md` — produces 9 craft variables +
  Signature Moments that this file wraps.
- `14_PROSODY_AND_PHONETICS.md` — prosody validation gate before
  output.
- `15_NATURAL_LANGUAGE_DIRECTION.md` — vocabulary library that
  this file uses to construct Style Box and Lyrics Box.
- `99_PERSONAL_OPTIONAL.md` — operator-specific verified tips
  applied during construction (cited in output footer).

---

<!-- USER EXTENSION ZONE — append discovered templates / patterns below -->



---

## SECTION 11. 7-PART FORMULA TEMPLATE (NEW v2.7)

### 11.1 What 7-Part Formula is

External research (Suno Field Guide 2026 + community testing): the
most reliable Style Box formula across genres has 7 standardized
parts. v2.7 absorbs this as a default scaffold.

### 11.2 The 7 parts

1. **Genre anchor** (1-3 micro-genres + era)
2. **Tempo + Key** (BPM number + key/mode)
3. **Vocal directive** (gender, range, timbre, inflection)
4. **Lead instruments** (3-4 named, with descriptors)
5. **Production texture** (sonic qualities, era anchor)
6. **Mix / frequency architecture** (frequency separation, stereo)
7. **EXCLUDE list** (placed at very end)

### 11.3 Template (period-structured per 09 §30)

```
[1: Genre]. [2: Tempo + Key]. [3: Vocal]. [4: Lead instruments].
[5: Production texture]. [6: Mix architecture].
EXCLUDE: [7].
```

### 11.4 Filled example — K-Pop modern

```
Modern K-pop with Y2K bedroom-pop revival, 2024-2026 contemporary.
128 BPM, A minor with chromatic mediant lifts to F major.
Female alto vocal, smooth airy on verses, powerful belting on
chorus peaks, K-pop modern inflection. Layered analog synth pads,
chiming Rhodes electric piano, sidechain-pumping sub-bass,
brushed snare with rim-click accents. Y2K nostalgic warmth with
2026 modern crisp top end, occasional vinyl crackle texture,
analog tape saturation on master bus. Frequency separation: vocal
corridor 500Hz-3kHz protected, sub-bass mono 20-80Hz tight,
stereo width L40/R40 on synths preserved.
EXCLUDE: muddy mix, harsh digital sheen, robotic vocal autotune,
stadium reverb crowd.
```

### 11.5 Filled example — Indie folk

```
Indie folk singer-songwriter, late-2010s Phoebe Bridgers lineage,
2020s bedroom production.
85 BPM, D major with occasional borrowed iv minor color.
Female alto vocal, intimate close-mic conversational, vulnerable
confessional delivery, subtle vibrato narrow.
Fingerstyle nylon-string guitar, distant brushed drums,
upright bass plucked, ambient pad swell on choruses.
Warm analog tape saturation, room reflection medium-large,
slight tape hiss, no compression on lead vocal, natural breath
audible. Frequency separation: vocal forward, guitar L30/R30,
ambient pad spread wide L70/R70.
EXCLUDE: pop polish, autotune, modern radio production, electronic
drums.
```

### 11.6 Filled example — Hip-hop modern

```
Contemporary hip-hop, 2024-2026 alternative trap, Tyler the Creator
lineage with abstract instrumental palette.
75 BPM half-time (effective 150 trap), F# minor with chromatic
descending bass.
Male tenor rap-singing, conversational mumble verses, melodic hook
choruses, occasional auto-tune warble on emotional peaks.
808 sub-bass with sliding pitch, hi-hat rolls 32nd-note,
Rhodes electric piano chord stabs, vinyl-textured drum loop.
Lo-fi grit on drums, sub-bass mono and forward, vocal centered with
short slap delay 80ms. Tape saturation throughout, no full-stadium
reverb. Frequency separation: 808 mono 20-100Hz, hi-hat 8kHz-14kHz
crisp, vocal mid 500Hz-3kHz protected.
EXCLUDE: stadium reverb, modern Atlanta trap defaults, generic
EDM drop.
```

### 11.7 When to use 7-Part formula

- Operator hasn't specified a special pattern (default scaffold)
- New genre territory (need full coverage)
- Operator reports "Style Box not landing" (force complete structure)

### 11.8 When NOT to use

- Quick sketch / one-shot mode
- Style Box budget < 400 chars (drop parts 5, 6)
- Operator named a different pattern (09 §3.5g — Polarity Fusion,
  Substitution Map, etc.)

### 11.9 Compression strategy if over limit

If 7-Part fills > 1000 chars (Suno limit):
1. Part 5 (Production texture) → 2 keywords only
2. Part 6 (Mix) → 1 sentence only
3. Part 4 (Instruments) → 3 instruments, not 4
4. EXCLUDE → 3-4 items default (v2.11). Max 5-6 with 5-tier priority pruning (see 00 C-46)
5. If still over: drop Part 5 entirely, keep Part 6 frequency
   separation as critical

---

## SECTION 12. VERIFICATION TEMPLATES (NEW v2.7)

### 12.1 Why verification templates

Operator's recurring issue: Suno generates, output diverges from
intent, operator cannot diagnose why. Verification templates capture
*what to check* in known failure modes.

### 12.2 Pop Gravity Well verification

After generation, if output sounds *generic / pop-ified*:

```
DIAGNOSTIC TEMPLATE — POP GRAVITY WELL
======================================

Intended genre: [...]
Output genre detected: [...]
Pop-leaning elements heard:
  □ Standard 4-on-floor kick
  □ Reverb-washed atmosphere
  □ Polished vocal compression
  □ Modern radio mix
  □ Predictable chord progression

Remedy applied:
  □ Added EXCLUDE: pop, modern pop production
  □ Tried weird combination: [...]
  □ Strategic contrast: emphasize anti-pop element
```

### 12.3 Vocal Anchor verification

If vocal character is wrong:

```
DIAGNOSTIC TEMPLATE — VOCAL ANCHOR
==================================

Anchor text: [...]
Anchor position: [line 1? / lower?]
5-element check:
  □ Gender + range
  □ Main timbre
  □ Range-by-section behavior
  □ Genre inflection
  □ Special technique (optional)

Output vocal heard:
  Gender:  [...]
  Range:   [...]
  Timbre:  [...]

Mismatches: [...]
Remedy: [reduce anchor / add negation / Style Box reinforcement]
```

### 12.4 Lyric Bleed verification

If Style Box content appears in vocal:

```
DIAGNOSTIC TEMPLATE — LYRIC BLEED
=================================

Suspected leaked phrase: [what's being sung that shouldn't]
Source location:
  □ Style Box (line, character)
  □ Anchor (which element)
  □ Section marker text

Trigger pattern:
  □ Poetic sentence in Style Box
  □ ALL CAPS phrase in Style Box
  □ Quoted phrase in Style Box
  □ Natural prose in Style Box
  □ Empty Lyrics Box

Remedy applied:
  □ Style Box rewritten as technical/dense
  □ Lyrics Box filled
  □ //*****/// separator added
  □ Quotes removed
```

### 12.5 Pop Gravity Well prevention prompt

Embed before generation for high-risk genres:

```
PRE-GENERATION CHECK — POP GRAVITY WELL
========================================

Intended genre: [genre]
Distance from Pop (0-10):
  Rock         → 4 (high pull)
  Funk         → 3 (high pull)
  Emo          → 2 (very high pull)
  Metal        → 6 (moderate pull)
  Hip-hop      → 5 (moderate pull)
  Folk         → 7 (low pull)
  Orchestral   → 8 (low pull)

If distance < 5: MANDATORY EXCLUDE pop + use weird combination
If distance 5-7: Recommended EXCLUDE pop
If distance 8+: Optional
```

### 12.6 22-Item Gate verification (output-ready check)

Before any lyric output:

```
GATE CHECK — 22 ITEMS (14_PROSODY §7)

A. Phonetic (6):
  □ 1.  Syllable count fits BPM range
  □ 2.  받침 ratio (Korean) / consonant cluster density tempo-fit
  □ 3.  Long vowels on sustained notes
  □ 4.  No 3+ consonant clusters
  □ 5.  Vowel harmony (Korean mimetic)
  □ 6.  Pronunciation overrides applied

B. Prosodic (5):
  □ 7.  Stressed syllables on stressed beats (English)
  □ 8.  Word stress respected (Spanish, English)
  □ 9.  Pitch accent okay (Japanese key words)
  □ 10. Lyric phrase = melody phrase boundary
  □ 11. Stable/Unstable match section function

C. Semantic / Persona (5):
  □ 12. Persona consistent
  □ 13. Tense consistent (or intentional shift)
  □ 14. POV consistent (or intentional shift)
  □ 15. One-metaphor rule
  □ 16. Semantic field unified (5-6 fields)

D. Anti-Pattern (3):
  □ 17. No banned nouns (08 §6.2)
  □ 18. No banned phrases (08 §6.3)
  □ 19. No banned rhyme pairs (08 §6.4)

E. Craft Quality (3 — NEW v3.5):
  □ 20. Verb wattage audit, <30% weak verbs
  □ 21. AID applied to verses
  □ 22. Show > Tell ratio met

PASS: all 22  → ship
1-3 FAIL    → operator review
4+ FAIL     → return to 07/08
```

---




## SECTION 13. OUTPUT TEMPLATES (v2.10 — Inline Default + File Option)

### 13.0 v2.10 Philosophy Shift

v2.8까지: 6-파일 분리 출력 디폴트 → 다운로드 → 6개 파일 열기 → 복붙.
v2.10 반전: **인라인 6-블록 출력 디폴트** → 채팅에서 헤더 보고 → Suno
6개 칸에 바로 복붙.

이유:
- 인라인 = 채팅 한눈 검토 + 즉시 비교 / 수정 가능
- 파일 다운로드 = 단계 추가 + 검토 어려움 + 토큰 낭비
- Suno UI 자체가 6개 칸이라 영역만 명확하면 복붙 동선 동일

파일 모드는 운영자 명시 시만 옵션 (큰 곡 / 보관용 등).

---

### 13.1 인라인 6-블록 표준 포맷 (v2.10 DEFAULT)

곡 본작업 시 채팅 본문에 다음 포맷으로 출력:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎵 [곡명] v[N] — [한 줄 컨셉]
━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━ CREATE ━━━

📋 Style of Music — Suno "Style" 칸 ([NNN자])

[CREATE Style Box 풀바디 내용]


📋 Exclude Styles — Suno "Exclude" 칸 ([NN자])

[CREATE EXCLUDE 4-6개 콤마 분리]


📋 Lyrics — Suno "Lyrics" 칸 ([NNNN자])

[Vocal Anchor]
[가사 풀바디 — 섹션 태그 + 마이크로큐 + 가사 라인]


━━━ COVER ━━━

📋 Style of Music — Suno "Style" 칸 ([NNN자])

[COVER Style Box 풀바디 내용]


📋 Exclude Styles — Suno "Exclude" 칸 ([NN자])

[COVER EXCLUDE 4-6개 콤마 분리]


📋 Lyrics — Suno "Lyrics" 칸 ([NNNN자])

(CREATE와 동일)
또는
[COVER 전용 Lyrics 풀바디]

━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Gate 22/22 / 🔧 [보강] / 🔍 [진단]
📏 Style C/V [NNN/NNN자] · Lyrics [NNNN자] · Exclude [N/N개] · 곡 길이 [~M:SS]
━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 13.2 인라인 출력 발동 조건

**자동 발동 (default):**
- 곡 본작업 (Style Box + 가사 둘 다 작성하는 작업)
- 운영자 명시 우회 발화 없음

**파일 모드로 전환 (옵션):**
- 운영자 명시: "파일로 줘 / 다운로드 / .txt로 / 패키지로"
- 곡 매우 큼 (Lyrics 4,500자 + 운영자 검토 어렵다 신호)
- 운영자 "검토해야 해서 파일로" 발화

**부분 출력 (인라인 sub-set):**
- Style Box만 작성: 6-블록 중 Style 2개만 출력
- Lyrics만 작성: Lyrics 1개만 출력 (CREATE/COVER 구분 명시)
- 진단·수정 응답: 영향 받는 블록만

---

### 13.3 응답 본문 형식 (인라인 6-블록)

#### 13.3.1 첫 출력 (v[1])

```
[1줄 반응 또는 0줄]

━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎵 [곡명] v1 — [컨셉]
━━━━━━━━━━━━━━━━━━━━━━━━━━━

[6-블록 풀바디]

━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Gate 22/22
📏 Style 467/892자 · Lyrics 3,650자 · Exclude 4/4개 · 곡 길이 ~3:20
━━━━━━━━━━━━━━━━━━━━━━━━━━━

[필요 시 1-2줄 핵심 결정 메모]
```

#### 13.3.2 수정 출력 (v[N+1])

```
[변경 영역 1-2줄 요약]

━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎵 [곡명] v[N+1] — [변경 한 줄]
━━━━━━━━━━━━━━━━━━━━━━━━━━━

[6-블록 풀바디 — 복붙 편의성 유지]

━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Gate 22/22 / 🔧 [변경 보강 항목]
📏 [변경된 글자수]
━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

#### 13.3.3 부분 수정 (운영자 "X만 정리해")

```
[변경 1-2줄]

━━━ [영향 받는 블록만 헤더 + 풀바디] ━━━

[해당 블록 풀바디]

✅ [변경된 블록] 검증 1줄
```

---

### 13.4 파일 모드 (옵션)

운영자 명시 시 발동. 구조:

```
[곡명]_v[N]/
├── README.txt                  ← 곡 메타 + 복붙 가이드
├── create/
│   ├── 01_prompt.txt           ← Suno "Style of Music" 칸
│   ├── 02_exclude.txt          ← Suno "Exclude Styles" 칸
│   └── 03_lyrics.txt           ← Suno "Lyrics" 칸
└── cover/
    ├── 01_prompt.txt
    ├── 02_exclude.txt
    └── 03_lyrics.txt
```

#### 13.4.1 README.txt 표준 양식

```
[곡명] v[N] — Suno 복붙 패키지
================================

🎵 Title: [한국어 / 영어 병기]
🎯 Workflow: CREATE → 결과 듣고 → COVER (같은 가사 / 새 사운드)
⏱️ 예상 곡 길이: [M:SS]

📁 create/ — CREATE 단계 (멜로디 / 뼈대 / 보컬 코어)
  01_prompt.txt   → Suno "Style of Music" 칸 ([NNN자])
  02_exclude.txt  → Suno "Exclude Styles" 칸 ([NN자])
  03_lyrics.txt   → Suno "Lyrics" 칸 ([NNNN자])

📁 cover/ — COVER 단계 (사운드 텍스처 / 믹스 / 마스터)
  01_prompt.txt   → Suno "Style of Music" 칸 ([NNN자])
  02_exclude.txt  → Suno "Exclude Styles" 칸 ([NN자])
  03_lyrics.txt   → Suno "Lyrics" 칸 ([NNNN자])

📏 글자수 검증:
  Prompt 한도 1000자 / Lyrics 한도 5000자 / Exclude 4-6개
  모두 한도 안.

🔧 Notes (옵션):
  - [컨셉 한 줄]
  - [핵심 시그니처 1-2개]
```

#### 13.4.2 파일 모드 출력 워크플로우 (Claude 내부)

Step 1: bash로 파일 작성 (한 번에)
  - mkdir -p create / cover 디렉토리
  - bash cat heredoc으로 6개 파일 작성

Step 2: wc -c로 실측
  - 각 파일 글자수 검증

Step 3: outputs 폴더로 복사
  - mkdir /mnt/user-data/outputs/[song_name]_v[N]
  - cp -r 복사

Step 4: README.txt 작성

Step 5: present_files 호출 (7개 파일: README + create 3 + cover 3)

Step 6: 응답 본문 — 변경 영역 + 검증 1-2줄

---

### 13.5 가사 분량 매트릭스 (00 §C-3.1 연동)

곡 길이 → Lyrics 분량 추정 (v2.10):

| 곡 길이 | 권장 분량 | 사용 케이스 |
|---|---|---|
| 2:00-2:30 | 2,000-2,800자 | sketch / 인터루드 |
| 2:30-3:00 | 2,800-3,300자 | 미니 발라드 |
| **3:00-3:30** | **3,000-3,800자** | **표준 default** |
| 3:30-4:00 | 3,500-4,500자 | 정교한 작사 곡 |
| 4:00-4:30 | 4,200-4,800자 | 서사 곡 / 듀엣 |

**한도:**
- Hard: 5,000자
- Over-cued: 4,800자+ = 후반 가사 씹힘
- Under-cued: 2,500자 미만 = 보컬 러싱

**원칙:** 분량 ≠ 최저 목표. 곡 컨셉에 필요한 만큼이 1순위.
시스템이 Pre-Production Estimate (00 §C-39)에서 미리 추정 → 운영자 확인.

---

### 13.6 토큰 효율 비교 (v2.8 → v2.10)

| 항목 | v2.8 (파일 default) | v2.10 (인라인 default) |
|---|---|---|
| 응답 본문 토큰 | ~500-1000 (압축) | ~2500-3500 (풀바디) |
| 파일 생성 토큰 | ~1500 (bash + present_files) | 0 |
| 운영자 검토 동선 | 다운로드 → 파일 열기 → 복붙 | 채팅 → 복붙 |
| 검토 / 비교 용이성 | 어려움 (파일 6개 열어야) | 쉬움 (한눈에) |
| 토큰 합계 | ~2000-2500 | ~2500-3500 |

**핵심:** 토큰은 v2.10이 약간 더 쓰지만, 운영자 검토 시간 / 채팅 흐름
유지가 훨씬 좋음. 큰 곡이나 보관 필요 시만 파일 모드.

---

### 13.7 발동 분기 표

```
운영자 발화 → 본작업 진입
    ↓
명시 "파일로" / "다운로드" / "패키지로" 발화?
    ├── YES → 파일 모드 (§13.4)
    └── NO  → 인라인 6-블록 (§13.1) DEFAULT
```

---

## SECTION 14. STYLE BOX BUDGET TEMPLATE (v2.11 NEW)

This template implements 00 C-44 (Style Box budget) + C-45 (Position
weighting) for 1-shot writing — eliminates 8-9 compression rounds.

### 14.1 The budget worksheet (Dense Mode 955 chars target)

Fill BEFORE writing. Don't write full body then compress.

| Position | Part | Content | Char budget |
|---|---|---|---|
| **1 (50% weight)** | Part 1 — Genre anchor | Microgenre + era | 80-120 |
| 2 (25% weight) | Part 2 — Tempo + Key | BPM + Key/Mode | 60-90 |
| 3 (12.5% weight) | Part 3 — Vocal directive | 5-element open | 180-250 |
| 4-5 | Part 4 — Lead instruments | 3-4 instruments | 150-200 |
| 6 | Part 5 — Production texture (COVER) | Texture descriptors | 150-200 |
| 7 | Part 6 — Mix architecture (COVER) | Frequency architecture | 130-180 |
| 8 | Part 7 — Throughout discipline | Maintain phrase | 60-100 |
| — | **Total** | — | **810-1140 → 955 avg** |

### 14.2 Tight Mode budget (300 chars target)

| Position | Content | Char budget |
|---|---|---|
| 1 (50%) | Microgenre (1-2 words) | 60 |
| 2 (25%) | Era anchor | 30 |
| 3 (12.5%) | Vocal 1-line | 80 |
| 4-5 | Lead instrument 1-2 | 60 |
| 6+ | Signature trait 1 | 70 |
| — | **Total** | **300 ± 20** |

### 14.3 1-shot writing procedure

```
Step 1: Choose Tight (250-350) or Dense (700-950)
Step 2: Fill budget worksheet (§14.1 or §14.2)
Step 3: Plan Position 1-3 specifically (87.5% of weight)
Step 4: Write each Part ONCE within its char budget
Step 5: wc -c verification (single call)
Step 6: If over by 5%+: trim longest Part only
Step 7: Ship

Iteration cap: 2 (write + 1 trim)
If 3rd iteration needed → C-44 violation → operator report
```

### 14.4 Position 1-3 planning worksheet

| Position | Decision | Example (hardstyle) | Example (UK garage) |
|---|---|---|---|
| 1 | Strongest microgenre | "Festival mainstage hardstyle anthem" | "Modern UK 2-step garage" |
| 2 | Era / lineage | "late-2020s European club" | "2024 UKG revival" |
| 3 | Vocal/signature | "female mezzo belt crisp" | "PinkPantheress-era breathy" |

### 14.5 Common Position 1 mistakes (from Case 41)

- ❌ `"K-pop X"` → K-pop steals Position 1/2 (industry category)
- ❌ `"Pop electronic"` → genre cloud splits Position 1
- ❌ `"Beautiful emotional ballad"` → mood wastes Position 1
- ✅ Always microgenre + era as Position 1-2

### 14.6 Cross-reference

- 00 C-44 / C-45 / C-16.5
- 09 §37 / §38
- 10 §23

---

# END OF 12_PROMPT_TEMPLATES v2.11


## § USER EXTENSION ZONE v2.0 (2026-05-24)

SJY response-templates 풀바디. 18 RESPONSE_TEMPLATES 신규 파일이
17-type 라우팅의 본체.


### §UE-1. 18 RESPONSE_TEMPLATES 라우팅

```
운영자 발화 → Phase 0 → 17-type 매칭 (C-55) → 18 §[해당 type]
```


### §UE-2. Style Box Templates (Tight Mode 권장)

#### §UE-2.1 K-pop Girl Crush Template

```
Style (300자):
K-pop girl group, fierce EDM trap, sassy female vocals,
heavy bass drop, chant chorus, 135 BPM, confident attitude,
glossy production, mixed group vocals, [Korean-English bilingual]
```

#### §UE-2.2 K-pop Cute Template

```
Style (290자):
K-pop, bubblegum pop, bright synths, chirpy female vocals,
catchy hook, youthful energy, 125 BPM, layered harmonies,
mixed group vocals, glossy production
```

#### §UE-2.3 K-pop Ballad Template

```
Style (310자):
Korean ballad, emotional piano, string orchestra,
soaring female vocals, key change final chorus, 70 BPM,
cinematic, lush arrangement, intimate verse build
```

#### §UE-2.4 Indie Pop Template

```
Style (280자):
Indie pop, dreamy synths, breathy female vocal, 
intimate verse, 110 BPM, jangly guitar, soft drums,
nostalgic warmth, bedroom pop aesthetic
```

#### §UE-2.5 Modern Hip-Hop Template

```
Style (290자):
Modern hip-hop, trap beats, 808 sub bass, melodic male rap,
auto-tuned hook, 80 BPM, dark atmosphere, hi-hat rolls,
moody synths, polished production
```


### §UE-3. Lyrics Box Templates

#### §UE-3.1 K-pop Verse Template

```
[Vocal: female group, mixed harmonies, K-pop idol delivery]

[Intro]
(Short instrumental intro, 4 bars)

[Verse 1 - Korean]
사랑해 너를 향한 시선
[Singing: airy delivery, intimate]
멈출 수 없는 마음의 떨림

[Pre-Chorus]
[Singing: building, layered]
이제는 말할게 

[Chorus - English]
You're the one, you're the only one
(only one!)
Burning bright, my heart belongs to you
```

#### §UE-3.2 Solo Vocal Verse Template

```
[Vocal: female alto, smooth and soulful, breathy on quiet
lines powerful on peaks, contemporary R&B inflection,
slight vocal fry on phrase ends.]

[Intro]
(4 bar instrumental, piano + soft pad)

[Verse 1]
[Singing: hushed conversational]
Walking through *empty* streets tonight
[Pause half bar]
Wondering if you'd see the light

[Pre-Chorus]
[Singing: rising, breathy intensity]
But I still remember when

[Chorus]
[Singing: full belt, doubled vocals]
We were "young and free"
(yeah, free!)
```


# === END 12 USER EXTENSION ZONE v2.0 ===





# ============================================================
# § USER EXTENSION v2.0 FINAL v2 (2026-05-26)
# Suno 슬라이더 권장값 매트릭스
# C-83 정합
# ============================================================


## §UE-A. Suno 슬라이더 권장값 풀바디 매트릭스

**3개 슬라이더 (Suno V5/V5.5 공식)**:

```
1. Weirdness (0-100, default 50)
   - 음악적 모험 / 비일상 정도

2. Style Influence (0-100, default 50)
   - 스타일 prompt 적용 강도

3. Audio Influence (0-100, UI default 25 — COVER는 25에서 올림: lead 60-75 / texture 20-40)
   - Audio upload 시만 활성화
   - upload 음원 가이드 강도
```


## §UE-B. 곡 자리별 권장값

```
[Sketch / 탐색 단계]
Weirdness 50-60 / Style 40-50
→ Suno에게 자유 / 컨셉 발견 자리

[Polished 메인 작업]
Weirdness 40-50 / Style 70-80
→ 정밀 prompt / Suno 따라옴

[K-pop / Pop radio-safe]
Weirdness 35-45 / Style 70-85
→ 평균 회귀 + 정밀 lock

[Indie / Singer-songwriter]
Weirdness 45-55 / Style 55-70
→ 인디 자연 결 + 살짝 surprise

[R&B / Soul]
Weirdness 40-50 / Style 60-75
→ 그루브 + texture / 정밀 stilo

[Hip-Hop / Rap]
Weirdness 50-60 / Style 60-75
→ wordplay + 리듬 / 정밀 결

[Experimental / Avant-garde]
Weirdness 70-85 / Style 40-50
→ Suno 한계 밀어 / loose prompt

[Microtonal / Avant]
Weirdness 75-85 / Style 40-50
→ 비일상 음정 / 실험 결

[Cover (장르 점프)]
Weirdness 50-60 / Style 55-70
→ CREATE보다 약간 자유

[Bridge 실험 자리]
Weirdness 55-70 / Style 45-60
→ Verse/Chorus 대비 surprise

[Reference upload Lead]
Audio Influence 60-75
→ upload 음원 강한 가이드

[Reference upload Texture]
Audio Influence 20-40
→ upload 텍스처만 참고
```


## §UE-C. CREATE vs COVER 차등 결정

```
원칙: COVER = CREATE보다 ±5-10 변동 (다른 결 유도)

Polished K-pop (CREATE Polished + COVER 약간 변동):
- CREATE: W 40 / S 75
- COVER:  W 50 / S 65 (살짝 자유)

Experimental (CREATE 실험 + COVER 안정):
- CREATE: W 75 / S 45
- COVER:  W 60 / S 55 (radio-friendly)

Cover with upload:
- CREATE: W 45 / S 70 / A — (no upload)
- COVER:  W 50 / S 65 / A 70 (upload Lead)
```


## §UE-D. 자동 출력 의무 (모든 곡 작업)

```
모든 곡 본작업 응답 시 시스템 자동:

1. 곡 컨셉 / 장르 / 안전 vs 실험 결정
2. 매트릭스 매칭 (§UE-B)
3. CREATE / COVER 차등 결정 (§UE-C)
4. 7번째 블록 자동 출력 (C-83/C-84)

기본값 + Reasoning 명시:
🎛️ CREATE:
- Weirdness: 40 (Polished - K-indie 발라드, 안정 결)
- Style Influence: 75 (Tight - 정밀 prompt 락)
- Audio Influence: — (no upload)

🎛️ COVER:
- Weirdness: 50 (Balanced - 약간 자유)
- Style Influence: 65 (Tight - 정밀이지만 cover 결)
- Audio Influence: — (no upload)

🎛️ Reasoning: K-indie 발라드 → CREATE 정밀 락, COVER 살짝 자유 (다른 결)
```
