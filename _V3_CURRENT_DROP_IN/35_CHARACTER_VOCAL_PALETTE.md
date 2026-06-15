# 35. CHARACTER VOCAL PALETTE — 29 캐릭터 보이스 (Project 상주, GitHub 404 무관)
# VERSION: v1.1 (2026-06-15) — 이력은 CHANGELOG.txt
#   v1.1: 2026-06-11 Suno/YouTube 카탈로그(365곡 복원) 실사용 근거를 각 시드에 📊로 보강 + 신규 캐릭터 §2.6 추가
# Scope: §6(보컬 디렉션)·29(화자 엔진)의 캐릭터 데이터층. 이름 호출 시 *여기서* 보이스를 불러온다.
#        ★이 파일이 Project에 있으므로 캐릭터 불러오기는 GitHub(yuny-suno-os 404) 없이도 작동한다.
# 발동: 운영자가 캐릭터명/별칭(루크/레베카/카샤스/봉남/타투…)을 호출할 때 → INDEX 매칭 → 해당 [VOICE] 적재.

## §0. 운용 규칙 (절대) — 이름은 라우팅 키지 가사·필드가 아니다
- **이름/별칭은 라우팅 키일 뿐 — Suno 필드(Style/Lyrics/EXCLUDE)에 절대 진입 금지.** 항상 *Suno 디스크립터로 변환*해서 박는다(아래 각 캐릭터 seed).
- **기본 적재 = [VOICE] 블록(음성 물리)만.** 세계관/역할([LORE])은 운영자가 "걔 설정대로/세계관으로"를 *명시 호출*할 때만 — 읽힌 lore는 "무시" 선언과 무관하게 생성을 오염시킨다. (이 파일엔 [VOICE]만 수록; lore는 별도 보관.)
- **이름 = 음성/장르 약칭이지 고정 설정 아님.** 곡이 필요로 하면 장르 자유 변경 — 키/음역/peak/BPM음절/편곡밀도를 *선택한 딜리버리로 재계산*. 보컬 정체성은 *레코드에 도움 되는 만큼만* 보존.
- **반복 사용으로 비슷해지기 시작하면 한 축만 회전:** 그루브 / 시대 / 가사 레지스터 / 악기 / 섹션 역할. (29 Expression Ledger와 연동.)
- 캐릭터 호출 = 화자(29 Speaker Card)와 별개 — 캐릭터는 *음색*, 화자는 *말하는 사람*. 둘 다 잡아야 한다.

