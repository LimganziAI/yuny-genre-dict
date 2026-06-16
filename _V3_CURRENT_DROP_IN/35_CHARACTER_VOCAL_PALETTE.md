# 35. CHARACTER VOCAL PALETTE — 29 캐릭터 보이스 (Project 상주, GitHub 404 무관)
# VERSION: v1.1 (2026-06-15) — 이력은 CHANGELOG.txt
#   v1.1: 2026-06-11 Suno/YouTube 카탈로그(365곡 복원) 실사용 근거를 각 시드에 📊로 보강 + 신규 캐릭터 §2.6 추가
#   v1.2: 2026-06-15 카탈로그 솔로곡 분석으로 보컬 정체성 교정 — 젠슨(저음 모노톤 나레이션→청량 밝은 멜로딕 텐서+훅 falsetto, 0014·0039 근거) · 라이자(구버전 'soprano D4–E5'→아이묭 결 alto/mezzo 저음 고정, 고음 드리프트 차단)
#   v1.3: 2026-06-15 운영자 결 디테일 반영 — 네르(서양락커·두께방지) 마리(J-rock 앞으로째는 발성) 레베카(상냥 인디팝·짧은호흡) 루크(살짝 낮음) 체니(bratty 제거) 샐리(funk 두께방지 초고음) 월콧(크라잉+신나는 하드랩 양면) 봉남(마리결+더 랩시) 타투(아이유 결 Mode C 기본+노이즈 저음 Mode A 보존)
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
| 루크/Luke | 루크, Luke | female 맑은 boyish 클리어 팝 (소프라노보다 살짝 낮음) | bright pop, EDM topline, clean ballad |
| 마리/Marie | 마리, Marie | female 밝고 파워풀 허스키 J-rock 펑크 (앞으로 째는 발성) | J-rock punk anthem, punk rock, bittersweet pop-rock |
| 네르/Nerh | 네르, Nerh | female 미성 기반 파워 직선 chest belt — 서양락커, 두께 과하지 않게 | pop rock, alt rock, rock anthem |
| 레베카/Rebecca | 레베카, Rebecca | female 여리고 상냥한 순수 인디팝 미성 (짧은 호흡) | acoustic pop, intimate ballad, music-box chamber pop |
| 령/Ryeong | 령, Ryeong, Ryung | non-singing 로봇/글리치 샘플 (FX용) | hyperpop FX, glitch EDM, cyber ambient |
| 체니/Chenny | 체니, Chenny | female 초고속 하이톤 또랑또랑 어린애 펑크 랩 (bratty X) | comic punk rock, hyper punk rap, chaotic pop rap |
| 라이니/Laini | 라이니, Laini | female 나른 유혹 재즈 R&B 미성 | jazz pop, smooth R&B, lounge pop |
| 세리카/Serica | 세리카, Serica | female 차분 예의 맑은 글래시 톤 | clear pop ballad, ambient pop, elegant synth ballad |
| 샐리/Sally | 샐리, Sally | female 초고음 가벼운 비음 펑크 톡싱 (funk 두께 방지) | jazz funk, disco pop, sassy city groove |
| 테피/Tepi | 테피, Tepi | female 따뜻 진솔 소울팝 미드레인지 | soul pop, acoustic pop, warm folk pop |
| 카샤스/Kashas | 카샤스, Kashas | male 미드하이 스크래치 멜로딕 그런지 싱잉랩 | grunge funk rock, melodic rap-rock, alt funk rock |
| 올레그/Oleg | 올레그, Oleg | male 굵고 거친 하드록, 제한된 scream peak | hard rock, metal anthem, industrial rock |
| 월콧/Walcott | 월콧, Walcott | male 하이톤 — 처절 크라잉 + 신나는 하드 랩 양면 | fast hip hop, rap-rock, panic punk rap |
| 크래더/유진/Crader | 크래더, 유진, Crader, Eugene, Yujin | male 힘 뺀 나른 인디 도시 보컬 | city pop, lo-fi indie, soft synthpop |
| 박봉남/Bongnam | 박봉남, 봉남, Bongnam | female 마리 결 밝은 파워 + 더 랩시 sassy | pop rap, comic dance-pop, sassy funk pop |
| 젠슨/Jensen | 젠슨, Jensen | male 청량 밝은 young tenor, 멜로딕·훅 falsetto | bright J-pop-rock, modern K-indie pop, warm city-pop ballad |
| 현암/Hyeonam | 현암, Hyeonam | male 타령조 구수한 분석적 랩 (받침 살림) | fusion gugak, taryeong rap, Korean folk-hop |
| 미첼/Mitchell | 미첼, Mitchell | female 세련 시크 City Pop Diva, breathy soulful R&B | city pop, sophisticated R&B, synthpop |
| 타투/Tatoo | 타투, Tatoo, Tattoo, 시스타투, Sis Tatoo, シスタトゥー | female dry close-mic 멀티모드 (C 맑고상냥=기본/A 느와르 저음/B 샤프하이) | chic synthpop, dry indie dance-pop, trip hop, dark jazz |
| 우나/Una | 우나, Una | female 부서질 듯 속삭임 몽환 dream-pop | dream pop, ambient pop, ethereal ballad |
| 마르티나/Martina | 마르티나, Martina | female 중저음 섹시 벨벳 재즈 라틴 | Latin pop, jazz pop, bossa-inflected pop |
| 타라한/Tarahan | 타라한, Tarahan | female 솜털 effortless 여린 teen-girl 미성 (pulled-back) | K-indie acoustic, soft folk pop, dreamy acoustic |
| 웰링/Welling | 웰링, Welling | male 정석 남성 팝/락 (다용도 기본형) | rock, pop rock, mainstream pop |

