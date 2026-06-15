# 13. REFERENCE ANALYSIS — Reference-First Workflow Protocol
# Version: 2.0 (Specific Moment Capture + Web Search Integration)
# Loads on: Reference input trigger (track URL, artist mention, song title,
#           audio description, playlist, lyric sample, listening context).
# Authority: This file defines the entry-point protocol for Reference-First mode.
# Replaces: v1.1

---

## SECTION 0. PURPOSE

This file translates a reference signal into a **locked song blueprint with
specific reproducible moments** in a single analytical pass.

**Outputs of one Reference-First response:**
1. Confidence self-check (memory vs web search needed)
2. Reference digging output (3-5 signature moments captured in natural language)
3. 5-axis decomposition reframed as craft variables
4. 9th craft variable: Signature Moment Vocabulary (NEW in v2.0)
5. 1-shot prompt proposal that uses natural-language direction
   (not just comma-separated descriptors) — see `15_NATURAL_LANGUAGE_DIRECTION.md`
6. A single confirmation question

**The core problem v2.0 fixes:**
v1.x decomposed references into generic category labels (BPM zone, voice type,
era cue) that produced **average-of-genre** outputs. v2.0 captures the
**specific moments** that make a reference distinct from its genre baseline,
then translates those moments into Suno-readable natural language directions.

This file runs BEFORE any Phase 0 deliberation. Phase 0 is opt-in only.

---

## SECTION 1. WHEN TO LOAD THIS FILE

**Triggers (any of):**
- Operator provides a track URL, song title, or artist name as a sound reference
- Operator says "○○ 같은 느낌", "○○ 스타일로", "이런 분위기" with a named anchor
- Operator pastes lyrics, screenshots, or a description of an existing track
- Operator describes a sound concretely enough to map to known references
- Operator shares a public playlist link or "Replay/Wrapped" summary
- Operator says "이 플레이리스트 분위기로" / "내가 요즘 듣는 느낌으로"

**NOT triggers (route elsewhere):**
- Pure mood/scene without sound anchor → 01 Phase 0 (build-up mode)
- Specific harmonic/rhythmic question → 02-04
- Ready-to-output prompt request → 09 + 12

---

## SECTION 2. THE REFERENCE DIGGING PROTOCOL (NEW IN v2.0)

This is the most important section of the file. Skipping this section produces
the "average indie folk" failure mode.

### 2.1 Confidence Self-Check (mandatory first step)

The moment a reference arrives, the system asks itself three questions:

1. Can I name the BPM, key, and form of this track within 5 seconds with
   high confidence?
2. Can I describe 3+ specific signature moments of this track (not generic
   genre features)? Examples of specific moments:
   - "Verse 2 마지막 라인에서 갑자기 head voice flip"
   - "Chorus 진입 직전 0.3초 silence"
   - "Bridge에서 코드가 반음 점프"
   - "Outro에서 vocal layer가 3개로 누적"
3. Do I know the release year, producer, and scene context?

**All 3 YES → proceed with memory-based analysis.**
**Any 1 NO or uncertain → trigger web search (Section 2.2).**

The system does not bluff. If it cannot name 3 specific moments, it admits
this and searches. Bluffed analysis is the #1 cause of generic output.

### 2.2 Web Search Trigger

When confidence check fails, fire batch web searches:

```
- "[song title]" "[artist]" BPM key chord progression
- "[song title]" production analysis OR breakdown OR review
- "[artist]" signature vocal style OR techniques OR phrasing
- "[song title]" lyrics meaning OR interpretation       (if lyric ref)
- "[artist]" producer OR engineer OR studio              (for Decomposed Signature)
```

What to extract from results:
- **BPM and key as confirmed single values** (not range guesses)
- **Specific chord progressions** for verse / pre-chorus / chorus / bridge
- **Vocal performance signatures**: where falsetto enters, where belting
  appears, where the singer drops to whisper, where vibrato is used
- **Producer/engineer signatures** translated into Decomposed Signature
  vocabulary (no direct names in final prompt — see `09_SUNO_ENGINE.md` § 5)
- **Lyric craft patterns**: imagery type, narrator stance, codeswitching
  position, ending particle system (Korean), meter (English)
- **Section-by-section dynamics**: which section is sparsest, which is
  densest, where the energy drop happens

If web search also fails to confirm, the system tells the operator
honestly: "I don't have reliable info on this track. Can you give me one
more anchor (similar artist, year, scene) or a 1-line sonic description?"

The system never invents details to fill gaps.

### 2.3 Specific Moment Capture (the heart of v2.0)

Before 5-axis decomposition, capture **3-5 signature moments** of the track
in natural language. Each moment must include:
- Approximate timestamp or section position
- What changes (vocal register, harmony, rhythm, density, processing)
- How it feels (the perceptual effect)

**Good moment capture example:**

