# 09. SUNO ENGINE — Operating Manual

**Version**: 2.4
**Last Updated**: 2026-05-12
**Engine Target**: Suno v5 / v5.5 (with backward notes for v4)
**Load Trigger**: Whenever generating, debugging, or formatting any Suno prompt — this file is consulted on every generation.
**Companion Files**: `10_SUNO_LYRICS_TAGS.md`, `12_PROMPT_TEMPLATES.md`, `06_VOCAL_PRODUCTION.md`

---

## SECTION 0. PURPOSE

This file is the engineering reference for Suno itself — not for music. It governs:
1. The hard limits of the engine (character count, token weighting, mode behavior).
2. The CREATE / COVER role separation doctrine.
3. The One-Shot vs Two-Stage workflow.
4. Genre-blending mechanics inside the prompt.
5. Artist-reference encoding without copyright triggers.
6. Tag priority, ordering, and re-tokenization avoidance.

Every Suno prompt produced by this system must comply with this file before delivery to the user.

---

## SECTION 1. ENGINE FACTS (HARD LIMITS)

### 1.1 Character Limits

| Field | v5 / v5.5 | v4 and older |
|---|---|---|
| Style of Music (Style Box) | **1,000 characters** | ~200 characters |
| Lyrics field | **5,000 characters** total | ~3,000 |
| Exclude Styles (negative) | ~200 characters | ~200 |
| Persona description | ~1,000 characters | n/a |

**Counting rule**: Suno counts **characters, not bytes, not tokens**. Korean, Japanese, Chinese, and emoji each count as 1 character per visible glyph.

**Truncation behavior**: when the limit is exceeded, Suno **silently truncates** without warning. The cut happens at the character boundary — mid-word is possible. Anything past the cut has zero influence.

### 1.2 Effective Influence Window
Although the Style Box accepts 1,000 characters, **influence is heavily front-loaded**:
- The first 60-80 characters carry ~60% of stylistic weight.
- Characters 80-300 carry ~30%.
- Characters 300-1,000 carry the remaining ~10%, often acting as fine-tuning seasoning.

**Operating principle**: write the prompt as if only the first 200 characters will be heard. Use the rest for refinement, not core identity.

### 1.3 Re-Tokenization Risk
When a prompt exceeds 1,000 characters and gets cut mid-token, Suno's tokenizer can re-segment the remaining string in unintended ways, producing incoherent style hits. Avoid by:
- Hard-counting before submission (every prompt this system produces is character-counted).
- Keeping the last 50 characters as a safety buffer.
- Never placing critical genre/vocal anchors in the final 100 characters.

### 1.4 Forbidden Characters in Style Box
- **Square brackets `[ ]`** — illegal in Style Box. They belong in the Lyrics field only. Suno will either reject them or reinterpret them.
- **Newlines** — collapse to spaces; do not rely on visual structure.
- **Excessive punctuation** — `!!!`, `???`, repeated commas — degrade parsing.

Use only: lowercase/uppercase letters, numbers, commas, periods, hyphens, parentheses, single spaces.

### 1.5 Tag Order Matters
Confirmed across community testing: earlier-positioned tags carry more weight. Order rule:
1. **Genre anchor** (1-2 words) — first.
2. **Era / sub-style** modifier — second.
3. **Vocal directive** — third.
4. **Tempo / mood** — fourth.
5. **Instrumentation** — fifth.
6. **Production / mix character** — sixth.
7. **Texture / atmosphere seasoning** — last.

---

## SECTION 2. SUNO MODES

### 2.1 Simple Mode (One-Shot)
- Single text box. User describes the song in natural language. Suno infers genre, writes lyrics, generates audio.
- **Strength**: holistic, often more "finished" sounding because Suno auto-balances lyrics, style, and structure.
- **Weakness**: zero precision control. Cannot lock genre, vocal type, or structure.

**Use when**:
- Rapid sketching, mood exploration.
- The user has a vibe but no fixed structural intention.
- Cover/remix referencing where you want the engine to interpret freely.

### 2.2 Custom Mode (Two-Field)
- Two fields: **Style of Music** (1,000 chars) + **Lyrics** (5,000 chars). Optional: Title, Persona, Exclude Styles.
- **Strength**: full control over genre encoding, vocal directive, structural tagging, pronunciation.
- **Weakness**: requires disciplined prompt construction; novice prompts often underperform Simple Mode.

**Use when**:
- Professional output is required.
- Specific vocal type, language, accent, or section structure is non-negotiable.
- Iterative refinement is planned.

### 2.3 Persona Mode
- A saved style profile that auto-fills the Style of Music field. Built either from a previous Suno generation (vocal-cloned) or manually as a reusable description.
- **Strength**: vocal consistency across multiple tracks (album work). Frees the Style Box for musical direction since identity is locked in the Persona.
- **Weakness**: Personas built from generations carry over the original's quirks (good and bad).

**Operating rule**: when working on an album or multi-track project, build a Persona for the lead vocalist first, then use Custom Mode with the Persona attached. The Style Box then focuses purely on per-track musical direction.

### 2.4 Cover Mode
- Takes an uploaded audio (or existing Suno track) and re-renders it in a new style while preserving melody and lyric phrasing.
- **Strength**: melodic identity is locked; only arrangement, instrumentation, and vocal character change.
- **Weakness**: cannot fundamentally restructure the song; cover follows source phrasing.

### 2.5 Remix / Extend
- **Remix**: alters style/instrumentation while keeping the audio waveform reference.
- **Extend**: continues an existing track from any timestamp using new prompt input.

These are referenced here for completeness; detailed operation is in `12_PROMPT_TEMPLATES.md`.

---

## SECTION 3. THE CREATE / COVER DOCTRINE

This is the core production strategy of the system. It applies whenever the user wants high-quality output with controllable iteration.

### 3.1 The Problem It Solves
A single prompt trying to do everything — define genre, vocal, structure, melody, atmosphere, lyric mood — collides with Suno's front-loading bias. The first generation either nails the vibe but botches the vocal, or vice versa. Re-rolling the whole song wastes credits and loses good elements.

The CREATE / COVER pair separates **bone** (structural/melodic identity) from **texture** (timbral/atmospheric character). Generate the bone first, then re-skin it via Cover.

### 3.2 Role Separation

**CREATE PROMPT (Generation 1 — bone)**:
- **Job**: establish melody, song structure, lyric phrasing, vocal phrasing, tempo, key feel.
- **Style Box content**: minimal genre anchor + clear vocal directive + tempo + minimal instrumentation. Resist atmosphere/texture description.
- **Goal**: produce a take where the melody and vocal flow are usable, even if the production sounds plain.
- **Acceptance criteria**: melody memorable, vocal range/timbre correct, lyric prosody clean, structure tags respected. Mix quality is secondary.

**COVER PROMPT (Generation 2 — texture)**:
- **Job**: re-skin the chosen CREATE take with the target genre, instrumentation, mix character, atmosphere.
- **Style Box content**: full genre encoding + production keywords + atmosphere + texture + reference encoding. Vocal directive is light (Persona or Cover preserves the original).
- **Goal**: deliver the final-feel version while preserving the melody/vocal that worked in CREATE.
- **Acceptance criteria**: genre identity strong, mix character matches reference, melody preserved from CREATE.

### 3.3 What Goes Where — Decision Table

| Element | CREATE | COVER |
|---|---|---|
| Primary genre anchor (1-2 words) | ✅ light touch | ✅ full encoding |
| Sub-genre, era, regional flavor | ❌ avoid | ✅ here |
| Vocal gender, range, timbre | ✅ here | partial (Persona handles) |
| Vocal accent, language | ✅ here | preserved by Cover |
| Tempo (BPM) | ✅ here | preserved |
| Key/mode | ✅ here | preserved |
| Song structure tags | ✅ in Lyrics | preserved |
| Lyric content | ✅ here | preserved |
| Instrumentation (specific instruments) | minimal | ✅ here |
| Production character (lo-fi, polished, vintage) | ❌ avoid | ✅ here |
| Mix character (wide stereo, dry, reverb-soaked) | ❌ avoid | ✅ here |
| Atmosphere/mood adjectives | minimal | ✅ here |
| Reference artist encoding | ❌ avoid | ✅ here |
| Hybrid genre ratio | ❌ avoid | ✅ here |

### 3.4 The CREATE Prompt — Construction Rule
Keep the Style Box under **300 characters**. Goal is a clean melodic/vocal foundation. Example skeleton:


[primary genre], [tempo BPM], [key/mode if relevant], [vocal: gender + voice type + range + 2 timbre adjectives + language/accent + delivery], [minimal instrumentation: voice + 2-3 core instruments], clear melody focus, structural clarity.

### 3.5 The COVER Prompt — Construction Rule
Use the full 1,000-character window strategically. Example skeleton:

[primary genre encoding with sub-style and era], [reference encoding: Artist-Song-style format, see Section 5], [hybrid ratio if applicable, see Section 6], [full instrumentation list with role specificity], [production character: era, format, processing], [mix character: stereo width, dynamics, EQ tilt], [atmosphere keywords], [texture seasoning].

### 3.5b CREATE/COVER Overlap Prevention (v2.1)

CREATE and COVER must NOT contain similar descriptors. They serve
different functions.

**The 30% Rule:**
If CREATE and COVER Style Boxes share more than 30% of their
descriptors (excluding genre anchor and BPM), one of them is wrong.
Rewrite the weaker one before sending.

Typical failure: CREATE is over-described with production language
that belongs in COVER.

**CREATE budget guardrail (v2.6):** Dense **700-950 characters** 기본
(sketch/다양성 우선 시만 Tight 250-350). bone 8항목(장르·시대 / BPM·key /
섹션 화성 / 컨투어 / 보컬5 / 구조·아크 / 악기3-4 / 시그니처)을 다 박으면
자연히 이 분량 (§2 CREATE Density / C-115). 638자 같은 부실 = 항목 누락 신호.
※ 700자 초과는 정상 bone 밀도이지 텍스처 누설이 아니다. CREATE↔COVER 중복은
*길이 ceiling*이 아니라 **30% Rule**(§3.5b)로 잡는다 — production/mix 언어가
CREATE에 들어갔는지는 *내용*으로 판정(0%여야 함), 글자수로 판정 금지.

**COVER budget guardrail:** Dense **700-950 characters** (texture 채널 =
사실상 항상 Dense). Under 700 = 텍스처 채널 저활용. Over 950 = truncation 위험.
※ CREATE/COVER는 *내용*(뼈대 vs 텍스처)이 다른 것이지 길이가 다른 게 아니다.

### 3.5c Genre-Shift COVER Pattern (v2.1)

When the operator wants cross-genre transformation (e.g., punk
bone → EDM texture):

- CREATE: source genre keywords, melodic chord progression in
  source vocabulary, BPM that works for both genres.
- COVER: target genre keywords + explicit instrument substitution
  map + Hz redistribution.

**Substitution map format (state plainly in COVER NOTES):**
- "replace electric guitars with sidechained supersaws"
- "replace live drums with four-on-floor kick + future-bass
  chord stabs"
- "sub-bass shifted from bass guitar to 808"
- "guitars-to-synth band 2-6kHz handoff"

This signals to Suno that the CREATE bone is being re-skinned,
not regenerated.

### 3.5d 보컬 디렉션 분배표 (v2.4 신규)

오빠 핵심 지적: "보컬은 CREATE/COVER 둘 다 들어가야 하는데 어떻게 다르게?"

**핵심 룰: CREATE 보컬 = identity (5요소 / 정체성), COVER 보컬 = treatment (처리 / 표면)**

| 보컬 요소 | CREATE | COVER |
|---|---|---|
| 성별 (Gender) | ✅ 필수 명시 | 캐릭터 핸들 재주입 (Tip §11.5) |
| 음역 (Range) | ✅ 필수 명시 (C4-F5 등 구체) | preserve (변형 X) |
| 음성 타입 (Voice type) | ✅ 필수 (soprano/tenor 등) | preserve |
| 언어 / 억양 (Language/Accent) | ✅ 필수 (Korean / English+Spanish 등) | preserve |
| 음색 (Timbre 형용사 2-3개) | ✅ 본질 (breathy / husky / clear 등) | reinforce + 보호 키워드 |
| 딜리버리 (Delivery) | ✅ 본질 (conversational / belted 등) | reinforce + 그루브 큐 |
| **보컬 처리 (Processing)** | ❌ 절대 금지 | ✅ 여기에만 (organic화 / saturation / detune 등) |
| **레이어링 (Doubled / Stack)** | ❌ 절대 금지 | ✅ 여기에만 (+3rd / +5th harmony 등) |
| **공간 / Reverb** | ❌ 절대 금지 | ✅ 여기에만 (close-mic / plate / hall 등) |
| **압축 / De-esser / EQ** | ❌ 절대 금지 | ✅ 여기에만 |
| **Throughout 키워드** | ❌ | ✅ ("[character] maintained throughout") |

**CREATE 보컬 디렉티브 표준 형식** (1줄, 70-100자):
```
female mezzo C4-F5 breathy conversational, Korean clear vowel diction
```

**COVER 보컬 처리 표준 형식** (3-4줄):
```
[char timbre keywords] [delivery] maintained throughout despite [genre] arrangement,
vocal organic bus + corridor + warmth (= 99_OPERATOR_VAULT Part F (Suno-Hacking 검증 키워드) 풀처방 자동 확장),
doubled lead +10c detune L15/R15, plate reverb 12% verse / 22% chorus,
de-esser 5-8kHz, vocal corridor 500-3kHz protected
```

**검증 케이스**: Case 23 (캐릭터 핸들 + 처리 분리), Case 32.5 세리카 (Tip §11.5 핸들 재주입).

### 3.5e CREATE→COVER Patch 프로토콜 (v2.4 신규)

CREATE 결과 듣고 COVER에서 무엇을 바로잡는지의 SOP.

기존 문제: CREATE 결과가 만족스럽지 않을 때 운영자가 "별로야" 한 마디만 하면 시스템이 CREATE 전체 재생성으로 가서 좋은 멜로디까지 잃어버림.

**5단계 Patch 흐름**:

**1단계 — 결과 분류**
운영자가 CREATE 결과를 들은 직후 시스템이 묻는다:
```
"이번 CREATE 결과 들어봤어? 다음 5가지 중 어느 거야?
A. 멜로디/구조 OK, 사운드/믹스만 아쉬움 → COVER로 해결
B. 보컬 톤 드리프트 (캐릭터에서 벗어남) → COVER에 핸들 재주입
C. 멜로디 일부 라인만 어색 → COVER 안 함, 같은 CREATE 재생성 + 가사 미세조정
D. BPM/Key 자체가 안 맞음 → CREATE 재설계
E. 구조 자체가 흩어짐 (verse-chorus 구분 약함) → Lyrics Box bar count 보강 + CREATE 재생성"
```

**2단계 — A/B 응답 시: COVER 1차 작성**
- A: 표준 COVER (장르 텍스처 + 99_OPERATOR_VAULT Part F (Suno-Hacking 검증 키워드) 풀처방)
- B: COVER 첫 200자 내 캐릭터 핸들 2-3개 (Tip §11.5)

**3단계 — A/B + 장르 점프 응답 시: §3.5c Substitution Map 적용**
운영자가 "CREATE 포크였는데 COVER 하드락으로 갈래" 같은 cross-genre 요청하면:
- COVER 첫 50자에 새 장르 명시 ("now hard rock skin")
- 악기 치환 맵 명시 ("replace nylon guitar with distorted Les Paul")
- BPM 유지 confirmed in COVER ("preserve 110 BPM bone")

**4단계 — A/B + 미분음/모듈레이션 갑작스레 응답 시: §3.5f 적용**
운영자가 "여기 갑자기 quarter-tone bend 넣고 싶어" 또는 "Final Chorus 갑자기 키 1단 올리자" 요청:
- §3.5f COVER 단계 화성 변경 패턴 적용 (아래)

**5단계 — C/D/E 응답 시: 다른 흐름**
- C: Lyrics Box 가사 미세 조정 + 같은 CREATE Style Box로 재생성
- D: CREATE 재설계 (BPM/Key 변경 명시)
- E: Lyrics Box bar count 의무 표기 + CREATE 재생성

### 3.5f COVER 단계 갑작스러운 화성 변경 (v2.4 신규)

CREATE에서 평범하게 진행되던 곡을 COVER에서 갑자기 모듈레이션·미분음·돌발 코드로 비트는 패턴.

**적용 패턴 1: COVER에서 Final Chorus 키 모듈레이션 추가**

CREATE:
```
F major throughout, four-chord progression I-V-vi-IV
```

COVER 추가:
```
Final Chorus modulates abruptly to F# major (half-step lift) without prep,
truck driver modulation but executed cleanly, vocal stack +3rd +5th over modulation,
signature moment: the half-step lift is the climax, not the chorus melody itself
```

