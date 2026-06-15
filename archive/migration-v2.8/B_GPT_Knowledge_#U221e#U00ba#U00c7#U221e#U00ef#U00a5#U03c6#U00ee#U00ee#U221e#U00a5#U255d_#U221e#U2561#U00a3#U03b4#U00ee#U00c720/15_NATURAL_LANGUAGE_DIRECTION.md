# 15. NATURAL LANGUAGE DIRECTION — Suno Prompt Expression Library
# Version: 1.0 (NEW in YUNY v2.0)
# Loads on: Whenever a Style Box or Lyrics Box is being constructed,
#           especially when Signature Moments from `13` need translation.
# Authority: This file is the vocabulary library for natural-language
#            direction. It supersedes the comma-separated descriptor
#            style of v1.x where richer expression is needed.

---

## SECTION 0. PURPOSE

Suno's Style Box accepts up to 1,000 characters and is parsed as natural
language with weighted token influence (front-loaded). Most v1.x prompts
used 400-600 characters of comma-separated descriptors and produced
average-of-genre output. This file shifts the prompt construction
philosophy:

**Old approach (v1.x):**
> "K-pop, 130 BPM, female vocal C4-F5, breathy timbre, conversational
> delivery, Korean, four-piece arrangement, polished modern mix."

**New approach (v2.0):**
> "Late-2020s K-indie pop at 130 BPM, the kind that opens with finger-
> picked acoustic and lets the room ambience breathe before the drums
> arrive. Female vocal C4-F5, breathy and conversational in the verses
> with chest dominance, lifting to a slightly airy mix on the chorus
> hook — never belted, just brighter. Korean lyrics with one English
> phrase landing on the chorus melodic peak. Verses sparse with acoustic
> + soft bass + brushed kit; chorus brings in a warm pad and a doubled
> guitar at +octave. The bridge drops to voice + acoustic only for four
> bars, then the band re-enters quietly under a held vocal note.
> Production sits late-2020s indie polish — controlled but not crushed,
> air shelf at 10kHz, plate reverb on the vocal at 12% wet on verses
> blooming to 25% on chorus." (count: 884/1000)

The natural-language approach (Dense Style Box, 700-950 chars)
paints a scene the engine can follow and explicitly directs
**moments** (where the chorus brightens, where the bridge drops,
what re-enters and how). The example above sits comfortably in the
v2.6 Dense zone. This directing applies to **both** boxes — CREATE
paints the *bone* (composition/arrangement/performance) in rich
natural language, COVER paints the *texture* (production/mix/space)
in rich natural language. Same length, different content layer.

This file provides the vocabulary library for that directing.

---

## SECTION 1. THE THREE LAYERS OF SUNO INSTRUCTION

Every Suno prompt operates on three instruction layers. Each layer
accepts different language types.

### Layer 1: Style Box — Natural-Language Production Direction
- Accepts: full sentences with descriptors weaving together
- Best for: scene-setting, mood, era, instrumentation, mix character,
  producer signatures (decomposed), section-level dynamic shifts
- **Character budget (v2.6 Dense):**
  - CREATE Style Box: Dense 700-950 chars (sketch 시 Tight 250-350).
    bone in natural language — genre, BPM, key, chord sketch, vocal
    5-element, core instruments, melody char, structure. NO
    production/mix/atmosphere language — that's COVER's layer (내용
    혼입 0%). 700자 초과는 정상 밀도이지 누설 아님.
  - COVER Style Box: Dense 700-950 chars (the full natural-language
    texture scene as taught in this file)
  - ONE-SHOT: 850-950 chars (CREATE bone + COVER texture fused)
- This file's vocabulary serves **both boxes** — CREATE for
  bone-level natural language, COVER/ONE-SHOT for texture-level.
  같은 길이, 다른 내용 층.

### Layer 2: Lyrics Box — Section Tags + Microcues + Lyric Content
- Accepts: bracketed structural tags + bracketed performance directions
  + parenthetical inline ad-libs + the lyric text itself
- Best for: per-section vocal direction, transitions, layering,
  pronunciation overrides, sudden silence cues, vocal register changes
- **Character budget (v2.1 default):**
  - 3:30+ tracks: 3,500-4,500 chars target
  - Under 2,500 = under-cued, vocal-rushing risk
  - Hard ceiling: ≤4,800 of 5,000

### Layer 3: Exclude Styles + Persona
- Accepts: short comma-separated descriptors (Exclude) or full vocal
  identity description (Persona)
- Best for: hard negation (Exclude) or vocal identity locking (Persona)

This file teaches the **vocabulary** for Layer 1 and Layer 2.

---

## SECTION 2. PER-SECTION [SINGING:] CUE LIBRARY

`[Singing:]` cues live in the Lyrics Box and direct vocal performance
for that section. One cue per section minimum.

### 2.1 Cue Construction Formula

```
[Singing: <texture>, <dynamics>, <phrasing>, <special technique if any>]
```

3-5 elements per cue. 10 words or less. Specific over abstract.

**Avoid abstract emotion words alone:**
- ❌ `[Singing: emotional]`
- ❌ `[Singing: soulful, with feeling]`
- ❌ `[Singing: heartfelt]`

**Use specific texture + dynamics + phrasing:**
- ✅ `[Singing: breathy verse, behind-beat phrasing, intimate close-mic]`
- ✅ `[Singing: chest-dominant, slight rasp on belted notes, forward-placed]`
- ✅ `[Singing: half-spoken vulnerable, slower delivery, breath audible]`

### 2.2 Cue Library by Section Function

#### Verse 1 (introduction, sparse)

```
[Singing: breathy verse, behind-beat phrasing, intimate close-mic feel]
[Singing: conversational mezzo, dry tone, no vibrato, observational distance]
[Singing: hushed lower register, head voice lean, narrow dynamic]
[Singing: speech-rhythm relaxed, mid-chest, slight uptalk on line ends]
[Singing: deadpan dry close-mic, slight vocal fry, no embellishment]
[Singing: airy soft introduction, restrained breath support, gentle approach]
```

#### Pre-Chorus (rising tension)

```
[Singing: building intensity, cadence tightening, fuller projection]
[Singing: breath quickens, slight push on phrase ends, anticipation rising]
[Singing: lifting toward chest mix, tightening from breath into tone]
[Singing: forward-placed urgency, step-by-step climbing in dynamic]
[Singing: tension hold, monotone tightening, barely raising volume]
```

#### Chorus (release, hook)

```
[Singing: chest mix on hook, controlled belt with slight rasp on peak notes]
[Singing: open vowel emphasis, brighter timbre, doubled lead on second phrase]
[Singing: anthemic forward projection, harmony +3rd entering bar 5]
[Singing: passionate chest-belt, no auto-tune residue, organic warmth]
[Singing: still light but brighter, no belt — proximity not power]
[Singing: half-time vocal phrasing over double-time band, behind beat]
```

#### Verse 2 (development, slightly fuller)

```
[Singing: same intimacy as V1 but slightly closer mic, +1dB presence]
[Singing: V1 phrasing maintained, subtle ad-lib breath on line 3]
[Singing: warmer texture than V1, head voice flip on bar 6]
```

#### Bridge (departure, contrast)

```
[Singing: stripped down to whisper, vocal alone for first two bars]
[Singing: half-spoken vulnerable, slower delivery, breath audible]
[Singing: raw confession, almost a quiet admission, melody minimal]
[Singing: detached observer voice, third-person posture, dry close-mic]
[Singing: belted edge with controlled rasp, climactic break]
```

#### Final Chorus (climax)

```
[Singing: full belt with controlled rasp, harmony +3rd +5th stack]
[Singing: chest dominance maximum, doubled lead, ad-libs on line ends]
[Singing: warmest of the song, slight tear in tone, organic close-mic]
[Singing: half-step modulation lift, vocal ascends with key change]
[Singing: still monotone but the warmest it gets all song]
```

#### Outro (resolution, fade)

```
[Singing: returning to intimate distance, vocal contracts to dry close-mic]
[Singing: breathy fade, last phrase trailing into silence]
[Singing: each repeat thinning out, final pass voice + single layer only]
[Singing: held final note, vibrato emerging slow, breath release at end]
```

### 2.3 Genre-Specific Cue Patterns

#### Hip-Hop / Trap

```
[Singing: melodic-rap delivery, half-spoken-half-sung, ad-libs throughout]
[Singing: tight on-grid flow, percussive consonants, slight pitch correction]
[Singing: triplet flow, behind-beat lay-back, hook stays melodic]
[Singing: deadpan UK-accent rap, no auto-tune, conversational lethal]
```

#### R&B / Neo-Soul

```
[Singing: melismatic ornaments at phrase ends, behind-the-beat phrasing]
[Singing: falsetto-heavy with breathy attack, melismatic chorus runs]
[Singing: smooth-warm with melismatic ornaments, controlled vibrato]
[Singing: D'Angelo-influenced laid-back, voice slightly behind grid]
```

#### Indie Folk

```
[Singing: half-whispered verses, fragile head-voice on chorus]
[Singing: conversational unpolished, off-mic ad-libs, tape wobble texture]
[Singing: room-mic ambience preserved, audible breath, no studio polish]
```

#### J-Pop

```
[Singing: bright clean Japanese articulation, melismatic phrase-ends]
[Singing: anime-influenced power belt with melismatic ornaments]
[Singing: city-pop soft delivery with breath-stops for emphasis]
```

#### Korean Modern

```
[Singing: late-2020s K-indie polished hush, vocal-forward intimate close-mic]
[Singing: 4th-gen K-pop airy unison + +3rd harmony, breathy with chest mix]
[Singing: K-ballad chest-belt with controlled rasp, vibrato on long notes]
```

### 2.4 Dynamic Within-Section Direction

Suno responds to dynamic direction within a single verse. Use sequential
cues:

```
[Verse 1]
[Singing: deadpan close-mic dry]
First two lines monotone observational.

[Singing: cadence tightens slightly]
Next two lines pull tighter.

[Singing: weight increases, still flat affect]
Last two lines slightly fuller but still flat.
```

This produces an internal arc within the verse without requiring full
section change.

---

## SECTION 3. SIGNATURE MOMENT TRANSLATION TABLE

This is the practical translation between the 9th craft variable
(Signature Moments from `13`) and Suno-readable instruction.

### 3.1 Vocal Register Transitions

| Signature Moment | Suno Translation |
|---|---|
| Verse 마지막에 head voice flip | Lyrics: `[Singing: last line lifts to head voice, breath release]` |
| Chorus에서 falsetto 진입 | Lyrics: `[Chorus] [Singing: falsetto entry on hook, light airy upper register, controlled not strained]` |
| Bridge에서 whisper로 떨어짐 | Lyrics: `[Bridge] [Stripped to whisper, vocal alone first two bars]` |
| Pre-chorus 마지막에 belt 진입 | Lyrics: `[Pre-Chorus end: vocal pushes into belted edge, controlled rasp]` |
| Final chorus key change up | Lyrics: `[Final Chorus: half-step modulation up, vocal ascends with key]` |
| Verse는 chest, chorus는 mix | Style Box: "verse stays chest-dominant intimate, chorus lifts into mixed register without breaking" |

