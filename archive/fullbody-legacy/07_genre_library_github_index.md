# ACTIVE GITHUB GENRE PATCH — read before legacy body

For genre work, use the GitHub genre dictionary when exactness matters.

Repository path:
`knowledge-evolving/genre-dictionary/`

Routing:
exact slug -> adjacent slug -> fallback DNA.
Start with `index/GENRE_INDEX.md`, `index/genre_index.json`, or `index/genre_index.csv`.
Fetch only the relevant fullbody entry or 1-2 adjacent entries.
If exact entry is missing, preserve the requested term in the prompt and build from adjacent DNA.
For Tech Para / テクパラ style gaps, preserve the term and use Eurobeat + Hyper Techno + Trance + J-pop + ParaPara DNA.

---

# ACTIVE GPT ROUTE HEADER
- Current GPT file: `07_genre_library_github_index.md`
- Purpose: Genre library and GitHub external index
- Preserved source aliases: 05_GENRE_LIBRARY, 21_GENRE_LIBRARY_SEARCH, 23a_GENRE_INDEX_MASTER, GENRE_EXTERNALIZE_PATCH
- Use rule: Use for genre lookup, GitHub raw entries, exact/adjacent/fallback DNA. Together: 05,08,11,18.
- Cross-link rule: Follow `instructions.txt` first. Legacy `# SOURCE:` blocks below are source provenance, not current routing names. If retrieval is thin, search this file by both current terms and preserved source aliases.

---

# v2.2 routing reinforcement
For genre work, do not guess from a broad label. Route exact slug -> adjacent slug -> fallback. If an exact entry does not exist, explicitly name the adjacent DNA used. For Tech Para / テクパラ and ParaPara / パラパラ, preserve those requested terms in the prompt while building the sound from adjacent DNA such as Eurobeat, Hyper Techno, Trance, J-pop, ParaPara.

---

# Active GPT patch: Genre/GitHub use
Use the genre index before guessing. Exact slug -> adjacent genres -> fallback. Fetch 1-3 relevant external entries when available; if not fetched, say fallback briefly. For missing TechPara entries, combine Eurobeat, Hyper Techno, Trance, J-pop, ParaPara DNA and state the requested term in prompt.

---

# SOURCE: 05_GENRE_LIBRARY.md

05_GENRE_LIBRARY.md
# GENRE LIBRARY — COMPOSITION AND PRODUCTION REFERENCE
# Version: 1.0
# Scope: 24 contemporary genres + hybrid encoding rules
# Use: Genre selection, production conventions, reference artists,
#      Suno Style Box recipes per genre

For each genre, this file documents:
- Core DNA (BPM, key tendency, form, texture)
- Harmonic vocabulary
- Rhythmic fingerprint
- Vocal directive defaults
- Reference artists for [Artist-Song-style] encoding
- Suno Style Box recipe template
- Common pitfalls and diagnostic triggers

---

## ENCODING RULE (CRITICAL)

When generating Suno prompts, do not use raw genre names alone.
Encode all genre references as `[Artist-Song-style]` format. This
provides Suno with a concrete sonic blueprint rather than an
abstract category.

Examples:
- Avoid: "K-pop", "Indie rock", "Bossa nova"
- Use: "NewJeans-Hype-Boy-style K-pop", "Hyukoh-Tomboy-style
  Korean indie rock", "João-Gilberto-Garota-de-Ipanema-style
  bossa nova"

Translate the artist reference into craft variables (BPM,
harmonic density, vocal phrasing, arrangement density,
production-era cues). Do not reproduce protected expression
(specific melodies, lyrics, signature riffs, samples,
identifiable arrangement sequences).

---

## GENRE INDEX (24 Total)

**Pop Family**: Pop-Rock, Indie/Alternative, Synth-Pop & New Wave,
K-Pop, J-Pop & City-Pop

**Urban Family**: Hip-Hop & R&B, Trap & Drill, UK Garage & 2-Step,
Afrobeats & Amapiano

**Electronic Family**: Electronic/EDM, House & Techno,
Drum and Bass & Jungle, Ambient & Downtempo,
Hyperpop & Digicore

**Roots Family**: Folk/Roots/Traditions, Country & Americana,
Blues & Soul, Reggae & Dub

**Jazz Family**: Jazz Styles, Fusion & Nu-Jazz

**Latin Family**: Latin Pop & Reggaeton, Bossa Nova & MPB

**Sacred & Theatre**: Gospel & CCM

**Heavy**: Rock, Metal & Prog

---

## 1. POP-ROCK

### Core DNA
- BPM range: 92-138 (sweet spot 108-124)
- Key tendency: Major keys (C, D, E, G, A) for anthems; relative
  minors (Am, Bm, Em) for ballad sub-mode
- Form: VPCVPCBC standard; older 70s rock uses VVCVVCBC
- Time signature: 4/4 dominant; 6/8 for power-ballad sub-mode
- Texture: Drum kit + bass + electric/acoustic guitar pair +
  vocal lead + optional pads

### Harmonic Vocabulary
- Anthem progressions: I-V-vi-IV (Axis), vi-IV-I-V (Sensitive
  Female), I-vi-IV-V (50s)
- Modal pop-rock: i-VII-VI-VII (Aeolian rock),
  I-bVII-IV (Mixolydian rock — Beatles, Oasis lineage)
- Pre-chorus device: IV→V or ii→V or vi→IV→V→V/V to lift tension
- Bridge tools: relative-key shift, chromatic mediant, modal mixture

### Rhythmic Fingerprint
- Backbeat on 2 and 4 (snare), kick on 1 and 3
- Hi-hat 8th notes default; 16ths for upbeat pop-rock
- Crash on chorus downbeat
- Bass: root-fifth pattern in verses, eighth-note drive in choruses

### Vocal Directive Defaults
Female alto, range A3-E5, warm-edged with chest mix on chorus,
conversational verses, anthem power on chorus, breathy ad-libs in
bridge, English with slight rasp on belted notes.

Or: Male tenor, range C3-A4, grainy mid-range, half-spoken
verses, full-throated chorus, falsetto bridge tag, English.

### Reference Artists
**Modern**: Coldplay, U2, Imagine Dragons, OneRepublic,
Maroon 5, Hozier
**Classic**: Beatles, Eagles, Tom Petty, Fleetwood Mac
**Alternative**: Paramore, The 1975, Phoebe Bridgers
**Korean**: IU (mid-tempo), Day6, Cherry Bullet, Jaurim

### Suno Style Box Recipe

Coldplay-Yellow-style anthem pop-rock, 116 BPM, Key of B major, I-V-vi-IV chorus progression with IV-V pre-chorus lift, tight backbeat drums with crash on chorus downbeat, ringing arpeggiated electric guitar layered over strummed acoustic, melodic root-fifth bass driving to eighth-notes in chorus, warm pad bed, female alto A3-E5 with breathy verses opening to chest-mix anthem chorus, layered harmony stack at chorus +3rd +5th, polished radio mix, organic dynamic contrast verse-to-chorus

### Diagnostic Triggers
- "Boring chorus" → Insert IV-V pre-chorus, vary progression
- "Doesn't feel anthemic" → Layered +3/+5 harmony, crash, key lift
- "Too generic" → Borrowed iv chord, chromatic mediant in pre-chorus

---

## 2. INDIE / ALTERNATIVE

### Core DNA
- BPM range: 78-142 (dual cluster — slowcore 78-96, indie-rock 110-142)
- Key tendency: Open tunings (DADGAD, drop-D, open-G); modal
  centers preferred over functional major
- Form: Loose — AABA, or VCVCB-extended-outro; long instrumental
  codas common
- Texture: Lo-fi room sound, single-coil guitars, tape-saturated
  drums, soft-spoken vocal close to mic

### Harmonic Vocabulary
- Modal staples: Dorian (i-IV), Mixolydian (I-bVII-IV),
  Lydian (I-II) for dreamy passages
- Chord shapes: open-string drones, sus2/sus4 instead of clean
  triads, add9 colors throughout
- Movement: stepwise descending bass, or pedal-tone over shifting
  upper structures
- Avoid: clean V7→I cadences (too "pop")

### Rhythmic Fingerprint
- Slowcore: half-time feel, kick on 1, snare on 3, brushed or
  rim-click texture
- Indie-rock: motorik 8ths (Krautrock-derived), or shuffle 12/8
  dream-rock
- Math-indie: odd meters 5/4, 7/8 (Battles, Foals)
- Loose timing tolerance — quantize 60-75% (not grid-locked)

### Vocal Directive Defaults
Male baritone, range G2-F4, intimate close-mic delivery,
half-whispered verses, fragile head-voice climaxes, slight tape
wobble, English with no rasp, breath audible.

Or: Female mezzo, range G3-C5, conversational unpolished delivery,
off-mic ad-libs, no studio polish, double-tracked chorus only.

### Reference Artists
**International**: Phoebe Bridgers, Big Thief, Vampire Weekend,
Sufjan Stevens, The National, Mitski, Lucy Dacus, Adrianne Lenker,
Bon Iver, Beach House
**Korean**: 검정치마 (The Black Skirts), Hyukoh, Silica Gel,
새소년 (Saesoneon), Wave to Earth, Yerin Baek

### Suno Style Box Recipe
Phoebe-Bridgers-Motion-Sickness-style indie alternative, 92 BPM, Key of D Mixolydian, I-bVII-IV-vi loop with sus2 voicings throughout, fingerpicked acoustic guitar with capo on 4th, lo-fi tape-saturated brushed drums, walking root-third bass, shimmer reverb pad in distance, intimate female mezzo G3-C5 close-mic with audible breath, no auto-tune, dynamic crescendo to fragile head-voice climax in bridge, vinyl-warmth mix, room ambience preserved, single-coil guitar sparkle

### Diagnostic Triggers
- "Too clean / too pop" → Strip layers, closer mic, less reverb
- "Feels static" → Stepwise descending bass under static melody
- "Missing emotion" → Single drum entry in pre-chorus

---

## 3. SYNTH-POP & NEW WAVE

### Core DNA
- BPM range: 110-134 (80s classic 118-128; 2020s synthwave
  80-100 half-time)