**적용 패턴 2: COVER에서 미분음 quarter-tone bend 추가**

CREATE:
```
A minor, conventional Western harmony
```

COVER 추가 (Tip §11.2 참조):
```
Maqam influence on lead vocal lines bridge only, [1/8 Tone Pitch Bends],
±25 cents detune triple-track on bridge climax word, quarter-tone bend
on "사라져" landing note, returns to conventional Western tuning by Final Chorus.
```

**적용 패턴 3: COVER에서 chromatic mediant 추가**

CREATE:
```
B major all sections
```

COVER 추가:
```
Chromatic mediant drop B→G (down a major third) on every chorus "그냥" word,
landing back to B major next bar — signature gut-drop moment, vocal stays flat
through the drop (gap-moe vocal inversion), Final Chorus modulation to C
preserves the same B→G structure but as C→Ab
```

**적용 패턴 4: COVER에서 borrowed iv 한 마디만 갈기기**

CREATE:
```
D major diatonic
```

COVER 추가:
```
Bridge bar 5 single chord change: D major borrowed iv (Gm) for one bar only,
modal interchange creating sudden shade then immediate return to D major bar 6,
vocal harmonizes the Gm chord with neighbor tone descent
```

**원칙**: CREATE는 "걸어가는 길", COVER는 "도중에 갑자기 비트는 장치". 단, COVER에서 비틀려면 CREATE에서 그 자리의 vocal/structure는 미리 안내선 마련해둬야 함 (예: bridge bar 5 자리 vocal 강조 라인).

### 3.5g CREATE/COVER 다양화 패턴 (v2.4 신규)

오빠 지적: "일률적으로 박을 수 없다. 다양한 패턴 대응이 있어야 한다."

| 패턴명 | 사용 시 | CREATE 어법 | COVER 어법 |
|---|---|---|---|
| **A. 70/30 정통** | 명확한 메인 장르 + 1개 서브 | 단일 장르명 (메인) + BPM + Key + 보컬 5요소 | 메인 70% + 서브 30% 명시 (instrument 비율 / Hz 분리) |
| **B. 자연어 위주 (장르 모호)** | 하이브리드 3개+ 모호 결합 | 자연어 무드 phrase + BPM | 자연어 풀묘사 (§3.20.10 헤드 어법) |
| **C. 적당히 섞기** | "2-3장르 적당히 섞어줘" | 메인 장르 + "with [서브1] and [서브2] elements" | 자연어 + Hz/instrument 분리 가이드 |
| **D. 레퍼런스 우선** | 특정 곡 anchor | "[era]-style [genre]" + Decomposed Signature 200자 | 풀 분해 (5축) + Producer Decomposed §3.20.6 |
| **E. 장르 점프** | CREATE 포크 → COVER 하드락 | CREATE는 원 장르대로 | COVER 첫 50자 새 장르 + Substitution Map (§3.5c) |
| **F. 화성 변경** | COVER에서 모듈레이션/미분음 | CREATE 평범한 진행 | §3.5f 패턴 1-4 적용 |
| **G. Polarity Fusion** | 두 극단 융합 | 중립 베이스 | Cover A (극단 1) + Cover B (극단 2) + Mashup (99_OPERATOR_VAULT Part C (Polarity Fusion) 참조) |
| **H. Persona-locked** | 캐릭터 보컬 락 | Persona 사용 + 음악 디렉션만 | 음악 디렉션 + 캐릭터 핸들 재주입 |
| **I. ONE-SHOT 압축** | 빠른 sketch, ≤2:00 | N/A (사용 안 함) | §4.2 850-950자 압축형 |

**선택 가이드** (운영자 발화 → 패턴 선택):

| 운영자 발화 | 패턴 |
|---|---|
| "메인은 K-indie인데 J-pop 풍 살짝" | A. 70/30 |
| "Future-Retro B-boy 같은 거 만들어줘" | B. 자연어 위주 |
| "2-3장르 적당히 섞어줘 / 카오스하게" | C. 적당히 섞기 |
| "OO곡처럼" / "OO 1집 분위기" | D. 레퍼런스 우선 |
| "CREATE는 포크인데 COVER에서 하드락으로 갈래" | E. 장르 점프 |
| "Final Chorus 갑자기 키 올리자" / "여기 미분음" | F. 화성 변경 |
| "두 극단 융합 / 정반대 결 동시" | G. Polarity Fusion |
| "[캐릭터명]으로 / 시그니처 보컬 락" | H. Persona-locked |
| "빠르게 sketch / quick test" | I. ONE-SHOT 압축 |

**복합 패턴 OK**: D + E (레퍼런스 + 장르 점프), A + F (정통 70/30 + COVER 모듈레이션), G + B (Polarity Fusion + 자연어) 등.

### 3.5h CREATE/COVER 다양화 검증 체크리스트 (v2.4 신규)

각 패턴 출력 직전 자가 검증:

**모든 패턴 공통**:
- [ ] CREATE Style Box Dense 700-950자 / COVER Style Box Dense 700-950자 (둘 다, ≤950 / sketch면 250-350)
- [ ] 30% Rule 통과 (§3.5b)
- [ ] CREATE에 production/mix 언어 0개
- [ ] COVER에 melody 명시 0개
- [ ] 첫 80자 영향 윈도우 priority A 정보 (§23.3)
- [ ] CREATE 보컬 5요소 명시 (§3.5d)
- [ ] COVER 캐릭터 핸들 재주입 (§3.5d / Tip §11.5)

**패턴별 추가**:
- 패턴 A: 70/30 비율 명시되었는가?
- 패턴 B: 자연어 phrase가 장르 라벨보다 길게 들어갔는가?
- 패턴 E: Substitution Map (§3.5c) 적용?
- 패턴 F: COVER에 변경 위치 명시? (bar 5, Final Chorus 등)
- 패턴 G: Mashup 단계 명시? (CREATE + 2 Covers + Mashup workflow)

### 3.6 When CREATE/COVER is NOT Needed
- **Simple Mode quick sketch** (Section 4.1).
- **Persona-locked album work** where vocal identity is already fixed and only one prompt is needed per track.
- **Single-take experiments** where the user explicitly wants a one-shot.

---

## SECTION 4. ONE-SHOT MODE

### 4.1 Definition
A single Custom Mode generation where one prompt carries both the bone and the texture. Used when the user accepts that one of the two will be slightly compromised in exchange for speed and credit efficiency.

### 4.2 One-Shot Construction Rule
Compress the COVER prompt skeleton, but front-load the CREATE essentials:

Position 1-100 chars: [primary genre] + [vocal directive condensed] + [tempo] Position 100-400 chars: [instrumentation] + [structure clarity cue] + [key sub-genre tags] Position 400-800 chars: [production character] + [mix character] + [atmosphere] Position 800-950 chars: [texture seasoning] + [reference encoding if any] Position 950-1000 chars: SAFETY BUFFER — leave empty

### 4.3 One-Shot Trade-offs (Disclose to User)
- Higher chance of vocal-genre mismatch (engine may pick a vocal that fits the texture better than the directive).
- Less control over melody character.
- More re-rolls likely until a usable take emerges.
- Better for short tracks (≤2:30) than full-length productions.

### 4.4 Decision Rule
Use One-Shot when:
- User says "quick test," "sketch," "rough idea."
- Track length ≤ 2:00.
- User has limited credits.

Use CREATE/COVER pair when:
- User says "release-ready," "final version," "album track."
- The track must hit a specific reference sound.
- Vocal identity must be precise.

---

## SECTION 5. ARTIST REFERENCE ENCODING

### 5.1 The Problem
Direct artist names in the Style Box are flagged or blocked by Suno's filter to avoid name/likeness/voice misappropriation. Saying "in the style of [Artist]" or "[Artist]-inspired" triggers the same filter.

### 5.2 The Encoded Reference Format
Use the **descriptive surrogate** format:

[Adjective]-[Adjective] [genre] reminiscent of [decade/era] [scene/region], in the tradition of [scene name], with [specific signature element].

This communicates the target aesthetic without naming the artist.

### 5.3 The Decomposed Signature Method
Instead of naming an artist, list **what makes them sound like them**:

| Wanted Sound | Decomposed Encoding |
|---|---|
| Billie Eilish vibe | whispered female vocal close-mic'd, sub-bass forward, minimal percussion, dark bedroom-pop production, ASMR intimate texture |
| Tatsuro Yamashita city-pop | bright major-7 jazz harmony, slap bass, clean electric piano, polished 80s Tokyo studio production, brassy horn stabs, falsetto lead male vocal |
| Frank Ocean R&B | hazy alternative R&B, sparse drum programming, layered falsetto male vocal, lo-fi reverb-washed production, harmonic sophistication, melancholic texture |
| NewJeans 4th-gen K-pop | airy female group vocals in unison and thirds, light UK garage 2-step pulse, minimal warm synths, polished 2020s K-pop production, breezy nostalgic texture |
| Hans Zimmer cinematic | massive orchestral brass, ostinato string patterns, deep low-end percussion, sub-bass drone, epic film score production, wide stereo image |

The Decomposed Signature Method is the **default** for all professional output.

### 5.3b Direct Name Priority (v2.1 Override)

The Decomposed Signature Method (§5.3 above) remains the fallback,
but **direct artist names are tried first** when the operator
provides a reference. Many artist names pass Suno's filter and
produce strong results.

**Default procedure:**
1. Operator names an artist → use the name directly in Style Box.
2. If Suno blocks or distorts → fall back to Decomposed Signature.
3. Do NOT pre-emptively warn "we can't use that name." Let the
   filter speak first.