> Reference: Phoebe Bridgers — "Motion Sickness"
>
> Moment 1 (0:48, end of verse 1): Vocal stays conversational mezzo through
> the verse, then on "I have emotional motion sickness" the line lifts
> slightly while the texture stays absolutely flat — no vibrato, no lift in
> dynamic. The flatness IS the emotional weight.
>
> Moment 2 (1:15, chorus entry): Drums enter with a soft kick + brushed
> snare pattern but no crash, no cymbal swell. The "lift" comes from a
> second guitar layer panning right + stacked vocal harmony at +3rd, not
> from a typical pop production climb.
>
> Moment 3 (2:30, bridge): Density drops to acoustic + voice + sparse
> string pad. The chord progression breaks from the verse pattern with a
> chromatic descent in the bass.
>
> Moment 4 (3:20, final chorus + outro): Vocal layers stack to triple-
> tracked + harmony, but the lead vocal stays dry close-mic — the layers
> are around her, not on top of her. Outro fades on the same hook
> repeating, with each repeat thinning out.

**Bad moment capture (avoid):**

> "Sad indie folk feel. Vulnerable vocal. Acoustic-driven."

This is a genre label, not moments. Genre labels produce genre averages.

### 2.4 Lyric Specificity Extraction (when lyrics are referenced)

If the reference includes lyrics or the operator wants the lyric craft to
be referenced (not just the sound), extract:

- **Narrator position**: 1st / 2nd / 3rd person, addressing whom
- **Ending particle system** (Korean):
  소녀체 (~の, ~かな, ~ちゃった) /
  중성·모던 (~じゃない, ~んだろ, ~でしょ) /
  서술 (~た, ~である) /
  Korean: ~잖아 / ~더라 / ~지 / ~구먼 grouping
- **Sensory dominance**: which sense (sight / sound / touch / temperature /
  organic) dominates? Phoebe Bridgers leans organic + visual; Mitski leans
  organic + violent kinesthetic; Frank Ocean leans tactile + temperature.
- **Cliché avoidance index**: how often does the lyric use direct emotion
  words (love, lonely, sad)? Most great references avoid these almost
  entirely.
- **Tense pattern**: present narrative / past recall / future hypothetical
- **Code-switching position**: line-level (K-pop standard) vs
  phrase-level (HANA, modern global crossover)
- **Image moments**: which 1-2 lines stop time? (Phoebe Bridgers technique)

The system does not reuse the lyric content. It extracts the **method** and
applies the method to new content.

---

## SECTION 3. THE 5-AXIS DECOMPOSITION (REFRAMED)

The 5 axes from v1.x are preserved, but each axis now must produce
**reproducible craft variables** rather than abstract adjectives.

### Axis 1: Vocal Engineering
- Gender / weight class
- Timbre (2-3 specific adjectives)
- Phrasing tendency (legato / staccato / breathy / behind-the-beat / pushed)
- **Range center with specific notes** (not "high female" — use "C4-F5
  with chest dominance, head flip above E5")
- **Register transition map**: where the voice changes register across the
  song (verse stays chest, chorus mixes, bridge falsettos)
- Processing signature (dry / plate / hall / tape doubling / formant shift)

### Axis 2: Harmonic & Melodic Design
- Key with modal color
- **Chord palette per section** (verse uses X, chorus uses Y, bridge uses Z)
- Cadence behavior (functional / suspended / static-loop / chromatic mediant)
- Melody shape (stepwise / leap-driven / motivic)
- **Non-diatonic moments**: borrowed chords, chromatic mediants, modal
  interchange — where they happen and why

### Axis 3: Acoustic Architecture
- BPM as a single value
- Frequency band ownership (sub presence / vocal corridor / air shelf)
- Stereo image (narrow-mono / wide pads / panned percussion)
- Dynamic profile (compressed-loud / dynamic / breathing / minimal)
- Era cue (specific decade + region + scene, not just decade)
- **Production signature in 2-3 sentences of natural language**, not
  comma-separated tags

### Axis 4: Temporal Dynamics
- Form with bar counts per section
- Build strategy (linear / call-response / drop-driven / quiet-build)
- Section length tendency
- Energy curve (front-loaded / back-loaded / flat / wave)
- **Where the highest energy moment is and how it's achieved** (more
  layers? key change? vocal lift? texture shift?)

### Axis 5: Lyric Strategy
- Language(s)
- Imagery type (concrete sensory / abstract / narrative / fragmented)
- Narrator stance
- Hook construction (repeated phrase / refrain shift / instrumental hook)
- **Cliché posture**: does this reference avoid or embrace genre clichés?

---

## SECTION 4. CRAFT VARIABLES TRANSLATION

This section was the heart of v1.x. It is preserved and extended with
the 9th variable.

### 4.1 The 9 Craft Variables (mandatory extraction)

| # | Variable | Format | Where it goes in Suno |
|---|---|---|---|
| 1 | Tempo zone | BPM single value | Style Box front |
| 2 | Groove type | 4-on-floor / shuffle / half-time / trap / breakbeat | Style Box `[BPM] [groove]` |
| 3 | Harmonic density | triadic / 7th-loaded / extended / chromatic | Style Box or natural language |
| 4 | Form | VCVCBC / through / multi-section / loop | 12 §1 template + Lyrics tags |
| 5 | Vocal range + phrasing | F3-Eb5 mezzo, behind-beat, breathy | 06 5-element directive |
| 6 | Arrangement density | sparse / mid / dense / wall-of-sound | Style Box instrumentation |
| 7 | Instrumentation core | 3-5 essential instruments | Style Box mid section |
| 8 | Era + production cue | "late-2010s East Coast bedroom indie" | Style Box era anchor |
| 9 | **Signature Moments** ⭐ NEW | 3-5 natural-language moments | Style Box natural-language layer + Lyrics Box [Singing:] cues + microcues |

