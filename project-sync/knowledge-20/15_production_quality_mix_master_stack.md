# CURRENT ADDENDUM — Final-Record Quality Council

## Final-Record Quality Council
For serious COVER, quality is a director, not an adjective. COVER must include compact controls for:
vocal corridor, low-end separation, low-mid carve, high-mid/air control, stereo/depth, dynamics/finish.

Suno can improve clarity and arrangement complexity but may still sanitize vocals, over-layer harmonies, misread era/genre prompts, or ignore detailed effect descriptions. Therefore use positive, perceptual + structural controls and let lyrics/cues carry vocal behavior. Avoid toy texture vocabulary; block actual failed render classes in COVER EXCLUDE.

# 15 — Production Quality / Mix / Master Stack

## CURRENT PATCH — COVER Quality Stack Required

For serious COVER/refine, include a quality stack when relevant:
- vocal corridor: centered lead, clear vowels, controlled consonants, de-essed highs, no buried lead
- low end: tight gentle low end, separated kick/bass, no mud
- low-mid: carved body, no boxy room
- air/highs: smooth high end, no hissy sibilance, no harsh cymbals
- stereo/depth: wide soft room, not mono collapse
- dynamics: polished modern master, not over-compressed
Quality belongs in COVER prompt, not only EXCLUDE.


## CURRENT HOTFIX — COVER Quality Rescue Stack
For serious COVER, especially after bad render feedback, include all six groups in perceptual language. If the user says "음질", this card outranks decorative style tokens.

### Failure-specific controls
- Old/d dated sound: modern high-fidelity finish, no retro kids-TV theme, no old radio rock, no cheap MIDI guitars, no thin karaoke backing, no early-2000s pop-punk default unless requested.
- Mono vocal collapse: lead vocal center-forward and mono-compatible; hook response, gang shouts, and doubles wide L/R; separate lead center from backing stereo field.
- Buried Korean vocal: protect vocal corridor 500Hz-3kHz; keep guitars off-center; do not stack shout layers on top of lead syllables.
- Harsh/fizzy: de-ess 5-8kHz, smooth 2-5kHz bite, controlled 8-14kHz air.
- Mud/boxiness: carve 200-400Hz cloud, centered kick/bass separation, mono low end only below 80Hz.
- Weak shouts: one-bar rest or sudden drop before shout, call-response cue, wide gang response, short dry room, no crowd/stadium wash.
- Weak instrument transform: use substitution map with concrete instrument replacements, not just "harder".

### Prompt placement
When quality is the failure, mention "modern high-fidelity [target genre] transform" near the front, then preserve/substitute, then 6-group quality stack. Do not bury all quality language at the very end if it is the user's main complaint.

## TRIGGER
Every serious COVER (mandatory); harsh/muddy/thin/buried/artificial/unfinished/먹먹/쏘는/보컬 묻힘 feedback; 음질 utterances.

## MUST APPLY
**COVER = the final record. The quality stack is not optional garnish — it is the most frequently MISSED component. Serious COVER without it = defect.**

**The stack (select per genre, keep coverage of all 6 groups):**
- VOCAL (prevents: buried, synthetic, harsh, masked): forward human lead; natural breath texture restored; remove digital artifacts and mechanical edge; warm tube saturation on vocal bus; optional +8 cent detune L15/R15 width; vocal corridor 500Hz-3kHz protected; de-esser 5-8kHz; harmony stack supports, never masks.
- LOW END (prevents: smeared sub, kick/bass blur): mono sub-bass 20-80Hz; kick/bass center separation; sidechain bass to kick ~80ms (dance/EDM); no smeared 100-250Hz body.
- LOW-MIDS (prevents: mud, boxiness): carve 200-400Hz mud; warm body without cloud; pads/ac-gtr/piano off the vocal chest range.
- HIGH-MIDS & AIR (prevents: harshness, brittle fizz): smooth 2-5kHz (kill painful edge); controlled 8-14kHz air, no brittle fizz.
- STEREO & DEPTH (prevents: flat center pileup, uncontrolled reverb): deliberate L/R placement; center reserved for lead vocal+kick+bass+main hook; controlled reverb/delay tails; depth varies by section.
- DYNAMICS & FINISH (prevents: brickwall, lifeless transients, abrupt-feeling end): transient punch preserved; bus glue compression; tape/master saturation 1-2%; loudness by genre — streaming -14 LUFS/-1 dBTP default; club/dance -6~-8 LUFS only on request. Brickwall = defect.

**Era anchor in the first 200 chars** of the COVER prompt locks the production decade.

**Placement law:** Genre-Transform → stack comes AFTER target anchor+maps (card 14 order). Texture-Refine → preserve identity → repair target → stack → section fixes → final/outro.

**Vocal-rescue preset (보컬 묻혀):** corridor protected + carve 200-400Hz on competing layers + de-ess + "lead vocal forward, +1dB above the bed" + center reservation + Audio Influence recheck (too low = re-render buried it) + check EXCLUDE for vocal-killing words.

**Keyword guard (critical nuance):** words like muddy/compressed/vocoder inside EXCLUDE can make Suno avoid vocal processing altogether. Prefer POSITIVE control: explicit Hz distribution + "open dynamics, clear vocal presence". Use specific failure phrases ("smeared low-mid wash") only when that exact failure occurred.

