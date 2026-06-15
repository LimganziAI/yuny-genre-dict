# Suno-Native PD & Render Control Layer
경로 후보: `knowledge-evolving/production-engineering/suno_native_render_control.md`
성격: GitHub 상주 풀바디(Knowledge 21번째 카드 아님 — 20-slot 보존). 카드 11/14/15/16/17이 GITHUB FETCH ROUTE로 이 파일을 가리킨다.
출처: RESEARCH_SUNO_NATIVE_RENDER_CONTROL_v2.md (2026-06-10). 모든 수치·메커니즘 주장은 라벨 유지.

## TRIGGER
새 곡 아키텍처 직전(card 11과 동시); COVER 결과 진단(멜로디 사라짐/변환 약함/보컬 묻힘/구조 단순화); Audio Influence·렌더 제어 질문; Studio↔프롬프트 경계 질문; "왜 이렇게 나와?" 류 렌더 메커니즘 질문.

## MUST APPLY
**렌더 제어 모델 — 전부 [가설], 내부 구조 단정 금지. 운영 규칙의 받침으로만:**
- H1 [가설] 오디오 조건 = 멜로디·보컬·구조 보존 우세 / 텍스트 조건 = 스타일·텍스처 주도 → "지킬 것은 preserve map에 **명시**, 바꿀 것은 substitution map에 **장르어로 명시**" — 미명시 = 무보호.
- H2 [가설] Audio Influence = 오디오 조건 vs 텍스트 조건의 비율 제어 → 멜로디 생존 60-75 / 균형 45-55 / 재해석 20-40 (수치는 케이스로만 보정).
- H3 [가설·커뮤/高 정합] 텍스트는 비결정 soft guidance — 태그·바카운트·코드 표기는 방향 제시지 악보가 아니다 → 1렌더 실패 ≠ 결함; 동일 프롬프트 2-3회가 진단 0단계.
- H4 [가설·커뮤/中 정합] 조건 신호는 분산된다 — 과밀 태그+고정 SI = mush → lean 우선순위 스택. "첫 80-120자 최중요"는 **운영 가설로만** 유지(확정 금지).

**Bone / Skin / Finish 3단 (CREATE↔COVER 배분의 상위 문법):**
- Bone = tempo · key/tonal color · melody contour · chord motion · section arc → CREATE 전속
- Skin = instrument palette · groove · vocal texture · arrangement events → COVER 주도(모드 b 전면 교체)
- Finish = quality stack · stereo/depth · dynamics · vocal corridor → COVER 전속(CREATE에 Finish 언어 = 결함)
모드 a(refine) = Skin 일부+Finish / 모드 b(transform) = Skin 전체+Finish. Bone은 어느 모드에서도 COVER가 재서술하지 않는다(30% 중복 룰의 상위 원리).

**PD Blueprint 9항목 → 필드 맵 (Dossier보다 먼저 — Blueprint가 정하고 Dossier가 상속):**
user feeling→감각번역(card 02) · intended listener→보컬 태도+가사 register · scene→Position 1-2 era/scene+Dossier · emotional arc→section arc(CREATE)+cue 에너지 곡선(LYRIC) · vocal identity→anchor 5+CREATE 1-3슬롯 · genre/era anchor→Position 1 · arrangement density→Density Governor · hook thesis→Dossier+CREATE hook shape · ending image→outro cue+final-image 줄.

**Density Governor (프롬프트에 영어로 박는다):**
Verse ≤3-4 simultaneous layers · Pre = +tension layer + percussion motion · Chorus = hook-support layers, "space kept for lead vocal" · Bridge = harmonic 또는 texture turn 정확히 1개 · Final Chorus = **새 lift 정확히 1개** · Outro = signature motif maintained. 위반 증상: 산만/벽소리/보컬 매몰/파이널 과적.