## §2. [VOICE] SEEDS — Suno 디스크립터로 박을 실제 문구 (이름 대신 이것)

**루크/Luke** — `female clear bright boyish pop vocal, clean youthful register sitting a touch lower than the airy sopranos, light idol-adjacent clarity, straight melodic phrasing, minimal vibrato` · 레베카 결이되 ★살짝 낮고 더 또렷·straight (boyish 고유색), 곡 따라 EDM topline/발라드/청량 팝 · EXCL: thick chest belt, raspy rock vocal, mature diva tone, dark smoky delivery, heavy vibrato
  · 📊 실사용 27곡 — 음역 C4-E5 · 빈출: clear; high-pitched; sweet; bright; boyish straight

**마리/Marie** — `female bright powerful husky J-rock punk vocal, forward-cutting J-rock placement, slightly raspy edge, raw heartfelt emotion, passionate desperate chorus lift, bittersweet rock anthem delivery` · ★J-rock 발성(앞으로 째는 배치), 후렴 후회·답답함 밀어붙임(두꺼운 디바 X) · EXCL: polished idol sweetness, operatic belt, metal growl, soft breathy-only
  · 📊 실사용 48곡 — 음역 A3-F5 · 실측: bright thin piercing J-rock placement forward and cutting, husky raspy edge, raw frustration, belting high notes

**네르/Nerh** — `female powerful straight chest-belt rock vocal, Western-rocker placement, clear commanding projection, gritty-but-controlled texture, medium body kept from going too thick, no vibrato, rock-heroine strength — power not rasp` · 앞공명 직선 파워 벨트(★서양 락커 발성), falsetto 거의 X·두께 과하지 않게 방지 · EXCL: airy falsetto lead, overly thick heavy diva belt, shout-scream, raspy harsh yell, idol nasal chant, thin breathy float
  · 📊 실사용 26곡 — 음역 A3-F5 (low-mid~mid-high) · 실측 반복: powerful belting, straight tone, chest voice, "No Falsetto", "No Rasp - Just Power", commanding rock heroine

**레베카/Rebecca** — `female high-pitched pure delicate indie-pop vocal, gentle kind sweet tone, breathy with short clipped breaths, close-mic intimacy, soft sustained endings` · ★상냥하고 여린 인디팝, 짧은 호흡·긴 여운·가까운 마이크 · EXCL: strong punk attack, fast rap, thick low chest, brassy diva chorus
  · 📊 실사용 20곡 — 음역 C4-E5 · 빈출: warm; gentle; high-pitched; delicate; airy

**령/Ryeong** — `non-singing robot voice samples, glitch fragments, spectral whispers, rhythmic SFX, vocoder punctuation` · 메인 보컬 X, 리듬·효과음·글리치 이벤트용 · EXCL: full lead vocal, warm soul singing, natural acoustic realism
  · 📊 실사용 18곡 — 음역 표기없음 · 빈출: sweet; the female vocal must be clear; the delivery is soft and gentle; high-pitched cute vocals; growling

