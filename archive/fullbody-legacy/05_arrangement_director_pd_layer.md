# ACTIVE GPT ROUTE HEADER
- Current GPT file: `05_arrangement_director_pd_layer.md`
- Purpose: Arrangement Director / PD orchestration
- Preserved source aliases: 28_ARRANGEMENT_DIRECTOR
- Use rule: Use before final fields for CREATE×COVER pairing, preserve/substitution maps, lead axis, density, instrument weight, frequency footprint. Together: 02,06,07,18.
- Cross-link rule: Follow `instructions.txt` first. Legacy `# SOURCE:` blocks below are source provenance, not current routing names. If retrieval is thin, search this file by both current terms and preserved source aliases.

---

# Active GPT patch: Arrangement Director / PD layer
Before final fields, internally run the PD layer: choose CREATE×COVER pairing, lead axis, preserve map, substitution map, density, instrument weight, frequency footprint, and quality plan. If user says audio is harsh/muddy/buried, route to production-aware quality stack, not a new random song.

---

# SOURCE: 28_ARRANGEMENT_DIRECTOR.md

# ============================================================
# 28_ARRANGEMENT_DIRECTOR.md  —  PD / 편곡감독 레이어
# YUNY v2.8 (2026-06-05)  ·  버전이력 = CHANGELOG.txt 단독
# ============================================================
# 한 줄 정의: §1(CREATE/COVER)·§2(밀도)·§3(스타일박스)·§10(평균회귀)·
#   §11(레퍼런스)·§18(연쇄) *위에 얹히는* 오케스트레이터. 컴포넌트 전문성
#   (단일 장르·보컬·Suno 메커니즘·글자수)은 이미 충분 — 이 파일은 그걸 *전곡
#   아키텍처로 조율*하고 CREATE↔COVER에 *배분*하고 *음질을 끌어올리는* 의사결정 층.
#
# LOADED BY  : 00 SYSTEM §1.5 훅 / D 라우팅("조합·페어링·아쉽다·음질·트렌드·
#              실험곡·악기무게·거장결·분위기" 발화) / G AUTO-EXEC(새 곡 아키텍처)
# ROUTES TO  : 장르조합→23a INDEX→web_fetch(품질목적, 매번X) / 악기주법→16 /
#              음질·주파수·마스터링→20·11 / 평균회귀·트렌드→§10·web_search /
#              레퍼런스·프로듀서 DNA→§11·22 / 보컬→06·§6 / 화성·미분음→02·03·04
# 효율 원칙  : PD 추론은 전부 *내부(thinking)*. 표면은 출력-우선 유지
#              (7-블록 + 핵심 0-2줄 / 불쑥 코멘트는 짧게). 파일 반사적 로드 금지.
# 본 파일 위상: 참고용 *지식 라이브러리*(16·22처럼 깊게 — §5.1은 전세계 9개 권역
#              거장·전통 시그니처) + 의사결정 *프로토콜*. 라이브러리(§1.2·§4.1·
#              §5.1·§6)는 *성장한다* — 99z 로깅 시 추가. 거장 이름은 프롬프트 금지,
#              항상 5-Layer 분해 키워드로(§11).
# ============================================================


## §0. IDENTITY & ACTIVATION — 언제 PD가 켜지나

PD = 비전문가일 수 있는 운영자를 *끌어주는 편곡감독*. 단일 장르·보컬·글자수는
시스템이 이미 잘함. PD가 메우는 건 **"전체를 어떻게 조합하고, CREATE↔COVER에
어떻게 나누고, 음질을 어떻게 올릴지"** 라는 *수평/아키텍처* 결정.

**ON (자동 발동):** 새 곡 아키텍처(7-블록 前) / "아쉽다·부족·밋밋·한쪽으로만·
올드" 피드백 / 조합·페어링 질문 / 실험곡(미분음·자연음·odd meter) / 음질 신고
(얇음·뭉개짐·분리 안 됨) / 다양성 정체(같은 family·BPM zone 3곡+) / "누구 스타일·
요즘 결·어느 나라 결" 발화.

**OFF (개입 최소):** "그냥 해/알아서/찾아와/빠르게" → 제깍 실행, 불쑥도 자제 /
운영자가 페어링·리드축 이미 명시 → 실행만 / 단순 미세수정(단어·음절) → §18 Micro.

**행동 규약:** PD는 *말로 설명하지 않고 더 나은 페어링·배분·음질로 보여준다*
(제0원칙). 후보는 2-3안 + *각각 뭘 얻고 뭘 잃는지* 1줄 — 강의 금지.


## §1. CREATE×COVER PAIRING ENGINE (★ 이 파일의 심장)

**전제:** 페어링(CREATE 베이스 × COVER 스킨)이 곡 퀄리티의 *최고 레버리지 결정*.
충돌 회피만이 아니라 **더 잘 어울리는 결을 먼저 안내**하는 게 PD 일. 보사노바
CREATE + 하드락 COVER가 "시간 걸렸"던 건 이 페어링을 맨 앞에서 제안하는 엔진이
없었기 때문 — 이제 있다.

### §1.1 페어링 호환성 4축 (후보 거를 때 먼저)
1. **Tempo:** COVER는 소스 프레이징 따라감(09 §2.4) → BPM 크게 다른 장르 덮으면
   그루브 어긋남. 안 맞으면 CREATE BPM을 스킨 쪽으로 미세조정(§18 연쇄).
2. **Rhythmic-grid:** straight↔swung↔syncopated. 베이스 swung+스킨 quantized면
   충돌 → 통일하거나 스킨에 "loose/human grid".
3. **Harmonic-density:** 베이스 화성 복잡(7th/9th/텐션)할수록 스킨은 *덜 두껍게*.
   두꺼운 스킨엔 단순 화성 베이스.
4. **Vocal-survivability:** 스킨이 broadband·loud일수록 보컬 묻힘 → "vocal X%
   [정체성] throughout, arrangement only" + corridor 보호(§3).

### §1.2 페어링 전략 라이브러리 (전이 가능 패턴 — 성공 페어링을 *전략으로* 꺼냄)

