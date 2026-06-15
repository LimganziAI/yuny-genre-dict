# ACTIVE GITHUB CASE PATCH — read before legacy body

For repeated failures, use GitHub cases before surface rewriting.

Repository paths:
- `cases/failure/`
- `cases/success/`
- `knowledge-evolving/prompt-patterns/`

Failure workflow:
classify failure -> lock what worked -> search similar cases if useful -> route upstream -> rebuild full output -> record/update case when useful.

Do not treat one failure as a global rule. Promote by:
observation -> case -> repeated pattern -> knowledge patch -> instruction patch.

---

# ACTIVE GPT ROUTE HEADER
- Current GPT file: `19_diagnostics_revision_cascade.md`
- Purpose: Diagnostics, revision cascade, failure routing
- Preserved source aliases: 19_DIAGNOSTIC_CHECKLISTS, §18 MID-FLIGHT RECALL
- Use rule: Use for weak/generic/bad/음질/가사큐/맥락 failures, repeated issues, context lock, cascade. Together: failing upstream files.
- Cross-link rule: Follow `instructions.txt` first. Legacy `# SOURCE:` blocks below are source provenance, not current routing names. If retrieval is thin, search this file by both current terms and preserved source aliases.

---

# v2.3 ACTIVE DIAGNOSTIC GUARD
If user reports that the converted GPT is not using .md knowledge, do not defend the package. Check: current file names vs legacy SOURCE aliases, route selected, missing source function, and whether the failure should have triggered 02/05/06/07/16/19.

If user reports harsh/painful/muddy/buried COVER output, classify as production-aware failure, not lyric/prompt wording failure. Required route: 19 -> 02 COVER mode -> 05 PD preserve/substitution map -> 06 full quality stack -> 03 cue/section preservation -> sliders.

If EXCLUDE contains unrelated languages or random tokens, classify as EXCLUDE seeding failure. Replace with generalized drift terms unless the language actually leaked in output.


# v2.2 routing reinforcement
When the user says the package/system is failing, analyze process and knowledge routing first; do not output Suno fields. When the user says the generated track failed, separate Suno randomness from prompt/routing failure. Repeated audio-quality failure routes to 02+05+06, not surface word replacement.

---

---

# SOURCE: 19_DIAGNOSTIC_CHECKLISTS.md

# ============================================================
# 19_DIAGNOSTIC_CHECKLISTS.md
# 11-Category Diagnostic Routing + Suno-Specific Diagnostics
# YUNY v2.0 "Complete Renaissance Edition"
# Source: SJY051 assets/diagnostic-checklists + bitwize mastering-checklist
# ============================================================

운영자 *진단 발화* → 시스템이 11-카테고리 중 1개 매칭 →
진단 SOP 풀바디 발동. 00_ROUTER.md §3.3 + C-54 통합.


## §0. 라우팅 매트릭스

| 카테고리 | 운영자 발화 신호 | §섹션 |
|---|---|---|
| ① Chorus weak | "후렴 약해" / "hook 안 박혀" / "임팩트 없어" | §1 |
| ② Verse boring | "verse 지루해" / "단조로워" | §2 |
| ③ Melody flat | "멜로디 단조" / "기억 안 나" | §3 |
| ④ Harmony stale | "코드 진부" / "느낌 안 살아" | §4 |
| ⑤ Transition awkward | "넘어가는 게 어색" / "끊겨" | §5 |
| ⑥ Arrangement crowded | "꽉 차" / "muddy" / "복잡해" | §6 |
| ⑦ Groove off | "그루브 안 맞아" / "리듬 어색" | §7 |
| ⑧ Lyric thin | "가사 빈약" / "와닿지 않아" | §8 |
| ⑨ Bridge weak | "브릿지 약해" / "기능 못해" | §9 |
| ⑩ Reference miss | "레퍼런스랑 다르게 나옴" | §10 |
| ⑪ Writer's block | "막혀" / "아이디어 없어" | §11 |

**+ Suno-specific 진단** (§12-§20):
- 가사 쏟아짐 / 후반 풀림 / 평균 회귀 / Pop Gravity / generic 가사 등


## §1. Chorus Weak — 후렴 약해

**증상:** 후렴 임팩트 부족, hook 기억 안 남, verse보다 약함

**진단 5단계:**