### 3.2 Harmonic / Chord Shifts

| Signature Moment | Suno Translation |
|---|---|
| Bridge 코드 반음 점프 | Style Box: "bridge drops a half-step into [target key] — chromatic mediant landing, sudden floor-drop feel" |
| Chorus에 borrowed iv | Style Box: "chorus turnaround borrows the parallel minor iv chord — bittersweet pivot before returning to major" |
| Pre-chorus 코드 climbing | Style Box: "pre-chorus climbs through ii-iii-IV under a held vocal pedal, tension builds harmonically not dynamically" |
| Bridge stays static | Style Box: "bridge holds on a single chord for eight bars while the bass walks chromatically underneath" |
| Modulation final chorus | Lyrics Box: `[Final Chorus: KEY CHANGE UP HALF-STEP, full band maximum]` |

### 3.3 Density / Arrangement Shifts

| Signature Moment | Suno Translation |
|---|---|
| Bridge에서 모든 악기 빠짐 | Lyrics: `[Bridge] [Stripped to vocal + piano only, four bars]` |
| Chorus에서 layer 누적 | Lyrics: `[Chorus] [Doubled] [Harmony +3rd]` + Style Box: "chorus accumulates layers — doubled lead enters bar 1, +3rd harmony bar 5, +5th bar 9" |
| Outro layer 줄어듦 | Lyrics: `[Outro] [each repeat thinning out, final pass voice + single guitar]` |
| 갑자기 풀밴드 입장 | Lyrics: `[band: full ensemble entry on downbeat, no transition fill]` |
| Drum drop out V2 시작 | Lyrics: `[Verse 2] [Drums drop out, snaps only first four bars]` |

### 3.4 Silence / Transition Moments

| Signature Moment | Suno Translation |
|---|---|
| Chorus 진입 직전 0.5초 silence | Lyrics: `[Sudden Absolute Silence: 0.5 seconds full band cut]` |
| Bridge 직전 1마디 silence | Lyrics: `[Sudden Absolute Silence: 1 bar full band cut]` |
| 전형적 build-up 없는 진입 | Style Box: "no riser, no crash, no cymbal swell — chorus just begins" |
| Drum fill into chorus | Lyrics: `[end of pre-chorus: 2-bar drum fill into chorus]` |
| Half-bar dropout | Lyrics: `[half-bar dropout before chorus entry]` |

### 3.5 Processing / Effect Moments

| Signature Moment | Suno Translation |
|---|---|
| Verse dry, chorus wet | Style Box: "verses recorded dry close-mic, chorus opens into 2.5-second plate bloom — the room arrives only on the hook" |
| Outro reverb tail extends | Lyrics: `[Outro] [each repeat: reverb tail extends, vocal stays close-mic]` |
| Vocal double detune | Lyrics: `[Chorus second phrase: doubled lead +10 cent detune, no harmony stack]` |
| Tape stop into bridge | Lyrics: `[end of chorus 2: tape-stop effect into bridge]` |
| Final chord sustains | Lyrics: `[End: final chord sustains with reverb tail, slow fade over 4 bars]` |

### 3.6 Rhythmic / Tempo Moments

| Signature Moment | Suno Translation |
|---|---|
| Half-time chorus | Lyrics: `[Chorus] [Half-time feel]` + Style Box: "chorus drops to half-time perception, drums stay grid but feel 70 BPM" |
| Beat switch bridge | Lyrics: `[Bridge] [Beat switch: 4-on-floor to half-time]` |
| Triplet flow on bridge rap | Lyrics: `[Bridge] [Singing: triplet flow rap, on-grid precision]` |
| Stop-time bridge | Lyrics: `[Bridge: stop-time, band hits on 1 only, vocal in the silence]` |

---

## SECTION 4. VOCAL PROTECTION KEYWORDS

When the vocal range pushes Suno's reliability ceiling, protection
keywords stabilize the output. Apply automatically based on range.

### 4.1 Female Above F5

If chorus melody crosses F5 or any sustained note hits G5+:

Required keywords in Style Box:
```
sweet light airy upper register, warm natural human texture,
controlled breath support, no strain on top notes, crystal clear thin
```

These keywords reduce husky breakup and screech artifacts.

### 4.2 Male Above A4 (Falsetto Required)

If male vocal exceeds A4 in chest, specify falsetto explicitly:

Required keywords in Style Box:
```
controlled falsetto on upper register, sweet airy head voice,
not strained, smooth phonation, organic warmth on falsetto
```

### 4.3 Husky / Raspy Voice Stabilization

When the requested voice character is raspy, prevent degradation into
artifact distortion:

```
controlled rasp on belted notes only, smooth phonation in verse,
husky-tinted but supported, vintage analog tube warmth, organic
human texture
```

### 4.4 Robotic Output Prevention

When Suno's mix tendencies produce uncanny-valley vocal:

```
natural human breath, organic phrasing with microvariation,
audible breath between phrases, no auto-tune residue, warm
analog tube saturation on vocal bus
```

### 4.5 Anti-Drift Keywords (Exclude Styles field)

For frequently-misinterpreted negations:

```
auto-tune heavy, vocoder, robotic vocal, child voice,
accented Korean robotic, vocalized onomatopoeia spoken bam syllables,
crowd cheering stadium ambience, generic K-pop chorus belt
```

Place in Exclude Styles field, not Style Box.

---

## SECTION 5. NATURAL-LANGUAGE SCENE-PAINTING

For Style Box position 100-800 characters, paint a scene the engine can
follow. This is where the prompt budget gets spent productively.

### 5.1 Scene-Painting Anatomy

A good Style Box scene paragraph contains:

1. **Era anchor with scene specificity** (not just decade)
2. **What instrument arrives first and how** (intro setup)
3. **What the verse texture is** (instrumentation density)
4. **What changes at chorus** (the lift moment)
5. **What the bridge does differently** (departure)
6. **What the mix sits like overall** (production character)

Example breakdown:

```
[Era anchor]
Late-2010s East Coast bedroom indie folk, the kind that

[Intro setup]
opens with finger-picked acoustic and lets the room ambience
breathe before the drums arrive at bar 9.

[Verse texture]
Verses sparse — acoustic + soft bass + brushed kit, vocal
forward and dry close-mic, a single ambient pad sustaining
underneath barely audible.

[Chorus lift]
Chorus brings in a warm pad and a doubled acoustic guitar
at +octave; the lift comes from layering, not from drum
intensity.

[Bridge departure]
Bridge drops to voice + acoustic only for four bars, then the
band re-enters quietly under a held vocal note.

[Production sit]
Production sits late-2020s indie polish — controlled but not
crushed, air shelf at 10kHz, plate reverb on the vocal at
12% wet on verses blooming to 25% on chorus.
```

This 5-element scene paragraph runs 480 characters and gives the engine
specific moments to render.

### 5.2 Era Anchor Specificity

Vague era anchors fail. Specific era anchors lock production cluster.

| Vague (avoid) | Specific (use) |
|---|---|
| "vintage" | "late-1970s Philadelphia soul scene" |
| "old-school" | "early-1990s Tokyo city-pop revival" |
| "modern" | "late-2020s K-indie polished bedroom" |
| "retro" | "1985-1988 LA studio synth-funk" |
| "indie" | "mid-2010s Brooklyn DIY bedroom indie" |
| "hip-hop" | "2018-2020 Atlanta trap, post-808 era" |
| "ballad" | "early-2010s K-ballad cinematic-piano scene" |

### 5.3 Producer / Engineer Signature (Decomposed)

Direct producer names trigger Suno's filter. Decompose into descriptors.

**Andrew Scheps lineage:**
"warm bus-glue compression, mid-forward presence, controlled low-end,
vocal slightly forward in the mix"

**Jack Antonoff lineage:**
"reverb-soaked stadium-intimate hybrid, layered synth pads, vocal
processed with subtle plate, dynamic open verses to compressed chorus"

**Tom Elmhirst lineage:**
"vintage warmth, plate reverb, analog tape character, vocal with
controlled compression and slight tube saturation"

**MJ Cole lineage (UK Garage):**
"late-90s MJ Cole golden-era UK garage scene, jazz-house Rhodes pads,
2-step skip groove, vocal-chop foundations"

**Mura Masa lineage:**
"chopped vocal samples as percussion, bright plucks and supersaw stabs,
modern UK-inflected production"

### 5.4 Frequency Architecture in Plain Language

Instead of "mids: 500Hz-3kHz vocal corridor", write:

> "Vocal sits forward in the mids, instruments carved underneath
> to leave space — guitars and pads pulled back below 1kHz,
> air shelf above 8kHz untouched."

This is more readable AND more reliable in Suno parsing.

### 5.5 Dynamic Profile in Plain Language

Instead of "LUFS -8, DR 6":

> "Loud modern master with dynamic chorus drops — verses breathe at
> moderate density, choruses hit full but the limiter doesn't squash
> the transients."

### 5.6 Section Energy Map in Plain Language

Instead of structural tags only:

> "Verses at 30% energy, pre-chorus climbs to 60%, chorus opens to
> 85%, bridge drops back to 40% intentionally, final chorus reaches
> 100% with the half-step lift."

---

## SECTION 6. CHARACTER FILL STRATEGY (COVER / ONE-SHOT)

> **Note:** This fill strategy applies to **both Style Boxes**
> under v2.6 Dense (700-950) and **ONE-SHOT (850-950)**. The
> position map below is texture-oriented (COVER/ONE-SHOT); for a
> CREATE box, fill the same 700-950 budget with *bone* content
> (composition/arrangement/performance, no production language —
> 내용 혼입 0%) per `09_SUNO_ENGINE.md` § 3.5b and
> `12_PROMPT_TEMPLATES.md` § 1.1.

Old v1.x prompts ran 400-600 characters and left 400+ characters
of budget unused. v2.6 targets Dense 700-950 with the following
allocation:

### 6.1 Character Budget Template

```
Position 0-80   (80 chars):   Genre anchor + tempo + key + core vocal
Position 80-300 (220 chars):  Scene-painting paragraph (era + instruments + texture)
Position 300-600 (300 chars): Section dynamics (verse-chorus-bridge contrast)
Position 600-800 (200 chars): Signature moments (2-3 specific events)
Position 800-950 (150 chars): Production / mix character + protection keywords
Position 950-1000 (50 chars): SAFETY BUFFER, leave empty
```

This produces a Style Box of approximately 880-920 characters that
covers all 9 craft variables with specific direction.

### 6.2 What NOT to Cut When Compressing