**Pairing Risk Matrix (card 11 P-코드에 위험·보정 열 부착 — AI 수치 전부 [가설]):**
| 조합 | AI [가설] | 보컬 매몰 위험 | EXCLUDE lockout | stack 우선 |
|---|---|---|---|---|
| sparse acoustic bone × dense electronic skin (P2/P3) | 50-60/b | 中 — "verses stay sparse" | "wall of synths" 류 과밀 차단 | STEREO·DYN |
| ballad bone × arena rock skin (P13) | 50-65/b | **高** — corridor + "drive on instruments only" | crowd/live T1 강제 | VOCAL·DYN |
| city-pop bone × modern funk skin (P12) | 50-60/b | 低-中 | "80s gated snare, city-pop clean chorus guitar" | LOW END·STEREO |
| trap bone × orchestral dark skin (P11) | 55-65/b | 中 — 현악 mid 침범 | "pop chorus, radio polish" | LOW-MIDS·LOW END |
| cinematic bone × pop skin (P8) | 50-65/b | 低 | 과장 트레일러 라이저 차단 | DYN·HM/AIR |
| bossa/soul bone × loud skin (P1) | 60-70/b | **최고** — corridor + "lead vocal +1dB above the bed" | "smeared low-mid wash"는 실제 발생 시만 | VOCAL·LOW-MIDS |

**Prompt vs Studio 경계:**
프롬프트가 푼다 — vocal corridor · arrangement space · controlled reverb/delay · center reservation · 섹션 depth. Studio가 푼다 — fader 밸런스 · pan · 외과적 EQ · 스템 보수(약한 스템: 어쿠스틱기타/피아노/스트링/BGV [커뮤/中]). 재프롬프트 기준: 구조·장르·정체성 = 프롬프트 / 국소 밸런스·한 악기 톤 = Studio 먼저. Remaster = 정체성 유지+사운드 강화 / Cover = 방향 전환 [커뮤/中]. 긴 인트로 소스 = Start At로 멜로디 구간부터; 장편 불안정 = 최강 섹션 Cover → Extend → Replace Section → Get Whole Song [커뮤/中].

**Cue-to-Render Device Map [내부+커뮤 정합]:**
강(단독 OK) — ALL-CAPS 1-2회/곡 · 모음 늘림(lo-o-ove) · [Whispered][Belted][Held][Airy][Raspy] · [Sudden Absolute Silence: 1 bar] · [Chorus|Anthemic|Stacked] · speaker labels. 약(단독 금지 — 강 장치와 결합) — *asterisk* · **bold** · 정밀 강세 표기.

**Slider Failure Map [전부 가설 — 케이스 3회 전 수치 확정 금지]:**
melody lost in cover → AI +5~10 · transform too timid → AI -10~20 또는 source lockout 강화 · vocal buried → AI 재점검+corridor 재강조 · generic → SI↑+Position-1 재작성 · chaotic → Weirdness↓+프롬프트 밀도↓ · too safe/flat → Weirdness +10 또는 signature motif 1개 spike.

## FIELD PLACEMENT
Bone→CREATE PROMPT · Skin/Finish→COVER PROMPT · Blueprint 9항목→위 맵 분산 · Density 문구→CREATE(section arc)+COVER(events) · lockout→EXCLUDE · AI/W/S→SLIDERS · Studio 권고→필드 밖 1줄(8필드 오염 금지).

## FAILURE SIGNALS
- CREATE에 Finish 언어 / COVER가 Bone 재서술(30% 초과).
- preserve map 없는 "멜로디 살려" 빌드.
- Final Chorus lift 2개+(과적) 또는 0개(평탄).
- Studio 일을 3회째 재프롬프트(또는 역).
- [가설] 수치를 확정처럼 서술.

## GITHUB FETCH ROUTE
인접: production-engineering/cover_quality_stack_runtime.md · prompt-patterns/(승격 페어링·lockout) · cases/failure/(증상 일치).

## OUTPUT PHRASES
- "Bone은 CREATE가 다 쥐고, COVER엔 Skin+Finish만 — 겹치면 평균치로 끌려가."
- "멜로디 증발 = preserve map 미명시 + AI 저값 조합 [가설]. 명시+65로 재투입."
- "이건 프롬프트가 아니라 Studio 일이야 — 스템에서 한 악기만 내리면 끝."
- "수치는 아직 가설. 같은 프롬프트 두 번 더 + 변수 하나만 바꿔서 케이스로."

## COMPRESSION PRIORITY
Keep: H1-H4 한 줄씩 · 3단 분리 · Density Governor · 매트릭스 6행 · Prompt/Studio 기준. Drop first: 매트릭스 비고 · Blueprint 세부 맵(card 11 보유).
