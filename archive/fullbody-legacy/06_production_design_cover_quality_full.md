# ACTIVE GPT ROUTE HEADER
- Current GPT file: `06_production_design_cover_quality_full.md`
- Purpose: Production design and full COVER quality stack
- Preserved source aliases: 11_PRODUCTION_DESIGN, 20_PRODUCTION_AWARE
- Use rule: Use for every COVER quality/mix/space/frequency issue. Must supply 7-zone, vocal corridor, tube/tape sat, de-ess, sidechain, transient, LUFS targets when relevant. Together: 02,05,03.
- Cross-link rule: Follow `instructions.txt` first. Legacy `# SOURCE:` blocks below are source provenance, not current routing names. If retrieval is thin, search this file by both current terms and preserved source aliases.

---

# v2.2 routing reinforcement
If the user reports harsh, painful, muddy, thin, buried, distorted, or low-quality COVER output, do not invent a new song. Keep the current CREATE/COVER context lock, preserve the declared hook/topline/duet/section/modulation/micro-bends/signature motif, then rebuild the COVER prompt using: target genre micro-anchor -> preserve map -> substitution map -> vocal identity -> section events -> full production-aware quality stack -> final/outro preservation. For Genre-Transform, quality is mandatory but does not replace the genre anchor.

---

# Active GPT patch: COVER quality full prescription
Every COVER is the final-quality form. For audio-quality failure or any serious COVER, retrieve this file and include more than a token "mono sub/glossy air" line. Required production-aware vocabulary includes:
- vocal organic bus + corridor + warmth
- remove digital artifacts / mechanical edge from lead vocal
- natural human breath texture restored
- warm analog tube saturation on vocal bus
- doubled/organic width such as +8 cent detune L15/R15 when appropriate
- vocal corridor 500Hz-3kHz protected
- de-esser 5-8kHz
- sub-bass mono 20-80Hz
- separated kick and bass center
- sidechain bass to kick around 80ms for dance/EDM when useful
- carved 200-400Hz low-mid mud
- smooth 2-5kHz high-mids
- controlled 8-14kHz air without harshness
- stereo L/R instrument placement and depth
- reverb/delay tails controlled, not washed out
- transient punch, bus glue compression, tape saturation 1-2% or master tape saturation when useful
- loudness target by genre; streaming -14 LUFS / -1 dBTP, or club/dance -6~-8 LUFS only when desired
In Genre-Transform, place this stack after genre/preserve/substitution/vocal/section content. Do not start with Quality-rescue unless the task is explicitly Texture-Refine/repair only.

---

# SOURCE: 11_PRODUCTION_DESIGN.md

11. PRODUCTION DESIGN — Macro & Micro Sound Architecture
Version: 1.0 Last Updated: 2026-04-30 Load Trigger: When designing arrangement, mix character, frequency balance, dynamic arc, or stereo image — typically during COVER prompt construction. Companion Files: 04_RHYTHM_AND_FORM.md, 05_GENRE_LIBRARY.md, 09_SUNO_ENGINE.md

SECTION 0. PURPOSE
This file teaches the system to think like a producer, not just a songwriter. It governs how a track sounds — frequency distribution, dynamic shape, stereo image, density curve, and mix character — independent of melody and lyric. These are the variables that turn a good song into a finished record.

This file is consulted heavily during:

COVER prompt construction (where production character is the main input).
Hybrid genre design (where competing frequency ranges must be separated).
Diagnosing why a generation sounds "small," "muddy," "thin," or "amateur."
SECTION 1. THE TWO LEVELS OF DESIGN
1.1 Macro Design (Song Level)
The arc of the entire track. Concerns:

Energy curve from intro to outro
Density progression (sparse → full → sparse)
Section-to-section contrast
Climax placement
Length and pacing
1.2 Micro Design (Section Level)
The internal architecture of each section. Concerns:

Frequency distribution within the section
Stereo placement of each element
Layer count and role of each layer
Dynamic envelope of the section
Transition into and out of the section
A great track has both: macro arc that pulls the listener through, and micro detail that rewards close listening.

SECTION 2. THE ENERGY CURVE
2.1 The Universal Shape
Almost every successful song follows a variation of this curve:

Energy
  │                              ╱╲          ╱╲
  │                          ╱╲ ╱  ╲    ╱╲ ╱  ╲
  │                      ╱╲ ╱  V    ╲  ╱  V    ╲
  │                  ╱╲ ╱  V         V          ╲
  │              ╱╲ ╱  V                         ╲
  │      ___╱╲ ╱                                  ╲___
  │   __╱     V                                       __
  └─────────────────────────────────────────────────────────►
   Intro  V1  PC  C1  V2  PC  C2  Bridge  Final C   Outro
Key principles:

Start lower than your final climax. Reserve top energy for the final chorus or last drop.
Each chorus should be slightly bigger than the previous. Layer addition, harmony stacking, or production density increase.
Bridge is a release, not a peak. Pull energy down before the final climax for maximum impact.
Outro descends. Even an "anthemic" outro descends from the final chorus peak.
2.2 Energy Tools (How to Add or Subtract Energy)
To increase energy without raising volume:

Add a layer (harmony vocal, strings, percussion fill)
Activate a frequency range (sub-bass enters, hi-hats double-time)
Tighten the rhythm (16th-note hat, snare ghost notes)
Widen the stereo image
Add reverb tail or delay throw on the lead vocal
Add an octave double on the bass or melody
To decrease energy:

Remove drums (dropout)
Strip to one or two instruments
Narrow the stereo image (push elements to center)
Tighten reverb (less tail, more dry)
Drop an octave on bass or melody
Shift to half-time feel
2.3 The Six Energy States
Every section sits in one of six energy states. Use these as design vocabulary:

Sparse intimate — one or two instruments, dry, narrow stereo, low density.
Rising warm — building, layers entering one at a time, mid-density.
Full balanced — typical pop chorus density, all instruments active, wide stereo.
Climactic dense — final chorus with stacked harmonies, double percussion, max width.
Tension hold — full instruments but compressed dynamics, sense of pressure.
Release/breath — sudden drop in density, often after climax or before final chorus.
A well-designed track moves through 4-5 of these states across its length.