**Verified-passing names (operator's empirical findings):**
Mrs. GREEN APPLE, YOASOBI, Tatsuro Yamashita, MJ-style (Michael
Jackson), PinkPantheress era, Charli XCX Brat era.

**Higher-risk category:** Specific song titles are blocked more
often than artist names. For song-level reference, prefer
Decomposed Signature from the start.

This override is set by the system instruction (v2.1 §C-1).

### 5.4 Optional Surrogate Codes
Some operators use deliberately altered spellings (e.g., obfuscated artist names with numbers/symbols). This is a **gray-zone** practice. This system does **not** use it by default because:
1. It flirts with the spirit of Suno's TOS.
2. It produces less reliable results than the Decomposed Signature Method.
3. It complicates copyright posture if the output is monetized.

If the user explicitly requests it, deliver it with a written caveat. Otherwise, use Decomposed Signature.

### 5.5 Era and Scene Anchoring
Substitute specific years, decades, regions, and scenes for artist names:
- "1980s Tokyo city-pop scene" instead of [artist].
- "1970s Philadelphia soul" instead of [artist].
- "early 2010s Brooklyn indie" instead of [artist].
- "2020s K-pop 4th generation girl group" instead of [artist].
- "late-90s UK garage scene" instead of [artist].

This often works better than artist names anyway because Suno's training has strong era/scene clusters.

### 5.6 Song Title Surrogates
Same principle for song-level references:
- Instead of "[Song]-style" → describe the production: "hooky 4-on-the-floor anthem with stadium-sized synth chorus."
- Instead of [signature track] → describe the arrangement: "bossa-influenced verses with a horn-driven chorus."

---

## SECTION 6. HYBRID GENRE ENCODING

### 6.1 The Failure Mode
Listing two genres side-by-side ("trap and country") causes Suno to either pick one and ignore the other, or produce an unconvincing mush. Genre blending requires explicit ratios and zone assignment.

### 6.2 The 70/30 Ratio Rule
For most hybrids, the **primary genre takes ≥70%** of the prompt weight; the secondary genre is **applied to a specific zone** (instrument, section, or texture layer).

Primary genre [70%] with [secondary genre] elements applied to [specific zone], [primary genre full encoding], [secondary genre intrusion: specific instrument or section].

### 6.3 Zone Assignment Patterns

| Hybrid Type | Primary Zone | Secondary Zone |
|---|---|---|
| Genre-on-vocal | full track in Genre A | vocal delivery from Genre B |
| Genre-on-rhythm | full track in Genre A | drum pattern from Genre B |
| Genre-on-bass | full track in Genre A | bass tone/pattern from Genre B |
| Genre-on-section | verses in Genre A | chorus or bridge in Genre B |
| Genre-on-instrument | full track in Genre A | one signature instrument from Genre B (e.g., banjo in trap) |

### 6.4 Tempo Unification
When two genres have different default BPMs, pick one and force the other to fit. State the BPM explicitly. Example: trap (140) + bossa nova (120) → declare 130 BPM with trap rhythm and bossa harmony.

### 6.5 Frequency Separation
When two genres compete for the same frequency range (both heavy in low-end, both heavy in mids), assign one to a different range. Example: amapiano log-drum (low-mid) + neo-soul electric piano (mid) → push the piano up an octave or thin its body.

### 6.6 Hybrid Examples

**K-Pop × Trap (70/30)**:
Modern 4th-gen K-pop primary, 130 BPM, female group vocals in airy unison and thirds, polished 2020s K-pop production with crisp top-end, trap-influenced rhythm: 808 sub-bass, hi-hat triplet rolls, half-time feel in the second half of each chorus, minor-key topline with bright synth pads, clean radio-ready mix with wide stereo image.

**Country × Trap (70/30)**:
Modern country primary, 95 BPM with half-time trap feel underneath, acoustic guitar and pedal steel as harmonic foundation, narrative male vocal with subtle Southern accent, 808 sub-bass on the kick, hi-hat triplet rolls in transitions, organic-meets-programmed production, warm analog-tape mix character.

**Bossa Nova × Neo-Soul (70/30)**:
Modern bossa nova primary, 110 BPM, nylon-string guitar with João-Gilberto- style syncopated chord rhythm, soft brushed drums, walking upright bass, neo-soul harmonic vocabulary with extended chords, female alto vocal with intimate breathy timbre, vintage tube-warmth production, mid-forward mix with subtle plate reverb.

### 6.7 Three-Way Fusion
Avoid unless the user explicitly requests. If forced, use 60/25/15 ratio and assign each genre to a different layer (e.g., 60% genre on rhythm, 25% on harmony, 15% on texture).

---

## SECTION 7. TAG PRIORITY & ORDER REFERENCE

### 7.1 Style Box Order Template

[1. Primary genre + sub-style + era], [2. Tempo BPM + key/mode if needed], [3. Vocal directive: 5-element compact form], [4. Core instrumentation (3-5 instruments)], [5. Production character (era, format, processing)], [6. Mix character (stereo, dynamics, EQ tilt)], [7. Atmosphere/mood (2-4 adjectives)], [8. Optional reference encoding (Decomposed Signature)], [9. Optional texture seasoning].

### 7.2 Vocal Directive Compact Form
For inside the Style Box (full form lives in `06_VOCAL_PRODUCTION.md`):

[gender] [voice type] vocal, range [low-high], [2-3 timbre adjectives] timbre, [delivery] delivery, [language] [accent] [special technique if any]

Example:
female mezzo vocal, range G3-D5, smooth-warm-intimate timbre, behind-the-beat conversational delivery, English neutral accent with subtle melismatic ornaments.

### 7.3 Lyric Field Tag Order
(Expanded library in `10_SUNO_LYRICS_TAGS.md`.)

[Section tag with bar count — e.g., Verse 1 8] [Optional vocal direction tag — e.g., Singing: breathy, intimate] Lyric line one Lyric line two ...
[Next section tag] ...

Place vocal direction tags **immediately under** the section tag. Place ad-libs and harmony cues inline within the lyric where they occur.

### 7.4 Negative Prompt (Exclude Styles) Use
The Exclude Styles field is short (~200 chars) but powerful. Use to remove:
- Unwanted vocal characteristics ("auto-tune, vocoder, child voice").
- Unwanted instruments ("orchestra, electric guitar solo").
- Unwanted production traits ("muddy mix, lo-fi compression, hiss").
- Unwanted genre drift ("country twang, EDM drop, metal scream").

Order in Exclude: most-likely drifts first.

---

## SECTION 8. RE-TOKENIZATION AVOIDANCE

### 8.1 The Counting Protocol
Before any prompt is delivered to the user:
1. Compute character count of Style Box.
2. If ≥ 950, trigger truncation review.
3. Identify lowest-priority tags (texture seasoning, optional references).
4. Cut from the back until count ≤ 950.
5. Re-verify count.

This system **never** delivers a prompt over 950 characters in the Style Box. The 50-character buffer absorbs Suno UI quirks and any user paste-time additions.

### 8.2 Compression Techniques (when over limit)
In priority order — apply until under 950:
1. Drop trailing texture adjectives.
2. Merge adjacent adjectives ("warm and analog" → "warm-analog").
3. Drop redundant era qualifiers.
4. Compress instrumentation lists (drop 4th and 5th instruments).
5. Drop one of the production character clauses.
6. Drop the reference encoding (move to user-level explanation outside the prompt).

Never compress: primary genre, vocal directive, tempo, key.

### 8.3 Re-Tokenization Symptoms (Diagnosing a Bad Output)
If a generation produces an output that ignores half the prompt:
- Check character count first. If over ~1,000, the back half was truncated.
- Check tag order. If the genre anchor is buried past character 80, re-front-load.
- Check for forbidden characters (square brackets in Style Box). Remove and regenerate.
- Check for negative-language drift ("not too heavy"). Suno often ignores negation inside the Style Box; move negatives to the Exclude Styles field.

---

## SECTION 9. THE PROMPT-LOCKING TECHNIQUES

### 9.1 Identity Anchor at Position 1
The first 4-7 words must contain the **non-negotiable identity** of the track. Order:
1. Primary genre (1-2 words).
2. Sub-style or era (1-2 words).
3. BPM declaration if structurally critical.

Example anchor: `Modern 4th-gen K-pop, 130 BPM, ...`

### 9.2 The Repeat-for-Emphasis Technique
For any element that **must** survive the generation, mention it twice in the prompt — once early, once late. Example: if a Korean female vocal is critical:

... female Korean vocal, ... [middle] ... Korean lead vocal preserved.

The double-mention significantly raises retention through re-rolls.

### 9.3 Persona-Locked Workflow
For album/series work:
1. Build Persona once (vocal identity + base style).
2. Use Custom Mode + Persona for every track.
3. Style Box per track focuses only on what differs (tempo, mood, instrumentation).
4. Lyrics field carries structure tags and lyric content.

This produces the most consistent multi-track output Suno can deliver.

### 9.4 The Reference-Take Lock
Once a CREATE generation produces a usable take:
1. Save it as a Persona (vocal-cloned).
2. Or use it as the source for Cover Mode (preserves melody).
3. Future iterations build off this locked source rather than generating from scratch.

---

## SECTION 10. NEGATIVE-LANGUAGE HANDLING

### 10.1 The Rule
Do **not** put negations in the Style Box. Suno frequently parses negations as **inclusions** of the negated thing. Examples that backfire:
- "not too heavy" → produces heavy.
- "no auto-tune" → produces auto-tune.
- "without electric guitar" → produces electric guitar.

### 10.2 The Fix
Move all negations to the **Exclude Styles** field. State them as positive nouns:
- Style Box: focus only on what you want.
- Exclude Styles: `auto-tune, electric guitar, heavy distortion`.

### 10.3 Reframing Examples
| Wrong (Style Box) | Right (Style Box + Exclude) |
|---|---|
| "not aggressive" | Style: "gentle, intimate" / Exclude: "aggressive, distorted" |
| "no rap" | Style: "sung melodic verses" / Exclude: "rap, spoken word" |
| "without orchestra" | Style: "small ensemble, intimate" / Exclude: "orchestra, strings section" |

---

## SECTION 11. THE PRE-GENERATION GATE (10 CHECKS)

Before any prompt is delivered, all 10 must pass:

1. **Character count** — Style Box ≤ 950 chars. Lyrics field ≤ 4,800 chars.
2. **No forbidden characters** — no `[ ]` in Style Box; no extra newlines.
3. **Front-loaded anchor** — primary genre in first 4-7 words.
4. **Vocal directive complete** — gender, voice type, range, timbre, delivery, language all present (in CREATE) or covered by Persona (in COVER).
5. **Tempo declared** — BPM stated explicitly when structurally important.
6. **Structure tags valid** — `[Section]` tags in Lyrics field use approved syntax (`10_SUNO_LYRICS_TAGS.md`).
7. **Vocal direction cues** — `[Singing: ...]` or equivalent placed where needed.
8. **Reference encoding compliant** — direct artist name used when operator provides reference (try first per §5.3b). Decomposed Signature applied only as fallback when filter blocks. Song titles default to Decomposed. 
9. **Negations relocated** — all negative language moved to Exclude Styles field.
10. **Format integrity** — output formatted as `--- CREATE PROMPT ---` and `--- COVER PROMPT ---` (or `--- ONE-SHOT PROMPT ---`) with Style Box and Lyrics Box clearly labeled.

A prompt that fails any check is fixed before delivery, never delivered as-is with a warning.

---

## SECTION 12. OUTPUT FORMAT (MANDATORY)

Every Suno prompt the system delivers uses this exact structure:

12.1 CREATE/COVER Pair Format
--- CREATE PROMPT ---

[STYLE BOX] (count: NNN/1000)
<style box content>

[LYRICS BOX]
<lyrics with section and direction tags>

[EXCLUDE STYLES]
<exclude content>

[NOTES]
<brief generation notes for the user>


--- COVER PROMPT ---

[STYLE BOX] (count: NNN/1000)
<style box content>

[LYRICS BOX]
(preserved from CREATE — no changes needed)

[EXCLUDE STYLES]
<exclude content>

[NOTES]
<brief notes on what changes between CREATE and COVER>
12.2 One-Shot Format
--- ONE-SHOT PROMPT ---

[STYLE BOX] (count: NNN/1000)
<style box content>

[LYRICS BOX]
<lyrics with section and direction tags>

[EXCLUDE STYLES]
<exclude content>

[NOTES]
<brief notes>
12.3 Always Include the Character Count
The (count: NNN/1000) annotation is mandatory. It serves two purposes:
1.	Proves the gate was passed.
2.	Lets the user verify after pasting (catches paste-time mutations).
________________________________________
SECTION 13. COMMON FAILURES & FIXES
Symptom	Likely Cause	Fix
Wrong genre delivered	genre anchor buried past char 80	front-load primary genre
Wrong vocal gender/range	vocal directive too late or missing	move vocal block to position 3, repeat at end
Auto-tune appears unwanted	negation in Style Box	move "auto-tune" to Exclude Styles
Section structure ignored	tags malformed or missing bar counts	use [Verse 1 8] format with bar count
Output sounds generic	no era/scene anchor	add "1980s Tokyo city-pop scene" or equivalent
Output drifts from reference	direct artist name was filtered	apply Decomposed Signature Method
First take great, second take random	no Persona or Cover lock	save take as Persona; iterate via Cover
Style Box truncated mid-sentence	over 1,000 chars	run compression protocol (Section 8.2)
Hybrid genre comes out as one genre only	genres listed without ratio/zone	apply 70/30 with zone assignment
Pronunciation wrong on key word	no override tag	add bracket pronunciation in Lyrics: word [PRO-noun-see-AY-shun]
Korean lyric sung with English accent	language not declared in vocal directive	add "Korean lead vocal, native pronunciation"
High note breaks/strains	closed vowel on sustained note	rewrite that line; see 08_LYRIC_CRAFT_ENGLISH.md § 8.4
________________________________________
SECTION 14. WORKFLOW SUMMARY
USER REQUEST
   │
   ▼
PHASE 0 — Strategic Blueprint (01_OPERATING_RULES.md)
   │
   ▼
LOAD relevant knowledge files (genre, harmony, lyric, vocal)
   │
   ▼
DECIDE MODE:
   │
   ├── Quick sketch?  → ONE-SHOT
   │
   ├── Album / release-ready?  → CREATE/COVER PAIR
   │
   └── Multi-track series?  → PERSONA + CUSTOM
   │
   ▼
CONSTRUCT prompt per Section 7 order template
   │
   ▼
CHARACTER COUNT (Section 8.1)
   │
   ▼
PRE-GENERATION GATE (10 checks, Section 11)
   │
   ▼
DELIVER in mandatory format (Section 12) with count annotation
   │
   ▼
USER GENERATES → review → refine via Cover, Extend, or re-roll
________________________________________
SECTION 15. REFERENCES
Suno official:
•	Suno blog — Introducing Covers (suno.com/blog/covers)
•	Suno blog — Personas updates
•	Suno help center — character limits, mode descriptions
Community-validated guides:
•	r/SunoAI — v5.5 master prompt threads
•	HookGenius — character limits and settings guides
•	JackRighteous — Personas and Covers guides
•	TagASong — meta tag library
•	Hooktheory — chord-melody analysis (for Cover prompt construction)
•	Berklee Online — songwriting and production fundamentals
Academic / reverse-engineering:
•	Tokenization and weighting analyses circulated in r/SunoAI
•	Genre fusion methodology references (SunoMV, Medium guides)
•	Persona system advanced threads
________________________________________
SECTION 16. RELATED FILES
•	10_SUNO_LYRICS_TAGS.md — complete bracket tag library (section tags, vocal direction tags, ad-libs, harmonies).
•	12_PROMPT_TEMPLATES.md — copy-paste skeletons for CREATE/COVER, One-Shot, Persona workflows, plus diagnostic decision tree.
•	06_VOCAL_PRODUCTION.md — full vocal directive system (referenced in compact form here).
•	05_GENRE_LIBRARY.md — per-genre Style Box recipes.
•	01_OPERATING_RULES.md — overall workflow and gate enforcement.
________________________________________

## SECTION 13. (Reserved — Reference Anchor)

이 슬롯은 v2.4 정비 시점 미사용. 향후 추가 어법 슬롯으로 보존.

레퍼런스 어법 관련 콘텐츠는 다음 위치 참조:
- §5 Artist Reference Encoding (Decomposed Signature)
- §21 레퍼런스 표기법 강화 (v2.2 신규)
- `13_REFERENCE_ANALYSIS.md` Reference Digging Protocol

## SECTION 14. (Reserved — Vocal Anchor)

이 슬롯은 v2.4 정비 시점 미사용.

보컬 관련 콘텐츠는 다음 위치 참조:
- §3.5d 보컬 디렉션 분배표 (v2.4 신규)
- §7.2 Vocal Directive Compact Form
- `06_VOCAL_PRODUCTION.md`
- `15_NATURAL_LANGUAGE_DIRECTION.md` §4 Vocal Protection Keywords
- `99_OPERATOR_VAULT.md` Part F (검증 키워드 라이브러리) — 보컬 딜리버리

## SECTION 15. (Reserved — Genre Anchor)

이 슬롯은 v2.4 정비 시점 미사용.

장르 / 하이브리드 관련 콘텐츠는 다음 위치 참조:
- §6 Hybrid Genre Encoding
- §3.5g CREATE/COVER 다양화 패턴 (v2.4 신규)
- `05_GENRE_LIBRARY.md`
- `99_OPERATOR_VAULT.md` Part F — 검증된 하이브리드 장르

## SECTION 16. (Reserved — Effects Anchor)

이 슬롯은 v2.4 정비 시점 미사용.

이펙터 / 사운드 처리 관련 콘텐츠는 다음 위치 참조:
- §23 함축 압축 SOP (v2.3 신규)
- `16_INSTRUMENT_ARTICULATION.md` §17 Effects Processing Bank
- `16_INSTRUMENT_ARTICULATION.md` §18 CREATE/COVER 분배 결정 트리
- `15_NATURAL_LANGUAGE_DIRECTION.md` §19 Effects Direction Bank

________________________________________

## SECTION 17 — V5.5 최신 변경사항 (2026-03-26 기준)
## (NEW v2.2 / 회의록 직격 보강)

이 섹션은 Suno v5.5의 2026년 3월 26일 출시 이후 변경사항과
그 이전 버전 대비 차이점을 정리. 우리 워크플로우(프롬프트
출력까지)에 영향을 주는 항목만 등록.

### 17.1 v5.5 출시 (2026-03-26)

**핵심 변경사항** (Blake Crosley 가이드, Suno 공식 문서 검증):

1. **Voice Cloning** — 자기 목소리를 학습시켜 generation에 사용.
   인증 절차 필요 (목소리 소유권 확인). Pro/Premier 전용.
   - Create 메뉴에서 "Voices" 버튼이 기존 "Personas" 버튼을 대체
   - Style Personas는 Voices 메뉴 안에서 계속 접근 가능

2. **Custom Models** — 자기 라이브러리 곡 6개 이상으로 v5.5의
   개인화된 변형 모델을 최대 3개까지 학습 가능.
   - 학습 데이터가 스타일적으로 일관될수록 좋음
   - 장르 섞으면 학습 노이즈 발생
   - 한 번 학습하면 prompt 정밀도 낮아도 일관된 결과
   - Pro/Premier 전용

3. **My Taste** — 모든 사용자에게 제공되는 적응형 선호 시스템.
   - Generation history, likes, interactions를 학습
   - 미래 generation을 사용자 선호 스타일로 편향
   - Style 입력 옆 magic wand 아이콘으로 트리거
   - 명시적 prompt나 slider 설정을 override하지는 않음

4. **8분 단일 generation** (V4.5에서 도입, V5.5도 유지)

5. **Studio 1.2** (2026-02 업데이트, Premier 전용)
   - Warp markers + quantize: 개별 노트/phrase 타이밍 미세 조정
   - 우리 워크플로우 범위 외 (오빠 지시 사항)

### 17.2 우리 워크플로우 영향도

**적용 범위**:
- ✅ Voices/Personas: 99의 캐릭터 베이스라인 시스템과 결합 가능
- ✅ Custom Models: 향후 Limganzi 시그니처 학습 모델 후보 (장기)
- ⚠️ My Taste: 자동 편향이라 우리 prompt 정밀 제어와 충돌 가능
  → **My Taste 끄기 권장** (명시적 prompt 우선)
- ❌ Studio: 범위 외

**워크플로우 변경 없음**: CREATE/COVER 페어 전략 유지.
출력까지가 우리 범위.

### 17.3 모델 버전 타임라인 (참고용)

| 버전 | 출시 | 핵심 변화 |
|------|------|----------|
| V4 | 2024-11-19 | 4분 generation, multilingual, Covers, 2-stem |
| V4.5 | 2025-05-01 | 8분 generation, Creative Sliders, Prompt Helper |
| V4.5-All | 2025 후반 | Free tier 모델 |
| V5 | 2025-09 | Studio-grade audio, Suno Studio DAW, 12-stem |
| V5.5 | 2026-03-26 | Voice Cloning, Custom Models, My Taste |

내부 코드네임: V5/V5.5 = "chirp-crow"

### 17.4 우리 시스템 타겟 명시

**현재 타겟**: Suno v5.5 (2026-03-26 출시 기준)
**호환**: v5도 동작 (Custom Models / Voice Cloning 기능만 차이)

향후 v6.x 출시 시 09 파일 §17 섹션에 변경사항 추가.

---

## SECTION 18 — Style Box Character Limit 명확화 (NEW v2.2)

회의록 트리거: 외부 자료(HookGenius)는 200자라고 하는데
우리는 850-950자로 운영. 이 충돌 해소 + 명확한 운영 룰 정의.

### 18.1 두 한도의 본질

**Hard Limit (기술적 max)**:
- Style Box: 1,000자
- 1,000자 초과 시 silent truncation
- 1,000자 안에 들어가면 입력 자체는 받음

**Effective Influence Window (실효 영향력)**:
- 첫 60-80자: 약 60% 가중치
- 80-300자: 약 30%
- 300-1,000자: 약 10% (fine-tuning seasoning)

이는 모순 아님. **둘 다 사실**:
- 1,000자가 기술적 한계
- 200자가 "decisive 영향력 sweet spot"

### 18.2 우리 시스템의 850-950자 운영 근거

**왜 200자 sweet spot이 아니라 850-950을 쓰는가**:

1. **Front-loading 전략 + Texture seasoning 동시 활용**:
   - 첫 80자: 결정적 정체성 (장르·BPM·키·보컬 코어)
   - 80-300자: 핵심 어법 (코드 진행·악기 hierarchy·시그니처 모먼트)
   - 300-700자: 디테일 (frequency architecture·stereo·dynamics)
   - 700-900자: 후반 reinforcement (throughout 키워드·anti-drift)
   - 900-950자: 안전 buffer (50자)

2. **Throughout Discipline 보강용 공간**:
   - "X architecture maintained throughout all sections" 같은
     후반 일관성 강제 키워드는 후반 50-100자에서 작동
   - 200자 압축에서는 이 보강 못 함 → 후반 드리프트 발생

3. **Decomposed Signature 표현 공간**:
   - 직접 아티스트 이름 안 쓰고 결을 묘사하면 50-150자 추가 필요
   - 200자 안에서는 "장르명만" 가능, 결 표현 불가

### 18.3 운영 룰 (확정)

**CREATE Style Box: Dense 700-950자 (sketch/다양성 우선 시만 Tight 250-350)**
- 첫 80자: 장르 anchor(마이크로+시대) + BPM + 키/mode + 보컬 코어
- 80-300자: 섹션별 코드 진행(비다이어토닉 명시) + 핵심 악기 3-4개(디스크립터 부착)
- 300-550자: 멜로디 컨투어(3층) + 구조 + 에너지 아크 + 시그니처 moments
- 550-800자: 보컬 5-element 확장(거동/굴절) + protection 키워드(필요시)
- 800-950자: 잔여 시그니처/뉘앙스 압축
- 프로덕션/믹스 언어 금지 (그건 COVER로). 8항목 다 박으면 자연히 이 분량.
  638자 같은 부실 = 누락 신호이지 "얇은 게 정상"이 아님 (§2 CREATE Density).

**COVER Style Box: Dense 700-950자 (≤950 안전)**
- 첫 80자: 장르 anchor + BPM + 키 (CREATE와 일치)
- 80-300자: era anchor + Decomposed Signature
- 300-600자: 풀 instrumentation + frequency architecture +
  stereo image
- 600-800자: mix character + texture seasoning + signature moments
- 800-900자: throughout 키워드 + LUFS 타겟
- 900-950자: 마지막 anti-drift reinforcement
- 950 초과 시 §8.2 압축 프로토콜 발동

**ONE-SHOT Style Box: 850-950자**
- COVER 압축 형태
- 보컬 정보를 첫 80자에 압축 포함

### 18.4 200-자 어법과의 호환성

가벼운 sketch / Simple Mode 작업 시 200자 어법 사용 가능.
이때 우선순위:
1. 장르 (1-2단어)
2. 보컬 방향
3. 핵심 무드 (1-2)
4. 핵심 악기 1-2개
5. BPM
6. 프로덕션 quality

이 모드는 우리 메인 워크플로우 아님 — 회의록 답변/빠른 실험용.

### 18.5 Lyrics Box 한도 + 곡 길이 매트릭스 (v2.10 갱신)

#### 18.5.1 Hard 한도

- **Hard limit**: 5,000자 (Suno v5.5 공식)
- **Over-cued 임계**: 4,800자 이상 = 후반 가사 씹힘 위험 (Case 25 검증)
- **Under-cued 임계**: 2,500자 미만 = 보컬 러싱 위험 (예외: 의도적 미니멀)

#### 18.5.2 곡 길이 → 가사 분량 매트릭스 (v2.10)

곡 컨셉·복잡도에 따라 매트릭스로 결정. 일률 강제 X.

| 곡 길이 (예상) | Lyrics Box 권장 분량 | 사용 케이스 |
|---|---|---|
| 2:00-2:30 (sketch) | 2,000-2,800자 | 빠른 데모 / 짧은 인터루드 |
| 2:30-3:00 (짧은 곡) | 2,800-3,300자 | 미니 발라드 / sketch 본 |
| **3:00-3:30 (기본 default)** | **3,000-3,800자** | **표준 K-pop/indie/ballad** |
| 3:30-4:00 (풍성) | 3,500-4,500자 | 정교한 작사 곡 / 마당놀이 / 사설조 |
| 4:00-4:30 (대형) | 4,200-4,800자 | 서사 곡 / 듀엣 / Bridge 확장 곡 |

#### 18.5.3 핵심 원칙 (v2.10)

**분량 ≠ 최저 목표.** 곡 컨셉에 필요한 만큼이 1순위.
- 같은 3:30 곡이어도, 미니멀 발라드는 3,000자 / 사설조는 4,500자
- 시스템이 곡 컨셉 보고 분량 추정 → 00 §C-39 Pre-Production Estimate에
  포함 → 운영자 확인

#### 18.5.4 분량별 디렉션 밀도 가이드

| 분량 zone | 디렉션 밀도 | 어떻게 |
|---|---|---|
| 2,000-2,800자 | 가벼움 | 섹션 태그 + 1 [Singing:] / 섹션 |
| 2,800-3,500자 | 표준 | 섹션 태그 + [Singing:] + 마이크로큐 일부 |
| 3,500-4,500자 | 풍성 | 섹션 태그 + [Singing:] 2개/12바+ 섹션 + 마이크로큐 풀 |
| 4,500-4,800자 | 정교 | 마이크로큐 풀 + 강세 / 호흡 / 레이어링 디테일 |

**디렉션 많을수록 좋은 건 아니다.** 곡 결에 맞는 밀도가 1순위.
모든 섹션에 마이크로큐 도배 시 → 보컬 답답함 + 후반 씹힘.

#### 18.5.5 v2.10 운영 (00 §C-3.1 단일 진실)

이전 09 v2.7 README "Lyrics 2,000-3,500자" vs 09 §18.5 v2.7 "3,500-4,500자"
충돌 해소. v2.10 매트릭스가 단일 진실.

다른 .md 파일 (01 Gate 5 / 15 §1 등)이 "3:30+ 트랙 3,500-4,500자" 등으로
표기 시 v2.10 매트릭스의 *3:30-4:00 행*으로 해석.

### 18.6 Title 한도

- **Hard limit**: 80자 (외부 자료 검증)
- 음악적 출력에 영향 거의 없음
- 정리·검색용

---

## SECTION 19 — Parameterized Metatags (NEW v2.2 — 검증된 신규 어법)

Blake Crosley 가이드와 Reddit 검증 자료에서 확인된 v5.5 신규
실용 어법. Lyrics Box 안에서 섹션별 정밀 제어 가능.

### 19.1 기본 구문

```
[Section: modifier1, modifier2, modifier3]
가사 라인...
```

콜론 + 콤마 분리 modifier로 섹션 단위 제어.
Style Box 변경 없이 특정 섹션만 다른 캐릭터로.

### 19.2 검증된 사용 예시

**섹션별 보컬·악기 동시 제어**:
```
[Verse: whispered vocals, acoustic guitar only]
Walking through the morning mist
The world still sleeping, still

[Chorus: full band, powerful vocals, cymbal crashes]
But I'm awake, I'm alive
And every sound is a sign

[Bridge: stripped down, piano only, vulnerable vocals]
And in the quiet after the storm
```

**섹션별 다이내믹 제어**:
```
[Verse 1: sparse, intimate close-mic, 30% energy]
[Pre-Chorus: building intensity, layers entering]
[Chorus: full production, soaring vocals, 90% energy]
[Bridge: dropped to piano only, vulnerable, 40% energy]
[Final Chorus: explosive, key change up half-step, 100% energy]
```

**섹션별 디튠·미분음 색채** (회의록 직접 적용):
```
[Verse: standard tuning, dry close-mic vocal]
[Chorus: doubled lead +12 cent detune, organic warmth]
[Bridge: chromatic mediant accent, subtle quarter-tone color
on lead synth only]
[Final Chorus: triple-tracked vocals with ±10 cent detune width]
```

### 19.3 Vertical Bar 표기 (Reddit 검증)

콤마 대신 vertical bar 사용 시 더 명확한 파싱:

```
[Verse: whispered vocals | acoustic guitar only | dry close-mic]
[Chorus: full band | powerful vocals | wide stereo]
```

콤마 vs bar 선택:
- **콤마**: 표준, 가장 호환성 높음
- **Bar**: 명확한 구분 필요할 때 (긴 modifier 리스트)

둘 다 작동. 케이스별 선호.

### 19.4 우리 시스템 통합

**기존 [Singing: ...] cue와의 관계**:
- `[Verse]` + `[Singing: breathy intimate]` (기존 어법) → 분리된 두 줄
- `[Verse: whispered vocals]` (parameterized) → 통합 한 줄

**권장 사용**:
- 보컬 디렉션만 → `[Singing: ...]` (기존)
- 보컬 + 악기/다이내믹 동시 → `[Section: ...]` (parameterized)
- 두 어법 동시 사용 가능:
  ```
  [Verse: acoustic guitar only, sparse drums]
  [Singing: breathy intimate close-mic, behind-beat phrasing]
  가사...
  ```

### 19.5 검증된 효과적 modifier 카테고리

**Production**:
- "full band" / "stripped down" / "minimal production"
- "lo-fi production" / "polished production"
- "ambient pads" / "reversed guitar"
- "tape saturation" / "vinyl warmth"

**Vocals**:
- "whispered vocals" / "powerful vocals" / "soaring vocals"
- "vulnerable vocals" / "intimate close-mic"
- "doubled lead" / "harmonized" / "choir backing"

**Instruments**:
- "acoustic guitar only" / "piano only" / "synth pad only"
- "no drums" (섹션 단위는 작동, Style Box에서는 부정형 회피)
- "808 bass dropout" / "kick on beat 1 only"

**Dynamics**:
- "30% energy" / "90% energy"
- "soft" / "medium" / "loud" / "explosive"
- "fade in" / "fade out" / "crescendo"

**Production FX**:
- "reverb-heavy" / "dry" / "plate reverb 25% wet"
- "wide stereo" / "narrow centered"
- "slap-back delay" / "tape echo"

### 19.6 Parameterized Metatag 사용 결정 트리

```
섹션 단위 제어 필요?
   │
   ├── 보컬만 변화? → [Singing: ...] (기존 어법)
   │
   ├── 악기 진입/이탈? → [Section: instrument changes]
   │
   ├── 다이내믹 변화? → [Section: dynamics]
   │
   └── 복합 변화? → [Section: vocals + instruments + dynamics]
        + 보컬은 세분화 필요시 [Singing: ...] 추가
```

---

## SECTION 20 — Exclude Styles 활용법 강화 (NEW v2.2)

회의록 트리거: "Exclude (네거티브) - 이것도 활용해야할 땐
잘 활용하게."

09 §10 (Negative-Language Handling)의 보강. Exclude Styles는
Style Box보다 짧지만(~200자) 강력한 도구.

### 20.1 Exclude Styles 작동 원리

**작동 방식**:
- 짧은 콤마 분리 키워드 리스트
- Style Box의 부정형을 대체
- "이것이 출력되면 안 된다"는 강한 신호

**길이**: 약 200자 (콤마 포함)
- 콤마 분리 8-15개 항목이 sweet spot
- 너무 많으면 Suno 혼란, 너무 적으면 무력

**위치**: Suno UI의 별도 필드 (Style Box와 분리)

### 20.2 카테고리별 Exclude 키워드 라이브러리

**보컬 드리프트 방지**:
```
auto-tune T-Pain heavy, vocoder, robotic vocal,
accented Korean robotic, foreign-accented Korean diction,
child voice, screaming vocals, growled vocals
```

**아레나/군중 환각 차단** (검증된 트리거):
```
stadium reverb, live audience, crowd cheering,
arena ambience, stadium sound, concert atmosphere
```

**프로덕션 드리프트**:
```
muddy mix, lo-fi compression artifacts, distorted vocals,
crushed dynamics, over-compressed master, peaking distortion
```

**장르 드리프트** (의도하지 않은 장르 인입 방지):
```
country twang, EDM drop, metal scream, K-pop chorus belt,
generic K-pop production, big-room EDM,
festival sound, dubstep wobble
```

**악기 드리프트**:
```
orchestra, electric guitar solo, brass section,
banjo, accordion, harmonica, tuba
```

**시대 드리프트**:
```
1990s production, 1980s gated reverb, vintage tape hiss,
old-school sound, dated production
```

**Latin Percussion 트리거 차단** (Case 19 검증):
```
conga, bongo, cowbell, clave, Latin percussion, reggae,
dancehall, Afrobeat, Caribbean rhythm
```

**의성어 / 잘못된 ad-lib 차단**:
```
vocalized onomatopoeia, spoken bam syllables,
shouted ad-libs, scatting, beatboxing
```

### 20.3 곡 컨셉별 Exclude 템플릿

**Modern K-pop (NewJeans / ILLIT 결)**:
```
auto-tune heavy, K-pop chorus belt, big-room EDM drop,
generic idol backing, distorted guitar, crowd cheering,
stadium reverb, vintage 80s gated reverb
```

**Indie Folk Intimate**:
```
electronic drums, auto-tune, EDM, polished radio-pop,
aggressive bass, festival sound, generic K-pop production,
crowd cheering, stadium reverb, distorted guitar
```

**Hip-Hop / Trap**:
```
acoustic guitar, country twang, orchestral strings,
jazz harmony, generic boom-bap, K-pop production,
crowd cheering, sing-rap melodic
```

**Modern Club / Vogue Ballroom (Case 24 결)**:
```
auto-tune heavy, big-room EDM drop, generic idol backing,
country twang, metal scream, crowd cheering,
stadium reverb, distorted guitar, accented Korean robotic
```

**Cinematic Ballad**:
```
electronic drums, distorted guitar, auto-tune,
modern compressed loudness, EDM drop, generic K-pop production,
crowd cheering, stadium ambience, hyperpop glitch
```

**Microtonal / Experimental** (NEW v2.2):
```
standard equal temperament rigid, polished pop production,
auto-tune correction, K-pop chorus belt, EDM drop,
generic radio-pop, modern compressed loudness
```

### 20.4 Exclude 디버깅 — 작동 안 할 때

**Symptom A**: "Auto-tune 빼라고 했는데 나옴"
- 원인: Style Box에 "polished modern" 같은 auto-tune 트리거
  키워드 잔존
- 처방: Style Box 검토 → "auto-tune"과 결합되는 키워드 제거
  ("polished" → "natural human texture" 등)

**Symptom B**: "Crowd cheering 계속 들림"
- 원인: Style Box의 "stadium" / "live" / "concert" 키워드
- 처방: Style Box 정화 + Exclude 강화
  → "studio recording clean isolated" Style Box 추가

**Symptom C**: "K-pop 아닌데 K-pop 결로 빠짐"
- 원인: "Korean" 키워드 자체가 K-pop 트리거
- 처방: 명확한 대안 제시
  - Style Box: "Korean indie polished bedroom feel"
  - Exclude: "K-pop, idol, generic K-pop chorus belt"

**Symptom D**: "Exclude 키워드 너무 많아서 결과가 흐릿함"
- 원인: 15개 초과 시 Suno 혼란 발생
- 처방: 우선순위 재배치
  - Top 5 핵심 anti-drift만 유지
  - 나머지는 Style Box positive 키워드로 우회

### 20.5 Exclude 작성 체크리스트

곡 출력 전 Exclude 검증:
- [ ] 8-15개 항목 안에 들어가는가?
- [ ] 콤마 분리 표기 정확한가?
- [ ] Style Box positive 키워드와 충돌 없는가?
- [ ] 99_OPERATOR_VAULT Part F default anti-drift 묶음 포함했는가?
- [ ] 곡 장르별 특이 anti-drift (Latin Percussion 등) 포함?
- [ ] 케이스에서 발견된 트리거 (예: "stadium" → 군중) 포함?

---

## SECTION 21 — 레퍼런스 표기법 강화 (NEW v2.2 / 회의록 직격)

회의록 답변 직접 반영: "한국 아이돌이면 한글표기(영문표기)_노래
제목 이렇게 적고 각국의 레퍼런스면 그 국가의 아이돌명 표기()
또는 그 그룹에 보컬명도 함께 표기_노래제목 등등으로 직접 표기할
수 있게 해서 일부가 필터링에 걸려도 잘 포함되게."

09 §5.3b의 "Direct Name Priority" 보강. Case 28 (Look At Me)
검증 자료 통합.

### 21.1 핵심 원칙

**Priority Order** (시도 순서):
1. **직접 표기 우선 시도** (필터 통과 사례 다수)
2. 차단 시 → 다중 표기로 재시도
3. 여전히 차단 시 → Decomposed Signature 폴백
4. 곡 제목은 Decomposed 우선 (필터 리스크 더 높음)

### 21.2 국가별 표기 형식 (확정)

**한국 아티스트**:
```
형식: 한글명(영문명) 또는 영문명(한글명)
예: NewJeans(뉴진스) / 아이브(IVE) / 아일릿(ILLIT)
   Mrs. GREEN APPLE 같은 영문 그룹은 그대로
   솔로: 로제(ROSÉ) / 카리나(Karina)
```

**일본 아티스트**:
```
형식: 한자명(로마자) 또는 가타카나(로마자)
예: ヨルシカ(Yorushika) / Aimer(エメ) / 藤井 風(Fujii Kaze)
   Mrs. GREEN APPLE 같은 영문 그룹은 그대로
   YOASOBI(요아소비) / ado(아도)
```

**서양 아티스트**:
```
형식: 영문명 단독 (가장 안전)
필요 시: 영문명(국가/시대 anchor)
예: Charli XCX / Chappell Roan
   Charli XCX(2024 Brat era)
   Sabrina Carpenter(2024 Short n' Sweet era)
```

**중국/대만 아티스트**:
```
형식: 한자명(로마자/영문)
예: 周杰倫(Jay Chou) / 蔡依林(Jolin Tsai)
```

**라틴 아티스트**:
```
형식: 영문명 단독 (스페인어 이름은 그대로)
예: Bad Bunny / Karol G / Rosalía / Peso Pluma
```

### 21.3 보컬리스트 명시 (그룹 곡에서 특정 보컬 색)

**한국 그룹 + 특정 멤버**:
```
형식: 그룹명(영문) + 멤버명(한글/영문)
예: NewJeans 민지(Minji) / aespa 카리나(Karina)
   NewJeans Hanni(하니) / IVE Wonyoung(원영)
```

**효과**: 멤버별 보컬 톤 차이를 Suno에게 직접 전달.
민지 = 낮은 톤 / 하니 = 명료하고 투명 / 다니엘 = 허스키 미음

**일본 솔로 / 그룹**:
```
예: YOASOBI 이쿠라(ikura)
   Mrs. GREEN APPLE 大森元貴(Motoki Omori)
```

### 21.4 곡 제목 표기 (다중 안전망)

곡 제목은 아티스트명보다 필터 리스크 높음.

**Tier 1 (시도 가치)**:
```
"NewJeans-style 'Hype Boy' breezy UKG 2-step"
"aespa Whiplash strut groove"
```

**Tier 2 (Decomposed 권장)**:
```
"NewJeans Get Up era polished K-indie crossover"
"aespa MY WORLD era cyberpunk K-pop"
```

**Tier 3 (Era + 결만)**:
```
"2024 4th-gen K-pop polished crossover, breezy UKG influence"
"2024 K-pop SM Entertainment cyberpunk strut"
```

### 21.5 다중 표기로 필터 통과율 올리기

**전략**: 같은 레퍼런스를 여러 표기로 분산.

**예시 (NewJeans 결 추구)**:
```
"NewJeans(뉴진스)-style polished K-indie crossover,
4th-gen HYBE girl group bright airy unison,
breezy 2024 Korean pop production"
```

3중 보강:
1. 직접 명 (필터 통과 시 직격)
2. 회사 + 세대 anchor (대안)
3. 시대 + 결 (Decomposed 폴백)

하나가 차단돼도 나머지 2개가 결을 잡아줌.

### 21.6 검증된 통과 아티스트 목록 (2026-05 기준)

**한국**:
- NewJeans, IVE, LE SSERAFIM, ILLIT, BABYMONSTER, aespa
- Mrs. GREEN APPLE (한국 아닌데 한국 K-pop 결로 자주 언급)

**일본**:
- Mrs. GREEN APPLE, YOASOBI, Tatsuro Yamashita
- ヨルシカ(Yorushika), 藤井 風(Fujii Kaze), Aimer
- Ado (single name 안전)

**서양**:
- Charli XCX (Brat era 명시 시 강함)
- Sabrina Carpenter, Chappell Roan, Olivia Rodrigo
- The Weeknd, Lana Del Rey
- Tame Impala, Bon Iver, Phoebe Bridgers
- PinkPantheress (UK 어법 트리거 강함)

**검증 실패 / 차단 사례** (Decomposed 강제):
- Taylor Swift (강한 필터)
- BTS (특정 곡명 함께 시 차단)
- BLACKPINK (필터 변동 큼)
- 새로 데뷔한 아티스트 (학습 데이터 부족)

목록은 변동. 차단 발견 시 99_OPERATOR_VAULT Part F (검증 키워드)에 검증 사례 등록.

### 21.7 곡 제목 직접 인용 안전망

곡 제목 직접 인용 시:

**안전 어법**:
```
"in the spirit of NewJeans 'Hype Boy' breezy UKG"
"echoing aespa 'Whiplash' strut energy"
"Mrs. GREEN APPLE 'Lilac' chorus engine"
```

**위험 어법** (자주 차단):
```
"cover of [곡명]"
"[곡명] remake style"
"exact replica of [곡명]"
```

원칙: "in the spirit of" / "echoing" / "channeling" 같은
**간접 인용 어구**가 직접 카피 어구보다 안전.

### 21.8 Producer / Engineer 표기

**Producer 직접 명시**:
```
"Cirkut-produced modern pop polish"
"Jack Antonoff retro 80s lush production"
"Finneas minimalist bedroom pop"
"BNYX dark hyperpop edge"
```

대부분 통과. Producer 이름은 아티스트 이름보다 필터 약함.

**Engineer / Mixer 표기**:
```
"Serban Ghenea-style modern radio-polish mix"
"Manny Marroquin-style punchy bright top end"
"Tom Elmhirst-style vintage warmth plate reverb"
```

### 21.9 한 곡에 다중 레퍼런스 사용

**Hybrid Reference 어법**:
```
"NewJeans(뉴진스) verse texture + Charli XCX(Brat era) club drop"
"Phoebe Bridgers intimate verse + Bon Iver layered chorus"
"aespa cyberpunk verse + Cirkut-produced pop chorus polish"
```

**제한**: 최대 3개 레퍼런스. 4개 이상 시 결 흐릿해짐.



---

## END OF v2.2 NEW SECTIONS (17-21)

## SECTION 22 — REINFORCEMENT PASS (출력 직전 게이트)

### 22.1 목적
Style Box / Lyrics Box 최종 출력 전에 Brief·Ledger와의 정합성을 검증하여 누락·드리프트를 차단한다.

### 22.2 검증 체크리스트 (7항목)
🔧 REINFORCEMENT PASS □ MUST-HAVE 1 → Style Box 키워드 포함? □ MUST-HAVE 2 → Style Box 키워드 포함? □ MUST-HAVE 3 → Style Box 키워드 포함? □ MUST-AVOID 1-3 → Exclude Styles 포함? □ Decision Ledger 최근 5개 → 반영? □ Concept 핵심 단어 → Style Box 첫 80자 내 포함? □ BPM/Key → 정확히 명시?


### 22.3 미반영 항목 자동 보강 규칙

| 미반영 유형 | 자동 보강 방식 |
|---|---|
| MUST-HAVE 키워드 누락 | Style Box 앞부분 추가 (영향 윈도우 0-80자 우선) |
| MUST-AVOID 누설 | Exclude Styles에 추가 (200자 한도 내) |
| Decision 미반영 | 해당 섹션 키워드 교체 |
| Concept 누락 | Style Box 첫 문장 재작성 |
| BPM 모호 | `[BPM: 132]` 메타태그 명시 |

### 22.4 출력 형식
[정상 출력] ... 🔧 Reinforcement: 2개 항목 보강됨

MUST-HAVE "polyrhythm bridge" → Style Box 추가
Exclude "Latin percussion" → Exclude Styles 추가

보강 0건이면 표시 생략.

### 22.5 850-950자 한계와 충돌 시 처리
- 보강으로 950자 초과 예상 시: **MUST-AVOID 키워드 우선 압축** (Exclude로 이동)
- 그래도 초과 시: **장식적 키워드 (analog warmth, glossy, lush 등) 우선 제거**
- Concept · MUST-HAVE · BPM/Key는 **절대 압축 대상 제외**

---

## SECTION 23 — 함축 압축 SOP (NEW v2.3 / 2026-XX)

### 23.0 이 섹션이 다루는 것

회의록 트리거: "출력할 때 중요한 사항들을 함축적으로 글자수
내에 넣는 게 중요해. 어떻게 넣어야 하는지 요령."

§8.2 압축 프로토콜의 확장 + 검증된 7원칙. 매 출력 직전 자동 발동.

### 23.1 압축 7원칙 (검증됨, 우선순위 순)

#### 원칙 1 — 악기+이펙터 페어 묶기
❌ "Rhodes electric piano. Chorus modulation effect on Rhodes." (60자) ✅ "chorused Rhodes electric piano warm 70s" (39자)

**압축률**: 35%
**적용**: 모든 악기-이펙터 조합

#### 원칙 2 — 형용사 하이픈 결합
❌ "warm and analog and slightly saturated" (38자) ✅ "warm-analog tube-saturated" (26자)
**압축률**: 31%
**적용**: 동일 카테고리 형용사 2-3개 묶을 때

#### 원칙 3 — 시대 anchor 한 번만
❌ "1980s synth-pop, 80s analog warmth, 80s gated reverb" (52자) ✅ "1985 LA synth-pop scene, gated reverb signature, analog warmth" (62자)
**압축률**: 변화 적지만 명확도 ↑
**적용**: 시대성 한 번 박고 그 시대 시그니처 요소만 나열

#### 원칙 4 — 위치 명시 어법으로 다중 정보 압축
❌ "Rhodes piano. Pan left 40%. Chorus effect. Subtle reverb." (56자) ✅ "chorused Rhodes L40 light plate" (32자)

**압축률**: 43%
**적용**: 4개 이상 정보 한 phrase로 묶기

#### 원칙 5 — Suno-hacking 디폴트 묶음을 약어처럼

99_OPERATOR_VAULT Part F 표준 처방을 매번 풀로 박지 말고 약어 사용:
풀 버전 (180자): "remove digital artifacts mechanical edge from lead vocal, natural human breath texture restored, warm analog tube saturation on vocal bus, +8 cent detune L15/R15 organic width, vocal corridor 500Hz-3kHz protected de-esser 5-8kHz"

약어 (40자): "vocal organic bus + corridor + warmth"

**압축률**: 78%
**적용**: 모던 팝 / K-pop 디폴트 처리 시
**조건**: 시스템이 약어 → 풀 처방으로 자동 확장 적용

#### 원칙 6 — 모먼트 description 동사 중심으로
❌ "There is a sudden silence at the entry of the chorus, lasting about 0.5 seconds." (76자) ✅ "chorus entry: 0.5s silence preceding" (37자)

**압축률**: 51%
**적용**: 모든 Signature Moment 묘사

#### 원칙 7 — 절대 자르지 않는 것 vs 자르는 우선순위

**절대 자르지 않는 것** (priority A):
- 장르 anchor (첫 30자)
- BPM
- 키 / 모드
- 코드 진행 (CREATE만)
- 보컬 5요소
- Signature Moments
- Era anchor (구체 시대 + 지역 + scene)

**자르는 순서** (priority Z → A):
1. LUFS / 마스터링 태그 (가장 마지막 순위)
2. 텍스처 시즈닝 ("vinyl crackle", "tape hiss")
3. 분위기 형용사 ("dreamy", "wistful", "nostalgic")
4. 스테레오 디테일 (CREATE에서만; COVER는 유지)
5. 오디오 품질 형용사 ("polished", "pristine", "glossy")
6. 보조 악기 5번째 이상
7. 모던 디폴트 묶음 (priority A 보호 후 약어로 압축)

### 23.2 글자수 실측 의무화

체감 판단 절대 금지. 출력 전 무조건 실측:

```bash
echo "..." | wc -c
또는
파일 작성 후 wc -c file.txt

검증된 케이스:

Case 25 COVER 1차 1209자 → 미발견 → Suno에서 ~250자 잘림
Case 27 Style Box 1252자 → 미발견 → 후반 디렉션 무효화
규칙: 850자 초과 시 압축 프로토콜 자동 발동.

23.3 첫 80자 영향 윈도우 SOP
Suno는 첫 80자에 가중치 60% 부여 (검증됨, Blake Crosley 가이드). 이 영역에 들어가야 할 우선순위:
첫 30자: 장르 anchor + 핵심 보컬 한 줄 (e.g., "Late-2020s
K-indie, female mezzo C4-F5,")

30-60자: BPM + 키 + 핵심 코드 진행 sketch

60-80자: 첫 번째 시그니처 모먼트 또는 era anchor
검증된 패턴:
"Modern K-pop 4-piece girl group, 130 BPM, F major modulating
to F# major, female mezzo C4-E5 airy crystal-clear..."
        ↑
        80자 지점

23.4 압축 검증 체크리스트 (출력 직전)
 Style Box 글자수 실측했는가?
 CREATE/COVER 둘 다 Dense 700-950자(≤950 안전 / sketch면 250-350) 범위 안인가?
 첫 80자 안에 priority A 정보가 있는가?
 7원칙 중 적용 가능한 것 다 적용했는가?
 약어로 압축 가능한 디폴트 묶음 처리했는가?
 30% Rule (CREATE/COVER 중복) 통과하는가?
 마지막 50자 안전 buffer 확보했는가?
23.5 모범 압축 사례 (Before/After)
Before (1247자, 한계 초과):
2024-2026 modern Korean indie pop crossing into K-pop
sensibility, 130 BPM, F major modulating to F# major in
the final chorus. Female group vocals A3-E5: airy and
crystal-clear in the verses, slightly chest mix on chorus
hook, never crossing into belt — modern K-pop preserves
proximity over power. Korean lyrics with one English phrase
landing on the chorus melodic peak. Verse arrangement is
sparse: soft drum kit with brushed snare, sub-bass on the
kick fundamental, sustained warm pad in background, plucked
acoustic carrying harmonic motion. Pre-chorus brings UK-
garage 2-step hi-hat skip without changing kick. Chorus
opens with doubled lead vocal slight detune ten cents,
layered synth pluck doubling topline at plus octave, fuller
pad bed but density stays moderate, not wall-of-sound.
Mix has warm analog character, controlled but not crushed
loudness, mid-forward presence with air shelf untouched
above ten kilohertz, vocal corridor protected. Brushed kit
narrow, controlled sub-bass mono below eighty hertz side-
chained at eighty milliseconds, plucked acoustic guitar pair
left forty right forty, warm Juno-style pad bed sustained...
[계속]

After (920자, 압축 적용):
Late-2020s K-pop crossing into K-indie bedroom feel, 130 BPM,
F major→F# major final chorus. Female group A3-E5: airy
crystal-clear verses, slight chest mix chorus hook, no belt
proximity-not-power. Korean verses + English chorus hook on
melodic peak.

Verse sparse: soft kit + brushed snare + sub-bass on kick fund
+ sustained warm pad + plucked acoustic. Pre-chorus adds UKG
2-step hi-hat skip. Chorus: doubled lead +10c detune + layered
synth pluck +octave + fuller pad bed, density moderate not
wall-of-sound.

Signature moments: (1) chorus enters without crash/riser, just
begins (4th-gen K-pop convention); (2) bridge: vocal +
sub-bass + sparse piano only 4 bars; (3) final chorus +half-
step modulation + full layered harmony +3rd +5th.

Mix character: warm analog modeled, controlled-not-crushed,
mid-forward with air shelf 10kHz+ untouched. Vocal corridor
500-3kHz protected. Brushed kit narrow, sub-bass mono <80Hz
sidechain 80ms, plucked acoustic L40/R40, Juno pad sustained,
synth pluck L60/R60 chorus, doubled lead centered +10c.

Verse vocal dry close-mic 8% wet plate, chorus blooms 22%
wet + room ambience, bridge nearly dry hall tail, final
chorus same as chorus + modulation preserved.

Vocal organic bus + corridor + warmth. Drum modern layered.
Master -10 LUFS + tape sat. Wide stereo vocal+bass centered.

[EXCLUDE: auto-tune heavy, vocoder, festival EDM, generic
idol backing, distorted guitar, crowd cheering, stadium
reverb]

압축 결과: 1247자 → 920자 (26% 감소), 정보 손실 0%.

---

## VERSION HISTORY

**v2.4 (2026-05-12) — 클순이 귀환 정비**:
- §3.5d 보컬 디렉션 분배표 신설 (CREATE identity / COVER treatment 분리)
- §3.5e CREATE→COVER Patch 프로토콜 신설 (5단계 결과 분류)
- §3.5f COVER 단계 갑작스러운 화성 변경 패턴 4종 (모듈레이션 / 미분음 / chromatic mediant / borrowed iv)
- §3.5g CREATE/COVER 다양화 패턴 9종 (A~I)
- §3.5h 다양화 검증 체크리스트
- §13~§16 빈 슬롯을 cross-ref 가이드로 채움 (dead navigation 방지)
- 99 파일 분할 (99a/99b/99c) 동기화

**v2.3 (2026-XX)**:
- §22 Reinforcement Pass 추가 (출력 직전 게이트)
- §23 함축 압축 SOP 추가 (7원칙)

**v2.2 (2026-05-09)**:
- §17 v5.5 최신 변경사항
- §18 Style Box Character Limit 명확화
- §19 Parameterized Metatags
- §20 Exclude Styles 활용법 강화
- §21 레퍼런스 표기법 강화

**v2.1 (2026-05-07)**:
- §3.5b CREATE/COVER Overlap Prevention (30% Rule)
- §3.5c Genre-Shift COVER Pattern

**v1.0 (2026-04-30)**:
- 초기 버전

---

## §24. v2.6 대수술 보강 — 평균 회귀 시대의 Suno 엔진 (2026-05-20)

2026-05-19 외부 리서치 (Suno v5/v5.5 시점) 검증 결과를 반영한
엔진 운영 원칙 보강. 기존 §1-23은 그대로 유효, 본 섹션이 상위
점검 레이어로 작동.

### §24.1 평균 회귀 원리 — CREATE/COVER 분리의 진짜 근거

**핵심 진단**: Suno는 확률 엔진. 긍정형 프롬프트만 주면 그
지시어 훈련 데이터 클러스터의 "통계적 중심 = 평균"을 겨냥함.
거시 장르명일수록 클러스터가 거대해 평균 회귀가 강함. 가만
두면 무조건 중심으로 수렴 — "비슷한 곡이 계속 나온다"의
구조적 원인.

**CREATE/COVER 분리의 재해석**:
- 단순히 "역할 분리"가 아니라, **두 번의 프롬프트 통과로 평균에
  서 두 번 떨어뜨리는 구조**. CREATE에서 멜로디·화성 평균,
  COVER에서 텍스처·믹스 평균. 한 번에 다 박으면 두 평균이
  동시에 적용돼 generic 가속.
- 즉 §3 30% Rule은 *역할 중복 방지*가 아니라 *평균 회귀
  방지*가 진짜 목적. CREATE/COVER가 30% 이상 겹치면 같은
  평균을 두 번 겨냥 → 더 generic.

### §24.2 마이크로 장르 1차 룰 (거시 장르 금지)

**룰**: CREATE Style Box 1번 자리에 거시 장르명("pop", "rock",
"city pop", "ballad") 단독 금지. 항상 다음 3요소로 좁힘:
- **하위 장르** (subgenre) — "dream pop" "shoegaze" "neo city pop"
- **시대 앵커** (era) — "2020s", "late-2010s", "80s Tokyo"
- **시그니처 디테일** (signature) — 핵심 텍스처 1개

**근거**: 1만 회 이상 생성 패턴 분석상 서브장르가 부모 장르를
거의 매번 이김. "pop"은 카테고리, "dream pop"은 방향, "80s-
inspired dream pop with shoegaze guitars"는 지도. 구체성이
장식이 아니라 토크나이저가 차트 음악 40년 평균을 가로지르는
대신 훈련 분포의 좁은 영역에 착지하게 만드는 핵심.

**적용**: 운영자가 "시티팝으로 가자" 시 시스템이 즉시 "어느
시티팝? 80s 도쿄 정통 / Neo City Pop 2020s / Mac DeMarco
어쿠스틱 결 / Yebba 모던 R&B 영향 / 사이트팝 보컬 우선" 등
하위 갈래 제시. 그 다음에 박스 진입.

### §24.3 두 장르 스택 한계 — 3개 이상은 모순

**룰**: 하이브리드 시 두 장르까지가 스위트 스팟. "indie folk
meets bedroom pop" OK. 세 장르 섞으면 신호가 모순돼 generic
평균으로 회귀.

**§3.5g 다양화 패턴 보강**: 패턴 C(2-3 장르 적당히 섞기)에서
3장르 시도는 *섹션별 명시 분할*만 허용:
- 불가: "city pop, hyperpop, country" (한 박스에 3장르)
- 가능: `[Verse: indie folk] [Chorus: bedroom pop with subtle
  hyperpop synths]` (섹션 분할 + 한 섹션 내 2장르)

60/30/10 블렌딩 원칙(99_OPERATOR_VAULT Part F (60/30/10 블렌딩 원칙))은 *비율*이 아니라 *우선
순위* 표현. 실제 박스에는 주 장르 1번 + 보조 장르 1번 + 시그
니처 1개로 2태그 압축.

### §24.4 앞뒤 양쪽 배치 룰 — 1차 80자 + 마지막 자리

**기존 룰 유지**: 토크나이저는 앞쪽 처리 가중치 높음 → 장르
1번 자리, 무드 2번 자리 (1차 80자 룰).

**신규 추가**: 프롬프트가 무시되면 가장 중요한 요소를 **맨 앞
과 맨 뒤** 양쪽에 배치. 중요 태그가 중간에 묻히지 않게.

**EXCLUDE 위치 명문화**: Suno는 긍정형을 먼저 처리하고 그
다음 exclusion 적용. EXCLUDE는 **Style Box 맨 끝**에 두는 게
효과 최대. (Custom Mode의 별도 Exclude 필드를 쓸 경우는 이
룰 무관.)

### §24.5 악기는 디스크립터 없이 부르지 마라

**룰**: Style Box에서 악기명 단독 금지. 항상 1-2단어 디스크
립터 부착.
- 불가: "Rhodes", "bass", "guitar"
- 가능: "dusty Rhodes", "warm fingered bass", "chorused
  clean guitar 16th comping"

**근거**: 각 디스크립터가 출력 가능 공간을 수천 가지에서 수십
가지로 좁힘. "dusty Rhodes"는 악기 + 시대(빈티지) + 톤
(살짝 바램) + 미학(따뜻함)을 동시 전달. "Rhodes" 단독은
Suno의 디폴트 Rhodes 평균(현대 클린 톤)으로 회귀.

**예외**: COVER 단계에서 이미 CREATE에 디스크립터 박혔으면
COVER에서 동일 악기 재호명 시 짧게 가능. 단 첫 등장은 항상
디스크립터 동반.

### §24.6 곡 작업 시작 시 §24 자동 점검 체크리스트

운영자가 새 곡 요청 시 시스템이 박스 진입 전 자동 점검:

1. **CREATE 1번 자리** — 거시 장르명만 아닌 하위+시대+시그니처?
2. **장르 스택 수** — 2개 이내인가? 3개면 섹션 분할로 전환했나?
3. **악기 디스크립터** — 모든 악기명에 디스크립터 부착됐나?
4. **EXCLUDE 위치** — Style Box 맨 끝인가? (Custom Mode Exclude
   필드 사용 시 무관)
5. **30% Rule** — CREATE/COVER 디스크립터 중복 30% 미만인가?

미통과 항목 자동 보강 후 박스 출력. 보강 시 출력 하단에
"🔧 §24 보강: [항목] 보완됨" 1줄 표기.

---

EOF (END OF FILE 09_SUNO_ENGINE.md)


---

## SECTION 25 — VOCAL ANCHOR (NEW v2.7 / External Research)

### 25.1 핵심 발견

외부 검증 (Suno Field Guide 2026): **Suno v5는 첫 1-2초 안에
보컬 캐릭터 확정**. 가이드 안 하면 무작위 결과. Vocal Anchor를
*가사 필드 맨 위*에 박으면 모든 후속 가창 일관성 확보.

### 25.2 단일 보컬 Vocal Anchor 어법

가사 필드 맨 첫 줄:
```
[Vocal: female alto, smooth and soulful, airy on quiet lines,
powerful natural belting on peaks, contemporary R&B inflection.]
```

구성 요소 (4-6개):
1. **성별 / 음역**: female alto / male tenor / female soprano /
   male bass-baritone
2. **메인 톤**: smooth / gritty / silky / breathy / clear /
   nasal / warm / cool
3. **음역대 변화**: airy on quiet / powerful on peaks /
   restrained verse / explosive chorus
4. **장르 인플렉션**: contemporary R&B / classic rock /
   K-pop modern / J-pop bright / country narrative
5. **특수 기법** (선택): vibrato narrow / slight slide /
   no melisma / minor pitch curls

### 25.3 듀엣 보컬 Vocal Anchor 어법

```
[Vocal 1 (Serica): female soprano C4-E5, clear calm polite voice,
refined gentle, K-pop ballad inflection, no vocal fry.]
[Vocal 2 (Cheny): female high soprano E4-G5, child-like punk-rap,
sweet light airy texture, warm natural human warmth, occasional
shouting on hooks, no descending phrase-end curls.]
```

라벨 룰:
- 운영자 핵심 캐릭터 이름 = 브라켓 안에 표기 가능 (Serica / Cheny)
- 라인 위 라벨로 *각 라인*에 어떤 보컬이 부를지 명시 (10 §18 참조)
- "vocal 1:" prefix 형태 금지 — *bracket label only*

### 25.4 캐릭터 이름의 Vocal Anchor 처리

운영자 핵심 캐릭터 (Serica / Cheny / 테피 / 우나 / 크래더 / 봉남이):
- *Style Box에 캐릭터 이름 박지 마* (Suno 필터 / 의미 없음)
- *Vocal Anchor 라벨로만 사용* — 가사 추적용 메타데이터
- *V1 / V2 약어로 lyrics body에 표시* (각 라인 위)

예시:
```
[V1] 6시 옥상 위에 콘크리트가 녹아
[V2] 에어컨이 죽었다, 너에게 보낸 톡
[V1+V2] 답장은 오지 않고 햇빛이 차오르네
[V2] 공룡들도 이런 날에 안녕했을까
```

### 25.5 Vocal Anchor 통과 검증

운영자 신고 "보컬이 이상해 / 다르게 나왔어" 시 진단:
1. Vocal Anchor가 가사 *첫 줄*에 있나?
2. 4-6 element 모두 박혔나?
3. Suno가 anchor 무시한 패턴인가? (예: 여성 anchor에 남성 보컬 출력)
4. 안 통과 시: Anchor 더 짧고 명확하게 / 특정 단어 (예: "airy")만
   살리기

---

## SECTION 26 — POP GRAVITY WELL (NEW v2.7 / External Research)

### 26.1 핵심 발견

외부 검증 (Suno Field Guide / 통계 분석):
- **모든 장르가 Pop으로 끌림**
- Rock ↔ Pop: 315B 통계 연결
- Funk ↔ Pop: 116B
- Emo ↔ Pop: 12.2B
- Metal ↔ Pop: 별도 통계 / 약하지만 끌림
- "emo metal" 박으면 → emo pop 출력 (Metal 약 / Pop 강)

### 26.2 메커니즘

Suno는 *통계적 중력 우물* 모델. 가만 두면:
1. 거시 장르 (Pop / Rock / Electronic) 중 가장 인기 있는 쪽으로 끌림
2. Pop이 압도적 1위 → 모든 장르 자동 pop화
3. 명시 EXCLUDE 없으면 의도한 장르가 pop pop화됨

### 26.3 탈출 3종 어법

#### A. 명시 EXCLUDE
```
EXCLUDE: pop, synth pop, modern pop production
```
가장 강력. 의도 장르 외 모든 pop variant 차단.

#### B. 이상한 조합 강제
*예측 불가능한* 조합으로 평균 벗어남:
- "emo industrial" (emo 12.2B → 12.2B 차단)
- "orchestral phonk" (둘 다 약한 tag → 약한 평균)
- "shoegaze country" (장르 충돌 → 새로운 위치)

#### C. 전략적 대조
의도 장르의 *반대 element* 거부:
- 의도 = Rock → EXCLUDE에 "smooth production, pop polish"
- 의도 = Folk → EXCLUDE에 "synth, electronic drums"
- 의도 = Jazz → EXCLUDE에 "pop hook, autotune"

### 26.4 자동 점검 (출력 직전)

운영자 의도 장르 vs Suno 확률 매핑 자동 비교:
- Rock 의도 → Pop 끌림 위험 → EXCLUDE 자동 권유
- Metal 의도 → Pop 더 약함 → 강한 metal 강화 또는 이상한 조합
- Emo / Indie / Hyperpop → pop 자석 → EXCLUDE 의무

### 26.5 운영자 신고 트리거

"의도한 장르 안 나옴 / 팝처럼 들림 / generic해 / 비슷한 곡 나옴"
→ Pop Gravity Well 진단:
1. EXCLUDE pop 박혔는가?
2. CREATE 1번 자리 거시 장르?
3. 이상한 조합 시도 가능한가?
4. 안 풀리면 마이크로 장르로 더 좁히기

---

## SECTION 27 — GENRE CLOUDS (NEW v2.7 / External Research)

### 27.1 개념

특정 장르 박으면 *cluster*가 따라옴 (떨어지지 않는 통계 연결).

### 27.2 검증된 4 주요 cloud

#### A. Rap Cloud
박으면 자동 동반: trap, bass, hip-hop, beat, urban, 808

#### B. Orchestral Cloud
박으면 자동 동반: epic, cinematic, dramatic, piano, strings,
soundtrack

#### C. Indie Cloud
박으면 자동 동반: pop, acoustic, dreamy, psychedelic, lo-fi,
bedroom

#### D. Dark Electronic Cloud
박으면 자동 동반: synth, electro, synthwave, futuristic, glitch

### 27.3 전략적 활용

#### 의도와 cloud 일치
"rap" 박으면 trap / 808 / urban 따라옴 → 의도가 hip-hop이면 OK

#### 의도와 cloud 불일치
"indie" 박으면 pop 따라옴 → 의도가 pure indie folk면 EXCLUDE pop

#### Cloud 깨기
한 cloud 안의 *드문* element 박기:
- "rap" 대신 "boom bap" / "abstract hip-hop" (rap cloud의 변두리)
- "orchestral" 대신 "chamber" / "neoclassical" (orchestral cloud 변두리)

### 27.4 Cloud 검증법

운영자 의도 장르 → 가사 출력 → 어떤 cloud element가 따라왔는지
역추적 → 불필요 element EXCLUDE 박기.

---

## SECTION 28 — STRONG vs WEAK TAGS (NEW v2.7 / External Research)

### 28.1 강한 tag (다른 지시 압도)

```
pop, rock, electronic, hip-hop, country
```

박으면 다른 지시 무력화 가능성 ↑. *단독 사용 위험*. 강한 tag는
*subtype과 결합*해서 박기:
- "pop" → "K-pop hyperhook"
- "rock" → "garage rock revival"
- "electronic" → "deconstructed club"

### 28.2 약한 tag (강화 필요)

```
grunge, math rock, swing, shoegaze, post-punk, dream pop, jungle,
breakcore, hyperpop, witch house, vaporwave, indietronica
```

박으면 *해석 약하거나 무시 가능*. 약한 tag 활용 시:
- 약한 tag 3-4번 반복 (가능한 자리에서)
- 약한 tag의 시그니처 element 함께 박기
- 약한 tag와 강한 tag 결합 시 *약한 쪽 과도 강화 + 강한 쪽 EXCLUDE*

### 28.3 약+강 결합 처방

예: "indie + pop" 박으려면:
- 약한 쪽 (indie) 풀바디: "lo-fi bedroom indie, 4-track production,
  acoustic-leaning, intimate close-mic"
- 강한 쪽 (pop) EXCLUDE: "no commercial pop polish, no streaming
  loudness, no modern radio production"

### 28.4 자동 점검

CREATE Style Box에서:
- 약한 tag 검출 시 → 시그니처 element 자동 보강 권유
- 강한 tag 검출 시 → subtype 자동 권유

---

## SECTION 29 — MAX MODE / START_ON / PIPE STACK (NEW v2.7)

### 29.1 MAX Mode

```
[Is_MAX_MODE: MAX](MAX)
[QUALITY: MAX](MAX)
[REALISM: MAX](MAX)
[REAL_INSTRUMENTS: MAX](MAX)
```

배치: 가사 *맨 첫 줄* (Vocal Anchor 직후).

효과:
- **유효 장르**: acoustic / folk / country / orchestral /
  singer-songwriter / unplugged / chamber
- **무효 장르**: electronic / trap / synthwave / EDM / hyperpop
- 유효 장르에서 *substantial improvement* 검증
- 무효 장르는 박아도 차이 없음

작동 원리:
- Suno에게 "real instruments / quality" 신호
- 합성 / 디지털 sheen 줄임
- Organic texture 강화

### 29.2 START_ON

#### 29.2.1 부수적 인트로 스킵
```
[START_ON: TRUE]
```
배치: 가사 첫 줄. 효과: instrumental intro 스킵, 즉시 보컬 시작.

#### 29.2.2 시작 지정 (텍스트)
```
[START_ON: "Tell me are you ready"]
```
효과: 정확히 그 텍스트부터 시작.

#### 29.2.3 DUET_START_ON (듀엣 시작 지정)
```
[DUET_START_ON: TRUE]
[MALE_START_ON: "First, I"]
[FEMALE_START_ON: "Then, you"]
```

### 29.3 Pipe Tag Stacking (Grenar Trick #8)

#### 29.3.1 기본 구문
```
[Chorus | Anthemic | Stacked harmonies | Brass section | Drop]
```

#### 29.3.2 우선순위 룰
- 최대 7 element
- 좌 → 우 우선순위 (앞이 더 강함)
- 첫 element는 *section 명* ([Verse] / [Chorus] / [Bridge] 등)
- 둘째부터 modifiers

#### 29.3.3 검증된 패턴

```
[Chorus | Anthemic | Stacked harmonies | Brass]
[Verse | Sparse | Single vocal | Acoustic guitar only]
[Bridge | Stripped down | Closer mic | Intimate]
[Final Chorus | Key up half-step | Layered vocals | Full band]
[Drop | Heavy 808 | Sidechained synth | Vocal chops]
```

#### 29.3.4 Section-by-Section Build

복합 곡 어법:
```
[Intro | Solo piano | 8 bars]
[Verse 1 | Vocal + Piano only | 16 bars | Singing: tender restrained]
[Pre-Chorus | Adds bass + soft drums | 8 bars | Ascending pad]
[Chorus | Full band entry | 16 bars | Stacked harmonies | Anthemic]
[Verse 2 | Slight rhythmic variation | 16 bars | Subtle hi-hat detail]
[Pre-Chorus | Bigger build | 8 bars | Layered synth pad]
[Chorus | Full instrumentation | 16 bars | Higher harmonies +5th]
[Bridge | Stripped to piano + voice | 8 bars | Singing: vulnerable
 confessional]
[Final Chorus | Key up half-step | 16 bars | Belted vocal | Full
 layered production]
[Outro | Slow fade | 8 bars | Piano holds out]
```

### 29.4 Two-Songs-in-One Splicing

긴 곡 2개 컨셉 결합 어법:
```
[CONCEPT_A: dance pop verse-chorus, 128 BPM, 1st half]
[Intro to Chorus 2 — dance pop arrangement]

[TRANSITION | half-time drop | 4 bar bridge | tempo halves]

[CONCEPT_B: cinematic ballad, 80 BPM, 2nd half]
[Bridge to Outro — orchestral ballad arrangement]
```

운영자 "한 곡에 두 곡 / 곡 안에서 장르 점프" 요청 시 사용.

---

## SECTION 30 — PERIOD vs COMMA RULE (NEW v2.7 / External Research)

### 30.1 핵심 발견

외부 검증 (Suno Field Guide):
- **마침표 (`.`)** = 개념 경계 신호 = **필수**
- **콤마 (`,`)** = 선택적 element 신호
- **`and / with`** = 필수 element 접속

### 30.2 어법 비교

❌ 잘못된 어법 (콤마만):
```
acoustic guitar, male vocals, emotional, reverb, slow tempo
```
→ Suno 해석: 모두 선택적 → 일부만 적용 가능성 ↑

✅ 올바른 어법:
```
acoustic guitar with male vocals and emotional delivery,
reverb-heavy production. Slow tempo around 70 BPM.
```
→ Suno 해석: 첫 문장 = 필수 / 둘째 문장 = 강조 / 콤마는 양념

### 30.3 적용 룰

#### A. 필수 element는 문장으로
```
Modern K-pop with female vocals and synth-pop production.
```
세 element (K-pop / 여성 보컬 / synth-pop) 모두 필수.

#### B. 선택 element는 콤마 나열
```
Modern K-pop, occasional rap break, ad-libs, vocal chops.
```
첫 element 필수 / 나머지 양념.

#### C. 두 카테고리 결합
```
Modern K-pop with female vocals and 128 BPM. Synth-pop production,
analog warmth, occasional vocal chops, distant ad-libs.
```
첫 문장 = core (필수) / 둘째 문장 = production texture (양념).

### 30.4 자동 변환

CREATE/COVER 출력 직전 자동 변환:
- 콤마만 나열된 Style Box → 필수 vs 선택 분류 → 마침표 구조화
- 변환 시 "🔧 Period Structure: 필수/선택 재구조화" 표기

---

## SECTION 31 — LYRIC BLEED PROBLEM (NEW v2.7 / External Research)

### 31.1 문제 정의

Suno는 *singable look*하는 텍스트를 *모두 노래로 부름*. Style Box
안의 시적 라인 / quoted phrase / ALL CAPS / 자연 prose가 Lyrics
필드로 *bleeding*.

### 31.2 트리거 패턴

다음이 Style Box에 있으면 Lyric Bleed 위험:
1. **시적 라인**: "the sound of her voice in the morning"
2. **인용부호 phrase**: `"like a dream"` / `"never let go"`
3. **ALL CAPS phrase**: `BIG BOLD STATEMENT` (Style Box 안)
4. **자연 prose**: 완결된 문장 / 1인칭 진술
5. **빈 Lyrics Box**: Suno가 Style Box에서 가사 자동 생성

### 31.3 완화 처방

#### A. Style Box dense / technical 만들기
```
✗ "feels like the sound of dreams"
✓ "dreamy reverb-soaked vocal, 200ms plate reverb, sidechain swell"
```

#### B. Lyrics Box 항상 채우기
빈 Lyrics Box 절대 금지. 최소 1줄이라도 박기.

#### C. 분리자 박기
Style Box 끝에:
```
[end of style description] ///*****///
```
일부 검증.

#### D. 인용부호 회피 (구조 필드 외)
```
✗ vocal style "smooth and silky"
✓ smooth silky vocal style
```

### 31.4 자동 점검

Style Box 출력 직전:
- 트리거 패턴 5종 자동 스캔
- 발견 시 자동 완화 권유
- "⚠️ Lyric Bleed Risk: [패턴] 발견. [완화 처방] 자동 적용" 표기

---


---

## SECTION 33. VOICE / PERSONA SYSTEM (v5.5) — v2.11 NEW

External verification (Suno v5.5 docs, mindstudio.ai 2026):
Suno v5.5 introduces persistent voice profiles trained from
operator-uploaded samples — *not* style references, but identity
profiles.

### 33.1 Tier requirements

- **Free**: Personas not available
- **Pro ($10/mo)**: Personas + Custom Models (up to 3)
- **Premier**: Personas + unlimited Custom Models + Studio access

### 33.2 What Suno Persona learns

- **Timbre**: tonal color identifiable across content
- **Register / range**: natural sit zone (chest/head/mix)
- **Resonance patterns**: frequency interaction
- **Voice texture**: breathiness, fry, sibilance baseline

### 33.3 What Persona is NOT

- Not text-to-speech
- Not vocal style transfer of existing recording
- Not a perfect 1:1 clone
- Generates *new* musical performance with operator's voice
  characteristics applied

### 33.4 Workflow

```
1. Record 3-4 clean vocal sections (8-16 bars each):
   - Different tempos (slow / mid / uptempo)
   - Different keys (low / mid / high)
   - Both soft + powerful delivery
2. Clean audio: no reverb, no background, no other voices
3. Upload to Suno → Train Persona
4. Save Persona ID
5. Future songs: apply Persona ID + Style + Lyrics
```

### 33.5 Operator catalog opportunity

99_OPERATOR_VAULT Part B has 24+ character baselines. Each could become a Persona:
- 24 Personas = series continuity locked
- Character cross-references baseline → Persona ID

**Cross-reference:** 00 C-49 / 06 §14 / 10 §21.6.

---

## SECTION 34. STUDIO MODE (v5.5) — v2.11 NEW

External verification (Blake Crosley v5.5 reference, Hollyland 2026).

### 34.1 What Studio is

In-browser DAW for post-generation editing. Pro/Premier tier only.

### 34.2 Capabilities

1. **Stem export**: vocals/instrumental split OR 12-track breakdown
2. **Section Replace**: regenerate one section (Verse 2 only) without
   whole-song regeneration
3. **Warp Markers**: micro-adjust timing of notes/phrases with
   quantize snap
4. **Alt Takes**: generate alternative sections inline
5. **Remove FX**: strip AI-applied reverb/delay for dry stems
6. **Time signature grid**: 3/4, 6/8, odd time signatures (editing
   surface only — does not condition generation)

### 34.3 Why this matters

Default workflow (Free/Pro): regenerate whole song until satisfied.
*Wasteful*. Studio enables:
- Keep good sections, replace weak ones
- Stem editing in DAW (move to Logic / Ableton / Pro Tools)
- Time tightening on important phrases

### 34.4 Iterative workflow

```
Generation 1 → listen → identify good/bad sections
Section Replace bad sections (multiple takes if needed)
Final cut → export stems → DAW polishing
```

External verification: *"Effective Suno usage follows iterative
workflow, not single-prompt approach."*

**Cross-reference:** 00 C-48 / 10 §25.

---

## SECTION 35. REFERENCE TRACK UPLOAD — v2.11 NEW

External verification (Suno API docs, openmusicprompt 2026).

### 35.1 What it does

Upload audio clip → Suno learns style/texture/voice characteristics →
applied to new generations.

### 35.2 Capabilities by tier

| Tier | Upload duration |
|---|---|
| Free | 6-60 seconds |
| Pro | up to 2 minutes (some models 8 min) |
| Premier | up to 8 minutes + persistent style learning |

### 35.3 Use cases

**Catalog consistency:**
- Upload operator's best track in style X
- Future style-X songs: include as reference
- Result: Suno learns operator's catalog sound

**Style emulation:**
- Upload reference of target style (legally — own work or licensed)
- Audio Influence slider 60-80%
- Suno mirrors texture/voice/production

**Continuation:**
- Upload partial track (6-60 sec)
- Suno extends it

### 35.4 Best practices

- Clean audio (no background, no other voices)
- Match desired output (don't upload metal for ballad target)
- Set Audio Influence 60-80% for shape-mirroring
- Pair with detailed Style Box for genre+tempo lock

**Cross-reference:** 00 C-49 / 10 §26.

---

## SECTION 36. CREATIVE SLIDERS — v2.11 NEW

External verification (Suno v5.5 docs, Hollyland 2026,
openmusicprompt 2026).

### 36.1 Three sliders

**Weirdness (0-100, default 50):**
- 0-30: Safe, average, distribution-following
- 40-60: Balanced (default sweet spot)
- 70-100: Glitch, dark, experimental, unexpected harmonies

**Style Influence (0-100, default 50):**
- 0-30: Genre tag weakly applied — more freedom
- 40-60: Typical strength
- 70-100: Aggressively applied — every detail conforms

**Audio Influence (0-100, UI default 25 — COVER는 25에서 올림: lead 60-75 / texture 20-40):**
- Only when reference audio uploaded
- 0-40: Vibe suggestion
- 50-70: Shapes production
- 80-100: Strongly constrains

### 36.2 Slider presets

**Sketch/exploration:** Weirdness 50-60 / Style 40-50
**Polished production:** Weirdness 40-50 / Style 70-80
**Experimental:** Weirdness 70-85 / Style 40-50
**Reference-locked:** Weirdness 30-40 / Audio 70-80

### 36.3 Cross-reference

- 11 §17 — production design (existing partial coverage)
- 00 C-47 — Tight/Dense mode connects to Style Influence slider

---

## SECTION 37. POSITION-BASED WEIGHTING — v2.11 NEW

Detailed reference for Position weighting (00 C-45 / 10 §23).

### 37.1 The weight distribution

| Position | Influence | Notes |
|---|---|---|
| 1 | ~50% | First sonic descriptor — half the prompt's weight |
| 2 | ~25% | Second priority — strong influence |
| 3 | ~12.5% | Third — meaningful but secondary |
| 4 | ~6% | Fourth — supporting detail |
| 5+ | <5% | Diminishing |

### 37.2 Style Box position planning (Tight Mode)

```
Tight Mode (250-350 chars budget):
Position 1: Strongest microgenre (e.g. "Festival mainstage hardstyle")
Position 2: Era anchor / dominant mood
Position 3: Vocal identity OR signature instrument
Position 4-5: Tempo + key
Position 6+: One signature trait (drop if over budget)
```

### 37.3 Style Box position planning (Dense Mode)

```
Dense Mode (700-950 chars budget):
Position 1 (50%): Microgenre 1-word/phrase
Position 2 (25%): Era + style lineage
Position 3 (12.5%): Vocal directive 5-element open
Position 4+: Instruments, production, mix, throughout
```

### 37.4 Position 1 — DOs

✅ Strong microgenres reward specificity:
- `Festival mainstage hardstyle anthem`
- `Modern UK garage 2-step`
- `2026 hyperpop crystal`
- `Vintage 70s funk soul`
- `Brazilian bossa nova jazz fusion`
- `Korean indie crossover ballad`

### 37.5 Position 1 — DON'Ts

❌ Industry category leak (50% wasted on regression):
- `K-pop` — average regression to 2010s mid
- `J-pop` — same trap
- `Latin pop` — same trap

❌ Genre cloud single-word (too vague):
- `Pop` — Pop Gravity Well
- `Electronic` — vague
- `Rock` — vague

❌ Mood-first (wastes 50% on adjective):
- `Beautiful` / `Emotional` / `Dark`
- Use as Position 4+ qualifier, not Position 1

### 37.6 Verification

Before output, check:
- Position 1 = microgenre (not industry / cloud / mood)?
- Position 2 = era/lineage?
- Position 3 = vocal/signature?

**Cross-reference:** 00 C-28.1 ② / C-45 / 10 §23.

---

## SECTION 38. STYLE BOX POSITION WORKFLOW — v2.11 NEW

Connects 00 C-44 budget system with C-45 position weighting.

### 38.1 1-shot writing procedure

```
Step 1: Choose mode (Tight 250-350 / Dense 700-950)
Step 2: Plan Position 1-3 (50% + 25% + 12.5% = 87.5%)
        These three carry the song.
Step 3: Allocate Part 1-7 character budget (00 C-16.5 table)
Step 4: Write in ONE PASS
        Don't write full body then compress.
        Write within budget per part.
Step 5: wc -c verification (1 call)
Step 6: If ±5% over → adjust longest Part only (1 pass)
Step 7: Ship

Max iterations: 2 (write + 1 adjust)
3+ iterations → C-44 violation, auto-report
```

### 38.2 Position 1-3 worksheet

Before writing Style Box, fill this (mental or written):

| Position | Decision | Example |
|---|---|---|
| 1 (50%) | Strongest microgenre | "Festival mainstage hardstyle" |
| 2 (25%) | Era / lineage | "late-2020s European club aesthetic" |
| 3 (12.5%) | Vocal/signature anchor | "female mezzo belt with crisp diction" |

That's 87.5% of the prompt's effective weight. The rest is detail.

### 38.3 Common mistakes (from Case 41)

**Mistake 1: K-pop in Position 1**
- v1 wrote: `"Hardstyle K-pop hybrid"` — K-pop got 25% (Position 2)
- Better: `"Festival mainstage hardstyle anthem"` (K-pop out of P1-2)

**Mistake 2: Compound microgenre splitting Position 1**
- ❌ `"Pop-rock indie-folk crossover"` — 3 weak genres splitting 50%
- ✅ `"Indie folk-rock"` (single unit) + `"with pop polish"` (Position 4)

**Mistake 3: Mood-first**
- ❌ `"Beautiful emotional ballad"` — 50% wasted on "Beautiful"
- ✅ `"Cinematic piano ballad"` + `"beautiful, emotional"` (Position 4)

---

## SECTION 39. ITERATIVE WORKFLOW PROTOCOL — v2.11 NEW

External verification (Blake Crosley v5.5 reference 2026).

### 39.1 Default workflow (Free/Basic Pro)

```
1. Write Style + Lyrics
2. Generate (full song)
3. Listen
4. If unsatisfactory: REWRITE prompt → regenerate (waste credits)
```

### 39.2 Iterative workflow (Pro+ with Studio)

```
1. Write Style + Lyrics
2. Generate (full song)
3. Listen — identify good sections + weak sections
4. Section Replace WEAK sections only (Studio mode)
5. Multiple takes per section as needed
6. Once satisfied → export stems for DAW work
7. (Optional) Save best Persona for future use
```

### 39.3 Section Replace tips

External verification (Blake Crosley): *"Rarely does the first
replacement perfectly match the surrounding context. Budget 2-5
attempts for clean transitions into the surrounding material.
Best practice: Include a structural metatag like [Verse 2]
before the replacement target line."*

### 39.4 Operator catalog application

For songs already in 99c (already generated):
- Don't regenerate from scratch if mostly satisfied
- Section Replace targeted weak spots only
- Re-export stems for catalog mastering pass

**Cross-reference:** 00 C-48 / 10 §25.

---

## SECTION 40. ARTIST WORKAROUND 5-LAYER FRAMEWORK — v2.11 NEW

Detailed reference for 00 C-1.2 5-Layer artist workaround.

### 40.1 The 5 layers

| Layer | Purpose | MJ example |
|---|---|---|
| 1. Producer Name | Person who shaped sound | "Quincy Jones style + Teddy Riley style" |
| 2. Genre + Era | Time-localized microgenre | "new jack swing + 80s pop-funk" |
| 3. Sound Trait | Audible characteristic | "bass-driven + tight groove + horn stabs" |
| 4. Vocal Description | How vocals sound | "powerful male vocals + falsetto runs" |
| 5. Production Style | Mix/production result | "polished production + warm analog synths" |

Stack all 5 → ~95% convergence on blocked artist's sound.

### 40.2 Producer Names library (safe to use)

**80s Pop-Funk (MJ era):**
- Quincy Jones, Teddy Riley, Jam & Lewis, Babyface

**Modern Pop:**
- Max Martin, Shellback, Jack Antonoff, Greg Kurstin, Finneas,
  Benny Blanco

**K-pop:**
- Teddy Park, Yoo Young-jin (한글 음역 가능), Shinsadong Tiger,
  Black Eyed Pilseung, Kenzie

**EDM:**
- Diplo, Calvin Harris-style, Skrillex-style, Hardwell-style,
  Tiësto-style

**R&B:**
- Pharrell-style, Timbaland-style, Mike Will Made It-style,
  Bryan-Michael Cox-style

**Hip-hop:**
- Dr. Dre-style, J Dilla-style, Mike Will-style, Metro Boomin-style,
  Kenny Beats-style

**Rock:**
- Rick Rubin-style, Butch Vig-style, Brendan O'Brien-style,
  Steve Albini-style

**Country:**
- Dann Huff-style, Jay Joyce-style, Frank Liddell-style

**Latin:**
- Tainy-style, Sky Rompiendo-style, Mauro Cattivelli-style

### 40.3 Era + work combination examples

| Blocked artist | Workaround |
|---|---|
| Michael Jackson | "King of Pop 80s era + Thriller-era pop-funk" |
| Madonna | "Like a Virgin era pop + Material Girl era" |
| Prince | "Minneapolis sound era + Purple Rain era" |
| Whitney Houston | "I Will Always Love You era ballad + power-vocal R&B" |
| Mariah Carey | "Vision of Love era + whistle-register R&B" |
| Beyoncé | "Crazy in Love era pop-R&B + Lemonade era" |
| BTS | "K-pop boy group hyperhook crossover" + 비티에스 |
| BLACKPINK | "girl crush hyperpop crossover + 4-member girl group" |

### 40.4 Sound Trait library by genre

**Funk:** bass-driven, tight groove, syncopated, horn stabs, slap bass,
clavinet, wah guitar

**R&B:** smooth, melismatic, breathy, ad-lib heavy, layered backing,
808 sub-bass

**Pop:** polished, hook-forward, layered vocal stack, four-on-floor,
sidechain

**Hip-hop:** boom-bap / trap / drill / phonk (specify), hi-hat rolls,
808 slides

**EDM:** sidechain pumping, riser-drop, supersaw lead, distorted kick,
white-noise sweep

**Rock:** distorted guitar, double-tracked, snare crack, room reverb

**Country:** twangy guitar, steel guitar slide, kick-snare drive,
group harmony

### 40.5 Cross-reference

- 00 C-1.2 (5-Layer rule)
- 00 C-50 (unofficial hacks — only if 5-Layer fails)
- 10 §27 (unofficial hacks detail)
- 99b §[new] — Producer Names library expansion

---

# END OF 09_SUNO_ENGINE v2.11


## § USER EXTENSION ZONE v2.0 (2026-05-24)

bitwize v5-best-practices 25KB + suno-engineer SKILL.md 13KB +
tips-and-tricks 8KB + v5-changes + suno CHANGELOG 풀바디 통합.

**이 USER EXTENSION = Suno V5/V5.5 운영 풀바디.**


### §UE-1. Suno V5/V5.5 Quick Reference Card

```
Quick Start Formula:
[genre], [subgenre], [instruments], [mood], [tempo], [vocal description]

Example:
nerdcore hip-hop, glitchy IDM beats, lo-fi digital artifacts,
nostalgic, melancholic, 85 BPM, male vocals, gravelly voice, introspective
```

### §UE-2. V5 Key Improvements (외부 검증)

```
| Feature | Description |
|---|---|
| Intelligent Composition | 30s hooks ~ 8-min epics, coherent |
| Studio-Grade Audio | 44.1 kHz, balanced mixes |
| Vocal Engine | Human-like vocals, breath/emotion/vibrato |
| 10x Faster | Seconds instead of minutes |
| 12 Stem Extraction | Full stem control |
| Extended Length | Up to 8 minutes |
| Persistent Memory | Vocal/instrument stable across project |
| Granular Controls | Tempo/key/dynamics with automation |
```


### §UE-3. V5.5 Update (2026-03-26) — Pro/Premier 전용

**No prompt syntax changes.** V5 prompts run identically on V5.5.

```
| Change | Impact |
|---|---|
| Nuanced phrasing, dynamic range | "slightly detuned vintage keys" delivers |
| Better instrument separation | Less mud on dense prompts |
| More expressive vocals | Emotion tags track closer |
| Voices (Pro/Premier) | Voice cloning |
| Custom Models (Pro/Premier) | Fine-tuned on 6+ tracks |
| My Taste (all tiers) | Passive learning, autogenerate only |
```


### §UE-4. Prompt Construction — Critical Rules

#### §UE-4.1 Sweet Spot: 4-7 Descriptors (외부 검증)

```
❌ Bad (prompt fatigue, 8+):
"Ethereal indie folk with vintage analog warmth and melancholic
undertones, finger-picked acoustic, tape hiss, lo-fi, intimate,
breathy, whispery, nostalgic, contemplative, minimalist production"

❌ Bad (too vague, < 4):
"Nice upbeat music"

✅ Good (4-7 descriptors):
"Sad indie folk, acoustic, gentle, breathy female vocal, intimate"
```

#### §UE-4.2 Four-Part Anatomy (외부 정설)

```
1. Genre + Era + Influences
   "90s alt-rock with Britpop undertones"

2. Tempo/BPM + Key (optional)
   "120 BPM, A minor"

3. Instrumentation & Arrangement
   "Live drums with room ambience; palm-muted guitars; warm bass"

4. Production & Mix Notes
   "Analog glue compression; tape saturation; lead vocal upfront"
```

#### §UE-4.3 Top-Loaded Palette (C-62)

```
[Mood] + [Energy] + [2 Instruments] + [Vocal Identity]

Example:
"Melancholic, slow-burn, piano and strings, female alto with subtle vibrato"
```


### §UE-5. Don't Reuse Old Prompts (Suno CTO #1)

**V4/V4.5 prompts X on V5.** V5 listens differently.
Write new prompts.


### §UE-6. Token Bias Avoidance (C-63)

```
Bias 단어 8개:
Neon / Echo / Ghost / Silver / Shadow / Whisper / Crystal / Velvet

→ 자주 박지 마
→ 자동 점검: Style Box 2+ bias 단어 발견 → 치환 권유
→ 가사 박을 때: "Do not change any words. Sing exactly as written." 지시
```


### §UE-7. Negative Prompting (C-28.2)

**V5 handles exclusions reliably (외부 검증).**

```
✅ Good:
"Acoustic folk, warm, intimate, no drums, no electric instruments"

❌ Bad (over-specified):
"No drums, no bass, no synths, no reverb, no distortion, no..."
```


### §UE-8. Bar Count Targeting (C-65)

```
[INTRO 4] [VERSE 1 8] [PRE 4] [CHORUS 8] 
[VERSE 2 8] [PRE 4] [CHORUS 8] 
[BRIDGE 8] [CHORUS 8] [OUTRO 4]
```

- Approximate (targets, not guarantees)
- intro/outro 길이 제어에 효과적


### §UE-9. Song Editor (V5 신규)

```
| Action | Use |
|---|---|
| Remake | 같은 prompt로 섹션 재생성 |
| Rewrite | 가사/멜로디 변경, role 유지 |
| Extend | 섹션 꼬리에 bars 추가 |
| Reorder | 섹션 이동 |
| Delete | 약한 영역 제거, transition 엔진 처리 |

Workflow:
1. 풀 곡 생성
2. 약한 섹션 식별
3. Remake/Rewrite individual
4. Extend 1-2 bars 트랜지션
5. Delete weak → 엔진 transition smoothing

Note: Extend 2-3 max per song.
```


### §UE-10. Voices & Custom Models (V5.5, Pro/Premier)

#### §UE-10.1 Voices (voice cloning)

```
- 15초-4분 audio upload
- 4 credits per creation
- 18+ age-gated
- Consent box mandatory

Prompting:
- Drop gender/register descriptors (Voice carries)
- Voice + Persona = redundant
- 1-2 genres + instrumentation
```

#### §UE-10.2 Custom Models (fine-tuning)

```
- 최소 6 original tracks
- Build time 2-5 min
- Up to 3 models / account
- Series/album consistency 직격

Prompting:
- Drop generic production language
- Keep genre + section direction
- Off-brand 트랙은 generic v5.5 권장
```

#### §UE-10.3 My Taste (all tiers)

```
- Passive learning
- Affects autogenerate only, not explicit prompts
```


### §UE-11. Personas

```
- Pro/Premier
- 200 free songs per cycle, then 10 credits
- Most reliable vocal consistency
- December 2025: Personas dominant (Style 충돌 시 Persona 이김)

Best Practices:
- Keep prompts simple (1-2 genres)
- Don't fight Persona
- Move Persona across genres OK
```


### §UE-12. Stem Extraction (12 stems)

```
Vocals / Backing Vocals / Drums / Bass / Guitar / Keyboard /
Strings / Brass / Woodwinds / Percussion / Synth / FX/Other

Workflow:
1. More Actions (...) on clip
2. Get Stems
3. Original OR 12 Track
4. Import to DAW

Cleaner Vocals (double-process):
1. Get Stems on original
2. Get Stems again on extracted vocal
```


### §UE-13. Suno Studio (Premier)

```
- Multitrack Editor (timeline)
- Stem Controls
- MIDI Export
- Audio Upload
- Sample to Song
- Pitch Transpose (±12 semitones, no regeneration)
```


### §UE-14. Troubleshooting (외부 검증)

```
| Problem | Solution |
|---|---|
| Vocal too buried | "lead vocal 1-2 dB louder than band" |
| Mix feels flat | "bus compression 2-3 dB, slow attack/fast release" |
| Arrangement busy | "verse 2: bass rests for 4 bars" |
| Genre drift | Reassert influences mid-prompt |
| Chorus not lifting | "double-time hats; octave guitars" |
```


### §UE-15. Known V5 Limitations

```
- Heavy electric guitars: dirty/blend together
- Acoustic nuance imperfect
- Niche subgenres (metalcore, extreme) miss hallmarks
- Extreme cross-style fusions → muddy
- Quality degrades past 6-7 minutes
- V4.5 may be better for heavy genres (metal, hardcore)
```


### §UE-16. Ownership & WMG Partnership (Nov 2025)

```
- "Commercial use rights" 부여
- "Generally not considered the owner" of generated content
- Suno NOT take revenue share
- New WMG-licensed models 2026
- Current models will be DEPRECATED → DOWNLOAD CATALOG (C-70)
```


### §UE-17. K-Pop Suno 직격 (외부 검증 풀바디)

#### §UE-17.1 Core Approach

```
Style Prompt:
- Always include "K-pop" explicitly + production terms
  ("maximalist", "glossy", "dynamic shifts")
- Place vocal description first: "mixed group vocals,
  layered harmonies, K-pop idol group"
- Specify concept: "girl crush", "cute concept",
  "dark concept", "retro disco"
- Include BPM:
  * Dance: 120-140
  * Ballads: 60-80
  * Hip-hop: 80-100
```

#### §UE-17.2 Group Vocal Sound

```
1번 키워드: "mixed group vocals"
보강:
- "layered harmonies"
- "gang vocals"
- "group chant"

Lyrics 어법:
- Parenthetical backing: "I'm on fire (on fire!)"
- [All] / [Group] section tag
- [Rap Verse] tag for different vocal character
```

#### §UE-17.3 Korean-English Code-Switching

```
- Hangul 직접 사용 (V5 better than V4)
- Romanized with hyphens 더 안전 ("Sa-rang-hae")
- [Clear Vocals] / [High Fidelity Vocals] when mixing
- Sections 분리 (Verse Korean / Chorus English)
```

#### §UE-17.4 Switch-Up (Mid-Song Genre Change)

```
[Verse 1]
(Soft R&B groove, gentle piano)
...lyrics...

[Chorus]
(Explosive EDM drop, heavy bass, full energy)
...lyrics...

[Rap Verse]
(Aggressive trap flow, 808 bass)
...lyrics...

[Bridge]
(Stripped-back ballad, solo piano)
...lyrics...

Style: "genre-fluid, dynamic shifts, maximalist K-pop production"
```

#### §UE-17.5 K-pop Section Structure

```
Intro → Verse 1 → Pre-Chorus → Chorus → Post-Chorus →
Verse 2 → Pre-Chorus → Chorus → Rap Verse → Bridge →
Dance Break → Final Chorus (key change up) → Outro

[Dance Break] = "(Instrumental, heavy beat)" + minimal/no lyrics
Final chorus often key change up half-step
```

#### §UE-17.6 K-pop Concept Style Prompts

```
Girl crush:
"K-pop girl group, fierce EDM trap, sassy vocals, heavy bass drop,
chant chorus, 135 BPM, confident attitude, glossy production"

Bright/cute:
"K-pop, bubblegum pop, bright synths, chirpy vocals, catchy hook,
youthful energy, 125 BPM, layered harmonies"

Dark/experimental:
"K-pop, industrial synths, aggressive rap, EDM bass drops, distorted bass,
maximalist chaos, 140 BPM, mixed group vocals"

K-ballad:
"Korean ballad, emotional piano, string orchestra, soaring vocals,
key change final chorus, 70 BPM, cinematic, lush arrangement"
```


### §UE-18. Genre-Specific Tips (외부 검증)

#### Hip-Hop / Rap
- Subgenre: boom bap, trap, lo-fi, nerdcore
- Beat style: 808s, sampled drums, crispy snares
- Flow description if important

#### Punk
- Subgenre: pop-punk, hardcore, skate punk
- Tempo (fast usually)
- Vocal style: snotty, shouted, melodic

#### Electronic
- Specific subgenres: house, techno, IDM, synthwave
- Synth types: analog, digital, chiptune
- BPM critical

#### Folk/Acoustic
- Instruments: fingerpicking, banjo, mandolin
- Tempo + mood
- Vocal intimacy level


### §UE-19. Iteration Tips

```
1. Start broad, refine
2. Log every attempt
3. Adjust one element at a time
4. Try different models (V4.5 vs V5)
5. Use extends to build on good sections
```


# === END 09 USER EXTENSION ZONE v2.0 ===





# ============================================================
# § USER EXTENSION v2.0 v2 — EXCLUDE Auto-Inject SOP
# ============================================================


## §UE-20. EXCLUDE Auto-Inject 자동 점검 (C-75 통합)

Style Box / EXCLUDE 칸 출력 직전 *자동 점검 + 강제 박음*.

### §UE-20.1 5-Tier 우선순위

```
Tier 1: 절대 자동 (모든 COVER)
- stadium reverb live audience crowd cheering
- muddy mix lo-fi compression artifacts
- autotune robotic vocal (vocoder 의도 X 시)

Tier 2: 컨셉 보호 (방향 따라 자동 발의)
- 컨셉 dark → EXCLUDE: bright cheerful pop, uptempo dance
- 컨셉 bright → EXCLUDE: dark moody melancholic, slow ballad emo
- 컨셉 acoustic → EXCLUDE: stadium production, heavy distortion
- 컨셉 electronic → EXCLUDE: live drums real instruments

Tier 3: Pop Gravity Well 차단
- emo / industrial / phonk / drill / hyperpop 등 약 장르 → EXCLUDE:
  pop chorus, radio polish, modern pop production
- EDM / hardstyle → EXCLUDE:
  pop ballad emotional, indie folk acoustic

Tier 4: V5 Token Bias 차단 (8 단어 점검)
- Neon / Echo / Ghost / Silver / Shadow / Whisper / Crystal / Velvet
- 가사에 2+ 발견 → EXCLUDE에 "Style autofill of [단어] bias terms"

Tier 5: 시점 anchor 위반 차단
- "2025 K-pop" → EXCLUDE: early 2010s K-pop, second-gen K-pop
- "vintage 70s" → EXCLUDE: modern R&B, 2020s production
- "2024 Rosé 솔로" → EXCLUDE: Teddy Park signature, fierce EDM trap
```

### §UE-20.2 자동 박음 출력 형식

```
📋 EXCLUDE 박힘 (Auto-Inject + 운영자 명시):

Tier 1 (자동):
- stadium reverb live audience crowd cheering
- muddy lo-fi mix compression artifacts

Tier 2 (컨셉 보호):
- bright cheerful pop (컨셉 dark)

Tier 3 (Pop Gravity 차단):
- pop chorus radio polish (장르 emo)

Tier 4 (Token Bias):
- (해당 사항 없음 — 가사 점검 통과)

Tier 5 (시점 anchor):
- early 2010s K-pop (시점 2025 명시)

[운영자 명시]:
- no falsetto
- no auto-tune

총: 7개 / 240자 / 통과
```

### §UE-20.3 한도 룰 v2.0 v2 갱신

```
200자 = 권장 baseline (외부 정설)
실제 한도:
- 5-7개 / 200-300자: 안전권
- 8-10개 / 400자+: 깎기 점검 필요 (우선순위 낮은 거)
- 11개+: V5 arrangement unstable 경고

깎기 우선순위 (한도 초과 시):
1. Tier 5 (시점 anchor) — 절대 사수
2. Tier 1 (anti-drift) — 절대 사수
3. Tier 4 (Token Bias) — 절대 사수
4. Tier 3 (Pop Gravity) — 약한 장르면 사수, 강하면 깎기 가능
5. Tier 2 (컨셉 보호) — 우선순위 가장 낮은 거부터 깎기
6. 운영자 명시 (제일 마지막 깎기, 그래도 운영자에게 확인 발의)
```

### §UE-20.4 자동 점검 트리거 (출력 전 1회 의무)

```
CREATE/COVER 출력 직전:
1. 현재 EXCLUDE 박힘 확인
2. Tier 1-5 박을 거 자동 결정
3. 중복 / 충돌 점검
4. 한도 점검 (200자 권장, 300자 한도 권장)
5. 표기 + 출력

Reinforcement Pass (C-13) 통합:
✅ Gate 27/27 / 🔧 EXCLUDE Auto-Inject [N개] / 🔍 Diagnostic [발견]
```


# === END 09 USER EXTENSION v2.0 v2 ===
