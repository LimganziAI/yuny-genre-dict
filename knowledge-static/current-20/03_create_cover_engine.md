# CURRENT ADDENDUM — Multi-Role Production Council

## Council before final
Before FINAL-CANDIDATE, run a Multi-Role Production Council:
- lyricist: lyric works without cues; no cheap explanatory lines
- topliner: hook-cell, range, contour, peak, syllable grid are modern and singable
- PD/arranger: section jobs, density, motif owner, cue-prompt instrument sync
- vocal director: vocal identity, range, mic posture, doubles, whisper/hold feasibility
- COVER director: final record preserve map + substitution map + Audio Influence triangle
- quality engineer: vocal corridor, low-end separation, anti-toy texture, stereo/depth, finish
- diagnostics director: entrypoint, one-variable A/B, upstream rebuild if repeated

## quality engineer stop rule
If any director finds a hard conflict, do not ship final. Repair the highest layer and rerun the council.

# 03 — CREATE/COVER Engine

## CURRENT PATCH — Current-Concept Rebuild + Prompt Density

- Concept relock means rebuild fields from the current song, not patch old prompts.
- CREATE prompt must be executable: microgenre/scene, BPM-feel, key/tonal color, range anchor, vocal acting, melody contour, hook shape, section arc, 3-4 articulated instruments, motif, energy, mix corridor.
- COVER prompt is the final record: target refine/transform, preserve map, do-not-change map, substitution/refine map, vocal protection, timing/rest protection, section events, quality stack, final/outro.
- Fixed lyrics become source material for timing/cue/prompt design; they are not permission to rush.
- If prompt has remaining budget and lacks code/tempo/range/articulation/quality, it is underbuilt.


## CURRENT HOTFIX — Full-Process Completion Gate
- Full song output is valid only after S10 cross-field audit. A liked lyric is not a pass for CREATE/COVER/EXCLUDE/SLIDERS.
- If the user asks for final while CREATE/COVER are underbuilt, output a staged repair note or rebuild the fields; do not ship a fake final.
- Before 8-field delivery run G4/G5:
  1. CREATE has bone only, no mix/master/finish language.
  2. LYRIC has cue-after-lyric logic and cue-removal survival.
  3. COVER names preserve map, substitution map, vocal identity, section events, quality stack, final/outro preservation.
  4. EXCLUDE holds all negatives and known render failures.
  5. SLIDERS use only Weirdness / Style Influence / Audio Influence.
- When feedback says "가사는 마음에 든다" lock LYRIC unless user explicitly approves text change. Repair prompt/COVER fields only.
- If the build has both genre transform and sound-quality rescue, split internally into transform then refine/remaster. A single overloaded COVER prompt often loses either skin or finish.

## TRIGGER
Every song build. Any utterance touching 뼈대/멜로디 유지/리믹스/장르 변환/음질/커버.

## MUST APPLY
**Workflow mechanism (non-negotiable):** COVER does not generate from air. It takes the audio that CREATE produced and re-renders it through Audio Influence, keeping melody/structure/lyric phrasing and re-skinning sound/arrangement. So the COVER prompt describes how to CHANGE an existing track, never describes a new song.

**CREATE = bone.** Nine mandatory items, all present, every serious build:
1 microgenre+era (+scene) 2 BPM/feel 3 key or tonal color 4 vocal identity 5 elements (card 08) 5 melody contour 6 hook shape 7 section arc with energy 8 core instruments 3-4 with articulation 9 signature motif. A 600-char CREATE = missing items, not efficiency. No production/mix/mastering language in CREATE.

**COVER = final record body.** Two modes — judge from user intent, confirm in 1 line if ambiguous:
- (a) Texture-Refine (same genre): production/mix/texture only; bone untouched. Audio Influence 20-40.
- (b) Genre-Transform: full re-arrangement in the target genre — new instrumentation, groove, rhythm, reharmonization allowed. Audio Influence 45-75. Order per card 14.

**30% rule:** if CREATE and COVER share >30% descriptors, rewrite the weaker side — aiming the same average twice doubles genericness.

**Substitution map** (auto when genre family jumps — Pop/Rock/Electronic/Trad/Hip-hop/R&B/Latin): Drums / Bass / Lead / Vocal treatment / Texture each get a different answer in CREATE vs COVER.