2.4 Section-by-Section Energy Map (Standard Pop)
Section	Energy State	Typical Density
Intro	Sparse intimate or Rising warm	20-40%
Verse 1	Sparse intimate	30-40%
Pre-Chorus 1	Rising warm	50-60%
Chorus 1	Full balanced	70-80%
Verse 2	Rising warm	40-50%
Pre-Chorus 2	Rising warm	60-70%
Chorus 2	Full balanced (slightly fuller)	75-85%
Bridge	Tension hold or Release/breath	40-60%
Final Chorus	Climactic dense	90-100%
Outro	Release/breath	30-50%
SECTION 3. FREQUENCY ARCHITECTURE
3.1 The Six Frequency Zones
Every mix occupies a frequency spectrum from roughly 20 Hz to 20 kHz. Six functional zones to design around:

Zone	Frequency Range	Function	Typical Occupants
Sub-bass	20-60 Hz	Body, weight, physical impact	Sub-bass synth, kick fundamental, 808
Bass	60-250 Hz	Warmth, foundation	Bass guitar, bass synth, kick body, low piano
Low-mids	250-500 Hz	Body of instruments, can mud up	Acoustic guitar body, vocal chest, piano body
Mids	500 Hz-2 kHz	Presence, clarity, vocal core	Vocal main, snare crack, guitar mids
High-mids	2-6 kHz	Definition, attack, edge	Vocal sibilance, guitar pick attack, snare snap
Highs	6-20 kHz	Air, sparkle, openness	Cymbals, vocal air, synth shimmer, reverb tail
3.2 The Distribution Rule
A balanced mix has energy distributed across all six zones, but one zone may dominate by genre design:

Genre	Dominant Zone	Reasoning
Hip-Hop / Trap	Sub-bass + Bass	808 culture
EDM	Sub-bass + Highs	drop impact + sparkle
Pop	Mids + High-mids	vocal-forward
R&B / Neo-Soul	Bass + Low-mids	warmth, intimacy
Indie	Mids	balanced, raw, present
Rock	Mids + High-mids	guitar-forward
Cinematic	Sub-bass + Mids + Highs	massive scope
Folk / Acoustic	Low-mids + Mids	natural body
Country	Mids + High-mids	vocal + acoustic clarity
K-Pop	Bass + Mids + Highs	polished modern balance
3.3 Frequency Conflict Resolution
When two elements compete in the same zone, one must move:

Two basses (bass guitar + 808): 808 takes sub-bass, bass guitar takes bass zone.
Vocal vs. lead synth: synth steps to high-mids, vocal stays in mids.
Kick vs. bass: kick takes 60-100 Hz fundamental, bass cleared in that range.
Snare vs. clap: clap shifts to high-mids, snare keeps mids.
Acoustic guitar vs. piano: one takes low-mids, other takes mids — never both in same zone.
This translates directly into prompt language:

Bass guitar in low frequencies, 808 sub-bass underneath,
clear separation between kick fundamental and sub.
3.4 Mud and Harshness
Mud zone: 200-400 Hz. Too much energy here makes mixes sound boxy. In prompts, use "tight low-mids" or "carved low-mids" to signal restraint here.
Harsh zone: 2-5 kHz. Too much energy here causes ear fatigue. In prompts, use "smooth high-mids" or "refined treble" to soften.
SECTION 4. STEREO IMAGE ARCHITECTURE
4.1 The Stereo Field
Three positional zones in stereo:

Center (mono core): lead vocal, kick, snare, bass, sub-bass. Always centered for stability.
Mid-pan (10-50% L/R): rhythm guitars, keys, supporting vocals, harmonies.
Wide (50-100% L/R): pads, doubled guitars, atmospheric textures, room reverb.
4.2 The Stability Rule
Low frequencies stay centered. Why: low frequencies have long wavelengths that don't localize well in stereo and they consume mono compatibility. Sub-bass and bass always centered. Kick always centered.

4.3 The Width Curve
Stereo width can change across the track to support the energy curve:

Intro: narrow (40-60% width) — focused, intimate.
Verse: medium-narrow (50-70%) — close, conversational.
Pre-Chorus: medium (70-85%) — opening up.
Chorus: wide (90-100%) — full stereo embrace.
Bridge: variable (often narrow for contrast, then wide).
Final Chorus: maximum (100%+ with stereo enhancement).
Outro: contracts back to center.
In prompts:

[Verse] narrow stereo, intimate close-mic feel
[Chorus] wide stereo image, expansive
[Bridge] narrow centered feel
[Final Chorus] maximum stereo width with enhanced sides
4.4 Panning Conventions by Element
Element	Typical Pan
Lead vocal	Center
Backing vocal lower harmony	Slight L (10-30%)
Backing vocal upper harmony	Slight R (10-30%)
Doubled lead vocal	Hard L+R (90%+)
Kick	Center
Snare	Center (or slightly off, 5%)
Hi-hat	20-40% one side
Toms	Spread across stereo (low to high, L to R or R to L)
Overheads	Hard L+R
Bass	Center
Rhythm guitar 1	60-80% L
Rhythm guitar 2	60-80% R
Lead guitar	Center or slight off
Piano	Stereo (natural left-low to right-high)
Pads	Wide stereo
Strings ensemble	Wide stereo
Percussion (shaker, tambourine)	40-80% one side
4.5 Stereo Tricks for Prompts
Effect	Prompt Language
Fake stereo from mono source	"stereo-doubled vocal," "Haas-effect texture"
Stereo widener	"enhanced stereo width," "expanded stereo image"
Mid-side processing	"wide sides, focused center"
3D depth	"front-to-back depth," "layered depth field"
Room ambience	"natural room sound," "stereo room reverb"
SECTION 5. DENSITY DESIGN (LAYERS)
5.1 The Layer Inventory
A finished track typically has 8-25 layers running at any given moment. Categorized:

Foundation (always present in full sections)

Kick
Snare/Clap
Bass (or sub-bass)
Lead vocal
Harmonic bed 5. Rhythm chords (guitar, keys, or pads) 6. Sustained pad or strings 7. Counter-harmony instrument

Rhythmic detail 8. Hi-hat 9. Percussion (shaker, tambourine, claps) 10. Ghost-note snares or rim hits

Vocal layers 11. Doubled lead 12. Harmony +3rd 13. Harmony +5th or octave 14. Ad-libs / runs 15. Backing vocals on chorus

Atmosphere 16. Reverb wash 17. Delay throws 18. Ambient texture (vinyl, room, field recording) 19. Risers / sweeps 20. Impacts / crashes

Lead detail 21. Melodic counterline 22. Solo instrument (during instrumental break)

Sub-bass / low-end specials 23. 808 (in trap/hip-hop) 24. Sub-bass drone (in cinematic/EDM)

FX 25. White-noise riser, reverse cymbal, vinyl crackle, etc.

