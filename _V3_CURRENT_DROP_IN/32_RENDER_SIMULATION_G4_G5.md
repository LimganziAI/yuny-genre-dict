# 32. RENDER SIMULATION G4/G5 — CREATE 소스 시뮬 + COVER 최종 시뮬 + 렌더 실패 카탈로그
# VERSION: v1.0 (2026-06-15) — 이력은 CHANGELOG.txt
# Scope: §0.6 PASS 4·6의 실행층. 30(렌더 제어 H1-H4)·14(COVER 변환)·15(음질)·11/28(PD) 위에 얹힌다.
#        30이 "렌더가 어떻게 동작하나(제어 모델)"라면, 32는 "출하 전 그 동작을 어떻게 미리 돌려보나(시뮬)"이다.
# 발동: PASS 4(CREATE 소스 시뮬) / PASS 6(COVER 최종 시뮬) / "강함·최종" 주장 전 / 렌더 결과 진단.
# ★라벨 규율(절대): 이 파일의 모든 시뮬 예측·수치·메커니즘은 [가설]. 내부 구조 단정 금지.
#   운영자 청취 평결만 사실 — 충돌 시 청취가 시뮬을 덮어쓴다(31 FINAL RECORD LAW).

## §0. 이 파일이 푸는 것 — 한 줄
"돌려보기 전에 머릿속으로 렌더를 돌려, 깨질 곳을 미리 잡는다." CREATE는 G4(소스 진실)로, 
COVER는 G5(변환 진실)로 audit. 깨지면 출하 전에 수선. 전부 [가설]이므로 *받침*으로만 쓰고 사실처럼 말하지 않는다.

---

## §1. PASS 4 — CREATE SOURCE SIMULATION (소스 시뮬레이션) [C-146]
CREATE 프롬프트+가사가 만들 **소스 오디오**를 예측한다. 각 항목 [가설], 케이스로만 보정.

| 예측 축 | 무엇을 보나 | 깨짐 신호 | 1차 수선 |
|---|---|---|---|
| melody age | 멜로디가 의도한 시대/나이로 나오나 | 컨투어가 장르 평균으로 회귀 | Position 1 재작성 + 컨투어 구체화 |
| vocal age | 보컬 나이/질감이 화자와 맞나 | 너무 어리거나 늙음 | 보컬 정체성 슬롯(08) 재명시 |
| range/posture | 음역·마이크 자세가 키와 맞나 | 키가 보컬존 밖, 무리한 belt | 키/톤 컬러 조정 + corridor 메모 |
| BPM×syllable grid | BPM에 음절이 안 밀리나 | 가사 러싱(말이 박자 못 따라감) | 음절 줄이거나 BPM/호흡 재설계 |
| lyric rushing | 섹션별 글자수가 호흡에 맞나 | 한 줄에 과밀 음절 | 줄 분할 + breath 큐 |
| source texture | 소스 질감이 toy/벽소리 아닌가 | 과밀 태그 → mush [H4] | lean 스택, 악기 3-4개로 절제 |
| intro density | 인트로가 비거나 과적인가 | 빈 프론트 / 벽 인트로 | Density Governor 인트로 구문 |
| cue obedience | 큐가 실제로 먹을 device인가 | 약장치 단독(*만), 추상 큐 | renderable device(§5)로 교체 |
| preserve strengths | 지킬 만한 강점이 뭔가(→COVER preserve map) | (강점 미식별) | preserve map에 명시 후 COVER로 |
| source failures | 위 중 무엇이 깨졌나 종합 | — | PASS 5 소스 수선 |

**규칙:** CREATE가 깨졌으면 **COVER 가기 전에** CREATE부터 고친다(PASS 5). 뼈 고치고 피부 칠한다.

---

## §2. CREATE G4 AUDIT — 소스 음악 진실 6체크 [C-146]
CREATE PROMPT이 bone/source로서 자기완결인지 감사. (CREATE에 mix/master/finish 언어 = 결함, §1 LAW.)
1. **key ↔ vocal zone** — 키가 보컬 음역/자세와 맞나.
2. **BPM ↔ syllable grid** — 템포가 음절 밀도를 감당하나.
3. **one peak** — 곡에 명확한 피크 1개(파이널 리프트 등)가 설계됐나.
4. **one band** — 주파수 대역에서 리드가 설 자리 1개가 비어 있나.
5. **motif owner** — 시그니처 모티프를 *어느 악기가* 쥐나(오너 명시).
6. **vocal room** — 편곡에 보컬 들어갈 공간("space kept for lead vocal")이 있나.
하나라도 FAIL → CREATE 수선 후 재audit. (G4는 카운슬 PD/vocal/topliner 석과 연동.)

