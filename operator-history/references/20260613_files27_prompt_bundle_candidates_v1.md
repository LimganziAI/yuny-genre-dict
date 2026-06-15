# files(27) Prompt Bundle Candidates V1

Date: 2026-06-13
Source: Claude `files(27)` linkage workbook / CSV package
Status: candidate prompt vocabulary mined from metadata. Not final Suno fields.

## Why this is useful
The machine linkage data contains many usable Suno prompt patterns. The best value is not automatic final matching; it is reusable prompt language:
- vocal range anchors
- natural-language acting lines
- instrument articulation
- mix/quality stack phrases
- cover preserve/refine language
- conflict cases where prompts were too weak or mis-scoped

## Use rules
- Treat these as vocabulary banks.
- Do not paste raw prompt bundles blindly.
- Current concept wins over old metadata.
- If a phrase came from a failed render, keep only the lesson, not the exact failed prompt.
- EXCLUDE should use actual failure classes only.

---

## 1. Vocal range anchors that appear useful
Use when locking voice more precisely:
- female bright sharp dry soprano-to-high-mezzo
- female light dry upper-mezzo/soprano
- female mezzo A3-E5 clear but husky
- female alto C4-F5 when the song needs lower weight, but pair with melody firewall
- male mid-high scratchy tenor for Kashas-like rock/funk
- male laid-back mid-low/mid-high tenor for Kreather/Crader-like relaxed groove

Required pair phrase when changing vocal color only:
- preserve topline contour, hook lift, phrase lengths, chorus shape, pitch center, lyric timing; change vocal color only

## 2. Natural-language acting phrases worth keeping
- sings as if keeping the room quiet
- tossed aside, still pitched
- low-effort but centered
- cool deadpan, not emotionally inflated
- smiles without brightening the tone
- holds back the line instead of pushing it
- crisp rapid diction without mumbling
- raspy break only on chorus peak, not throughout
- playful but mature
- clear Korean vowels with controlled consonants
- breath only at phrase tails

## 3. Instrument articulation phrases worth keeping
Piano:
- close bright upright piano, small repeating two-note motif, light broken eighths, soft pedal
- flowing legato piano arpeggio on verses, hammered block chords on chorus downbeats
- felt hammer soft attack, sustained chords, sparse single-note answers

Drums:
- light brushed indie-pop drums, soft kick, restrained snare brush, gentle rim taps
- punchy live-pop drums with ghost notes
- explosive snare on 2 and 4, parallel-compressed only if energetic song
- tucked soft four-on-floor pulse under brushed drums when refining, not transforming

Bass:
- round palm-muted picked bass, short warm notes, gentle eighth-note lift
- Flea-style slap bass, syncopated thumb-pop technique for funk-rock only
- offbeat octave synth bass for TechPara/ParaPara branches only

Guitar:
- clean muted electric guitar offbeats and high-register arpeggio answers
- Telecaster 16th-note funk scratches with wah-wah pedal
- crunchy power-chord stabs locked to kick accents

Brass / strings / texture:
- sharp brass stabs, trumpet/sax/trombone fanfare only when big-band/funk branch needs it
- pizzicato strings, glockenspiel, toy piano are character/scene-specific and should not become default cute instrumentation

## 4. COVER preserve/refine language
Useful COVER skeleton:
- Preserve the melody map, lyric timing, section order, quoted rests, final/outro gesture, and vocal identity.
- Keep the topline fully melodic; do not reinterpret timing.
- Refine as the same song, not a new genre, unless user explicitly asks for transform.
- Center the lead vocal; protect clear Korean vowels and controlled consonants.
- Preserve final line/outro image; do not add ad-libs over the ending.

For quality/refine covers:
- centered vocal, clear Korean vowels, controlled sibilance, de-essed phrase-tail breath
- smooth high end, tight gentle low end, warm close-mic presence
- wide soft stereo ambience, polished modern indie-pop master
- no mono collapse, no old karaoke mix, no buried vocal

For transform covers:
- target anchor first, then preserve map, then substitution map
- specify what changes: drums, bass, texture, vocal treatment, section events
- specify what does not change: melody, lyric timing, structure, final gesture

## 5. EXCLUDE actual-failure classes
Good EXCLUDE families:
- vocal delivery drift: talk-singing, flat narration, rushed vocal, whisper-only vocal
- diction defects: blurred Korean consonants, nasal pronunciation, slurred endings
- vocal mix defects: buried lead, excessive breath noise, harsh sibilance, robotic autotune
- wrong vocal identity: male vocal only when gender drift is plausible or observed; baby voice when mature/feminine route is intended; glossy sweet soprano when dry edge is required
- mix defects: muddy low end, harsh cymbals, mono mix, over-compressed master, old karaoke mix
- lyric defects: lyric truncation, changed lyric timing, changed melody when cover should preserve

Bad EXCLUDE families:
- abandoned brainstorm genre with no render drift
- obvious absence with no risk
- huge negative spam that repeats the prompt vocabulary in reverse

## 6. Useful branch bundles

### Rainy K-indie / literary room song
Good for songs like `히비스커스`:
- rainy Korean indie pop, dry close upright piano, brushed kit, muted guitar, round picked bass
- female dry high-mezzo/soprano or upper-mezzo, close-mic, low-effort, clear diction
- rests after quoted lines
- final/outro image preserved
- quality cover should refine vocal and mix, not change genre

### TechPara / ParaPara branch
Good for recent Japanese dance cluster, not for abandoned concepts:
- Y2K TechPara / ParaPara, Velfarre hyper-techno, 150 BPM locked
- vocals half-time relaxed over double-time sixteenth rave drive
- JP-8000 supersaw, hoover stabs, offbeat octave bass, gated claps, rave risers
- preserve melody and Japanese lyric timing
- use only when final target actually is TechPara/ParaPara

### Breakbeat / hard J-rock action branch
Good for Bongnam / kinetic characters:
- fast high-energy breakbeat rock-pop, punchy kick/snare, tom fills, crash attacks
- distorted rhythm guitars, octave doubles, turntable scratches only as ear-candy
- raspy chorus peak, clear lead vocal on top
- protect transient punch and stereo width

### Funk / soul small-luck duet branch
Good for Luke x Kreather-type songs:
- 1970s funk/soul/R&B/rock-and-roll, 114 BPM, mixolydian funk vamp
- slap-pop bass, muted wah-wah guitar, Telecaster jangle, horn stabs, tambourine vamp
- male laid-back funk tenor verses, feminine bright soprano chorus lift
- call-response duet, stacked hook, groove clarity

### Latin / Martina branch
- Latin funk, flamenco rumba, samba rhythm, acid jazz
- nylon guitar strums, congas/bongos/timbales, wood bass, brass stabs
- mature mid-low husky female vocal, sexy/smooth, controlled vibrato, powerful chorus only when needed

### Cute chaos / Chenny branch
- digital hardcore, happy hardcore, pop-punk, gabber/bubblegum bass
- extreme high thin rapid-fire female vocal, cheeky aggressive cute, shouted/doubled hooks
- never apply accidentally to Luke/Rebecca/Tatoo unless intended

## 7. Integration plan
1. Keep this as a reference vocabulary bank.
2. Use it before writing CREATE/COVER prompts.
3. For official character cards, promote only after user confirmation or repeated strong evidence.
4. During song work, create a current-lock table before fields:
   - fixed
   - changed
   - discarded
   - do-not-touch
   - observed failures
5. Then write 8 fields only after S10.