5.2 The Density Curve by Section
Section	Active Layer Count
Intro	2-5
Verse 1	5-8
Pre-Chorus 1	8-12
Chorus 1	12-18
Verse 2	6-10 (slightly fuller than V1)
Pre-Chorus 2	10-14
Chorus 2	14-20
Bridge	4-10 (intentional contrast)
Final Chorus	18-25
Outro	2-6
5.3 The Layer Entry/Exit Choreography
Layers don't all enter at once. Stagger entries:

Verse 1 → Pre-Chorus: add hi-hat, add rhythm guitar.
Pre-Chorus → Chorus: add full drums, add bass, add backing vocals, widen stereo.
Chorus → Verse 2: drop one or two layers, but verse 2 stays slightly thicker than verse 1.
Verse 2 → Pre-Chorus 2: add a layer not in pre-chorus 1 (new texture).
Pre-Chorus 2 → Chorus 2: add upper harmony stack.
Chorus 2 → Bridge: strip 50%+ of layers for contrast.
Bridge → Final Chorus: massive entry — all layers + new top layer (e.g., choir, octave-up vocal).
Final Chorus → Outro: layers exit one or two at a time.
5.4 Sparse Arrangement Tricks
When a section is intentionally sparse, fill perceptual space without adding density:

Use reverb tails as "phantom" layers.
Use delay throws on key vocal phrases.
Add subtle textures (vinyl crackle, room tone, breath).
Use silence as a layer — strategic gaps create tension.
Let sustained notes ring (long piano sustain, held synth pad).
In prompts:

[Verse] sparse arrangement with long reverb tails on vocal,
subtle vinyl texture, sustained piano chords ringing into the gaps.
SECTION 6. DYNAMIC DESIGN
6.1 Dynamic Range vs. Loudness
Dynamic range (DR): the difference between the quietest and loudest parts of the song. Loudness: the perceived volume average.

Modern streaming targets:

