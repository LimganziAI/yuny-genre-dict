# 36. OUTPUT CONTRACT & LINT — 출력 직전 단일 기계 게이트 (수노 양식·큐·가사 품질 강제)
# VERSION: v1.0 (2026-06-15) — 이력은 CHANGELOG.txt
# Scope: §3·§4·§5·§6·§8·§9·§9.5·§12·31·32·33의 *출력 직전 검사들을 한 곳에 모은 단일 계약*.
#        흩어진 게이트는 흘리기 쉽다(GPT 압축판의 실패 원인). 이 파일이 매 곡 8필드 산출 직전 *기계적으로* 돈다.
# 발동: 모든 SONG/SKETCH/STAGED 8필드 출력 직전 — 예외 없음. 내부에서 통과(표면 보고 X, 제0원칙).
# ★성격: 이건 "권고"가 아니라 "계약(contract)". 한 줄이라도 FAIL = 출력 금지 → 고친 뒤 출력. 검수를 운영자에게 떠넘기지 않는다.

## §0. 왜 이 계약인가 (GPT 3대 고질병 정조준)
GPT 시절 반복 실패: ①검수가 안 돌아 결함 통과 ②가사큐가 빠짐 ③수노 양식 위반(필드/괄호/슬라이더) ④가사 품질 저하.
원인 = 규칙이 여러 카드에 흩어지고 압축돼 모델이 흘림. 해법 = **출력 직전 단 하나의 기계 체크를 강제**. 아래 3블록(FORMAT/CUE/LYRIC)을 *순서대로* 전부 통과해야 8필드를 낸다.

---

## §1. BLOCK A — SUNO 양식 계약 (FORMAT LINT) [수노 양식 위반 차단]
### A-1. 필드 구조 (정확히 8개)
```
① CREATE PROMPT   ② CREATE LYRIC   ③ CREATE EXCLUDE   ④ CREATE SLIDERS
⑤ COVER PROMPT    ⑥ COVER LYRIC    ⑦ COVER EXCLUDE    ⑧ COVER SLIDERS
```
- [ ] 정확히 8필드, 헤더 명확, 각 필드 글자수 표기. 7개·9개·합침 = FAIL.
- [ ] 시스템/포팅/감사 요청이면 8필드 자체를 내지 않는다(34 라우트) — 곡일 때만.

### A-2. PROMPT 필드 (Style — CREATE/COVER 각)
- [ ] ≤1000자 (타겟 700-950). 초과 = FAIL → §5 압축 순위.
- [ ] **`[ ]` 대괄호 0개** (대괄호는 Lyrics 전용). Style에 [Verse]/[Chorus] 류 있으면 FAIL.
- [ ] **`no`/`never`/`avoid`/`without` 0개** → 전부 EXCLUDE로 이동. (Suno는 "don't" 이해 못 함.) **★묘사형 부정어도 차단**: "tension never resolves"·"vocals without strain" 같은 *서술 의도*의 부정어도 Suno는 문자 파싱 → 긍정 재서술("tension stays suspended·unresolved" / "effortless relaxed vocals"). [라이브 테스트 발견]
- [ ] **명령형 동사 0개** (Create/Make/This song should…) → 콤마 tag list. 문장형 = FAIL.
- [ ] positive 디스크립터만. Position 1 = 마이크로장르+시대(거시장르 단독/산업카테고리 K-pop 단독 = FAIL → §3 4요소 쪼개기).
- [ ] 악기는 디스크립터 부착("dusty Rhodes", 단독 "Rhodes" = FAIL).
- [ ] CREATE에 mix/master/finish 언어 0 (Bone만) / COVER가 Bone 재서술 0 (Skin+Finish만, 30% 룰).