## §1. INDEX — 먼저 이걸로 매칭 (별칭 → 캐릭터 → §2 seed 적재)
| 캐릭터 | 별칭 | 음성 씨앗 한 줄 | 장르 존 |
|---|---|---|---|
| 루크/Luke | 루크, Luke | female 맑은 밝은 고음 클리어 팝 | bright pop, EDM topline, clean ballad |
| 마리/Marie | 마리, Marie | female 밝고 파워풀 허스키 J-rock 펑크 | J-rock punk anthem, punk rock, bittersweet pop-rock |
| 네르/Nerh | 네르, Nerh | female 미성 기반 시원한 직선 rock, 끝 airy falsetto | pop rock, alt rock, tropical-night hybrid rock |
| 레베카/Rebecca | 레베카, Rebecca | female 여리고 떨리는 순수 브레시 미성 | acoustic pop, intimate ballad, music-box chamber pop |
| 령/Ryeong | 령, Ryeong, Ryung | non-singing 로봇/글리치 샘플 (FX용) | hyperpop FX, glitch EDM, cyber ambient |
| 체니/Chenny | 체니, Chenny | female 초고속 하이톤 떼쓰는 펑크 랩 | comic punk rock, hyper punk rap, chaotic pop rap |
| 라이니/Laini | 라이니, Laini | female 나른 유혹 재즈 R&B 미성 | jazz pop, smooth R&B, lounge pop |
| 세리카/Serica | 세리카, Serica | female 차분 예의 맑은 글래시 톤 | clear pop ballad, ambient pop, elegant synth ballad |
| 샐리/Sally | 샐리, Sally | female 비음 애교 재즈펑크 톡싱 | jazz funk, disco pop, sassy city groove |
| 테피/Tepi | 테피, Tepi | female 따뜻 진솔 소울팝 미드레인지 | soul pop, acoustic pop, warm folk pop |
| 카샤스/Kashas | 카샤스, Kashas | male 미드하이 스크래치 멜로딕 그런지 싱잉랩 | grunge funk rock, melodic rap-rock, alt funk rock |
| 올레그/Oleg | 올레그, Oleg | male 굵고 거친 하드록, 제한된 scream peak | hard rock, metal anthem, industrial rock |
| 월콧/Walcott | 월콧, Walcott | male 하이톤 처절 속사포 랩 | fast hip hop, rap-rock, panic punk rap |
| 크래더/유진/Crader | 크래더, 유진, Crader, Eugene, Yujin | male 힘 뺀 나른 인디 도시 보컬 | city pop, lo-fi indie, soft synthpop |
| 박봉남/Bongnam | 박봉남, 봉남, Bongnam | female 까랑까랑 재기발랄 sassy 팝랩 | pop rap, comic dance-pop, sassy funk pop |
| 젠슨/Jensen | 젠슨, Jensen | male 감정 없는 저음 나레이션 (spoken용) | narration FX, dark synth interlude, trip-hop spoken word |
| 현암/Hyeonam | 현암, Hyeonam | male 타령조 구수한 분석적 랩 (받침 살림) | fusion gugak, taryeong rap, Korean folk-hop |
| 미첼/Mitchell | 미첼, Mitchell | male 세련 시크 시티팝 R&B (2갈래) | city pop, synthpop, sophisticated R&B |
| 타투/Tatoo | 타투, Tatoo, Tattoo, 시스타투, Sis Tatoo, シスタトゥー | female dry close-mic 멀티모드 (A 느와르/B 샤프하이/C 여린dry) | trip hop, dark jazz, chic synthpop, dry indie dance-pop |
| 우나/Una | 우나, Una | female 부서질 듯 속삭임 몽환 dream-pop | dream pop, ambient pop, ethereal ballad |
| 마르티나/Martina | 마르티나, Martina | female 중저음 섹시 벨벳 재즈 라틴 | Latin pop, jazz pop, bossa-inflected pop |
| 타라한/Tarahan | 타라한, Tarahan | female 맑고 달콤 quirky K-인디 미성 | K-indie acoustic, quirky folk pop, bright acoustic pop |
| 웰링/Welling | 웰링, Welling | male 정석 남성 팝/락 (다용도 기본형) | rock, pop rock, mainstream pop |

## §2. [VOICE] SEEDS — Suno 디스크립터로 박을 실제 문구 (이름 대신 이것)

**루크/Luke** — `female high-pitched clear bright pop vocal, clean youthful upper register, light idol-adjacent clarity, straight melodic phrasing` · 맑은 고음 미성, 곡 따라 EDM topline/발라드/청량 팝 변형 · EXCL: thick chest belt, raspy rock vocal, mature diva tone, dark smoky delivery
  · 📊 실사용 27곡 — 음역 C4-E5(1) · 빈출: clear; : high-pitched; sweet; bright; high-pitched

**마리/Marie** — `female bright powerful husky J-rock punk vocal, slightly raspy edge, raw heartfelt emotion, passionate desperate chorus lift, bittersweet rock anthem delivery` · 후렴에서 후회·답답함 밀어붙임, 날 선 감정(두꺼운 디바 X) · EXCL: polished idol sweetness, operatic belt, metal growl, soft breathy-only
  · 📊 실사용 48곡 — 음역 A3-E5(2), B3-F5(1) · 빈출: sweet; the female vocal must be clear; gentle delivery with quiet; the delivery is soft and gentle; clear diction