---

## §3. PASS 6 — COVER PRE-FINAL SIMULATION (COVER 최종-레코드 시뮬) [C-146]
COVER가 CREATE 오디오를 **최종 레코드로** 변환할 때 깨질 곳을 예측. COVER는 *제로에서 새 곡 기술 금지* — 
항상 CREATE 오디오를 *변환*한다(30 Bone/Skin/Finish: Bone은 COVER가 재서술 안 함).

**COVER 순서 8체크 (출력 전 — 30 §3과 동일):**
①타겟 마이크로장르 앵커 → ②preserve map → ③do-not-change map → ④substitution/refine map → 
⑤보컬 정체성/음역 보호 → ⑥섹션/에너지 이벤트 → ⑦음질 스택(6그룹 전체) → ⑧Final/Outro 보존. 
순서 위반 = 변환 실패 위험.

**COVER LYRIC 최종 스테이징 체크:** 게으른 복붙 금지(정밀 전달 보존이 목표일 때만 동일). 재스테이징 항목 — 
최종 밀도, 위스퍼 픽업, 하드 스톱, 드롭 셀, 무보컬 필, 훅 강조, 보컬 찹 소재, 최종 홀드/컷 제스처, 소스 렌더 교정.

---

## §4. COVER G5 AUDIT — 변환 진실 삼각형 [C-146]
COVER는 세 개가 *서로 동의*할 때만 G5 통과:
- **preserve map** (지킬 것: 멜로디·탑라인·가사 타이밍·섹션 순서·엔딩 제스처)
- **substitution map** (바꿀 것: 장르어로 명시 — 미명시 = 무보호 [H1])
- **Audio Influence** (오디오 vs 텍스트 비율 [H2])

삼각형 정합 규칙:
- preserve가 "멜로디 살려"인데 AI가 저값(20-40)이면 **모순** → 멜로디 증발 위험. AI 60-75로 올리거나 preserve 명시 강화.
- substitution이 전면 교체(모드 b)인데 AI가 고값(70+)이면 변환이 안 먹음 → AI 45-61로.
- **COVER Audio Influence는 절대 "—" 금지** (CREATE만 "—"). lead 보존 60-75 / 균형 45-55 / 텍스처 재해석 20-40.

**Audio Influence 대역 (16/30 정합):** 70-75 강보존 / 62-68 보존+변환 / 55-61 균형 / 45-54 스킨 교체 / 20-40 느슨 텍스처. 수치는 케이스 3회 전 확정 금지 [가설].

---

## §5. 렌더 실패 카탈로그 + 수선 라우팅 (COVER 결과 진단) [C-146]
운영자가 "이렇게 나왔어" 하면 증상→원인[가설]→수선으로 라우팅. 1렌더 실패 ≠ 결함(같은 프롬프트 2-3회가 진단 0단계 [H3]).

| 증상 | 추정 원인 [가설] | 1차 수선 (필드 어디를) | 슬라이더 [가설] |
|---|---|---|---|
| 멜로디 증발(cover) | preserve map 미명시 + AI 저값 | preserve map 명시 + 재투입 | AI +5~10 |
| 변환 너무 약함(timid) | substitution 빈약 또는 AI 고값 | substitution 장르어 강화 | AI -10~20 또는 source lockout↑ |
| 보컬 묻힘(buried) | corridor 부재 + 과밀 스킨 | "space for lead vocal" + corridor 재강조 | AI 재점검 |
| 평범함(generic) | Position 1 거시장르 회귀 | Position 1 재작성(마이크로장르) | SI↑ |
| 산만/카오스(chaotic) | 과밀 태그 mush [H4] | 프롬프트 밀도↓ | Weirdness↓ |
| 너무 안전/평탄(flat) | 시그니처 부재 | signature motif 1개 spike | Weirdness +10 |
| toy 텍스처 | 과밀+SI 고정 mush | lean 스택 | — |
| 빈 프론트(empty front) | 인트로 밀도 부족 | Density Governor 인트로 구문 | — |
| 약한 드롭(weak drop) | 드롭 셀 설계 부재 | [Sudden drop]/[One-bar rest] 큐 | — |
| 한국어 보컬 묻힘 | corridor + 스킨 충돌 | corridor + "lead vocal +1dB above bed" | AI 재점검 |
| 모노 붕괴(mono) | 스테레오 미설계 | 스테레오/뎁스 구문 | — |
| 거친 고역(harsh highs) | HM/AIR 과다 | EXCLUDE에 harsh/sibilant | — |
| 머디 로우미드 | 저역 분리 부재 | LOW-MIDS 정리 구문 | — |
| 소스-스킨 블리드 | Bone/Skin 경계 붕괴 | COVER가 Bone 재서술하는지 점검(30% 룰) | — |
| 가사 타이밍 드리프트 | 음절 그리드 미스 | 가사 큐 재동기(LYRIC) | — |

