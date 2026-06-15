# VOCAL PRODUCTION — DIRECTIVES, TECHNIQUES, SUNO KEYWORDS
# Version: 1.0
# Scope: Vocal 5-element directive system, vocal classification,
#        timbre vocabulary, technique reference, Suno-specific
#        keyword conventions, vocal effects and processing,
#        layering and harmony stack notation
# Use: Every vocal direction in CREATE/COVER prompts must produce
#      a complete 5-element directive that Suno's vocal engine
#      can interpret reliably

---

## SECTION 1 — THE 5-ELEMENT VOCAL DIRECTIVE

Every vocal directive in a Suno prompt requires 5 specifications.
Missing any element causes unpredictable vocal output (wrong
gender, wrong range, undesired timbre, mismatched delivery, or
language drift).

### 1.1 The Five Elements

1. **Gender** — male / female / androgynous / group / duet
2. **Range** — specific note range (e.g., C4-F5)
3. **Timbre** — 2-3 specific quality adjectives
4. **Attitude / Delivery** — emotional and technical character
5. **Language** — language with accent simulation if applicable

### 1.2 Directive Template

[Gender] [voice type], range [low note]-[high note], [timbre adjective 1] [timbre adjective 2] timbre, [attitude/delivery] delivery, [language] [accent if needed] [special technique if any]

### 1.3 Complete Examples

**Pop-rock anthem**:
"Female alto, range A3-E5, warm-edged with chest mix on chorus,
conversational verses opening to anthem-power chorus, English
with slight rasp on belted notes"

**Hip-hop verse**:
"Male tenor, range C3-G4, husky-grainy timbre, melodic-rap
delivery with attitude, English with regional slang and ad-libs
throughout"

**Indie folk intimate**:
"Male baritone, range A2-E4, intimate close-mic with audible
breath, story-telling Appalachian-accented English, no auto-tune"

**K-pop multi-member group** (4 members):
"Female group of 4 — Lead vocal soprano D4-E5 clean clear timbre,
Sub-vocal alto A3-C5 warm timbre, Rapper speech-tone husky timbre,
Lead-vocal 2 mezzo G3-D5 powerful timbre with belt ad-libs.
Korean primary with English chorus phrases. Distinct timbral
identity per member."

**Neo-soul melismatic**:
"Male tenor, range C3-Bb4, falsetto-heavy intimate close-mic with
melismatic runs, English with controlled vibrato, no auto-tune"

**Jazz standard**:
"Female alto, range G3-D5, smoky cabaret-style with melismatic
phrase ends and behind-beat phrasing, English with rounded vowels,
no auto-tune"

---

## SECTION 2 — VOCAL CLASSIFICATION (RANGE)

### 2.1 Standard Voice Type Ranges

These ranges represent the typical comfortable singing range for
each voice type. Suno responds best when the requested range
falls within standard classifications.

**Female Voice Types**:

| Voice Type | Range | Tessitura (Comfortable Zone) |
|-----------|-------|------------------------------|
| Soprano | C4 to A5/C6 | F4 to G5 |
| Mezzo-Soprano | A3 to F5 | G3 to E5 |
| Alto / Contralto | F3 to D5 | A3 to D5 |

**Male Voice Types**:

| Voice Type | Range | Tessitura (Comfortable Zone) |
|-----------|-------|------------------------------|
| Countertenor | E3 to E5 (falsetto-based) | A3 to D5 |
| Tenor | B2 to G4 (or A4 with falsetto) | D3 to F4 |
| Baritone | G2 to E4 | A2 to C4 |
| Bass | E2 to E4 | G2 to A3 |

### 2.2 Suno Range Ceiling Rules

**Female ceiling**: F5 reliable. G5 and above triggers vocal
husky breakup, screech, or auto-tune artifacts.

**Workaround for G5+**: Add protection keywords:
"sweet light airy, warm natural human texture, crystal clear thin"

These keywords stabilize Suno's vocal engine in the upper register
and allow occasional G5 with reduced artifact risk.

**Male ceiling**: A4 reliable in chest voice. Above A4 requires
falsetto specification. G4-A4 zone is the modern pop male upper
range (Sam Smith, The Weeknd belt zone).

**Workaround for male B4+**: Specify "falsetto" in directive:
"Male tenor with falsetto in chorus, range C3-D5 chest C3-A4
with falsetto extending to D5"

### 2.3 Range Selection Strategy

Decision criteria:
- Reference vocalist's actual range
- Genre conventions (pop alto-mezzo female / tenor male standard)
- Emotional target (lower = intimate / higher = anthemic)
- Lyric prosody (Korean batchim density vs BPM)

Common pitfalls:
- Choosing range that pushes singer past comfortable tessitura
- Specifying range too wide (3+ octaves) causing inconsistent
  vocal character
- Ignoring genre conventions (jazz contralto in K-pop context
  produces mismatch)

---

## SECTION 3 — VOCAL TIMBRE VOCABULARY

Timbre is the tonal quality of a voice that distinguishes it from
others of the same range and pitch. Suno's vocal engine responds
to specific timbre adjectives.

### 3.1 Core Timbre Categories

**Smooth / Polished**:
- smooth, silky, polished, refined, clean, clear
- Use: pop, R&B, jazz vocal standard, gospel lead
- Pairs with: warm, rich, mellow

**Breathy / Airy**:
- breathy, airy, whispered, soft-spoken, intimate, hushed
- Use: indie, folk ballad, dream pop, Billie Eilish-style
- Pairs with: vulnerable, fragile, light, sweet

**Husky / Raspy**:
- husky, raspy, gravelly, gritty, rough-edged, smoky
- Use: rock, blues, country, modern country pop
- Pairs with: warm-toned, soulful, emotional

**Bright / Piercing**:
- bright, piercing, crystal-clear, ringing, resonant, pure
- Use: K-pop lead, opera-pop, choir lead, theatrical
- Pairs with: clean, projected, soaring

**Warm / Mellow**:
- warm, mellow, velvety, rich, full-bodied, lush
- Use: jazz, R&B, soul, cabaret, ballad
- Pairs with: smooth, intimate, smoky

**Nasal / Twangy**:
- nasal-light, twangy, country-twang, edge
- Use: country, some K-indie, traditional folk
- Caution: heavy nasal alone produces unpleasant Suno output

**Deep / Resonant**:
- deep, resonant, sonorous, gravelly-low, chest-heavy
- Use: deep male voice, narration, doom metal clean