**네르/Nerh** — `female mid-high piercing rock vocal, powerful straight projection, bright chest-mix belt, thin-to-medium body, open-throat release, phrase endings feather into airy falsetto` · 앞공명 직선, 끝만 가성/숨 · EXCL: thick diva belt, shout-scream, raspy harsh yell, idol nasal chant
  · 📊 실사용 26곡 — 음역 A3-E5(1), B3-F5(1) · 빈출: clear; powerful; sweet; no falsetto; low-mid range

**레베카/Rebecca** — `female high-pitched pure delicate breathy vocal, trembling fragile tone, close-mic intimacy, soft sustained endings` · 숨소리·취약함이 장점, 작은 호흡·긴 여운·가까운 마이크 · EXCL: strong punk attack, fast rap, thick low chest, brassy diva chorus
  · 📊 실사용 20곡 — 음역 표기없음 · 빈출: warm; gentle; : high-pitched; delicate; airy

**령/Ryeong** — `non-singing robot voice samples, glitch fragments, spectral whispers, rhythmic SFX, vocoder punctuation` · 메인 보컬 X, 리듬·효과음·글리치 이벤트용 · EXCL: full lead vocal, warm soul singing, natural acoustic realism
  · 📊 실사용 18곡 — 음역 표기없음 · 빈출: sweet; the female vocal must be clear; the delivery is soft and gentle; high-pitched cute vocals; growling

**체니/Chenny** — `female extreme high-pitched child-like rapid-fire punk rap, bratty shout-chant, comic chaos, sharp syllable attack` · 짧은 훅·말맛·과장 chaos 강, 긴 멜로디엔 조절 · EXCL: smooth adult R&B, slow elegant ballad, low monotone narration
  · 📊 실사용 26곡 — 음역 C4-F5(3), B3-E5(1) · 빈출: cheeky; sassy; child-like; clear; explosive shouts

**라이니/Laini** — `female high-pitched smooth seductive jazz R&B vocal, lazy glide, silky phrasing, smoky upper register, controlled vibrato` · 고음이나 힘 X 미끄러지듯 · EXCL: punk shout, child-like chant, robot FX, raw grunge rasp
  · 📊 실사용 22곡 — 음역 C4-E5(1) · 빈출: seductive; smooth; clear; : high-pitched; :clear

**세리카/Serica** — `female clear calm polite high-pitched vocal, composed diction, glassy tone, gentle controlled breath, elegant melodic restraint` · 정돈된 호흡·신비로운 거리감 · EXCL: messy punk energy, desperate scream, nasal comic delivery
  · 📊 실사용 19곡 — 음역 B3-E5(1), C4-F5(1) · 빈출: clear; gentle; : high-pitched; breathy; warm

**샐리/Sally** — `female high-pitched sassy nasal jazz-funk vocal, playful bends, cheeky phrasing, rhythmic talk-sing, bright groove attitude` · 비음 애교·넉살, 리듬 타고 말하듯 · EXCL: flat polite ballad, ethereal whisper-only, deep monotone male
  · 📊 실사용 29곡 — 음역 F5-G5(2), E4-C6(1) · 빈출: sassy; sweet; nasal; orchestral hits; : high-pitched

**테피/Tepi** — `female clear warm gentle soul pop vocal, honest midrange, soft smile tone, rounded vowels, comforting melodic phrasing` · 위로·온기·부드러운 open vowel · EXCL: cold robotic sample, abrasive punk rasp, screamed rock chorus
  · 📊 실사용 18곡 — 음역 C4-E5(1) · 빈출: gentle; warm; vibe:warm; clear sections; gentle dynamic build

**카샤스/Kashas** — `male mid-high scratchy melodic grunge sing-rap, laid-back groove, dry attitude, raspy hooks, loose rhythmic phrasing` · 츤데레 무심·껄렁, 선율과 랩 사이 · EXCL: clean boy-band pop, deep operatic rock, polite narration
  · 📊 실사용 10곡 — 음역 표기없음 · 빈출: and gritty power chords; piercing screamed chorus; high-pitch emotional shouting; upbeat city pop mastered 132bpm energetic duet bright commercial; verse male focus then female focus clear switches

