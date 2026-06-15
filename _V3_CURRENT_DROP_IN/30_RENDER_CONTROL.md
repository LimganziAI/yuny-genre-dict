# 30. RENDER CONTROL — Suno-native 렌더 제어층 (가설 라벨 규율)
# VERSION: v1.0 (2026-06-10) — 이력은 CHANGELOG.txt
# Scope: §1(CREATE/COVER)·§4(EXCLUDE)·§12(Sliders)·28(PD)·19(진단) 위에 얹히는 제어 모델.
# 라벨 규율: [공식]=Suno 공식 / [연구-가설]=공개 연구 기반 설계 가설(내부 구조 단정 금지) /
#            [커뮤/低·中·高]=커뮤니티 관찰+신뢰도 / [가설]=미검증(케이스 3회 前 룰 승격 금지).

## §1. 렌더 제어 모델 — H1-H4 (전부 가설: 운영 규칙의 받침으로만, 사실처럼 서술 금지)
- **H1 [연구-가설/정합 높음]** 오디오 조건 = 멜로디·보컬·구조(의미층) 보존 우세 / 텍스트 조건 =
  스타일·텍스처 주도. Suno 공식 Covers 정의("멜로디 유지+스타일 재해석")와 정합 [공식].
  → 운영 규칙: **지킬 것은 preserve map에 명시, 바꿀 것은 substitution map에 장르어로 명시 — 미명시 = 무보호.**
- **H2 [가설]** Audio Influence = 오디오 vs 텍스트 조건의 비율 제어. 멜로디 생존 60-75 / 균형
  45-55 / 재해석 20-40. 수치는 케이스로만 보정.
- **H3 [커뮤/高 정합]** 텍스트는 비결정 soft guidance — 섹션 태그·바카운트·코드 표기는 방향
  제시지 악보가 아니다(코드를 써도 단순화·이탈 가능). → 1렌더 실패 ≠ 결함: 동일 프롬프트
  2-3회 재생성이 진단 0단계(§15 랜덤 분리의 받침).
- **H4 [커뮤/中]** 조건 신호는 분산된다 — 과밀 태그+고정 Style Influence = mush. → lean 우선순위
  스택(§3 Prompt Designer의 받침). "첫 80-120자 최중요"는 **운영 가설로만** 유지(Position 1 규율).

## §2. Bone / Skin / Finish — CREATE↔COVER 배분의 상위 문법 [C-140]
Bone(tempo·key/tonal·멜로디 컨투어·코드 모션·섹션 아크) = **CREATE 전속** /
Skin(악기 팔레트·그루브·보컬 텍스처·편곡 이벤트) = **COVER 주도**(모드 b 전면 교체) /
Finish(음질 스택·스테레오/뎁스·다이내믹스·vocal corridor) = **COVER 전속**.
모드 a(refine) = Skin 일부+Finish / 모드 b(transform) = Skin 전체+Finish.
위반 신호: CREATE에 Finish 언어 · COVER가 Bone 재서술(30% 룰 초과) · "멜로디 살려" 빌드에 preserve map 부재.

## §3. COVER 순서 감사 8체크 + 라우팅 (출력 前)
①타겟 마이크로장르 앵커 ②preserve map ③substitution map ④보컬 정체성 ⑤섹션/에너지 이벤트
⑥음질 스택(6그룹 전체) ⑦Final/Outro 보존 ⑧Audio Influence 의도 동기화. 순서 위반 = 변환 실패 위험.
- **Cover↔Remaster:** 정체성 맞고 사운드만 강화 → 모드 a/Remaster 경로 / 방향 전환 → 모드 b [커뮤/中].
- **장편 불안정·긴 인트로 소스:** Start At로 멜로디 구간부터 → 최강 섹션 Cover → Extend →
  Replace Section → Get Whole Song. 구조 단순화는 *거동이지 결함이 아님* [커뮤/中].
- **소스 권리 게이트:** 업로드 기반 COVER는 original/licensed 확인 1줄 필수 — ToS는 권리 없는
  업로드·타인 Voice Model·impersonation 금지 [공식]. 케이스에 input_audio_ownership 기록.

## §4. Pairing Risk 보정열 (28 P-라이브러리에 부착 — AI 수치 전부 [가설])
| 조합(28 연동) | AI[가설] | 보컬 매몰 | EXCLUDE lockout | 스택 우선 |
|---|---|---|---|---|
| sparse acoustic×dense electronic (P2/P3) | 50-60/b | 中 — "verses stay sparse" | 신스 과밀 차단 | STEREO·DYN |
| ballad×arena rock (P13) | 50-65/b | **高** — corridor+"drive on instruments only" | crowd/live T1 강제 | VOCAL·DYN |
| city-pop×modern funk (P12) | 50-60/b | 低-中 | 80s gated snare 류 명시 | LOW END·STEREO |
| trap×orchestral dark (P11) | 55-65/b | 中 — 현악 mid 침범 | pop chorus/radio polish | LOW-MIDS·LOW END |
| cinematic×pop (P8) | 50-65/b | 低 | 과장 트레일러 라이저 | DYN·HM/AIR |
| bossa/soul×loud (P1) | 60-70/b | **최고** — corridor+"+1dB above bed" | smeared low-mid는 실제 발생 시만 | VOCAL·LOW-MIDS |