**Theatrical / Operatic**:
- theatrical, declamatory, operatic, classical-trained, projecting
- Use: musical theatre, classical crossover, operatic moments

### 3.2 Combining Timbre Adjectives

Use 2-3 adjectives for clear directives. Avoid stacking 4+
adjectives (creates contradictions or dilutes signal).

**Effective combinations**:
- "warm and slightly husky" (R&B, soul)
- "bright clean and crystal clear" (K-pop lead)
- "breathy and intimate" (indie, dream pop)
- "smoky and mellow" (jazz, late-night)
- "powerful and rough-edged" (rock, anthem)
- "soft-spoken and fragile" (folk ballad, indie)
- "smooth and soulful with melismatic ornaments" (R&B)

**Avoid contradictions**:
- "powerful and breathy" — these conflict; choose one direction
- "raspy and crystal-clear" — incompatible
- "operatic and conversational" — register mismatch

### 3.3 Korean and Asian Vocal Timbre Conventions

K-pop and K-indie often emphasize specific timbral qualities:

- **Clean clear (맑고 깨끗한)**: bright soprano with no rasp,
  ideal for K-pop main vocal
- **Warm gentle (따뜻하고 부드러운)**: mid-range alto warmth,
  K-ballad standard
- **Husky low (낮고 허스키한)**: contralto or alto with
  controlled rasp, K-indie
- **Sweet light airy (달콤하고 가볍고 공기감 있는)**: high
  soprano protection keywords for upper register stability
- **Powerful soulful (파워풀하고 소울풀한)**: belted alto with
  gospel-influenced delivery, K-vocalist style

J-pop and city pop conventions:
- **Bright clean (明るくクリーン)**: J-pop standard, Tatsuro
  Yamashita lineage
- **Whispered intimate (ささやくような親密な)**: bossa-influenced
  city pop, Bebel Gilberto style
- **Anime power belt**: theatrical projection with melismatic
  ornaments, LiSA / Yorushika style

---

## SECTION 4 — VOCAL TECHNIQUE / DELIVERY

### 4.1 Voice Register Techniques

**Chest Voice**:
- Lower register, full-bodied resonance in chest
- Speaking voice extension into singing
- Power, presence, emotional weight
- Suno keyword: "chest voice", "chest mix", "chesty delivery"

**Head Voice**:
- Upper register, resonance in head/face
- Lighter, airier than chest
- Lyrical, ethereal quality
- Suno keyword: "head voice", "head register", "lifted head tone"

**Mixed Voice (Mix)**:
- Blend of chest and head voice
- Modern pop lead vocal foundation
- Allows belting at high pitches without strain
- Suno keyword: "mixed voice", "mix-belt", "modern pop mix"

**Falsetto**:
- Light, breathy upper register
- Distinct from full head voice (less weight)
- Common in male vocals for high notes
- Suno keyword: "falsetto", "falsetto flip", "falsetto tag"

**Whistle Register** (rare):
- Above soprano range, female-specific
- Mariah Carey, Ariana Grande signature
- Suno: limited reliable production; avoid as primary directive

### 4.2 Vocal Power Techniques

**Belting**:
- Powerful chest-dominant projection at high pitches
- Anthem chorus signature
- Suno keyword: "belted", "full-throated belt", "anthem belt"

**Projection**:
- Forward placement, clear articulation
- Theatrical or anthemic
- Suno keyword: "projected", "forward placement", "clear projection"

**Soft Singing**:
- Gentle dynamic, controlled breath
- Intimate ballad signature
- Suno keyword: "soft", "gentle", "delicate", "hushed"

**Whisper Singing**:
- Very low dynamic, breath-emphasized
- Indie / dream pop / intimate ballad
- Suno keyword: "whispered", "intimate close-mic whisper"

### 4.3 Phrasing and Delivery Modes

**Conversational**:
- Speech-rhythm phrasing, natural inflection
- Use: indie, country story-telling, modern pop verse
- Suno keyword: "conversational", "speech-rhythm", "natural inflection"

**Declamatory**:
- Theatrical, emphatic delivery
- Use: musical theatre, dramatic ballad
- Suno keyword: "declamatory", "theatrical", "emphatic"

**Melismatic**:
- Multiple notes per syllable, vocal runs
- Use: R&B, soul, gospel, jazz
- Suno keyword: "melismatic", "with melismatic runs", "vocal runs"

**Behind-the-beat**:
- Lazy phrasing, slightly delayed from grid
- Use: jazz, neo-soul, hip-hop
- Suno keyword: "behind-the-beat phrasing", "laid-back delivery"

**On-grid / On-beat**:
- Precise rhythmic placement, mechanical feel
- Use: EDM, modern pop, K-pop precision
- Suno keyword: "on-beat precise", "rhythmically locked"

**Ahead-of-beat (push)**:
- Slightly anticipating the beat
- Use: rock urgency, punk push
- Suno keyword: "pushing the beat", "urgent forward delivery"

**Detached**:
- Emotionally distant, observational
- Use: synth-pop, alt-pop, modern indie
- Suno keyword: "detached", "cool restrained delivery"

**Passionate**:
- Emotionally intense, full commitment
- Use: ballad climax, gospel, Latin pop
- Suno keyword: "passionate", "emotionally committed"

**Half-spoken (Sprechgesang)**:
- Between speech and song
- Use: rap-vocal hybrid, Bowie-style theatrical, K-pop bridge rap
- Suno keyword: "half-spoken", "speak-sung", "sprechstimme"

**Belted with grit**:
- Power belting with controlled rasp
- Use: rock anthem, soul, modern country
- Suno keyword: "belted with controlled rasp"

### 4.4 Vibrato Specifications

**No vibrato**:
- Straight tone, no oscillation
- Use: indie, modern pop precision, choir blend
- Suno keyword: "no vibrato", "straight tone"

**Subtle vibrato**:
- Light oscillation on sustained notes
- Use: pop, R&B, modern country
- Suno keyword: "subtle vibrato", "controlled vibrato"

**Wide vibrato**:
- Pronounced oscillation
- Use: gospel, soul, classical crossover, K-trot
- Suno keyword: "wide vibrato", "operatic vibrato"

**Slow vibrato**:
- Gradual oscillation rate
- Use: ballad, classical
- Suno keyword: "slow wide vibrato"

**Fast vibrato**:
- Rapid oscillation rate
- Use: classical, some opera, intense moments
- Suno keyword: "fast vibrato"