```
1. Melody Contour 진단:
   - Verse → Chorus 음역 상승 있나? (1 octave up 권장)
   - Chorus 최고음이 곡 전체 climax인가?
   - 첫 마디 long note (2-4 beats sustained)?
   
2. Harmonic Lift 진단:
   - Verse → Chorus 코드 변화 임팩트 있나?
   - Chorus 첫 코드가 I 또는 IV 진입 (안정 + 폭발)?
   - V/vi (deceptive resolution) 활용?
   
3. Rhythmic Density 진단:
   - Chorus 드럼 패턴 변화 (kick + snare 두꺼워짐)?
   - 16th hat 또는 percussion 추가 있나?
   - Bass 라인이 verse보다 active?
   
4. Lyric Hook 진단:
   - Title이 첫 줄 또는 마지막 줄에 있나?
   - Repetition 2-3회 있나?
   - 영어/한국어 짧고 chantable 한 줄 있나?
   
5. Production Layer 진단:
   - Stacked vocals (3 part harmony+) 있나?
   - Side chain pumping 활용?
   - Reverb tail 길게 풀려나가나?
```

**처방 우선순위:**
1. Melody contour: 음역 상승 + 첫 마디 sustained note
2. Lyric hook: title repetition 2-3회 보강
3. Layered vocals: [Doubled] [Harmony +3rd] [Stacked vocals]
4. Drum density: kick on 1+3 → 1+2.5+3 / hat 16th 보강
5. Harmonic lift: V/vi 또는 borrowed iv 자리 발의


## §2. Verse Boring — Verse 지루

**증상:** Verse 단조, 듣다 졸림, 같은 모티프 반복

**진단 5단계:**

```
1. Phrase Structure 진단 (C-58):
   - Period (8+8) 단조? → Sentence (2+2+4) 또는 Hybrid 권유
   - 라인 길이 다 같음? → 변화 박음

2. Melodic Variation 진단:
   - 같은 모티프 반복만? → transposition / inversion / fragmentation
   - 음역 변화 없음? → octave shift 1-2 자리

3. Rhythmic Variation 진단:
   - Quarter note 위주? → syncopation 1-2 자리
   - 끝마디 같은 결? → 마지막 라인 rhythmic surprise

4. Lyric AID 진단 (C-26.8):
   - Action 없음? → 동사 강화
   - Imagery 없음? → 감각적 디테일 박음
   - Detail 없음? → 구체 명사 박음

5. Arrangement Variation 진단:
   - 같은 악기 throughout? → V2에서 새 악기 1개 추가
   - 같은 dynamic? → V2 살짝 build-up
```


## §3. Melody Flat — 멜로디 단조

**진단 + 처방:**

```
1. Contour Check:
   - 곡 전체 melody 음역 폭 < 1 octave? → 확장
   - Repeated note 4+ → 변화 박음
   - Direction 일관 (계속 상승 또는 하강)? → contour 변화

2. Phrase Endings:
   - 같은 음으로 끝남? → 끝음 변화
   - Stable note만 끝남? → unstable note 1-2 자리

3. Rhythmic Hook:
   - Syncopation 없음? → 1-2 자리 박음
   - 곡 시그니처 리듬 모티프 있나?

4. Range:
   - 보컬 range 안전권만? → 1-2 자리에 chest-to-head transition
   - 최고음이 chorus climax?
```


## §4. Harmony Stale — 코드 진부

**진단:**

```
1. Diatonic Only?
   - I-V-vi-IV만 반복? → borrowed iv / chromatic mediant 발의
   
2. Modal Color 없음?
   - Major key only? → mixolydian (bVII) 또는 lydian (#IV) 발의
   - Minor key only? → dorian (IV major) 또는 phrygian (bII) 발의
   
3. Voice Leading?
   - Root motion 위주? → smooth voice leading 발의
   - Common tone retention 활용?
   
4. Reharmonization 가능?
   - Tritone sub / Backdoor / Modal interchange 발의
```

**처방** (18 §3 Reharm Template 통합):
[Option A: Modal mixture]
[Option B: Tritone sub]
[Option C: Chromatic mediant]


## §5. Transition Awkward — 넘어감 어색

**진단:**

```
1. Section Boundary:
   - Verse → Chorus pivot 코드 있나?
   - V/vi (secondary dominant)로 들어가나?

2. Drum Fill:
   - Section 진입 1 bar 전 fill 있나?
   - Build-up (hat 16th / snare roll / risers)?

3. Pre-Chorus 자리:
   - Verse → Chorus 직접? → Pre-Chorus 박음 권유
   - 4 bar build-up 자리 박음

4. Outro 자리:
   - 갑자기 끊김? → fade out / held note / [End] 태그

5. Modulation:
   - Key change 자리 dramatic? → pivot 코드 또는 direct shift
```