### 4.2 The 9th Variable in Detail: Signature Moments

This is the variable that breaks the "generic genre output" failure mode.

A signature moment is a **specific, time-located, reproducible** event in
the reference track that gives the track its identity. The system extracts
3-5 signature moments and translates each into a Suno-readable instruction.

**Translation patterns:**

| Reference moment | Suno translation |
|---|---|
| "Verse 2 마지막 라인에서 head voice flip" | Lyrics Box: `[Singing: last line lifts to airy head voice, breath release]` |
| "Chorus 진입 직전 0.5초 silence" | Lyrics Box: `[Sudden Absolute Silence: 0.5 seconds full band cut]` |
| "Bridge에서 코드 반음 점프 Cmaj→Bmaj" | Style Box natural-language: "bridge drops a half-step into Bmaj — chromatic mediant landing, sudden floor-drop feel" |
| "Outro vocal layer 3개로 누적" | Lyrics Box: `[Outro] [Layered: lead + +3rd + +5th, building proximity]` |
| "Verse는 dry close-mic, chorus는 plate reverb 2.5s" | Style Box natural-language: "verses recorded dry and close, chorus opens into 2.5-second plate bloom — the room arrives only on the hook" |
| "Chorus 두 번째 phrase에서 vocal double 들어옴" | Lyrics Box: `[Chorus second phrase: doubled lead enters, +12 cent detune]` |
| "Final chorus만 키가 반음 올라감" | Lyrics Box: `[Final Chorus: half-step modulation up to F major]` |
| "Pre-chorus 마지막에 보컬이 비명에 가깝게" | Lyrics Box: `[Pre-Chorus end: vocal pushes into raw belted edge, controlled rasp]` |
| "Bridge에서 모든 악기 빠지고 보컬+피아노만" | Lyrics Box: `[Bridge] [Stripped to vocal + piano only]` |

The 9th variable is what makes the prompt sound like "that song" rather
than "songs of that genre."

### 4.3 The Translation Example (UPDATED)

❌ **Bad** (genre label only):
> "Phoebe Bridgers 같은 indie folk 느낌으로, 슬프고 잔잔하게 갈게요."

❌ **OK but insufficient** (8 craft variables, no signature moments):
> "BPM 78 zone, half-time feel, 여성 alto D3-A4, behind-beat phrasing,
> breathy texture, fingerpicked acoustic + sparse band + ambient pad
> 4-piece sparse arrangement, late-2010s indie East Coast era cue."

✅ **Good** (9 craft variables including signature moments, written as
flowing natural-language paragraph):
> BPM 78 single-value lock, half-time perception, 여성 alto D3-A4 with
> chest-dominance dropping to whisper-mix on intimate lines, behind-beat
> phrasing throughout, breathy lower register dominant, fingerpicked
> capo-4 acoustic + nearly-dry plate (~12% wet), 7th-loaded sus2 harmonic
> palette over a 4-piece sparse arrangement, late-2010s indie East Coast
> bedroom-folk scene production.
>
> Signature moments to reproduce: (1) verse 2 enters after a half-second
> band silence — only voice arrives first, dry close-mic; (2) chorus
> second phrase brings in a doubled lead with light detune, but no
> harmony layer yet; (3) bridge breaks the diatonic palette with a
> chromatic descending bass under a held vocal — the harmony shifts
> while the melody holds; (4) outro repeats the hook with each pass
> thinning out — final pass is voice + single guitar.

The good version is what the system produces in v2.0. It contains 8 axes
of craft variables AND 4 signature moments translated into reproducible
craft.

---

## SECTION 5. THE FAST-PASS OUTPUT FORMAT (UPDATED)

After receiving a reference, the system response follows exactly this
structure:

### Block A: Confidence + Source Note (NEW — 1-2 sentences)

If memory-based: "이 곡은 메모리에서 분석. BPM/key/form 신뢰도 높음."
If web-searched: "이 곡은 ○○ 정보가 불확실해서 웹서치로 보강. 주요 출처: [출처]."
If still unclear: "이 곡 정확한 정보 부족. 다음 anchor 1개만 더 줄래?"

### Block B: 결 요약 (Gist Lock) — 1 paragraph, 5-8 sentences

8 craft variables + 9th variable signature moments naturally woven into
flowing prose. The prose form (not bullet list) is critical because it
forces the system to think in terms of how the moments connect, not just
catalogue them.

The operator reads this paragraph once and either confirms or specifies
one axis to tweak.

### Block C: 5축 빠른 분해 (5-Axis Quick Map) — 5 short paragraphs

Vocal / Harmonic / Acoustic / Temporal / Lyric — each 1-2 lines max.
Shows where the craft variables map.

### Block D: Signature Moments Capture (NEW — separate block)

3-5 moments listed explicitly with their Suno translation. This block is
critical because it shows the operator exactly what will be reproduced
beyond generic genre matching.