**올레그/Oleg** — `male deep gruff powerful hard-rock vocal, heavy chest weight, controlled scream peaks, gravel texture, arena-sized aggression` · 샤우팅/포효, Suno 과하면 소음화 → peak 위치 제한 · EXCL: soft indie mumble, delicate falsetto lead, clean idol tone
  · 📊 실사용 13곡 — 음역 A2-G4(1) · 빈출: (oleg):deep; **powerful rock vocal/screamer; ** **aggressive shouts; (walcott):high-pitched; orchestral hits

**월콧/Walcott** — `male high-pitched extremely fast desperate rap, breathless urgency, clipped consonants, panic-drive flow, rap-rock compatible` · 절박·과호흡 에너지 · EXCL: slow crooner, warm acoustic ballad, smooth lounge
  · 📊 실사용 26곡 — 음역 G3–D5(1), C3-G4(1) · 빈출: shouted group harmonies to create a massive wall of sound; : extreme high-pitched; child-like; rapid-fire punk-rap; staccato shouting

**크래더/유진/Crader** — `male laid-back relaxed indie pop vocal, soft lazy diction, light nasal warmth, casual city-pop phrasing, underplayed emotion` · 힘 뺀 나른, 덜 부르는 감정선 · EXCL: screamed rock belt, hyperactive rap, dramatic musical theater
  · 📊 실사용 32곡 — 음역 표기없음 · 빈출: bright; featuring a male vocalist with a clear; slightly raspy tenor voice; the mix is bright and clear; raspy indie tone

**박봉남/Bongnam** — `female high-pitched sassy energetic pop-rap vocal, sharp bright tone, cheeky adlibs, fast comic phrasing, elastic hook delivery` · 깨방정·쌔끈·짧은 말맛 훅 · EXCL: solemn ambient vocal, deep male narration, fragile whisper ballad
  · 📊 실사용 58곡 — 음역 A3-E5(1) · 빈출: sassy; sweet; deep; powerful; high-pitched

**젠슨/Jensen** — `male calm deep monotone narration, dry analytical delivery, low close-mic voice, spoken interjections, minimal melody` · spoken bridge/intro narration/glitch break용 · EXCL: full melodic chorus, bright high pop lead, comic child-like rap
  · 📊 실사용 16곡 — 음역 표기없음 · 빈출: shouted group harmonies to create a massive wall of sound; 4/4 with gentle half-time feel in verses; male mid-tenor warm light sung melodic delivery; soft falsetto stacks in chorus; stepwise conversational verses with gentle leaps on emotional words

**현암/Hyeonam** — `male deep analytical taryeong-style rap, earthy Korean phrasing, rhythmic chant-singing, grounded low resonance, fusion gugak cadence` · 한국어 장단·어미·받침 살림 · EXCL: generic trap imitation, Western diva belting, thin idol nasal chant
  · 📊 실사용 21곡 — 음역 표기없음 · 빈출: the female vocal must be clear; sweet; the delivery is soft and gentle; shouted group harmonies to create a massive wall of sound; ** comedic clash(sassy latin vs deadpan rap)

**미첼/Mitchell** — `male sophisticated city-pop R&B vocal, high smooth chic tone OR husky late-night R&B variant, controlled cool delivery, polished groove` · 곡 따라 high smooth / husky R&B 택1 · EXCL: raw punk scream, comic rapid chant, folk-taryeong cadence
  · 📊 실사용 24곡 — 음역 G3–D5(1) · 빈출: crystal clear; distinct sections:smooth jazz vs modern city pop/r&b; bittersweet; smooth transitions; vocals:v1(martina):mid-low

**타투/Tatoo (멀티모드 — 여성, Sis Tatoo=같은 인물의 모드)** — 곡마다 모드 택1, 멜로디는 안 떨어뜨리고 보컬 색만:
  · 📊 실사용 19곡 — 음역 표기없음 · 빈출: sassy; and low-energy voice; her delivery is almost monotone and spoken-like; with minimal vibrato; she must avoid high notes and emotional belting completely