**Vibrato on long notes only**:
- Straight tone with vibrato emerging on sustained notes
- Use: modern pop standard
- Suno keyword: "straight tone with vibrato emerging on
  sustained notes"

### 4.5 Ornamentation

**Trills**:
- Rapid alternation between two pitches
- Use: classical, opera, some R&B runs

**Grace Notes**:
- Quick passing notes before or after main note
- Use: country, folk, traditional, K-traditional

**Bends / Slides**:
- Sliding into or out of notes
- Use: blues, country, soul, K-traditional sigimsae

**Riffs and Runs**:
- Fast melismatic passages
- Use: R&B, gospel, soul, modern pop bridge
- Suno keyword: "with R&B runs", "gospel-style melismatic riffs"

**Ad-libs**:
- Improvised vocal additions (yeah, oh, mm)
- Use: pop final chorus, gospel, hip-hop, R&B
- Suno keyword: "with ad-libs throughout", "vocal ad-libs in
  chorus and outro"

---

## SECTION 5 — LANGUAGE AND ACCENT

### 5.1 Single-Language Specification

Always specify the primary language explicitly:
- "English lyrics"
- "Korean lyrics"
- "Japanese lyrics"
- "Spanish lyrics"
- "Portuguese lyrics"
- "French lyrics"
- "Mandarin Chinese lyrics"

### 5.2 Code-Switching (Multilingual)

When mixing languages, specify primary and secondary:
- "Korean primary with English chorus phrases"
- "Spanish verse with English hook"
- "Japanese with occasional English phrases"
- "Bilingual Korean-English with English on melodic peak"

**Critical Suno hack**: Place the secondary language on the
melodic peak (chorus hook) for international ear anchoring.
This is K-pop standard for global appeal.

### 5.3 Accent Simulation

Suno does not have a direct accent slider. Accent is achieved
through:

1. Phonetic respelling of lyrics (see `09_SUNO_ENGINE.md`)
2. Style box accent tag

**Common accent tags**:
- "British accent simulation" / "UK accent"
- "Southern American accent" / "Appalachian accent"
- "Jamaican accent" / "Patois inflection"
- "Russian accent" / "Eastern European inflection"
- "French accent" / "Parisian inflection"
- "Spanish accent (Castilian)" / "Spanish accent (Latin American)"
- "Japanese accent (Tokyo)" / "Japanese accent (Kansai)"
- "Korean accent (Seoul standard)" / "Korean accent (Busan
  satoori)"
- "Italian accent"
- "German accent"

**Effective accent tag usage**:
"Male tenor C3-G4 deadpan UK-accented melodic-rap with London
inflection, English lyrics with British colloquialisms"

### 5.4 Korean Vocal Specifics

Korean lyrics in Suno benefit from:
- Specifying "Korean lyrics" or "한국어 가사" in directive
- Including 받침 awareness in lyric prosody (see
  `07_LYRIC_CRAFT_KOREAN.md`)
- For K-pop export-ready style: "Korean primary with English
  chorus hook"
- Avoiding heavy nasal tone (specify "clean clear" for K-pop main
  vocal)

### 5.5 Japanese Vocal Specifics