- Key tendency: Minor keys (Am, Em, F#m, Bm) dominant;
  bittersweet major (D, F, Bb) secondary
- Form: Strict VCVCBC; 8-bar instrumental intros with arpeggiator;
  outros vamp on chorus
- Texture: Analog-modeled synths, gated reverb snare, pulsing
  arpeggio, sidechain pump

### Harmonic Vocabulary
- Classic 80s: i-VI-III-VII (Andalusian-pop), i-VII-VI-V
  (epic minor descent), Am-F-C-G (Aeolian pop)
- Synthwave-modern: i-v-VI-IV with extended Mmaj9 colors
- Chord voicings: stacked 5ths in pads, arpeggiated triads in
  lead synth
- Modulation: half-step lift in final chorus

### Rhythmic Fingerprint
- Drum machine staples: LinnDrum, TR-808, TR-909,
  Simmons SDS-V toms
- Gated reverb snare on 2 and 4 (massive room → noise gate cut)
- Hi-hat 8ths or off-beat 16ths
- Bass: root-octave pulse on 8ths (Italo-disco), or sequenced
  16th note arpeggio (synthwave)

### Vocal Directive Defaults
Male tenor, range D3-B4, dry detached delivery in verses, layered
chorus harmonies +octave +5th, slight chorus-effect on lead, gated
reverb tail, English with smooth vowels.

Or: Female soprano, range C4-F5, breathy androgynous delivery,
processed with subtle vocoder doubling, theatrical phrasing.

### Reference Artists
**Classic**: Depeche Mode, New Order, Tears for Fears,
Pet Shop Boys, A-ha, Eurythmics
**Modern Synthwave**: The Weeknd, Dua Lipa "Future Nostalgia",
The Midnight, FM-84, Carpenter Brut
**J-Pop adjacent**: YOASOBI, Aimer

### Suno Style Box Recipe
The-Weeknd-Blinding-Lights-style synth-pop, 171 BPM half-time feel at 85.5 BPM perception, Key of F minor, i-VI-III-VII Andalusian descent in chorus, pulsing 80s LinnDrum kit with gated reverb snare on 2 and 4, sequenced 16th-note synth bass arpeggiator, stacked Juno-style pad chords, neon lead synth doubling vocal at chorus, male tenor D3-B4 with dry detached verses opening to layered +octave +5th chorus, sidechain pump on bass against kick, glossy 80s mix with chorus-effect on lead vocal, gated drum room cut hard

---

## 4. K-POP (3RD AND 4TH GENERATION)

### Core DNA
- BPM range: 95-155 (multi-zone within one song common)
- Key tendency: Frequent modulation; mid-song tonal center shifts
  are a feature
- Form: Extended hybrid — Intro → Verse → PreChorus → Chorus →
  PostChorus → Verse → PreChorus → Chorus → Rap-Bridge →
  Drop/Dance-Break → Final-Chorus (with key change) → Outro
- Time signature: 4/4 default; 3rd-gen choruses sometimes flip
  to half-time on drop
- Texture: Maximalist — every section can swap genre (pop verse,
  trap pre-chorus, EDM drop, ballad bridge)

### Harmonic Vocabulary
- Verse: i-VI-III-VII or vi-IV-I-V (familiar pop bedrock)
- Chorus: hooks on a single repeated 2-chord oscillation (vi-IV)
  for memorability
- Bridge: chromatic mediant or unrelated key (e.g., Bm → Eb)
- Final chorus: half-step or whole-step lift signature
  (NewJeans, IVE, aespa)

### Rhythmic Fingerprint
- Switch-up culture: every 8-16 bars, the rhythmic feel changes
- Verse: trap-style 16th hi-hats with rolls
- Pre-chorus: build with snare rolls + riser
- Chorus: four-on-floor OR half-time hip-hop feel OR UK-garage
  2-step
- Dance-break: EDM drop or future-house plucks
- Sub-bass: 808 sustained throughout, key-aware

### Vocal Directive (Multi-Member)
Female group of 4 with distinct timbres:
- Lead vocal: soprano D4-E5, clean clear timbre
- Sub-vocal: alto A3-C5, warm timbre
- Rapper: speech-tone, husky timbre
- Lead-vocal 2: mezzo G3-D5, powerful with belted ad-libs

Korean primary with English chorus phrases.
Distinct timbral identity per member required.

### Reference Artists
**4th Gen (2020s+)**: NewJeans, IVE, LE SSERAFIM, aespa, ITZY,
Stray Kids, ENHYPEN, TXT, BABYMONSTER, KATSEYE
**3rd Gen**: BTS, BLACKPINK, TWICE, Red Velvet, EXO, Seventeen,
MAMAMOO
**Solo**: IU, Taeyeon, G-Dragon, Jennie, Rosé, Jung Kook

### Suno Style Box Recipe
NewJeans-Hype-Boy-style K-pop, 100 BPM verse expanding to drum-and-bass-feel chorus at 170 BPM half-time perception, Key of E major modulating to F# major final chorus, vi-IV-I-V verse oscillating to vi-IV chorus loop, 16th-note trap hi-hat verses transitioning to UKG 2-step chorus groove, sub-bass 808 sustained through key changes, plucky lead synth doubling chorus vocal, female group 4-member vocal stack with distinct timbres D4-E5 lead and A3-C5 sub-vocal, Korean primary with English hook phrase repeated, layered ad-libs in second chorus, switch-up at bridge into rap-vocal section, final chorus lifted whole-step

### K-Pop-Specific Hacks
- Section-level genre cues: encode each section as separate
  sub-genre tag in Style Box
- Switch-up handling: explicitly mark transition bars with
  [Drop] or [Dance Break] structure tag
- Maximalist production: layer at least 3 melodic elements
  simultaneously in chorus (lead vocal + counter-melody synth +
  harmony stack)
- Concept keywords: include era-specific keywords (Y2K, cyber,
  dreamcore, retro-future) to lock visual-sonic match
- Language: Korean primary + English chorus hook for
  4th-gen export-ready style

---

## 5. J-POP & CITY-POP

### Core DNA
- BPM range: J-pop 110-140; City-pop 96-112 (laid-back groove)
- Key tendency: Major-key bias; frequent secondary dominants;
  sophisticated jazz-derived harmony
- Form: J-pop = AABA-extended (Aメロ-Bメロ-サビ structure:
  Verse-Climb-Chorus); City-pop = looser jazz-influenced
- Texture: Bright pop production for J-pop; warm analog synths +
  electric piano + chicken-pickin' guitar for City-pop

### Harmonic Vocabulary
- J-pop signature: extensive secondary dominants (V/ii, V/V, V/vi);
  IVmaj7 → V → iii → vi (Royal Road progression)
- City-pop: Maj7/9 chords throughout, ii-V-I jazz cadences,
  modal interchange (bVII, bVI from parallel minor)
- Bメロ device: stepwise ascending bass with deceptive cadence
  into サビ (chorus)

### Rhythmic Fingerprint
- J-pop: 16th-note hi-hat patterns, snare on 2 and 4, busy fills
- City-pop: laid-back 16th groove (slight push-pull), funk-inflected
  drums, ghost-noted snare
- City-pop bass: slap bass or fingered melodic lines, syncopated

### Vocal Directive Defaults
Female mezzo, range G3-D5, bright clean delivery, melismatic
ornaments at phrase ends, breath-stops for emphasis, Japanese with
clear vowel articulation, layered chorus harmonies +3rd.

### Reference Artists
**City-pop classic**: Tatsuro Yamashita, Mariya Takeuchi, Anri,
Toshiki Kadomatsu, Taeko Ohnuki, Hiroshi Sato
**Modern J-pop**: YOASOBI, Aimer, Ado, King Gnu, Vaundy,
Fujii Kaze, Mrs. GREEN APPLE, Official Hige Dandism
**Anime**: LiSA, Eve, Yorushika, Yuuri, Kenshi Yonezu

### Suno Style Box Recipe
Tatsuro-Yamashita-Sparkle-style city-pop, 108 BPM, Key of A major with frequent secondary dominants, IVmaj7-V-iii-vi Royal Road progression, slap bass syncopated 16th lines, electric piano Rhodes warmth, chicken-pickin' clean guitar with chorus effect, ghost-noted snare laid-back groove, female mezzo G3-D5 bright clean Japanese delivery with melismatic phrase-ends, +3rd harmony stack on chorus, warm 80s Tokyo studio mix, analog tape saturation, no auto-tune

---

## 6. HIP-HOP & R&B (NEO-SOUL)

### Core DNA
- BPM range: Hip-hop 70-100 (often felt half-time at 140-200);
  R&B 60-95
- Key tendency: Minor keys dominant (Am, Bm, F#m, C#m);
  modal mixture frequent
- Form: Hip-hop = 16-bar verses + 8-bar hook ABAB; R&B = standard
  pop VCVCBC with extended bridge
- Texture: Sample-based or sample-emulating; vinyl crackle,
  MPC swing, sub-bass 808

### Harmonic Vocabulary
- Hip-hop loops: 2-bar or 4-bar minor loops; i-VI, i-iv, i-bVII-VI
- R&B: jazz-influenced with extended chords (m9, maj9, 11th, 13th);
  neo-soul = D'Angelo voicings (rootless, 7th in bass)
- Modulation: rare in hip-hop, common in R&B bridges

### Rhythmic Fingerprint
- Boom-bap: kick on 1 and 3, snare on 2 and 4, swung 8th hats,
  MPC humanize feel
- R&B: laid-back snare, syncopated kick, 16th hat with ghost notes
- Neo-soul: drunken-sounding swing (D'Angelo "Voodoo" feel),
  drummer slightly behind grid

### Vocal Directive Defaults
**Hip-hop**: Male tenor speech-rhythm rap, range C3-G4,
conversational with attitude, English, slight grain, no auto-tune.

**R&B/Neo-soul**: Male tenor C3-Bb4 falsetto-heavy melismatic
delivery with breathy vocal fry, English, vibrato controlled.

Or: Female alto G3-Eb5, smooth-runs vocal acrobatics,
melismatic, English, falsetto bridge.

### Reference Artists
**Hip-hop**: J. Cole, Kendrick Lamar, Drake, Travis Scott,
Tyler the Creator, Mac Miller, Joey Bada$$, Logic
**R&B**: Frank Ocean, SZA, H.E.R., Daniel Caesar, Brent Faiyaz,
Summer Walker, Steve Lacy
**Neo-soul classic**: D'Angelo, Erykah Badu, Lauryn Hill,
Maxwell, Bilal
**Korean R&B**: DEAN, Crush, Heize, 백예린 (Yerin Baek), 죠지

### Suno Style Box Recipe
D-Angelo-Untitled-style neo-soul R&B, 72 BPM with drunken laid-back swing, Key of E minor, Em9-Am11-Bm7-Em9 progression with rootless D-Angelo voicings, dusty drum break with swung hats and snare slightly behind grid, fingered fretless bass walking through chord tones, Rhodes electric piano with chorus modulation, male tenor C3-Bb4 falsetto-heavy delivery with melismatic runs, layered harmony stack at +3rd +5th +octave, vinyl crackle and tape saturation, warm analog mix, no auto-tune, intimate close-mic vocal placement

---

## 7. TRAP & DRILL

### Core DNA
- BPM range: Trap 130-160 (felt half-time as 65-80);
  UK Drill 138-144; NY Drill 135-145; Chicago Drill 60-75
- Key tendency: Minor keys (F#m, Gm, C#m); often locked to single
  tonal center for entire song
- Form: Loop-based — 8-bar intro, 16-bar verse, 8-bar hook, repeat
- Texture: 808 sub-bass + trap kit + sparse melodic loop (often
  piano, bell, or flute sample)

### Harmonic Vocabulary
- Minimalist: single chord vamp, or 2-chord oscillation (i-VI, i-iv)
- Drill specific: dark minor melodic loop in upper register, no
  functional progression — the bassline IS the harmony
- Sliding 808: pitched sub-bass that glides between chord tones,
  replacing traditional bass-and-chord layering

### Rhythmic Fingerprint
- Trap: 808 kick on syncopated downbeats, snare/clap on 3
  (half-time), hi-hat 16ths with triplet rolls and 32nd skitters
- UK Drill: sliding 808 with fast pitch glides, snare on 3 only,
  off-grid hat patterns, "dn-dn-dn" sliding bass signature
- NY Drill: similar to UK with adapted hat patterns, often samples
  R&B/soul melodic loops
- Chicago Drill: heavier kicks, double-time hi-hats, more
  aggressive snare placement

### Vocal Directive Defaults
**Trap**: Male tenor melodic-rap, range C3-A4, auto-tuned but
tasteful, ad-libs throughout (yeah, ay, slatt), English with
regional slang.

**Drill**: Male tenor speech-flow, range C3-G4, deadpan delivery,
no auto-tune, English with UK accent simulation, ad-libs minimal.

### Reference Artists
**Trap**: Travis Scott, Future, Lil Baby, Gunna, 21 Savage, Migos
**UK Drill**: Central Cee, Headie One, Digga D
**NY Drill**: Pop Smoke, Fivio Foreign, Sheff G
**Chicago Drill**: Chief Keef, Lil Durk, Polo G, King Von
**Korean trap/drill**: BIBI, Jay Park, BewhY

### Suno Style Box Recipe
Central-Cee-Doja-style UK drill, 144 BPM, Key of F# minor static loop, i-VI two-chord minimalist oscillation, sliding 808 sub-bass with fast pitch glides between F# and D, sparse dark piano melodic loop in upper register, drill snare on beat 3 only, off-grid hi-hat 16ths with triplet rolls, sliding bass dn-dn-dn signature pattern, male tenor C3-G4 deadpan UK-accented melodic rap with minimal ad-libs no auto-tune, doubled hook vocals, modern drill master, sub-bass dominant low end, sparse mid-range

---

## 8. UK GARAGE & 2-STEP

### Core DNA
- BPM range: 130-138 (UKG sweet spot 134-136)
- Key tendency: Minor keys with major-7th and 9th color;
  jazz-house influence
- Form: Dance structure — Intro 16 / Drop 32 / Breakdown 16 /
  Drop 32 / Outro
- Texture: Skippy 2-step drums + sub-bass + chopped vocal samples
  + jazz-tinged keys

### Harmonic Vocabulary
- Jazz-house roots: m7, m9, maj7, sus chords; ii-V-I in unexpected
  places
- Skippy progressions: vi9-Imaj9-iii7-IV (pop-jazz hybrid)

### Rhythmic Fingerprint (THE 2-STEP SIGNATURE)
- 2-step skip pattern: kick on 1 and "and-of-3" or "3-and-half",
  snare on 2 and "4-skipped-to-3-and", hi-hats syncopated
- NOT four-on-floor — this is the defining feature
- Shaker or rim-click filling 8th-note grid
- Sub-bass on syncopated 16ths, often gliding

### Vocal Directive Defaults
Female soprano, range C4-G5, soulful delivery with diva ad-libs,
English UK accent, chopped vocal sample treatment in verses, full
vocal in chorus, +5th harmony stack.

### Reference Artists
**Golden-era**: MJ Cole, Artful Dodger, Craig David
**Modern**: Disclosure, AlunaGeorge, Jamie xx
**2020s revival**: PinkPantheress, Nia Archives

### Suno Style Box Recipe
MJ-Cole-Sincere-style UK garage 2-step, 134 BPM, Key of G minor with jazz extensions, vi9-Imaj9-iii7-IV progression with maj7 colors throughout, signature 2-step skip drum pattern with kick on 1-and-3-and snare on 2-and-skipped-3-and, syncopated sliding sub-bass, jazz-tinged Rhodes pads, chopped female soulful vocal samples in verses opening to full diva delivery in chorus C4-G5, UK accent ad-libs, club master, glossy chrome production, shaker filling 8th grid

---

## 9. AFROBEATS & AMAPIANO

### Core DNA
- BPM range: Afrobeats 100-112; Amapiano 108-118; Afro-house 118-124
- Key tendency: Major or modal (Mixolydian, Dorian); often single
  chord vamps
- Form: Loop-based with extended intros and outros; vocal hook
  repeated as mantra
- Texture: Log drum (Amapiano signature), shaker patterns, brass
  stabs (Afrobeats), pitched percussion

### Harmonic Vocabulary
- Afrobeats: I-V-vi-IV in laid-back groove; modal vamps on single
  chord with color tones
- Amapiano: minor key with jazz extensions; ii-V-i with maj7 colors;
  piano-driven harmony

### Rhythmic Fingerprint
- **Afrobeats clave**: 3-2 son clave under straight kick;
  shaker on every 8th; rim click on syncopated downbeats
- **Amapiano log drum**: pitched melodic bass-drum hybrid playing
  syncopated 16th patterns; this IS the genre signature
- Shaker/clap layering: dense polyrhythmic top end

### Vocal Directive Defaults
Male tenor, range C3-A4, melodic afrobeats delivery with Pidgin
English and Yoruba phrases, smooth runs, ad-libs (eh-eh, oh-na-na),
call-response with female backing vocal alto G3-D5.

### Reference Artists
**Afrobeats**: Burna Boy, Wizkid, Davido, Tems, Rema, Asake,
Ayra Starr, Tyla
**Amapiano**: Kabza De Small, DJ Maphorisa, Focalistic,
Major League DJz, Uncle Waffles
**Afro-fusion**: Yemi Alade, Mr Eazi

### Suno Style Box Recipe
Kabza-De-Small-Asibe-Happy-style amapiano, 112 BPM, Key of A minor with jazz extensions, ii-V-i with Am9-Dm9-Em7 progression, signature pitched log drum playing syncopated 16th melodic-bass pattern, jazz Rhodes piano comping, layered shakers and claps polyrhythmic top, deep house-derived kick on 1, male tenor C3-A4 smooth South African accented English with Zulu phrases, +3rd female alto backing vocals call-response, club-warm master, log drum dominant low-mid, expansive reverb on percussion

---

## 10. ELECTRONIC / EDM

### Core DNA
- BPM range: Big-room 126-132; Future-bass 140-160 (felt 70-80);
  Trance 130-140; Dubstep 140 (half-time 70)
- Key tendency: Minor keys for emotional, major for euphoric;
  supersaw stacks dominate
- Form: Strict EDM — Intro 32 / Build 16 / Drop 32 / Breakdown 16
  / Build 16 / Drop 32 / Outro 32
- Texture: Synthesized everything; sidechain pump is mandatory

### Harmonic Vocabulary
- Big-room/EDM: i-VI-III-VII or vi-IV-I-V; supersaw stacks
  playing chords + lead in unison
- Future-bass: lush maj7/maj9 chords; pitched synth chords
  playing lead melody
- Trance: extended cycles of 8 chords with arpeggiated cycling

### Rhythmic Fingerprint
- Big-room: four-on-floor kick, snare/clap on 2 and 4,
  off-beat open hat
- Drop: kick removed temporarily then dropped on 1 of new section
- Sidechain pump: bass and pads ducked under kick
  (fundamental to genre)
- Future-bass drop: half-time feel with pitched synth chord stabs
  replacing traditional drums

### Vocal Directive Defaults
Female soprano, range C4-G5, processed with vocoder/talkbox
treatment, chopped vocal samples for hook, anthemic clean delivery
in verses, English with reverb tails, layered +octave +5th in drop.

### Reference Artists
**Big-room**: Martin Garrix, Hardwell, Tiësto
**Progressive**: Above & Beyond, Eric Prydz, Anjunabeats roster
**Future-bass**: Flume, San Holo, Illenium, Marshmello
**Mainstream**: Calvin Harris, David Guetta, Zedd, Avicii (legacy)

### Suno Style Box Recipe
Flume-Never-Be-Like-You-style future-bass, 145 BPM felt half-time at 72.5 BPM, Key of F# minor with maj9 colors, i-VI-III-VII-IVmaj9 progression, pitched supersaw chord stabs replacing traditional drums in drop, sidechain pump on bass against kick, lush pad bed with shimmer reverb, vocal-chop samples chromatic-pitched melodic lead, female soprano C4-F5 anthemic verses with talkbox-processed hook, layered +octave +5th in drop section, festival master, expansive stereo image, future-bass drop signature with pitched synth chords carrying melody, reverb-soaked outro

---

## 11. HOUSE & TECHNO

### Core DNA
- BPM range: Deep house 118-124; Tech-house 124-128; Techno 125-135;
  Detroit techno 130-140
- Key tendency: Minor keys for emotional; major for happy/disco-house;
  modal for techno
- Form: DJ-tool structure — long intros (32-64 bars), gradual
  builds, extended outros; verse-chorus de-emphasized
- Texture: Four-on-floor kick mandatory; analog synths; minimal
  vocals or chopped vocal samples

### Harmonic Vocabulary
- Deep house: jazz-house Rhodes chords with maj7/9; soulful vocal
  samples
- Tech-house: minimal harmony, often single bass riff carrying
  tonality
- Techno: drone-based, modal (often Phrygian for dark techno)
- Detroit techno: hopeful minor with major lift in breakdowns

### Rhythmic Fingerprint
- Four-on-floor kick mandatory across all subgenres
- Hi-hat patterns: open hat on off-beat
- Clap on 2 and 4 with reverb tail
- Tech-house: shuffled hat groove; bongo/conga percussion layers
- Techno: stripped to kick + clap + percussion + drone

### Vocal Directive Defaults
**House**: Female mezzo, range G3-D5, soulful diva chops, English
chopped phrases, no full lyrics — only hook fragments.

**Techno**: Male spoken-word or pitched-down vocal sample, range
A2-D4, monotone delivery, processed with delay.

### Reference Artists
**Deep house**: Dixon, Âme, Kerri Chandler, Larry Heard, MoBlack
**Tech-house**: Fisher, Chris Lake, Solardo, Hot Since 82
**Techno**: Charlotte de Witte, Amelie Lens, Adam Beyer, Tale of Us
**Detroit**: Jeff Mills, Carl Craig, Derrick May, Juan Atkins

### Suno Style Box Recipe
Dixon-Where-We-Belong-style deep house, 122 BPM, Key of D minor with jazz extensions, vi9-Imaj9-iii7-IVmaj7 progression, four-on-floor kick mandatory, off-beat open hi-hat, clap on 2 and 4 with reverb tail, jazz Rhodes chord stabs syncopated, deep analog sub-bass groove, chopped female soulful vocal samples G3-C5 mezzo diva chops English fragments only no full lyrics, polyrhythmic conga percussion layer, club master, expansive reverb on snare and pads

---

## 12. DRUM AND BASS / JUNGLE

### Core DNA
- BPM range: 165-180 (DnB sweet spot 174); Jungle similar with
  chopped breakbeats
- Key tendency: Minor for darkness (Liquid DnB), major for euphoric
  (Liquid+); modal for neuro-funk
- Form: DJ-tool — Intro 32 / Drop 32 / Breakdown 32 / Drop 32 / Outro
- Texture: Amen break or amen-derivative drums; Reese bass or
  sub-bass; pad layer

### Harmonic Vocabulary
- Liquid DnB: jazzy maj7/m9 chords, soulful vocal lines
- Neuro-funk: minimal harmony, modal drones
- Jump-up: simple minor riff with bass-led harmony
- Jungle: reggae/dub-influenced minor riffs, dub chord stabs

### Rhythmic Fingerprint (THE AMEN BREAK)
- Amen break as foundation: chopped/programmed drums based on
  Winston's "Amen, Brother"
- 2 and 4 snare with ghost-note 16th hits
- Kick syncopated, not four-on-floor
- 16th hi-hat skitters with breakbeat humanization
- Jungle: heavy chopping and resequencing of original breakbeat

### Vocal Directive Defaults
**Liquid DnB**: Female alto, range A3-E5, soulful R&B-style
delivery, English with melismatic runs, full vocal not chopped.

**Jungle**: MC/toaster style, male tenor, range C3-A4, Jamaican
patois English, delay-drenched.

### Reference Artists
**Liquid**: Calibre, High Contrast, LSB, Lenzman, Logistics
**Neuro**: Noisia, Black Sun Empire, Mefjus, Phace
**Jump-up**: Hazard, DJ Hype, Macky Gee
**Modern jungle revival**: Nia Archives, Sherelle, Tim Reaper

### Suno Style Box Recipe
Calibre-Drop-It-Down-style liquid drum-and-bass, 174 BPM, Key of A minor with jazz extensions, vi9-IVmaj7-Imaj9-V11 progression, amen break drum foundation chopped and programmed with ghost-note 16th hits and 2-and-4 snare, deep Reese bass with movement, jazz Rhodes pad bed, female alto A3-E5 soulful R&B-style English vocal with melismatic runs full vocal not chopped, expansive reverb on pads, club master, breakbeat humanization preserved, sub-bass dominant low end, atmospheric drift between drops

---

## 13. AMBIENT & DOWNTEMPO

### Core DNA
- BPM range: Ambient 0-80 (often beatless); Downtempo 70-95;
  Trip-hop 85-100
- Key tendency: Modal, often slow shifts between two tonal centers;
  major-7th colors dominate
- Form: Long-form (4-10 min), gradual evolution, no traditional
  verse-chorus
- Texture: Dense pad layers, field recordings, processed acoustic
  instruments, sparse melodic motifs

### Harmonic Vocabulary
- Ambient: drone-based, two-chord oscillations (Imaj7 ↔ vimin9),
  Lydian color
- Downtempo: jazz-influenced ii-V-I but stretched timewise;
  modal vamps
- Trip-hop: minor key with cinematic darkness, sample-based with
  vinyl artifacts

### Rhythmic Fingerprint
- Ambient: often beatless or single hit per bar
- Downtempo: laid-back hip-hop-derived swung 8ths, kick on 1 and 3
- Trip-hop: dusty break-beat samples, swung snare slightly behind grid

### Vocal Directive Defaults
**Ambient**: Female soprano, range C4-G5, processed wordless
vocalese, breathy ah/oo, layered with reverb-soaked harmonies.

**Trip-hop**: Female alto, range G3-D5, intimate detached delivery,
English with emotional disconnect, processed.

### Reference Artists
**Ambient**: Brian Eno, Stars of the Lid, Tim Hecker, Grouper,
Aphex Twin (Selected Ambient Works)
**Downtempo**: Bonobo, Tycho, Emancipator, Nightmares on Wax
**Trip-hop**: Portishead, Massive Attack, Tricky, Morcheeba

### Suno Style Box Recipe
Portishead-Glory-Box-style trip-hop, 88 BPM, Key of B minor cinematic darkness, i-VI-III-VII modal vamp with maj7 colors, dusty break-beat sample foundation with vinyl artifacts and crackle, swung snare slightly behind grid, deep sub-bass walking line, distorted Rhodes electric piano, female alto G3-D5 intimate detached emotionally-disconnected English delivery processed with tape wobble, atmospheric pad layer expansive reverb, warm analog master, theremin-like lead melodic motif sparse, sample-based aesthetic preserved

---

## 14. HYPERPOP & DIGICORE

### Core DNA
- BPM range: 140-180 (extreme — digicore can hit 200+)
- Key tendency: Major keys with extreme pitch-shifting;
  key-shifts mid-phrase
- Form: Compressed — sub-2-minute songs, abrupt section changes,
  no traditional dynamics
- Texture: Maximally distorted, clipping intentional, pitched-up
  vocals, synthesized everything

### Harmonic Vocabulary
- Major-key bias: I-V-vi-IV but distorted beyond recognition
- Pitched-up samples: chord progressions chosen for shift-up impact
- Glitch-edits: stutters between chord changes

### Rhythmic Fingerprint
- Hyperpop: pop-rock backbeat distorted to clipping; trap hi-hats
  accelerated to 32nds
- Digicore: breakcore-derived chopped drums, blast beats mixed
  with trap kicks
- Sidechain pump: extreme — bass ducks 90% under kick

### Vocal Directive Defaults
Androgynous tenor or pitched-up alto, range D4-A5
(post-pitch-shift), heavily auto-tuned, glitched and stuttered,
English with distorted phrases, layered with formant-shifted
doubles.

### Reference Artists
**Hyperpop**: 100 gecs, SOPHIE (legacy), Charli XCX, A.G. Cook,
Caroline Polachek
**Digicore**: Quinn, glaive, ericdoa, Aldn, Brakence,
Jane Remover, 2hollis
**PC Music adjacent**: Hannah Diamond, Felicita

### Suno Style Box Recipe
100-gecs-money-machine-style hyperpop, 160 BPM accelerating sections, Key of D major shifting to F major mid-phrase, I-V-vi-IV progression distorted beyond recognition, clipping pop-rock backbeat with 32nd-note trap hi-hats, extreme sidechain pump bass ducks 90 percent under kick, synthesized everything maximally distorted, pitched-up female-coded androgynous vocals D4-A5 heavily auto-tuned glitched and stuttered English with formant-shifted doubles, abrupt section changes no traditional dynamics, clipping intentional, glitch-edits between chord changes, breakcore drum chops in bridge

---

## 15. FOLK / ROOTS / TRADITIONS

### Core DNA
- BPM range: Ballad 60-80; Folk-rock 90-120; Bluegrass 140-180
  (felt double-time)
- Key tendency: Major keys (D, G, A, E) for guitar; modal
  (Dorian, Mixolydian) for traditional
- Form: Verse-Chorus or AABA; story-driven verses; refrain
  rather than power-chorus
- Texture: Acoustic guitar primary, fiddle, banjo, mandolin,
  upright bass, accordion (regional)

### Harmonic Vocabulary
- Folk staples: I-IV-V-I (Three Chords and Truth); I-V-vi-IV
- Modal folk: Dorian for Celtic (i-VII-i-IV), Mixolydian for
  Appalachian (I-bVII)
- Open tunings: DADGAD (Celtic), drop-D (Americana), open-G
  (Delta blues adjacent)

### Rhythmic Fingerprint
- Strumming: D-DU-UDU acoustic strum pattern (folk),
  Carter family alternating bass-strum (country-folk)
- Bluegrass: rapid 8th-note picking, fiddle/banjo rolls
- Celtic: 6/8 jig feel or 4/4 reel feel; bodhrán pulse

### Vocal Directive Defaults
Male baritone, range A2-E4, story-telling delivery, conversational
tone, English with regional accent (Appalachian, Irish, etc.),
no auto-tune, harmony partner mezzo +3rd in chorus.

### Reference Artists
**Americana**: Bon Iver, Fleet Foxes, Iron & Wine, Jason Isbell,
Brandi Carlile, The Lumineers, Hozier
**Folk-classic**: Bob Dylan, Joni Mitchell, Joan Baez,
Simon & Garfunkel, Nick Drake
**Bluegrass**: Bill Monroe, Alison Krauss, Punch Brothers,
Billy Strings
**Celtic**: The Chieftains, Lúnasa, Lankum, Lisa Hannigan
**Korean folk-fusion**: 김광석, 이상은, 더 콰이엇 (acoustic mode)

### Suno Style Box Recipe
Bon-Iver-Skinny-Love-style folk Americana, 100 BPM, Key of D major with capo, I-V-vi-IV progression with sus2 voicings, Carter-family alternating bass-strum acoustic guitar pattern, fingerpicked secondary acoustic, brushed snare drum sparse, upright bass walking, fiddle melodic counter-line, male baritone A2-E4 story-telling Appalachian-accented delivery, female mezzo +3rd harmony in chorus, no auto-tune, room-mic ambience preserved, warm analog master, vinyl-warmth aesthetic, dynamic verse-to-chorus crescendo

---

## 16. COUNTRY & AMERICANA

### Core DNA
- BPM range: Country ballad 70-90; Modern country 100-130;
  Bro-country 124-134
- Key tendency: Major keys (E, A, G, D) for traditional;
  minor for outlaw country
- Form: VCVCBC standard; story-song variant uses extended verses
  with refrain
- Texture: Steel guitar, telecaster, fiddle, banjo, drums (modern),
  upright or electric bass

### Harmonic Vocabulary
- Traditional country: I-IV-V-I, I-vi-IV-V (50s);
  I-V-vi-IV (modern crossover)
- Outlaw country: minor i-iv-V; bluesy I7-IV7-V7
- Modern bro-country: pop-rock progressions with country
  instrumentation overlay

### Rhythmic Fingerprint
- **Train beat**: rapid 8th-note snare with cross-stick,
  kick on 1 and 3
- Country shuffle: swung 8ths with brushed snare
- Boots-on-floor: bass drum 1 and 3, snare 2 and 4
  (modern country = pop-rock kit)

### Vocal Directive Defaults
Female alto, range G3-D5, twangy delivery with melismatic phrase
ends, English with Southern American accent, conversational
story-telling, no auto-tune, harmony partner male tenor +5th below
in chorus.

### Reference Artists
**Modern**: Kacey Musgraves, Chris Stapleton, Maren Morris,
Zach Bryan, Tyler Childers, Sturgill Simpson
**Bro-country**: Luke Bryan, Florida-Georgia Line, Kane Brown
**Outlaw classic**: Willie Nelson, Waylon Jennings, Johnny Cash,
Merle Haggard
**Crossover**: Taylor Swift (early), Shania Twain, Faith Hill

### Suno Style Box Recipe
Kacey-Musgraves-Rainbow-style modern country Americana, 92 BPM, Key of G major, I-V-vi-IV progression with sus2 acoustic voicings, fingerpicked acoustic guitar primary, pedal steel guitar atmospheric pad, telecaster clean lead, brushed snare with cross-stick, upright bass walking lines, female alto G3-D5 twangy Southern-accented English with melismatic phrase ends, story-telling verses opening to layered chorus harmonies, no auto-tune, Nashville studio ambience, dynamic verse-to-chorus expansion, dobro slide guitar fills

---

## 17. BLUES & SOUL

### Core DNA
- BPM range: Slow blues 60-80; Shuffle blues 100-130;
  Soul ballad 70-90; Motown 110-135
- Key tendency: Major keys with dominant-7th color throughout;
  minor for emotional blues
- Form: 12-bar blues (I-I-I-I / IV-IV-I-I / V-IV-I-V); 8-bar blues;
  soul = standard pop VCVCBC
- Texture: Hammond B3 organ, electric piano, horn section, blues
  guitar, gospel-derived backing vocals

### Harmonic Vocabulary
- 12-bar blues: I7-IV7-V7 with quick-change variation
- Soul harmony: I-iii-IV-IVm (Motown-cliche), ii-V-I in jazz-soul
- Gospel-soul: extensive secondary dominants, deceptive cadences,
  modulation up half-step

### Rhythmic Fingerprint
- Shuffle blues: swung 8ths, kick on 1 and 3, snare on 2 and 4
- Soul: tight pocket drumming, ghost-note snare, syncopated kick
- Motown: backbeat snare with handclaps, four-on-floor kick on
  faster tracks

### Vocal Directive Defaults
Female alto, range G3-Eb5, gospel-influenced melismatic delivery,
full-throated belted choruses, English with Southern Black-American
gospel inflection, vibrato wide and slow, ad-libs in late choruses.

### Reference Artists
**Soul classic**: Aretha Franklin, Otis Redding, Sam Cooke,
Marvin Gaye, Stevie Wonder, Al Green
**Motown**: The Supremes, The Temptations, Smokey Robinson,
Four Tops
**Modern soul**: Leon Bridges, Anderson .Paak, Yebba, Celeste
**Blues**: B.B. King, Albert King, Stevie Ray Vaughan,
Gary Clark Jr., Buddy Guy

### Suno Style Box Recipe
Aretha-Franklin-Respect-style soul, 116 BPM, Key of C major with secondary dominants, I-vi-IV-V progression with passing V/V chords, gospel-derived horn section stabs, Hammond B3 organ swells, electric piano Wurlitzer comping, four-on-floor kick with backbeat snare and handclaps, walking electric bass, female alto G3-Eb5 gospel-melismatic full-throated belted English with Southern Black-American inflection wide vibrato, three-piece female backing vocal stack +3 +5 +octave with gospel call-response, warm analog master with tape saturation, dynamic verse-to-chorus build, ad-libs in final chorus

---

## 18. REGGAE & DUB

### Core DNA
- BPM range: Roots reggae 60-80; Dancehall 90-110; Dub variable
- Key tendency: Major keys for roots, minor for dub; modal for
  dub-techno crossover
- Form: Verse-Chorus or extended jam; dub = remix-based,
  instrumental focus
- Texture: Bass-and-drums foundation, skanking guitar/keys on
  off-beats, horn section, melodica (dub)

### Harmonic Vocabulary
- Reggae: I-IV-V-I or I-vi-IV-V; one-drop emphasizes 3 (not 1)
- Dub: minimalist — single chord vamp, with bass riff carrying
  tonality
- Dancehall: minor riddim, two-chord oscillation, hook-based

### Rhythmic Fingerprint (THE ONE-DROP)
- **One-drop**: kick and snare BOTH on beat 3 (not 1);
  empty 1 and 2; signature reggae feel
- **Stepper**: kick on 1, 2, 3, 4 (four-on-floor adapted);
  roots variant
- **Rockers**: kick on 1 and 3 with snare on 2 and 4
  (mainstream reggae)
- **Skank**: guitar/keys play off-beat
- Bass: heavy melodic lines, often syncopated, occupies space
  drums leave

### Vocal Directive Defaults
**Reggae**: Male tenor, range C3-G4, smooth Jamaican-accented
English, melodic sung-spoken delivery, layered with toasted MC
backing.

**Dub**: heavily processed, delay-drenched, often
instrumental-only with vocal samples.

### Reference Artists
**Roots reggae**: Bob Marley, Burning Spear, Toots & the Maytals,
Peter Tosh, Black Uhuru
**Dub**: King Tubby, Lee "Scratch" Perry, Mad Professor, Scientist
**Dancehall**: Sean Paul, Beenie Man, Vybz Kartel, Popcaan, Spice
**Modern**: Chronixx, Koffee, Protoje

### Suno Style Box Recipe
Bob-Marley-Three-Little-Birds-style roots reggae, 76 BPM, Key of A major, I-IV-V-I progression with sus2 voicings, signature one-drop drum pattern with kick and snare both on beat 3 empty 1 and 2, off-beat skanking electric guitar on and-of-each-beat, off-beat organ bubble Hammond style, heavy melodic syncopated bass occupying drum spaces, horn section stabs trumpet trombone sax, male tenor C3-G4 smooth Jamaican-accented English melodic sung-spoken delivery, +3rd backing vocal harmonies, warm analog master, spring reverb on snare, dub-derived delay throws on key vocal phrases

---

## 19. JAZZ STYLES

### Core DNA
- BPM range: Ballad 60-80; Mid-tempo swing 100-140;
  Up-tempo 180-280
- Key tendency: All keys via modulation; jazz harmony allows
  constant tonal shifts
- Form: 32-bar AABA standard; 12-bar blues; modal jazz = static
  or single-key
- Texture: Piano-bass-drums trio core; horns (trumpet, sax,
  trombone) lead/solos

### Harmonic Vocabulary
- Bebop: ii-V-I in every key, rapid modulation, secondary
  dominants, tritone substitutions
- Modal jazz: Dorian (So What), Phrygian, Lydian — extended
  improvisation over single mode
- Cool jazz: relaxed harmony, fewer chord changes, melodic emphasis
- Free jazz: harmony abandoned, atonal exploration

### Rhythmic Fingerprint
- Swing: triplet feel ("ding-da-ding" ride pattern), bass walking
  quarters, drums comping
- Bossa: straight 8ths, latin clave-derived
- Bebop: rapid swing, drummer "dropping bombs"
- Modal: open spacious feel, drummer plays time more than fills

### Vocal Directive Defaults
Female alto, range G3-D5, smoky cabaret delivery with melismatic
phrase ends, English with rounded vowels, behind-beat phrasing,
scat-singing capability in solos.

### Reference Artists
**Vocal jazz**: Ella Fitzgerald, Sarah Vaughan, Billie Holiday,
Norah Jones, Diana Krall, Gregory Porter, Cécile McLorin Salvant
**Bebop**: Charlie Parker, Dizzy Gillespie, Bud Powell,
Thelonious Monk
**Modal**: Miles Davis (Kind of Blue), John Coltrane,
Herbie Hancock
**Modern**: Robert Glasper, Esperanza Spalding, Kamasi Washington,
Jacob Collier

### Suno Style Box Recipe
Norah-Jones-Don-t-Know-Why-style modern jazz vocal, 88 BPM, Key of B-flat major, ii-V-I jazz progression with maj7-9th colors throughout, smoky piano comping rootless voicings, walking upright bass quarter-notes, brushed snare swing pattern with ride cymbal ding-da-ding, muted trumpet melodic counter-line, female alto G3-D5 smoky cabaret-style English delivery with melismatic phrase ends behind-beat phrasing, intimate close-mic placement, warm analog master, room-mic ambience preserved, scat-improv in second chorus

---

## 20. FUSION & NU-JAZZ

### Core DNA
- BPM range: Fusion 110-160; Nu-jazz 90-130
- Key tendency: Modal-heavy, frequent shifts; complex altered
  harmony
- Form: Extended (5-10 min), complex multi-section arrangements
- Texture: Electric instruments — Rhodes, electric bass (often
  fretless), synth, guitar (effects-heavy), horns

### Harmonic Vocabulary
- Fusion: altered dominants (V7#9, V7#5b9), complex modulations,
  modal shifts
- Nu-jazz: hip-hop derived loops + jazz changes; broken-beat
  influence
- Acid jazz: funk-driven with jazz harmony; soul-jazz crossover

### Rhythmic Fingerprint
- Fusion: complex meter (5/4, 7/8, 11/8), polyrhythm, drum kit
  pyrotechnics
- Nu-jazz: programmed beats blended with live drums, swung 16ths,
  broken-beat patterns
- Acid jazz: tight funk pocket, syncopated drums

### Vocal Directive Defaults (Optional)
Female mezzo or scat-singer, range G3-D5, jazz-trained melismatic,
English with neutral or French inflection, often used as
instrument-equivalent rather than narrative lead.

### Reference Artists
**Fusion classic**: Weather Report, Mahavishnu Orchestra,
Return to Forever, Headhunters
**Nu-jazz**: Jaga Jazzist, The Cinematic Orchestra, GoGo Penguin,
Yussef Dayes
**Modern fusion**: Snarky Puppy, Hiatus Kaiyote, Robert Glasper
Experiment, Thundercat
**Acid jazz**: Jamiroquai, Brand New Heavies, Incognito

### Suno Style Box Recipe
Robert-Glasper-Cherish-the-Day-style nu-jazz, 95 BPM, Key of D minor with modal shifts, vi9-Imaj9-iii7-IV with altered dominants, hip-hop derived swung-16th drum loop blended with live brushed drums, fretless electric bass syncopated melodic lines, Rhodes electric piano comping rootless voicings, atmospheric synth pad layer, optional female mezzo scat-singer G3-D5 melismatic English used as instrument-equivalent, warm analog hybrid master, broken-beat influence preserved, cinematic atmospheric drift, modulation to relative major in bridge

---
## 21. LATIN POP & REGGAETON

### Core DNA
- BPM range: Reggaeton 90-95 (felt half-time); Latin pop 100-125;
  Bachata 130-140 (felt half-time at 65-70)
- Key tendency: Minor for reggaeton; major for Latin pop;
  modal for traditional fusion
- Form: Reggaeton = loop-based VCVCBC; Latin pop = pop-standard
  VCVCBC; bachata = AABA with traditional structure
- Texture: Dembow rhythm core (reggaeton); Latin percussion
  (congas, timbales, bongo); acoustic/electric guitar

### Harmonic Vocabulary
- Reggaeton: i-VI-III-VII or i-VII-VI-V; minor-key bias
- Latin pop: I-V-vi-IV with Spanish-language phrasing
- Bachata: m-VII-i-V, with characteristic guitar-led harmony
- Cumbia: I-IV-V repeating

### Rhythmic Fingerprint (THE DEMBOW)
- **Dembow rhythm**: kick on 1 and 3, snare/clap on syncopated
  downbeats forming "boom-ch-boom-chick" pattern; fundamental
  to reggaeton
- Latin percussion: congas, timbales, cowbell, güiro filling
  polyrhythmic top
- Bachata: distinctive bongo + güira pattern
- Cumbia: accordion + percussion shuffle

### Vocal Directive Defaults
**Reggaeton**: Male tenor, range C3-A4, melodic-rap delivery with
Spanish, ad-libs (ay, oh-no-no, sí), auto-tune tasteful, doubled
hooks.

**Latin pop**: Female mezzo, range G3-D5, passionate Spanish
delivery with melismatic ornaments, no auto-tune, layered
harmonies.

### Reference Artists
**Reggaeton**: Bad Bunny, J Balvin, Daddy Yankee, Karol G,
Rauw Alejandro, Anuel AA, Feid, Peso Pluma
**Latin pop**: Shakira, Maluma, Camila Cabello, Rosalía,
Manuel Turizo
**Bachata**: Romeo Santos, Aventura, Prince Royce, Juan Luis Guerra
**Cumbia/Norteño**: Selena (legacy), Grupo Frontera, Fuerza Regida
**Música Mexicana modern**: Peso Pluma, Junior H, Natanael Cano

### Suno Style Box Recipe

Bad-Bunny-Tití-Me-Preguntó-style reggaeton, 92 BPM, Key of A minor, i-VI-III-VII progression, signature dembow rhythm with kick on 1 and 3 and snare clap on syncopated downbeats boom-ch-boom-chick pattern, congas timbales cowbell güiro polyrhythmic top, deep sub-bass following root motion, plucky synth lead doubling vocal, male tenor C3-A4 melodic-rap Spanish delivery with ad-libs ay oh-no-no, tasteful auto-tune, doubled hook vocals, modern Latin master, sub-bass dominant low end, expansive reverb on percussion

---

## 22. BOSSA NOVA & MPB

### Core DNA
- BPM range: Bossa 100-130 (felt as relaxed mid-tempo);
  MPB variable
- Key tendency: Major-key bias with extensive jazz harmony;
  modal interchange common
- Form: AABA jazz-derived; samba-influenced extended forms
- Texture: Nylon-string guitar primary, soft brushed drums,
  upright bass, light percussion (shaker, tamborim)

### Harmonic Vocabulary
- Bossa: ii-V-I throughout, with maj7/9 colors; secondary
  dominants; tritone substitutions
- MPB: jazz-influenced with regional Brazilian colors;
  modal mixture
- Samba-jazz: complex chromatic motion within bossa structure

### Rhythmic Fingerprint
- Bossa nova: signature João Gilberto guitar pattern (bass note
  + syncopated upper chord stabs)
- Brushed snare: soft pulse on 2 and 4
- Tamborim/shaker: 16th-note ostinato
- Samba: faster, more energetic version of bossa rhythm

### Vocal Directive Defaults
Female alto or male tenor, range G3-D5 (F)/C3-G4 (M), intimate
whisper-soft Portuguese delivery, melismatic phrase ends, no
auto-tune, behind-beat phrasing, breath audible.

### Reference Artists
**Bossa classic**: João Gilberto, Antônio Carlos Jobim, Stan Getz,
Astrud Gilberto, Vinicius de Moraes
**MPB**: Caetano Veloso, Gilberto Gil, Milton Nascimento,
Chico Buarque, Elis Regina, Maria Bethânia
**Modern**: Bebel Gilberto, Marisa Monte, Seu Jorge,
Anitta (crossover)

### Suno Style Box Recipe
João-Gilberto-Garota-de-Ipanema-style bossa nova, 124 BPM relaxed feel, Key of F major with jazz extensions, ii-V-I-vi9 progression with maj7-9 colors and tritone substitutions, signature João Gilberto nylon-string guitar pattern bass note plus syncopated upper chord stabs, brushed snare soft pulse on 2 and 4, tamborim 16th-note ostinato, upright bass walking jazz lines, female alto G3-D5 intimate whisper-soft Portuguese delivery with melismatic phrase ends behind-beat phrasing breath audible, warm analog master, room-mic ambience preserved, no auto-tune, optional flute melodic counter-line

---

## 23. GOSPEL & CCM

### Core DNA
- BPM range: Gospel ballad 60-80; Up-tempo gospel 100-135;
  CCM 80-120
- Key tendency: Major keys for praise; minor for testimony;
  frequent modulation upward
- Form: Standard pop with extended bridges; gospel "vamp" sections
  (repeated 1-2 chord vamp with vocal improvisation)
- Texture: Hammond B3, piano, full drum kit, bass guitar, choir,
  solo lead voice

### Harmonic Vocabulary
- Gospel staples: I-IV-V with extensive secondary dominants;
  II-V-I in jazz-gospel
- Modulation: half-step or whole-step lift in final chorus
  is mandatory
- Chord substitutions: gospel-specific voicings — I/3, IV/5, V/7
  inversions; tritone subs

### Rhythmic Fingerprint
- Gospel shuffle: swung 8ths with handclaps
- Modern gospel: hip-hop influenced beats, R&B groove
- CCM: pop-rock rhythm section

### Vocal Directive Defaults
**Lead**: Female alto, range G3-Eb5, gospel-melismatic delivery,
full-throated belted choruses, English with Black-American gospel
inflection, wide slow vibrato, ad-libs throughout, choir backing.

**Choir**: SATB choir, mixed range, layered harmony stacks
+3 +5 +octave +octave-down, English call-response with lead.

### Reference Artists
**Modern gospel**: Kirk Franklin, Mary Mary, Tasha Cobbs Leonard,
Marvin Sapp, Travis Greene, Maverick City Music
**CCM**: Hillsong United, Bethel Music, Lauren Daigle, MercyMe,
Casting Crowns, Elevation Worship
**Classic gospel**: Mahalia Jackson, Aretha Franklin (gospel mode),
James Cleveland, The Clark Sisters
**Korean CCM**: 마커스워십, 어노인팅, 제이어스

### Suno Style Box Recipe
Kirk-Franklin-Stomp-style modern gospel, 120 BPM, Key of E-flat major modulating to F major final chorus, I-IV-V with secondary dominants and II-V-I jazz-gospel progressions, Hammond B3 organ swells, gospel piano comping rootless voicings, full drum kit with backbeat snare and handclaps, bass guitar walking, female alto G3-Eb5 gospel-melismatic full-throated belted English with Black-American inflection wide slow vibrato ad-libs throughout, SATB choir backing layered harmonies +3 +5 +octave call-response with lead, warm analog master, dynamic verse-to-chorus expansion, half-step modulation in final chorus, vamp section with vocal improvisation

---

## 24. ROCK / METAL / PROG

### Core DNA
- BPM range: Hard rock 100-140; Metal 130-180; Prog variable
  (often shifts within song)
- Key tendency: Minor keys (Em, Am, Dm, F#m) dominant; modal
  (Phrygian, Locrian) for darker metal
- Form: Standard rock = VCVCBC; Prog = extended multi-section,
  often through-composed
- Texture: Distorted electric guitars (often paired left/right),
  bass guitar, full drum kit with double-kick for metal,
  vocals from clean to growled/screamed

### Harmonic Vocabulary
- Hard rock: power chord progressions (1-5 dyads),
  I-bVII-IV (Mixolydian), i-bVII-bVI (Aeolian)
- Metal: i5-bVII5-bVI5 (power chord drop), Phrygian dominant runs,
  tritone tension intervals
- Prog: complex extended harmony, modulations within sections,
  modal interchange, occasionally jazz-influenced
- Doom/sludge: slow tritone-heavy progressions, drone-based
- Math metal: odd-meter riff cycles, polyrhythmic guitar layers

### Rhythmic Fingerprint
- Hard rock: backbeat with double-time hi-hat, kick variations
- Metal: double-kick patterns (trigger-driven), blast beats,
  syncopated chugging riffs
- Prog: odd meters (5/4, 7/8, 11/8), tempo changes, polyrhythm
- Doom: half-time crawl, beats stretched to maximum
- Math rock/metal: beat-by-beat rhythmic shifts, tapping

### Vocal Directive Defaults
**Hard rock**: Male tenor, range C3-A4, raspy with grain, anthemic
belt in chorus, English, controlled vibrato.

**Metal clean**: Male tenor or baritone, range B2-G4, powerful
projection, emotional intensity, English, occasional vibrato.

**Metal extreme**: Male, growled or screamed, range varies,
guttural or piercing, English or other, no traditional pitch.

**Prog**: Male tenor, range C3-A4, theatrical phrasing, narrative
delivery, melismatic ornaments, English typically.

### Reference Artists
**Classic rock**: Led Zeppelin, Pink Floyd, The Who, Queen,
Black Sabbath
**Hard rock**: AC/DC, Guns N' Roses, Foo Fighters, Royal Blood
**Metal classic**: Metallica, Iron Maiden, Megadeth, Judas Priest
**Modern metal**: Gojira, Mastodon, Sleep Token, Spiritbox,
Bring Me the Horizon
**Math metal**: Meshuggah, Animals as Leaders, Polyphia (instrumental)
**Prog rock**: Yes, Genesis, Rush, King Crimson, Tool
**Prog metal**: Dream Theater, Opeth, Between the Buried and Me
**Doom/sludge**: Sleep, Electric Wizard, Boris

### Suno Style Box Recipe
Tool-Schism-style progressive metal, 95 BPM with 5/4 and 7/8 sections, Key of D minor with Phrygian color, i-bII-i-bVII-i progression with tritone tension, distorted electric guitars paired hard L/R 60 degrees with palm-muted chugging riffs, fretless bass following guitar with melodic counter-line, full drum kit with double-kick patterns and odd-meter accents on snare, atmospheric pad bed in bridge, male tenor C3-A4 theatrical phrasing with controlled vibrato, English narrative delivery, intimate verses opening to anthemic chorus belt, modern metal master, drum bus parallel compression, dual guitar stereo image preserved, dynamic verse-to-chorus expansion

### Diagnostic Triggers
- "Doesn't feel heavy" → Lower-tuned guitars, double-tracked
  rhythm guitars hard L/R, sub-bass below 60Hz
- "Vocals lost in mix" → Vocal corridor protection 500Hz-3kHz,
  guitars carved with notch at 1-2kHz
- "Drums sound thin" → Layered kick (sub-bass + click on top),
  parallel compression on drum bus

---

## HYBRID GENRE ENCODING

When two or more genres combine in one song, encode them with
explicit ratio and section assignment.

### Hybrid Encoding Format
[Primary-Artist-Song-style] [Primary genre] meets [Secondary-Artist-Song-style] [Secondary genre], [ratio if relevant], [section assignment if relevant]

### Common Hybrid Patterns

**K-Pop + Trap**:
NewJeans-Hype-Boy-style K-pop verse with Pop-Smoke-Dior-style
NY drill chorus, 100 BPM verse felt half-time at 145 BPM drill
in chorus

**K-Pop + Future-Bass**:
IVE-After-Like-style K-pop dance verse with Flume-style
future-bass drop in chorus, 130 BPM throughout

**Country + Trap (Country-Trap)**:
Lil-Nas-X-Old-Town-Road-style country trap, banjo and steel
guitar with 808 sub-bass and trap hi-hats

**Indie Folk + Electronic**:
Bon-Iver-22-style indie electronic folk, fingerpicked acoustic
verse with vocoder-stacked chorus and electronic percussion

**R&B + Drill (R&B Drill)**:
PinkPantheress-Boys-a-Liar-style R&B drill, soulful melodic R&B
vocal over UK drill drum pattern

**Jazz + Hip-Hop**:
Robert-Glasper-Black-Radio-style jazz hip-hop, jazz harmony with
hip-hop derived swung beats and rap verses

**Bossa Nova + Electronic**:
Bebel-Gilberto-style electro-bossa, nylon-string bossa pattern
with electronic percussion and ambient pads

**Latin + Trap (Latin Trap)**:
Bad-Bunny-Yo-Perreo-Sola-style Latin trap, dembow rhythm with
trap 808 sub-bass and Spanish melodic-rap vocal

**Gospel + Hip-Hop**:
Kanye-Jesus-is-King-style gospel hip-hop, gospel choir with
hip-hop production and rap verses

**Metal + Pop (Metal-Pop)**:
Bring-Me-the-Horizon-Mantra-style metal-pop, distorted guitars
with pop song structure and clean vocal hooks

### Hybrid Construction Principles

1. **Primary genre ≥ 50%**: One genre should dominate. Equal
   50/50 splits often produce genre confusion rather than fusion.

2. **Section-specific genre**: Often more effective than blended
   throughout. Example: trap verse + R&B chorus, rather than
   trap-R&B blended in every section.

3. **Common element bridges**: One element preserved across
   genre shifts (vocal, key, melodic motif) anchors listener
   through genre changes.

4. **Tempo unification**: Use half-time/double-time perception
   tricks to bridge genres at different native BPMs. Example:
   140 BPM trap can flip to 70 BPM half-time chorus that feels
   like ballad without changing actual tempo.

5. **Frequency band separation**: When two genres play
   simultaneously, assign them to distinct frequency ranges.
   Latin percussion in low-mid (200-500Hz), J-pop guitars in
   high-mid (3-6kHz), vocal in protected corridor (500Hz-3kHz).

---

## GENRE FAMILY DIAGNOSTIC SHORTHAND

### When generated track misses target genre

**"Sounds generic K-pop"** → Add maximalist + glossy + concept
keyword (Y2K, retro-future, etc.) + per-section genre cues

**"Trap sounds dated"** → Off-grid trip patterns instead of
predictable hat rolls

**"Drill sounds soft"** → Sliding 808 dominant; remove harmonic
chords leaving single melodic loop

**"Future-bass not impactful"** → Drop-in pull-back arrangement
(vocal + kick only first 2 bars of drop)

**"Folk too produced"** → Strip layers, room-mic ambience,
acoustic-only palette

**"Jazz feels stale"** → Modal interchange cascade or tritone
substitutions in bridge

**"Latin feels cliché"** → Layer congas/timbales/güiro
polyrhythmic top + specific regional reference

**"Gospel lacks soul"** → SATB choir backing + call-response +
vamp section with improvisation

**"Country sounds pop"** → Steel guitar / fiddle / banjo
prominence + cross-stick train beat

**"Metal sounds polished"** → Lower tuning + double-tracked
rhythm guitars hard L/R + room ambience on drums

---

## REFERENCES AND FURTHER READING

The information in this file synthesizes from the following:

- Hooktheory's TheoryTab database — popular music harmonic patterns
- Berklee Online genre composition curriculum
- "Computational Analysis of K-Pop Music Production" academic studies
- Roland production tutorials (Amapiano log drum, EDM, hip-hop)
- Attack Magazine production breakdowns (UK garage, drum and bass)
- Sound on Sound producer interviews (D'Angelo "Voodoo" sessions,
  Frank Ocean studio practice, K-pop production teams)
- NPR Music genre essays (hyperpop microgenre evolution)
- Reddit r/musictheory crowd-sourced genre analysis
- Genre-specific YouTube tutorials from established producers
- Wikipedia musicology entries for traditional and regional genres
- The Ethan Hein Blog harmonic and rhythmic analyses
- "Music Genre" reference texts (Allmusic genre guides)
- Hyperpop/digicore microgenre documentation (NPR, NME, Pitchfork)
- City pop revival scholarship (Vault Publication, Vanpaugam)
- Korean indie scene documentation (Korean Indie blog,
  Sound of Life)

For harmonic considerations within genres, see
`02_HARMONY_FOUNDATIONS.md` and `03_HARMONY_ADVANCED.md`.

For rhythmic patterns and groove formulas, see
`04_RHYTHM_AND_FORM.md`.

For Suno-specific encoding rules and pronunciation guides, see
`09_SUNO_ENGINE.md` and `10_SUNO_LYRICS_TAGS.md`.

<!-- USER EXTENSION ZONE — append additional genres, sub-genres,
     reference artists, or genre-specific notes below this line -->

---
<!-- ============================================================ -->
<!-- USER EXTENSION (v2.2 / 2026-05-09) — 2025-2026 GLOBAL TREND   -->
<!-- ============================================================ -->

## SECTION 9 — 2025-2026 K-POP PRODUCTION TRENDS

### 9.1 거시 트렌드 요약 (검증: CNN 2026-05, Billboard 2025, Hollywood Reporter 2025)

5세대 K-pop은 다음 4가지 축으로 정리된다.

1. **Tempo 상승** — 평균 BPM 110→128로 이동. UK garage·jersey club·Baltimore club 인용.
2. **Hyperpop 인접** — pitched-up vocal chops, glitch fills, sub-bass drops, 808 glide.
3. **Vocal layering 단순화** — 4세대(NewJeans) 미니멀 + 5세대 detune triple-track 혼합.
4. **Sonic identity 분화** — HYBE(밝은 plucky), SM(어두운 hybrid trap), YG(loud trap), JYP(retro funk-pop).

### 9.2 검증된 2025-2026 레퍼런스 트랙 (표기 규약 준수)

#### A. 한국 (한글–영문 병기 필수)

- **에스파 – Whiplash (위플래쉬)** | 2024-10 | SM
  - 핵심 사운드: muted brass stabs, plucky synth, UK garage shuffle, sub-bass slide
  - BPM 99 / Key F minor / 2-step garage groove
  - Suno 키워드: `muted brass stab, plucky synth lead, UK garage shuffle, sub-bass slide, dark minimalist K-pop`

- **르세라핌 – Chasing Lightning (체이싱 라이트닝)** | 2025 | HYBE/SOURCE
  - 핵심 사운드: drum-and-bass breakbeat, distorted bass, urgent female vocal
  - BPM 174 (DnB feel) / Key D minor
  - Suno 키워드: `drum and bass breakbeat, reese bass, urgent female vocal, atmospheric pad, K-pop DnB hybrid`

- **로제 & 브루노 마스 – APT.** | 2024-10 | THEBLACKLABEL/Atlantic
  - 핵심 사운드: 80s power-pop chord stack, gang vocal chant, Toni Basil "Mickey" interpolation
  - 프로듀서: Cirkut (2026 Grammy POTY)
  - Suno 키워드: `80s power pop, gang vocal chant, syncopated handclap, retro disco guitar, glossy pop production`

- **베이비몬스터 – DRIP (드립)** | 2025 | YG
  - 핵심 사운드: distorted 808, trap hi-hat triplet, aggressive shout-rap, YG signature loud snare
  - BPM 140 / Key G minor
  - Suno 키워드: `distorted 808 bass, trap hi-hat triplet, aggressive shout rap, YG style loud snare, hard hitting K-pop`

- **아일릿 – Magnetic (마그네틱)** | 2024 | HYBE/BELIFT
  - 핵심 사운드: Jersey club bed-squeak kick, plucky NewJeans-lineage synth, breathy vocal
  - BPM 150 (Jersey club) / Key F# minor
  - Suno 키워드: `jersey club bed squeak kick, plucky synth, breathy female vocal, minimal NewJeans style production, half-time chorus`

- **헌트릭스 – Golden (골든)** | 2025 | KPop Demon Hunters OST
  - 핵심 사운드: cinematic K-pop, orchestral hybrid, anthemic chorus
  - Suno 키워드: `cinematic K-pop, orchestral synth hybrid, anthemic female chorus, hero theme energy`

- **헬로비너스 후속 5세대: HEARTS2HEARTS, IZNA, ALLDAY PROJECT** (2025-2026 데뷔)
  - 공통 키워드: `5th gen K-pop, refined minimalism, mid-tempo 110-125 BPM, breathy harmony stack`

#### B. 일본/J-Pop (영문–로마자 병기)

- **Mrs. GREEN APPLE – Lilac (ライラック)** | 2024 | EMI
  - Suno 키워드: `bright J-pop band, melodic male tenor, anime opening energy, modulating chorus`

- **Creepy Nuts – Bling-Bang-Bang-Born** | 2024
  - Suno 키워드: `Japanese hip-hop, jersey club kick, rapid-fire rap, anthemic hook`

- **Number_i – BON** | 2024 | TOBE
  - Suno 키워드: `Japanese hip-hop K-pop hybrid, sharp boy group vocal, modern trap production`

#### C. 글로벌 (2025-2026)

- **Lady Gaga – Abracadabra** | 2025 | Interscope (Mayhem 앨범)
  - 프로듀서: Cirkut, Andrew Watt
  - Suno 키워드: `dark electroclash, gothic dance pop, pulsating synth bass, theatrical female vocal, 2000s electro revival`

- **The Weeknd – Big Sleep** | 2025 | XO/Republic (Hurry Up Tomorrow)
  - 프로듀서: Cirkut, Mike Dean
  - Suno 키워드: `cinematic synthwave, melancholic male falsetto, atmospheric pad, late-night R&B`

- **Charli XCX – BRAT (Deluxe)** | 2024-2025 | Atlantic
  - Suno 키워드: `bratty hyperpop, distorted 808, dry close-mic vocal, A.G. Cook style production, club ready`

- **Sabrina Carpenter – Espresso / Manchild** | 2024-2025 | Island
  - Suno 키워드: `disco pop revival, cheeky female vocal, walking bass, syncopated kick, retro modern hybrid`

- **Chappell Roan – Pink Pony Club / Good Luck Babe!** | 2024 | Island
  - Suno 키워드: `theatrical synth-pop, soaring female belt, 80s coming-of-age, lush analog synth pad`

- **Billie Eilish – BIRDS OF A FEATHER** | 2024 | Darkroom (Hit Me Hard And Soft)
  - 프로듀서: FINNEAS
  - Suno 키워드: `bedroom pop, intimate close-mic vocal, breathy female lead, minimal acoustic, warm tape saturation`

### 9.3 2025-2026 K-pop 5세대 미세 장르 (Sub-genre Map)

| 미세 장르 | 핵심 BPM | 대표 그룹 | Suno 키워드 |
|---|---|---|---|
| K-Garage | 130-145 | aespa, ILLIT | `UK garage shuffle, 2-step groove, plucky synth, breathy vocal` |
| K-Jersey | 140-160 | ILLIT, Creepy Nuts | `jersey club bed-squeak kick, half-time chorus, sliding 808` |
| K-DnB | 165-180 | LE SSERAFIM, ITZY | `drum and bass breakbeat, reese bass, atmospheric pad, urgent vocal` |
| K-Trap-Loud | 130-150 | BABYMONSTER, BLACKPINK | `aggressive trap, distorted 808, loud snare, shout rap, YG style` |
| K-Hyperpop | 140-180 | NMIXX, KISS OF LIFE | `pitched-up vocal chop, glitch fill, hyperpop synth, genre switch` |
| K-Retro-Funk | 100-115 | NewJeans-lineage | `2000s R&B, plucky synth, breathy harmony, minimal kick, retro K-pop` |
| K-Cinematic | 90-130 | aespa, Huntr/x | `orchestral hybrid, hero theme, cinematic K-pop, dramatic chorus` |

### 9.4 NewJeans-Lineage 미니멀 K-Pop 정밀 어법

NewJeans 사운드는 4세대 후반~5세대 초반의 표준이 되었다. 직접 언급은 Suno 차단 위험이 있으므로 다음 우회 표현 사용:

- ❌ Avoid: "NewJeans style"
- ✅ Use: `breathy female vocal, plucky synth, minimal kick drum, 2000s R&B revival, soft brushed snare, half-time groove, airy texture`

### 9.5 HYBE / SM / YG / JYP 시그니처 분해 (2025-2026)

**HYBE (BELIFT/SOURCE/ADOR)**
- Plucky synth, breathy vocal, minimal kick, half-time chorus, jersey club 인용
- 키워드: `bright plucky synth, breathy female harmony, minimal modern K-pop, jersey club influence`

**SM Entertainment (aespa, RIIZE, NCT)**
- Hybrid trap, dark synth, sub-bass, UK garage 인용, theatrical 보컬
- 키워드: `hybrid K-pop, dark synth, sub-bass slide, UK garage shuffle, theatrical vocal layering`

**YG Entertainment (BLACKPINK, BABYMONSTER)**
- Loud snare, distorted 808, aggressive shout, trap signature
- 키워드: `loud snare, distorted 808 bass, aggressive shout rap, hard hitting trap K-pop`

**JYP Entertainment (TWICE, NMIXX, ITZY)**
- Genre-switching, retro funk-pop, brassy stabs, melodic chorus
- 키워드: `genre-switching K-pop, retro funk pop, brassy stab, melodic female chorus, mid-tempo`

---

## SECTION 10 — 2025-2026 GLOBAL POP TRENDS

### 10.1 핵심 거시 트렌드

1. **Disco/Funk Revival 2.0** (Sabrina Carpenter, Dua Lipa) — walking bass, syncopated handclap, glossy retro-modern hybrid
2. **Bedroom Pop 성숙화** (Billie Eilish, Gracie Abrams) — close-mic intimacy, tape saturation, minimal arrangement
3. **Hyperpop 주류화** (Charli XCX BRAT) — distorted 808, dry vocal, club-pop hybrid
4. **80s Synth-Pop 재해석** (Chappell Roan, The Weeknd) — analog pad, gated reverb 변형, theatrical belt
5. **Electroclash 부활** (Lady Gaga Mayhem) — pulsating synth bass, 2000s-electro 인용

### 10.2 2026 Grammy Producer of the Year — Cirkut Decomposed

**시그니처 요소**:
- Wide stereo synth pads with subtle pitch modulation
- Layered drum stacks (acoustic + electronic kick)
- Vocal stack: lead + 4-6 harmony layers, each detuned ±5-10c
- Retro reference + modern processing (80s synth + 2020s side-chain)

**Suno Style Box 어법 (200자 모드)**:
2020s pop production, Cirkut-inspired layered synth stack, wide stereo pad with subtle detune ±10 cents, layered acoustic-electronic kick, glossy female vocal with tube saturation, retro disco guitar accent, side-chain pumping pad, anthemic chorus

### 10.3 장르별 프로듀서 매핑 (2025-2026)

| 장르 | 대표 프로듀서 | 핵심 어법 |
|---|---|---|
| Mainstream Pop | Cirkut, Max Martin, Andrew Watt | layered synth, wide stereo, glossy vocal |
| Indie/Alt-Pop | Jack Antonoff, Aaron Dessner | tube saturation, vintage drums, intimate vocal |
| Bedroom/Alt | FINNEAS | close-mic, minimal acoustic, breathy lead |
| Hyperpop | A.G. Cook, Dylan Brady, BNYX | distorted 808, dry vocal, glitch chops |
| Hip-Hop/R&B | Mike Dean, Metro Boomin, BNYX | atmospheric pad, sub-bass, dark trap |
| K-Pop Hit-Maker | 250, Slow Rabbit, Ryan S. Jhun | UK garage, plucky synth, hybrid trap |

---

## SECTION 11 — 장르 LIBRARY 적용 워크플로우

### 11.1 신곡 작업 시 결정 순서

1. **컨셉 → 미세 장르 매칭** (§9.3 표 사용)
2. **레이블/프로듀서 시그니처 선택** (§9.5 또는 §10.3)
3. **레퍼런스 트랙 1-3개 선택** (§9.2, §10.1) — 표기 규약 준수
4. **Suno 키워드 추출** → 각 레퍼런스에서 3-5개 핵심 키워드 채택
5. **Style Box 작성** (CREATE/COVER 둘 다 Dense 700-950 / sketch 시 Tight 250-350)
6. **Exclude Styles 작성** — 의도하지 않은 트렌드 차단 (예: K-pop 작업 시 Latin percussion 차단)

### 11.2 Genre Confusion 방지 규칙

- 한 트랙에 미세 장르는 최대 2개까지 hybrid 허용
- 3개 이상 섞으면 Suno가 평균화하여 generic 결과 산출
- 의도된 genre-switching이라면 섹션별로 명시: `[Verse: K-garage] [Chorus: K-hyperpop]`

<!-- USER EXTENSION ZONE -->

## §12. v2.6 보강 — 마이크로 장르 풀 + 2026 트렌드 인덱스 (2026-05-20)

09 §24.2 마이크로 장르 1차 룰의 실전 적용을 위한 풀. 거시 장르
요청 시 시스템이 이 풀에서 하위 갈래를 즉시 제시해 평균 회귀
차단.

### §12.1 거시 vs 마이크로 장르 — 구분 기준

**거시 장르 (Style Box 1번 자리 사용 금지)**:
pop, rock, hip-hop, country, electronic, jazz, R&B, folk, ballad,
city pop, K-pop, J-pop

위 단어 단독 사용 시 Suno는 해당 거시 클러스터의 통계적 중심
= "평균"으로 회귀. 항상 하위 + 시대 + 시그니처로 좁힘.

**마이크로 장르 (Style Box 1번 자리 사용 권장)**:
서브장르명 자체에 시대·텍스처·미학이 압축돼 있는 태그. 모델을
훈련 분포의 좁은 영역에 착지시킴.

### §12.2 거시 장르별 마이크로 풀

**Pop → 마이크로**
- dream pop, bedroom pop, hyperpop, art pop, sophisti-pop
- synth-pop (80s-inspired / late-2010s revival)
- electropop, baroque pop, jangle pop, twee pop
- chamber pop, indie pop with shoegaze guitars

**Rock → 마이크로**
- shoegaze, slowcore, math rock, post-rock, krautrock
- 90s grunge (Seattle sound), post-punk revival
- garage rock (60s mod / 2000s NYC)
- emo revival, indie rock (2010s Brooklyn)
- alt-rock with cinematic strings

**Hip-hop → 마이크로**
- boom bap (90s East Coast), trap (Atlanta 2010s)
- melodic drill (UK), cloud rap, pluggnB
- conscious rap (jazz-influenced), Memphis horror rap
- lo-fi hip hop (Tokyo bedroom), drumless hip hop

**Electronic / Dance → 마이크로**
- modern melodic club (2024-2026), Afro house, amapiano
- melodic techno (deep / progressive), UK garage 2-step
- jersey club, footwork, drum & bass (liquid / neurofunk)
- synthwave, vaporwave, hyperpop, future bass
- cinematic EDM (2026 트렌드 — 페스티벌 군중 아닌 스토리텔링용 드랍)

**Country / Folk → 마이크로**
- Americana, alt-country, modern country pop (2024+)
- Appalachian gothic folk, fingerstyle neo-soul folk
- bedroom folk, sad-girl indie folk (Phoebe Bridgers 결)
- bluegrass revival, country trap crossover

**Jazz / Soul / R&B → 마이크로**
- neo-soul (D'Angelo era), modern R&B (Yebba / SZA 결)
- nu-jazz, fingerstyle neo-soul
- bossa nova revival, samba-jazz, broken beat
- smoky lounge jazz, late-night sophisti-soul

**City Pop / J-pop 계열 → 마이크로**
- Neo City Pop (2020s Tokyo revival — 2026 핫 트렌드)
- 80s Tokyo city pop (Tatsuro Yamashita / Mariya Takeuchi 결)
- shibuya-kei, J-pop with anime opening DNA
- J-rock acoustic (YOASOBI 결), Mrs. GREEN APPLE-style
- futurefunk (city pop sample-based dance)

**Ballad / Acoustic → 마이크로**
- piano ballad (slow / mid-tempo)
- chamber ballad (string-led)
- indie folk ballad (fingerpicked)
- modern pop ballad (radio-ready cinematic)
- alt-R&B ballad (Frank Ocean 결)

**Korean 장르 → 마이크로**
- K-indie (Hyukoh era / Adoy / Se So Neon 결)
- modern K-pop 5th-gen (2024-2026 production spine)
- K-ballad (early-2000s revival)
- K-trot modernized (oompah + electronic)
- K-rock (J-rock anime opening DNA 융합)

### §12.3 2026 5월 트렌드 인덱스

운영자가 "최신/트렌디"를 요청하거나 곡이 자꾸 올드해질 때
참조. 외부 검증된 2026 핫 트렌드:

**1. Neo City Pop 글로벌 메인스트림**
- 80s 도쿄 네온 + 모던 베드룸 팝 렌즈
- 풍성한 재즈 코드, 하이퍼클린 프로덕션, 낙관 + 멜랑콜리
- 단순 복고 아닌 미래지향 청사진
- 키워드: "neo city pop, 2020s Tokyo revival, jazz-inflected
  harmony, bedroom pop production, optimistic melancholy"

**2. 시네마틱 EDM (성숙한 댄스)**
- 2010s 네온·베이스 헤비 시대와 다름
- 댄스 + 시네마틱 사운드 디자인 + 감정적 분위기 +
  하이브리드 오케스트럴
- 페스티벌 군중이 아닌 **스토리텔링용 드랍**
- 키워드: "cinematic EDM, narrative drops, hybrid orchestral
  textures, emotional pulsing kicks, brand-friendly polish"

**3. Organic Sounds (AI 백래시 반응)**
- 진짜 악기, 진정성, grounded minimalism
- 슈퍼 정제된 디지털 광택에서 멀어짐
- 키워드: "organic instruments, raw recording feel, slight
  timing imperfections, human-played not programmed,
  analog warmth"

**4. Rock / Metal 부활**
- 90s nu-metal 부활 → 2020s 모던 록 광범위
- emo revival, post-punk revival, alt-rock with cinematic strings
- 키워드: "modern rock revival, distorted guitars with
  cinematic depth, raw vocals not polished"

**5. Wild Genre-Blending (마이크로 융합)**
- 두 장르 스택까지(09 §24.3 한계) — 예상 밖 조합일수록 강함
- Afro House × Drum'n'Bass, Hyperpop × Indie Folk,
  Bossa Nova × Drill, Synth-pop × Doom Metal
- pluggnB 같은 나노장르 부상

**6. 감정 기반 조직 (장르 라벨에서 무드로)**
- Spotify 플레이리스트가 감정·무드 컬렉션으로 이동
- 곡 제목·태그도 감정 우선 ("the feeling of empty Sunday
  morning" 식)
- 17 Scene Dossier 철학과 직결 — 감정·장면을 1차 앵커로

### §12.4 §11.2 보강 — 장르 스택 룰 갱신

기존 §11.2(2-3장르 hybrid 허용)는 09 §24.3 검증 후 정정:

- 한 박스 1-2장르까지가 안전. 3장르 직접 박으면 generic 평균
- 3장르 의도 시 **섹션별 분할만** 허용:
  `[Verse: K-garage] [Chorus: K-hyperpop with subtle drum'n'bass break]`
- 60/30/10 블렌딩은 *비율 박스 안에 명시*가 아니라 *우선
  순위 머릿속*에서. 실제 박스에는 주 1 + 보조 1로 압축.

---

# END OF GENRE LIBRARY


---

## SECTION 13. INDUSTRY CATEGORY DECOMPOSITION (v2.11 NEW — Case 41)

Operator discovery (Case 41 v2.10 session):
> *"K-pop은 그냥 분위기 정도이지 쓴다고 해도 뭔가 특별 가수도
>  지칭도 안 되고 한글로 지랄해도 어차피 안 감겨서 차라리
>  쪼개는 게 훨씬 나은 거 같아"*

National-pop labels ("K-pop", "J-pop", "Latin pop", "C-pop",
"Afrobeats", "Hyperpop") are *industry categories*, not genres.
Suno regresses to 5-7 year average when these appear in Position 1.

This section provides decomposition tables for each industry category.

### 13.1 K-pop decomposition

❌ `"K-pop"` (Position 1)
✅ One of these (Position 1):

**5세대 (2023+) sound:**
- `Modern Korean pop production 2024-2026 + [microgenre]`
- Microgenre choices: `contemporary R&B`, `UK garage 2-step`,
  `Y2K nostalgia pop`, `hyperpop crystalline`, `plugg trap`,
  `Jersey club`, `phonk`, `drill-influenced`

**4세대 (2018-2022) sound:**
- `Late-2010s K-pop production + [microgenre]`
- Microgenre: `EDM-pop fusion`, `tropical house`, `future bass`,
  `noise music`, `experimental pop`

**3세대 (2012-2017) sound:**
- `Mid-2010s K-pop production + [microgenre]`
- Microgenre: `dubstep-pop`, `trap-pop`, `electro house pop`

**2세대 (2007-2011) sound:**
- `Late-2000s K-pop production + Eurodance pop`
- Often paired with: `2-step shuffle`, `synthpop revival`

**Trot:**
- `Modern crossover trot + [microgenre]` (07 영문 음역 페어 의무)

### 13.2 J-pop decomposition

❌ `"J-pop"` (Position 1)
✅ One of these (Position 1):

**City Pop:**
- `1980s Japanese city pop revival + 2024 production`
- Add: `analog warmth`, `slap bass`, `dreamy synth pads`

**Modern J-pop:**
- `Modern Japanese pop production 2024-2026 + [microgenre]`
- Microgenre: `J-rock`, `anison`, `Vocaloid-influenced`, `kawaii pop`

**Shibuya-kei revival:**
- `Shibuya-kei nostalgic indie pop + sample-heavy crate-digging`

**Vocaloid:**
- `Vocaloid hyperpop crossover + pitched-up vocal + crystalline synth`

### 13.3 Latin pop decomposition

❌ `"Latin pop"` (Position 1)
✅ One of these (Position 1):

**Reggaeton:**
- `Modern reggaeton perreo 2024-2026 + dembow rhythm + Spanish topline`

**Bachata:**
- `Modern bachata + Dominican guitar lead + Spanish vocal topline`

**Cumbia:**
- `Modern Mexican cumbia + accordion lead + cumbia rhythm`

**Latin trap:**
- `Latin trap + 808 + Spanish-language flow`

**Tropical / Bossa:**
- `Brazilian bossa nova jazz fusion + Portuguese topline`

### 13.4 Hyperpop decomposition

❌ `"Hyperpop"` (Position 1) — too vague, splits between PC Music /
hyperflip / etc.

✅ One of these (Position 1):

**PC Music aesthetic (early hyperpop):**
- `PC Music aesthetic 2023 + pitched-up vocal + crystalline detune`

**Hyperflip (Frailty era):**
- `Hyperflip 2024 + glitched 808 + crash heavy + ravecore`

**Bubblegum bass:**
- `Bubblegum bass + sugar-rush synth + chipmunk vocal pitch-up`

**Digicore:**
- `Digicore + emo-rap crossover + autotuned vocal + trap drums`

### 13.5 Afrobeats decomposition

❌ `"Afrobeats"` (Position 1)
✅ One of these (Position 1):

**Amapiano:**
- `Amapiano + log drum + Lagos production`

**Lagos Afrobeats:**
- `Lagos Afrobeats 2024 + Yoruba topline + percussion-driven`

**Highlife:**
- `Ghanaian highlife + guitar-driven + group vocal call-response`

### 13.6 Universal decomposition pattern

Any industry category can be decomposed using:

```
[Microgenre] + [Era anchor] + [Language topline] + [Production trait]
```

Examples applied:
- `Hyperpop crystal + 2024 + English-language topline + glitched 808`
- `Modern K-indie + late-2020s + Korean-language vocal + lo-fi tape`
- `City pop revival + 2024 + Japanese topline + analog warmth`
- `Latin trap + 2025 + Spanish-language flow + 808 slides`

### 13.7 Cross-reference

- 00 C-40 (industry category banishment)
- 00 C-45 (Position weighting)
- 09 §40 (artist workaround framework)

---

## SECTION 14. 2026 MICROGENRE DIVERSITY POOL (v2.11 NEW)

Operator concern (v2.11 session):
> *"다양성 최신 트렌드적 사운드 만들어내는 건 잘 못하고 있으니
>  그런 부분도 추가 보충"*

This section catalogs 2026-current microgenres to expand diversity
beyond the existing 99c rotation.

### 14.1 Electronic / Dance microgenres

**Festival / Mainstage:**
- Festival hardstyle (155 BPM, reverse bass)
- Big-room house revival (128 BPM, mainstage drops)
- Trance revival (132-140 BPM, Goa-influenced)
- Eurodance 2026 (132 BPM, 90s sample references)

**Underground / Club:**
- UK 2-step garage (138-140 BPM, skippy drums)
- Future garage (130 BPM, sub-bass + skip)
- Speed garage revival (140 BPM, reece bass)
- Bassline (140 BPM, wobble bass + vocal chops)
- Jersey club (140 BPM, bed-squeak sample + claps)
- Baltimore club (130 BPM, sample chops)
- Brazilian funk / Baile (130 BPM, atabaque + vocal chant)

**Experimental:**
- Hyperflip (varies BPM, glitched 808)
- Drum & bass liquid (174 BPM, jazzy chords)
- Drum & bass jump-up (174 BPM, wobble bass)
- Footwork / Juke (160 BPM, triplet rhythm)
- Phonk (140 BPM, cowbell + Memphis rap vocal)
- Drift phonk (140 BPM, hard distortion)
- Ambient techno (120 BPM, atmospheric pads)

### 14.2 Hip-hop / R&B microgenres

**Trap / Drill:**
- Plugg (130 BPM, ethereal synths + 808)
- Rage (160 BPM, distorted synths + trap drums)
- Sexy drill (140 BPM, Latin / R&B sample + drill drums)
- Detroit drill (140 BPM, raw / aggressive)
- UK drill (140 BPM, sliding 808 + skip-hat)
- Brooklyn drill (140 BPM, NY sample + drill drums)
- Memphis trap revival (140 BPM, cowbell + crunchy snare)

**R&B:**
- Alt R&B (90-100 BPM, atmospheric + breathy vocal)
- Hyper R&B (varies, pitched-up vocal + crystalline synth)
- 90s R&B revival (90 BPM, new jack swing + smooth vocal)
- Trap-soul (100 BPM, 808 + melismatic vocal)

### 14.3 Rock / Indie microgenres

**Rock:**
- Math rock (varies BPM, polyrhythmic + tapping guitar)
- Post-rock cinematic (slow build, crescendo)
- Shoegaze revival 2024 (mid-tempo, wall-of-guitar)
- Slowcore (60-80 BPM, sparse + mournful)
- Emo revival (170 BPM, math-influenced + emo vocal)
- Midwest emo (140 BPM, intricate guitar + raw vocal)

**Indie:**
- Bedroom pop (mid-tempo, lo-fi + intimate vocal)
- Dream pop (mid-tempo, reverb-heavy + ethereal vocal)
- Hyperpop crystal (any BPM, pitched-up + crystalline)
- Pluggnb (90 BPM, plugg synths + R&B vocal)

### 14.4 Cinematic / Atmospheric

- Cinematic hybrid (epic strings + modern percussion)
- Trailer music (rising tension + impact hits)
- Lo-fi study (80-90 BPM, jazz samples + vinyl crackle)
- Ambient drone (no fixed BPM, sustained pads)
- Dark ambient (no fixed BPM, drone + texture)
- Neoclassical (piano-driven, modern composer style)

### 14.5 Folk / Acoustic / World

- Modern folk revival (90-100 BPM, banjo + violin + harmony)
- Indie folk (mid-tempo, fingerpicked guitar)
- Nu folk (100 BPM, folk + indie pop crossover)
- Brazilian bossa fusion (100 BPM, nylon guitar + Portuguese)
- Cumbia digital (130 BPM, accordion + 808)
- Reggaeton perreo (95 BPM, dembow)

### 14.6 Crossover/fusion microgenres (Operator's specialty)

These are *Operator-discovered Polarity Fusion candidates*:
- Trot × Future Bass (Case 38 lineage)
- 마당놀이 × NU DISCO (Case 34 lineage)
- City Pop × Modern Club (Case 40 lineage)
- UK Garage × Vintage Disco (Case 24b lineage)
- Indie ballad × J-rock (Case 36/37 lineage)
- J-rock × Piano-rock 2-step garage (Case 36)
- MJ-Funk × EDM Club (Case 39 lineage)

### 14.7 Diversity rotation rules

- Same genre family 3+ songs consecutively → rotate to different
  family (C-37)
- Same BPM zone (130-140) 3+ songs → shift to different zone
- Use Tight Mode (250-350 chars) for fresh / unfamiliar microgenres
  to maximize Position 1 weight

### 14.8 Cross-reference

- 00 C-37 (diversity rules) / C-47 (Tight/Dense mode)
- 99b §[new] — Microgenre keyword library (v2.11 expansion)

---

## SECTION 15. PRODUCER NAMES — ARTIST WORKAROUND DEEP LIBRARY (v2.11 NEW)

Detailed Producer Names library for 5-Layer artist workaround
(00 C-1.2 / 09 §40). Use these as Layer 1 when blocked artist is the
target.

### 15.1 By era

**1960s-70s Motown / Soul:**
- Berry Gordy / Holland-Dozier-Holland / Smokey Robinson / Norman Whitfield

**1970s Disco / Funk:**
- Nile Rodgers / Bernard Edwards / Giorgio Moroder / Quincy Jones

**1980s Pop/R&B:**
- Quincy Jones / Jam & Lewis / Babyface / L.A. Reid / Teddy Riley

**1990s Hip-hop / R&B:**
- Dr. Dre / Timbaland / Pharrell / Rodney Jerkins / Babyface

**2000s Pop:**
- Max Martin / Rodney Jerkins / Bloodshy & Avant / The Neptunes

**2010s Pop:**
- Max Martin / Shellback / Dr. Luke / Stargate / Greg Kurstin

**2020s Pop:**
- Jack Antonoff / Finneas / Greg Kurstin / Max Martin / Shellback /
  Cirkut / Benny Blanco

### 15.2 By genre

**Hip-hop:**
- Dr. Dre / J Dilla / Pharrell / Timbaland / Kanye West-style /
  Just Blaze / Mike Will Made It / Metro Boomin / Boi-1da /
  Kenny Beats / Pierre Bourne / Wheezy / Murda Beatz

**R&B:**
- Pharrell / Timbaland / Rodney Jerkins / Jam & Lewis / Babyface /
  Bryan-Michael Cox / Tricky Stewart / The-Dream / Hit-Boy

**Pop:**
- Max Martin / Shellback / Jack Antonoff / Greg Kurstin / Finneas /
  Benny Blanco / Cirkut / Stargate / Dr. Luke / Ryan Tedder

**EDM:**
- Diplo / Calvin Harris-style / Skrillex-style / Hardwell-style /
  Tiësto-style / Martin Garrix-style / David Guetta-style /
  Major Lazer-style / Marshmello-style / Kygo-style

**K-pop:**
- Teddy Park (테디) / Yoo Young-jin (유영진) / Shinsadong Tiger
  (신사동호랭이) / Black Eyed Pilseung (블랙아이드필승) / Kenzie /
  RYAN JHUN / Bang Si-hyuk-style

**Rock:**
- Rick Rubin / Butch Vig / Brendan O'Brien / Steve Albini-style /
  Bob Rock-style / Mutt Lange-style / Jeff Lynne-style

**Country:**
- Dann Huff / Jay Joyce / Frank Liddell / Buddy Cannon / Dave Cobb

**Latin:**
- Tainy / Sky Rompiendo / Mauro Cattivelli / Edge / DJ Luian /
  Mambo Kingz / Rauw Alejandro-style

### 15.3 Modern "style lineage" alternatives

When producer name doesn't exist or is too specific, use lineage:

- `Motown-era production`
- `Atlantic Records 1970s soul-era production`
- `Tin Pan Alley songwriting tradition`
- `Studio One reggae roots-era`
- `Memphis Stax soul production`
- `Detroit Techno first-wave production`
- `Cologne minimal techno production`

### 15.4 Cross-reference

- 00 C-1.2 / C-1.3 — 5-Layer + Producer Names default
- 09 §40 — 5-Layer workaround framework
- 99b §[new] — Producer Names quick-reference list

---

# END OF 05_GENRE_LIBRARY v2.11


## § USER EXTENSION ZONE v2.0 (2026-05-24)

bitwize/genres INDEX (1,143줄 → 388 장르 인덱스) + SJY051 genres
20 인덱스 통합. 풀바디 우회 어법은 *21 GENRE_ARTIST_LIBRARY*에
잠금. 본 파일은 인덱스 보강.


### §UE-1. 21 GENRE_ARTIST_LIBRARY 라우팅

운영자 *"[장르] 결로"* 발화 시:
1. 본 파일 §UE-2 인덱스 → 21 §[해당 장르] view
2. 21에 없음 → zip bitwize/genres/[X]/README.md view
3. zip에도 없음 → 외부 검증 + Sketch 1개 권유 (C-41)


### §UE-2. Microgenre Quick Reference (2025-2026)

#### Pop Microgenres
- hyperpop / glitchcore / bedroom pop / alt-pop / dance pop /
  synth-pop revival / maximalist pop / minimal pop

#### Hip-Hop Microgenres
- drill (Chicago / UK / NY) / plugg / phonk / jersey club /
  bedroom hip-hop / hyperpop rap / trap / afrotrap / pluggnb

#### Electronic Microgenres
- amapiano / afrobeats / UK garage revival / 2-step revival /
  drum-and-bass revival / hardstyle / techno minimal /
  jersey club / shatta / dembow / reggaeton / hyperpop electronic

#### Rock Microgenres
- shoegaze revival / post-punk revival / math rock / emo revival /
  indie sleaze / grunge revival / garage rock / psychedelic rock

#### World Microgenres
- K-pop (4-gen, 14 subgenres — §UE-3)
- J-pop (city pop revival, vocaloid, anime-OST)
- Latin (reggaeton, perreo, dembow, bachata, cumbia)
- Afro (afrobeats, amapiano, alté, afrofusion)
- Trot (Korean traditional, modern revival)
- Bollywood / C-pop / Mando-pop / Arabic / Khaleeji
- Brazilian funk (baile funk)


### §UE-3. K-Pop 14 Subgenres (bitwize 검증)

```
1. Idol Pop                — Girls' Generation, TWICE, IVE, NewJeans
2. K-Hip-Hop / Idol Rap    — Stray Kids, BTS, Big Bang, ATEEZ
3. K-Hip-Hop Independent   — Epik High, Dynamic Duo, Jay Park
4. K-R&B                   — Zion.T, Crush, DEAN, Heize, BIBI
5. K-Ballad                — Taeyeon, Park Hyo-shin, IU, Ailee
6. Dark/Experimental       — Stray Kids, ATEEZ, Dreamcatcher, (G)I-DLE
7. Noise Music/Hyperpop    — NCT 127, Stray Kids, aespa, NMIXX
8. Girl Crush              — BLACKPINK, 2NE1, ITZY, aespa, LE SSERAFIM
9. Cute/Fresh              — early TWICE, Oh My Girl, fromis_9
10. Retro/Disco Revival    — BTS "Dynamite", SHINee "Don't Call Me"
11. K-City Pop             — Newtro 운동
12. K-Rock / Band Idol     — DAY6, CNBLUE, FT Island
13. K-Indie                — Nell, Standing Egg, 10cm, Hyukoh, Jannabi
14. Trot                   — Lim Young-woong, Young Tak
```


### §UE-4. SJY051 genres 20 인덱스

```
SJY 풀바디 흡수 완료 장르:
- Pop / Indie pop / Synth-pop / Bedroom pop
- Hip-hop / Trap / Boom bap / Lo-fi hip-hop
- R&B / Neo-soul / Alt R&B
- Folk / Indie folk / Acoustic
- Rock / Indie rock / Alternative
- Electronic / EDM / House / Techno / Ambient
- Jazz / Smooth jazz / Bebop
- Country / Americana
- Classical / Orchestral
- World / Latin / Afro

각 장르 풀바디 디테일은 SJY references/genres/*.md 또는
21 GENRE_ARTIST_LIBRARY 참조.
```


### §UE-5. 388 Genre Pull-on-Demand (bitwize zip)

```
bitwize/genres/ 디렉토리 구조:
- 388 폴더 × README.md
- 풀바디 우회 어법
- 운영자 발화 시 자동 view
```


# === END 05 USER EXTENSION ZONE v2.0 ===


---

# SOURCE: 21_GENRE_LIBRARY_SEARCH.md

# ============================================================
# 21_GENRE_LIBRARY_SEARCH.md
# YUNY v2.0 FINAL Polish — Genre / Reference Search Library
# 작곡가 어법 X / 검색 우선 / 유명 아티스트만
# Release: 2026-05-26
# ============================================================

## §운영 원칙

```
❌ 안 박는 것:
- "[작곡가] style" 어법 (Teddy Park style 등 자동 박지 마)
- 일반 작곡가 의존 어법 (운영자가 명시한 매우 유명한 케이스만)

✅ 박는 것:
- 마이크로 장르 + 시대 + 시그니처 음향 (음악적 디렉션 first)
- 운영자가 *명시한 매우 유명한 아티스트* (예: Beatles / MJ / Bruno Mars)
- web_search 자동 발동 (특정 곡/아티스트 분석 필요 시)
- 5-Layer 우회 어법 (Producer Name 자리는 *우회 옵션*)
```


## §호출 트리거

```
사용자: "[아티스트] 결로" / "OO곡 결로"
  ↓
시스템 자동:
1. 운영자 명시 매우 유명한 아티스트 (Beatles / MJ 등) → 직접 박음 가능
2. 그 외 → web_search 발동:
   - 공신력 출처 (Wikipedia / Pitchfork / Rolling Stone)
   - 정의 / 시그니처 / 대표곡
3. 결과 → 5축 분해 (13 §3)
4. 5-Layer 우회 변환 (작곡가 자리는 *Layer 1 - 우회 옵션*)
5. Style Box 적용
```


## §5-Layer 우회 어법

```
Layer 1 (옵션): Producer Name (운영자 명시 매우 유명한 케이스만)
Layer 2: Genre + Era (마이크로 장르 + 시대)
Layer 3: Sound Trait (음향 특성)
Layer 4: Vocal Description (보컬 묘사)
Layer 5: Production Style (프로덕션 결)

원칙: Layer 1은 *옵션*. 안 박아도 Layer 2-5만으로 안전.
운영자가 "[유명 아티스트] 결로" 명시 시만 Layer 1 활성화.
```


## §안전 통과 아티스트 케이스

```
✅ Direct Artist Name 안전 통과 (검증된 케이스):
- Mrs. GREEN APPLE, YOASOBI, Tatsuro Yamashita (일본)
- Bruno Mars-style (안전)
- MJ-style, PinkPantheress era, Charli XCX Brat era (-style/-era 접미사)
- Beatles (역사적)
- David Bowie (시대 명시 시)

❌ 위 외 모든 아티스트는 default 우회 어법:
- Layer 2-5 어법으로 변환
- 또는 web_search → 5축 분해 → Style Box
```


## §장르 검색 어법

```
운영자 발화: "[장르] 결로"
  ↓
시스템 자동:
1. 23 풀바디 사전 X (v2.0 FINAL에서 다이어트 삭제됨)
2. web_search "[장르명] genre music characteristics"
3. 공신력 출처:
   - Wikipedia (정의)
   - Pitchfork / Rolling Stone / RYM / AllMusic (분석)
   - HookGenius / SongFacts (현재 트렌드)
4. 결과 → 13 §3 5축 분해:
   Axis 1 Vocal / Axis 2 Harmonic / Axis 3 Acoustic /
   Axis 4 Temporal / Axis 5 Lyric
5. 마이크로 장르 + 시대 + 시그니처 추출
6. Style Box 적용 (Position 1 — 음악적 디렉션 first)

장르 분류 어법 (검색용 카테고리):
- Rock & Metal (alternative / indie / shoegaze / metal 등)
- Electronic & Dance (EDM / house / techno / UK garage 등)
- Hip-Hop & Rap (trap / drill / boom-bap / plugg 등)
- Pop & East Asian Pop (K-pop / J-pop / hyperpop 등)
- R&B / Soul / Funk / Disco
- Jazz & Blues
- Country & Folk
- Classical / Opera / Orchestral
- World / Latin / Afro / Reggae / Caribbean
- 특수 (cinematic / soundtrack / video game music 등)
```


## §Reference Deep Research Pipeline (C-74)

```
운영자 "OO곡 결로" 발화 시 4-Stage 자동:

Stage 1: 내부 자산 점검
  - 13 REFERENCE_ANALYSIS §2.1 Confidence Self-Check
  - BPM/Key/코드/시그니처 확실? → 직접 박음
  - 불확실 → Stage 2

Stage 2: Web Research (불확실 자리만)
  - 공신력 출처 우선
  - 곡 발매 연도 / 프로듀서 / 작곡가 / 장르

Stage 3: 곡 자체 분석 (URL 제공 시)
  - BPM / Key / 구조 / Signature Moments
  - 5-element 보컬 / 악기 인벤토리

Stage 4: Suno 프롬프트 변환
  - 5축 → CREATE/COVER
  - Position 1 자리 마이크로 장르 + 시대
  - Pop Gravity 차단 EXCLUDE
  - 시점 anchor 의무
```


## §Time-Anchored Context (C-73)

```
운영자 "[아티스트] 결로" 발화 시:
"이 아티스트는 시점에 따라 결이 다른데, 어느 시점?

ⓐ 데뷔/초기
ⓑ 전성기/대표작
ⓒ 최근 활동
ⓓ 특정 곡/앨범
ⓔ 특정 멤버 솔로"

자동 추론:
- 곡 제목 명시 → ⓓ
- 멤버 솔로 → ⓔ
- 연도 명시 → 해당 시점
- "최근/요즘/신곡" → ⓒ
- "옛날/데뷔" → ⓐ
```


## §Member-Solo vs Group 분기 (C-76)

```
"BLACKPINK 결로" → 그룹 default
"BLACKPINK Rosé 결로" → 회의 발의 (그룹 ⓐ vs 솔로 ⓑ)
"Rosé 결로" (그룹명 없이) → 솔로 default 추정
"APT" / "rosie" 등 곡 명시 → 솔로 자동
"최근/신곡" → 솔로 활동기 자동

각 분기 시 web_search → 시점별 프로듀서 / 장르 / 사운드 추출
```


## §EXCLUDE Auto-Inject (C-75)

```
참조 곡 결로 작업 시 자동 EXCLUDE:
- Tier 5 시점 anchor: 이전 시기 결 차단
  예: "Rosé 2024-2025" → EXCLUDE: "Teddy Park signature, fierce EDM trap"
- Tier 1 Anti-drift: 모든 COVER 자동
- Tier 3 Pop Gravity Well 차단
```


# === END OF 21 (Slim Edition) ===


---

# SOURCE: 23a_GENRE_INDEX_MASTER.md

# ============================================================
# 23a_GENRE_INDEX_MASTER.md  —  On-Demand 장르 인덱스 (외부 fetch 버전)
# YUNY v2.7  ·  풀바디 본문은 외부(public GitHub)에 위치, 본 인덱스만 프로젝트 상주
# ============================================================
#
# ▶ 조회 절차 (장르 발화 시):
#   1) 아래 표에서 장르명 또는 [slug] 매칭
#   2) 그 줄의 raw URL을 그대로 web_fetch → 그 장르 본문만 로드 (개당 ~4-16K)
#   ※ 각 줄에 전체 raw URL이 박혀 있음(조합 불필요). repo 이름 바꾸면 일괄 치환.
#   ※ 매칭 실패 시 인접 후보 1-2개 fetch 후 판단, 그래도 없으면 web_search → 5축
#   ※ web_fetch가 막히면(드묾) bash로 'curl -s <URL>' 또는 운영자가 URL 직접 투척
#
# 총 277개 장르 / 10개 카테고리.  형식:  표시명 [slug] → 경로
# ============================================================

## Classical / Opera / Orchestral  (23i · 2)  →  classical/
Classical [classical] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/classical/classical.md
Opera [opera] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/classical/opera.md

## Country / Folk / Acoustic  (23h · 13)  →  country-folk/
Americana [americana] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/americana.md
Bakersfield Sound [bakersfield-sound] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/bakersfield-sound.md
Bluegrass [bluegrass] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/bluegrass.md
Bro-Country [bro-country] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/bro-country.md
Celtic [celtic] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/celtic.md
Country [country] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/country.md
Folk [folk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/folk.md
Honky-Tonk [honky-tonk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/honky-tonk.md
Indie Folk [indie-folk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/indie-folk.md
Neotraditional Country [neotraditional-country] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/neotraditional-country.md
Outlaw Country [outlaw-country] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/outlaw-country.md
Singer-Songwriter [singer-songwriter] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/singer-songwriter.md
Western Swing [western-swing] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/western-swing.md

## Electronic & Dance  (23c · 47)  →  electronic-dance/
2-Step Garage [2-step-garage] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/2-step-garage.md
Acid Jazz [acid-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/acid-jazz.md
Ambient [ambient] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/ambient.md
Balearic [balearic] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/balearic.md
Bass House [bass-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/bass-house.md
Bassline [bassline] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/bassline.md
Breakbeat [breakbeat] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/breakbeat.md
Breakcore [breakcore] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/breakcore.md
CHILLWAVE [chillwave] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/chillwave.md
Chiptune [chiptune] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/chiptune.md
Deep House [deep-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/deep-house.md
Drum and Bass [drum-and-bass] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/drum-and-bass.md
Dubstep [dubstep] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/dubstep.md
Electronic Dance Music (EDM) [edm] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/edm.md
Electro [electro] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/electro.md
Electronic [electronic] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/electronic.md
Eurodance [eurodance] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/eurodance.md
Folktronica [folktronica] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/folktronica.md
Footwork [footwork] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/footwork.md
Future Bass [future-bass] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/future-bass.md
Future Funk [future-funk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/future-funk.md
Glitch [glitch] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/glitch.md
Glitch Hop [glitch-hop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/glitch-hop.md
Grime [grime] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/grime.md
Hardstyle [hardstyle] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/hardstyle.md
House [house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/house.md
HYPERPOP [hyperpop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/hyperpop.md
IDM [idm] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/idm.md
Italo Disco [italo-disco] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/italo-disco.md
Jersey Club [jersey-club] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/jersey-club.md
Jungle [jungle] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/jungle.md
Minimal Techno [minimal-techno] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/minimal-techno.md
Moombahton [moombahton] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/moombahton.md
Neurofunk [neurofunk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/neurofunk.md
Nightcore [nightcore] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/nightcore.md
PHONK [phonk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/phonk.md
Progressive House [progressive-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/progressive-house.md
Reggaeton [reggaeton] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/reggaeton.md
Synthwave [synthwave] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/synthwave.md
Tech House [tech-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/tech-house.md
Techno [techno] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/techno.md
Trance [trance] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/trance.md
Trip-Hop [trip-hop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/trip-hop.md
Tropical House [tropical-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/tropical-house.md
UK Garage [uk-garage] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/uk-garage.md
Vaporwave [vaporwave] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/vaporwave.md
Witch House [witch-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/witch-house.md

## Hip-Hop & Rap  (23d · 20)  →  hiphop-rap/
Abstract Hip-Hop [abstract-hip-hop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/abstract-hip-hop.md
Boom Bap [boom-bap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/boom-bap.md
Cloud Rap [cloud-rap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/cloud-rap.md
Country Rap [country-rap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/country-rap.md
Crunk [crunk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/crunk.md
Drill [drill] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/drill.md
East Coast Hip Hop [east-coast-hip-hop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/east-coast-hip-hop.md
Emo Rap [emo-rap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/emo-rap.md
G-Funk [g-funk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/g-funk.md
Gangsta Rap [gangsta-rap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/gangsta-rap.md
Grime [grime] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/grime.md
Hip-Hop [hip-hop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/hip-hop.md
Horrorcore [horrorcore] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/horrorcore.md
Jazz Rap [jazz-rap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/jazz-rap.md
Latin Trap [latin-trap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/latin-trap.md
Mumble Rap [mumble-rap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/mumble-rap.md
PHONK [phonk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/phonk.md
Southern Hip Hop [southern-hip-hop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/southern-hip-hop.md
Trap [trap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/trap.md
Underground Hip Hop [underground-hip-hop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/underground-hip-hop.md

## Jazz & Blues  (23g · 15)  →  jazz-blues/
Acid Jazz [acid-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/acid-jazz.md
Bebop [bebop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/bebop.md
Big Band [big-band] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/big-band.md
Blues [blues] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/blues.md
Bossa Nova [bossa-nova] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/bossa-nova.md
Cool Jazz [cool-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/cool-jazz.md
Delta Blues [delta-blues] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/delta-blues.md
Hard Bop [hard-bop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/hard-bop.md
Jazz [jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/jazz.md
Latin Jazz [latin-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/latin-jazz.md
Modal Jazz [modal-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/modal-jazz.md
Ragtime [ragtime] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/ragtime.md
Smooth Jazz [smooth-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/smooth-jazz.md
Swing / Neo-Swing [swing] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/swing.md
Vocal Jazz [vocal-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/vocal-jazz.md

## Other / Children / Faith / Specialty  (23k · 52)  →  other-specialty/
A Cappella [a-cappella] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/a-cappella.md
Beatboxing [beatboxing] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/beatboxing.md
Blackgaze [blackgaze] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/blackgaze.md
Chopped and Screwed [chopped-and-screwed] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/chopped-and-screwed.md
Cinematic [cinematic] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/cinematic.md
Conscious Hip-Hop [conscious-hip-hop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/conscious-hip-hop.md
Contemporary Christian Music [contemporary-christian] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/contemporary-christian.md
Dark Ambient [dark-ambient] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/dark-ambient.md
Dark Jazz [dark-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/dark-jazz.md
Darksynth [darksynth] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/darksynth.md
Darkwave [darkwave] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/darkwave.md
Deathcore [deathcore] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/deathcore.md
Downtempo [downtempo] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/downtempo.md
Drone [drone] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/drone.md
Drone Metal [drone-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/drone-metal.md
Dungeon Synth [dungeon-synth] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/dungeon-synth.md
EBM [ebm] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/ebm.md
Electroswing [electroswing] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/electroswing.md
Enka [enka] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/enka.md
Ethio-Jazz [ethio-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/ethio-jazz.md
Future House [future-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/future-house.md
Glitch Pop [glitch-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/glitch-pop.md
Gypsy Jazz [gypsy-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/gypsy-jazz.md
Hair Metal [hair-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/hair-metal.md
Jazz Fusion [jazz-fusion] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/jazz-fusion.md
Kayokyoku [kayokyoku] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/kayokyoku.md
Lo-Fi [lo-fi] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/lo-fi.md
Lo-Fi House [lo-fi-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/lo-fi-house.md
Madchester [madchester] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/madchester.md
New Age [new-age] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/new-age.md
Noise Pop [noise-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/noise-pop.md
Nu Jazz [nu-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/nu-jazz.md
PC Music [pc-music] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/pc-music.md
Plugg [plugg] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/plugg.md
Pop Rap [pop-rap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/pop-rap.md
Post-Dubstep [post-dubstep] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/post-dubstep.md
Post-Metal [post-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/post-metal.md
Progressive Metal [progressive-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/progressive-metal.md
Psychedelic Trance [psychedelic-trance] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/psychedelic-trance.md
Riot Grrrl [riot-grrrl] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/riot-grrrl.md
Slowcore [slowcore] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/slowcore.md
Soul Jazz [soul-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/soul-jazz.md
Soundtrack [soundtrack] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/soundtrack.md
Space Disco [space-disco] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/space-disco.md
Spaghetti Western [spaghetti-western] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/spaghetti-western.md
Spoken Word [spoken-word] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/spoken-word.md
Trap Metal [trap-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/trap-metal.md
Trot [trot] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/trot.md
Twee Pop [twee-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/twee-pop.md
Video Game Music [video-game-music] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/video-game-music.md
Visual Kei [visual-kei] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/visual-kei.md
Worship [worship] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/worship.md

## Pop & East Asian Pop  (23e · 17)  →  pop-eastasian/
Anisong [anisong] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/anisong.md
Art Pop [art-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/art-pop.md
Baroque Pop [baroque-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/baroque-pop.md
Britpop [britpop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/britpop.md
Bubblegum Pop [bubblegum-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/bubblegum-pop.md
Cantopop [cantopop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/cantopop.md
Chamber Pop [chamber-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/chamber-pop.md
City Pop [city-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/city-pop.md
Electropop [electropop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/electropop.md
HYPERPOP [hyperpop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/hyperpop.md
J-Pop [j-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/j-pop.md
K-Pop [k-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/k-pop.md
Mandopop [mandopop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/mandopop.md
Pop [pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/pop.md
Sophisti-pop [sophisti-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/sophisti-pop.md
Synth-Pop [synth-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/synth-pop.md
Vocaloid [vocaloid] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/vocaloid.md

## R&B / Soul / Funk / Disco  (23f · 15)  →  rnb-soul-funk/
Alternative R&B [alternative-rnb] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/alternative-rnb.md
Boogie [boogie] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/boogie.md
Disco [disco] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/disco.md
Doo-Wop [doo-wop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/doo-wop.md
Funk [funk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/funk.md
Gospel [gospel] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/gospel.md
Motown [motown] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/motown.md
Neo-Soul [neo-soul] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/neo-soul.md
New Jack Swing [new-jack-swing] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/new-jack-swing.md
Nu Disco [nu-disco] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/nu-disco.md
P-Funk [p-funk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/p-funk.md
Post-Disco [post-disco] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/post-disco.md
Quiet Storm [quiet-storm] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/quiet-storm.md
R&B / Soul [rnb] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/rnb.md
Trap Soul [trap-soul] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/trap-soul.md

## Rock & Metal  (23b · 49)  →  rock-metal/
Alternative Rock [alternative] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/alternative.md
Arena Rock [arena-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/arena-rock.md
Black Metal [black-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/black-metal.md
Death Metal [death-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/death-metal.md
Djent [djent] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/djent.md
Doom Metal [doom-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/doom-metal.md
Dream Pop [dream-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/dream-pop.md
Emo [emo] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/emo.md
Folk Metal [folk-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/folk-metal.md
Garage Rock [garage-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/garage-rock.md
Grindcore [grindcore] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/grindcore.md
Groove Metal [groove-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/groove-metal.md
Grunge [grunge] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/grunge.md
Hardcore Punk [hardcore-punk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/hardcore-punk.md
Indie Folk [indie-folk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/indie-folk.md
Indie Rock [indie-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/indie-rock.md
Industrial [industrial] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/industrial.md
Jam Band [jam-band] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/jam-band.md
Jangle Pop [jangle-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/jangle-pop.md
Krautrock [krautrock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/krautrock.md
Math Rock [math-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/math-rock.md
Melodic Death Metal [melodic-death-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/melodic-death-metal.md
Metal [metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/metal.md
Metalcore [metalcore] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/metalcore.md
Nerdcore [nerdcore] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/nerdcore.md
New Wave [new-wave] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/new-wave.md
Noise Rock [noise-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/noise-rock.md
Nu-Metal [nu-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/nu-metal.md
NWOBHM [nwobhm] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/nwobhm.md
Pop Punk [pop-punk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/pop-punk.md
Post-Punk [post-punk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/post-punk.md
Post-Punk Revival [post-punk-revival] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/post-punk-revival.md
Post-Rock [post-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/post-rock.md
Power Metal [power-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/power-metal.md
Progressive Rock [progressive-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/progressive-rock.md
Psychedelic Rock [psychedelic-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/psychedelic-rock.md
Punk [punk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/punk.md
Rockabilly [rockabilly] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/rockabilly.md
Screamo [screamo] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/screamo.md
Shoegaze [shoegaze] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/shoegaze.md
Ska Punk [ska-punk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/ska-punk.md
Sludge Metal [sludge-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/sludge-metal.md
Space Rock [space-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/space-rock.md
Speed Metal [speed-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/speed-metal.md
Stoner Rock [stoner-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/stoner-rock.md
Surf Rock [surf-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/surf-rock.md
Symphonic Metal [symphonic-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/symphonic-metal.md
Thrash Metal [thrash-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/thrash-metal.md
Viking Metal [viking-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/viking-metal.md

## World / Latin / Afro / Caribbean / Middle Eastern  (23j · 47)  →  world/
Afro-Cuban [afro-cuban] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/afro-cuban.md
Afro House [afro-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/afro-house.md
Afrobeats [afrobeats] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/afrobeats.md
Afropop [afropop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/afropop.md
Afroswing [afroswing] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/afroswing.md
Amapiano [amapiano] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/amapiano.md
Axe [axe] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/axe.md
Bachata [bachata] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/bachata.md
Baile Funk [baile-funk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/baile-funk.md
Banda [banda] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/banda.md
Bhangra [bhangra] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/bhangra.md
Bolero [bolero] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/bolero.md
Bollywood [bollywood] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/bollywood.md
Bongo Flava [bongo-flava] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/bongo-flava.md
Bossa Nova [bossa-nova] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/bossa-nova.md
Calypso [calypso] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/calypso.md
Chanson [chanson] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/chanson.md
Cumbia [cumbia] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/cumbia.md
Dancehall [dancehall] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/dancehall.md
Dub [dub] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/dub.md
Fado [fado] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/fado.md
Flamenco [flamenco] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/flamenco.md
Ghazal [ghazal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/ghazal.md
Highlife [highlife] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/highlife.md
Indian Classical [indian-classical] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/indian-classical.md
Juju [juju] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/juju.md
Klezmer [klezmer] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/klezmer.md
Kuduro [kuduro] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/kuduro.md
Kwaito [kwaito] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/kwaito.md
Latin [latin] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/latin.md
Latin Trap [latin-trap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/latin-trap.md
Lovers Rock [lovers-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/lovers-rock.md
Mambo [mambo] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/mambo.md
Mbalax [mbalax] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/mbalax.md
Merengue [merengue] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/merengue.md
Qawwali [qawwali] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/qawwali.md
Reggae [reggae] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/reggae.md
Reggaeton [reggaeton] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/reggaeton.md
Rocksteady [rocksteady] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/rocksteady.md
Roots Reggae [roots-reggae] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/roots-reggae.md
Samba [samba] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/samba.md
Schlager [schlager] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/schlager.md
Ska [ska] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/ska.md
Soca [soca] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/soca.md
Soukous [soukous] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/soukous.md
Tango [tango] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/tango.md
Tropicalia [tropicalia] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/tropicalia.md

# ── 중복 slug (2개+ 카테고리에 존재 — 조회 시 카테고리로 구분) ──
#   acid-jazz: electronic-dance, jazz-blues
#   bossa-nova: jazz-blues, world
#   grime: electronic-dance, hiphop-rap
#   hyperpop: electronic-dance, pop-eastasian
#   indie-folk: rock-metal, country-folk
#   latin-trap: hiphop-rap, world
#   phonk: electronic-dance, hiphop-rap
#   reggaeton: electronic-dance, world


---

# SOURCE: GENRE_EXTERNALIZE_PATCH.md

# 장르사전 외부화 — 셋업 가이드 (YUNY v2.7)

목표: 풀바디 장르사전(23b–k, ~4MB)을 프로젝트에서 빼 **public GitHub**에 두고,
프로젝트엔 **슬림 인덱스만** 남겨 장르 발화 시 해당 장르 1개만 `web_fetch`.
→ 프로젝트 ~4MB 확보 + 친구한테 줄 때 커넥터 없이 즉시 사전식 조회.

라우팅 3곳은 동봉한 **활성화 버전 시스템 지침**(`00_SYSTEM_INSTRUCTION_for_YUNY.txt`)에 이미 반영됨.
아래는 네가 GitHub에 올리고 프로젝트 파일만 교체하면 끝.

================================================================
## 1. 들어가는/나가는 파일
================================================================
| 위치 | 파일 | 처리 |
|---|---|---|
| 프로젝트 유지 | `23a_GENRE_INDEX_MASTER.md` | **파일명 그대로**, 내용만 새 슬림 인덱스로 덮어쓰기 |
| 프로젝트 제거 | `23b`–`23k` (슬림 구버전) | GitHub로 이전 → 용량 확보 (풀버전이 대체) |
| GitHub(public) | `23_GENRE_FULLBODY/` + `README.md` | 277 장르 + 인트로 10 + 부록 1 |

⚠️ GitHub엔 이번에 올린 **확장 풀버전**을 올림(프로젝트의 슬림 구버전 아님).

================================================================
## 2. GitHub 올리기 — 계정 LimganziAI
================================================================
### A) repo 생성
1. github.com 로그인 → 우상단 `+` → **New repository**
2. Owner `LimganziAI` / Name `yuny-genre-dict` / **Public** / (Add README 체크 해제) → Create

### B) 파일 올리기 — 방법 1: 웹 드래그(설치 X)
1. `23_GENRE_FULLBODY.zip` 압축 풀기 → `23_GENRE_FULLBODY/` 폴더 + 동봉 `README.md` 준비
2. repo 페이지 → **Add file ▸ Upload files** → 폴더와 README 드래그 → **Commit changes**
3. 파일 288개라 한 번에 안 올라가면 카테고리 폴더(rock-metal 등) 단위로 나눠 드래그

### B) 방법 2: git CLI(288개 한 방 — 안정적). repo는 A에서 빈 상태로 만든 뒤:
```
cd <압축 푼 자리>
git init
git remote add origin https://github.com/LimganziAI/yuny-genre-dict.git
git add 23_GENRE_FULLBODY README.md
git commit -m "Add genre full-body dictionary (277 genres)"
git branch -M main
git push -u origin main
```
(GitHub Desktop 앱이면 GUI로 동일 — 폴더 끌어다 commit→push)

### C) 확인: 아무 장르 raw URL 열어보기
`https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/dream-pop.md`
→ 본문 뜨면 성공.

================================================================
## 3. 출처 표기 (CC BY 4.0) — 이미 처리됨
================================================================
동봉 `README.md`에 아래가 들어있음. repo에 그 파일만 올리면 표기 끝(추가 작업 0):

  Based on "Music Composition Agent Skill v1.0" by SJY051 and contributors
  (https://github.com/SJY051/music-composition), licensed under CC BY 4.0.
  Changes made: expanded ~5–6× and restructured into per-genre files with
  Suno-specific prompt keywords. This adapted work is likewise CC BY 4.0.

CC BY 4.0은 상업 포함 개작·재배포를 허용 — 이 한 줄(출처+라이선스+변경표시)만 있으면 완전 합법.

================================================================
## 4. 연동 — 어떻게 작동하나 (커넥터 0)
================================================================
1. 프로젝트엔 `23a_GENRE_INDEX_MASTER.md`(슬림, 각 장르 경로 + BASE_URL) 상주.
2. "[장르] 결로" 발화 → 인덱스에서 장르명/[slug] 매칭 → 전체 URL = BASE_URL + "/" + 경로
3. `web_fetch(URL)` → 그 장르 본문만 로드(~4–16K). 통짜 789K fetch 문제 해소.
4. public raw URL이라 인증·커넥터 불필요. 친구는 "프로젝트 + 인덱스"만 받으면 동일 작동.
5. BASE_URL은 인덱스 맨 위 한 줄(LimganziAI/yuny-genre-dict로 박아둠 — repo명 바꾸면 그 줄만 수정).

================================================================
## 5. 시스템 지침 라우팅 — 반영된 3곳 (참고)
================================================================
- §15 fetch: `장르→05·23a INDEX(슬림,프로젝트)→web_fetch 장르파일(GitHub)`
- D 인덱스: `장르 "[장르] 결로" → 05 / 23a INDEX(슬림) → slug 매칭 → web_fetch(BASE+경로) / 없으면 web_search`
- 로스터: `23a 장르인덱스(슬림; 23b-k 본문=외부 public GitHub)`

================================================================
## 6. 중복 slug 8개 (정상 — 2개 카테고리 교차 등재)
================================================================
indie-folk, acid-jazz, grime, hyperpop, phonk, reggaeton, latin-trap, bossa-nova
→ 카테고리 폴더로 분리돼 충돌 없음. 인덱스에 둘 다 등재.
