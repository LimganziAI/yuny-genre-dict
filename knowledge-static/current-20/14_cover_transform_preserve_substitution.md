# CURRENT ADDENDUM — COVER Final Record Preflight

## COVER Final Record Preflight
COVER is the final record from CREATE audio. Before final, answer:
- What from CREATE source is good enough to preserve?
- What source skin must be substituted?
- What must never change: melody, Korean lyric timing, hook shape, final gesture?
- What final-record cues must be in COVER LYRIC?
- Does Audio Influence match preserve/substitution intent?

If source diagnosis says CREATE is broken, go upstream first. If source is usable but final sound failed, repair COVER prompt/COVER LYRIC/quality stack/EXCLUDE/sliders.

# 14 — COVER Transform: Preserve & Substitution Maps

## CURRENT PATCH — Source-Aware COVER Final Record

COVER receives CREATE audio as hidden source. It is not a fresh-song prompt and not a lazy copy.
Order:
1. target refine/transform anchor
2. preserve map: melody, lyric timing, chords/feel, section order, rests, final/outro
3. do-not-change map
4. substitution/refine map: drums, bass, harmonic bed, texture, vocal treatment, bridge/final event
5. vocal identity/range/acting protection
6. timing/rest protection
7. quality stack
8. final/outro preservation

Discarded meeting ideas do not enter COVER unless they are actual source-skin leak risks.


## CURRENT HOTFIX — Transform/Refine Split and Source-Skin Control
When COVER feedback includes 음질, 옛날 느낌, 보컬 모노, 보컬 묻힘, 샤우트 약함, 악기 약함:
1. Confirm whether lyric is approved. If yes, lock LYRIC/COVER LYRIC text.
2. Decide mode:
   - Transform COVER: change genre skin while preserving melody/topline/lyric timing.
   - Refine/Remaster COVER: keep current genre skin and repair vocal, stereo, finish.
   - 2-step strategy: transform first, then remaster/refine if one prompt is overloaded.
3. Preserve map must name what survives: melody/topline, Korean lyric timing, hook chant shape, vocal identity, section order, final/outro gesture.
4. Substitution map must name what changes: drum source, bass source, guitars/synths, shout layers, instrumental break, bridge/final events.
5. If old source skin follows the audio, lower Audio Influence by one A/B step rather than adding more adjectives.
   - Strong preserve: 65-75
   - Balanced transform: 55-64
   - Skin replacement: 45-54
6. COVER prompt must not read like a new song. It must read like "preserve X; substitute Y; repair Z."

## TRIGGER
Genre-Transform COVER (장르 바꿔/리믹스/다른 느낌으로/멜로디는 살려); COVER mode ambiguity; transform feedback.