표기: 베이스=CREATE bone / 스킨=COVER. AI=COVER Audio Influence 권장(lead 60-75 /
texture 20-40, UI 기본 25 기준). 모드 = a(텍스처 refine, 같은 family) / b(편곡·장르
변환). ★보컬 정체성은 모든 페어링 공통 사수.

| # | 전략 | 베이스(CREATE) | 스킨(COVER) | 얻는 것 | AI / 모드 | 실패 → 가드 |
|---|------|---------------|------------|--------|----------|------------|
| P1 | **Organic-base × Loud-skin** (보사×하드락 일반화) | bossa/soul/citypop/folk — 따뜻·멜로딕 | hard rock/그런지/메탈/덴스 일렉 | 멜로디·화성 온기 유지 + 음질·밀도·임팩트 | 60-70 / b | 보컬 묻힘 → corridor 보호 + "drive on instruments only" |
| P2 | **Acoustic-base × Electronic-skin** | 핸드플레이드 어쿠스틱 | synthpop/electronic/hyperpop | 친밀 + 모던 펀치·정밀 | 55-65 / b | 기계화 인간미 증발 → "human timing, breath retained" |
| P3 | **Sparse-base × Dense-skin** (역도) | 미니멀·여백 편곡 | 풀밴드/오케스트라 | 여백↔채움 대비 드라마 | 50-60 / b | 여백 다 메움 → "leave verses sparse, build chorus" |
| P4 | **Vintage-base × Modern-master-skin** | 레트로 코드·멜로디(60s-90s) | 동시대 라우드니스·클래리티·새추 | 노스탤직하지만 안 올드 | 45-60 / a | 레트로 죽음 → era anchor를 CREATE에, 스킨은 해상도만 |
| P5 | **Genre-pure × Cross-genre (b)** | 깔끔한 단일 장르 정체성 | 대담한 타장르 재편곡(09 §3.5c) | 멜로디 명료 + 과감 변신 | 60-75 / b | 평균수렴 → Substitution 풀가동 + 원곡장르 EXCLUDE |
| P6 | **Refine-only (a, 같은 장르)** | 이미 장르 맞는 곡 | 동장르 음질 폴리시만 | 순수 음질↑, 결 안 흔듦 | 25-40 / a | 텍스처 과욕 → 장르 키워드 반복 금지, 믹스어만 |
| P7 | **Hard-base × Organic-skin** (역 P1) | trap/DnB/phonk 비트 척추 | 유기 텍스처·생악기 | 펀치 유지 + 온기·인간미 | 50-60 / b | 비트 흐려짐 → kick/베이스 "preserved, untouched" |
| P8 | **Cinematic-base × Pop-skin** | 시네마틱 화성·스트링·아크 | 라디오 팝/댄스 후렴·훅 | 서사 깊이 + 캐치 임팩트 | 50-65 / b | 후렴이 시네마틱 죽임 → bridge·outro만 회귀 |
| P9 | **Folk-base × Cinematic-orchestral** | 포크 핑거픽·소박 보컬 | 오케스트라 스웰·합창 | "친밀한 서사시" | 50-60 / b | 포크 진정성 묻힘 → verse 포크 유지, 스웰은 chorus |
| P10 | **Jazz-base × Lo-fi-skin** | jazz 7th/9th·brushed 드럼 | 로파이 테이프·vinyl·filtered | 늦은밤·study, 세련된 머드 | 30-45 / a | 화성 진흙 → corridor·zone strict + "open dynamics" |
| P11 | **Trap-base × Dark-orchestral** (Metro 결) | 808 글라이드·sparse 하이햇 | 다크 시네마 스트링·choir | 위협적 웅장 + 펀치 | 55-65 / b | 808 묻힘 → sub mono·sidechain 유지, 오케스트라 mid-high |
| P12 | **City-pop-base × Modern-funk** (2026 부활) | 80s 시티팝 코드·멜로디 | 모던 펑크 그루브·슬랩·클린 | 레트로 글로우 + 현행 그루브 | 50-60 / b | 올드 펑크化 → 코드 CREATE, 펑크는 리듬·믹스만 |
| P13 | **Ballad-base × Arena-rock** | 인티밋 발라드·피아노 | 빅 록 다이내믹·기타·드럼(후렴) | 절제→폭발 다이내믹 레인지 | 50-65 / b | 빌드 없음 → verse 스트립, chorus만 arena |
| P14 | **Bedroom-pop-base × Hyperpop** | 로파이·인티밋·홈레코딩 | 글리치·피치드·맥시멀 | 날것 친밀 + 폭발 모던 | 55-70 / b | 인티밋 증발 → verse bedroom, 후렴만 hyper |
| P15 | **Latin-base × House-skin** | bossa/salsa/cumbia 따뜻 | four-on-floor 클럽 하우스 | 라틴 온기 + 클럽 추진력 | 55-65 / b | 라틴 결 평면화 → 퍼커션·코드 CREATE, 4-on-floor만 |
| P16 | **Neoclassical-base × Electronic** | 피아노·스트링 네오클래식 | 일렉 프로세싱·비트·텍스처 | neoclassical electronica 영화감 | 45-60 / b | 피아노 정서 깨짐 → dry 보존, 일렉은 주변 |
| P17 | **Dub-space × Modern-pop/electronic** | 모던 팝·일렉 곡 | 더브 드롭아웃·테이프에코·스프링리버브 공간 | 최면적 공간감·긴장·여백(dub 미학) | 35-50 / b | 곡 흐름 끊김 → 드롭아웃은 bridge/break에, 보컬 corridor 사수 |
| P18 | **Amapiano-base × R&B/Soul-skin** | log drum 그루브·deep-house 코드 | 소울풀 R&B 보컬·neo-soul 화성 | 최면 그루브 + 보컬 따뜻함 | 50-60 / b | 그루브 묻힘 → log drum "preserved", R&B는 보컬·코드만 |
| P19 | **Cinema-fusion-base × Trap-skin** (Rahman 결) | lush 스트링+동양 악기·드론 | 808 트랩·하이햇 롤 | 동서 퓨전 웅장 + 모던 펀치 | 55-65 / b | 퓨전 산만 → 스트링·드론 CREATE 깊게, 트랩은 리듬만 |
| P20 | **Bossa-base × Downtempo-electronic** | 무트 나일론 기타·jazz 화성 | 다운템포 비트·필터드 텍스처 | nu-bossa/라운지, 세련된 칠 | 35-50 / a | 보사 숨 죽음 → 기타·보컬 dry 가까이, 비트는 뒤로 |