Japanese lyrics in Suno benefit from:
- "Japanese lyrics with clear vowel articulation"
- Pitch accent rather than stress accent (specify "natural
  Japanese pitch accent")
- For anime-style: "anime J-pop power vocal with melismatic
  ornaments"
- For city-pop: "soft warm J-pop with breath-stops for emphasis"

---

## SECTION 6 — VOCAL LAYERING AND HARMONY STACKS

### 6.1 Single Lead vs Doubled Lead

**Single tracked lead**:
- One vocal track, raw and intimate
- Use: indie, folk, jazz vocal standard, intimate ballad
- Suno keyword: "single tracked lead vocal"

**Doubled lead**:
- Lead vocal recorded/generated twice, panned slightly L/R
- Creates fuller, wider lead without harmony intervals
- Standard in modern pop, K-pop, country choruses
- Suno keyword: "doubled lead with +10 cent detune spread,
  panned 15 degrees L and R"

**Triple-tracked lead**:
- Center + +10 cents right + -10 cents left
- Used in chorus for maximum width
- Suno keyword: "triple-tracked lead with center plus +10 cent
  right plus -10 cent left, panned 20 degrees each side"

### 6.2 Harmony Stack Notation

**+3rd harmony**:
- Voice singing 3rd above lead
- Bright sweetening
- Suno keyword: "+3rd harmony above lead"

**+5th harmony**:
- Voice singing 5th above lead (or +octave -3rd = 6th)
- Open, anthemic
- Suno keyword: "+5th harmony", "+5th and +octave stack"

**+octave harmony**:
- Voice singing octave above lead
- Power, brightness
- Suno keyword: "+octave doubled harmony"

**Standard chorus stack**:
- Center: lead
- L20°: -3rd or unison double
- R20°: +3rd or unison double
- L40°: +5th
- R40°: +octave
- Suno keyword: "layered harmony stack +3rd +5th +octave"

**Unison stack** (no harmonies, just doubles):
- All voices sing same note
- Creates massive single-note presence
- Suno keyword: "unison stacked vocals, multiple takes layered"

### 6.3 Backing Vocal Roles

**Sustained pads** (oo, ah on sustained notes):
- Atmospheric backing under lead
- Suno keyword: "sustained ah-oo backing pad vocals"

**Counter-melody backing**:
- Independent melodic line beneath lead
- Suno keyword: "counter-melody backing vocal in low register"

**Call-response backing**:
- Lead asks, backing answers (or vice versa)
- Use: gospel, soul, K-pop chorus
- Suno keyword: "call-response backing vocals with lead voice
  prominent"

**Echo / repeat backing**:
- Backing repeats end of lead phrase
- Use: classic R&B, doo-wop
- Suno keyword: "echo backing vocals repeating end of phrases"

**Crowd-chant backing**:
- Group shout on hook
- Use: anthem chorus, sports anthem, festival EDM
- Suno keyword: "crowd-chant unison shout on hook"

### 6.4 Choir Specifications

**SATB choir** (Soprano-Alto-Tenor-Bass):
- Mixed-gender 4-part choir
- Use: gospel, classical, cinematic
- Suno keyword: "SATB choir with layered +3 +5 +octave harmonies"

**Female chorus**:
- 3+ female voices
- Use: K-pop, pop ballad
- Suno keyword: "female chorus 3-part harmony"

**Male chorus**:
- 3+ male voices
- Use: classic rock, hymn, traditional
- Suno keyword: "male chorus 4-part harmony hymn-style"

**Children's choir**:
- Children's voices
- Use: cinematic, holiday, choral
- Suno keyword: "children's choir innocent unison"

### 6.5 Cluster Vocal Dissonance (Modern Technique)

Layered vocal harmonies with deliberate semitone clashes for
emotional tension:

- m2 (minor 2nd) below lead: F lead with E sub-layer
- M7 above lead: F lead with E above
- Tritone for maximum dissonance

**Suno keyword**:
"Cluster vocal dissonance with m2 intervals below lead and M7
above on bridge climax phrase only, dissonance layer 6dB below
lead with formant shift and tape saturation"

Use sparingly — bridge moment, not throughout. See
`11_PRODUCTION_DESIGN.md` for full implementation.

---

## SECTION 7 — VOCAL EFFECTS AND PROCESSING

### 7.1 Auto-Tune

**Tasteful auto-tune**:
- Subtle pitch correction, slight quantize
- Use: modern pop, R&B, country crossover
- Suno keyword: "tasteful auto-tune, subtle pitch correction"

**T-Pain / Travis Scott auto-tune**:
- Aggressive pitch quantize, characteristic warble
- Use: trap, hyperpop, modern hip-hop
- Suno keyword: "Travis-Scott-style heavy auto-tune with pitch
  quantize artifacts" or "trap-style auto-tune throughout"

**No auto-tune**:
- Natural pitch, unprocessed
- Use: jazz, folk, indie, country traditional, R&B classic, bossa
- Suno keyword: "no auto-tune, natural unprocessed vocal"

### 7.2 Vocoder

Synthesizer-based vocal processing producing robotic timbres.

- Use: synth-pop, electronic, future-bass hook, hyperpop
- Suno keyword: "vocoder-processed lead vocal", "talkbox-style
  vocal processing"

### 7.3 Formant Shifting

Alters resonance characteristics without changing pitch.

- Slight up shift: brighter, younger character
- Slight down shift: darker, mature character
- Used for backing vocals to differentiate from lead
- Suno keyword: "formant-shifted backing vocal +25 cents up,
  panned L20"

### 7.4 Reverb on Vocals

**Dry vocal**:
- No reverb, intimate close-mic
- Use: hip-hop verse, acoustic intimate, indie close
- Suno keyword: "dry close-mic vocal"

**Plate reverb**:
- Smooth metallic reverb, classic studio sound
- Use: classic pop, soul, jazz
- Suno keyword: "plate reverb on vocal, 1.5 second decay"

**Hall reverb**:
- Long natural decay, spacious
- Use: ballad, anthem chorus, gospel
- Suno keyword: "hall reverb on vocal, 2.5 second decay,
  pre-delay 80ms"

**Spring reverb**:
- Vintage character, slight metallic spring sound
- Use: reggae, dub, vintage country, surf
- Suno keyword: "spring reverb on vocal, vintage character"

**Slap-back delay**:
- Single short echo, 80-150ms
- Use: rockabilly, classic rock and roll
- Suno keyword: "slap-back delay on vocal, 100ms single echo"

### 7.5 Distortion / Saturation

**Tape saturation**:
- Subtle warmth from analog tape modeling
- Use: vintage warmth across genres
- Suno keyword: "tape saturation on vocal, analog warmth"

**Tube saturation**:
- Warm harmonic distortion from tube modeling
- Use: rock, modern pop warmth, gospel
- Suno keyword: "tube saturation on vocal bus, harmonic warmth"

**Heavy distortion**:
- Aggressive vocal distortion
- Use: industrial, metalcore, hyperpop
- Suno keyword: "distorted lead vocal, aggressive saturation"

### 7.6 Compression Character

**Light compression**:
- Subtle leveling
- Use: jazz, indie, classical
- Suno keyword: "lightly compressed vocal, dynamic preserved"

**Tight pop compression**:
- Forward, punchy lead
- Use: modern pop, K-pop, EDM
- Suno keyword: "tight pop compression on lead vocal, forward
  presence"

**Parallel compression**:
- Heavy compression on parallel send blended with dry
- Use: modern pop, R&B, hip-hop
- Suno keyword: "parallel compression on vocal bus -3dB blend"

### 7.7 De-essing and Frequency Refinement

- "De-esser refined 5-8kHz for sibilance control"
- "High-shelf air boost +1.5dB at 12kHz for expensive sheen"
- "Vocal corridor protected 500Hz-3kHz, no instrument intrusion"
- "Notch filter at 2-4kHz on instruments to make space for vocal"

---

## SECTION 8 — SUNO-SPECIFIC VOCAL ENGINEERING

### 8.1 Common Suno Vocal Issues and Fixes

**Issue: Wrong gender output**
Symptom: Requested female, got male (or vice versa)
Fix:
- Place gender at TOP of vocal directive
- Repeat gender keyword 2-3 times in different ways
- Use [Female Vocal] or [Male Vocal] in lyrics if mixed-gender
  song
- Avoid ambiguous vocal range that overlaps both genders

**Issue: Vocal range mismatch**
Symptom: Output goes higher/lower than requested range
Fix:
- Specify range with octave numbers (C4 not just "C")
- Use protection keywords for upper register (sweet light airy)
- Reference singer with that range ("range like Phoebe Bridgers")

**Issue: Husky breakup at high notes**
Symptom: Vocal cracks, screeches, or sounds strained at top
Fix:
- Lower upper range ceiling to F5 (female) or A4 (male chest)
- Add protection keywords: "warm natural human texture, smooth
  breath support, no strain"
- Specify falsetto for high male notes

**Issue: Vocal sounds processed/AI-like**
Symptom: Robotic, over-polished, uncanny valley quality
Fix:
- Add "natural unprocessed vocal" or "no auto-tune"
- Add "warm human texture" or "organic vocal delivery"
- Specify "intimate close-mic" or "live takes preserved"

**Issue: Mumbling or unclear diction**
Symptom: Lyrics inaudible, vocal compressed by instruments
Fix:
- Add "+2dB vocal lift in chorus"
- Specify "vocal forward in mix"
- Hi-pass vocal at 150Hz for high-BPM diction clarity
- Reduce syllables per line if BPM > 130

**Issue: Wrong accent or pronunciation**
Symptom: Korean lyrics garbled, English homographs mispronounced
Fix:
- Use phonetic respelling for problem words (see
  `09_SUNO_ENGINE.md`)
- Add accent specification keyword
- Separate Korean and English into different sections

### 8.2 Vocal Keyword Stacking for Reliability

When a specific vocal characteristic is critical, stack multiple
synonymous keywords:

**Example: protect upper register**
"Female soprano D4-G5, sweet light airy with warm natural human
texture and smooth breath support, no strain in upper register,
crystal clear thin tone"

**Example: lock husky-tinted alto**
"Female alto F3-C5, smoky husky-tinted with controlled rasp and
warm depth, mid-range mezzo character, jazz-influenced cabaret
delivery"

**Example: assertive male tenor**
"Male tenor C3-A4 with chest-projected belt, powerful
forward-placed delivery with controlled vibrato, anthemic
projection on chorus, English with slight rasp on belted notes"

### 8.3 Top-Anchor Approach

Place the most important vocal characteristic at the START of
the directive. Suno's prompt engine weights early tokens more
heavily.

**Less effective**:
"96 BPM acoustic ballad with female alto vocal singing breathy
intimate verses and chorus belt"

**More effective**:
"Female alto vocal, breathy intimate verses opening to chorus
belt, 96 BPM acoustic ballad accompaniment"

The vocal directive should appear as its own clearly delimited
phrase, not buried inside the genre/instrumentation description.

### 8.4 Suno Persona System (Pro/Premier)

Suno Pro and Premier tiers offer Persona feature to save vocal
identity across multiple songs:

1. Generate one song with desired vocal
2. Save as Persona in Suno interface
3. In subsequent prompts, reference Persona name + simpler prompt
4. Suno reuses vocal identity for consistency

This is the most reliable way to maintain vocal consistency
across an album or project.

### 8.5 Gender-Switching Within One Song

For songs with multiple vocalists (duet, K-pop multi-member):

- Use [Verse 1 - Female Vocal] / [Verse 2 - Male Vocal] section
  tags
- Repeat gender keyword in [Singing:] cue per section
- Specify each vocalist's full 5-element directive in style box

**Example**:
"Duet: Female alto verse 1 (range A3-D5, warm intimate timbre,
breathy delivery, English) and Male tenor verse 2 (range D3-G4,
husky warm timbre, conversational delivery, English).
Both vocals on chorus with +3rd harmony stack."