If budget exceeds 950, compress in this priority order:

**Cut first (low priority):**
- Atmospheric mood adjectives (dreamy / nostalgic / wistful)
- Texture seasoning ("with subtle vinyl crackle" type details)
- Stereo image specifics (in CREATE only; preserve in COVER)
- Optional reference encoding (if using Persona-locked)

**Cut last / never (high priority):**
- Genre anchor (position 0-30)
- BPM, key
- Vocal 5-element directive
- Era anchor specificity
- Signature moments (the 9th craft variable)

### 6.3 Common Failure: "Tag Soup"

Old approach often produced tag soup:
> "K-pop, modern, polished, female vocal, breathy, airy, sweet,
> light, crystal clear, warm, intimate, conversational, English
> chorus hook, Korean verses, 130 BPM, F major, four-piece, synth
> pads, light drums, sub-bass, polished mix, wide stereo, late
> 2020s, K-indie influence, bedroom feel, modern production..."

This is 250+ characters but conveys very little. The engine sees
adjective stacking and produces averaged output.

The same content as natural-language scene:

> "Late-2020s polished K-pop crossing into K-indie bedroom feel.
> 130 BPM, F major. Female vocal C4-F5: breathy and conversational
> in Korean verses, airy crystal-clear on the English chorus hook,
> never crossing into belt. Verse arrangement is light — soft kit,
> sub-bass, sustained pad, single plucked acoustic. Chorus brings in
> a layered synth + doubled vocal hook, but stays at moderate density.
> Wide stereo image with vocal centered."

This is 480 characters but conveys far more direction. The engine
sees a scene with specific instructions.

---

## SECTION 7. INLINE LYRIC DIRECTION

The Lyrics Box is not just for lyrics. Direction lives inline.

### 7.1 The Asterisk Punch-In

Suno renders `*word*` as an in-place vocal stress punch.

Use case: emphasizing a single word in the line that should hit harder
than the surrounding syllables.

```
You called it once, you called it *twice*
[Pre-Chorus]
*Three* times you called and I ain't blink
```

Limit: 2-4 per verse. Over-use desensitizes.

### 7.2 Quoted Phrase as External Voice

`"phrase"` quotes are rendered as a slight tonal shift, often
declarative or quoted speech.

```
And you said "I'm not enough"
"Not enough" for what, exactly?
```

Use for self-quotation, world's voice quoted back, or rhetorical
declaration.

### 7.3 Inline Whisper

`(whisper: phrase)` produces an actual whispered ad-lib.

```
And you smile back (whisper: but you're already gone)
```

Combine with `[Sudden Absolute Silence]` for maximum effect — band
drops, then whisper appears in the gap.

### 7.4 Inline Ad-Libs

`(ad-lib syllable)` placed at line end produces a sung interjection.

```
I'll keep walking forward (yeah)
The rain just keeps falling (oh)
```

Genre-typical ad-lib syllables:
- Pop / R&B: yeah, oh, mmm, woo, ay
- Hip-hop / trap: yuh, skrrt, ay, let's go, uh
- Soul / gospel: oh, mmm, yes, Lord
- K-pop: ay, oh, woo, na na, la la

### 7.5 The Sudden Absolute Silence

The strongest dramatic device available in Suno.

```
[Pre-Chorus]
This time I won't —

[Sudden Absolute Silence: 0.5 seconds full band cut]

[Chorus]
This time I won't break.
```

Variants:
- `[Sudden Absolute Silence: 0.3 seconds]` — mid-line stagger
- `[Sudden Absolute Silence: 0.5 seconds full band cut]` — chorus entry
- `[Sudden Absolute Silence: 1 bar full band cut]` — bridge entry
- `[Sudden Absolute Silence: 2 bars]` — pre-final-chorus build

### 7.6 Pause Markers

For breath control in dense lyric sections:

- `[Pause half bar]` — short breath between lines
- `[Pause 1 bar]` — longer breath, section internal
- `[Pause 2 bars]` — bridge stillness or outro decay

### 7.7 Section-Internal Layer Direction

Layer specifications can change within a single section:

```
[Chorus]
[Singing: solo lead]
First two lines — solo lead only.

[Doubled enters]
[Singing: doubled lead]
Next two lines — doubled lead.

[Harmony +3rd enters]
[Doubled] [Harmony +3rd]
Final four lines — doubled with harmony stack.
```

This produces the "layer accumulation" Signature Moment from `13` § 4.2.

---

## SECTION 8. CODE-SWITCHING DIRECTION

For multilingual lyrics, position-based direction.

### 8.1 Line-Level Switching (K-pop standard)

```
[Verse]
밤이 깊어지면 너는 어디에
어둠 속에서 너를 찾아 헤매

[Chorus]
[Pronunciation: English]
Lost in the night, I'm calling your name
```

Place `[Pronunciation: English]` before each language-switched section
to lock pronunciation.

### 8.2 Phrase-Level Switching (HANA / global crossover)

```
ただ — everything else just tastes plain now
It still got me — どうしようもないな
```

Within-line switching mid-phrase. Suno generally handles this if the
phrase boundary is at a natural musical phrase boundary (caesura).

### 8.3 Word-Level Mixing (loanword)

```
(됐어, no — keep going)
(잠깐, wait)
(아 mute it)
```

Treat embedded loanwords as natural Korean speech. No special
direction needed unless pronunciation is ambiguous.

### 8.4 Hidden Korean in Global Track

The "잠깐의 잡념" hidden-Korean technique (`99` §1.8 lineage):

```
[Bridge]
[Stripped, vulnerable]
(됐어, no — keep going)
Push through, one more mile
[Sudden Absolute Silence: 0.5 seconds]
```

One Korean phrase as a brief private thought in an otherwise English
track. Effective for global tracks that want operator's signature
without breaking ear-friendliness.

---

## SECTION 9. THE ANTI-PATTERN CATALOG

Common failure modes and their fixes.

### 9.1 Over-Comma'd Tag Soup

**Symptom:** Style Box is just a list of adjectives, engine produces
generic average.

**Fix:** Convert to scene-painting paragraph (Section 5).

### 9.2 Negation Inside Style Box

**Symptom:** "not too heavy" produces heavy. "without auto-tune"
produces auto-tune.

**Fix:** Move all negations to Exclude Styles field (Section 4.5).

### 9.3 Vague Era / Producer Reference

**Symptom:** "vintage" / "modern" / "polished" produce engine-default
average.

**Fix:** Specific decade + region + scene (Section 5.2).

### 9.4 Direct Artist Name (v2.1 — try first, fallback after)

**Symptom:** Suno filter blocks or returns generic distorted output.

**v2.1 policy:** Direct artist names are **tried first** (per
system instruction C-1 + 09 §5.3b). Many names pass the filter
(verified: Mrs. GREEN APPLE, YOASOBI, Tatsuro Yamashita,
PinkPantheress era, Charli XCX Brat era, etc.).

**Fix only if Suno actually blocks/distorts:** fall back to
Decomposed Signature (Section 5.3, also `09` §5.3a).

Song titles default to Decomposed (higher filter risk than
artist names).

### 9.5 Under-cued Style Box (under 700 chars)

**Symptom:** engine improvises freely, output drifts from intent.
Applies to either box below the Dense floor (638자 = 부실/누락 신호).

**Fix:** Fill to Dense 700-950. COVER → scene paragraph + Signature
Moments (Section 6). CREATE → bone content (composition/arrangement/
performance, no production leak — 내용 혼입 0%). 같은 길이, 다른 내용 층.

### 9.6 Onomatopoeia in Lyrics

**Symptom:** `(Bam!)` rendered as the singer literally saying "bam".

**Fix:** Move to Style Box as instrument direction:
"hard punchy syncopated brass stab on hook downbeat"

### 9.7 Stadium / Crowd Reverb Drift

**Symptom:** "stadium reverb" or "live energy" triggers crowd cheering
in output.

**Fix:** Specify "studio recording clean isolated" + Exclude
"crowd cheering, live audience, stadium ambience".

### 9.8 K-Pop Trigger When Korean Lyrics Used

**Symptom:** Korean lyrics auto-pull into 4th-gen K-pop production
even when intent is K-indie or K-ballad.

**Fix:** Explicit alternative scene anchor + Exclude "K-pop, idol,
generic K-pop chorus belt".

### 9.9 [Intro] Tag Producing Strange Result

**Symptom:** Bare `[Intro]` produces bizarre instrumental opening or
is ignored.

**Fix:** Specify intro type:
- `[Short Instrumental Intro: 4 bars]`
- `[Vocal Intro: voice only first 2 bars]`
- `[Atmospheric Intro: pad and ambience, 4 bars]`

### 9.10 Final Chorus Identity Drift

**Symptom:** First chorus locks to intended scene, but final chorus
reverts to engine default.

**Fix:** Include "throughout / maintained" keywords in Style Box:
"vogue ballroom architecture maintained throughout all sections,
finger snap + clap preserved through outro"

### 9.11 Under-Cued Lyrics Box (Vocal Rushing)

**Symptom:** Vocals pour out too fast, singer doesn't breathe,
lyrics feel rushed despite correct BPM.

**Root cause:** Lyrics Box under-utilized. Without explicit timing
cues (bar counts, [Singing:] direction, breath tags), Suno
compresses sections and rushes through lyrics.

**Density target:** A 3:30 track Lyrics Box should run
3,500-4,500 characters (whitespace inclusive) when properly
micro-cued. Below 2,500 characters = under-cued.

**Fix checklist:**
1. Add bar counts to every section tag: `[Verse 1 16]` not
   `[Verse 1]`.
2. Add `[Singing:]` cue to every vocal section (minimum 1,
   sections 12+ bars get 2).
3. Insert `[Pause half bar]` or `[Half-bar dropout]` between
   dense lyric lines.
4. For English-heavy verses with high syllable density:
   `[One line per 2 bars, full breath between every line]`
5. Verify Style Box first-80 doesn't include "rapid", "rushed",
   "fast-paced" — replace with "spaced", "patient",
   "behind-the-beat".

**Mandatory microcue toolkit (apply by default, not on request):**
- Section bar count anchoring on every section tag
- `[Singing:]` cue per section with internal variation for 12+ bar
  sections
- `*word*` stress punch-in: 2-4 per verse on key words
- `"word"` quoted shouts for self-quotes and callouts
- `(whisper: ...)` at line-end after silence cues
- Inline ad-libs `(yeah)` `(oh baby)` always at line-end, NEVER
  on independent lines (causes serial dispersion)
- Breath/pause tags with explicit duration: `[Pause half bar]`,
  `[Pause 1 bar]`, `[Sudden Absolute Silence: 0.5 seconds full
  band cut]` — unit-less `[Pause]` / `[Hold]` NOT verified
- Layering directives at section open: `[Doubled]`,
  `[Harmony +3rd]`, `[Stacked vocals]`

