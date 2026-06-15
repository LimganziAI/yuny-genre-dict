# files(27) Style Ratio / MJ-style / Dense Prompt Mining V1

Date: 2026-06-13
Source: Claude files(27) linkage workbook and deduped Suno metadata
Status: candidate prompt-mining notes. Not final canon.

## Why this matters
The recent metadata shows that some older/current Suno prompts were much denser and more executable than the weaker Hibiscus drafts. Useful patterns include:
- percentage blend ratios
- MJ-style rhythmic seasoning
- range anchors
- harmonic/key anchors
- instrument articulation
- stereo/frequency placement in high-energy covers
- cover preserve/transform language

This file records prompt-shape lessons for future packages.

## 1. Percentage blend patterns
Observed useful form:
`primary genre 45-70% + secondary color 20-35% + seasoning 5-15%`

Examples from metadata:
- `65% K-indie / 25% ambient folk / 10% neo-classical`
- `55% K-indie acoustic pop / 30% light city pop groove / 15% lyrical dream pop`
- `60% UK garage 2-step / 25% acoustic breakbeat / 15% J-rock`
- `45% nu-disco / 30% J-electro / 15% dnb / 10% MJ style`
- `K-indie pop rock 45% / Mrs Green Apple bright modern J-rock chorus engine 35% / MJ style seasoning 15% / subtle electronic texture 5%`

Use cases:
- Good when user asks for hybrid reference lanes.
- Good when preserving a main lane while adding only a flavor.
- Good in CREATE for bone identity, and in COVER for target transformation ratio.

Rules:
- Percentages should describe sound-function, not name soup.
- One primary lane must dominate.
- 5-15% seasoning is useful for rhythm/ad-lib/pocket/MJ style.
- Do not use percentages when the song is already narrow and intimate; it may overcomplicate the prompt.

## 2. MJ-style pattern
`MJ style` appears in useful forms as rhythm/pocket/ad-lib seasoning, not usually as the whole genre.

Observed functions:
- staccato pocket
- syncopated slap/funk bass
- rhythmic ad-libs
- sharp phrase endings
- dance-pop groove control
- pop-funk articulation

Good prompt form:
- `MJ-style rhythmic pocket seasoning 10-15%`
- `MJ-staccato funk pocket, used as groove articulation only`
- `syncopated pop-funk bass and clipped phrase endings, not impersonation`

Avoid:
- direct artist imitation as identity
- making MJ the main vocal identity
- using MJ style where the character/vocal does not need funk-punctuation

## 3. Dense create prompt shape that worked
Strong CREATE prompts often include:
1. genre blend or ratio
2. BPM and key
3. chord progression or tonal motion
4. vocal range anchor and character of delivery
5. melody behavior or hook event
6. 3-5 instruments with articulation
7. section arc or final lift
8. mix/finish line

Example template:
`K-indie pop rock 45% with bouncy syncopation, modern J-rock chorus engine 35%, MJ-style groove seasoning 15%, subtle electronic texture 5%, 148 BPM, A major with chromatic mediant A to F hook drop, female mezzo-soprano A3-E5 bright husky tone, raspy break only on chorus peaks, clean Korean diction, bright pick-attack guitars, bouncy bass, punchy live-pop drums, clean studio vocal-forward mix.`

## 4. Dense cover prompt shape that worked
Strong COVER prompts often specify:
- maintain exact melody/timing/BPM when preservation is needed
- transform/refine target
- vocal layer architecture
- instrument substitution with frequency/stereo where useful
- ducking or vocal-forward corridor
- clear final/master quality

Useful high-energy cover language:
- `Maintain exact melody BPM and lyric timing`
- `lead vocal 2-4kHz CENTER dominant clear diction`
- `double vocal center support; harmony wide; chant response right-side only`
- `all duck 2-4kHz vocals forward`
- `wide stereo modern production, tight low end, crystal separation`

Caution:
Frequency/stereo language is useful for high-energy dense covers, but can be overkill or artificial for intimate K-indie songs.

## 5. Vocal range anchor lesson
Prompts often became more stable when using specific anchors:
- female soprano C4-F5
- female mezzo-soprano A3-E5
- female alto / low mezzo when darkness is wanted
- male tenor / mid-high scratchy tenor

But range anchors must be paired with melody firewall when only tone changes:
`preserve topline contour, chorus lift, phrase lengths, lyric timing; change vocal color only.`

## 6. Instrument articulation lessons
Good prompts name how instruments play, not only instrument names:
- `close bright upright piano, small repeating two-note motif, light broken eighths, soft pedal`
- `light brushed drum kit with soft kick, snare sweeps, rim taps`
- `round palm-muted picked bass, short warm notes, gentle eighth-note lift`
- `clean muted electric guitar offbeats and high arpeggio answers`
- `Telecaster 16th-note funk scratches with wah-wah pedal`
- `slap-pop bass ghost notes syncopated`
- `offbeat octave synth bass for TechPara only`

## 7. What to promote into runtime
Candidate runtime rules:
1. Percentage ratio allowed and useful for hybrid lanes.
2. MJ-style should be treated as groove/ad-lib seasoning, not identity imitation.
3. Serious prompts must approach the 1000-character budget with execution value.
4. Cover prompt must be as engineered as create prompt.
5. Frequency/stereo/layer language is optional but valuable for dense covers.
6. Intimate songs should use quality-stack language more than frequency spam.
7. Prompt examples from metadata are vocabulary banks, not automatic final truth.

## Open questions for user
1. When you say `MJ style`, which function matters most to you: groove pocket, ad-lib behavior, bass articulation, phrase ending, or dance-pop polish?
2. Do you want percentage-ratio prompts used regularly for hybrid genres, or only when reference blending is explicit?
3. For high-energy covers, do you like the very technical `2-4kHz CENTER / HARD-L / ducking` style, or should YUNY translate it into more natural Suno language unless the mix is failing?
4. Which characters should get official percentage/style bundles first: Bongnam, Marie, Sally/ex-Sally, Tatoo, Luke/Kreather, Martina, Kashas?
5. Are there any recent prompts you remember as especially successful that should become gold examples?