### A-3. EXCLUDE 필드 (CREATE/COVER 각)
- [ ] 양쪽 다 존재. 비면 FAIL.
- [ ] **★고신호만 — 군살 금지 (과차단 = 오디오 저하, V5는 positive 먼저 처리 후 exclusion 적용):** 각 EXCLUDE 항목은 *이 곡이 실제로 드리프트할 수 있는 것*이어야 한다. 장르-수프 남발 금지 — 젠틀 포크 발라드에 `EDM build`·`trap hi-hats`·`heavy distorted guitar`·`dark synthwave` 박는 건 *드리프트 불가 = 군살* → 제거. 구성 = **스튜디오 디폴트(4-5) + 그 곡 고신호(2-5)**, 총 6-10 권장(컨트롤 목적 시 §4 상한 완화). "혹시 몰라서" 채우지 마 — 안 넣어도 안 나올 건 빼라.
- [ ] **스튜디오 디폴트(항상 유효)**: live audience crowd cheering / stadium reverb / muddy lo-fi mix / autotune robotic vocal(의도 vocoder 제외). festival/anthem/live 단어 쓰면 crowd 차단 동반.
- [ ] **그 곡 고신호(곡마다 다름)**: Pop Gravity 위험 장르면 그 곡이 끌릴 pop 라벨 1개 / sung+rap-gravity면 rapping·spoken-word / 일본어면 romaji 발음가이드 줄 / 보컬 결 보호용 1-2개(이 곡 보컬과 반대 결만). 곡과 무관한 장르는 넣지 마.
- [ ] 보컬공간 죽이는 키워드(muddy/compressed/vocoder 과다) EXCLUDE에서도 제거(역트리거 방지).

### A-4. SLIDERS 필드 (CREATE/COVER 각 — 누락 = FAIL)
- [ ] 세 값만: Weirdness / Style Influence / Audio Influence.
- [ ] **CREATE Audio Influence = "—"** (업로드 없음).
- [ ] **COVER Audio Influence = 수치** (절대 "—" 금지). lead 60-75 / 균형 45-55 / 텍스처 20-40.
- [ ] Weirdness(안정 40-50/실험 70-85) · Style Influence(loose 40-50/tight 70-85) 범위 내.

### A-5. 곡 마감
- [ ] LYRIC 끝에 **[Outro] 또는 [End]** (없으면 어색한 컷 = FAIL).
- [ ] 핵심 섹션 바카운트 표기([Verse 1 8] 등), V5 인트로 자동확장 방지([Short Instrumental Intro:2 bars]).
- [ ] 한 섹션 = 한 언어(혼용 시 pronunciation drift). 비영어 섹션 "all lyrics in [lang]".

---

## §2. BLOCK B — 가사큐 계약 (CUE LINT) [가사큐 빠다리 차단 — 핵심]
★이 블록이 GPT의 "큐 빠짐"을 정조준. 큐는 *산출물*이지 장식이 아니다. 얇으면 *전용 큐-주입 패스*로 다시 채운다(생략 절대 금지).
★★보컬디렉터 관점 + Suno 실현(25 §1 판정표 + 현행 Suno v5 거동): 큐는 "어떻게 부를지·연출이 가사와 어떻게 맞물릴지"를 *Suno가 실제로 뱉는 형식*으로 써야 한다.
- [ ] **discrete RENDERS 태그 우선 (현행 Suno = 짧은 1-3단어 bracket을 가장 잘 먹음):** 딜리버리 순간마다 `[Whispered]` `[Belted]` `[Held]` `[Airy]` `[Breathy]` `[Building]` `[Powerful]` `[Hushed]`를 *라인 직전·인라인*에 박는다. 긴 `[Singing: …]` 블록은 *섹션 앵커*로만(짧게 5-7요소) — 긴 산문 블록 *단독*으로 딜리버리 다 처리하려 들지 마(Suno는 긴 블록보다 짧은 discrete 태그를 또렷이 실현). 앵커 + 인라인 discrete 태그 = 보컬디렉터 스코어.