---

## SECTION 9 — REFERENCE ARTIST VOCAL TYPES

When using [Artist-Song-style] encoding, the following catalog
maps reference artists to vocal classifications:

### Female Vocalists

**Soprano (high)**:
- Mariah Carey (high soprano with whistle register)
- Ariana Grande (high soprano with melismatic R&B style)
- IU (Korean soprano with versatile timbre)
- LiSA (anime power soprano)
- Florence Welch (operatic soprano with theatrical projection)

**Mezzo-Soprano (mid-high)**:
- Adele (mezzo with chest-dominant power belt)
- Beyoncé (mezzo with versatile R&B/pop range)
- Norah Jones (smoky mezzo with jazz inflection)
- Taylor Swift (mezzo with country-pop crossover)
- Olivia Rodrigo (mezzo with modern pop style)

**Alto / Contralto (low)**:
- Amy Winehouse (alto with retro soul timbre)
- Lana Del Rey (alto with breathy noir style)
- Phoebe Bridgers (alto-mezzo with intimate indie style)
- Billie Eilish (alto with whispered intimate style)
- 백예린 (Korean alto with sophisticated indie style)

### Male Vocalists

**Countertenor / High Tenor**:
- Jacob Collier (countertenor with extreme range and harmonic
  sophistication)
- Jeff Buckley (high tenor with falsetto-heavy ethereal style)
- Justin Vernon / Bon Iver (high tenor with falsetto stacks)

**Tenor**:
- The Weeknd (tenor with falsetto-heavy R&B/synth-pop)
- Sam Smith (tenor with falsetto-heavy soul/pop)
- Daniel Caesar (tenor with falsetto-heavy R&B)
- BTS Jungkook (Korean tenor with versatile pop range)
- Frank Ocean (tenor with conversational R&B style)

**Baritone**:
- Hozier (baritone with rich folk-rock projection)
- John Legend (baritone with smooth R&B/soul)
- Leon Bridges (baritone with retro soul timbre)
- Chris Stapleton (baritone with country-blues grit)

**Bass / Bass-Baritone**:
- Johnny Cash (bass-baritone with deep American storytelling)
- Leonard Cohen (bass with intimate spoken-poetic style)
- Barry White (bass with deep velvet R&B)

---

## SECTION 10 — APPLICATION GUIDE

### 10.1 Building a Vocal Directive Step-by-Step

Step 1: Identify gender (single voice or group)
Step 2: Determine voice type and range (consult Section 2)
Step 3: Choose 2-3 timbre adjectives (consult Section 3)
Step 4: Specify delivery and attitude (consult Section 4)
Step 5: Specify language and accent (consult Section 5)
Step 6: Add layering/harmony specs if applicable (Section 6)
Step 7: Add effects/processing if needed (Section 7)
Step 8: Verify completeness with the 5-element check
Step 9: Place directive at top of style box (top-anchor approach)

### 10.2 Common Pitfalls

- **Missing one of 5 elements**: Always include all 5 even for
  brief directives
- **Range too wide**: 3+ octaves causes inconsistent character
- **Contradictory timbre adjectives**: "powerful breathy" or
  "operatic conversational"
- **Genre-vocal mismatch**: contralto in K-pop context, soprano
  in death metal
- **Forgetting accent for bilingual**: assume Suno will get
  Korean accent right when generating Korean lyrics
- **Burying vocal directive**: place as separate phrase, not
  embedded in genre description
- **Over-stacking effects**: 5+ effects keywords cause prompt
  fatigue

### 10.3 Quality Verification

Before finalizing vocal directive, verify:
- ☐ Gender stated explicitly
- ☐ Range with octave numbers (C4-F5 format)
- ☐ Timbre with 2-3 adjectives, no contradictions
- ☐ Delivery/attitude specified
- ☐ Language stated, accent if applicable
- ☐ Range respects Suno ceiling (F5 female / A4 male without
  falsetto, unless protection keywords applied)
- ☐ Top-anchored at start of style box
- ☐ Layering/harmony notation if used
- ☐ Effects/processing keywords match genre

---

## REFERENCES AND FURTHER READING

The information in this file synthesizes from the following:

- Yale University Library vocal range classification reference
- OperaVision voice type pedagogy
- BBC Maestro vocal timbre education
- Synchro Arts vocal layering production tutorials
- Sage Audio formant and pitch technique reference
- Berklee Online vocal production curriculum
- Suno official documentation and community discussions
  (r/SunoAI, Suno style catalog)