> ★역방향·변주 자유: 위는 *전형 케이스*. "어느 결을 베이스/스킨으로"는 호환 4축
> (§1.1)으로 판정. 새 성공 페어링은 99z 로깅 때 이 형식으로 추가, 실패(예: 99 Part
> G Case 41 하드스타일+한국보컬)은 *반례*로 같은 자리에 기록. 권역별 결은 §5.1과 교차.

### §1.3 페어링 결정 출력 (PD 1단계 — 내부에서 굳히고 표면은 짧게)
①의도 → ②호환 4축 → ③라이브러리 후보 2-3 → ④추천 1 + 트레이드오프. 표면엔 *진짜
분기일 때만* 2-3안, 아니면 바로 7-블록. CREATE 베이스 레퍼런스 DNA(누구/어느 권역
결)도 여기서 결정(§5.1 → §11 5-Layer 분해, 이름 직접 금지).

### §1.4 조합 재점검 (초안 *나온 뒤*, 출력 前 — 조합 단위)
□ 보컬 생존(corridor·throughout) □ 주파수 충돌(같은 zone 3+, §3/20 §1) □ 그루브
호환(§1.1-②) □ 30% Rule(09 §3.5b) □ 평균수렴 위험(§10) □ 음질 채널 *실제로* 찼나
(§3 — 최빈 결손) → 걸리면 출력 前 수선, 표면 보고 X.


## §2. PROMPT LEAD-AXIS SELECTOR (★ "일정한 유형이 아니다")

곡마다 프롬프트가 *무엇을 앞세워야 하는지*가 다르다. 전곡 장르-우선 = 평균치.
PD는 *이 곡의 리드축*을 먼저 고른다 (Position 1·배분·끌어올 파일이 축마다 다름).

| 리드축 | 언제 (차별점이 ~) | Position 1 앞자리 | CREATE↔COVER | 자료 |
|--------|------------------|-----------------|-------------|-----|
| **Genre-led** | 장르 정체성이 후크 | 마이크로장르+시대+시그니처 | 장르=CREATE / 음질=COVER | 05·23a·§3 |
| **Vocal-led** | 발라드·R&B·인디·듀엣 | 보컬 5-element first(§3) | 보컬=CREATE / 처리=COVER | 06·§6·24 |
| **Frequency/Hz-led** | 편곡 빽빽 → 분리·음질 생사 | corridor·zone 배치 언어 | 화성·악기=CREATE / 주파수=COVER | 20 §1·11·§3 |
| **Deliberate-blur ("뭉개기")** | lo-fi·슈게이즈·드림팝(머드=미학) | "washed/blurred/tape-melted" 긍정 | 무드=CREATE / 의도 머드=COVER | 16·20·§3.3 |
| **Harmonic/Microtonal-led** | 구성·진행·코드·미분음이 영혼 | 화성 컬러+컨투어+microtonal | 화성·미분음=CREATE 깊게 | 02·03·04 §UE-8 |
| **Ambient/Zen-led** | 자연음·필드레코딩·명상이 캐리 | atmosphere+자연음 first | 분위기=CREATE+COVER / 비트 최소 | 11·17·§7 |

**규칙:** 축은 섞일 수 있다(Vocal+Frequency 보호 등). 단 Position 1은 한 축. 미지정
시 PD 추정+1줄 확인. "뭉개기"는 *버그 아닌 선택* — lo-fi/shoegaze에선 머드 키워드를
EXCLUDE에서 빼고 Style 긍정으로, 보컬 corridor만 보호.


## §3. SONIC-QUALITY ELEVATION (★ 음질 — 지금 가장 자주 빠지는 자리)

음질 작업은 대부분 *COVER+주파수+마스터링*에 사는데, 멜로디·가사·장르에 집중하다
COVER 텍스처 채널이 저활용/누락됨. PD는 음질을 *1급 점검*으로 들고, 본체 지식은
20·11에 있으니 *언제 끌어올지*를 소유(품질 목적 — 반사적 로드 아님).

### §3.1 음질 상승 무브 (COVER 중심, 일부 bone-level)
- **zone 소유권:** 같은 zone 3+ 악기 → EQ separation(20 §1 7-zone).
- **Vocal corridor:** 500Hz-3kHz 비우기 + de-esser 5-8kHz(99 Part F).
- **Sub-bass mono + sidechain:** 20-80Hz mono, kick 사이드체인(20 §4.2).
- **Glue·새추:** bus comp + tape/tube saturation = "physicality"(2026 트렌드).
- **Transient:** 펀치 zone 강조 / 따뜻함은 attack 둥글림.
- **Stereo·Depth:** pan degrees + detune(+8cent L15R15) / dry 가까이·reverb 멀리.
- **LUFS:** 장르별(20 §2) / 마스터 -14 LUFS·-1 dBTP.
- **bone-level:** 편곡 밀도는 CREATE에서 — 빽빽하면 믹스로도 안 뚫림 → §4로 먼저 솎기.

### §3.2 음질 CREATE↔COVER 분배
CREATE = 편곡 밀도·보컬 정체성·화성 복잡도(*뚫릴 여지*) / COVER = frequency·glue·
새추·stereo·LUFS·corridor(*실제 광택*). 모드 a면 COVER 몰빵 / b면 새 장르 음질 컨벤션.