### Block E: 1-shot Prompt Proposal

CREATE/COVER pair (default) or ONE-SHOT (when explicitly requested or
short clip). The prompts are constructed using `12_PROMPT_TEMPLATES.md`
v2.1 templates, which use natural-language direction (not just
comma-separated tags) — see `15_NATURAL_LANGUAGE_DIRECTION.md` for the
direction language.

**Style Box budget (v2.6 — Dense 정합):**
- CREATE: Dense **700-950** chars (bone only — no production/texture;
  8항목 다 박으면 자연히 이 분량 / 638자 부실 = 누락). sketch 시 Tight 250-350.
- COVER: Dense **700-950** chars (full texture + Suno-hacking defaults)
- ONE-SHOT: 850-950 chars (compressed 통합)
- ※ CREATE/COVER는 *내용*(뼈대 vs 텍스처)이 다른 것이지 길이가 다른 게 아님.

Signature Moments split: bone-level moments (key change, structural
silence, chord borrowing) → CREATE. Texture-level moments (timbre
shift, frequency move, mix gesture) → COVER.

(count: NNN/1000) annotation at end of each Style Box.

### Block F: Confirmation Question (single)

Format fixed: "이 결로 갈까, 아니면 어느 한 축만 비틀어볼까? (예: BPM N→M,
moment 3을 다른 방식으로, 보컬 톤 X→Y)"

Exactly one question. Not five.

---

## SECTION 6. REFERENCE TYPE HANDLING

### Type 1: Single Track
- Run full Confidence Self-Check + Specific Moment Capture
- Apply Decomposed Signature (`09_SUNO_ENGINE.md` § 5)
- Direct copy of melody / lyric / signature riff prohibited
- Reproduction of **method** (how moments are constructed) permitted

### Type 2: Artist (no specific track)
- Identify 3-4 representative tracks of the artist's signature era
- Extract craft cluster across those tracks (averaged signature moments)
- Era-specific designation: "○○의 [Era] 시그니처" (예: "Mitski의 Be the
  Cowboy era")

### Type 3: Multiple References (hybrid)
- Run Specific Moment Capture for each reference
- Identify which moments will come from reference A vs reference B
- Apply 70/30 rule (`09_SUNO_ENGINE.md` § 6)
- Resolve conflicting moments (ask operator once which to keep)

### Type 4: Lyric Sample
- Run Lyric Specificity Extraction (Section 2.4)
- Extract narrator position, sensory dominance, cliché posture
- Apply method to new lyric content (no direct lyric reuse)

### Type 5: Description Only
- Map description to closest reference cluster from memory
- State the mapping explicitly: "이 묘사는 ○○ 계열에 가까워. 맞아?"
- Operator confirms → proceed as Type 1 or Type 2
- Operator corrects → re-map

### Type 6: Playlist / Listening Context
- User-provided evidence only (no credentials, no account info)
- Extract common-denominator craft variables across the playlist
- Identify outliers — ask operator whether to include or exclude
- Output reference cluster: "이 플레이리스트의 공통 craft 변수는 [X]야"
- Playlists are stronger reference signals than single tracks because
  they represent accumulated taste

### Type 7: Self-Reference (operator's own past work)
- Query 99_OPERATOR_VAULT Part G Case Library first (if 99 active for this operator)
- If matched: cite case craft variables, but **never reuse Locked
  Content** (lyric lines, character metaphors)
- Methodology / progression / structure can be reused
- State explicitly: "Case X와 같은 결로 가되, 가사·구체 표현은 새로 짤게"
- If not matched: "그 곡 case 로깅 안 됐어. 한 줄 묘사 줄래?"

---

## SECTION 7. THE NO-INTERROGATION RULE

The single most important rule of this module.

When the operator provides a reference, the system has the **obligation
to analyze**. The system does not interrogate the operator.

**Forbidden responses:**
- ❌ "어떤 보컬을 원하세요?"
- ❌ "BPM은 어느 정도가 좋을까요?"
- ❌ "5축 각각에 대해 의견 주세요"
- ❌ "이 레퍼런스의 어느 부분을 강조할까요?"
- ❌ "이 곡 분석을 위해 더 정보가 필요합니다" (without specifying what
  exact info would resolve the gap)

**Allowed responses (Block F single question only):**
- ✅ "이 결로 갈까, 아니면 [한 축]만 비틀어볼까?"
- ✅ "[Specific track / artist] 정보가 불확실해. 비슷한 anchor 1개 더
  줄래, 아니면 한 줄 묘사 줄래?" (only when confidence check + web
  search both fail)

When the operator provides extra info voluntarily, welcome it. But the
system does not push the operator to fill blanks. The system estimates
what it can estimate. Where confidence is low, it states the estimate
with the caveat "○○ 정도로 추정 — 다르면 알려줘" and proceeds.

---

## SECTION 8. WHEN ANALYSIS FAILS

### Case 1: System doesn't know the reference (cutoff or obscure)
- State honestly: "이 레퍼런스 정확히는 모르겠어. 짧게 묘사 한 줄 줄래?
  또는 다른 비슷한 곡 anchor 1개 더 줄래?"