**Vocal identity survives both modes:** "vocal X% [identity] maintained throughout; [new genre] applied to instruments and arrangement only" — unless the user explicitly changes the voice.

**Throughout discipline:** every COVER carries at least one "[signature] maintained throughout, including final chorus and outro."

## FIELD PLACEMENT
Bone items → CREATE PROMPT. Mode/maps/quality → COVER PROMPT. Original-genre markers (mode b) → COVER EXCLUDE. Mode → Audio Influence value in COVER SLIDERS.

## COMPRESSION PRIORITY
CREATE: cut texture adjectives first; never cut items 1, 4, 5, 9. COVER: cut redundant genre restatement; never cut preserve map or quality stack.

## FAILURE SIGNALS
- COVER prompt reads like a fresh song description.
- Audio Influence missing or "—" on COVER.
- CREATE contains "-14 LUFS", "de-esser", "mix" vocabulary.
- Same microgenre words open both prompts in mode b.

## GITHUB FETCH ROUTE
prompt-patterns/create-cover/ for stored pairings; knowledge-evolving/genre-dictionary for the transform target.

## OUTPUT PHRASES
- "COVER는 새 곡 설명이 아니라 'CREATE 결과물을 어떻게 바꿀지'야 — 그래서 preserve map부터 박았어."
- "장르 점프라 모드 (b)로 갔고, 원곡 장르 마커는 EXCLUDE로 차단했어."

**G4 hook + anti-dump:** before the CREATE prompt ships, run the musical-truth audit (cards 11/12): key↔vocal money zone, BPM↔groove↔syllable grid, one peak, instruments = one playable band, motif has an owner instrument and a place. Then the deletion pass — every token must serve one of the 9 bone slots; a token serving none is deleted. Deletion, not addition, is the anti-average move.
## CURRENT ADDENDUM — Technical Prompt Density and Material Mining
When files(27), v5.5 metadata, or prompt banks are available, use them as vocabulary mines before serious CREATE/COVER writing. Extract ratios, BPM/key/chord hints, range anchors, instrument articulation, cover maps, and quality language; do not treat machine matches as canon.
Serious CREATE must look engineered: ratio or microgenre if useful, BPM/feel, key/tonal color, vocal range+acting, melody contour, hook event, 3-4 articulated instruments, motif owner, density curve.
Serious COVER must look like final-record engineering: preserve/substitute/protect/finish. User preference allows technical mix language when useful, especially for high-energy songs.

---

## 2026-06-14 CURRENT RC PATCH — Two-Pass CREATE→COVER Finalization Ladder

The first 8-field package is the **first executable production draft**. It is not the finished master unless the two-pass logic passes.

### PASS 0 — Production Bible
Before fields, freeze: final COVER target, lyric mode, vocal physics, genre/groove, source bone, preserve targets, hard bans, predicted render failures.

### PASS 1 — CREATE source audio
CREATE PROMPT + LYRIC generate the source audio. CREATE is not "low effort" and not "final mix"; it is the bone/source. The LYRIC field is a 5000-char source-performance runway: section timing, lyric delivery, breath/cue map, hook cells, motif handoff, whisper/stop/hold/drop devices when they affect source timing.

### PASS 1.5 — CREATE render review
After CREATE audio exists, or before if internally simulating, evaluate:
- melody age / contour / hook cell
- vocal age, range, posture, belting risk
- groove pocket and BPM×syllable grid
- source texture and instrument role
- empty intro or density failure
- lyric rushing or straight recitation
- cues obeyed or ignored
- what must be preserved into COVER

### PASS 2 — COVER final record
COVER CREATE PROMPT + COVER LYRIC transform the CREATE audio into the final record. COVER LYRIC is a second 5000-char final-record staging script, not a copy obligation. It may reinforce: whisper pickups, one-bar rests, hard stops, drop cells, no-vocal fills, hook emphasis, vocal chops, final held/cut gesture, and density changes.

### PASS 2.5 — COVER render review
Evaluate final audio: expensive texture vs toy synth, vocal corridor, low-end separation, high-mid harshness, weak drop, source-skin bleed, melody loss, lyric timing drift, Audio Influence fit.

### FINAL-CANDIDATE
Only call final after G4 + G5 + cue map + EXCLUDE/slider + measured S10 + render-chain logic pass.
