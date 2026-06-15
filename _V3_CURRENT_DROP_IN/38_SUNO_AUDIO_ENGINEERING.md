# 38. SUNO AUDIO ENGINEERING & TRANSPLANTS — 믹스 제어·음질·v5.5 거동 + 외부 이식
# VERSION: v1.0 (2026-06-15) — 이력은 CHANGELOG.txt
# 근거: 11(프로덕션디자인)·20(프로덕션aware)·§D 7-zone·§4 EXCLUDE + 현행 Suno 엔지니어링 web 검증(2026-06)
# 위상: 11/20(일반 프로덕션 이론)·37(편곡 현대화)와 구별 — 이 파일은 *Suno 특이적 믹스/음질 제어 어휘 + v5.5 거동 + 외부 이식*.
# 발동: 음질·믹스·사운드·머디·"보컬 묻힘"·"얇다"·"촌스러운 사운드" 피드백 / COVER 음질 스택 / 새 곡 프로덕션 결정.
# 핵심: ★Suno 머디·아마추어 = *프로덕션 서술어 부재*(고장 아님). 믹스는 프롬프트 어휘로 *제어 가능*. 충돌 태그가 게인을 깎는다.

## §0. 원리 — Suno 믹스는 프롬프트로 제어된다
"sad rock song"처럼 프로덕션 서술 0 → Suno 디폴트 밸런스(머디·얇음). 외부 검증: 머디의 최빈 원인은
*기술 고장이 아니라 서술어 부재 + 충돌 태그*. → 명시 프로덕션 어휘를 박고, 충돌("quiet aggressive")을 없앤다.

## §1. MIX-CONTROL 어휘 — 각 단어가 Suno 출력에 하는 일 (★핵심 이식)
```
의도                         →  Suno가 먹는 프로덕션 어휘
─────────────────────────────────────────────────────────────────
보컬 우선(믹스 우선순위)      →  ★보컬 서술을 프롬프트 *앞쪽*에 = Suno가 보컬을 믹스에서 우선.
                              "present vocals, vocal forward, lead vocal one dB above the bed,
                              space kept for the lead vocal, clear expressive vocals"
보컬 타이트 vs 자연          →  "compressed"(보컬 조여 또렷·앞으로) / "uncompressed, open"(자연·덜 두드러짐)
분리·또렷                    →  "clear mix, separated instruments, defined frequencies,
                              frequency separation, each instrument in its own space"
EQ 방향                      →  "warm"(미드↑) / "crisp·bright"(고역↑) / "airy"(초고역) / "round·dark"(로우미드)
                              — 장르·의도에 매칭(밝힘 vs 따뜻)
스테레오                      →  "wide stereo image" / "intimate narrow mix" / "[element] in mono"
드럼 펀치                     →  "punchy drums, tight transients, snappy kit"
저역                          →  "sub-forward bass, mono sub 20-80Hz, sidechained to the kick"
음질 앵커(블런트 — 절제)      →  "polished, professional studio quality, hi-fi, radio-ready, balanced EQ"
                              ※ 블런트라 *구체 서술 우선*, 이건 보조. 남발 X.
```

## §2. SUNO가 프로 대비 빠뜨리는 3가지 → 프롬프트 처방 (이식: Undetectr 분석)
```
Suno 결핍                    →  프롬프트 처방
─────────────────────────────────────────────────────────────────
1. 미세 타이밍(인간은 정박 X) →  "organic imperfect groove, human feel, not quantized,
                              slight push-pull, loose pocket"
2. 노이즈 플로어(룸/장비 noise)→  "room tone, analog warmth, tape character, recorded-in-a-room,
                              subtle air" (의도적 lo-fi면 "tape hiss, vinyl crackle")
3. 마스터된 다이내믹 레인지    →  "open dynamics, transient contrast, dynamic range, not brickwalled"
                              (37 §3.2 다이내믹>음압 연동)
```
→ 이 셋을 깔면 "AI 같음"이 줄고 인간 프로덕션 결이 산다.

## §3. MUDDY-FIX 프로토콜 (최빈 엔지니어링 실패)
진단: 머디 = 로우미드 누적 + 분리 부재 + 충돌 태그.
처방(순서):
1. **분리 어휘 주입:** "clear mix, separated instruments, defined frequencies, frequency separation".
2. **EQ 방향:** 보컬 코리도어 보호("vocal corridor 500Hz-3kHz protected"), 머드 컷 암시("clean low-mid").
3. **충돌 태그 제거:** "quiet aggressive"·"fast slow"·"lush minimal" 같은 모순 → 코히어런트로.
4. **7-zone 규율(§4):** 동일 zone 3+ 악기 → EQ separation 큐.
5. ★보컬 죽이는 키워드는 EXCLUDE에서도 빼라(muddy/compressed/vocoder 과다 = 역트리거, §4 연동).

## §4. 주파수·공간 (D 7-zone + 20 + 11 통합)
7-zone: Sub 20-60 / Bass 60-250 / Low-mid 250-500 / **Mid 500-2k(vocal corridor)** / Upper-mid 2k-4k /
Presence 4k-8k / Air 8k-20k. 동일 zone 3+ 악기 충돌 → "frequency separation" 큐 + 악기 음역 분산.
마스터: -14 LUFS / -1 dBTP(스트리밍). sub 80Hz 이하 mono. de-esser 5-8kHz.
★COVER = 최종 음질 형태: 풀 스택 필수(7-zone 공간배치 + vocal corridor 보호 + sub mono + de-esser +
plate reverb short + 마스터 -14 LUFS + era anchor 첫 200자). 모드 b(변환)도 *새 장르 맞춤* 음질.