- HookGenius Suno prompting guides
- Production engineer interviews (Sound on Sound, Tape Op,
  MixOnline)
- Vocal coach educational content (Voice Lessons, Singing Tips,
  contemporary vocal pedagogy YouTube channels)
- The Voice Foundation classification standards
- Genre-specific vocal style guides (R&B Runs, Gospel Vocal
  Stylings, K-pop vocal direction analyses)

For Suno-specific keyword conventions and engine quirks, see
`09_SUNO_ENGINE.md`.

For lyric structure tags and [Singing:] cue library, see
`10_SUNO_LYRICS_TAGS.md`.

For Korean lyric prosody and 받침 considerations affecting
vocal delivery, see `07_LYRIC_CRAFT_KOREAN.md`.

For English lyric meter and stress placement considerations,
see `08_LYRIC_CRAFT_ENGLISH.md`.

<!-- USER EXTENSION ZONE — append additional vocal techniques,
     reference artists, or genre-specific vocal notes below -->

---




---

## SECTION 11 — VOCAL ANCHOR PROTOCOL (NEW v2.7)

### 11.1 What Vocal Anchor is

External research (Suno Field Guide 2026): Suno v5 **determines vocal
character within the first 1-2 seconds** of generation. Without an
anchor at the top of the Lyrics field, vocal character is random.

A Vocal Anchor is a single bracket tag, placed as the **first line**
of the Lyrics field, that locks Suno's vocal interpretation before
any musical content begins.

### 11.2 Anchor placement

Mandatory position: **top of Lyrics field, before any section tag**.

```
[Vocal: ...] ← Anchor here, line 1

[Intro 8]
...
```

Not below section tags. Not in Style Box. Lyrics field, line 1.

### 11.3 Single-vocal Anchor template

```
[Vocal: <gender> <range>, <main timbre>, <range-by-section behavior>,
<genre inflection>, <special technique>.]
```

5-element formula:
1. Gender + range
2. Main timbre (1-2 adjectives)
3. Range-by-section behavior (verse vs chorus dynamics)
4. Genre inflection (which singing tradition)
5. Special technique or constraint (optional)

Examples:

```
[Vocal: female alto, smooth and soulful, airy on quiet lines,
powerful natural belting on peaks, contemporary R&B inflection,
slight vocal fry on phrase ends.]
```

```
[Vocal: male tenor, gritty and lived-in, conversational on verses,
explosive on choruses, classic rock inflection, no melisma.]
```

```
[Vocal: female mezzo-soprano, clear and bright, restrained on
verses, full-voiced on chorus, K-pop modern inflection, occasional
fast vibrato narrow.]
```

### 11.4 Duet Vocal Anchor template

Two separate anchors, one per vocal:

```
[Vocal 1 (Serica): female soprano C4-E5, clear calm polite voice,
refined gentle, K-pop ballad inflection, no vocal fry,
no descending phrase-end curls.]
[Vocal 2 (Cheny): female high soprano E4-G5, child-like punk-rap,
sweet light airy texture, warm natural human warmth, occasional
shouting on hook peaks, no descending phrase-end curls.]
```

Then in body, line-level labels (10 §19):
```
[V1] line by vocal 1
[V2] line by vocal 2
[V1+V2] both together
```

### 11.5 Character names in anchors

Operator's named characters (Serica / Cheny / 테피 / 우나 / 크래더 /
봉남이):
- Anchors only — `(Serica)` inside brackets
- *Never* in Style Box
- Body uses V1/V2 labels, not character names

### 11.6 Anti-patterns

```
✗ Anchor in Style Box ("female alto, soulful, airy")
   → Style Box mentions are weaker; can leak into vocal output
✗ "vocal 1:" prefix syntax
   → not recognized by Suno parser
✗ Character names without bracket
   → ignored by parser
✗ Anchor after [Intro] or [Verse 1]
   → too late; vocal already determined
✗ Anchor with 10+ adjectives
   → parser confuses, drops parts
```

### 11.7 Anchor failure recovery

Operator reports "vocal came out wrong":
1. Check anchor is line 1
2. Check 5 elements present
3. Reduce to 3 most essential elements
4. Add explicit *negation* in special technique slot
   ("no vocal fry, no melisma, no descending curls")
5. If still wrong: anchor + Style Box "smooth pop vocal" reinforce

### 11.8 Range markers (operator-verified)

Use Hz / pitch notation in anchor for precise range:

| Range | Notation |
|---|---|
| Soprano | `C4-E5` or `C4-A5` |
| Mezzo-soprano | `A3-F5` |
| Alto | `F3-D5` |
| Tenor | `C3-A4` |
| Baritone | `A2-F4` |
| Bass | `E2-D4` |