## MUST APPLY
**Genre-Transform COVER order (fixed sequence inside the COVER prompt):**
1 target microgenre anchor (specific, era'd — card 09 rules apply to the TARGET)
2 **preserve map** 3 **substitution map** 4 vocal identity preservation 5 section/energy events 6 full production quality stack (card 15) 7 final/outro preservation.

**Preserve map — name what survives, explicitly:**
"melody and topline preserved · lyric phrasing and timing preserved · lead vocal identity [5-element shorthand] preserved · hook melodic shape preserved · section structure preserved". Unstated = unprotected. Melody-keep requests pin Audio Influence 60-75.

**Substitution map — every rhythm-section role gets a target-genre answer:**
Drums → [target kit/groove] · Bass → [target bass] · Lead/harmonic bed → [target] · Texture → [target] · Vocal TREATMENT (fx/space only, identity untouched) → [target]. Unmapped roles drift back to the source genre.

**Source-genre lockout:** original genre's marker words go to COVER EXCLUDE ("no city-pop chorus guitar, no 80s gated snare" → as EXCLUDE entries: "city-pop clean chorus guitar, 80s gated snare"). Without lockout, Audio Influence drags the old skin through.

**Audio Influence by intent:** preserve lead/topline 60-75 (멜로디 살려 = 65 default) · balanced transform 45-55 · loose texture re-skin 20-40. Melody wobbles after render → raise to 65-70; texture too timid → lower toward 35.

**Section/energy events keep the record alive:** at least 2 ("drums cut to half-time at bridge", "strip to vocal+keys for final pre-chorus", "drop hits 8 bars after chorus 2").

**Final/outro preservation:** Final Chorus + Outro inherit Verse-1-grade cue density; "signature maintained through final chorus and outro, never released."

**Order audit (8-check before output — order violation = transform-failure risk):** ① target anchor ② preserve map ③ substitution map ④ vocal identity ⑤ section/energy events ⑥ quality stack ⑦ final/outro preservation ⑧ Audio Influence synced to intent.

**Cover vs Remaster routing:** identity is right and only the sound needs strength → refine/remaster path (mode a), NOT a transform COVER; the direction itself changes → transform cover (mode b). Unstable long-form / long-intro sources: work section-first and treat structure simplification as behavior, not defect [커뮤/中] — full fallback ladder (Start At → strongest section → Extend → Replace Section → Get Whole Song) lives in GitHub suno_native_render_control.md.


## FIELD PLACEMENT
All of the above → COVER PROMPT in the fixed order. Lockout words → COVER EXCLUDE. AI value → COVER SLIDERS. Delivery deltas (if transform changes feel) → COVER LYRIC cue tweaks only.

## COMPRESSION PRIORITY
Keep: order audit 8-check, both maps, lockout, AI table, source gate. Drop first: event examples.

## FAILURE SIGNALS
- "Genre changed but melody gone" = preserve map absent or AI < 55.
- New genre sounds half-old = no source lockout.
- Transform reads like a fresh-song description (card 03 violation).
- Quality stack placed BEFORE the target anchor (weakens genre identity).

## GITHUB FETCH ROUTE
genre-dictionary fullbody for the TARGET genre (mandatory before writing the substitution map); prompt-patterns/create-cover/ for proven transform pairs; production-engineering/suno_native_render_control.md (render-control hypotheses [가설] + fallback ladder).

## OUTPUT PHRASES
- "preserve map에 멜로디·프레이징·보컬 정체성 명시 + Audio Influence 65 — '장르는 바꾸되 멜로디는 살려'의 정석 세팅이야."
- "원곡 장르 마커를 EXCLUDE로 잠가야 새 스킨이 안 밀려."

---

# PRECISION ADDENDUM — G5 TRANSFORM TRUTH

COVER passes only when preserve map, substitution map, and Audio Influence form a complete non-contradictory triangle.

Silence means surrender to genre average. Every important element must be either preserved or substituted.

Audio Influence intent table:
- 60-75: melody/topline/lead identity preservation, default 65
- 45-60: balanced transformation
- 20-40: loose texture refit or DNA-only reuse

Fresh-song detector:
If the COVER prompt restates key, BPM, section list, or melody contour as if starting from zero, rewrite it into transform language: preserve / substitute / treat / protect / maintain.

Vocal load default:
For energetic transforms, instruments carry aggression. Vocal identity stays clean unless the user explicitly asks for a changed vocal posture.

**Audio Influence decision table:** note-for-note melody survival 60-75 (default 65) · feel preserved but reframe allowed 45-60 · DNA only 25-40. The user's words decide ("멜로디 유지" = 65); on drift, move ±10 as a single-variable A/B — never with other edits.

**Vocal-load default (anti-strain):** energy raises ride the INSTRUMENTS by default — "vocal identity preserved; drive on drums/guitars only, relaxed chest, unforced final peak" + EXCLUDE: cracked strained vocal, raspy split, shouty belt. Vocal push happens only when the user explicitly asks for it.
## CURRENT ADDENDUM — Ratio Transform and Technical Cover Language
For COVER transforms, ratios may define the new skin, but preserve/substitution maps still decide success. Use ratios to set dominance, then name drums, bass, lead/harmonic bed, texture, vocal treatment, section events, and quality stack.
Technical mix language is allowed when the render goal is high-energy, dense, or quality-sensitive. If intimate, use perceptual quality words unless failure requires frequency/stereo control.

---

## 2026-06-14 CURRENT RC PATCH — COVER From Reviewed CREATE Source

COVER prompt is written after asking: "What did the CREATE audio actually become, and what must the final record do to it?"

Add this pre-map before writing COVER:
1. source strengths: melody hook, lyric timing, vocal color, section order, motif
2. source failures: oldness, toy texture, empty intro, weak drop, buried vocal, source-skin drag
3. final target: genre/era/texture and listener impact
4. preserve targets: melody/topline, hook phrasing, vocal identity, rests, final gesture
5. substitution targets: drums, bass, guitar/synth texture, harmonic bed, vocal treatment, section events
6. quality rescue: vocal corridor, low end, low-mids, high-mids/air, stereo/depth, dynamics
7. Audio Influence intent

COVER LYRIC must then restage the same map using cues and line placement. If the COVER prompt says "preserve hard stops" but the COVER LYRIC has no hard stops, G5 fails.

## 2026-06-14 CURRENT ADDENDUM — COVER Final Record Preflight
Before COVER fields ship, run final-record preflight:
1. What CREATE source traits will probably survive?
2. Which traits must be preserved: melody, hook timing, vocal identity, section order, final gesture.
3. Which traits must be substituted: drum source, bass source, harmonic bed, texture, vocal treatment, density, bridge/final event.
4. Which source traits must be blocked because they rendered badly?
5. Does COVER LYRIC actively re-stage the final record, or just copy CREATE LYRIC?
6. Does Audio Influence match preserve vs replacement?
7. Does the quality stack address the final listener result?
If any answer is vague, the COVER is a first draft, not FINAL-CANDIDATE.