### §3.3 ★음질 죽이는 키워드 가드 (99 Part G)
"muddy/over-compressed/vocoder 과다"는 EXCLUDE에서도 보컬 처리 회피 유발 → 머드는
**Hz 분배 strict + "open dynamics, frequency separation" 긍정**으로. EXCLUDE엔
"harsh digital sheen, over-compressed, clipped transients"처럼 능동 컨트롤로(§4). 보컬공간 죽이는 건 뺀다.

### §3.4 음질 누락 차단 게이트 (출력 前 내부)
□ COVER 텍스처 700-950자 채웠나(Under 700=저활용) □ corridor·zone·glue·LUFS 중 3개+
□ Audio Influence 값 박혔나(§12) → 비었으면 §3.1 보강. ("음질 빠짐" 90%가 여기.)


## §4. INSTRUMENT WEIGHT & DENSITY (★ "무슨 악기가 가볍고" + 편곡 리폼)

16은 *주법*. 본 §4는 *무게·밀도·주파수 발자국·역할*. PD가 "이 악기 무거워 보컬 묻혀
— 가벼운 걸로" 식 리폼하는 근거. 상세 articulation은 16으로.

### §4.1 악기 무게·밀도 (무게 / 밀도=먹는공간 / zone / 결 / CREATE·COVER)
**Keys:** 펠트피아노(가벼·좁·mid·친밀·CREATE) / 그랜드(중·중넓·broadband·정통·CREATE) /
Rhodes·Wurli(가벼중·중·warm mid·소울·CREATE) / Hammond B3(중·넓·mid sustain·가스펠·COVER) /
Mellotron(중·넓·mid 몽환·빈티지·CREATE/COVER)
**Guitars:** 나일론·어쿠스틱(가벼중·중·mid 투명·유기·CREATE) / 클린일렉jangle(중·중·mid
presence·모던·CREATE) / 디스토션리듬(무거·넓·broadband 톱니·벽·COVER) / 페달스틸(가벼중·
중·high-mid 우는·향수·CREATE) / 밴조·만돌린(가벼·좁·high·활기·CREATE)
**Bass:** 업라이트(중·좁·low-mid 따뜻·재즈·CREATE) / 슬랩펑크(중·중·mid 펀치·그루브·
CREATE) / Moog신스(중무거·넓·low 두꺼움·모던·CREATE) / 808·Sub(무거·low 독점·20-80Hz·
펀치·CREATE) / Reese(무거·넓·low-mid 거친·DnB·CREATE)
**Drums/Perc:** 재즈brush(가벼·좁·mid soft·스윙·CREATE) / 어쿠스틱록(중무거·넓·broadband·
인간·CREATE/COVER) / 빅룸(무거·넓·broadband 펀치·아레나·COVER) / 트랩키트808+hat(무거중·
펀치집중·low+high·모던·CREATE) / quantized머신(중·펀치집중·transient·기계·CREATE) /
셰이커·탬버린(가벼·좁·high air·필러·COVER) / 타블라·핸드퍼크(가벼중·좁·mid·월드·CREATE)
**Synth:** 패드(중무거·*매우넓*·broadband·접착·COVER, 과하면 머드) / pluck·arp(가벼·좁·
high·모션·CREATE/COVER) / saw lead(중·중넓·mid-high 강·드라이브·CREATE)
**Orchestral/Texture:** 스트링레가토(중·넓·broadband sustain·시네마·CREATE아크+COVER스웰) /
스트링pizz(가벼·좁·mid·장난·CREATE) / brass section(무거·넓·upper-mid 강·임팩트·COVER) /
sax solo(중·중·mid 표현·관능·CREATE/COVER) / flute·clarinet(가벼·좁·high-mid 맑·목가·
CREATE) / harp·celesta·glock(가벼·좁·high sparkle·장식·COVER) / choir·vocal pad(중·넓·
broadband·웅장·COVER) / vibraphone·marimba(가벼·좁·mid 부드·드림·CREATE) / field·자연음
(가벼·가변·가변·분위기 캐리어·CREATE+COVER §7)

### §4.2 편곡 리폼 레시피 (증상 → 리폼)
- **무겁다/답답:** 디스토션 리듬기타 → muted single-coil + 무게 베이스로 / pad 한 겹 제거 / kick-808 사이드체인 / broadband high-pass.
- **얇다/허전:** felt piano pad / topline 옥타브 아래 더블 / upright bass / room 두께 / 셰이커로 high.
- **뭉개진다(원치않게):** broadband 겹침 솎기 + zone 분배(§3.1) — Hz로 풀지 키워드 남발 X.
- **얇고 차갑다:** tape/tube 새추 + Rhodes/펠트 1겹 + 약한 plate.
- **보컬 묻힘:** corridor 비우기 + 충돌 대역 -1~2dB / sidechain 보컬.
- **그루브 밋밋:** swung hat·ghost note·신코페이션 베이스 + perc 1.
- **다이내믹 평면:** verse 솎고 chorus만 채움(레인지).
- **모던함 부족:** transient 드럼 + saturated bass + pluck/arp 모션.

### §4.3 ★불쑥 코멘트 트리거 (§8 연동)
무게/밀도/zone 위반 시 짧게: "이 pad broadband라 보컬 부딪혀 — 한 겹 빼거나 high-pass 치자" (1-2줄).


## §5. PRODUCER SIGNATURE & TREND ENGINE (★ 전세계 쌉고수 — 9개 권역)

### §5.1 거장·전통 시그니처 라이브러리 (전세계 — 프롬프트엔 5-Layer 분해 키워드만)
★★ 이 표는 *내부 참고 지식*(22 K-pop 딥다이브처럼). **Suno 프롬프트엔 이름 직접 금지.**
"[프로듀서/전통] 결"을 *5-Layer 분해 키워드*(드럼·베이스·화성·보컬처리·공간 디스크립터)로
박는다. "in the style of X"가 아니라 *Artist DNA*(§11). 권역별로 호환 페어링(§1.2)·리드축(§2) 병기.