- Mode A 느와르: `female low-mid dry monotone rhythmic sing-rap, noir close-mic delivery, cool deadpan phrasing, dark jazz/trip-hop pocket, restrained intimate tone, tiny phrase-end grain`
- Mode B 샤프하이: `female bright sharp dry soprano-to-high-mezzo vocal, cool chic deadpan delivery, biting clear Korean diction, dry close-mic tone, low-effort phrasing, melody remains fully sung and lifted`
- Mode C 여린dry: `female light dry upper-mezzo/soprano tone, delicate but centered, close-mic unpolished edge, restrained Korean diction, minimal vibrato, soft phrase ends without whisper collapse`
- ★주의: 낮은 느와르 싱잉랩도 *여성* 모드 — male 아님. EXCL(필요/드리프트 시): male vocal, chesty/thick low alto, heroic belt, cute idol aegyo, glossy sweet soprano, whisper-only, melody flattening, pitch collapse, robotic autotune

**우나/Una** — `female delicate ethereal whisper vocal, fragile airy tone, dream-pop float, close breath texture, soft blurred consonants` · 공기처럼 떠야 함(강하게 치고 X) · EXCL: power belt, fast punk rap, deep gruff rock vocal
  · 📊 실사용 15곡 — 음역 C4-E5(1) · 빈출: vocal: female whispering vocals; ethereal; falsetto high notes; ethereal shoegaze; breath texture 8khz hard-l 30% whisper

**마르티나/Martina** — `female mid-low sexy smooth jazz Latin vocal, mature velvet tone, relaxed rhythmic sway, warm chest color, elegant phrasing` · 중저음 벨벳·리듬 스웨이 · EXCL: child-like high chant, robot glitch voice, punk scream
  · 📊 실사용 20곡 — 음역 표기없음 · 빈출: deep; mid-low tone; husky & breathy whisper intro; powerful diva belting in chorus; vibrato

**타라한/Tarahan** — `female high-pitched clear sweet quirky K-indie vocal, bright nasal sweetness, casual conversational phrasing, youthful acoustic charm` · 아티스트명 금지 → quirky bright K-indie timbre로 분해 · EXCL: mature Latin jazz, deep male narration, heavy metal scream
  · 📊 실사용 11곡 — 음역 표기없음 · 빈출: breathy; bright; clear diction; clear and "kawaii" tone (girl next door vibe); powerful and energetic projection

**웰링/Welling** — `male standard pop-rock vocal, adaptable midrange, clean melodic delivery, light grit on chorus, reliable lead tone` · 다장르 받쳐주는 기본형 · EXCL: extreme-scream-only, robot-narration-only, fragile-whisper-only
  · 📊 실사용 10곡 — 음역 표기없음 · 빈출: delicate female vocalist; powerful melodic singing; part 1 (verse 1 only): ethereal gospel hymn; swelling string orchestra and a delicate; pure female soprano vocal



### §2.6. ★신규 캐릭터 (카탈로그 발굴 — 운영자 확정 완료 2026-06-15)
캐탈로그에서 발견된 신규 캐릭터. 아래 4명은 운영자 확정 — 실사용 tags 근거 기반 [VOICE] seed. (김갑수·하더는 캐릭터 미발전으로 팔레트 제외 — 곡은 catalog에 잔류.)

**Amy/에이미** ✅ — `bright airy summer dance-pop, princess fairytale crystalline, high airy soprano, sweet, not warm` · 📊 7곡 · 음역 A3-E5
  · 빈출 근거: bright airy summer dance-pop; princess fairytale crystalline; high airy soprano; sweet; not warm; glassy fairytale hook
  · 작품군: "Run Sarura Run!" (Bellona·Raiza와 트리오)