### 9.12 Late-Section Identity Drift (Final Chorus / Outro)

**Symptom:** First chorus matches intended scene, but final chorus
and outro revert to engine default. Signature instruments disappear
or simplify.

**Root cause:** Suno's generation model loses prompt specificity in
later sections. Without reinforcement keywords, the engine relaxes
toward genre average.

**Fix (mandatory for every COVER):**
1. Style Box must include at least one "throughout / maintained"
   construction:
   - "X architecture maintained throughout all sections including
     final chorus and outro"
   - "[signature element] preserved through outro, never released"
2. Final Chorus and Outro Lyrics Box sections must carry the SAME
   microcue density as Verse 1 — not fewer tags just because it's
   the end.
3. Add `[<signature instrument> ride continues through fade]` in
   Outro section.
4. If drift persists after re-generation, use Replace Section on
   Outro only.


---

## SECTION 10. INTEGRATION WITH 13 (REFERENCE ANALYSIS)

This file is the destination for the 9th craft variable produced by
`13`. The flow:

```
13 captures Signature Moments in natural language
    │
    ▼
13 §4.2 translates each Moment via the lookup table
    │
    ▼
15 § 3 (this file) provides the actual Suno-readable instruction
    │
    ▼
15 § 5 weaves them into a Style Box scene paragraph
    │
    ▼
15 § 7 places relevant moments inline in Lyrics Box
    │
    ▼
12_PROMPT_TEMPLATES.md v2.0 wraps this in CREATE/COVER format
    │
    ▼
14_PROSODY_AND_PHONETICS.md validates singability
    │
    ▼
09 § 11 Pre-Generation Gate validates engine constraints
    │
    ▼
Output to operator
```

---

## SECTION 11. RELATED FILES

- `13_REFERENCE_ANALYSIS.md` — produces Signature Moments that this
  file translates
- `12_PROMPT_TEMPLATES.md` — wraps the natural-language direction into
  CREATE/COVER prompt structure
- `10_SUNO_LYRICS_TAGS.md` — the bracketed tag library this file
  builds on
- `09_SUNO_ENGINE.md` — engine constraints, Decomposed Signature §5,
  hybrid §6, 10-Gate §11
- `06_VOCAL_PRODUCTION.md` — full vocal directive system
- `14_PROSODY_AND_PHONETICS.md` — prosody validation gate
- `99_PERSONAL_OPTIONAL.md` — operator-specific verified microcues
  and signature direction patterns (loaded as TIPS, not authority)

---

## VERSION

현행 시스템 버전 기준. Style Box = 양쪽 박스 Dense 700-950(sketch Tight 250-350),
CREATE↔COVER는 내용(bone↔texture)만 다름. 글자수 `wc -m`. 상세 이력은 CHANGELOG.txt.

---

## SECTION 12 — Microtonal Direction Bank (NEW v2.2 / 회의록 직격)

03 파일 §10-12에서 정립된 미분음·디튠·의도된 불협 이론을
Suno 프롬프트 어법으로 변환. 회의록(2026-05-08) 직접 트리거.

### 12.1 Subtle Organic Detune (검증된 어법)

라이브 악기적 풍성함 = 정확하지 않은 튜닝의 효과.
모든 비-드럼 악기에 ±5-10 cents 디튠 적용 시 organic 느낌.

**Suno Style Box 어법**:
```
"natural detuning organic ±5-10 cents on all melodic instruments"
"live-feel detune analog warmth, not perfect tuning"
"organic instrument tuning slightly off-grid like live recording"
"subtle pitch variations natural human performance feel"
```

**악기별 적용**:
```
"acoustic guitar with subtle string detune ±5 cents"
"brass section natural intonation drift ±8 cents on solo lines"
"strings warm vibrato with ±10 cent pitch variation"
"vocal lead organic pitch sway ±7 cents not pitch-corrected"
```

### 12.2 Vocal Doubling Detune (Case 검증)

**검증된 정확한 cent 값**:

```
"doubled lead vocal +10 cent detune L20/R20" (Case 24 검증)
"doubled lead +12 cent detune second phrase only" (Case 22)
"doubled lead +15 cent organic width" (Case 23)
"triple-tracked vocal: center + +10 cent right + -10 cent left" (모던 팝 표준)
```

**Cent 범위별 효과**:
- ±5-8 cents: 미세, 거의 인지 불가, 자연스러운 두께
- ±10-15 cents: 풍성한 organic width, 모던 팝 표준
- ±20-30 cents: 명확한 chorus 효과, 80s 어법
- ±40-50 cents: quarter-tone 영역, 의도된 텐션

### 12.3 Synth Detune (Supersaw 본질)

```
"supersaw with 7 voices ±15 cent detune spread"
"analog synth pad ±10 cent oscillator detune for warmth"
"detuned synth lead organic vibrato ±12 cents"
"two synth oscillators detuned +10 cents creating beating texture"
```

### 12.4 Quarter-Tone Color (24-EDO 부분 적용)

```
"quarter-tone bend on lead synth solo only"
"vocal melisma with quarter-tone passing notes Maqam-influenced"
"lead guitar bends through quarter-tone microtonal blue notes"
"synth lead with subtle quarter-tone slides between main notes"
```

**Lyrics Box inline cue (검증된 실전 어법)**:
```
[Verse]
가사 라인 (quarter-tone up)
다음 라인 (quarter-tone down)

[Chorus]
[Singing: melismatic with quarter-tone ornaments]
가사...
```

### 12.5 Whole-Track Xenharmonic (곡 전체 미분음)

```
"experimental microtonal composition in 24-EDO tuning"
"22-EDO xenharmonic harmonic palette throughout"
"non-Western microtonal scale, Maqam Bayati influenced"
"Korean traditional microtonal ornaments throughout, sigimsae bending"
"xenharmonic synth lead playing 24-EDO scales"
```

**Genre + Microtonal 조합**:
```
"experimental microtonal ambient with quarter-tone drones"
"microtonal jazz fusion 24-EDO horn voicings"
"Korean traditional inspired microtonal pop, gugak-influenced"
"Middle Eastern fusion with Maqam half-flat 2nd and 6th degrees"
"avant-garde microtonal composition, Harry Partch-influenced"
```

### 12.6 Intentional Dissonance (의도된 불협)

회의록 어법: "더블 기타인데 각각 다른 코드로 연주."

**Bitonal Doubling**:
```
"two guitars bitonal layering: rhythm guitar in C major,
lead guitar in Bb major creating parallel motion friction"

"guitar pair: left guitar plays C major triads,
right guitar plays F# major triads tritone polychord"

"two guitars one chord apart: rhythm I chord,
lead always IV chord, perpetual suspension"
```

**Cluster / Polychord**:
```
"polychord D major over C major bass tense layered harmony"
"cluster voicing 2-3 semitone friction on chorus climax only"
"upper voices D major triad, lower voices C major triad,
Stravinsky Petrushka-style polychord"
```

**Detuned Unison Phasing**:
```
"unison melody two instruments: piano standard,
synth -15 cents, intentional phasing texture"

"vocal doubled with second voice -25 cents,
psychedelic disorientation effect"
```

### 12.7 Live Instrument Simulation (organic feel)

비-라이브 악기에 라이브 풍성함 부여:

```
"VST instruments humanized: subtle pitch variations,
timing micro-shifts, velocity differences mimicking real players"

"sampled instruments with organic detune ±7 cents,
breath sounds between phrases, finger noise on guitar"

"electronic instruments NOT perfect tuning,
analog tape machine drift effect, slight wow and flutter"
```

### 12.8 Microtonal 사용 결정 트리 (Style Box 작성 시)

```
미분음 적용?
   │
   ├── 곡 전체에 이질적 색채? → §12.5 Whole-Track Xenharmonic
   │      → 첫 80자에 "experimental microtonal" 명시
   │      → 24-EDO / 22-EDO 시스템 specify
   │
   ├── 부분 색채만? → §12.4 Quarter-Tone Color
   │      → 특정 섹션·악기·라인만 quarter-tone
   │      → Lyrics Box inline cue (quarter-tone up/down)
   │
   ├── 라이브 풍성함? → §12.1-12.2 Organic Detune
   │      → ±5-10 cents 모든 melodic 악기
   │      → 보컬 더블 ±10-15 cents
   │
   ├── 두 악기 의도 충돌? → §12.6 Bitonal / Polychord
   │      → 정확한 두 키 명시
   │      → "intentional friction" 키워드 동반
   │
   └── 신스 organic화? → §12.3 Synth Detune
         → ±10-15 cents oscillator detune
         → "analog warmth" 동반 키워드
```

### 12.9 Microtonal Anti-Patterns (사용 시 주의)

**A. 너무 강한 미분음 → 듣기 거북함**
- 50+ cents 디튠을 모든 악기에 적용 시 mass-listening 어려움
- 처방: 곡 전체는 ±15 cents 이내, quarter-tone은 솔로/특정 라인만

**B. K-pop / Modern Pop에서 강한 미분음 → 장르 정체성 깨짐**
- "experimental microtonal" 키워드는 K-pop 디폴트와 충돌
- 처방: subtle organic detune (±5-10) + 명확한 장르 anchor 유지

**C. Suno의 평균율 편향 무시**
- Suno는 12-TET 학습 분포가 압도적
- 처방: 전체 미분음은 "experimental" / "avant-garde" / "Korean traditional"
  같은 미분음 친화 장르 anchor와 결합 필수

**D. Lyrics Box (quarter-tone up/down) cue 남용**
- 매 줄에 박으면 vocal pitch unstable
- 처방: 곡당 2-4회, 의도된 모먼트만

---

## SECTION 13 — Harmonic Direction Bank (NEW v2.2)

03 파일 §11에서 정립된 화성 다양성 어법을 Suno Style Box /
Lyrics Box 키워드로 변환. 회의록 Q2 직격 보강.

### 13.1 Section-by-Section Progression Notation

**원칙**: 섹션별 코드 진행을 분리 명시. 단일 키 표기 금지.

**Pattern A — 섹션별 코드 진행 직접 명시**:
```
"verse Em-C-G-D, pre-chorus Am-Bm-C-D climbing,
chorus Em-C-Eb-G-D with chromatic mediant Eb,
bridge stripped Am-G-F, final chorus same as chorus +
half-step modulation up to Fm"
```

**Pattern B — Roman Numeral + 키 동시 명시**:
```
"in C major: verse I-vi-IV-V, pre-chorus ii-iii-IV-V climb,
chorus I-vi-bIII-IV with borrowed bIII modal mixture"
```

**Pattern C — 코드 변형 텍스트 어법**:
```
"verse uses jazzy maj7 voicings,
pre-chorus introduces secondary dominant V/vi,
chorus drops to parallel minor for bittersweet color,
bridge climbs through chromatic mediants"
```