**Pairing Risk Matrix (28 P-코드 위험 열 — AI 수치 전부 [가설]):**
- sparse acoustic bone × dense electronic skin → AI 50-60/b, 보컬 매몰 中, "verses stay sparse", STEREO/DYN
- ballad bone × arena rock skin → AI 50-65/b, 매몰 **高**, corridor + "drive on instruments only", VOCAL/DYN
- city-pop bone × modern funk skin → AI 50-60/b, 매몰 低-中, "80s gated snare, city-pop clean chorus guitar", LOW END/STEREO
- trap bone × orchestral dark skin → AI 55-65/b, 매몰 中(현악 mid 침범), "pop chorus, radio polish", LOW-MIDS/LOW END
- cinematic bone × pop skin → AI 50-65/b, 매몰 低, 과장 트레일러 라이저 차단, DYN/HM·AIR
- bossa/soul bone × loud skin → AI 60-70/b, 매몰 **최고**, corridor + "lead vocal +1dB above the bed", VOCAL/LOW-MIDS

---

## §6. PROMPT vs STUDIO 경계 — 재프롬프트할지 스튜디오 일인지 [H 연동]
- **프롬프트가 푼다:** vocal corridor · arrangement space · controlled reverb/delay · center reservation · 섹션 depth · 구조·장르·정체성 변경.
- **Studio가 푼다:** fader 밸런스 · pan · 외과적 EQ · 스템 보수(약한 스템: 어쿠스틱기타/피아노/스트링/BGV [커뮤/中]).
- **재프롬프트 기준:** 구조·장르·정체성 = 프롬프트 / 국소 밸런스·한 악기 톤 = Studio 먼저.
- 긴 인트로 소스 = Start At로 멜로디 구간부터; 장편 불안정 = 최강 섹션 Cover → Extend → Replace Section → Get Whole Song [커뮤/中].
- **Studio 권고는 8필드 밖 1줄로** (필드 오염 금지).

---

## §7. Density Governor (프롬프트에 영어로 박는다) [C-146 연동]
Verse ≤3-4 동시 레이어 · Pre = +tension layer + percussion motion · Chorus = hook-support + "space kept for lead vocal" · 
Bridge = harmonic 또는 texture turn 정확히 1개 · Final Chorus = **새 lift 정확히 1개** · Outro = signature motif 유지. 
위반 증상: 산만/벽소리/보컬 매몰/파이널 과적(lift 2개+) 또는 평탄(lift 0개).

---

## §8. FAILURE SIGNALS (이 파일 자체의 오용 신호)
- 시뮬 [가설] 수치를 확정처럼 서술 → 규율 위반.
- CREATE에 Finish 언어 / COVER가 Bone 재서술(30% 초과).
- preserve map 없는 "멜로디 살려" 빌드.
- Final Chorus lift 2개+(과적) 또는 0개(평탄).
- Studio 일을 3회째 재프롬프트(또는 역).
- 1렌더 실패를 결함으로 단정(2-3회 재생성 생략).

## §9. 출력 어구
- "멜로디 증발 = preserve map 미명시 + AI 저값 [가설]. 명시+65로 재투입."
- "Bone은 CREATE가 다 쥐고 COVER엔 Skin+Finish만 — 겹치면 평균치로 끌려가."
- "이건 프롬프트 아니라 Studio 일 — 스템에서 한 악기만 내리면 끝."
- "수치는 아직 가설. 같은 프롬프트 두 번 더 + 변수 하나만 바꿔서 케이스로."