**Bellona/벨로나** ✅ — `orchestral hybrid rock, gritty, powerful belting, lead vocal 2-4kHz center dominant nasal groovy, high harmony 3-4kHz bright` · 📊 6곡 · 음역 표기없음(추후 보강)
  · 빈출 근거: orchestral hybrid rock; gritty; powerful belting; 5-layer vocals lead 2-4kHz center dominant nasal groovy; high harmony 3-4kHz hard-L 60% bright; all duck 2-4kHz vocals forward clear
  · 작품군: "Run Sarura Run!" (Amy·Raiza와 트리오)

**Silva/실바** ✅ — `dark orchestral, whispering ASMR, intimate close-mic breathy` · 📊 5곡 · 음역 표기없음(추후 보강)
  · 빈출 근거: dark orchestral; whispering ASMR; ASMR whisper
  · 비고: ASMR/속삭임 결이 핵심 — 음역·멀티모드는 곡 추가 시 보강

**Raiza/라이자** ✅ — `(보컬 추출 부족 — 곡 자료 추가 필요)` · 📊 3곡 (JP 'あと一歩' · 트리오 'Winter Rush' · '네시 반 담장 너머') · 음역 표기없음
  · 정체성 확정: ライザ/라이자 — 작품군 "Run Sarura Run!" (Amy·Bellona와 트리오)
  · ⚠️ 보컬 시드 추출 부족 — 솔로곡 태그 추가 익스포트 시 [VOICE] 보강 필요

> **제외 (팔레트 미등재):** 김갑수(2곡 · "Derville P.I.D." — 캐릭터 미발전, 운영자 판단), 하더(1곡 · "Run Sarura Run!" — 단역, 추후 곡 모이면 추가). 두 캐릭터의 곡은 catalog에 그대로 보존됨.

## §2.5. ★CROSS-CHARACTER 구별화 매트릭스 (서로 절대 안 헷갈리게 — 고유 식별자)
개별 시드는 §2에 있음. 문제는 *비슷한 캐릭터끼리 블러*되는 것. 아래 클러스터는 충돌 위험군 — 각자 **고유 식별자
(THE discriminator)** + **감정-보컬 시그니처(44 연동)**를 박아 절대 안 겹치게. 두 캐릭터가 동시 후보면 *식별자로 가른다*.

### 클러스터 A — 고음 맑은 여성 (6명, 최대 충돌군)
```
캐릭터    고유 식별자(THE one thing)        감정-보컬 시그니처(44)         절대 안 겹치는 점
──────────────────────────────────────────────────────────────────────────
루크      clean idol-clarity + STRAIGHT     밝은 열린 톤, 과한 cry 절제     숨/떨림 강조 X — 가장 깨끗·직선
세리카    GLASSY composed + 거리감          정돈된 호흡, deadpan 허용       유리알 침착·신비 거리(루크보다 차분)
레베카    TREMBLING breathy + close-mic     cry 정점·모음 연장·near-cry      떨림+숨이 *장점*(세리카는 침착)
우나      WHISPER float + 흐린 자음         whisper-sing·들리는 숨·blur      공기처럼 뜸(레베카보다 더 비물질)
타라한    QUIRKY nasal + conversational     밝은 톤·가벼운 quirk            비음 quirky 대화체(미성이나 장난기)
네르      PIERCING rock belt + falsetto끝   belt strain·끝만 airy           앞공명 직선 록(클러스터 유일 belt)
```
→ 가르기: 깨끗직선=루크 / 유리알거리=세리카 / 떨림숨=레베카 / 속삭임뜸=우나 / 비음quirky=타라한 / 록belt=네르.

### 클러스터 B — sassy/비음 여성 (3명)
```
샐리      NASAL aegyo + jazz-FUNK groove    비음 bend·넉살·talk-sing        펑크 그루브 talk-sing(랩 X)
봉남      SHARP pop-RAP + elastic hook      쌔끈 adlib·comic·짧은 훅        팝랩 탄력 훅(샐리보다 랩·날카로움)
체니      EXTREME child + RAPID punk rap     떼쓰는 shout-chant·chaos        초고속 애 같은 punk(가장 과장·빠름)
```
→ 가르기: 펑크그루브=샐리 / 팝랩탄력=봉남 / 초고속애punk=체니.