### 13.2 Borrowed Chord (모달 인터체인지)

```
"borrowed iv chord [Fm in C major] in chorus turnaround"
"parallel minor borrow on pre-chorus climb"
"bittersweet bVI lift before final chorus [Ab in C major]"
"Aeolian borrow in bridge, returning to Ionian on chorus"
"Mixolydian bVII borrow throughout for rock-anthem feel"
```

**검증된 효과**:
- iv (Fm in C): 가장 흔한 bittersweet borrow, 케이스 22 검증
- bVI (Ab in C): epic minor 색채
- bVII (Bb in C): rock anthem / Mixolydian 어법
- bIII (Eb in C): Aeolian 색채, Case 23 검증

### 13.3 Chromatic Mediant

```
"chromatic mediant up major-third [C major to E major]"
"chromatic mediant down minor-third [C major to A major]"
"floor-drop chromatic mediant landing on chorus hook"
"sudden modal shift via chromatic mediant Eb in C major progression"
"two chromatic mediants in bridge: C → E → Ab → C cycle"
```

**Case 검증 어법**:
- Case 23 "그냥 그런 거지": "chromatic mediant B major to G major
  sudden chord jump" — 시니컬 floor-drop 효과
- Case 27 "グッバイ・サクラ": "Cmaj7 chromatic mediant single
  accent in chorus" — 단짠 모먼트

### 13.4 Secondary Dominant

```
"secondary dominant V/vi [E7 leading to Am]"
"V/V applied dominant on pre-chorus climb"
"chain of secondary dominants: V/ii → V/V → V → I"
"V/vi appearing on chorus turnaround for emotional lift"
```

**위치별 권장**:
- Pre-chorus 마지막 마디: V/V (climb 직격)
- Chorus turnaround (8th bar): V/vi (deceptive 색채)
- Bridge 진입: V/iii (낯선 시작)

### 13.5 Modulation (전조)

```
"half-step modulation up to F# major final chorus"
"whole-step modulation up to G major final chorus"
"truck-driver modulation no pivot direct lift"
"pivot chord modulation through Am common to both keys"
"common-tone modulation: C held, transitioning to E major"
"chromatic modulation via German +6 enharmonic pivot"
```

**Lyrics Box 동반 태그**:
```
[Final Chorus]
[Key Change up half-step to F major]
[Singing: belted with modulation lift]
가사...
```

### 13.6 Polychord / Bitonal

```
"polychord D major over C major bass [Petrushka-style tension]"
"bitonal layering: piano right hand in F#, left hand in C"
"upper voices D major triad, lower voices Bb major triad,
modern jazz polychord"
"two guitars different keys creating intentional friction"
```

### 13.7 Quartal / Quintal Voicings

```
"quartal piano voicings stacked perfect fourths"
"McCoy Tyner-style quartal comping modal jazz"
"open quartal harmony floating above sustained bass"
"quintal voicings perfect fifths stacked, ambiguous color"
```

### 13.8 Modal Vamps (정통 모달)

```
"Dorian vamp i-IV [Cm-F] cool minor jazz feel"
"Mixolydian vamp I-bVII [G-F] rock anthem"
"Phrygian vamp i-bII [Em-F] flamenco-metal tension"
"Lydian vamp I-II/I [F-G/F] dreamy floating"
"Aeolian vamp i-bVI-bVII gothic minor"
```

### 13.9 Static Harmony (의도된 정체)

```
"single chord vamp 8 bars Em9 with melodic variation"
"pedal point on tonic D, upper voices shifting freely"
"drone-based harmony over A pedal throughout verse"
"static i chord with bass line moving chromatically underneath"
"modal stasis on Cmaj7#11, ambient floating"
```

### 13.10 Verse-Chorus Harmonic Differentiation Patterns

회의록: "Verse에서는 어떻게 가다가 Chorus에서는 변경이 있고."

**Pattern A — Diatonic Verse → Modal Chorus**:
```
"verse stays diatonic in C major Cmaj7-Am7-Fmaj7-G7,
chorus breaks into Aeolian Cm-Ab-Eb-Bb borrowed from parallel minor"
```

**Pattern B — Static Verse → Movement Chorus**:
```
"verse single chord vamp Em9 with melodic variation,
chorus opens to full progression Em-C-G-D"
```

**Pattern C — Triadic Verse → Extended Chorus**:
```
"verse simple triadic C-G-Am-F,
chorus 9th-loaded jazz palette Cmaj9-Em7-Fmaj9-G7sus4"
```

**Pattern D — Diatonic Verse → Chromatic Pre-Chorus → Resolved Chorus**:
```
"verse diatonic Em-C-G-D,
pre-chorus chromatic climb Am-Bm-C-D-D#dim,
chorus tension release Em-G-D-C"
```

**Pattern E — Major Verse → Borrowed Minor Chorus**:
```
"verse F major bright I-V-vi-IV,
chorus borrows parallel minor i-bVI-bIII-bVII for epic feel"
```

### 13.11 CREATE Style Box 화성 정보 위치 (재확인)

회의록 Q2 답변 직격: "프롬프트에도 확실히 create 단계에
들어가야 하는데 또 더블 기타인데 각각 다른 코드로 연주해서
화성 조합 혹은 일부러 불협화음을 일으킨다는거 그런 부분에
있어서도... 프롬프트단계에선 아예 안 나오는 경우가 많아."

**해결**:
1. CREATE Style Box 첫 200자 안에 코드 진행 sketch 의무 포함
2. 비다이어토닉 코드는 이름 + 효과 한 줄로
3. 섹션별 진행 분리 표기
4. Bitonal / Polychord 사용 시 명시적 어법

**검증된 CREATE 화성 정보 형식**:
```
[80-200자 zone]
"in [키], [verse 진행], [chorus 진행 변형 포인트],
[bridge / final chorus 변형]"

예시:
"in E major, verse C#m-A-E-B,
chorus E-B-Cmaj7-E with Cmaj7 chromatic mediant single accent,
bridge F#m7-Bsus4 jazz palette,
Final Chorus half-step up to F major"
```

### 13.12 화성 어법 디버깅 (15 파일 적용)

03 §11.8과 연계. 출력에서 화성 무시 시:

**Symptom**: "비다이어토닉 코드 다 사라짐"
- 처방 1: CREATE Style Box 첫 200자에 비다이어토닉 정보
- 처방 2: COVER에 "preserve modal mixture from CREATE" 명시
- 처방 3: Lyrics Box 해당 섹션에 [Section: chromatic mediant
  accent on this line] 명시

**Symptom**: "Verse / Chorus 동일 진행"
- 처방: 명시적 분리 — "verse [A], chorus [B]" 두 진행 모두 표기

**Symptom**: "Modulation 안 됨"
- 처방: Style Box "modulates half-step up" + Lyrics Box
  [Key Change up half-step] 동시 명시

---

## SECTION 14 — Synthesizer Articulation Bank (NEW v2.2)

회의록 트리거: "악기들 주법에 대해서도 연출이 가능한지
어떤 용어가 필요한지." 신스 음색 / 주법 / 처리법 라이브러리.

### 14.1 Synthesis Type별 키워드

**Subtractive Synthesis (감산)**:
```
"analog subtractive synth, sawtooth oscillator filtered"
"warm analog filter sweep, low-pass cutoff modulation"
"Moog-style ladder filter resonance"
```

**FM Synthesis (FM)**:
```
"FM synthesis bell tones, DX7-style electric piano"
"FM lead sharp metallic timbre, modulated carrier"
"FM bass aggressive growl, modulator depth high"
```

**Wavetable Synthesis (웨이브테이블)**:
```
"wavetable synthesis, morphing timbre throughout phrase"
"wavetable lead with table position automation"
"Serum-style wavetable bass, complex harmonics"
```

**Granular Synthesis (그래뉼러)**:
```
"granular synthesis pad, micro-grain texture"
"granular vocal sample stretched into ambient pad"
"glitchy granular timbre, fragmented sound particles"
```

**Additive Synthesis (가산)**:
```
"additive synthesis bell, controlled harmonic spectrum"
"organ-like additive pad, stacked sine partials"
```

**Physical Modeling**:
```
"physical modeling string, plucked virtual instrument"
"modeled wind instrument, breath-controlled timbre"
```

### 14.2 음색 카테고리별 키워드

**Pad / Atmosphere**:
```
"warm Juno-style analog pad, sustained chord wash"
"shimmer pad with reverb tail, ambient texture"
"evolving wavetable pad, slow morph throughout verse"
"cinematic pad with movement, filter sweeps"
"glass shimmer pad bright 5kHz+ air shelf"
```

**Lead Synth**:
```
"FM bell lead, crystalline metallic"
"saw lead detuned supersaw, festival energy"
"square wave lead, retro 80s arcade feel"
"vocoder lead, robotic processed vocal sample"
"acid lead 303-style squelchy resonant"
"plucky lead with short envelope, melodic stab"
```

**Bass Synth**:
```
"sub-bass mono 20-80Hz round warm"
"reese bass complex modulated, drum-and-bass classic"
"acid bass 303 squelchy moving filter"
"FM bass aggressive metallic growl"
"wobble bass dubstep modulation"
"sliding 808 sub-bass with pitch glide" (drill 시그니처)
```

**Pluck / Stab**:
```
"pluck synth short envelope crystalline"
"chord stab punchy syncopated rhythm"
"plucky arpeggio 16th-note sequence"
"hardstyle stab aggressive distorted"
```

**Arpeggiator / Sequencer**:
```
"sequenced arpeggiator 16th-note pattern"
"random arpeggiator unpredictable melodic"
"step sequencer locked pattern repeat"
"acid arpeggio modulated filter"
```

### 14.3 시대별 신스 결

**1970s 아날로그**:
```
"vintage Moog synth warm analog character"
"ARP 2600-style phasey filter sweep"
"Mellotron string section warm vintage"
"early polyphonic synth Prophet-5 era"
```

**1980s 디지털 + 아날로그**:
```
"DX7 FM electric piano shimmer"
"Juno-60 analog pad warmth"
"LinnDrum machine programmed beat"
"gated reverb snare massive 80s"
"Yamaha CS-80 lush polyphonic strings"
```

**1990s**:
```
"Korg M1 piano 90s classic"
"Roland JD-800 digital synth"
"Oberheim OB-Xa pad warmth"
"Novation Bass Station acid lead"
```

**2000s-2010s**:
```
"Massive supersaw stack EDM festival"
"Sylenth1-style trance lead bright"
"Serum wavetable modern bass"
"Moog Sub Phatty-style modern analog"
```

**2020s 현대**:
```
"Vital wavetable modern pluck"
"Diva analog modeling warm"
"Pigments hybrid synthesis modern"
"Phase Plant complex modular routing"
```

### 14.4 신스 처리법 (Articulation FX)