## §6. Arrangement Crowded — 꽉 차 / Muddy

**진단 (C-59 7-zone 활용):**

```
1. 주파수 충돌 점검:
   - 20-60Hz: sub-bass + kick fundamental 충돌?
   - 250-500Hz: bass + low piano + vocal chest 충돌?
   - 500-2kHz: vocal corridor 침범 악기?
   - 2k-4kHz: snare + vocal presence 충돌?
   - 4k-8kHz: hat + cymbal + vocal sibilance 충돌?

2. Stereo Image:
   - 모두 center? → L/R 분배
   - L/R 비대칭? → balance

3. Dynamic Conflict:
   - 모든 악기 forte? → 일부 piano
   - Side chain 활용?

4. Section Density:
   - Verse에 8+ 악기? → 4-5로 축소
   - Chorus에 12+ 악기? → 8개로 축소

5. EQ Carving:
   - 각 악기 frequency 영역 점령했나?
   - 충돌 자리 -2~-3dB cut
```

**처방 (20 PRODUCTION_AWARE 통합):**
1. Vocal corridor 500Hz-3kHz 보호 (다른 악기 -2dB cut)
2. Sub-bass mono 20-80Hz sidechain kick
3. Bass 80-250Hz / Kick 60-80Hz 분리
4. Hat / Cymbal 8k-12kHz / Vocal air 12-20kHz 분리


## §7. Groove Off — 그루브 안 맞음

**진단:**

```
1. BPM 적합?
   - 장르 BPM zone 안인가?
   - 보컬 음절 밀도와 BPM mismatch?

2. Drum Pattern:
   - Kick on 1+3 too plain? → 1+2.5+3 또는 1+3+3.5
   - Snare on 2+4 too plain? → ghost notes / off-beat snare

3. Bass Groove:
   - Bass follow kick exactly? → 80% follow + 20% syncopated
   - Walking / pumping / staccato 결정

4. Hat Pattern:
   - 8th hat? 16th hat? Triplet?
   - 장르 결과 맞나?

5. Vocal Phrasing:
   - On-beat 위주? → behind-the-beat 또는 ahead-of-beat 발의
   - Syncopation 없음? → 박음
```


## §8. Lyric Thin — 가사 빈약

**진단 (C-26.10 anti-patterns 통합):**

```
1. AI Anti-Pattern 체크:
   - 금지 명사 25개 등장? (whisper / shadow / neon / echo 등)
   - 클리셰 16개 등장?
   - Lazy rhyme 10조 등장?
   - 형용사 crutch 10개 등장?

2. AID 분해 (C-26.8):
   - Action 없음? → 동사 박음
   - Imagery 없음? → 감각 디테일
   - Detail 없음? → 구체 명사

3. Verb Wattage (Pat Pattison):
   - 모든 동사 약함 (is/have/want/feel)? → strong verb로 치환
   - Verb specificity 점검

4. Object Writing:
   - 추상어만? → 구체 사물 / 환경 / 감각 박음
   - 7 senses 다 활용?

5. Translation 투 (한국어):
   - 7대 번역투 패턴 (07 §5) 점검
   - 어순 / 조사 어색?
```

**처방:**
1. 금지 단어 치환
2. AID 박음 (Action 우선)
3. Verb 강화
4. Concrete noun 박음
5. 번역투 제거


## §9. Bridge Weak — 브릿지 약해

**진단:**

```
1. Function 점검:
   - Bridge 기능 (대비 / 휴식 / climax 준비) 명확?
   - Verse / Chorus와 differentiated?

2. Harmonic Departure:
   - 같은 key에서만? → modulation 또는 modal mixture
   - Borrowed iv / bVII 활용?

3. Melodic New:
   - 새 모티프? 또는 기존 모티프 변형?
   - Verse / Chorus 안 쓰는 음역?

4. Lyric Pivot:
   - 새 관점 / 새 화자 / 새 시점?
   - Plot twist / emotional shift?

5. Arrangement:
   - Density 변화 (thin → build 또는 build → thin)?
   - 새 악기 introduction?
```


## §10. Reference Miss — 레퍼런스랑 다름

**진단:**