**체니/Chenny** — `female extreme high-pitched child-like rapid-fire punk rap, fast bright syllable attack, energetic playful chant, clear crisp diction, no breathiness` · 초고음·빠름·어린애 목소리 또랑또랑 (★bratty/떼쓰는 톤 X), 긴 멜로디엔 조절 · EXCL: bratty whiny tone, tantrum shout, smooth adult R&B, slow elegant ballad, low monotone narration
  · 📊 실사용 26곡 — 음역 C4-F5 · 빈출: child-like; clear; rapid-fire; anime-loli; explosive but not whiny

**라이니/Laini** — `female high-pitched smooth seductive jazz R&B vocal, lazy glide, silky phrasing, smoky upper register, controlled vibrato` · 고음이나 힘 X 미끄러지듯 · EXCL: punk shout, child-like chant, robot FX, raw grunge rasp
  · 📊 실사용 22곡 — 음역 C4-E5(1) · 빈출: seductive; smooth; clear; : high-pitched; :clear

**세리카/Serica** — `female clear calm polite high-pitched vocal, composed diction, glassy tone, gentle controlled breath, elegant melodic restraint` · 정돈된 호흡·신비로운 거리감 · EXCL: messy punk energy, desperate scream, nasal comic delivery
  · 📊 실사용 19곡 — 음역 B3-E5(1), C4-F5(1) · 빈출: clear; gentle; : high-pitched; breathy; warm

**샐리/Sally** — `female ultra high-pitched feather-light nasal funk vocal, kept bright and light against funk's natural thickness, sassy coquettish playful bends, rhythmic talk-sing, MJ-style hiccups grunts and ad-libs, percussive crisp diction, subtle vocal-fry phrase ends` · ★funk인데 두꺼워지지 않게 초고음·가볍게, 비음 애교·MJ식 추임새 · EXCL: thick heavy funk vocal, low chest weight, flat polite ballad, ethereal whisper-only, deep monotone male
  · 📊 실사용 29곡 — 음역 A3-D5 (attitude-high, 가볍게 위로) · 실측: nasal sassy coquettish, percussive staccato, MJ-style hiccups & grunts, airy belt release on chorus peaks, vocal fry ends

**테피/Tepi** — `female clear warm gentle soul pop vocal, honest midrange, soft smile tone, rounded vowels, comforting melodic phrasing` · 위로·온기·부드러운 open vowel · EXCL: cold robotic sample, abrasive punk rasp, screamed rock chorus
  · 📊 실사용 18곡 — 음역 C4-E5(1) · 빈출: gentle; warm; vibe:warm; clear sections; gentle dynamic build

**카샤스/Kashas** — `male mid-high scratchy melodic grunge sing-rap, laid-back behind-beat groove, dry attitude, raspy hooks, loose rhythmic phrasing, clean melodic belt option` · 츤데레 무심·껄렁, 선율과 랩 사이 · EXCL: clean boy-band pop, deep operatic rock, polite narration
  · 📊 실사용 10곡 — 음역 tenor C3-G4 + falsetto G4-C5 · 실측: scratchy laid-back spoken-sing leaning rap-cadence behind-beat, clean melodic belt

**올레그/Oleg** — `male deep gruff powerful hard-rock vocal, heavy chest weight, controlled scream peaks, gravel texture, arena-sized aggression` · 샤우팅/포효, Suno 과하면 소음화 → peak 위치 제한 · EXCL: soft indie mumble, delicate falsetto lead, clean idol tone
  · 📊 실사용 13곡 — 음역 A2-G4(1) · 빈출: (oleg):deep; **powerful rock vocal/screamer; ** **aggressive shouts; (walcott):high-pitched; orchestral hits

**월콧/Walcott** — `male high-tone youthful rapper, two faces: (1) desperate near-crying emotional scream-rap with breathless panic urgency; (2) hyped energetic hard-hitting fast rap, punchy confident flow; plus low scratchy cynical spoken punchlines` · ★크라잉만 X — 신나게 갈기는 하드 랩도, clipped 자음 · EXCL: slow crooner, warm acoustic ballad, smooth lounge
  · 📊 실사용 26곡 — 음역 G3–D5 · 빈출: high-pitched; rapid-fire rap; emotional scream; 울기직전 hi-tone; low cynical punchline