## §5. 장르별 엔지니어링 (장르마다 음질 처방이 다르다 — 이식: 장르 포뮬러)
```
장르          핵심 음질 어휘 (Style에)
──────────────────────────────────────────────────────────────
folk/acoustic  room tone, dynamic, minimal compression, intimate close-mic, fret/breath noise left in
pop            polished, punchy drums, present vocals, wide stereo, controlled compression, radio-ready
hip-hop/trap   sub-forward mono bass, hard transients, vocal upfront and dry, 808 glide
rock           managed guitar wall, drum punch, midrange energy, analog warmth, raw edge
electronic     sub-bass mono, sidechain pump, wide bright synths, crisp top, tight low end
R&B/neo-soul   warm, smooth, intimate vocal, round sub, Rhodes texture, late-night air
lo-fi          tape-saturated drums, vinyl crackle, warm analog bass, pitched-down sample, tape hiss
cinematic      wide spatial image, dynamic swells, deep sub, orchestral depth, comfortable-melancholy
```

## §6. ★v5.5 프로덕션 거동 (이식 — 현행 검증, 모르면 사고남)
- **★era 태그 = 프로덕션 공격적 편향:** "1980s"를 trap에 넣으면 게이트 리버브 드럼·신스 텍스처 *강제 주입*.
  → **현대 프로덕션 + 빈티지 악기**를 원하면 *명시 분리*: "modern production, vintage 1970s guitar tone"
  (한 단어로 뭉뚱그리면 era가 프로덕션까지 끌고 감). 의도한 레트로면 era로 유도, 아니면 분리.
- **★"instrumental"은 *맨 끝* 배치:** v5.5에서 instrumental을 끝 아닌 자리에 두면 보컬이 새어 나옴. 무보컬이면 *마지막 태그*.
- **충돌 서술 금지:** "quiet aggressive"·"fast slow ballad"·"lush minimal" = 모델 혼란 → 코히어런트(§3 Prompt Designer).
- **첫 20-30단어 최강:** Suno는 앞 20-30단어를 가장 강하게 읽음 → 거시 결정(장르·보컬·핵심 텍스처) 앞배치(§3 Position 가중과 일치).
- **반복 생성 + Extend + 베스트 결합:** 한 방에 포기 X, 같은 프롬프트 2-3회 재생성으로 Suno 랜덤 격리(§15).

## §7. 외부 이식 로그 (무엇을 가져왔고, 무엇을 이미 가졌나)
```
외부 시스템 기능              우리 상태
──────────────────────────────────────────────────────────────
mix-control 프로덕션 어휘     ★이식(§1) — 흩어진 것 통합·체계화
Suno 3대 결핍 → 처방          ★이식(§2)
v5.5 era/instrumental 거동    ★이식(§6) — 신규
장르별 음질 포뮬러            ★이식(§5)
6-layer(Genre·Mood·Inst·Vocal·Structure·Production)  이미 보유 = CREATE 8항목(§2) — 우리가 더 세밀
Artist DNA(not "in style of") 이미 보유 = 5-Layer 우회(§11) — 우리가 더 엄격
critic pass 품질 채점         이미 보유 = 카운슬(31) + 출력 계약(36) — 우리가 더 다층
pronunciation engine          이미 보유 = 25 사운드엔진 + 07/08/26/27 + romaji 룰
debugger table                이미 보유 = §F 신고→처방 + 19 진단
Album Mode(다트랙 코히전)     ★경량 이식(§8) — 신규
```

## §8. ALBUM / CATALOG 코히전 모드 (이식 — 운영자 24+ 카탈로그 대응)
여러 곡을 *일관된 사운드 DNA*로 묶되 곡마다 변주. 발동: "앨범으로/시리즈로/같은 결 여러 곡/캐릭터 EP".
- **공유 DNA 고정(앨범 전체):** 보컬 정체성(캐릭터/Persona) · 프로덕션 팔레트(핵심 악기 3-4·음질 스택) ·
  마스터 타깃(-14 LUFS) · 무드 계열 · era anchor. → 매 곡 Style에 동일 DNA 블록 재사용.
- **곡별 변주(단조 방지):** 마이크로장르·BPM zone·키·화성 사건·템포·편성 밀도를 곡마다 시프트(§10 다양성).
- **v5.5 Persona/Custom Model 연동:** 보컬 일관 = Persona / 사운드 DNA = Custom Model(6+ 트랙 fine-tune). 카탈로그 24+ = Custom Model 자산화(§14).
- 출력: 곡마다 8필드 + "앨범 DNA 블록"(공유분) 헤더 1회 명시.

## §9. 출력 직전 엔지니어링 체크 (내부, 36/37과 함께)
```
□ 보컬 우선순위 = 프롬프트 앞쪽? present/forward/corridor 보호?
□ 분리 어휘(clear/separated/defined frequencies) 있나? 머디 위험 시 §3?
□ EQ 방향(warm/crisp) 장르 매칭? 스테레오 명시?
□ Suno 3대 결핍 처방(organic groove·room tone·open dynamics) 중 ≥1?
□ era 태그가 프로덕션 끌고 가나? 현대+빈티지면 분리 명시(§6)?
□ 무보컬이면 "instrumental" 맨 끝? 충돌 태그 0?
□ 장르별 음질 포뮬러(§5) 반영? COVER면 풀 스택?
□ 앨범/시리즈면 공유 DNA 블록 일관(§8)?
```
하나라도 빠지면 보강 후 출력(표면 보고 X — 고쳐서 낸다).