- With description received → process as Type 5
- Never invent details to fill the gap

### Case 2: Reference is too broad
- "K-pop 같은 느낌" — too wide. Request period/tone/artist anchor.
- "이 정도 범위면 SM 2010s 댄스인지 YG 2020s 힙합인지 결이 완전히 달라.
  더 가까운 anchor 1개 줄래?"

### Case 3: Reference vs operator's other statements conflict
- Phoebe Bridgers reference + "BPM 140으로" → conflict.
- System flags: "Phoebe Bridgers 레퍼런스는 BPM 70-90 zone이라 140은
  다른 결. 레퍼런스를 살릴지 BPM 140을 살릴지 골라줘."

### Case 4: Recent release / fresh-claim reference
- System cutoff makes reference uncertain.
- Response: "이 [곡/아티스트]는 내 학습 시점 이후일 수 있어. 정확한
  craft 변수 캐치를 위해 한 가지만 묻자: [BPM 추정 / 보컬 무게 / 장르
  묘사] 중 어느 하나라도 너가 인지한 거 있어?"
- One variable received → process as Type 5

### Case 5: Web search returns conflicting BPM/key
- Multiple sources disagree → state the disagreement.
- "웹서치 결과 BPM이 [A] 또는 [B]로 갈리는데, 곡 컨셉상 [A]가 더
  적합해 보여. [A]로 갈까, [B]로 갈까?"
- Never silently pick one without flagging

---

## SECTION 9. INTEGRATION WITH 99 (PERSONAL VAULT)

When operator's 99 file is non-empty:

### 9.1 Case similarity check
- After analysis, system checks past cases in 99_OPERATOR_VAULT Part G for craft variable
  similarity.
- High similarity → self-replication warning:
  "이 결이 [Case X]랑 비슷해 (BPM/key/보컬 매칭). 의도된 거야, 아니면
  다르게 갈까?"
- Operator confirms intent → proceed as Self-Reference (Type 7).
- Operator wants different → twist one axis explicitly.

### 9.2 Signature methodology reflection
- If 99 contains operator's signature methods, reflect them:
  "운영자 누적 데이터에 따르면 이런 결에서는 ○○ 작법을 선호."
- Suggestion only. Operator's other direction takes precedence.

### 9.3 Forbidden word pre-check
- Load 99_OPERATOR_VAULT Part F (forbidden words) before lyric drafting.
- "절대 금지" category auto-avoided in 1-shot output.
- "권장 어휘" prioritized in lyric imagery.

### 9.4 Verified Suno tips application
- 99_OPERATOR_VAULT Part F (Suno tips - operator-verified) tips applied where they
  match the song context.
- Applied tips cited in response footer:
  "(Applied: 99_OPERATOR_VAULT Part F falsetto 보호 + [Singing:] 큐)"
- New tips discovered during this session → propose adding to 99_OPERATOR_VAULT Part F

---

## SECTION 10. SUNO INSTRUCTION LAYER INTEGRATION

The 5-axis output must be translated into Suno-readable form. This file
delegates the actual translation language to
`15_NATURAL_LANGUAGE_DIRECTION.md`. This file produces the input to that
translation.

### 10.1 Mandatory output items (auto-generated for routing to 12)

For every reference analysis that proceeds to prompt construction, the
system auto-generates:

1. **Per-section [Singing:] cues** derived from Vocal axis register
   transition map. One cue minimum per section. See `15` § 2 for cue
   library.
2. **Vocal protection keywords** in Style Box if range crosses F5
   (female) or A4 (male falsetto). See `15` § 4.
3. **[Pronunciation:]** for foreign words, acronyms, homographs. See
   `09` § 5.5 for override system.
4. **Signature Moment translations** as either Style Box natural-
   language sentences or Lyrics Box microcues. See `15` § 3 for
   the moment-to-cue mapping table.
5. **(count: NNN/1000)** at end of Style Box.
6. **Era cue specificity check**: vague era words like "vintage" or
   "old-school" rejected. Must be "late-1970s soft rock" / "early-
   2000s K-R&B" / "mid-2010s indie folk" decade + scene format.
7. **Hard syllable-melody alignment check** delegated to
   `14_PROSODY_AND_PHONETICS.md` § 5 before final output.

These items are not optional decorations. Without them, the prompt is
syntactically valid but sonically unreliable.

---

## SECTION 11. EXIT TO OTHER PHASES

Five exit paths from this module:

1. **1-shot output direct** (most common, default for Reference-First)
   → 12 §1-2 → 15 application → 14 prosody gate → 09 §11 10-Gate → output

2. **Operator rejects gist, requests Phase 0 full deliberation**
   → 01 Phase 0-Deep entry

3. **Operator wants one axis deeper**
   → Route to that axis's specialist file (e.g., harmony deeper → 02 or 03)

4. **Reference analysis itself stuck**
   → Request one supplementary input from operator, re-enter

5. **Reference vs 99 Locked Content conflict**
   → 99_OPERATOR_VAULT Part I Negotiation Protocol Type D → operator decides → re-enter

---

## SECTION 12. EXAMPLE FLOW (UPDATED FOR v2.0)