Spotify, Apple Music, YouTube Music: normalize to roughly -14 LUFS integrated.
Tidal, Amazon Music HD: similar -14 to -16 LUFS targets.
Club / competitive masters: -8 to -10 LUFS (will be turned down by streaming, but feels louder on systems that don't normalize).
Per Mastering The Mix's 2026 trend report, contemporary masters favor:

Integrated LUFS: -10 to -8
Short-term peak LUFS: -7 to -6
Dynamic range: 5-6.5
Loudness range: 5-9 LU
6.2 Dynamic Contour by Section
A track shouldn't be uniformly loud. Sections should breathe:

Section	Relative Loudness	Compression Style
Intro	-3 to -6 dB below chorus	open, light compression
Verse	-2 to -4 dB below chorus	natural, semi-compressed
Pre-Chorus	-1 to -2 dB below chorus	tightening
Chorus	reference level (0)	full compression, glued
Bridge	-2 to -5 dB	open, breathy
Final Chorus	reference level (0)	maximum density
Outro	-3 to -8 dB	opening up
6.3 Compression Character Vocabulary (for Prompts)
Term	Meaning
"Open dynamics"	Light compression, natural breath
"Tight pop compression"	Glued chorus, aggressive on the drums
"Parallel compression"	Compressed and dry blended
"Bus glue compression"	Soft, holding the mix together
"Vintage tape compression"	Saturated, soft top, rounded transients
"Pumping sidechain"	Audible kick-driven duck
"Smashed loudness"	Modern aggressive, near-zero dynamic range
"Crushed dynamics"	Hyper-compressed, EDM festival style
6.4 Suno-Specific Note on Dynamics
Suno's mastering is generally aggressive — it tends to push toward modern loud levels by default. To get more dynamic output:

Specify "open dynamics" or "natural dynamics" in the COVER prompt.
Specify "vintage tape warmth" or "analog warmth" to soften the limiter behavior.
Specify "mid-range focused mix" to avoid the over-bright modern sound.
SECTION 7. PRODUCTION CHARACTER (ERA & FORMAT)
7.1 Era Vocabulary
Era keywords carry massive weight in Suno because they cluster training data tightly:

Era	Production Character
1960s	mono, tube saturation, plate reverb, narrow stereo
1970s	analog warmth, wide stereo, natural drum sound, tape compression
1980s	gated reverb, big drums, chorused guitars, DX7 keys, early digital
1990s	grunge dryness or hi-fi polish, sampled drums, wide guitars
2000s	early digital perfection, side-chained pop, dense low-end
2010s	EDM-influenced loudness, side-chain everywhere, polished radio sound
2020s	spatial audio, refined low-end, vocal-forward, less compressed than 2010s
7.2 Format Vocabulary
Format	Character
"Vinyl-recorded"	warm, slight crackle, mid-forward
"Tape-recorded"	analog saturation, slight wow/flutter, soft top end
"Cassette"	lo-fi, narrow stereo, hiss
"Live-tracked"	bleed, room sound, natural dynamics
"Studio-polished"	clean separation, controlled
"Bedroom-recorded"	lo-fi, intimate, quirky
"Garage-recorded"	raw, blown-out, energetic
"Field-recorded"	natural ambience, environmental sound
7.3 Mixing Engineer Vocabulary (Implied Style)
Avoid named engineer references (treated like artist references — see 09_SUNO_ENGINE.md § 5). Instead, use descriptive style language:

Andrew Scheps style → "warm bus-glue compression, mid-forward, controlled low-end."
Michael Brauer style → "multi-bus compression, open dynamics, vocal-prominent."
Serban Ghenea style → "modern radio-polished, wide stereo, glued chorus."
Manny Marroquin style → "punchy drums, bright top end, glossy high-mids."
Tom Elmhirst style → "vintage warmth, plate reverb, analog character."
SECTION 8. TRANSITION DESIGN
8.1 Why Transitions Matter
The boundary between sections is where listeners disengage if it's clumsy. A clean transition rewards continued attention; a rough one breaks the spell.

8.2 Transition Types
Type	Description	Use
Cymbal swell	Reverse cymbal or crash leading into downbeat	Verse → Chorus, Bridge → Final
Drum fill	1-2 bar drum fill into next section	Universal
Riser	White-noise or pitched riser building to drop	EDM, dance, modern pop
Drop-out	All instruments cut briefly, then re-enter	Adds drama, modern pop
Half-bar pause	Beat of silence before new section	Intimate, indie, R&B
Vocal pickup	Vocal phrase ends on the new section's downbeat	Pop, R&B
Beat switch	Drum pattern changes immediately	Hip-hop, modern pop
Reverse FX	Reverse-played sample or reverb sweep	Universal modern
Hard cut	No transition — immediate change	Punk, indie, experimental
Crossfade	Smooth blend between sections	Cinematic, ambient
8.3 Transition Prompt Language
Transitions: cymbal swells into each chorus,
quarter-bar drum fills into verse 2,
beat switch on the bridge,
reverse cymbal lifting into the final chorus,
quarter-beat dropout before final chorus entry.
8.4 The Two-Bar Rule
The strongest transitions occur in the last two bars before the new section. Save the highest-energy transition (cymbal + riser + drum fill stacked) for the entry to the final chorus.

SECTION 9. GENRE PRODUCTION SIGNATURES
Quick-reference production fingerprints. Use as Decomposed Signature ingredients in COVER prompts.

9.1 Modern K-Pop (4th Generation)
Crystal-clear vocal, multi-tracked harmonies, breath-forward intimacy.
Tight low-end, controlled 808 or sub-bass.
Hyper-clean mix separation.
Wide stereo, but vocal stays centered.
Polished but not over-compressed; modern controlled loudness.
Prompt: polished modern K-pop production, breathy multi-tracked female vocals, controlled sub-bass, crystal-clear top end, wide stereo image with centered vocal, precise mix separation.
9.2 Bedroom Indie / Lo-Fi Pop
Slight noise floor, intimate close-mic vocal.
Narrow stereo, mid-forward.
Tape saturation or vinyl crackle.
Dry vocal, minimal reverb.
Prompt: lo-fi bedroom production, intimate close-mic vocal with slight room sound, narrow stereo image, tape saturation warmth, mid-forward EQ tilt, minimal reverb.
9.3 Hip-Hop / Trap
Massive 808 sub-bass, side-chained to kick.
Hi-hat patterns front and center.
Vocal often double-tracked with ad-lib bed.
Sparse mid-range, leaving room for vocal.
Prompt: modern trap production, deep 808 sub-bass with kick punch, crisp hi-hat patterns, vocal-forward mix with ad-lib layers, sparse mid-range, half-time feel underneath.
9.4 Neo-Soul / Modern R&B
Warm low-end, rounded bass.
Live or live-feel drums, often with humanization.
Mwandishi-influenced electric piano (Rhodes).
Lush vocal stacks with melismatic ad-libs.
Prompt: warm modern R&B production, rounded fretless bass, live-feel drums with subtle swing, vintage Rhodes electric piano, lush stacked harmony vocals, plate reverb texture, vintage tube warmth.
9.5 Indie Folk / Americana
Acoustic-forward, minimal processing.
Live ensemble feel, room mics audible.
Modest reverb, mostly natural.
Vocal up-front and dry-ish.
Prompt: intimate indie folk production, acoustic guitar forward, live ensemble feel with audible room sound, modest plate reverb, dry-forward vocal, natural dynamics, mid-forward warmth.
9.6 Cinematic / Trailer Music
Massive dynamic range — quiet to enormous.
Sub-bass impacts.
Wide stereo orchestra with deep front-to-back depth.
Hybrid orchestral + electronic elements.
Prompt: cinematic trailer production, massive dynamic range from intimate to thunderous, sub-bass orchestral impacts, wide stereo orchestra with deep depth field, hybrid orchestral-electronic textures.
9.7 EDM / Festival
Crushed loudness, side-chained pumping.
Massive sub-bass on drops.
Bright top end, hi-hat triplets.
Wide stereo synths with mono bass.
Prompt: festival EDM production, crushed loudness, audible side-chain pumping on the drop, massive sub-bass, bright sparkling top end, wide stereo synth layers with centered bass.
9.8 City-Pop (1980s Tokyo)
Bright high-end with analog softness.
Slap bass forward.
Clean Rhodes or DX7 keys.
Live drums with light gated reverb.
Wide stereo, polished but warm.
Prompt: 1980s Tokyo city-pop production, bright analog warmth, prominent slap bass, clean Rhodes electric piano, lightly gated drum reverb, wide polished stereo, glossy high-end with vintage softness.
9.9 Modern Country (2020s)
Acoustic guitar foundation, optional electric tasteful.
Live drums, occasionally programmed.
Vocal up-front, slight Southern accent welcomed.
Pedal steel or fiddle as signature accent.
Prompt: modern 2020s country production, acoustic guitar foundation, live drums with light programmed accents, vocal-forward mix with subtle Southern accent, pedal steel signature, warm mid-range, controlled loudness.
9.10 Ambient / Downtempo
Long reverb tails as primary texture.
Sparse percussion or none.
Sub-bass drone.
Wide stereo atmosphere.
Slow evolving timbres.
Prompt: ambient downtempo production, long reverb tails as primary texture, sparse minimal percussion, sub-bass drone foundation, wide stereo atmosphere, slow evolving timbres, dreamy depth field.
SECTION 10. THE PRODUCTION CHECKLIST
Before finalizing a COVER prompt, confirm:

Era and format are anchored (e.g., "1980s Tokyo city-pop production").
Frequency dominance zone is declared (e.g., "vocal-forward mids, controlled sub-bass").
Stereo width is specified (e.g., "wide stereo with centered low-end").
Dynamic character is specified (e.g., "open dynamics" vs "modern controlled loudness").
Compression character is specified (e.g., "vintage tape warmth").
Layer density is appropriate to the section (sparse for verse, full for chorus).
Reverb character is specified (e.g., "plate reverb" vs "spring" vs "hall").
Mix character vocabulary doesn't conflict (no "intimate close-mic" + "stadium-wide" together).
Transitions are mentioned where structurally important.
No engineer/producer names used directly — Decomposed Signature applied.
SECTION 11. COMMON PRODUCTION FAILURES AND FIXES
Symptom	Cause	Fix in Prompt
Mix sounds muddy	over-energy in 200-400 Hz	"carved low-mids," "tight low-mid clarity"
Vocal sounds buried	no vocal-forward language	"vocal-forward mix," "vocal up-front"
Bass disappears on small speakers	bass with no fundamental	"punchy bass with strong fundamental," "bass with body"
Track feels small	narrow stereo, low density	"wide stereo image," "full production layers"
Track feels harsh	over-energy in 2-5 kHz	"smooth high-mids," "refined treble"
No dynamic excitement	uniform density	declare different energy states per section
Transitions abrupt	no transition language	specify cymbal swells, drum fills, risers
Sounds dated	mismatched era	clarify era explicitly
Sounds amateur	over-compressed default	request "open dynamics" or "vintage tape warmth"
Bridge feels random	no contrast plan	specify "stripped back bridge with intimate dynamics"
SECTION 12. APPLICATION WORKFLOW
COVER PROMPT BUILD
   │
   ▼
1. Lock genre + era anchor (Section 7.1, 9.x)
   │
   ▼
2. Declare dominant frequency zone (Section 3.2)
   │
   ▼
3. Declare stereo width strategy (Section 4.3)
   │
   ▼
4. Declare dynamic character (Section 6.3)
   │
   ▼
5. List 4-6 core instruments with role specificity (Section 5.1)
   │
   ▼
6. Add atmosphere/reverb character (Section 9.x examples)
   │
   ▼
7. Mention transitions if structurally critical (Section 8.3)
   │
   ▼
8. Run pre-generation gate (`09_SUNO_ENGINE.md` § 11)
   │
   ▼
DELIVER
SECTION 13. REFERENCES
Mixing & Production:

Mastering The Mix — guides to panning, stereo width, and 2026 mastering trends
iZotope — EQ Cheat Sheet, frequency range guide
Splice — stereo widening techniques, song structure guide
Universal Audio — mixing in stereo
EDMProd — tension and energy guide
Soundplate — streaming loudness LUFS table 2026
Songwriting & arrangement:

Pat Pattison — prosody and arrangement principles
Sample Focus — macro vs micro arrangement approaches
Point Blank Music School — song structure intro to outro
Streaming standards:

Spotify, Apple Music, Tidal loudness normalization documentation
Mastering Trends for 2026 (Mastering The Mix)
SECTION 14. RELATED FILES
04_RHYTHM_AND_FORM.md — section-level structure backing the macro arc.
05_GENRE_LIBRARY.md — per-genre BPM, key, instrumentation defaults.
09_SUNO_ENGINE.md — how to encode production language into Suno prompts.
12_PROMPT_TEMPLATES.md — copy-paste production prompt blocks.
06_VOCAL_PRODUCTION.md — vocal-specific production (effects, layering).



---

## SECTION 15. LUFS PLATFORM TARGETS (NEW v2.7 / External Research)

### 15.1 Streaming platform normalization (2026)

External research (Spotify / Apple / YouTube / Tidal 2026 docs):

| Platform | Normalization Target | Notes |
|---|---|---|
| Spotify | -14 LUFS integrated | Loud mode: -11 LUFS / Quiet: -19 |
| Apple Music | -16 LUFS integrated | Soundcheck on by default |
| YouTube | -14 LUFS integrated | Auto-normalized after 2023 |
| TIDAL | -14 LUFS integrated | HiFi tier respects loudness |
| SoundCloud | No normalization | Master can be louder |
| Amazon Music | -14 LUFS integrated | Same as Spotify default |
| Beatport | No normalization | DJ-targeted, louder OK |

### 15.2 Master target by use case

**Streaming-first master**: **-14 LUFS integrated**
- Plays at perceived equivalent loudness on all major platforms
- Headroom -1 dBTP (True Peak)
- Dynamics preserved

**Club / DJ master**: **-8 ~ -10 LUFS**
- For Beatport / DJ pool / club PA
- Hot master, may be normalized on streaming
- Use *separate masters* for streaming vs club

**Demo / Reference**: **-12 ~ -14 LUFS**
- Lower than final, leaves room for further mastering
- Closer to streaming reality

### 15.3 Genre LUFS conventions (C-17 mapping retained)

These are *creative production targets*, then **final master to
-14 LUFS** for streaming:

| Production phase | LUFS |
|---|---|
| Modern Dance/EDM creative | -6 ~ -8 |
| Modern Pop/K-pop creative | -7 ~ -9 |
| Modern Trot/Crossover | -8 ~ -10 (warm not loud) |
| Modern Ballad/R&B | -9 ~ -11 |
| Indie/Acoustic | -10 ~ -13 |
| Jazz/Classical | -12 ~ -14 |
| Vintage (70-80s) | -14 ~ -16 |
| Lo-fi/Ambient | -14 ~ -18 |

Then *master pass* to -14 LUFS for streaming distribution.

### 15.4 Suno Style Box LUFS specification

Suno doesn't directly accept LUFS numbers but interprets *loudness
language*:

```
loud and punchy modern master   → ~-8 LUFS feel
balanced dynamic master          → ~-12 LUFS feel
warm vintage master               → ~-14 LUFS feel
quiet intimate production         → ~-18 LUFS feel
```

Operator request "더 크게" / "louder" → louder language in Style Box.
Operator request "더 다이내믹" → "dynamic," "breathing room" language.

---

## SECTION 16. STEMS & UVR5 INTEGRATION (NEW v2.7)

### 16.1 Suno Stems (v5+)

Suno v5 / v5.5 supports stem download:
- Vocals (lead)
- Backing vocals (harmonies, ad-libs)
- Drums
- Bass
- Other (synths, guitars, keys, etc.)

Format: WAV 44.1 kHz / 16-bit (Pro / Premium tier).

### 16.2 UVR5 (Ultimate Vocal Remover) workflow

If Suno stem quality insufficient, post-process with UVR5:
1. Download Suno's "full mix" version
2. Run UVR5 (MDX-Net or Demucs)
3. Get cleaner stems
4. Re-mix in DAW

Use cases:
- Sample isolation
- Remix preparation
- Vocal extraction for layering

### 16.3 Stem-aware production prompts

Style Box can encourage clean stem separation:
```
clean instrumental separation, distinct frequency zones, no muddy
overlaps, sub-bass mono and isolated, vocal corridor protected.
```

Effect: Suno more careful with frequency separation, easier stem
extraction.

---

## SECTION 17. WEIRDNESS & STYLE INFLUENCE DIALS (NEW v2.7)

### 17.1 Suno v5 dial controls

Suno v5 added two creative dials:
- **Weirdness** (0-100, default 50)
- **Style Influence** (0-100, default 50)

### 17.2 Weirdness dial

| Range | Effect |
|---|---|
| 0-20 | Conservative, default genre conventions |
| 20-40 | Mild variation, slight surprises |
| 40-60 | Balanced (default zone) |
| 60-80 | Bold, unexpected elements |
| 80-100 | Experimental, chaos territory |

Use cases by genre:
- Mainstream pop: 30-50
- Indie / alt: 50-70
- Hyperpop / experimental: 70-90
- Ambient / drone: 60-80

### 17.3 Style Influence dial

| Range | Effect |
|---|---|
| 0-20 | Style Box treated as suggestion only |
| 20-40 | Loose interpretation |
| 40-60 | Balanced (default) |
| 60-80 | Tight adherence |
| 80-100 | Maximum compliance, risks over-fitting |

Use cases:
- Reference-based work: 70-90
- Free exploration: 30-50
- Style Box very detailed: 70-85 (let it lead)
- Style Box minimal: 40-60 (let model improvise)

### 17.4 Operator-verified combinations

| Goal | Weirdness | Style Influence |
|---|---|---|
| K-pop main, safe production | 30 | 70 |
| K-pop hyperhook, modern | 50 | 60 |
| Indie experimental | 70 | 50 |
| Reference cover | 25 | 85 |
| Polarity Fusion (99_OPERATOR_VAULT Part C (Polarity Fusion)) | 65 | 55 |
| Ballad / OST faithful | 25 | 75 |
| Hyperpop chaos | 80 | 45 |
| Ambient drone | 60 | 40 |

### 17.5 Dial adjustment via prompt

If operator can't access dials directly (some Suno UIs hide them),
prompt language can nudge:

For high weirdness:
```
unexpected element fusion, genre-bending moments, surprising
production choices throughout
```

For high style influence:
```
strict genre adherence, precise stylistic conventions, classic
[genre] vocabulary
```

---



## § USER EXTENSION ZONE v2.0 (2026-05-24)

SJY arrangement-for-mix + energy-and-dynamics + bitwize mastering
통합. 풀바디는 *20 PRODUCTION_AWARE* 신규 파일 참조.


### §UE-1. 20 PRODUCTION_AWARE 라우팅

```
COVER Style Box 작성 시 → 20 §1 7-zone 점검 자동 발동
LUFS 결정 시 → 20 §2 매핑 적용
Mastering 시 → 20 §5 chain + §6 QC
```


### §UE-2. Energy & Dynamics Arc (SJY)

```
Intro: 30-40% (build curiosity)
Verse 1: 50% (settle)
Pre-Chorus: 60-70% (build)
Chorus: 90-100% (peak)
Verse 2: 55-65% (slight build)
Pre-Chorus: 70-80%
Chorus: 95-100%
Bridge: 30-70% (contrast — usually quieter)
Final Chorus: 100% (key change + max)
Outro: 60-30% (decay)
```


### §UE-3. Arrangement for Mix (SJY 핵심)

7-zone (C-59) + Kick-Bass 관계 + Stereo Image —
**20 PRODUCTION_AWARE §1** 풀바디 참조.


# === END 11 USER EXTENSION ZONE v2.0 ===


---

# SOURCE: 20_PRODUCTION_AWARE.md

# ============================================================
# 20_PRODUCTION_AWARE.md
# Frequency Architecture + LUFS Mapping + Mastering
# YUNY v2.0 "Complete Renaissance Edition"
# Source: SJY051 arrangement-for-mix + bitwize/reference/mastering
# ============================================================

COVER Style Box / Final 마스터링 단계에서 자동 발동. C-59 (7-zone)
+ C-17 (LUFS) + Phase 8 (Master Workflow) 통합.


## §1. 7-Zone Frequency Architecture (C-59)

곡 작업 시 *7-zone* 자동 점검. COVER Style Box 박을 때 충돌 자리
EQ separation 큐 자동 보강.

### §1.1 Zone 정의 + 주요 악기

| Zone | Hz | 주요 악기 |
|---|---|---|
| ① Sub | 20-60 | Sub-bass synth / Kick fundamental (60Hz) / 808 sub |
| ② Bass | 60-250 | Bass guitar / Synth bass / Kick body / Low strings |
| ③ Low-mid | 250-500 | Body warmth / Chest voice / Guitar body / Snare body |
| ④ Mid | 500-2k | **Vocal corridor** / Guitar lead / Keys / Snare crack |
| ⑤ Upper-mid | 2k-4k | Vocal presence / Snare attack / Guitar bite |
| ⑥ Presence | 4k-8k | Hi-hat / Cymbal attack / Vocal sibilance / Strings air |
| ⑦ Air | 8k-20k | Sparkle / Air / Cymbal shimmer / Vocal breath |

### §1.2 Zone별 EQ 처리 표준

```
Zone ①  | High-pass filter 30Hz (rumble cut)
        | Sub-bass mono fold 20-80Hz
        | Sidechain to kick 80ms tightened

Zone ②  | Bass + Kick 분리: Bass 80Hz-200Hz / Kick 60-80Hz
        | Compression 4:1 medium attack
        | LPF 250Hz (mud cut)

Zone ③  | Mud zone — careful cut at 300Hz
        | Body 자리 (vocal chest / guitar body)
        | -2~-3dB at 400Hz when crowded

Zone ④  | Vocal corridor 500Hz-3kHz **보호**
        | Other instruments -2dB cut at 1-2kHz
        | Vocal +1dB at 1.5kHz (presence)

Zone ⑤  | Vocal presence + Snare attack
        | De-esser 5-8kHz on vocal
        | Snare +1dB at 3kHz (crack)

Zone ⑥  | Hi-hat / Cymbal / Vocal sibilance
        | -2dB at 6-8kHz if harsh
        | Vocal de-essing primary zone

Zone ⑦  | Sparkle / Air
        | High shelf +1-2dB at 12kHz (taste)
        | LPF 18kHz (mastering)
```

### §1.3 자동 점검 룰 (출력 전)

COVER Style Box 출력 직전 7-zone 1차 점검:

- 동일 zone 3+ 악기 겹침 → conflict 경고
- 충돌 자리 EQ separation 큐 자동 보강
- Vocal corridor 침범 악기 → -2dB cut 큐 박음
- Sub mono fold 누락 → "sub-bass mono 20-80Hz" 추가

### §1.4 Kick-Bass 관계 결정

가장 흔한 충돌 → 명시 처방:

```
Option A (Pop/EDM 표준):
- Kick fundamental: 60Hz
- Bass: 80-150Hz
- Sidechain bass to kick, 80ms

Option B (Hip-hop/Trap):
- 808: 30-60Hz (sub + body)
- Kick top: 60-100Hz (click)
- Bass 거의 없음 또는 808와 통합

Option C (Rock):
- Kick: 60-80Hz (punchy)
- Bass: 80-250Hz (full body)
- No sidechain (natural overlap)

Option D (Acoustic / Jazz):
- Upright bass: 50-200Hz
- Kick: 60-100Hz (soft)
- Natural overlap, no aggressive separation
```

### §1.5 Stereo Image Architecture

```
Center (mono):
- Lead vocal
- Kick + Snare
- Bass (20-80Hz mono fold)
- Lead instrument (solo 자리)

L far:
- Rhythm guitar L
- Pad L wide
- Backing vocals L

L near:
- Percussion L
- Synth L mid-width
- Doubled vocal L

R near:
- Percussion R
- Synth R mid-width
- Doubled vocal R

R far:
- Rhythm guitar R
- Pad R wide
- Backing vocals R
```


## §2. LUFS Mapping (C-17)

### §2.1 우리 시스템 매핑 (생성 자체 + 곡 결)

```
Modern Dance/EDM:        -6 ~ -8 LUFS
Modern Pop:              -7 ~ -9 LUFS
Modern Trot/Crossover:   -8 ~ -10 LUFS (warm not loud)
Modern Ballad/R&B:       -9 ~ -11 LUFS
Indie/Acoustic:         -10 ~ -13 LUFS
Jazz/Classical:         -12 ~ -14 LUFS
Vintage (70-80s):       -14 ~ -16 LUFS
Lo-fi/Ambient:          -14 ~ -18 LUFS
```

### §2.2 마스터링 최종 (외부 검증 — bitwize 풀바디)

**Streaming Standard: -14 LUFS / -1.0 dBTP**

장르별 정밀 매핑 (bitwize genre-specific-presets 247줄 통합):

#### Pop & Mainstream
| 장르 | LUFS | High-Mid Cut | Notes |
|---|---|---|---|
| pop | -14 | -1.0 dB | Bright, polished, radio-ready |
| k-pop | -14 | -1.0 dB | Crisp, punchy, vocal-forward |
| hyperpop | -14 | -1.5 dB | Aggressive brightness, taming |

#### Hip-Hop & Rap
| 장르 | LUFS | High-Mid Cut | Notes |
|---|---|---|---|
| hip-hop | -14 | -1.0 dB | Standard, bass-forward |
| rap | -14 | -1.0 dB | Same as hip-hop |
| trap | -14 | -1.0 dB | Keep hi-hat brightness |
| drill | -14 | -1.5 dB | Dark, aggressive |
| phonk | -14 | -1.5 dB | Lo-fi aesthetic, warmer |
| grime | -14 | -1.0 dB | UK sound, punchy |
| nerdcore | -14 | -1.0 dB | Clear vocals, nerdy themes |

#### R&B, Soul & Funk
| 장르 | LUFS | High-Mid Cut | Notes |
|---|---|---|---|
| rnb | -14 | -1.5 dB | Smooth, vocal clarity |
| soul | -14 | -1.5 dB | Warm, analog feel |
| funk | -14 | -1.5 dB | Punchy, groove-focused |
| disco | -14 | -1.5 dB | Bright but not harsh |
| gospel | -14 | -1.5 dB | Vocal warmth, choir clarity |

#### Rock
| 장르 | LUFS | High-Mid Cut | Notes |
|---|---|---|---|
| rock | -14 | -2.0 dB | Standard, tame guitar harshness |
| indie-rock | -14 | -1.5 dB | Less aggressive |
| alternative | -14 | -2.0 dB | Safe middle ground |
| grunge | -14 | -2.5 dB | Gritty but controlled |
| garage-rock | -14 | -2.0 dB | Raw energy |
| surf-rock | -14 | -1.5 dB | Bright twang |

#### Dynamic Rock (More Headroom)
| 장르 | LUFS | High-Mid Cut |
|---|---|---|
| jazz-rock | -16 | -1.0 dB |
| classic-rock | -14 | -1.5 dB |
| psychedelic | -14 | -1.5 dB |
| prog-rock | -16 | -1.0 dB |

#### Electronic
| 장르 | LUFS | High-Mid Cut |
|---|---|---|
| electronic | -14 | -1.5 dB |
| edm | -14 | -1.5 dB |
| house | -14 | -1.5 dB |
| techno | -14 | -1.5 dB |
| trance | -14 | -1.5 dB |
| dubstep | -14 | -2.0 dB |
| drum-and-bass | -14 | -1.5 dB |
| ambient | -16 | -0.5 dB (warm) |
| lofi | -16 | -2.0 dB (vintage) |

#### Folk, Acoustic & Country
| 장르 | LUFS | High-Mid Cut |
|---|---|---|
| folk | -16 | -1.0 dB |
| acoustic | -16 | -1.0 dB |
| country | -14 | -1.0 dB |
| bluegrass | -16 | -1.0 dB |
| americana | -14 | -1.0 dB |
| singer-songwriter | -16 | -1.0 dB |

#### Jazz & Blues
| 장르 | LUFS | High-Mid Cut |
|---|---|---|
| jazz | -18 | -0.5 dB (preserve dynamics) |
| blues | -16 | -1.0 dB |
| smooth-jazz | -16 | -1.0 dB |
| bebop | -18 | -0.5 dB |

#### Classical & Orchestral
| 장르 | LUFS | High-Mid Cut |
|---|---|---|
| classical | -23 | 0 dB (no cut) |
| orchestral | -18 | -0.5 dB |
| chamber | -20 | 0 dB |
| neo-classical | -18 | -0.5 dB |

#### Metal & Heavy
| 장르 | LUFS | High-Mid Cut |
|---|---|---|
| metal | -10 | -3.0 dB |
| heavy-metal | -10 | -3.0 dB |
| death-metal | -10 | -3.5 dB (extreme taming) |
| metalcore | -10 | -3.0 dB |
| djent | -10 | -3.0 dB |

### §2.3 LUFS 측정 도구

외부 자료 검증:
- **Free**: analyze_tracks.py (bitwize), Youlean Loudness Meter, MeterMatch
- **Paid**: iZotope Insight 2, Waves WLM Plus
- **DAW Built-in**: Logic Pro Loudness Meter, Pro Tools Loudness Analyzer

### §2.4 True Peak 한도

```
True Peak > 0 dBTP   → Clipping on playback → 왜곡
True Peak at -0.5 dBTP → 인코딩 후 클립 가능성
True Peak at -1.0 dBTP → 안전 헤드룸 (권장)
True Peak at -2.0 dBTP → 매우 안전 (잡음 적은 환경 권장)
```

### §2.5 Dynamic Range 권장치

```
| 장르 | 권장 LRA (LU) |
|---|---|
| Classical | 15-25 |
| Jazz/Folk | 10-15 |
| Rock/Pop | 6-12 |
| EDM/Hip-Hop | 4-8 |
```

LRA 4 미만 = over-compressed (피로감)
LRA 10 초과 = 평탄 (loudness 부족)


## §3. Suno Output Loudness (Pre-Mastering)

**외부 검증 (v5-best-practices §Suno Output Loudness):**

*"These are typical loudness levels Suno generates — not final mastering targets."*

| 장르 | Typical Suno Output |
|---|---|
| Pop/EDM | -9 to -7 LUFS |
| Lo-Fi | -12 to -11 LUFS |
| Podcast/Spoken | -16 to -14 LUFS |

**원칙:**
- Suno 생성 자체는 *프로 마스터링 X*
- 운영자가 *외부 mastering 거치고* 스트리밍 배포
- Suno 출력 → Stem extract → DAW mix → Master → -14 LUFS


## §4. Compression 처방

### §4.1 Bus Compression (믹스 글루)

```
Master Bus (Glue Compression):
- Ratio 2:1 ~ 4:1
- Threshold 2-3dB GR
- Attack 30-50ms (slow)
- Release 100-200ms (fast)
- Knee soft
```

**v2.0 외부 검증 (v5-best-practices §Troubleshooting):**
*"Mix feels flat" → "bus compression 2–3 dB, slow attack/fast release"*

### §4.2 Sidechain Compression

```
Bass sidechain to Kick:
- Ratio 4:1 ~ 8:1
- Threshold -10dB
- Attack 1-5ms (fast)
- Release 80-100ms (medium)
- Source: kick
- Target: bass
```

### §4.3 Vocal Compression

```
Lead Vocal:
- Stage 1 (controller): Ratio 3:1, Attack 5ms, Release 50ms, 3-4dB GR
- Stage 2 (color): Ratio 2:1, Attack 30ms, Release 150ms, 2dB GR
- Total GR: 5-6dB
```

### §4.4 Drum Compression

```
Snare:
- Ratio 4:1
- Attack 5-10ms
- Release 50-100ms
- 3-5dB GR

Kick:
- Ratio 3:1
- Attack 20-30ms (preserve attack)
- Release 80-100ms
- 2-3dB GR
```


## §5. Mastering Chain (Final Stage)

### §5.1 Standard Chain Order

```
1. Corrective EQ (cleanup)
   - HPF 30Hz (rumble cut)
   - Notch 100Hz mud
   - LPF 18kHz (anti-aliasing)
   
2. Multiband Compression (선택)
   - Low band: 4:1 (bass control)
   - Mid band: 2:1 (gentle glue)
   - High band: 2:1 (de-essing master)
   
3. Glue Compression (single band)
   - 2:1, slow attack, 2-3dB GR
   
4. Saturation / Harmonic Exciter (선택)
   - Tape saturation 1-2%
   - Tube warmth
   
5. Stereo Imager (선택)
   - Low frequency mono fold (under 80-100Hz)
   - High frequency widen
   
6. Final EQ (tonal balance)
   - Genre-specific shelf adjustments
   - High-mid cut from genre preset table
   
7. Limiter (Peak Control)
   - Threshold to hit target LUFS
   - True Peak -1.0 dBTP
   - Release medium
   
8. Output Stage
   - Final LUFS measurement
   - True Peak verification
```

### §5.2 Genre-Specific Mastering Recipes (bitwize 통합)

#### Modern Pop / K-Pop
```
1. HPF 35Hz
2. Notch 250Hz (mud)
3. Saturation 1% (warmth)
4. Glue comp 2-3dB GR
5. High-mid cut -1dB at 3.5kHz
6. High shelf +1dB at 12kHz (air)
7. Limit to -14 LUFS / -1.0 dBTP
```

#### Modern Hip-Hop / Trap
```
1. HPF 25Hz (preserve 808 sub)
2. Bass tilt +2dB at 60Hz
3. Saturation 1.5% (analog warmth)
4. Glue comp 2dB GR
5. High-mid cut -1dB at 3.5kHz
6. Limit to -14 LUFS / -1.0 dBTP
```

#### Indie / Acoustic
```
1. HPF 40Hz
2. Subtle warmth boost +1dB at 250Hz
3. Glue comp 1-2dB GR (preserve dynamics)
4. High shelf +1dB at 10kHz (air)
5. Limit to -16 LUFS / -1.0 dBTP
```

#### EDM / Dance
```
1. HPF 30Hz
2. Bass boost +2dB at 80Hz
3. Mid scoop -1dB at 400Hz
4. Multiband comp on low 3:1
5. Glue comp 3dB GR
6. Stereo widen high
7. Limit to -10 LUFS (club master) or -14 LUFS (streaming)
```

#### Jazz / Classical
```
1. HPF 25Hz (minimal)
2. No saturation (preserve transient)
3. Glue comp 1dB GR or none
4. No multiband
5. Tonal balance shelf adjustments only
6. Limit to -18 LUFS / -1.0 dBTP (preserve dynamics)
```


## §6. Mastering 7-Point QC (19 §20 통합)

```
1. LUFS Target 달성?
2. Peak < -1.0 dBTP?
3. Dynamic Range 적정?
4. Frequency Balance 양호?
5. Stereo Image 균형?
6. Vocal Presence 충분?
7. Mastering Chain 일관성?
```

**자동 발의:** 운영자 *마스터링* 발화 시 7-Point QC 풀바디 +
19 §20 통합 진단.


## §7. COVER Style Box 자동 보강

운영자 COVER 작성 시 본 파일 자동 발동:

1. 마이크로 장르 인식 → LUFS target 결정
2. 7-zone 점검 → EQ separation 큐 보강
3. Throughout discipline (C-5) 의무
4. v2.0 외부 검증 (v5-best-practices) 보조 어법 추가:
   - "Vocal too buried" → "lead vocal 1–2 dB louder than band"
   - "Mix feels flat" → "bus compression 2–3 dB, slow attack/fast release"
   - "Arrangement too busy" → "verse 2: bass rests for 4 bars"
   - "Chorus not lifting" → "double-time hats; octave guitars"


## §8. 외부 검증 통합

- SJY051 references/production-aware/arrangement-for-mix.md (7-zone 원천)
- bitwize/reference/mastering/genre-specific-presets.md (247줄 풀바디)
- bitwize/reference/mastering/loudness-measurement.md (313줄)
- bitwize/reference/mastering/mastering-checklist.md (269줄)
- bitwize/reference/mastering/mastering-workflow.md (527줄)
- bitwize/skills/mastering-engineer/SKILL.md (15KB)
- v5-best-practices §Suno Output Loudness

# ============================================================
# END OF 20_PRODUCTION_AWARE.md
# ============================================================