**[A] 북미/영미 (Anglo-American)**
| 결 | 시그니처 트레이트 | 5-Layer 분해 키워드(prompt) | 페어링·리드축 |
|----|-----------------|---------------------------|--------------|
| 인티밋 미니멀 (Finneas) | 속삭이는 close-mic, sub, 여백, found-sound, 드럼 최소 | whispered close-mic vocal, deep sub bass, negative space, finger-snap & found percussion, no drum kit | P14·Vocal/Ambient |
| 새추 빈티지 팝 (Antonoff) | gated/roomy 스네어, saturated 신스베이스, 더블드 보컬, 80s | gated roomy snare, saturated analog synth bass, doubled warm vocal, 80s tape warmth | P2·P4·P12 |
| 다크 시네마 트랩 (Metro) | 다크 오케스트라/choir 샘플, 808 글라이드, sparse 하이햇 | dark cinematic orchestral & choir sample, gliding 808, sparse hi-hats, ominous wide space | P11·Genre |
| 미니멀 펑크 (Neptunes) | 신코페이션 드럼, 여백, quirky 신스 stab, 카운트인 | syncopated minimal drum programming, spacious, quirky synth stabs, dry punch | P7·P15 |
| 오프킬터 (Timbaland) | 보컬/비트박스 퍼크, off-kilter 신코페이션, 월드 샘플 | vocal-beatbox percussion, off-kilter syncopation, world-music sample, stutter edits | Genre/실험 |
| 멜로딕 매스 팝 (Max Martin) | 타이트 구조, 스택드 보컬, 빅 폴리시 후렴 | tight pop structure, layered stacked vocal harmonies, big polished radio chorus | P13·Genre |
| 스트립 로우 (Rubin) | 벗긴·날것, 미니멀, dry, 숨 쉬게 | stripped raw arrangement, minimal, dry close sound, let-it-breathe dynamics | P9·Vocal |
| 웡키 그루브 (Kaytranada) | swung/wonky, 필터드 디스코펑크 chop, 바운시 베이스 | swung wonky groove, filtered disco-funk chops, bouncy bass, lo-fi-yet-clubby | P10·P15 |
| 앤서믹 가스펠 (Jeff Bhasker) | 빅 드럼, 가스펠 코드, 앤서믹 빌드, choir | big anthemic drums, gospel chord changes, choir swell, soaring build | P13·P8 |
| 사이키 새추 (Mike Dean) | 아날로그 패드, 헤비 새추, 광활 와이드 | analog synth pads, heavy tape saturation, wide psychedelic space, lush reverb | P16·Blur |
| 재즈·소울 샘플 (Sounwave/TDE) | 재즈/소울 라이브샘플, 변박 구조, 따뜻 | jazz-soul live sample, shifting song structure, warm vintage texture | P10·Harmonic |

**[B] 라틴/카리브 (Latin/Caribbean)**
| 결 | 시그니처 트레이트 | 5-Layer 분해 키워드 | 페어링·리드축 |
|----|-----------------|--------------------|--------------|
| 모던 레게톤 (Tainy) | 뎀보우 그루브, 자연스러운 Auto-Tune 굴절, 퓨처 신스 FX, gentle↔harsh | dembow groove (boom-ch-boom-chick), natural auto-tune inflection, futuristic synth fx, soft-to-harsh dynamic, steelpan accents | P15·Genre |
| 해체 perreo (Arca) | 해체·글리치 레게톤, ominous beat switch, 불협 텍스처, 인더스트리얼 | deconstructed glitched reggaeton, ominous beat switches, dissonant industrial textures | P5·실험 |
| 일렉 세션 트랩 (Bizarrap) | 미니멀 하드 일렉 트랩, 시그니처 신스베이스, build-drop, 비트스위치 | minimal hard electronic trap, signature synth bass, build-drop arrangement, beat switch | P11·Genre |
| 뎀보우/perreo 전통 | dembow riddim, 신코페이션 퍼크, 콜-리스폰스, 90-100 BPM | dembow riddim, syncopated percussion, call-and-response chant, 90-100 bpm perreo | P15 |

**[C] 아프리카 (Africa)**
| 결 | 시그니처 트레이트 | 5-Layer 분해 키워드 | 페어링·리드축 |
|----|-----------------|--------------------|--------------|
| 아마피아노 (Kabza/Maphorisa) | log drum 저음-멜로디, deep-house 코드, rim·shaker, 소울 보컬, ~112 BPM, 여백 | deep log-drum bassline, deep-house jazzy chords, rim-click & shaker, soulful vocal, spacious 112 bpm | P18·Genre |
| 아프로비츠 (Sarz) | Yoruba Fuji 퍼크, Highlife 기타 릴트, 실키 멜로딕 보컬, mid-tempo 바운스 | yoruba fuji-laced percussion, highlife guitar lilt, silky melodic vocal, mid-tempo afro bounce | P7·Vocal |
| 아프로스윙 (Jae5/UK) | Afrobeats+UK rap, swung 하이햇, 멜로딕 | afroswing groove, swung hi-hats, melodic rap topline, warm mid bass | P7·Genre |
| 하이라이프 전통 | 인터로킹 기타, horn section, palm-wine 그루브 | interlocking highlife guitars, horn section, palm-wine groove, lilting offbeat | P9 |

**[D] 일본 (Japan)**
| 결 | 시그니처 트레이트 | 5-Layer 분해 키워드 | 페어링·리드축 |
|----|-----------------|--------------------|--------------|
| 시티팝 (Yamashita) | AOR/soft-rock+funk+disco, Rhodes·타이트 세션 베이스, brass·lush 스트링, Brian Wilson 하모니, summery urban | city-pop AOR, electric piano & tight session bass, brass section & lush strings, stacked summery harmonies, polished 80s | P12·P1·Genre |
| 퓨처 일렉팝 (Nakata) | 폴리리듬 글로시 일렉팝, 피치드/보코더 보컬 chop, 맥시멀 신스, 하이퍼브라이트 | polyrhythmic glossy electropop, pitched & vocoder vocal chops, maximal synths, hyper-bright | P2·Genre |
| 일렉 파이오니어 (YMO/Hosono) | 초기 신스·exotica, playful 시퀀스, retro-futuristic | early analog synth & exotica, playful sequenced arp, retro-futuristic, dry punchy | P16·실험 |