**크래더/유진/Crader** — `male laid-back relaxed indie pop vocal, soft lazy diction, light nasal warmth, casual city-pop phrasing, underplayed emotion` · 힘 뺀 나른, 덜 부르는 감정선 · EXCL: screamed rock belt, hyperactive rap, dramatic musical theater
  · 📊 실사용 32곡 — 음역 표기없음 · 빈출: bright; featuring a male vocalist with a clear; slightly raspy tenor voice; the mix is bright and clear; raspy indie tone

**박봉남/Bongnam** — `female high-pitched sassy energetic vocal, Marie-adjacent bright power but more rap-leaning, sharp bright tone, tight rap flow, cheeky adlibs, fast comic phrasing, elastic hook delivery, faint husky-grit on chorus ends` · ★마리 결의 밝은 파워인데 더 랩시(sings less, raps more), 깨방정·쌔끈 · EXCL: solemn ambient vocal, deep male narration, fragile whisper ballad
  · 📊 실사용 58곡 — 음역 A3-F5 (alto~mezzo-soprano) · 실측: clear bright sassy energetic, tight rap flow, witty playful, faint husky-grit chorus ends

**젠슨/Jensen** — `male warm bright young tenor, clear refreshing tone, melodic and expressive, earnest heartfelt delivery, conversational verses lifting to light falsetto on hooks` · ★청량·밝고 진솔 (deadpan/저음 모노톤 X — 그건 초기 베이스였음) · 보조 모드: cool confident rhythmic spoken-word verse → melodic chorus (funk-rock 한정) · EXCL: deep monotone-only, flat deadpan narration as lead, dark gruff low chest, comic child-like rap
  · 📊 실사용 16곡 · 솔로 실측(0014·0039 일관): warm bright young tenor, melodic, light falsetto on hooks, "not low, never deadpan" — mid-tenor + 훅 falsetto

**현암/Hyeonam** — `male deep analytical taryeong-style rap, earthy Korean phrasing, rhythmic chant-singing, grounded low resonance, fusion gugak cadence` · 한국어 장단·어미·받침 살림 · EXCL: generic trap imitation, Western diva belting, thin idol nasal chant
  · 📊 실사용 21곡 — 음역 표기없음 · 빈출: the female vocal must be clear; sweet; the delivery is soft and gentle; shouted group harmonies to create a massive wall of sound; ** comedic clash(sassy latin vs deadpan rap)

**미첼/Mitchell** — `female sophisticated city-pop R&B diva vocal, high-pitched breathy elegant tone, soft silky soulful delivery, chic calm narrative phrasing, alto-to-mezzo-soprano, ethereal reverbed harmonies` · ★여성 (City Pop Diva) — 세련 시크 breathy soulful R&B, 곡 따라 airy soprano / silky mezzo · EXCL: male vocal, raw punk scream, comic rapid chant, heavy belt-only, mumbling
  · 📊 실사용 24곡 — 음역 A3-F#5 · 실측: City Pop Diva sophisticated chic, high-pitched breathy elegant soulful R&B, breath-heavy whisper, calm narrative (전곡 female)

**타투/Tatoo (멀티모드 — 여성, Sis Tatoo=같은 인물의 모드)** — 곡마다 모드 택1, 멜로디는 안 떨어뜨리고 보컬 색만. ★기본 권장 = Mode C(맑고 상냥 — 가사 따라 자연히 굳은 결, 잘 어울림). 매력적 저음 원래 의도는 Mode A로 보존:
  · 📊 실사용 19곡 — 음역 표기없음 · 빈출: sassy; low-energy; almost monotone spoken-like; minimal vibrato (구버전 모드) + 근래 맑고 상냥한 결로 이동