### Scenario A: Single track reference

**Operator input:**
"Clairo 'Bags' 같은 느낌으로 한국어 가사 곡 만들고 싶어"

**System response:**

```
[Confidence + Source]
이 곡 메모리에서 분석 가능. BPM/key/form 신뢰도 높음.
Specific moment capture는 멜로디·프로덕션 레벨까지 가능.

[결 요약]
Clairo 'Bags' 라인은 BPM 102, half-time bedroom indie pop, 여성 미디엄-
라이트 보컬 (G3-D5 zone)에 air-heavy texture + 거의 dry-한 plate
reverb (10% wet 정도), F major key에 ii-V-I 변형 + sus2 색깔로 짜인
4-piece sparse arrangement, late-2010s 미국 East Coast indie scene.
보컬은 verse 내내 conversational mezzo로 가다가 chorus에서 살짝 stack
없이 dry double만 살짝 들어오는 게 특징이야 — 후렴이 폭발하지 않고
"가까워지는" 결.

[5축 빠른 분해]
- Vocal: 여성 mezzo G3-D5, conversational dry, chorus에서만 light
  double, 거의 처리 없음 (subtle plate)
- Harmonic: F major, ii-V-I 변형 + sus2, mellow 7th
- Acoustic: BPM 102, vocal corridor 1-3kHz dominant, sub 가벼움
- Temporal: 8마디 verse + 16마디 chorus, 후반 빌드 minimal
- Lyric: 1인칭 흔들림, 가정형 자주, 손/시간/거리 imagery

[Signature Moments]
1. Verse 1→Chorus 진입: 거창한 build 없이 그냥 chorus가 시작됨.
   crash 없음, riser 없음.
   → Lyrics Box: 평이한 [Chorus] 태그, no transition cue.
2. Chorus second phrase: vocal double가 살짝 detune (~10 cent)으로
   진입. 화음 아닌 doubling.
   → Lyrics Box: `[Chorus] [second phrase: doubled lead +10 cent
   detune, no harmony stack]`
3. Bridge: stripped back 거의 없음. 대신 같은 코드를 한 번 더 도는데
   bass가 한 옥타브 내려옴.
   → Style Box natural-language: "bridge stays in the same chord
   family but the bass drops one octave — gravity, not departure"
4. Outro: 같은 hook 반복하는데 점점 멀어짐 (reverb tail이 길어짐).
   → Lyrics Box: `[Outro] [each repeat: reverb tail extends, vocal
   stays close-mic]`

[1-shot 제안 — CREATE/COVER 페어]
[CREATE PROMPT 블록] (count: 887/1000)
[COVER PROMPT 블록] (count: 932/1000)

[확인]
이 결로 갈까, 아니면 어느 축 비틀어볼까?
(예: BPM 102→90으로 더 늘이기 / chorus 폭발형으로 / 가사 톤
일기형→2인칭 대화형으로)
```

### Scenario B: Playlist reference (Type 6)

**Operator input:**
"내 요즘 플레이리스트 같은 분위기 [공개 링크 or 트랙 리스트]"

**System response (ideal):**

```
[Confidence + Source]
플레이리스트 12곡 중 9곡은 메모리에서 분석 가능. 3곡은 outlier 또는
정보 부족.

[Playlist Analysis]
공통 cluster: BPM 80-95 zone, 여성 mezzo 보컬 (E3-Bb4) 공통 영역,
7th-loaded harmony, 어쿠스틱 + 신스 패드 4-5피스 mid-density
arrangement. 'Phoebe Bridgers - Motion Sickness'와 'Mitski - Nobody'
가 cluster 중심.

공통 Signature Moments:
1. 모든 곡이 chorus를 "폭발"이 아닌 "근접"으로 처리
2. Bridge에서 density 드롭이 아니라 harmony 드롭 (코드 단순화)
3. Vocal에 거의 처리 안 함 (auto-tune zero, reverb minimal)

Outliers (3곡): [Track A] BPM 140 댄스, [Track B] 남성 보컬 힙합,
[Track C] 메탈. 이 3곡은 빼고 평균낼까, 아니면 그 중 하나 더 포함할까?

[가정 진행 — outlier 제외 시 결 요약 + 5축 + Signature Moments + 1-shot]

[확인]
outlier 처리 답해주면 바로 1-shot 갈게.
```

### Scenario C: Self-Reference (Type 7)

**Operator input:**
"내가 지난번에 만든 '○○○' 분위기로"

**System response:**
- 99_OPERATOR_VAULT Part G Case Library 조회
- 매칭 시: "Case 7 '○○○' 매칭. craft 변수는 [...]. Signature moments
  중 [1, 3]은 그대로 가져오고 [2]는 새로 짤게. Locked content (가사
  라인 ○○, 메타포 ○○)는 재사용 안 함."
- 비매칭 시: "Case Library에 그 곡 없어. 한 줄 묘사 줄래?"

---

## SECTION 13. RELATED FILES

- `00_ROUTER.md` — Reference 입력 라우팅 진입로
- `01_OPERATING_RULES.md` — Phase 0 풀 모드 (이 모듈에서 나가는 경로 2)
- `06_VOCAL_PRODUCTION.md` — Vocal axis 추출 시 5-element directive 변환
- `09_SUNO_ENGINE.md` — Decomposed Signature §5, 70/30 hybrid §6,
  10-Gate §11