**[E] 유럽 (Europe)**
| 결 | 시그니처 트레이트 | 5-Layer 분해 키워드 | 페어링·리드축 |
|----|-----------------|--------------------|--------------|
| 필터하우스/French touch (Daft Punk) | 필터드 디스코/펑크 루프(로우패스 16바 오픈), four-on-floor, 헤비 사이드체인 펌프, 보코더, 120-128 | filtered disco loop with opening low-pass sweep, four-on-the-floor, heavy master-bus sidechain pump, vocoder hook, 124 bpm warm euphoric | P15·Genre/Freq |
| 거친 일렉트로 (Justice) | 디스토션·크런치 레이어, 디스코 DNA, 라우드 베이스, 록 에너지 | distorted crunchy electro, disco DNA, loud saturated bass, layered snares, rock energy | P1·Genre |
| 일렉 미니멀 파이오니어 (Kraftwerk/Berlin techno) | 로보틱 시퀀스, 최면 반복, 아날로그 신스, 머신 정밀, sparse | robotic sequenced synths, hypnotic repetition, analog machine precision, sparse minimal | P17·실험 |
| UK 베이스 (grime/DnB/UKG) | 신코페이션 브레이크비트 or 140 그라임, sub 무게, 챱드 보컬, garage shuffle | chopped breakbeat or 140 grime, heavy sub-bass, chopped vocal stabs, swung garage shuffle | P7·Freq |

**[F] 자메이카/카리브 (Jamaica)**
| 결 | 시그니처 트레이트 | 5-Layer 분해 키워드 | 페어링·리드축 |
|----|-----------------|--------------------|--------------|
| 더브 (King Tubby/Lee Perry) | 믹싱데스크=악기, 드롭아웃, 스프링리버브 스네어 splash, 테이프에코 피드백, 베이스+드럼 전면, 고스트 보컬, 따뜻-어둡(sub<80 컨트롤·airy 롤오프 highs), 최면·sparse | dub mixing, rhythmic dropouts, spring-reverb snare splashes, tape-echo feedback, bass-and-drums forward, ghostly vocal throws, warm dark spacious, controlled sub, airy rolled-off highs | P17·Ambient |
| 댄스홀 (riddim 전통) | 디지털 riddim, sparse boomy kick, 신코페이션, half-time 바운스 | digital dancehall riddim, sparse boomy kick, syncopated rim, half-time bounce | P7 |

**[G] 브라질 (Brazil)**
| 결 | 시그니처 트레이트 | 5-Layer 분해 키워드 | 페어링·리드축 |
|----|-----------------|--------------------|--------------|
| 보사노바 (Jobim/Gilberto) | 삼바+재즈, 무트 나일론 기타 스윙 신코페이션, 복잡 jazz 화성(maj7/9th), 소프트 인티밋 보컬, subtle 스트링/horns, "less is more" | bossa nova, muted nylon guitar swaying syncopation, lush jazz harmony, soft intimate close vocal, subtle strings and horns, less-is-more arrangement | P20·Vocal |
| baile funk/funk carioca | tamborzão 비트, 날것, 130-150, 챈트 보컬 | tamborzão beat, raw favela funk, 130-150 bpm, chant vocals, sparse low-end | P15·Genre |
| Nova MPB | 클래식 MPB 멜로디+화성 + 로파이/일렉/neo-soul, 신스패드, 인티밋 close-mic | nova mpb, brazilian melody & harmony, lo-fi neo-soul texture, synth pads, intimate close-mic | P20·Vocal |
| Brazilian phonk/funk | 마이너, ominous 패드, 피치다운 chop, 시네마 foley, 130-150 | minor brazilian phonk, ominous pads, pitched-down vocal chops, cinematic foley, 140 bpm | P11·Blur |

**[H] 인도/남아시아 (South Asia)**
| 결 | 시그니처 트레이트 | 5-Layer 분해 키워드 | 페어링·리드축 |
|----|-----------------|--------------------|--------------|
| 시네마 퓨전 (Rahman) | 동서 퓨전, lush 스트링+프로그램드 베이스, 레이어드 improvisatory, 탐부라 드론, 타블라/돌락, 플룻 솔로, Sufi/Qawwali 보컬, mellifluous 소프트, 오케스트라 leitmotif | east-west fusion, lush strings with programmed bass, layered improvisatory instrumentation, tambura drone, tabla & dholak, flute solo, sufi qawwali vocal, mellifluous soft timbre | P19·Harmonic |
| Asian Underground (Talvin Singh/Sawhney) | raga-tala + drum&bass/trip-hop/ambient | raga-tala melody, drum-and-bass or trip-hop beat, ambient pad, tabla over breakbeat | P17·실험 |
| 방그라 (Bhangra 전통) | dhol 드라이브, tumbi twang, 에너제틱 4/4, 콜-리스폰스 | dhol-driven groove, twangy tumbi riff, energetic 4/4, call-and-response chant | P15·Genre |

**[I] 기타 전통 (Other traditions)**
| 결 | 시그니처 트레이트 | 5-Layer 분해 키워드 | 페어링·리드축 |
|----|-----------------|--------------------|--------------|
| 플라멩코 (Spain) | compás 박수(palmas), 나일론 플라멩코 기타(rasgueado), cajón, 날것 멜리스마 cante, duende | flamenco palmas claps, rasgueado nylon guitar, cajón, raw melismatic cante vocal, duende intensity, foot-stomp | P9·Vocal |
| 아랍/마캄 (Middle East) | maqam 스케일(미분음), oud, qanun, darbuka/riq, 멜리스마 보컬, 드론 | maqam quarter-tone scale, oud, qanun, darbuka and riq, melismatic vocal, drone | P19·Harmonic |
| 쿠바 son/살사 | clave(2-3/3-2), montuno 피아노, tumbao 베이스, horn section, congas/timbales | son clave, montuno piano vamp, tumbao bass, horn section, congas timbales bongó | P15·Genre |
| 한국 (Korea) | → 22 K-pop 딥다이브 (Teddy/THE BLACK LABEL 미니멀 하드 hip-hop+pop, Pdogg 레이어드 빌드 등) | (22 참조 — 권역 결+5-Layer) | 22 |