```
1. 13 §2 Confidence Self-Check:
   - BPM 정확 측정?
   - Key/mode 정확?
   - 코드 진행 정확?
   - 시그니처 모먼트 추출 (3-5개)?

2. CREATE/COVER 30% Rule (C-25):
   - 두 박스 비슷? (30%+ overlap)
   - CREATE에 프로덕션 언어 침투?
   - COVER에 멜로디 언어 침투?

3. Style Box Position 1 (C-45):
   - 1번 자리 거시 장르? → 마이크로화
   - 1번 자리 산업 카테고리 (K-pop / J-pop)? → 쪼개기

4. Pop Gravity Well (C-28.2):
   - 무명시 EXCLUDE? → 명시
   - 이상한 조합 강제?

5. Suno 검증 상태:
   - 99c에 비슷한 결?
   - 외부 검증?
```


## §11. Writer's Block — 막힘

**진단 + 처방:**

```
1. Brainstorm 카드 (18 §15):
   - 3-5 카드 옵션 제시
   - 운영자 선택 후 진입

2. Object Writing (C-26.7):
   - 10분 timer, 7 senses 박음
   - 추상어 금지 + 구체만

3. Constraint:
   - 강제 제약 박음 (예: "3개 단어만" / "이미지 1개만")
   - 제약이 창의 trigger

4. Reference 가져옴:
   - 운영자 카탈로그 인접 곡 분석
   - 외부 곡 분석 (13)

5. Genre Jump:
   - 다른 장르로 같은 컨셉 박음
   - 결 환기
```


## === Suno-Specific 진단 (§12-§20) ===


## §12. 보컬 러싱 / 가사 쏟아짐

**C-3.3 5단계 진단:**

```
1. 바카운트 확인/추가:
   - [Verse 1: 16] 명시?
   - 섹션 길이와 가사 라인 수 비례?

2. [Singing:] 밀도:
   - 매 섹션 1개+ 있나?
   - 12바 이상 섹션에 2번째 큐?

3. BPM × 음절 mismatch (14 §2.2):
   - BPM 140+ 한국어 음절 8+ per line? → 러싱
   - BPM 70- 한국어 음절 4 per line? → 비어보임

4. 받침 밀도 (한국어, 14 §2.3):
   - 받침 비율 60%+? → 발음 무거움
   - 받침 30%-? → 발음 가벼움

5. 강제 호흡 큐:
   - 밀집 라인 사이 [Pause half bar] 박음
   - [Pause 1 bar] section between 박음
```


## §13. 후반 풀림

**C-5 + C-48 통합:**

```
1. Throughout discipline 점검:
   - COVER Style Box에 "throughout" 키워드 있나?
   - "[X] maintained throughout all sections including final chorus and outro"
   
2. Final Chorus 마이크로큐:
   - Verse 1급 밀도?
   - [Singing:] [Doubled] [Stacked vocals] 다 박혔나?

3. Outro 마이크로큐:
   - [Held note] [voice trails off]?
   - 새 큐 1-2개 추가?

4. Section Replace 활용 (C-48):
   - 전체 재생성 X
   - Outro만 Remake / Rewrite

5. v2.0 신규: Bar Count Targeting (C-65):
   - [OUTRO 8] 명시 → 길이 컨트롤
```


## §14. 평균 회귀 ("비슷한 곡 나옴")

**C-28 8대 원리:**

```
1. CREATE 1번 자리:
   - 거시 장르 단독? → 마이크로 + 시대 + 시그니처
   - 산업 카테고리? → 쪼개기 (C-40)

2. 장르 스택:
   - 3+ 장르? → 섹션 분할
   - 2개 안에서

3. EXCLUDE:
   - 3-4개 default 있나?
   - Pop Gravity 명시 EXCLUDE?

4. Position Weighting (C-45):
   - Position 1 ~50% 활용?
   - Vocal-first 또는 마이크로 장르-first?

5. CREATE/COVER 30% Rule:
   - Overlap 30%+? → 약한 쪽 재작성

6. v2.0 신규: 21 Genre/Artist Library 활용:
   - 풀바디 우회 어법 다 박았나?
```


## §15. Pop Gravity Well 끌림

**C-28.2:**

```
탈출 3종:
1. 명시 EXCLUDE "no pop, no synth pop, no radio polish"
2. 이상한 조합 강제: "emo industrial" / "orchestral phonk"
3. 전략적 대조: 피하고자 하는 element 거부 강조

V5 외부 검증 (v5-changes):
"V5 handles negative prompting reliably"
→ EXCLUDE 정확 작동, 박음 OK
```


## §16. AI Generic 가사

**C-26.10:**