### 클러스터 C — 스무스/관능 여성 (2명)
```
라이니    HIGH smoky + lazy GLIDE           나른 glide·controlled vibrato   고음 미끄러짐(상부 스모키)
마르티나  MID-LOW velvet + Latin SWAY        중저음 chest·리듬 sway          중저음 벨벳(라이니보다 낮고 라틴)
```

### 클러스터 D — 나른/세련 남성 (3명)
```
크래더    LAZY indie + underplayed          힘 뺀 나른·덜 부르는 감정        인디 도시 언더플레이(가장 힘 뺌)
미첼      CHIC city-pop R&B + polished      쿨 controlled·세련 groove       세련 시크(크래더보다 폴리시·R&B)
웰링      STANDARD adaptable + light grit   안정 lead·후렴 light grit        다용도 기본형(개성보다 신뢰성)
```

### 클러스터 E — 랩/공격 남성 (4명)
```
카샤스    SCRATCHY grunge sing-rap + 무심    껄렁 dry·raspy hook·츤데레       선율↔랩 사이 스크래치(멜로딕)
월콧      HIGH desperate + RAPID panic      과호흡·clipped·절박             고음 속사포 패닉(가장 빠르고 절박)
올레그    DEEP gruff + scream peak          포효·gravel·arena               굵은 하드록 샤우팅(peak 제한)
현암      TARYEONG gugak + 받침 살림         한국어 장단·어미·grounded       타령조 국악 랩(유일 한국 전통)
```

### 클러스터 F — 비보컬/스포큰 (2명)
```
령        ROBOT glitch 샘플 (FX)            기계·vocoder·spectral          메인 보컬 X — 효과음/글리치
젠슨      DEEP human 모노톤 나레이션 (spoken) dry analytical·낮은 close-mic   사람 spoken(령은 기계, 젠슨은 인간 독백)
```

**독립(충돌 적음):** 마리(허스키 J-rock 펑크 anthem) / 테피(따뜻 소울팝 위로) / 타투(여성 멀티모드 A느와르/B샤프하이/C여린dry).

### 운용 규칙 (블러 방지)
- 캐릭터 적재 시 *고유 식별자 1줄을 Position 1-3에 반드시 박는다*(시드 + 식별자). 식별자 빠지면 클러스터 내 블러.
- 같은 곡/세션에서 같은 클러스터 2명 쓰면 → 식별자 + 감정-보컬 시그니처로 *대비 강조*(44).
- 반복 사용 비슷해지면 §0 축 회전(그루브/시대/레지스터/악기/섹션역할) + 29 Expression Ledger.
- 식별자는 *음색 차별점*이지 고정 설정 아님 — 곡이 장르 바꾸면 식별자 유지하되 나머지 재계산(§0).

## §3. 캐릭터 → 8필드 적재 절차
1. 별칭 매칭(§1) → [VOICE] seed 적재(§2).
2. seed를 **CREATE PROMPT Position 1-3 보컬 슬롯**에 디스크립터로 박음(이름 X). 혼성/듀엣이면 §6 어법.
3. EXCL 힌트 → CREATE/COVER EXCLUDE.
4. 곡 장르가 캐릭터 기본 존과 다르면 → 장르 자유 변경 + 키/음역/peak/BPM음절/밀도 재계산(§0).
5. 화자(29)는 별도로 잡음 — 캐릭터 음색 ≠ 화자 인격.
6. 반복 곡이면 한 축 회전(§0) + Expression Ledger 대조(29).

## §4. 출력 어구
- "레베카 불러왔어 — 이름은 안 박고 'female pure delicate breathy, close-mic, soft sustained endings'로 변환해서 CREATE 보컬 슬롯에."
- "타투는 이번 곡에 Mode B(샤프 하이)로 갈게 — 멜로디 유지하고 색만 차갑게."
- "이 캐릭터 기본은 발라드존인데 이번 곡 장르가 펑크라 음역·peak 다시 계산했어."