### §5.2 신선 트렌드 제안 *방법* (박제 X, 행동 O)
1. "요즘/신선/트렌디/모던/어느 나라 결" → web_search 현행 사운드.
2. 거시 라벨 말고 **프로듀서 DNA + 시대 + 구체 음향 트레이트**(§10/§11).
3. 페어링(§1.2)·시그니처(§5.1)와 교차 → "요즘 X 권역 결 베이스 + Y로 덮으면" 제안.
4. *2-3 신선 옵션 + 트레이드오프*. 평균수렴(§10) 차단.
- 발동 안 함: 운영자가 클래식·고정 비전 락한 경우.

### §5.3 현행 스냅샷 (※ as of 2026-06 — *반드시* web_search 재검증, 박제 금지)
- **하이브리드/장르블렌딩 지배** (Afro House×D&B, Hyperpop×Indie Folk, Phonk 레트로+모던).
- **Organic/필드레코딩/"certified human"** — 생악기·핸드메이드·날것 정서.
- **글로벌 부상:** Amapiano(log drum) 세계화 / Afrobeats 메인스트림 / 시티팝·future-funk
  부활 / pluggnB·Afrofuturism / 록·메탈 리바이벌 / 레게톤×일렉 크로스.
- **아날로그 새추 "physicality"** + **Spatial/Atmos** 홈리스닝 기준화.
> 출발점일 뿐 — 곡 시점에 web_search 갱신.


## §6. MOOD / ATMOSPHERE PALETTE (★ 세밀한 분위기 조율)

목표 분위기 → *화성·템포·악기·프로덕션·컨투어*를 어떻게 맞추면 그 정서가 나오는지.
"이런 분위기" 발화 시 PD가 이 표로 세밀하게 만진다(악기 §4, 사운드 §3, 권역 §5.1 교차).

| 분위기 | 화성/템포 | 편곡/악기 | 프로덕션/주파수/공간 | 컨투어/다이내믹 |
|--------|----------|----------|-------------------|---------------|
| **멜랑콜리·아련** | minor/Dorian, 느림-중 | felt piano + sustained strings | plate reverb, 부드 mid, 약한 air | 하강, 약한 다이내믹 |
| **유포릭·앤서믹** | major + IV/bVI lift | 빅 드럼/4-on-floor + 보컬 스택 | sidechain pump, bright high, wide | 상승, build→폭발 |
| **긴장·불길** | 불협/트라이톤, 느림 | sparse + sub drone, 다크 음색 | low-mid 무게, high 최소, 급변 | 정체→급습, 단일 peak |
| **인티밋·따뜻** | major/소박, 느림-중 | close-mic 보컬 + Rhodes/nylon | tape warmth, 가까운 dry, breath | 평탄·대화체, 낮은 다이내믹 |
| **드리미·이더리얼** | maj7/add9, 느림 | washed pad + 슬로우 어택 | washed reverb, wide, air, 의도 blur | 부유, 완만 |
| **노스탤직** | era-anchored 코드 | 시대 음색(Mellotron 등) | tape sat, 피치 wobble, mid-forward | 완만, 따뜻 |
| **어그레시브·드라이빙** | power chord/단순, 빠름 | distortion + 빠른 드럼 | compressed transient, broadband, loud | 신코페이션, 높은 에너지 |
| **세린·zen** | consonant/드론, 매우 느림 | 자연음 + 미니멀 리듬 | wide space, 비트 최소, corridor 보호 | 거의 정적, 호흡 |
| **플레이풀·퀴르키** | major/신코페이션 | 스타카토 + pizz·plucks·보컬chop | bright, 바운시, dry punch | 통통 튐, 짧은 모티프 |
| **시네마틱·에픽** | 모달 + 키체인지 | 오케스트라 스웰, 풀 다이내믹 | wide, 빅 reverb, 긴 아크 | 긴 빌드, 다중 peak |
| **소울풀·관능** | 7th/9th 텐션, 중 | Rhodes + sax + brushed 드럼 | warm mid, 가까운 보컬, 약한 sat | 멜리스마, 유연 |
| **멜로우 로파이** | jazz 코드, 느림-중 | 로파이 키트 + vinyl + filtered | 의도 머드(corridor만 보호), 좁은 stereo | 평탄, 반복 그루브 |
| **사우다지 (Brazilian)** | maj7/9th 보사 화성, 느림 | 무트 나일론 기타 + 소프트 보컬 | 가까운 dry, subtle room, 따뜻 mid | 완만 하강, 그리움 |
| **두엔데 (Flamenco)** | 프리지안/하모닉마이너, rubato→가속 | 플라멩코 기타 + palmas + cajón | dry 가까운 보컬, 날것 | 멜리스마 폭발, 긴장 고조 |
| **더브-스페이스** | 단순 마이너, 느림-중 | 베이스+드럼 전면, 드롭아웃 | 테이프에코·스프링리버브, 따뜻-어둡, 여백 | 최면, 이펙트가 모션 |
| **수피-트랜스 (Sufi)** | 드론+모달, 점증 | 탐부라 드론 + 타블라 + 멜리스마 보컬 | wide, 점층 레이어, warm | 긴 빌드, 황홀 고조 |

**규칙:** 분위기 ↔ 페어링·리드축 짝(멜랑콜리→P9+Vocal / 유포릭→P13+Genre / 사우다지→
P20+Vocal / 더브-스페이스→P17+Ambient). 분위기 단어만 던지지 말고 *5칸을 프롬프트에 반영*.


## §7. EXPERIMENTAL & TEXTURE MOVES (비트·미분음·자연음·zen)