**Modulation FX**:
```
"chorus modulation thick widening effect"
"phaser sweep psychedelic motion"
"flanger jet plane effect aggressive"
"tremolo amplitude modulation classic"
"vibrato pitch modulation expressive"
```

**Time-based FX**:
```
"reverb hall long tail spacious"
"plate reverb dense vintage"
"spring reverb vintage character"
"tape delay analog warmth"
"digital delay precise quantized"
"reverse reverb creative effect"
"shimmer reverb octave-up sparkle"
```

**Filter / EQ Movement**:
```
"low-pass filter sweep cutoff modulation"
"high-pass filter rising tension"
"band-pass filter narrowing focus"
"resonant filter peak emphasis"
"comb filter metallic character"
"vowel filter formant morphing"
```

**Distortion / Saturation**:
```
"tube saturation warm analog"
"tape saturation vintage cassette"
"bit-crusher 8-bit lo-fi"
"waveshaper aggressive harmonics"
"soft clip gentle drive"
"hard clip aggressive distortion"
```

### 14.5 Sidechain / Compression FX

```
"sidechain pump aggressive 90% duck under kick"
"subtle sidechain breathing 30% gentle pump"
"parallel compression NY-style punchy"
"glue compression bus-wide cohesion"
"ducking sidechain on bass under kick"
"sidechain on pads pumping with rhythm"
```

### 14.6 Stereo / Spatial Processing

```
"wide stereo synth pad L80 R80"
"narrow center mono synth bass"
"ping-pong delay alternating L/R"
"stereo widener Haas effect short delay"
"mid-side processing wide sides focused center"
"3D depth front-to-back synth layering"
```

### 14.7 Modern Production Synth Tricks (2024-2026)

**Hyperpop / Digicore**:
```
"glitchy stuttered synth chops"
"pitched-up vocal sample chord stabs"
"clipping intentional distortion creative"
"extreme sidechain 95% pump festival energy"
"formant-shifted synth lead alien character"
```

**Modern K-pop (4th-5th gen)**:
```
"crystal clear modern K-pop synth pluck"
"layered synth pad bright airy crystalline"
"future-bass chord stabs pitched vocal-style"
"polished modern synth lead, no vintage warmth"
"sub-bass 808 with subtle pitch glide between root notes"
```

**Modern Pop (Cirkut / Antonoff era)**:
```
"warm analog-modeled synth modern pop polish"
"retro 80s synth revival with modern clarity"
"synth bass modern pop wide stereo subtle saturation"
"layered synth pads cinematic texture"
```

**Bedroom Pop / Lo-fi**:
```
"warm fuzzy synth pad lo-fi character"
"detuned synth ±12 cents organic imperfection"
"vintage synth recorded through cassette"
"intimate synth close-mic feel small room"
```

---

## SECTION 15 — Drum Articulation & Modern Production Bank (NEW v2.2)

회의록 트리거: 최신 사운드를 위한 드럼 처리법 + 장르별
드럼 어법.

### 15.1 Kick (킥) 어법

```
"punchy kick 60-100Hz fundamental tight transient"
"sub kick 30-50Hz felt not heard"
"trap 808 kick sustained pitched bass"
"layered kick: sub-bass body + click attack 5kHz"
"sidechained kick driving the mix"
"reverb kick spacious large room feel"
"distorted kick aggressive drive"
"acoustic live kick room mic ambience"
```

**시대/장르별 킥**:
```
"1980s gated kick massive room"
"1990s boom-bap kick MPC-sampled"
"trap 808 sustained sub-bass kick"
"modern pop kick layered punch + sub"
"UK garage kick on 1-and-3-and skippy"
"amapiano kick deep house-derived on 1"
```

### 15.2 Snare (스네어) 어법

```
"crisp snare 200-300Hz body 5kHz crack"
"trap snare beat 3 only hard hit"
"backbeat snare 2 and 4 driving rock"
"ghost note snares 16th grid quiet velocity"
"rim cross-stick subtle alternative"
"clap stack instead of snare modern pop"
"layered snare: acoustic + sample + 808 transient"
```

**시대/장르별 스네어**:
```
"1980s gated reverb snare massive room"
"1990s boom-bap snare MPC-sampled lo-fi"
"trap snare 808-layered hard punch beat 3"
"K-pop crisp snare modern bright"
"drill snare sharp crack beat 3"
"amapiano clap-snare hybrid"
```

### 15.3 Hi-Hat (하이햇) 어법

```
"closed hi-hat 16th grid steady"
"open hi-hat off-beat house signature"
"trap hi-hat triplet rolls 32nd skitters"
"shuffled hi-hat swung feel hip-hop"
"crisp hi-hat 12kHz+ airy bright"
"vintage hi-hat 6kHz+ rolled-off warm"
"polyrhythmic hi-hat 8th + 16th layered"
```

**모던 트랩 / 드릴 어법**:
```
"trap hi-hat triplet rolls and 32nd skitters in transitions"
"drill hi-hat off-grid 16th patterns with triplet rolls"
"hi-hat opening on 'and' of beat with reverse cymbal"
"hi-hat rolls building tension into chorus drop"
```

### 15.4 808 / Sub-Bass 어법

```
"808 sub-bass mono 20-80Hz sustained"
"808 with pitch glide between root tones"
"sliding 808 dn-dn-dn drill signature"
"808 layered with sine sub-bass for fundamental"
"808 distorted aggressive trap"
"clean 808 modern pop subtle"
"808 sidechain duck under kick 80ms"
```

### 15.5 Percussion 레이어

```
"shaker 16th grid filling top end"
"tambourine on backbeat 2 and 4"
"conga polyrhythmic Latin layer"
"timbales accent fills"
"cowbell 80s rock signature"
"woodblock crisp percussive accent"
"rim click subtle alternative to snare"
"finger snaps modern pop top layer"
"hand claps doubled with snare"
"log drum amapiano signature pitched bass"
```

### 15.6 시대별 드럼 결

**1970s**:
```
"vintage 70s drum kit warm analog room"
"loose live drums natural dynamics"
"dry 70s soul drums tight punch"
```

**1980s**:
```
"LinnDrum machine programmed pattern"
"gated reverb snare massive room cut"
"DX7 drum samples digital crisp"
"electronic drums Simmons-style toms"
```

**1990s**:
```
"MPC-sampled boom-bap drums shuffled"
"breakbeat amen break chopped"
"grunge live drums roomy raw"
"trip-hop dusty drum break vinyl"
```

**2000s-2010s**:
```
"polished pop drums tight compressed"
"EDM big-room four-on-floor crushed"
"trap drums 808 + triplet hats"
"dubstep half-time heavy"
```

**2020s 현대**:
```
"modern pop drums layered punch + clarity"
"Afrobeats clave-derived 3-2 son pattern"
"amapiano log drum + deep house kick"
"drill sliding 808 + snare beat 3"
"hyperpop clipping kick + accelerated hats"
"K-pop 5th gen drums punchy bright crisp"
```

### 15.7 Modern Drum Tricks (2024-2026)

**Layered Drums (모던 표준)**:
```
"layered kick: 808 sub + acoustic body + click attack"
"layered snare: acoustic + sample + transient designer"
"hi-hat doubled: closed precise + open texture"
"clap layered: programmed + recorded crowd hand claps"
```

**Dynamic Processing (모던 어법)**:
```
"transient designer attack +3dB punch"
"parallel compression drum bus NY-style"
"saturation on drum bus glue and warmth"
"sidechain pumping creating breathing"
"micro-groove humanization 80% quantize"
```

**Spatial Drum Processing**:
```
"drum room mic ambient natural"
"close-mic drums tight modern"
"plate reverb on snare 1.5 second decay"
"drum bus reverb subtle 8% wet"
"stereo drum overheads wide L/R"
```

---

## SECTION 16 — Guitar Articulation Bank (NEW v2.2)

회의록 트리거: 악기 주법 종합. 기타 주법은 더 풍부해서 별도
정리 (16번 신규 파일에서도 다룸, 여기는 Suno 어법 핵심만).

### 16.1 어쿠스틱 기타 주법

```
"fingerpicked acoustic guitar Travis-style alternating bass"
"strummed acoustic D-DU-UDU folk pattern"
"capo on 4th fret bright high register"
"acoustic with palm muting tight rhythm"
"flatpicked acoustic country lead"
"slide guitar on acoustic bottleneck"
"hammer-on pull-off acoustic ornaments"
"acoustic chord melody jazz-style"
"percussive acoustic body taps + strums"
```

### 16.2 일렉트릭 기타 주법

```
"palm-muted electric guitar tight rhythm"
"chicken pickin hybrid pick + fingers country"
"tapping two-handed lead virtuoso"
"sweep picking arpeggiated speed"
"alternate picking precision lead"
"hybrid picking pick + fingers nuanced"
"slide guitar electric blues bottleneck"
"tremolo picking sustained tremolo"
"hammer-on pull-off legato lead"
"vibrato bar dive bombs whammy"
"natural harmonics chimes shimmer"
"pinch harmonics squealing accents"
"feedback controlled sustained notes"
```

### 16.3 Funk / R&B 기타 어법

```
"16th-note funk choke palm-muted Telecaster"
"chicken-scratch percussive muted strums"
"ninth chord stabs syncopated funk"
"clavinet-like guitar wah-wah envelope"
"comping muted chord rhythms"
"slap bass-style guitar percussive"
```

### 16.4 록 / 메탈 기타 어법

```
"distorted electric guitar power chords"
"palm-muted chugging rhythm metal"
"tremolo picking trem-pick speed metal"
"sweep arpeggios neoclassical metal"
"7-string guitar low chugging modern metal"
"djent palm-muted polyrhythmic"
"shoegaze wall of distorted reverb"
"grunge raw distorted barre chords"
```

### 16.5 인디 / 얼터너티브 기타 어법

```
"jangly clean electric guitar arpeggios"
"reverb-soaked dream pop guitar swirling"
"chorus-modulated 80s clean electric"
"fingerpicked electric clean indie"
"open-tuning acoustic DADGAD Celtic"
"sparse picked notes minimal indie"
"shimmer reverb guitar atmospheric"
```

### 16.6 K-Indie 기타 어법 (Limganzi 시그니처)

```
"palm-muted Telecaster 16th funk choke L60/R60"
"plucked acoustic guitar fingerpicking gentle"
"clean Telecaster with light chorus modulation"
"acoustic guitar primary center +2dB priority"
"Telecaster pair L20 R20 chorus only withdrawn verses"
"chicken-pickin clean Telecaster K-indie style"
```

### 16.7 시대별 기타 톤

```
"1970s warm vintage tube amp guitar"
"1980s chorused clean electric DX7-era"
"1990s grunge raw distorted Big Muff"
"2000s polished pop-rock guitar"
"2010s indie clean reverb-soaked"
"2020s modern pop guitar bright clarity"
```