- Mode A 느와르(원래 의도 "매력적 저음"): `female low-mid dry monotone rhythmic sing-rap, noir close-mic delivery, cool deadpan phrasing, dark jazz/trip-hop pocket, restrained intimate tone, tiny phrase-end grain`
- Mode B 샤프하이: `female bright sharp dry soprano-to-high-mezzo vocal, cool chic deadpan delivery, biting clear Korean diction, dry close-mic tone, low-effort phrasing, melody remains fully sung and lifted`
- Mode C 맑고상냥(★기본): `female clear warm sweet Korean tone, gentle tender emotional delivery, lightly breathy intimate close-mic, delicate but centered, soft natural phrasing, melody fully sung`
- ★주의: 낮은 느와르 싱잉랩(A)도 *여성* 모드 — male 아님. EXCL(필요/드리프트 시): male vocal, chesty/thick low alto, heroic belt, over-sweet idol aegyo, whisper-only, melody flattening, pitch collapse, robotic autotune

**우나/Una** — `female delicate ethereal whisper vocal, fragile airy tone, dream-pop float, close breath texture, soft blurred consonants` · 공기처럼 떠야 함(강하게 치고 X) · EXCL: power belt, fast punk rap, deep gruff rock vocal
  · 📊 실사용 15곡 — 음역 C4-E5(1) · 빈출: vocal: female whispering vocals; ethereal; falsetto high notes; ethereal shoegaze; breath texture 8khz hard-l 30% whisper

**마르티나/Martina** — `female mid-low sexy smooth jazz Latin vocal, mature velvet tone, relaxed rhythmic sway, warm chest color, elegant phrasing` · 중저음 벨벳·리듬 스웨이 · EXCL: child-like high chant, robot glitch voice, punk scream
  · 📊 실사용 20곡 — 음역 표기없음 · 빈출: deep; mid-low tone; husky & breathy whisper intro; powerful diva belting in chorus; vibrato

**타라한/Tarahan** — `female light airy young teen-girl soprano, very soft thin breathy head voice, pulled far back and effortless, low-energy unforced delivery, heartwarming gentle fresh K-indie charm, slight nasal sweetness` · 아티스트명 금지 → 결만 분해 · ★힘 뺀 effortless 솜털 미성(과한 projection X) · EXCL: mature Latin jazz, deep male narration, heavy belt, powerful loud projection
  · 📊 실사용 11곡 — 음역 D4-A5 (high light soprano) · 실측: light airy teen-girl soprano, thin breathy head voice, pulled far back low-energy effortless, "kawaii" girl-next-door, dreamy

**웰링/Welling** — `male standard pop-rock vocal, adaptable midrange, clean melodic delivery, light grit on chorus, reliable lead tone` · 다장르 받쳐주는 기본형 · EXCL: extreme-scream-only, robot-narration-only, fragile-whisper-only
  · 📊 실사용 10곡 — 음역 표기없음 · 빈출: delicate female vocalist; powerful melodic singing; part 1 (verse 1 only): ethereal gospel hymn; swelling string orchestra and a delicate; pure female soprano vocal



### §2.6. ★신규 캐릭터 (카탈로그 발굴 — 운영자 확정 완료 2026-06-15)
캐탈로그에서 발견된 신규 캐릭터. 아래 4명은 운영자 확정 — 실사용 tags 근거 기반 [VOICE] seed. (김갑수·하더는 캐릭터 미발전으로 팔레트 제외 — 곡은 catalog에 잔류.)

**Amy/에이미** ✅ — `bright airy summer dance-pop, princess fairytale crystalline, high airy soprano, sweet, not warm` · 📊 7곡 · 음역 A3-E5
  · 빈출 근거: bright airy summer dance-pop; princess fairytale crystalline; high airy soprano; sweet; not warm; glassy fairytale hook
  · 작품군: "Run Sarura Run!" (Bellona·Raiza와 트리오)

**Bellona/벨로나** ✅ — `female alto orchestral-hybrid-rock vocal, smoke-and-silk grounded verses opening into a firm gritty controlled belt on chorus, teenage-commanding strength, nasal-centered groovy tone — powerful not screaming` · 📊 6곡 · 음역 alto (대략 A3-E5, 추후 실측)
  · 실측 근거: Female alto lead, breathy yet grounded smoke-and-silk tone, chorus steady firm belt controlled power not screaming, "Teenage but Commanding, Gritty, Powerful Belting", gang vocals chorus
  · 작품군: "Run Sarura Run!" (Amy·Raiza와 트리오)

**Silva/실바** ✅ — `dark orchestral, whispering ASMR, intimate close-mic breathy` · 📊 5곡 · 음역 표기없음(추후 보강)
  · 빈출 근거: dark orchestral; whispering ASMR; ASMR whisper
  · 비고: ASMR/속삭임 결이 핵심 — 음역·멀티모드는 곡 추가 시 보강