For range extension (operator's Cheny: needs to reach G5):
```
[Vocal 2 (Cheny): female high soprano E4-G5, ...]
                  ↑ extended high range marked
```

### 11.9 Anchor + Style Box consistency

Anchor must NOT contradict Style Box:
- Anchor: female alto / Style Box: male vocals → conflict, random output
- Anchor: smooth / Style Box: aggressive vocal → conflict
- Anchor: R&B inflection / Style Box: country vocals → conflict

Solution: Style Box mentions vocal only if matching anchor, or omit
entirely from Style Box (anchor carries the directive).

### 11.10 Integration with 09 §25

This section is the *vocal-craft* side of Vocal Anchor protocol.
09 §25 is the *engine-level* side.

Use both together:
- 06 §11 = how to write the anchor text
- 09 §25 = where to place it / how Suno processes it
- 10 §19 = line-level vocal labels in the body

---

# END OF VOCAL PRODUCTION

---

## SECTION 12 — VOCAL TECHNIQUE PROFESSIONAL VOCABULARY (v2.11 NEW)

This section is a Suno-tested vocabulary library for vocal direction.
Operator's request: *"발성·톤 같은 것 등등 좀 전문적인 지식이 보충
되어야 할 거 같은데"* — addressed here.

### 12.1 Voice register taxonomy

| Register | Range zone | Vocabulary |
|---|---|---|
| **Vocal fry** | Lowest, creaky | `vocal fry on phrase ends`, `creaky low register`, `glottal fry texture` |
| **Chest voice** | Speaking range, full body | `chest voice belt`, `chest-resonant`, `full-body chest delivery`, `grounded chest tone` |
| **Mixed voice** | Bridge between chest/head | `mixed voice`, `chest-mix on peaks`, `blended register`, `bridge register lift` |
| **Head voice** | High, light, no chest | `head voice`, `light head register`, `airy head voice` |
| **Falsetto** | Highest male/female, breathy edge | `falsetto runs`, `airy falsetto`, `flute-like falsetto` |
| **Whistle register** | Above head voice (rare) | `whistle register`, `coloratura whistle peaks` |

### 12.2 Timbre adjectives (Suno-tested)

**Brightness:**
- `bright` / `crystalline` / `clear` / `pristine` / `silver-toned`
- `dark` / `smoky` / `husky` / `velvety` / `golden`

**Texture:**
- `breathy` / `airy` / `whispered` / `intimate`
- `raspy` / `gravelly` / `gritty` / `weathered`
- `silken` / `creamy` / `buttery` / `silken-smooth`
- `nasal` / `pinched` / `cutting`

**Weight:**
- `light` / `feathery` / `weightless` / `delicate`
- `heavy` / `grounded` / `chest-weighted` / `solid`
- `powerful` / `commanding` / `bold` / `triumphant`

**Color:**
- `warm` / `golden` / `honey-toned`
- `cold` / `glassy` / `metallic`
- `earthy` / `rooted` / `organic`

### 12.3 Delivery style descriptors

**Pace:**
- `behind-the-beat` (laid back, conversational)
- `on the grid` (precise, locked)
- `pushed forward` (urgent, leaning into beat)
- `rubato` (free time, no metronome)

**Connection:**
- `legato` (smooth, connected notes)
- `staccato` (separated, punchy)
- `marcato` (accented each note)

**Phrasing:**
- `conversational` (speech-like)
- `melismatic` (note-runs on one syllable)
- `straight tone` (no vibrato)
- `vibrato-rich` (oscillating pitch)
- `bend` (slide into note)
- `slide` (portamento between notes)

**Articulation:**
- `crisp consonants` (clear diction)
- `slurred` (lazy enunciation)
- `accented R/T/D` (rhythmic emphasis)
- `soft attack` (gentle note onset)
- `hard attack` (punchy note onset)

### 12.4 Emotional intent vocabulary

Mapped to vocal directions:

| Intent | Vocal direction |
|---|---|
| Longing | `aching falsetto`, `breathy upper register`, `vibrato-rich sustains` |
| Anger | `chest-belted shout`, `growl on phrase ends`, `staccato attack` |
| Tenderness | `whispered`, `soft head voice`, `intimate close-mic delivery` |
| Joy | `bright legato runs`, `playful staccato`, `head-voice trills` |
| Sadness | `vocal fry tail`, `breathy descending phrases`, `held notes with fade` |
| Confidence | `chest-belted declarative`, `straight tone`, `pushed-forward placement` |
| Vulnerability | `cracked voice`, `breath-leaking sustains`, `quivering vibrato` |
| Defiance | `nasal sassy edge`, `cutting upper register`, `accented R/T/D` |

### 12.5 Vocal styles by genre lineage

**Modern Pop / Top 40:**
- Polished diction, mixed-voice belt on chorus, light vocal fry on
  phrase ends, autotune as texture (or `no autotune` for raw)

**Modern R&B:**
- Melismatic runs, breathy upper register, ad-lib heavy, vocal fry
  prominent

**Indie / Alt:**
- Vocal fry, breathy intimate, head-voice prominent, raw less-polished
  texture

**Country / Folk:**
- Twangy nasal placement, vibrato-rich, conversational verse, belted
  chorus

**Hip-hop / Rap:**
- Spoken-word delivery, rhythmic syllable density, ad-libs
  (`yeah / uh / let's go`), vocal layering on hooks

**Hyperpop:**
- Pitched-up crystalline, robotic precision, autotune as feature,
  ad-libs glitched

**Hardstyle / Festival EDM:**
- Female: powerful belt on chorus, breathy verses, vocoder-treated
  ad-libs
- Male: chest-shouted hook, declamatory, anthem-style

**Trot (트로트):**
- Kkeokgi (꺾기) — phrase-end bend
- Ppongki (뽕끼) — dramatic flair
- Modern crossover: cleaner production, less vibrato

**City Pop / J-Pop:**
- Clear diction, light vibrato, conversational + delicate, head-voice
  prominent

### 12.6 Cross-language considerations

**Korean (한국어):**
- 받침 (final consonant) clarity affects diction
- 어절 spacing = breath unit
- 모음조화 (vowel harmony) affects mimetic word choice
- Use `crisp Korean consonant diction` / `Korean-language vocal topline`

**English:**
- Stress on strong beats (trochaic preferred)
- R-coloring choice (American vs British)
- Use `American English diction` / `British English vowel quality`

**Japanese:**
- Mora-timed phrasing
- Pitch accent on key words
- Use `Japanese-language vocal topline with mora-timed phrasing`

**Spanish:**
- Sinalefa (vowel elision across words)
- Rolled R / soft R choice
- Use `Spanish-language vocal with sinalefa-aware phrasing`

### 12.7 Cross-reference

- 06 §11 — 5-element Vocal Anchor (basic)
- 06 §13 — Range-to-timbre mapping (v2.11 NEW)
- 06 §14 — Persona system integration (v2.11 NEW)
- 10 §21.5 — Suno-tested vocal direction library
- 09 §25 — Vocal Anchor official syntax

---

## SECTION 13 — RANGE-TO-TIMBRE MAPPING (v2.11 NEW)

External research synthesis: vocal range vs natural timbre tendencies.

### 13.1 Female ranges

| Range | Standard label | Typical timbre default |
|---|---|---|
| F3-D5 | Contralto / low alto | Dark, husky, chest-grounded |
| G3-E5 | Alto | Warm, grounded, chest-mix natural |
| A3-F5 | Mezzo-soprano | Versatile, balanced |
| B3-G5 | Soprano | Bright, light, head-voice natural |
| C4-A5 | High soprano | Clear, ethereal, head-dominant |
| D4-C6 | Coloratura | Agile, ornamented, head/whistle |

### 13.2 Male ranges

| Range | Standard label | Typical timbre default |
|---|---|---|
| D2-A3 | Bass | Deep, resonant, chest-grounded |
| E2-C4 | Bass-baritone | Rich, warm, authoritative |
| F2-D4 | Baritone | Versatile, conversational |
| G2-E4 | Tenor | Bright, lifted, mixed natural |
| A2-F4 | Lyric tenor | Clear, agile, head-voice access |
| B2-G4 | High tenor / Countertenor | Light, ethereal, falsetto natural |

### 13.3 Operator catalog application (24 characters)

Map operator's 24 characters to range-timbre defaults:
- Each character → range label + 1-2 timbre descriptors
- Stored in 99_OPERATOR_VAULT Part B baseline (already exists)
- v2.11 expansion: link to §12.2 timbre vocabulary for consistency

### 13.4 Cross-reference

- 99_OPERATOR_VAULT Part B (캐릭터 베이스라인) — 24-character baseline (range info)
- 06 §11.8 — Range markers operator-verified
- 06 §12 — Timbre vocabulary

---

## SECTION 14 — SUNO PERSONA SYSTEM INTEGRATION (v2.11 NEW)

External verification (Suno v5.5 docs, arkiii Suno Personas guide
2026).

### 14.1 What Suno Personas are

Persistent voice profiles trained from operator-uploaded vocal samples.
Once trained, applied to future songs for consistent vocal identity.

**Tier requirements:**
- Free tier: Not available
- Pro tier: Personas available
- Premier tier: Personas + Custom Models + Studio

### 14.2 Why operator catalog benefits

Operator has 24 characters defined in 99_OPERATOR_VAULT Part B baseline. Each character
could become a Suno Persona:
- Series continuity (same character across songs = consistent voice)
- Reduces re-prompting friction
- Cross-references character baseline more directly to Suno output

### 14.3 Persona creation workflow

```
1. Pick a character (e.g. Cheny / Serica / 봉남)
2. Generate 3-4 short song sections (8-16 bars each) in:
   - Different tempos (slow ballad, mid-tempo pop, uptempo dance)
   - Different keys (low chest, mid range, high belt)
   - Both soft + powerful delivery
3. Clean audio: no reverb, no background music, no other voices
4. Upload to Suno → Train Persona
5. Save Persona ID associated with character name
6. Future songs: Apply Persona ID + character Vocal Anchor
```

### 14.4 Persona Stacking framework

External verification (arkiii guide 2026):
> *"Most Personas drift or feel ignored — design problem, not prompt
> problem. Persona Stacking is the system."*

**Three-layer stack:**
1. **Persona** (voice identity)
2. **Vocal Anchor 5-element** (06 §11 — performance instruction)
3. **Style Box** (genre/production context)

All three reinforce same character → max coherence.

### 14.5 Persona drift recovery

If Persona output starts drifting:
- Strengthen Vocal Anchor 5-element (more specific timbre descriptors)
- Lower Style Influence slider (less genre push)
- Re-train Persona with cleaner / more varied samples

### 14.6 Cross-reference

- 00 C-49 — Voice / Persona / Studio v5.5 integration
- 09 §33 — Persona system technical details
- 99_OPERATOR_VAULT Part B (캐릭터 베이스라인) — 24-character baselines (Persona candidates)
- 10 §21.6 — Persona Stacking framework

---

# END OF 06_VOCAL_PRODUCTION v2.11


## § USER EXTENSION ZONE v2.0 (2026-05-24)

bitwize voice-tags 19종 + SJY051 vocals 풀바디 통합.


### §UE-1. Vocal Style Tags 19종 (bitwize 풀바디)

```
| Tag | Description |
|-----|-------------|
| Staccato | Short, detached notes |
| Legato | Smooth, connected notes |
| Vibrato-heavy | Strong pitch oscillation |
| Monotone | Flat, single-pitch delivery |
| Melismatic | Multiple notes per syllable |
| Syncopated | Off-beat rhythmic emphasis |
| Operatic | Classical opera style |
| Chanting | Repetitive, ritualistic |
| Spoken-word | Speech-like delivery |
| Growling | Aggressive, guttural |
| Belting | Powerful, projected singing |
| Yodeling | Rapid pitch changes |
| Humming | Closed-mouth singing |
| Rapping | Rhythmic speech |
| Scatting | Jazz vocal improvisation |
| Falsetto runs | High-pitched runs |
| Yelping | Sharp, cry-like sounds |
| Grunting | Low, forceful sounds |
| Call-and-response | Interactive vocal pattern |
```


### §UE-2. Vocal Texture Tags (bitwize)

```
- Breathy / Airy
- Raspy / Gritty
- Smooth / Silky
- Powerful / Robust
- Intimate / Whispered
- Ethereal / Floating
- Soulful / Bluesy
- Aggressive / Forceful
- Tender / Soft
- Confident / Strong
```


### §UE-3. V5 Voice Gender Selector (bitwize)

**V5 Advanced Options에 *Voice Gender* selector (male/female):**
- *Most reliable gender control* — Style Box 묘사보다 일관적
- Style Box "male baritone" 또는 Personas 활용도 가능
- Advanced Options가 *baseline*


### §UE-4. Vocal Anchor 5-element 외부 검증 (C-29 통합)

```
1. Gender + range (필수)
2. Main timbre 1-2 adjectives (필수)
3. Range-by-section behavior (필수)
4. Genre inflection (필수)
5. Special technique or negation (옵션)
```

**Top-Anchor Approach** (v5-best-practices §Vocal Control):
*"Start your prompt with vocal description before lyrics"*

→ Position 1 자리 vocal-first 가능 (C-45 통합)


### §UE-5. Mixed Group Vocals (K-pop 직격)

```
1번 키워드: "mixed group vocals"
- K-pop multi-member 시뮬레이션 가장 중요한 태그

밀도 보강:
- "layered harmonies"
- "gang vocals"
- "group chant"

섹션 태그:
- [All] / [Group] (chant 자리)
- [Rap Verse] (rap line)
- [Dance Break] (instrumental + minimal lyrics)
```


### §UE-6. Section-by-Section Dynamics (v5-best-practices)

```
| Section | Dynamics | Phrasing | Vibrato |
|---|---|---|---|
| Verse | Low | Tight | Minimal |
| Pre-Chorus | Rising | Shorter | Growing |
| Chorus | High/Open | Sustained | Full |
| Bridge | Variable | New texture | Altered |
```


### §UE-7. Non-Human Character Voices (C-69)

```
외계인: "alien metallic crystalline overlapping whispering"
로봇: "robotic monotone vocoder synthetic glitchy compressed"
동물 (늑대): "wolf howl growling primal beast-throat raw"
신화 존재: "ethereal otherworldly haunting echoing immortal divine"

5-8 adjectives 동시 박음 → Suno 비인간 결로 해석.
```


# === END 06 USER EXTENSION ZONE v2.0 ===