## §5. Prompt vs Studio 분리 — 재프롬프트 낭비 차단
**프롬프트가 푼다:** vocal corridor · arrangement space · controlled reverb/delay · center
reservation · 섹션 depth — 구조·장르·정체성 문제.
**Studio가 푼다:** fader 밸런스 · pan · 외과적 EQ · 스템 보수 — 국소 밸런스·한 악기 톤.
약한 스템 주의: 어쿠스틱기타/피아노/스트링/BGV [커뮤/中] (드럼/리드보컬/베이스는 신뢰).
좋은 렌더 + 한 악기만 큰 문제 = Studio 먼저, 재프롬프트 금지. 같은 일로 재프롬프트 3회째 = 결함.

## §6. 주파수→언어 사전 (증상 → 프롬프트 문구)
200-400Hz pileup → "competing low-mid layers carved, warm body without cloud" ·
2-5kHz 쏘임 → "smooth high-mid presence, de-essed lead" ·
8-14kHz fizz → "controlled air, no brittle sheen" ·
보컬 매몰 → "lead vocal forward, center protected, vocal corridor 500Hz-3kHz" + "spacious mix,
vocal-forward" [커뮤/中] ·
킥-베이스 뭉개짐 → "centered kick/bass separation, mono sub, short sidechain where genre-appropriate".
**과잉 방지:** 스택은 장르별 압축하되 6그룹 커버리지 유지 — DAW 매뉴얼化 금지, "polished clean mix" 빈말 금지(11/20 연동).

## §7. EXCLUDE = Drift-Lockout 분류명 (§4 6-Tier·우선순위와 동일체 — 명명만)
①언어 드리프트 ②보컬/성별 드리프트(공식: Exclude는 악기·스타일·**보컬 스타일** 지원 —
Lyrics "[female vocals]" × Exclude "male vocals" 페어링 [공식]) ③소스장르 끌림+팝 중력
④관중/라이브 ⑤믹스 결함(guarded — 보컬공간 죽이는 키워드 금지, §4) ⑥딜리버리(rapping 류)
⑦엔딩(abrupt) ⑧로보틱 보컬. 전용 Exclude 필드가 inline 부정보다 **일관되게 강하다**
(신모델에서 inline 부정 일부 파싱 보고 [커뮤/中] — 룰 불변: 부정은 전부 EXCLUDE로).
엔트리 수: ~5개 클린 한계 관찰 [커뮤/中] — 룰 변경 보류(A/B 대상), 6+ 필요 시 high-signal만 묶음어 압축.

## §8. Slider Failure Map [전부 가설 — 케이스 3회 前 수치 확정 금지]
melody lost in cover → AI +5~10 · transform too timid → AI -10~20 또는 source lockout 강화 ·
vocal buried → AI 재점검+corridor 재강조 · generic → Style Influence↑+Position-1 재작성 ·
chaotic → Weirdness↓+프롬프트 밀도↓ · too safe/flat → Weirdness +10 또는 signature motif 1개 spike.

## §9. 진단 owner 보강 (19 연동 — 증상→소유 필드, C=CREATE L=Lyrics Cv=COVER E=EXCLUDE S=Sliders)
transform too timid → Cv·E·S / melody lost → Cv·S / 보컬 로보틱 → E·Cv(키워드 가드) /
과잉 리버브·관중 → E·Cv / 듀엣 한 목소리 붕괴 → C·L·E(slot-1 선언) / 한국어 번역투처럼 들림 → L(29) /
레퍼런스 미스 → C·Cv(§11 폴백 사다리). 0단계 = 동일 프롬프트 2-3회 재생성 → 이후 **단일 변수**만
교체(Position-1/preserve/lockout/AI±10/큐 밀도/스택/BPM×음절 중 1).

## §10. Suno v5.5 사실 + 운영 메모 (2026-03-26 [공식], 재검증 큐 대상)
- **Voices**(Personas 확장+클로닝 Pro/Premier): Voice 고정 시 음색어는 줄여도 *연기·자세 디스크립터는
  유지*(Voice=음색, 연기는 텍스트). 타인 Voice 클로닝 금지 [공식 ToS].
- **Custom Models**(6트랙+, 계정당 3): 캐릭터 카탈로그 프로젝트에 유효 — 정체성 글자 예산을 편곡으로 전환.
- **My Taste**: 과거 생성에서 학습 → **구식 사운드 강화 리스크**(운영자 관찰) — era 점프 곡에서는
  EXCLUDE로 상쇄, 드리프트 의심 시 비활성 검토.
- **Studio**(12스템·EQ·Warp): 마이너 믹스 흠의 사후 구제 가능 → §5 분리 기준 적용.
- 모델 업데이트 후: [커뮤] 기반 문구·[가설] 수치 전부 재검증 대상(세대별 사실 뒤집힘 전례: inline 부정).