**Raiza/라이자** ✅ — `female warm delicate Japanese indie-pop vocal, low-leaning alto/mezzo register, conversational understated tone, gentle breathy intimacy, natural unpolished folk-pop delivery, proximity not power` · 📊 3곡 · 음역 G3–C5 (alto/mezzo — ★낮게 고정)
  · 운영자 의도: 여린 일본소녀 인디팝, 아이묭(あいみょん) 결 — 담담·따뜻·살짝 허스키 (이름 금칙 → 결만 분해)
  · ★고음 드리프트 차단: 구버전이 'Single female soprano D4–E5'로 잡혀 자꾸 높게 나옴 → soprano 폐기, alto/mezzo 저음 고정. EXCL: high bright soprano, soprano range, piercing high notes, idol-high topline, bright belt, head-voice float, cute aegyo
  · 작품군: "Run Sarura Run!" (Amy·Bellona와 트리오)

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
타라한    EFFORTLESS airy + pulled-back     솜털 thin breathy·low-energy     힘 뺀 솜털 teen-girl(우나보다 덜 흐림·더 sweet)
네르      POWER chest belt + straight       파워 belt·no falsetto·no rasp    앞공명 직선 파워(클러스터 유일 belt·가성X)
```
→ 가르기: 깨끗직선=루크 / 유리알거리=세리카 / 떨림숨=레베카 / 속삭임뜸=우나 / 솜털effortless=타라한 / 파워belt=네르.

### 클러스터 B — sassy/비음 여성 (3명)
```
샐리      NASAL aegyo + MJ hiccups/grunts   비음 bend·넉살·percussive·fry    펑크 그루브 talk-sing+MJ추임새(랩 X)
봉남      SHARP pop-RAP + elastic hook      쌔끈 adlib·comic·짧은 훅        팝랩 탄력 훅(샐리보다 랩·날카로움)
체니      EXTREME child + RAPID punk rap     떼쓰는 shout-chant·chaos        초고속 애 같은 punk(가장 과장·빠름)
```
→ 가르기: 펑크그루브=샐리 / 팝랩탄력=봉남 / 초고속애punk=체니.

### 클러스터 C — 스무스/세련 여성 (3명)
```
라이니    HIGH smoky + lazy GLIDE           나른 glide·controlled vibrato   고음 미끄러짐(상부 스모키)
마르티나  MID-LOW velvet + Latin SWAY        중저음 chest·리듬 sway          중저음 벨벳(라이니보다 낮고 라틴)
미첼      ELEGANT breathy + City-Pop diva   silky soulful·breath-heavy      세련 diva R&B(라이니보다 elegant·breathy diva)
```

### 클러스터 D — 나른/세련 남성 (2명)
```
크래더    LAZY indie + underplayed          힘 뺀 나른·덜 부르는 감정        인디 도시 언더플레이(가장 힘 뺌)
웰링      STANDARD adaptable + light grit   안정 lead·후렴 light grit        다용도 기본형(개성보다 신뢰성)
```

### 클러스터 E — 랩/공격 남성 (4명)
```
카샤스    SCRATCHY grunge sing-rap + 무심    껄렁 dry·raspy hook·츤데레       선율↔랩 사이 스크래치(멜로딕)
월콧      HIGH desperate + RAPID panic      과호흡·clipped·절박             고음 속사포 패닉(가장 빠르고 절박)
올레그    DEEP gruff + scream peak          포효·gravel·arena               굵은 하드록 샤우팅(peak 제한)
현암      TARYEONG gugak + 받침 살림         한국어 장단·어미·grounded       타령조 국악 랩(유일 한국 전통)
```

### 클러스터 F — 비보컬/스포큰 (1명, FX 전용)
```
령        ROBOT glitch 샘플 (FX)            기계·vocoder·spectral          메인 보컬 X — 효과음/글리치
```

**독립(충돌 적음):** 마리(허스키 J-rock 펑크 anthem) / 테피(따뜻 소울팝 위로) / 타투(여성 멀티모드 A느와르/B샤프하이/C여린dry) / 젠슨(청량 밝은 young tenor + 훅 falsetto, earnest — 보조 spoken-verse 모드).

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