```
1. 금지 명사 25개:
   shadow / whisper / neon / echo / ghost / 등
   → 운영자 카탈로그에 없는 단어만 박음

2. 클리셰 16개:
   "broken pieces" / "shattered dreams" / "lost in time" 등
   → 구체 시나리오로 치환

3. Lazy rhyme 10조:
   light/night, fire/desire, heart/apart 등
   → Family rhyme / Additive 어법

4. 형용사 crutch 10개:
   beautiful / wonderful / amazing / 등
   → 동사 또는 구체 명사로 치환

5. Verb wattage:
   is/have/want/feel/need 등
   → strong verb (slice / shatter / drown / spin)

6. v2.0 신규: Token bias (C-63):
   Neon/Echo/Ghost/Silver/Shadow/Whisper/Crystal/Velvet
   → V5 model defaulting 주의
```


## §17. 보컬 라벨 안 박힘

**C-29 + C-21:**

```
1. 5-element 풀바디?
   - Gender + range
   - Main timbre
   - Range-by-section
   - Genre inflection
   - Special technique

2. 듀엣 라벨:
   ❌ vocal 1: / vocal 2:
   ❌ V1: / V2:
   ✅ [V1] [V2] [V1+V2]

3. Style Box vocal-first (v2.0 외부 검증):
   "Female pop vocalist, breathy, intimate, ..." Position 1
```


## §18. V5 Intro 너무 길어짐

**C-61:**

```
1. [Intro] 가사 줄임:
   - 1-2줄만 또는 비움
   
2. [Short Instrumental Intro] 명시

3. [Verse] 직접 시작 (intro 없이)

4. Bar Count Targeting (C-65):
   [INTRO 4] 명시
```


## §19. Pronunciation 이슈

**14 USER EXTENSION + bitwize pronunciation-guide:**

```
1. Homograph 점검 (live / read / lead / wind / 등):
   - 의미 따라 phonetic 표기
   - 우회 단어 또는 hyphenation

2. Tech terms (Linux / SQL / API / 등):
   - LIN-ucks / sequel / A-P-I 표기

3. Numbers:
   - "twenty-one" not "21"
   - 예외: '93 (year abbreviation)

4. Korean Hangul:
   - 직접 Hangul 박음 OK (V5)
   - 또는 hyphenated romanization (Sa-rang-hae)
   - V5 작동 검증

5. Multilingual (C-67):
   - 섹션별 언어 격리
   - 비영어 섹션에 "all lyrics in [language], no English"
```


## §20. 7-Point Mastering QC (bitwize 풀바디)

**최종 마스터링 점검:**

```
1. LUFS Target:
   - 장르 매핑 따라 (-7 ~ -16 LUFS)
   - 스트리밍 최종 -14 LUFS / -1.0 dBTP

2. Peak Level:
   - True Peak -1.0 dBTP 이하
   - Clipping 없음

3. Dynamic Range:
   - LRA 4-10 LU 권장
   - 4 미만 → over-compressed
   - 10 초과 → 평탄 (loudness war 부족)

4. Frequency Balance:
   - Low (20-200Hz): 적절
   - Mid (200-2kHz): vocal corridor 보호
   - High (2-20kHz): air / sparkle

5. Stereo Image:
   - Mono compatibility 점검
   - L/R balance
   - 20-80Hz mono fold

6. Vocal Presence:
   - Lead vocal 2-3 dB louder than band
   - De-essing 5-8kHz

7. Mastering Chain:
   - EQ (corrective) → Compression (glue) → 
     Limiter (peak control) → Output stage
   - LUFS 측정 final
```

**자동 발의:** 운영자 *마스터링* 발화 시 20 PRODUCTION_AWARE 풀바디 + 본 §20 적용.


## §21. 자동 라우팅 룰

```
Phase 9 (00_ROUTER §4):
  운영자 진단 발화 분석
    ↓
  11-카테고리 매칭 (§1-§11)
    ↓
  Suno-specific 매칭 (§12-§20)
    ↓
  본 파일 §[해당 섹션] 진단 + 처방
```


## §22. 외부 검증 통합

- SJY051 assets/diagnostic-checklists.md (원천)
- bitwize reference/mastering/mastering-checklist.md
- bitwize reference/suno/tips-and-tricks.md
- Pat Pattison (Verb Wattage / AID / Object Writing)
- 운영자 99d 진단 패턴 학습

# ============================================================
# END OF 19_DIAGNOSTIC_CHECKLISTS.md
# ============================================================
