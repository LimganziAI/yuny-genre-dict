# CURRENT ADDENDUM — Toy Texture Risk Gate

Toy Texture Risk Gate:
Avoid vague modern-light words as primary COVER texture: airy pluck, bright synth, synth blip, cute pluck, beep lead, ringtone lead, cartoon blip, cheap trance stab.
Use role-based materials instead: processed vocal texture, chopped guitar-resample, filtered noise/riser, pressure pad, dry clap/snare, tight hats, rolling sub, distorted low-mid stab.
Every texture must have role + register + density. If a lyric cue calls a texture, the prompt must contain its source material.

# 13 — Instrument Articulation & Voicing

## CURRENT PATCH — Instrument Articulation Density

Generic "piano, guitar, drums, bass" is not enough for serious Suno prompts.
Specify 3-4 instruments with:
- instrument type and register
- articulation: brushed, palm-muted, picked, rim taps, broken eighths, arpeggio answers
- role: motif, backbeat, pulse, answer, shimmer, low-end support
- density/space: tucked, low in mix, close-mic, wide, sparse
Cut novelty instruments if they turn lyric objects into toy-like decoration.


## TRIGGER
Choosing/naming any instrument; 악기 추천/소리가 얇아/꽉 차게/리얼하게 utterances.

## MUST APPLY
**Descriptor duty — bare instrument names BANNED.** Every instrument ships with grain+era+playing style:

| Family | Bare ❌ | Shipped ✅ |
|---|---|---|
| Keys | Rhodes / piano | dusty tape-saturated Rhodes; felt-muted upright piano; bright DX7 EP |
| Guitar | guitar | palm-muted tele chugs; chorused clean strat; nylon bossa fingerpicking |
| Bass | bass | round fingered P-bass; gliding 808 sub; upright walking bass |
| Drums | drums | brushed jazz kit; punchy gated 80s snare; crisp trap hats with sparse rolls |
| Strings | strings | tight staccato string stabs; warm legato cello line; soaring octave violins |
| Brass | horns | hard punchy brass stabs; mellow muted trumpet |
| Synth | synth | warm analog Juno pad; quirky resonant synth stab; icy supersaw layer |

**Articulation = the verb of the arrangement:** palm-muted, fingerpicked, brushed, staccato stabs, legato swells, glissando, pizzicato, tremolo, side-stick, ghost-note 16ths — these words change what Suno plays, not just timbre.

**CREATE carries 3-4 core instruments only** (bone identity); additional color/texture layers belong in COVER. Each core instrument earns its slot by owning a role: low anchor / groove engine / harmonic bed / signature voice.

**Zone assignment (collision pre-check):** Sub 20-60 / Bass 60-250 / Low-mid 250-500 / Mid 500-2k (VOCAL CORRIDOR) / Upper-mid 2k-4k / Presence 4k-8k / Air 8k-20k. 3+ instruments in one zone → add separation cue ("frequency separation between [a] and [b]", register split, or drop one). Nothing parks in the vocal corridor at chorus.

**Effect language:** prompt fields use natural speech ("chorused Rhodes", "spring-reverb guitar"); LYRIC uses brackets ([Chorus effect on guitar]) — and watch the Chorus-effect vs [Chorus]-section collision: name the instrument in the bracket.

**Onomatopoeia ban:** (Bam!) style noise-words never; use [Hard punchy brass stab].

## FIELD PLACEMENT
Core 3-4 with descriptors → CREATE slots 3-4. Texture/color layers + zone fixes → COVER. Section entrances/exits ("piano enters bar 5", "band drops out") → [Singing:] backing cues in LYRIC.

## COMPRESSION PRIORITY
Keep: descriptor duty, 3-4 core rule, corridor protection. Drop first: table rows (regenerate by pattern).

## FAILURE SIGNALS
- "piano, guitar, bass, drums" naked list in a prompt.
- Pad + rhythm guitar + keys all camped at 250-500Hz (mud).
- 7 instruments in CREATE, none with a role.

## GITHUB FETCH ROUTE
archive/fullbody-legacy/18_instrument_articulation.md for the full per-instrument technique library.

## OUTPUT PHRASES
- "악기는 단독 호명 금지야 — 'Rhodes'가 아니라 'dusty tape-saturated Rhodes'로 박아야 결이 잡혀."
- "패드랑 키가 같은 대역에 겹쳐서 머드가 떴어. 레지스터를 갈라놨어."
## CURRENT ADDENDUM — Prompt Bank Instrument Mining
From metadata/prompt banks, keep verbs and roles, not instrument lists. Reusable forms: close bright upright piano with two-note motif, brushed kit with rim taps, round palm-muted picked bass, muted guitar offbeats, Telecaster 16th funk scratches, slap-pop bass ghost notes.
Every mined instrument phrase must be assigned a role: low anchor, groove engine, harmonic bed, signature voice, answer motif, or texture layer. CREATE gets only core 3-4; COVER adds color and quality.

## 2026-06-14 CURRENT ADDENDUM — Toy Texture Risk Gate
For modern club/idol/festival covers, avoid words that can render as toy sounds unless intentionally desired:
- risky: beep, blip, cute pluck, bright synth, airy pluck, ringtone, chiptune, cheap EDM lead, cartoon stab.
- safer source descriptions: processed vocal texture, chopped guitar resample, filtered noise sweep, pressure pad, tight offbeat hat, dry clap/snare, rolling sub, low-mid stab, metallic percussion tick, short formant chop.
Every texture must have a role and register. If it sits in the vocal corridor or sounds childish, replace it before final.