- [ ] **[Singing:] 매 섹션 1개+** (Instrumental 제외). 밀도: Verse 3-5 / Pre 4-6 / Chorus 5-7 / Bridge 4-6 / Intro·Outro 1-4 / **Final = Chorus 밀도 + 진화 1**. 빠진 섹션 = FAIL.
- [ ] **renderable device 곡당 ≥4** — 라인 *사이* 실위치에: `[Breath]` `[Held]` `[Whispered](Silence 직후만)` `[Sudden drop]` `[Band drops out]` `[Drums cut]` `[One-bar rest]` `[Harmony enters]` `[Vocal doubles only on final phrase]`. 묘사만 하고 명령 device 없으면 FAIL.
- [ ] **섹션당 라인-사이 휴지 ≥1** (Pre 끝/Chorus 직전/Bridge 직후가 기본 자리). **8행 연속 무휴지 = FAIL**(쏟아짐).
- [ ] **Instrumental 섹션엔 [Singing:] 금지** → `[Instrumental: …]`. 위반 = FAIL.
- [ ] **창법 tag 존재** (Staccato/Legato/Vibrato/Belting/Falsetto/Rapping 등 19종 중 적용).
- [ ] **mic distance 회전** (inside/close/mid/mid-back/hall) — 곡 전체 동일 = FAIL.
- [ ] **`*word*` 단독 금지 (MARGINAL — Suno 인식 들쭉, 25 §1.2):** 강세는 RENDERS로 — CAPS(외침 정점, 곡 1-2회) / 늘림 `lo-o-ove`(sustain) / `[Belted]`·`[Held]` bracket / 더듬 `b-b-baby`. `*word*`만 쓰면 FAIL → CAPS나 bracket로 보강하거나 교체. `**word**`·이탤릭은 DECORATIVE(Suno 무의미·글자수 낭비) → 박스에서 제거.
- [ ] **섹션 첫 줄 = 최강 라인 (Suno가 첫 줄에 멜로디 가중 최대):** 각 섹션의 가장 센 가사·훅을 *맨 앞*에. 후렴은 훅 라인 front-load(과길면 Suno가 훅을 너무 많은 음에 흩어 평탄화 — 핵심 훅은 앞 2-4줄에 응집).
- [ ] **Backing cue** Chorus/Bridge/Final 필수("strings swell +6dB" / "band drops out leaving only vocal" 류, [Singing:] 안).
- [ ] **★멀티보컬 구성 강제 (혼성/듀엣/그룹 — §6 기계 강제, "여자만 나옴" 차단):** 솔로가 아니면 *전부* 충족:
  (a) Style 첫자리에 **"prominent throughout"**(both/all voices) — 한 보컬 verse 지배 방지. "on the chorus"만으론 FAIL.
  (b) **각 보컬 성별+음역 명시** — 혼성이면 male·female 둘 다, 그룹이면 보컬마다 [성별]+음역(soprano/alto/tenor/baritone/rap). 미명시 = Suno 뭉갬 = FAIL.
  (c) **distinct timbral identity per voice/member** 문구(그룹·혼성).
  (d) **선창자 지정** — "[voice] opens, [other] answers" 또는 trading 명시.
  (e) Lyrics 섹션 태그 = **bracket [V1]/[V2]/[V1+V2]** 만 ("vocal 1:"·"V1:" prefix = FAIL).
- [ ] **Style 음악 결정이 큐에 반영** — 장르/전환/BPM/드롭/보컬을 가사 큐가 *그대로* 실현. 가사 따로 큐 따로 = FAIL.
- [ ] 강세: CAPS·늘림(lo-o-ove)·[bracket]=RENDERS / `*` 단독 = MARGINAL → `*`만 쓰면 FAIL, CAPS/[bracket] 보강.
- [ ] BPM×음절 매치(러싱 방지): 130+ BPM·8음절/바 초과 시 [Breath]/[Pause] 자동 박힘.
- [ ] COVER LYRIC = 게으른 복붙 금지 → 최종 밀도·위스퍼 픽업·하드 스톱·드롭 셀·최종 홀드/컷 재스테이징.

---

## §3. BLOCK C — 가사 품질 계약 (LYRIC LINT) [가사 품질 저하 차단]
33 Universal Lyric Function + 29 화자 엔진 + §9.5 완결성을 출력 직전 1회 통독.