### 16.8 Two-Guitar Bitonal Technique (검증 필요)

회의록 직격 어법. 03 §12와 연계.

```
"two guitars bitonal layering: rhythm guitar in C major,
lead guitar in Bb major creating parallel friction"

"guitar pair polychord: rhythm I chord, lead IV chord
perpetual suspension"

"two guitars one mode apart: rhythm major,
lead Lydian one fourth higher"

"intentional detuned guitar pair: guitar 1 standard,
guitar 2 -10 cents organic warmth simulation"
```

---

## SECTION 17 — Modern Vocal Production Tricks (NEW v2.2)

2024-2026 글로벌 트렌드 보컬 처리법. Cirkut / Antonoff /
Finneas era 어법.

### 17.1 모던 보컬 더블링

```
"doubled lead +10 cent detune L20/R20" (검증)
"triple-tracked lead: center + +10 right + -10 left" (검증)
"vocal stacked harmonies +3rd +5th +octave"
"unison vocal stack 4 takes layered"
"formant-shifted backing vocal +25 cents up panned L20"
```

### 17.2 모던 보컬 처리

```
"warm analog tube saturation on vocal bus"
"de-esser refined 5-8kHz sibilance control"
"vocal corridor 500Hz-3kHz protected"
"high-shelf air boost +1.5dB at 12kHz"
"+1dB warmth boost 200-400Hz body"
"natural human breath texture preserved"
"organic close-mic intimacy"
"no auto-tune residue, natural pitch"
```

### 17.3 Cluster Vocal Dissonance (실험적)

Case 19 검증 어법. Bridge 모먼트용.

```
"cluster vocal dissonance with m2 intervals below lead
and M7 above on bridge climax phrase only,
dissonance layer 6dB below lead with formant shift"

"microtonal detuned robot harmony layer
formant-shifted L25/R25 -25 cents"
```

### 17.4 Vocal Chops / Granular Vocals

```
"vocal chop samples chromatic-pitched melodic lead"
"granular vocal sample stretched into pad texture"
"vocal stutter glitch chops modern pop"
"pitched-up vocal sample chord stabs hyperpop-style"
"cut-up vocal phrases rhythmic accent"
```

### 17.5 Auto-Tune / Pitch Processing

```
"tasteful auto-tune subtle pitch correction"
"Travis-Scott-style heavy auto-tune pitch quantize"
"vocoder-processed lead vocal robotic"
"talkbox-style vocal processing"
"melodyne-corrected pitch perfect modern pop"
"natural pitch no correction organic"
```

### 17.6 Modern Pop Vocal Stack (2024-2026 어법)

```
"modern pop vocal stack: lead + double +10c +
harmony +3rd quiet underneath + air doubling +octave"

"Cirkut-style polished modern pop vocal:
clean lead, subtle warmth saturation, controlled compression"

"Antonoff-style vocal: warm tube saturation,
plate reverb 25% wet on chorus, intimate verse dry"

"Finneas-style minimal vocal: dry close-mic intimate,
breath audible, almost no processing"
```

### 17.7 Bilingual / Code-Switching Vocal

```
"Korean primary verse, English chorus hook on melodic peak"
"Japanese primary with English ad-libs phrase-end"
"phrase-level code-switch HANA Blue Jeans-style"
"line-level code-switch K-pop standard"
"natural fluent Seoul Korean diction native pronunciation"
"clear Japanese vowel articulation"
"Pan-African accented English Tems-style"
```

### 17.8 Modern Vocal Anti-Patterns

**A. Robotic / AI-Like Output**:
- 처방: "natural human breath, organic phrasing,
  microvariation, audible breath between phrases,
  no auto-tune residue"

**B. Over-Compressed / Squashed**:
- 처방: "open dynamics, breath room, no aggressive limiting,
  controlled compression preserving transients"

**C. Lost in Mix (보컬 burial)**:
- 처방: "vocal forward in mix, vocal corridor 500Hz-3kHz
  protected, +2dB vocal lift in chorus"

**D. Dated Sound (vintage 의도 아닌데 vintage 결)**:
- 처방: era anchor 명시 → "2024-2026 modern" /
  "late-2010s polished" + "modern controlled loudness"

---

## SECTION 18 — Producer Signature Decomposed Bank (NEW v2.2 / 회의록 직격)

09 §5.3 Decomposed Signature Method 확장. 2024-2026 핫한
프로듀서들의 어법 정리. 99_OPERATOR_VAULT Part F와 연계.

### 18.1 Cirkut (2026 그래미 Producer of the Year)

대표작: ROSÉ × Bruno Mars "APT.", Lady Gaga "Abracadabra",
The Weeknd "Big Sleep", Coco Jones "AEOMG"

**시그니처**:
```
"Cirkut-style modern pop polish: warm tube saturation on bus,
controlled bus-glue compression, vocal forward presence,
wide stereo with centered low-end, retro-modern hybrid texture,
nostalgic synth elements with crisp modern clarity"
```

**ROSÉ × Bruno Mars "APT." 결**:
```
"2000s era percussion and beats meets modern pop polish,
vintage drum samples MPC-style, warm analog synth pads,
clean retro-pop production, Korean-English bilingual hook"
```

**Lady Gaga "Abracadabra" Mayhem era 결**:
```
"theatrical dance-pop, gothic ballroom aesthetic,
massive driving four-on-floor, dark electronic textures,
80s synth revival with modern aggression,
operatic dramatic vocal delivery"
```

### 18.2 Jack Antonoff

대표작: Taylor Swift, Lana Del Rey, Lorde, Sabrina Carpenter

**시그니처**:
```
"Jack Antonoff-style: reverb-soaked stadium-intimate hybrid,
layered synth pads warm 80s revival, vocal processed with
subtle plate reverb, dynamic open verses to compressed chorus,
nostalgic emotional production, 80s drum machine + organic"
```

**Sabrina Carpenter "Short n' Sweet" era**:
```
"playful 60s influence pop, bubblegum bright,
vintage-modern hybrid, retro vocal warmth,
gentle compression preserving dynamics"
```

### 18.3 Finneas (Billie Eilish)

대표작: Billie Eilish "Hit Me Hard and Soft" (2024)

**시그니처**:
```
"Finneas-style minimalist bedroom pop production:
intimate close-mic vocals with audible breath,
sub-bass forward, sparse percussion,
dark bedroom atmosphere ASMR intimate texture,
warm synth pads gentle, clean bass, airy percussion,
bright polished pop sound minimal layers"
```

**Billie Eilish 2024 era 결**:
```
"whispered female vocals close-mic, sub-bass dominant,
minimal percussion, dark bedroom-pop production,
ASMR intimate texture, layered vocal harmonies subtle"
```

### 18.4 BNYX (Modern Hyperpop / Dark Pop)

대표작: Drake, 21 Savage, Yeat 등 다크 트랩

**시그니처**:
```
"BNYX-style dark hyperpop edge: distorted 808 sub-bass,
glitchy percussion, ambient dark synth pads,
clipping intentional aggression, modern trap evolution"
```

### 18.5 Charli XCX Production (Brat era)

**시그니처**:
```
"Brat era Charli XCX production: hyperpop bratty energy,
distorted club beats, pitched vocal samples,
EDM-adjacent bratty female vocals, experimental modern pop,
2024 club summer revival aesthetic"
```

### 18.6 Mid-2010s Indie 시그니처 (참고용)

```
"Phoebe Bridgers / Bon Iver-style indie folk:
fingerpicked acoustic guitar, lo-fi tape-saturated drums,
intimate close-mic vocal audible breath, no auto-tune,
mid-2010s indie East Coast bedroom-folk scene,
vinyl-warmth aesthetic"
```

### 18.7 Producer Reference Decomposed 작성 절차

새 프로듀서 시그니처 추출 시:
1. 대표 트랙 3-4개 선정
2. 공통 사운드 특성 5-7개 추출
3. 보컬 / 드럼 / 신스 / 믹스 4축으로 분류
4. 영어 키워드 2-3 sentences로 압축
5. 99_OPERATOR_VAULT Part F 또는 이 §18에 등록

**예시 추출 절차** (Cirkut):
1. APT. + Abracadabra + Big Sleep 분석
2. 공통: 따뜻한 saturation, vocal forward, retro-modern hybrid,
   wide stereo, controlled compression, polished but warm
3. 4축 분류:
   - 보컬: 따뜻한 tube saturation, forward presence
   - 드럼: 모던 punch + 빈티지 sample 결합
   - 신스: 80s revival + 모던 clarity
   - 믹스: bus-glue compression, wide-centered
4. 압축: "Cirkut-style modern pop polish: warm tube saturation,
   controlled bus-glue compression, vocal forward presence,
   wide stereo with centered low-end, retro-modern hybrid texture"
5. §18.1로 등록 완료

---

---

## SECTION 19 — Effects Direction Bank (NEW v2.3 / 2026-XX)

### 19.0 이 섹션의 위치

16 §17 (Effects Processing Bank) = 이펙터 의사결정 (왜·언제)
15 §19 (이 섹션) = Suno 어법 라이브러리 (어떻게 박는가)

매 작업 시 16에서 결정 → 15에서 어법 픽업 → Style Box 조립.

### 19.1 Modulation 어법

#### Vibrato
"vocal with controlled vibrato on long sustained notes" "natural vibrato emerging at phrase ends" "wide operatic vibrato gospel-classical" "subtle vibrato modern pop standard" "no vibrato straight tone indie" "guitar lead with expressive vibrato bend" "synth lead with subtle LFO vibrato 5Hz depth ±10 cents" "string section with natural vibrato classical"

#### Tremolo
"tremolo guitar surf-rock signature 60s" "Twin Peaks tremolo-soaked clean electric" "amplitude-modulated electric piano vintage warmth" "slow tremolo on Wurlitzer 70s soul" "fast tremolo psychedelic 60s" "tremolo bar dive bombs whammy"

#### Chorus 이펙터
"clean electric guitar with chorus modulation 80s warmth" "Juno-style chorused pad sustained" "chorus-effect on Rhodes electric piano" "thick chorus on bass synth" "chorused 12-string acoustic shimmer" "subtle chorus modulation L/R wide" "80s chorused clean Telecaster signature"
**주의**: 곡 구조 [Chorus]와 충돌 → 자연어로 박거나
`[Chorus effect on <instrument>]` 형식 사용.

#### Phaser
"phaser sweep psychedelic motion" "slow phaser on rhythm guitar 70s funk" "phased Rhodes electric piano jazz fusion" "deep phaser stereo movement 70s" "subtle phaser drift modern neo-soul"


#### Flanger
"flanger jet plane sweep aggressive" "flanged drum fill bridge transition" "flanger on guitar solo 70s rock" "subtle flanger drift dreamy texture" "flanged synth stab modern trap transition"