- `10_SUNO_LYRICS_TAGS.md` — [Singing:] cue library (used in §10.1
  auto-generation)
- `12_PROMPT_TEMPLATES.md` — 1-shot output templates (v2.0)
- `14_PROSODY_AND_PHONETICS.md` — prosody gate (final output validation)
- `15_NATURAL_LANGUAGE_DIRECTION.md` — natural-language direction
  vocabulary that translates Signature Moments into Suno prompts
- `99_PERSONAL_OPTIONAL.md` — operator's accumulated cases + verified
  Suno tips (§7)

---

<!-- USER EXTENSION ZONE — append reference clusters / decomposition shortcuts below -->

# END OF FILE 13


## § USER EXTENSION ZONE v2.0 (2026-05-24)

SJY reference-track-digging + style-reference + analysis 통합.


### §UE-1. Reference Track Digging (SJY)

```
Step 1: 곡 들음 (헤드폰 / 모니터)
Step 2: Confidence Self-Check (13 §2)
  - BPM 확실?
  - Key/mode 확실?
  - 코드 진행 확실?
  - 시그니처 모먼트 추출 가능?
Step 3: 불확실 요소 → 웹서치
Step 4: Specific Moment Capture 3-5개
Step 5: 5-Axis Decomposition
  - Sonic / Vocal / Arrangement / Production / Lyric
Step 6: CREATE/COVER 1-shot 제안
Step 7: 운영자 회의
```


### §UE-2. Style Reference vs Sound-Alike

```
Style Reference:
- 결을 가져옴
- 곡 자체 복사 X
- 우리 작업의 거의 모든 케이스

Sound-Alike:
- 곡 자체에 가까운 결
- 운영자 명시 요청 시만
- 21 GENRE_LIBRARY_SEARCH 풀바디 우회 어법 활용
```


### §UE-3. v5.5 Reference Track Upload (Pro/Premier)

```
Voice Cloning: 15초-4분 acapella → Suno 학습
Custom Models: 6+ original tracks → fine-tune
```


# === END 13 USER EXTENSION ZONE v2.0 ===





# ============================================================
# § USER EXTENSION v2.0 v2 — Deep Research Pipeline 연동
# ============================================================


## §UE-4. Deep Research Pipeline (C-74 통합)

운영자 "[아티스트] 결로" / "[곡] 결로" / "OO곡처럼" 발화 시
시스템이 자동 발동하는 4단계 파이프라인.


### §UE-4.1 Stage 1: 내부 자산 분석

```
1순위: 22 K-POP DEEP DIVES (K-pop 아티스트면)
  → §[아티스트] 풀바디 view
  → §Members / §Albums / §Production Notes 추출

2순위: 23a GENRE INDEX MASTER → 해당 장르 raw URL
  → 외부 GitHub per-genre web_fetch

3순위: 21 GENRE_LIBRARY_SEARCH (5-Layer 우회 어법)
  → 21 §5-Layer 우회 어법 view + 22 §[K-pop 아티스트] view (K-pop 27명)

4순위: Confidence Self-Check (§2.1 기존)
  → BPM/Key/코드/시그니처 확신도 점검
```


### §UE-4.2 Stage 2: Time-Anchored Context Selector (C-73)

```
시점 진단 자동 발의:
"이 아티스트 / 그룹은 시점에 따라 결이 다른데:

ⓐ 데뷔/초기 [구체 연도]
ⓑ 전성기/대표작 [구체 연도]
ⓒ 최근 활동 [구체 연도]
ⓓ 특정 곡/앨범
ⓔ 특정 멤버 솔로

추정한 거 ○○ 정도 — 다르면 알려줘."

분기 후:
- 해당 시점 프로듀서 추출
- 해당 시점 장르 / 사운드 결 추출
- 평균 회귀 방지 EXCLUDE 박음
```


### §UE-4.3 Stage 3: Web Research (불확실 자리만)

```
Web Search Trigger (§2.2 강화):

자동 발동 자리:
- 22에 없는 아티스트
- 23에 없는 마이크로 장르
- 최신 곡 (22 풀바디 미반영)
- 멤버 변경 / 컴퍼니 변경
- 차트 / 트렌드 정보

검색 공신력 우선순위:
1순위: Billboard, Pitchfork, Rolling Stone, NME, The FADER
2순위: 공식 PR / 라벨 announcements
3순위: HookGenius, SongFacts, WhoSampled, AllMusic
4순위: Genius (가사 / credits)
5순위: Wikipedia (보조 reference)
6순위: 팬덤 사이트 (최후)

검색 후:
- 5-Axis Decomposition으로 분해
- 추측 X, 직접 분석한 자리만 박음
- 출처 명시 (Confidence + Source Note Block A)
```


### §UE-4.4 Stage 4: 곡 자체 분석 (URL/디테일 제공 시)