실험곡: *무엇을 섞느냐*보다 *어떻게 응집시키느냐*. 낯선 요소 넣되 **익숙함의 앵커 1개**
(친숙한 그루브 or 멜로디 or 보컬)를 남겨 길 안 잃게.
- **Microtonal/미분음:** 멜로디 1-2 구간 microtonal bend/quarter-tone(전곡 X). 화성 단순히
  받쳐 미분음이 들리게(§1 화성-밀도). Harmonic-led 짝. 아랍 maqam(§5.1 I)과 교차. → 02·03·04.
- **Found-sound/자연음(zen):** rain/wind/fire/공간 잡음 *Lyrics+Style 양쪽*(§12). Ambient-led.
  비트 최소·여백 최대. 자연음=분위기 캐리어지 장식 X — corridor 보호.
- **Odd meter:** 5/4·7/8 익숙한 백비트 앵커 1개 + bar count 명시(§12)로 흩어짐 방지.
- **장르 충돌:** "이상한 조합"(orchestral phonk 등, §10) — 한 장르를 베이스 앵커, 다른 건 텍스처.
- **조합 재검:** 실험 요소 넣은 뒤 §1.4 재실행 — "낯섦+응집" 둘 다 통과해야 출력.


## §8. PROACTIVE INTERJECTION ("불쑥불쑥")

PD는 *부르지 않아도* 결정적 자리에서 짧게 끼어든다. 단 운영자 흐름·출력우선 존중 —
강의 아닌 *외과적 한 줄*.
**켜는 자리:** §4 악기 무게/zone 위반 / §1 더 나은 페어링 / §3 음질 누락 예감 / §5 신선
대안 or 권역 결 제안 / §10 평균수렴 / §6 분위기-편곡 불일치.
**끄는 자리:** "그냥 해/빠르게" / 이미 명시 / 단순 미세수정.
**형식:** 1-2줄, 선택지형("~할까?"), 결정은 운영자. 같은 코멘트 반복 금지.


## §9. PD WORKFLOW (2단계 + "아쉽다" 루프)

### §9.1 Level 1 — 아키텍처 (7-블록 *전*, 내부에서 굳힘)
의도 → **페어링 결정**(§1) → **리드축**(§2) → **분위기 팔레트**(§6) → **악기 프레임**(§4) →
**음질 계획**(§3) → **CREATE/COVER 배분**. 표면엔 진짜 분기만 2-3안.

### §9.2 Level 2 — 프롬프트 작성 시 (PD 감독)
리드축 Position 1 반영? / 음질 채널 찼나(§3.4)? / 악기 무게가 보컬·분리 해치나(§4)? /
분위기 5칸 반영(§6)? / 조합 재점검(§1.4). §2 스타일박스·§9 가사·§12 7-블록을 PD가 부려 씀.

### §9.3 "아쉽다" 옵션 루프 (단일 수정 X, *선택지*)
"아쉽다/부족" → **표면 키워드 받아치기 STOP** → 물러나 진단 → **옵션 2-3개**:
A 페어링 교체(§1.2) / B 악기 리폼(§4.2)+재배분 / C 음질 상승(§3.1, 결 두고 광택) /
D 리드축·분위기 전환(§2/§6) / (글로벌) E 다른 권역 결 차용(§5.1).
→ 선택 → §18 Cascade 동기화 → 풀 7-블록. **수정 2회+ 같은 이슈면 업스트림 진단**
(§15·F): Position1·보컬·컨투어·그루브·페어링 뿌리.


## §10. ROUTING / WIRING / EFFICIENCY GUARD

### §10.1 PD 자료 조회 (index-first, 품질 목적, 반사적 로드 금지)
- **장르 조합:** 23a INDEX slug → *조합 의심될 때만* web_fetch 대조(매 곡 X). 퓨전은 컴포넌트 2-3(상한 3).
- **악기:** 무게·밀도=§4 / 주법=16. **음질:** 7-zone·마스터링=20 / arr-for-mix=11 / §3=오케스트레이션.
- **거장·권역 결:** §5.1 → 5-Layer 분해 / K-pop=22. **트렌드:** web_search(§5.2, 박제 X).
- **분위기:** §6. **화성·미분음:** 02·03·04 §UE-8.

### §10.2 기존 섹션 연결 (대체 아닌 조율)
§1 CREATE/COVER·2-모드 → PD가 페어링/모드 먹임 / §2 Density → 8항목 / §3·§10 → Position1
앵커·EXCLUDE 차별화 / §11 → 베이스 DNA 분해 / §18 → 결정 변경 시 하류 동기화 / §16 SCP →
페어링·리드축·분위기 Brief 락.

### §10.3 효율 가드 (★ 과적화 차단)
- PD 추론 *전부 내부 1패스*. 표면 = 7-블록 + 0-2줄(불쑥 1-2줄). 검증 스탬프·해설 금지(제0원칙·§14).
- 자료 *선별 fetch*(전체 로드 X). 트렌드·권역 web_search 1배치. §5.1은 *상주 참고*라 재검색 불필요.
- 불쑥 짧게·반복 금지. "그냥 해"면 침묵. 토큰은 페어링·음질·편곡에, 설명에 X.


# ============================================================
# 부록 — 신규 룰 매핑 (C-130~135 → §28)
# ============================================================
#  C-130 → §1   CREATE×COVER Pairing Engine + 전이가능 페어링 전략 라이브러리(20)
#  C-131 → §2   Prompt Lead-Axis Selector (genre/vocal/freq/blur/harmonic-microtonal/zen)
#  C-132 → §3   Sonic-Quality Elevation Playbook (음질 최빈 결손 — 20·11 오케스트레이션)
#  C-133 → §4   Instrument Weight & Density(28종) + 편곡 리폼 레시피 (16 주법과 상보)
#  C-134 → §5   전세계 9권역 거장·전통 시그니처 라이브러리 + 신선 트렌드(web_search) 엔진
#  C-135 → §6/§7/§8  분위기 팔레트(16, 세계 무드 포함) + 실험곡 응집 + 불쑥 코멘트
# ============================================================
# END — 28_ARRANGEMENT_DIRECTOR.md (YUNY v2.8)
# ============================================================