#### Rotary Speaker (Leslie)
"Hammond B3 with Leslie rotary fast" "Leslie speaker slow rotary on organ" "rotary modulation on electric piano" "Hammond organ Leslie cabinet speed change"


### 19.2 Reverb 어법
"plate reverb on vocal 1.5 second decay vintage" "hall reverb 2.5 second decay pre-delay 80ms ballad" "room reverb intimate close-mic indie" "spring reverb vintage character reggae" "shimmer reverb octave-up sparkle dream-pop" "gated reverb snare 80s signature" "verses dry close-mic 8% wet, chorus blooms 25% wet" "vocal corridor 500-3kHz protected with subtle plate" "reverb tail extends through outro fade" "completely dry close-mic no reverb intimate"


### 19.3 Delay 어법
"slap-back delay 100ms single echo rockabilly" "tape echo analog warmth wow flutter" "ping-pong delay alternating L/R modern pop" "1/8 dotted delay rhythm-locked EDM" "reverse delay creative effect dreampop" "throw delay on vocal phrase ends only" "long tape delay psychedelic 70s" "tight 1/16 delay tight modern"


### 19.4 Dynamics 어법
"tight pop compression on lead vocal forward presence" "parallel compression NY-style drum bus punchy" "bus glue compression cohesive master" "sidechain pump aggressive 90% duck under kick" "subtle sidechain breathing 30% gentle pump" "transient designer +3dB attack drum punch" "tube saturation +1dB on vocal bus warmth" "open dynamics natural transient preservation" "controlled compression preserving dynamics" "limited modern -8 LUFS streaming" "dynamic open -14 LUFS cinematic"

### 19.5 Distortion / Saturation 어법
"tape saturation +1dB master analog warmth" "tube saturation harmonic warmth on vocal bus" "warm overdrive on lead guitar blues-rock" "heavy distortion aggressive metal rhythm" "vintage fuzz Big Muff 60s psychedelic" "bit-crusher 8-bit lo-fi hyperpop" "waveshaper aggressive harmonics modern electronic" "subtle saturation organic warmth indie" "clipping intentional creative hyperpop"


### 19.6 Spatial 어법
"wide stereo synth pad L80 R80" "narrow centered mono synth bass" "stereo widener Haas effect short delay" "mid-side processing wide sides focused center" "3D depth front-to-back synth layering" "vocal centered, guitars L60/R60, pads L80/R80" "hard pan L100 R100 doubled lead" "narrow verse 60% to wide chorus 95%"


### 19.7 이펙터 분배 검증 어법 (CREATE vs COVER)

#### CREATE에 들어가는 이펙터 어법 (시그니처 톤)
"chorused Rhodes electric piano warm 70s" "tremolo-soaked clean electric guitar surf" "phaser-modulated rhythm guitar 70s funk" "distorted bass aggressive metal foundation" "fuzz guitar grunge raw" "vocal with subtle controlled vibrato"


#### COVER에 들어가는 이펙터 어법 (텍스처·연출)
"plate reverb on vocal 25% wet on chorus" "sidechain pump 80% on bass under kick" "flanger swell on bridge transition" "reverse cymbal into final chorus" "throw delay on vocal phrase ends" "tape saturation master bus +1dB" "transient designer +3dB on snare attack" "parallel compression drum bus" "hall reverb on bridge piano 35% wet" "shimmer reverb tail outro extending"


### 19.8 시그니처 모먼트로서의 이펙터 (CREATE Signature + COVER 처리)
시그니처 모먼트: "Bridge에서 갑자기 phaser 진입 (3초 sweep)"

CREATE Signature Moments에 명시: "bridge entry features sudden phaser sweep on rhythm guitar, 3-second slow phase"

COVER 처리법: "phaser modulation on bridge guitar L60/R60, slow rate 0.3Hz, deep 80%, wet 50%"


### 19.9 모던 사운드 디폴트 묶음 (99_OPERATOR_VAULT Part F 확장)

매 COVER에 자동 적용 (의도적 빈티지 제외):

**보컬 디폴트 묶음**:
"warm tube saturation on vocal bus, de-esser 5-8kHz, vocal corridor 500Hz-3kHz protected, +1dB warmth 200-400Hz, natural human breath texture, no auto-tune residue"


**드럼 디폴트 묶음**:
"transient designer +3dB attack, parallel compression drum bus NY-style, subtle saturation glue, layered kick sub + click + body, spatial drum room ambient"


**마스터 디폴트 묶음**:
"tape saturation +1dB master bus warmth, gentle bus glue compression, controlled limiting -10 LUFS streaming, mono compatibility check, transient preservation"


이 묶음은 COVER에 풀로 박지 말고 약어로:
"vocal organic bus + corridor protected + warmth" "drum modern layered + parallel + transient designer" "master streaming -10 LUFS + tape sat + glue"
→ 실제로는 위 묶음 풀 처방이 적용됨 (시스템 내부 약속).

## END OF v2.2 NEW SECTIONS (12-18)

15 파일 기존 섹션 1-11은 보존. 12-18이 신규 추가분.

**핵심 변경 요약**:
- §12: Microtonal Direction Bank (회의록 직격, 03 §10-12 연계)
- §13: Harmonic Direction Bank (Q2 답변, 03 §11 연계)
- §14: Synthesizer Articulation Bank (15+ 음색 카테고리)
- §15: Drum Articulation Bank (시대별 + 장르별)
- §16: Guitar Articulation Bank (주법별 + Two-Guitar Bitonal)
- §17: Modern Vocal Production Tricks (2024-2026 어법)
- §18: Producer Signature Decomposed Bank (Cirkut, Antonoff,
  Finneas, BNYX, Charli XCX 등)



<!-- USER EXTENSION ZONE — append discovered direction patterns below -->



---

## SECTION 20. EXTENDED VOCABULARY POOLS (NEW v2.7 / External Research)

External research synthesis (Suno field guide 2026 + Reddit community
testing): vocabulary pools that operator's prior SOP either lacked
or underdeveloped.

### §20.1 Modern era anchors (2024-2026)

Beyond generic "modern" / "contemporary":

```
2024-2026 contemporary
2026 cutting-edge
late-2024 trending
mid-2020s polish
post-2023 hyperpop influence
2024 viral aesthetic
2025-2026 Korea aesthetic
2026 Y2K revival
2024 indie sleaze
2025 hyperreal production
post-COVID intimate aesthetic
```

### §20.2 Vocal-character vocabulary (granular)

#### Tone modifiers
```
silky / velvety / honeyed / molten / smoky / sandpaper-rough /
gravel / glassy / icy / warm / sun-baked / tinny / chrome /
crystalline / wooden / hollow
```

#### Delivery dynamics
```
restrained throughout / explosive on hook / whispered conversational /
half-spoken half-sung / theatrical projection / under-projected /
intimate close-mic / wide stage-mic / shoulder-shrug casual
```

#### Phrase-end behaviors
```
no vocal fry / slight slide-up on phrase ends / hard cutoff endings /
breath release at line end / vibrato narrow / no vibrato /
slight pitch slide between notes / clean intonation / micro-pitch
slippage acceptable
```

### §20.3 Production texture vocabulary

#### Era textures
```
analog tape saturation (warm, mid-forward)
digital crisp (clean top end, modern)
vinyl crackle (subtle, mid-frequency noise)
cassette warmth (slight wow/flutter, mid-bump)
broken radio (band-limited, AM filter)
hi-fi audiophile (full spectrum, transparent)
lo-fi bedroom (compressed top end, narrow stereo)
```

#### Spatial textures
```
intimate close-mic (no reverb tail, present)
medium room (200ms reverb, natural)
large hall (800ms+ reverb, distant)
plate reverb (bright, metallic)
spring reverb (vintage, slightly resonant)
ambient cloud (very long, washed)
gated reverb (cuts hard, 80s drum effect)
```

#### Genre-specific texture sets

**K-pop modern**:
```
crystalline pads, sidechain-pumping sub-bass, layered analog synths,
subtle vinyl warmth, crisp 808 attack, vocal chops scattered
```

**Indie folk**:
```
warm tape saturation, natural room sound, fingerstyle clarity,
mid-forward acoustic guitar, intimate proximity, subtle hiss
```

**Hyperpop**:
```
pitched-up vocals, crushed compression, distorted bass blasts,
glitchy stutters, maximum brightness, deliberately jarring transitions
```

**Synthwave**:
```
gated reverb on snares, FM synthesizer leads, analog drum machine,
chorused electric piano, neon-bright lead synths, sidechain pumping
```

### §20.4 Korean-genre specific vocabulary

#### K-Ballad
```
slow building emotional arc, late-chorus key lift, restrained verse
delivery, full belted chorus, piano-vocal core, string arrangement
swelling into Final Chorus
```

#### K-R&B
```
neo-soul chord voicings, syncopated drum programming, breathy
intimate vocal, multilayered harmony stacks, jazz-influenced
chord substitutions, smooth Rhodes electric piano
```

#### K-Hip-Hop
```
boom bap drum kit / contemporary trap 808s, vocal chops, vintage
sample texture, mid-forward rap delivery, melodic hook chorus,
Korean rap cadence (faster than English)
```

#### K-Indie
```
bedroom production aesthetic, raw acoustic guitar, intimate
close-mic vocal, slight tape hiss, minimal effects, natural
room reflection, conversational delivery
```

#### Trot
```
kung-jjak rhythm pattern (two-beat pulse), kkeokgi melismatic
ornament, accordion accent, brass section stabs, vintage analog
warmth, dramatic phrase endings
```

### §20.5 Anti-cliché vocabulary substitutes

Replace tired terms with fresh ones:

| Cliché | Fresh substitute |
|---|---|
| "emotional" | "vulnerable confessional" / "raw exposed" |
| "powerful" | "throat-projected" / "diaphragm-driven" |
| "smooth" | "honeyed" / "silken" / "frictionless" |
| "dark" | "shadowy" / "smoke-laden" / "minor-mode brooding" |
| "bright" | "sun-bleached" / "high-gloss" / "crystalline" |
| "warm" | "tube-saturated" / "wool-blanketed" / "mid-forward" |
| "epic" | "stadium-scale" / "horizon-wide" / "monumental" |
| "intimate" | "close-mic confessional" / "private-room" |
| "anthemic" | "fist-pump declarative" / "stadium-singalong" |

### §20.6 Pat Pattison Verb Wattage applied to Style Box (NEW)

08 §5 Verb Wattage audit applies to *production language too*:

Weak (0-10W) production verbs to avoid:
```
"has reverb" / "is processed" / "with effects" / "uses synths"
```

Strong production verbs to use:
```
"reverb drenches the chorus" (50W)
"compression pumps in time with the kick" (200W)
"saturation crackles around 8kHz" (500W)
"the bass slams every downbeat" (1000W)
```

Style Box reads more decisively with strong verbs.

---