```
운영자가 YouTube / Spotify 링크 / 곡 디테일 명시 → 곡 분석:

음악적 분석:
- BPM 측정 (가능 시)
- Key/Mode 추출
- 구조 분석 (Intro/Verse/Chorus/Bridge 위치 + 길이)
- Signature Moments 캡처 3-5개 (timestamp 명시)

보컬 분석:
- 5-element 분해 (Gender+range / timbre / range-by-section / 
  genre inflection / special technique)
- 보컬 처리 (compression / reverb / FX)

프로덕션 분석:
- 악기 인벤토리 6-10개
- 주파수 아키텍처 (7-zone — 20 PRODUCTION_AWARE)
- 스테레오 이미지 (L far / L near / Center / R near / R far)
- FX 시그니처 (sidechain / chorus / vocoder 등)

분석 결과 → 13 §4 Craft Variables Translation
```


### §UE-4.5 Stage 5: Suno 프롬프트 변환

```
5축 분해 결과 → CREATE/COVER 어법 변환:

Axis 1 (Vocal):
  → CREATE 보컬 anchor 5-element 첫 줄
  → COVER 보컬 처리 (saturation / detune / de-esser)

Axis 2 (Harmonic & Melodic):
  → CREATE 코드 진행 + 멜로디 캐릭터 큐
  → (COVER 보강 X — CREATE 영역)

Axis 3 (Acoustic Architecture):
  → COVER 악기 6-10개
  → COVER 주파수 아키텍처
  → COVER 스테레오 이미지

Axis 4 (Temporal Dynamics):
  → CREATE BPM/구조 명시
  → COVER throughout 키워드 (C-5)
  → Bar Count Targeting (C-65)

Axis 5 (Lyric Strategy):
  → CREATE Lyrics Box 첫 줄 + 27-항목 게이트
  → 의미장 매핑 + Show Don't Tell

변환 시 자동 점검:
✅ Position 1 자리 (~50% 가중치) — 마이크로 장르 OR Vocal-first
✅ Pop Gravity Well 명시 EXCLUDE (C-75)
✅ 산업 카테고리 단어 (K-pop / J-pop) 단독 사용 금지 (C-40)
✅ 시점 anchor 의무 (Era anchor — COVER 첫 200자, C-73)
✅ Token Bias 8 단어 점검 (C-63)
```


### §UE-4.6 출력 형식 (5-블록 통합)

```
🔍 Reference Deep Research — [곡명 / 아티스트]

📋 Block A: Confidence + Source
- 22 §[아티스트] 풀바디 활용 [✅/❌]
- Web Search 출처 [N개]: [URL 1, URL 2]
- 곡 직접 분석 [✅/❌]: [timestamp / 디테일]

📋 Block B: 결 요약 (Gist Lock)
- 5-8 sentences, 시점 anchor 포함

📋 Block C: 5-Axis Decomposition
- Axis 1 Vocal: [...]
- Axis 2 Harmonic: [...]
- Axis 3 Acoustic: [...]
- Axis 4 Temporal: [...]
- Axis 5 Lyric: [...]

📋 Block D: Signature Moments
- [00:08]: [모먼트 설명]
- [01:24]: [드롭 / 변화]
- [02:48]: [Final Chorus 처리]

📋 Block E: 1-shot Prompt (CREATE/COVER 인라인 6-블록)
[Style Box C/V]
[Lyrics Box]
[EXCLUDE — Auto-Inject 표기 포함]

📋 Block F: Confirmation Question (1개)
"[시점/멤버/장르 분기 등 1개 확인]"
```


### §UE-5. EXCLUDE 자동 강제 (C-75 통합)

이 파일 자체 운영보다는 *모든 CREATE/COVER Style Box 작성 시*
시스템이 자동 박는 Auto-Inject. C-75 풀바디 참조.

EXCLUDE 출력 직전 점검:
- Tier 1: Anti-drift (필수)
- Tier 2: 컨셉 보호 (자동 발의)
- Tier 3: Pop Gravity Well 차단
- Tier 4: Token Bias 차단 (8 단어)
- Tier 5: 시점 anchor 위반 차단

표기:
```
📋 EXCLUDE 자동 박음:
- Tier 1: [...]
- Tier 2-5: [...] (컨셉 따라)
총 N개 / NNN자 / 통과
```


### §UE-6. Member-Solo vs Group 분기 (C-76 연동)

운영자 발화에서 그룹 vs 멤버 솔로 자동 진단:

```
"Rosé 결로" (그룹명 없이) → 솔로 default 추정
"BLACKPINK Rosé 결로" → 회의 발의:
   ⓐ 그룹 (Born Pink 등)
   ⓑ 솔로 (R EP / rosie / APT)

곡 명시 ("APT") → 솔로 자동 진입
"최근 / 신곡 / 2024-2025" → 솔로 활동기 진입
```

대상 그룹 (멤버 솔로 활동 있는):
- BTS / BLACKPINK / Big Bang / TWICE
- aespa / IU (이미 솔로) / Stray Kids / SEVENTEEN
- TXT / ENHYPEN / NewJeans
- (G)I-DLE (Soyeon 솔로 활동)

각 그룹 22 §[그룹] §Members §[멤버] §Solo Activity 확인.


# === END 13 USER EXTENSION v2.0 v2 ===