**Frequency-to-language dictionary (failure → prompt phrase):** 200-400Hz pileup → "competing low-mid layers carved, warm body without cloud" · 2-5kHz pain → "smooth high-mid presence, de-essed lead" · 8-14kHz fizz → "controlled air, no brittle sheen" · vocal buried → "lead vocal forward, center protected, vocal corridor 500Hz-3kHz" + "spacious mix, vocal-forward" [커뮤/中] · kick/bass blur → "centered kick/bass separation, mono sub, short sidechain where genre-appropriate".

**Prompt vs Studio split:** prompt solves corridor · arrangement space · controlled reverb/delay · center reservation · section depth. Studio solves fader balance · pan · surgical EQ · stem repair (weak stems: acoustic gtr, piano, strings, BGV [커뮤/中]). Good render + local one-instrument balance issue → Studio first, don't re-prompt. Anti-over-engineering: compress the stack per genre but keep all-6-group coverage — never balloon into a DAW manual, never shrink to "polished, clean mix".

**Studio defaults** (with card 16): crowd cheering / stadium reverb / live audience blocked on every serious build unless live concept.

## FIELD PLACEMENT
Stack+era → COVER PROMPT. Stack never in CREATE. Specific failure blocks → COVER EXCLUDE (guarded wording). LUFS intent → COVER PROMPT tail.

## COMPRESSION PRIORITY
Keep all 6 group HEADERS (+ prevents tags) + corridor + LUFS + keyword guard + Prompt/Studio split; compress within groups to genre-relevant lines. Never compress to "polished, clean mix" — that token-stack is the named anti-pattern.

## FAILURE SIGNALS
- COVER prompt ends at arrangement with zero production language.
- "mono sub, glossy air, no mud" three-token pseudo-stack.
- EXCLUDE stuffed with muddy/compressed → vocal came out raw/unprocessed.
- Loud-genre brickwall sheen on a ballad.
- Re-prompting 3× for a fader-level problem Studio fixes in one move (or the reverse).

## GITHUB FETCH ROUTE
knowledge-evolving/production-engineering/cover_quality_stack_runtime.md (canonical fullbody); production-quality-hacks/ for community/experimental phrases with provenance+confidence tags.

## OUTPUT PHRASES
- "COVER가 곧 최종 음원이라 음질 스택은 6그룹 전부 커버했어 — 마스터는 -14 LUFS/-1 dBTP."
- "보컬 묻힌 건 corridor 미보호 + 200-400Hz 머드야. 레스큐 프리셋으로 다시 입혔어."

---

# PRECISION ADDENDUM — QUALITY STACK COMPRESSION LADDER

Quality stack must be present in serious COVER, but it must not become a DAW manual.

Use one of three stack densities:
- Full serious COVER: 6 short groups covered in 120-180 chars.
- Sketch/refine: 3 lines — vocal corridor, low-end separation, finish/depth.
- Minimal demo: 1 line — vocal-forward controlled finish.

DAW-smell test:
If the phrase sounds like an engineer setting a plugin rather than a listener-heard quality, compress it into perceptual language.
Keep exceptions: vocal corridor and loudness anchor when needed.
## CURRENT ADDENDUM — Technical Quality Preference
User prefers technical prompt language when it improves Suno control. For energetic songs, do not avoid corridor/stereo/frequency/dynamics language. Use it compactly: center-forward lead, vocal corridor protected, low-end separated, high-mid smoothed, controlled air, wide but mono-compatible backing, transient punch preserved.
For intimate songs, use the same stack translated into listener language unless the mix is failing. Quality stack remains mandatory in serious COVER.

---

## 2026-06-14 CURRENT RC PATCH — Final-Record Texture Rescue

Because COVER is the final record, serious COVER must front-load texture and density when quality failed or is high-risk.

High-risk Suno render failures to block:
- toy synth / beep-boop / ringtone lead / cute blip / cheap EDM pluck
- empty intro or thin first 8 bars
- old idol / 90s J-pop / dated radio rock / karaoke backing
- buried Korean lead or mono vocal collapse
- weak drop, no sub impact, smeared low end
- harsh 2-5kHz bite, brittle 8-14kHz fizz

COVER positive texture language must name the role, not just "modern":
- processed vocal texture as hook material
- chopped guitar resample as rhythmic stab
- filtered noise/riser as pressure
- sidechain pressure bed under vocal corridor
- tight hats and dry clap/snare, not cartoon synth lead
- rolling sub with separated kick
- wide backing, center-forward lead

Quality stack must appear in COVER prompt and be echoed by COVER LYRIC cues when the section needs impact.

## 2026-06-14 CURRENT ADDENDUM — Final-Record Quality Council
COVER quality is judged as the released record, not as a style guess.

Quality council checks:
- bar 1 density: empty intro vs intended cold-open/full bed.
- vocal front: Korean lead center-forward, corridor protected, no buried hook.
- low end: kick/sub separated, no smeared low-mid wash.
- texture price: no toy synth, ringtone lead, cheap pluck, old rave/trance default unless wanted.
- stereo/depth: backing wide but lead/kick/bass center stable.
- dynamics: drop impact and transient punch, no weak final drop, no brickwall mush.
If one prompt is overloaded, use a 2-step plan: transform first, then refine/remaster.