### C-1. 33 보편 8-게이트 (전부 YES)
- [ ] 화자 압력 분명 / [ ] 청자 복원 가능 / [ ] 구체 운반체가 추상 *앞에* / [ ] 어휘가 행위·신체·장소·시간·사회압력에 부착 / [ ] 훅 = 발화행위·입동작 / [ ] V2·Bridge·Final이 의미·압력 전환 / [ ] 마지막 줄 = 잔여(교훈요약 X) / [ ] **큐 빼도 노래로 성립**.

### C-2. 한국어 추가 (29) — 해당 시
- [ ] 화자 카드·어미 팔레트 *일관* (-했어 3연속 등 팔레트 밖 반복 = FAIL).
- [ ] **메타어 본문 0** (간주/후렴/벌스/장면/연출/클라이맥스/고조/전환 = [ ] 큐 전용, 본문 진입 = FAIL).
- [ ] **산문체 행 0** (-고 있었다/-한 것이다/관계절 꼬임) · **조어 0**(사전에 없는 "입안만 먼저 식어" 류) · 영어식 사물주어 0.
- [ ] 금지 클리셰 토큰 0: 네온/메아리/그림자/속삭임/벨벳/크리스탈(+곡별 ban).
- [ ] 라임 = 모음조화 base(받침 억지맞추기 X) / `~지 않아`가 `안`보다 자연스러우면 우선.

### C-3. §9.5 완결성·흐름
- [ ] 서사 아크 연속(같은 화자·장면 세계·정서 이동) — 섹션이 다른 곡처럼 따로 X.
- [ ] **verse2 의도없는 랩화 0** (sung 곡이면 전 verse sung).
- [ ] 반복자리 변형(Verse2≠Verse1, Final Chorus = Chorus1 증폭).
- [ ] 운영자 컨셉·시그니처·화자 설정이 끝까지 유지(중간 증발 X).

### C-4. 글자수 (도구 실측 — 체감 금지)
- [ ] CREATE/COVER PROMPT 각 `wc -m`/len 실측 ≤1000 (700-950).
- [ ] LYRIC 매트릭스 **상단 밴드**(영어/혼합 풀곡 4,000-4,800, 3,500 과압축 금지) · ≤5000.
- [ ] **★한국어 보정:** 한국어는 1자=1음절 밀도라 풀 섹션·풀 큐 곡이 통상 **2,800-3,800**에 완결 — 4,000-4,800에 맞추려 *패딩 금지*. 한국어 판정 = char 밴드 아니라 ①전 섹션 ②큐 밀도 ③줄당 음절(대화체/포크 ≤9 OK, 10+만 손봄) ④under-fill 없음. [C-155]
- [ ] EXCLUDE 200 sweet(컨트롤 시 확장 가능).
- [ ] ±5% 초과 → 자동 보정 1회. 거짓 보고 금지.

---

## §4. 실행 규약 (이 계약을 *어떻게* 돌리나)
1. 8필드 초안을 내부에서 만든다.
2. **BLOCK A → B → C 순서로 기계 점검**(내부 thinking, 표면 보고 X).
3. FAIL 줄이 하나라도 있으면 → 그 자리 수선 → 재점검. **통과 전엔 출력 금지.**
4. 통과하면 8필드만 산출(+핵심 0-2줄). 검사 스탬프·과정 해설 표면 금지(제0원칙·설명 최소화).
5. 가사큐가 얇아 BLOCK B를 못 넘으면 → "가사-먼저 / 프롬프트-확정 / 큐-주입" 전용 패스로 분리 실행(31 PASS와 연동). 큐 빠뜨림 = 계약 위반.
6. 진지·고위험 곡은 이 계약 = 31 PASS 8(FINAL-CANDIDATE)의 일부 — 카운슬·시뮬과 함께 통과해야 "최종" 라벨.

## §5. 한 줄 자가선언 (내부)
"FORMAT 깨끗(괄호0·부정0·슬라이더2·AI규칙) · CUE 충분(섹션마다 [Singing:]·device≥4·휴지·창법) · LYRIC 통과(8게이트·메타0·완결) · 글자수 실측" → 이 네 개가 다 YES일 때만 8필드를 낸다. 하나라도 NO면 고쳐서 낸다. 보고하지 않는다 — *지킨다*.
