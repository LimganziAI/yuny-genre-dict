# Lyric Craft Function Report — YUNY

## 0. Executive goal

이 보고서는 특정 가수나 작사가를 따라 쓰기 위한 자료가 아니다. operator가 제공한 큰 장르/가수 풀을 **craft-diversity map**으로 보고, 좋은 가사가 노래 안에서 수행하는 기능을 추출해 YUNY가 새 화자, 새 장면, 새 사물, 새 훅으로 독창적인 한국어/일본어/글로벌 가사를 만들도록 하는 1차 연구본이다. 원문 가사, 유명 훅, 문장 단위 표현은 보존하지 않고, 화자 압력·어휘 결합·조사/어미·라임/호흡·후렴 기능·섹션 완결 진행만 규칙과 테스트로 변환한다.

## 1. Universal lyric function map

좋은 가사는 “예쁜 말”이 아니라 노래 안에서 일을 한다.

1. **speaker and listener setup**: 누가 누구에게 말하는지 정한다. 대상이 없으면 감정은 허공에 뜬다.
2. **scene/world/object bank**: 곡이 허용하는 사물과 장소를 정한다. 장르마다 사물이 다르다.
3. **emotional or causal thought spine**: 감정은 순서가 있어야 한다. 증거 → 압력 → 후렴 → 변형 → 잔상.
4. **hook/refrain function**: 후렴은 제목 반복이 아니라 화행이다. 고백, 명령, 부정, 위로, 챈트, 이미지 회귀, sound-cell 중 하나를 수행한다.
5. **section progression**: V1은 증거, Pre는 압력, Chorus는 중심 화행, V2는 새 증거/반박, Bridge는 균열, Final은 변한 반복, Outro는 residue.
6. **sound/prosody/mouthfeel**: 입이 부를 수 있어야 한다. 모음, 받침, 강세, 호흡, internal rhyme이 의미와 함께 움직인다.
7. **final completion or residue**: 마지막은 교훈이 아니라 남는 물건, 소리, 몸짓, 또는 바뀐 후렴이다.

## 2. Genre lane craft map

| lane | lyric job | vocabulary attachment | rhyme/prosody | hook function | section progression | failure mode | YUNY rule |
|---|---|---|---|---|---|---|---|
| hip-hop / rap | 압박받는 자아가 세계를 재명명한다 | 이름·숫자·장소·사회어를 동사와 붙여 신분/분노/방어를 만든다 | 끝말보다 내부 박자, 어절 절단, 반복되는 자음 압력 | 자기선언, 반박, 고발, 조롱, 생존 선언 | claim → evidence → reversal → sharper claim | 빈 플렉스, 추상 분노, 라임만 있고 생각 없음 | 라임보다 “다음 줄이 이전 주장에 상처를 내는가”를 먼저 본다 |
| R&B / soul | 닫힌 방 안의 관계 온도를 조절한다 | 빛·숨·피부·전화·새벽·문·잔 같은 근접 사물 | 부드러운 모음, 약한 받침, 유예된 행끝 | 속삭임, 유혹, 부정, 미련, 접촉 요청 | close scene → withheld desire → suspended hook → late confession | 무드만 있고 관계 압력 없음 | 감각어는 관계 행동과 묶어야 한다 |
| ballad | 말하지 못한 감정을 시간과 사물로 늦게 드러낸다 | 계절·길·창문·컵·사진·앨범·전화·방 | 긴 호흡, 어미 온도, 반복 후 작은 변화 | 위로명령, 고백, 체념, 기억 회수 | present wound → memory object → softened chorus → final residue | 성숙한 척하는 철학, 사물 없는 추상 | 감정명사 전 사물/행동 1개를 반드시 둔다 |
| folk / indie / literary | 작은 생활 장면이 큰 정서를 대신한다 | 식탁·정류장·골목·신발·우산·빨래·공구 | 평문 호흡, 행갈이 여백, 낮은 반복 | 관찰, 질문, 조용한 고백, 이미지 회귀 | small scene → social/private pressure → quiet turn → object left behind | 일기/산문/에세이 | “방금 본 행동”처럼 쓰고 결론은 늦춘다 |
| rock / band | 몸과 세계가 부딪히는 선언을 만든다 | 밤·길·불·하늘·피·숨·무대·엔진 | 열린 모음 피크, 강한 동사, 짧은 구호 | 외침, 거부, 결의, 집단 상승 | tension riff → declaration → rupture bridge → final shout/residue | 추상 구호, 몸 없는 저항 | 고음 피크는 추상어보다 몸/행동/장소에 둔다 |
| K-pop / dance | 입이 먼저 기억하는 퍼포먼스 언어를 만든다 | 동작동사·색·숫자·짧은 영어/한국어 셀 | 반복 모음, 또렷한 자음, 콜앤리스폰스 | 챈트, sound-cell, identity slogan, dance command | verse info-lite → pre lift → hook cell → post variation | 의미 0 slogan, 영어 장식 남발 | 훅은 입동작/몸동작/화행 중 하나로 설계한다 |
| trot / public song | 개인 감정을 모두의 말로 즉시 전달한다 | 길·강·고향·어머니·운명·사랑·눈물·밤 | 큰 모음, 호명, 반복 가능한 2행 | 호명, 탄식, 다짐, 운명 수락 | direct address → shared pain → proverb-like refrain → communal release | 박물관 말투, 낡은 단어 나열 | 오래된 정서는 현대 사물 1개로 현재화한다 |
| 7080 / legacy | 시대의 공기와 개인의 삶을 단순한 문장에 담는다 | 바람·거리·집·청춘·친구·기차·편지 | 긴 멜로디 호흡, 명료한 운율 | 회상, 선언, 위로, 세대 기억 | public scene → private memory → broad refrain → aftertaste | 복고 소품만 있고 현재성이 없음 | 시대 단어보다 문장 밀도와 선명한 시선을 배운다 |
| modern life folk | 사소한 생활 습관이 관계의 증거가 된다 | 카페·편의점·지하철·원룸·영수증·우산 | 말하듯 짧게, 같은 어미 과다 금지 | 민망한 고백, 농담 속 진심, 일상 명령 | mundane object → awkward admission → soft hook → small final change | 귀여움 과다, 생활어만 있고 압력 없음 | 생활 사물은 감정 압력을 증명할 때만 쓴다 |
| Japanese lyric craft | 생략과 모라 호흡으로 여운을 만든다 | 계절·빛·그림자·거리·몸짓·작은 자연물 | 모라, 장음/촉음/ん, 체언종지, 여백 | 이미지 회귀, 속삭인 결심, 미완의 잔향 | image field → omission → return phrase → changed silence | 한국어 논리 직역, register 혼합 | 의미보다 register와 모라 호흡을 먼저 고른다 |
| English/global pop lyric craft | stress와 hook clarity로 즉시 기억되게 한다 | strong verbs, concrete nouns, idiom-safe phrases | stress alignment, family rhyme, vowel hooks | title-as-action, chant, emotional spike | setup → pre tension → hook payoff → bridge reframe | cliché rhyme, idiom 오류, 설명 과다 | peak에는 content word와 strong vowel을 놓는다 |


## 3. Korean lyric engine

### 3.1 Korean priority order

1. 화자 압력: 이 사람이 왜 지금 이 말을 해야 하는가.
2. 청자/대상: 연인, 자기 자신, 관객, 세상, 부재자 중 누구인가.
3. 장면/사물 bank: 곡의 세계에 존재할 수 있는 사물 5-9개.
4. 어휘 결합: 사물은 반드시 행동·몸·시간·장소·사회압력 중 하나와 붙는다.
5. 조사 연기: 은/는, 이/가, 을/를, 도, 만, 까지가 태도를 만든다.
6. 어미 온도: -는데, -더라, -지, -잖아, -요, 명사종결 등이 거리와 체온을 만든다.
7. 후렴 기능: 제목 반복 금지. 화행 또는 sound-cell로 결정.
8. 섹션 완결: V2/Bridge/Final이 실제로 의미를 바꿔야 한다.
9. naked lyric survival: cue를 지워도 살아야 한다.
10. anti-AI filter: 개념어, 교훈, 예쁜 추상, generic uplift 삭제.

### 3.2 Josa / particle acting

- **은/는**: 대비, 거리두기, 자기분리. “나는”이 아니라 “나는/너는”의 거리.
- **이/가**: 새롭게 드러난 초점, 뒤늦은 깨달음.
- **을/를**: 손댐, 처리, 욕망, 비난.
- **도**: 남은 것, 이것마저, 양보.
- **만**: 축소, 핑계, 제한.
- **까지**: 감정이나 사건의 확대.
- 조사를 바꿨는데 정서가 안 바뀌면 그 조사는 기능하지 않는다.

### 3.3 Eomi / ending temperature

- **-는데**: 말끝을 열어 미완 압력을 남긴다.
- **-더라**: 뒤늦게 본 기억, 인정, 목격.
- **-지**: 체념, 방어, 가벼운 수락.
- **-잖아**: 상대도 아는 사실을 압박하거나 핑계로 쓴다.
- **-요/-예요**: 거리와 부드러움. 과하면 해설.
- **명사종결**: 시적 cut, final residue, 무게. 과하면 산문.
- 같은 어미 3연속은 chant/minimal 의도 외에는 결함.

### 3.4 Object-before-abstraction discipline

추상 감정은 늦게 등장해야 한다. “사랑/외로움/희망/분노” 같은 단어는 사물·행동·몸 반응이 먼저 증거를 만든 뒤에만 쓴다.

### 3.5 Internal rhyme / vowel / coda

- 발라드/R&B 피크: 열린 모음과 ㄴ/ㅁ/ㅇ 받침이 유리.
- 힙합/댄스: ㄱ/ㄷ/ㅂ/ㅈ 마찰이 리듬을 만든다.
- 록: 열린 모음 피크가 선언성을 살린다.
- 트로트: 큰 모음과 반복 가능한 2행 구조가 중요하다.
- 라임은 장식이 아니라 압력이다. 같은 소리가 같은 감정 감옥을 만들거나, 마지막에 깨져야 한다.

### 3.6 Plain speech vs literary pressure

한국어 가사는 말처럼 자연스러워도 되고, 시처럼 잘려도 된다. 단, 둘 다 기능이 있어야 한다. 말투는 화자를 만들고, 시적 절단은 여백을 만든다. 아무 기능 없는 “예쁜 문장”은 탈락.

### 3.7 Anti-AI Korean

AI 같은 가사는 보통 다음 증상이 있다.

- 주제만 있고 장면이 없다.
- 사물은 많은데 행동이 없다.
- 감정명사가 너무 빨리 나온다.
- 모든 섹션이 같은 어미 온도다.
- 후렴이 제목/주제 반복이다.
- V2와 Final이 사실상 복붙이다.
- cue를 지우면 아무 일도 안 남는다.

## 4. Japanese / global extension

### Japanese

일본어는 한국어 문장 논리를 그대로 옮기면 무거워진다. 먼저 register를 고르고, 모라 호흡을 설계한다. 장음, 촉음, ん이 시간을 먹는다. 의미를 줄이고 이미지·생략·체언종지·미완 여운을 사용한다. 일본어 훅은 설명보다 이미지 회귀와 짧은 결심이 강하다.

### English / global pop

영어는 stress가 핵심이다. 강박에는 content word가 와야 한다. strong verb, concrete noun, idiom-safe phrase, family rhyme/assonance를 감정 안정도에 맞춰 고른다. “tonight/alright” 같은 cliché closure는 피한다. 글로벌 훅은 이해가 빠르고 발음이 선명해야 한다.

### Bilingual / multilingual

줄단위 번역이 아니라 섹션 기능을 옮긴다. 한국어 verse가 장면과 정서를 맡고, 영어/일본어 hook이 sound identity를 맡을 수 있다. 언어 전환은 이벤트여야지 장식이 아니다.

## 5. Craft findings

```yaml
craft_finding:
  id: CF-001
  language: Korean
  genre_lane: hip-hop / rap
  function_name: Claim wound revision
  problem_it_solves: 랩이 라임만 있고 생각이 얕아지는 문제
  speaker_pressure: 나는 증명해야 하지만 동시에 방어한다
  vocabulary_attachment: 사회명사+숫자+장소를 강한 동사로 처리
  hook_or_refrain_function: 자기선언이 다음 줄에서 반박되며 깊어진다
  section_progression: claim→evidence→self-revision→harder claim
  rhyme_or_prosody: 내부운, 어절 단절, 강세 반복
  particle_or_ending_behavior: 반말 종결, 명사종결, 은/는으로 거리두기
  failure_if_misused: 빈 플렉스와 가짜 분노
  yuny_rule: 한 줄의 주장을 다음 줄이 수정하게 하라
  acceptance_test: 두 줄을 바꿔 읽었을 때 두 번째 줄이 첫 줄을 더 날카롭게 해야 통과
  rewrite_drill: 자랑 한 줄을 쓰고 바로 그 자랑의 약점을 찌르는 다음 줄을 써라
  source_basis: genre convention + operator-provided pool
```
```yaml
craft_finding:
  id: CF-002
  language: Korean
  genre_lane: hip-hop / rap
  function_name: Address pressure
  problem_it_solves: 화자가 누구에게 말하는지 흐려지는 문제
  speaker_pressure: 상대/세상/자기 자신 중 하나를 겨냥한다
  vocabulary_attachment: 너/걔/우리/이름/동네 같은 호명어를 동사와 붙인다
  hook_or_refrain_function: 후렴은 반박 또는 경고가 된다
  section_progression: V1 target naming→V2 target reversal→final self-address
  rhyme_or_prosody: 자음 충돌과 짧은 종결
  particle_or_ending_behavior: -지, -잖아, -라니까로 압박
  failure_if_misused: 대상 없는 랩은 독백 소음이 된다
  yuny_rule: 각 벌스 첫 4행의 청자를 고정하라
  acceptance_test: 대명사를 지워도 대상이 복원되면 통과
  rewrite_drill: 같은 사건을 세상에게/너에게/나에게 각각 2행씩 말해라
  source_basis: genre convention
```
```yaml
craft_finding:
  id: CF-003
  language: Korean
  genre_lane: hip-hop / rap
  function_name: Status noun engine
  problem_it_solves: 사회적 압력을 구체화하지 못하는 문제
  speaker_pressure: 존중받고 싶지만 상처를 숨긴다
  vocabulary_attachment: 돈·순위·이름·계약·빚·소문 같은 명사를 행 끝에 둔다
  hook_or_refrain_function: 훅은 지위 확인 또는 지위 거부
  section_progression: scene→status noun→cost→reclaim
  rhyme_or_prosody: 행 끝 명사 무게, 내부 반복
  particle_or_ending_behavior: 을/를로 처리대상, 까지로 확대
  failure_if_misused: 브랜드명 나열만 하면 빈 껍데기
  yuny_rule: 상태가 아니라 비용을 쓰라
  acceptance_test: 명사 뒤에 그 명사를 감당하는 행동이 오면 통과
  rewrite_drill: ‘이름’ ‘번호’ ‘빚’ 중 하나로 감정 4행 쓰기
  source_basis: genre convention
```
```yaml
craft_finding:
  id: CF-004
  language: Korean
  genre_lane: hip-hop / rap
  function_name: Compressed confession
  problem_it_solves: 고백이 발라드처럼 늘어지는 문제
  speaker_pressure: 말하기 싫은 취약함을 리듬 안에 숨긴다
  vocabulary_attachment: 몸 증상+거리 사물+짧은 부정
  hook_or_refrain_function: 후렴은 짧은 부정문 또는 반복 셀
  section_progression: deflect→slip→deny→admit in final
  rhyme_or_prosody: 짧은 모음 반복과 받침 마찰
  particle_or_ending_behavior: 아냐/됐어/몰라/맞아 같은 붕괴어
  failure_if_misused: 감정명사를 길게 설명하면 랩 에너지 붕괴
  yuny_rule: 고백은 세 줄 숨기고 한 단어만 새게 하라
  acceptance_test: 감정단어 없이 취약함이 보이면 통과
  rewrite_drill: ‘괜찮다’ 금지하고 괜찮지 않음을 6행
  source_basis: language/prosody reasoning
```
```yaml
craft_finding:
  id: CF-005
  language: Korean
  genre_lane: R&B / soul
  function_name: Room intimacy
  problem_it_solves: 무드만 있고 관계가 없는 문제
  speaker_pressure: 가까이 있지만 말 못 한다
  vocabulary_attachment: 방·불빛·숨·잔·전화·문을 접촉동사와 붙인다
  hook_or_refrain_function: 훅은 접촉 요청/회피/속삭인 부정
  section_progression: room setup→withheld touch→suspended chorus→late reveal
  rhyme_or_prosody: 부드러운 ㅇ/ㄴ/ㅁ, 열린 모음
  particle_or_ending_behavior: -는데, -같아, -면으로 유예
  failure_if_misused: 향/밤/숨만 나열하면 얕다
  yuny_rule: 감각어는 반드시 관계 행동과 묶어라
  acceptance_test: 감각어 뒤에 누가 무엇을 피하는지 보이면 통과
  rewrite_drill: ‘새벽’ 없이 새벽의 압력을 4행
  source_basis: genre convention
```
```yaml
craft_finding:
  id: CF-006
  language: Korean
  genre_lane: R&B / soul
  function_name: Breath gap hook
  problem_it_solves: 후렴이 너무 말이 많아지는 문제
  speaker_pressure: 하고 싶은 말을 숨 쉬는 틈에 둔다
  vocabulary_attachment: 짧은 동사+호흡+사물 하나
  hook_or_refrain_function: 훅은 빈칸이 남는 짧은 요청
  section_progression: verse close detail→pre silence→hook short phrase
  rhyme_or_prosody: 숨표, 쉼, 모음 지속
  particle_or_ending_behavior: 종결을 흐리되 의미는 흐리지 않기
  failure_if_misused: 긴 문장으로 섹시함을 설명하면 실패
  yuny_rule: R&B 훅은 말의 양보다 숨의 위치를 설계하라
  acceptance_test: 후렴을 절반으로 줄여도 더 세지면 통과
  rewrite_drill: 8음절 이하 후렴 5개 만들기
  source_basis: performance observation
```
```yaml
craft_finding:
  id: CF-007
  language: Korean
  genre_lane: R&B / soul
  function_name: English seam control
  problem_it_solves: 영어가 장식처럼 떠다니는 문제
  speaker_pressure: 한국어 정서와 글로벌 소리 사이에서 흔들린다
  vocabulary_attachment: 영어는 소리/키워드, 한국어는 관계 압력 담당
  hook_or_refrain_function: 훅은 bilingual seam 또는 sound tag
  section_progression: Korean scene→English mouth cell→Korean emotional return
  rhyme_or_prosody: 공유 모음, stress 위치
  particle_or_ending_behavior: 한 섹션 한 언어 또는 기능 분리
  failure_if_misused: 중간중간 영어를 뿌리면 무국적
  yuny_rule: 영어 조각은 의미보다 발음 기능을 먼저 정하라
  acceptance_test: 영어를 빼도 관계가 남고 넣으면 소리가 살아야 통과
  rewrite_drill: 영어 2단어 이하로 후렴 색만 바꾸기
  source_basis: language/prosody reasoning
```
```yaml
craft_finding:
  id: CF-008
  language: Korean
  genre_lane: ballad
  function_name: Object-before-tear
  problem_it_solves: 발라드가 감정요약이 되는 문제
  speaker_pressure: 울고 싶지만 어른스럽게 말한다
  vocabulary_attachment: 컵·창문·옷·앨범·길 같은 사물 먼저
  hook_or_refrain_function: 후렴은 고백/위로명령/체념 중 하나
  section_progression: present object→memory→soft hook→final residue
  rhyme_or_prosody: 긴 호흡, 부드러운 받침
  particle_or_ending_behavior: -죠, -겠죠, -더라, -는데
  failure_if_misused: 철학부터 나오면 AI 발라드
  yuny_rule: 추상 감정 전 만진 사물 1개를 둬라
  acceptance_test: 첫 4행에 손/물건/장소가 있으면 통과
  rewrite_drill: ‘슬프다’ 없이 슬픔을 행동으로 쓰기
  source_basis: operator-provided excerpt + genre convention
```
```yaml
craft_finding:
  id: CF-009
  language: Korean
  genre_lane: ballad
  function_name: Soft guilt engine
  problem_it_solves: 화자가 너무 착하거나 너무 잔인해지는 문제
  speaker_pressure: 떠나는 사람도 자기방어를 한다
  vocabulary_attachment: 계절/시간/길을 죄책감 완충재로 쓴다
  hook_or_refrain_function: 후렴은 상대를 달래는 명령
  section_progression: wound→naturalization→listener action→afterimage
  rhyme_or_prosody: 반복 후 조사 변화
  particle_or_ending_behavior: -예요/-죠로 완충, 짧은 사실문으로 깨기
  failure_if_misused: 완충어미 과다=에세이
  yuny_rule: 부드러운 어미 뒤에 짧은 사실행을 넣어라
  acceptance_test: 친절함 속 자기방어가 읽히면 통과
  rewrite_drill: 이별 사과 없이 상대 행동을 부탁하는 후렴 쓰기
  source_basis: operator-provided excerpt
```
```yaml
craft_finding:
  id: CF-010
  language: Korean
  genre_lane: ballad
  function_name: Counting memory
  problem_it_solves: 추억이 흐릿하게 나열되는 문제
  speaker_pressure: 잊고 싶지만 세는 것을 멈추지 못한다
  vocabulary_attachment: 횟수·시간·물건·몸짓을 숫자화
  hook_or_refrain_function: 후렴은 세기/멈추기/한숨
  section_progression: memory list→compulsion→failed stop→exhausted return
  rhyme_or_prosody: 반복 숫자 셀, 숨 삼킴
  particle_or_ending_behavior: 몇/하나/둘 뒤에 -나/-지로 흔들림
  failure_if_misused: 숫자만 많으면 장난처럼 들림
  yuny_rule: 수량은 강박의 증거로만 써라
  acceptance_test: 숫자가 감정 대신 행동을 만들면 통과
  rewrite_drill: 사랑을 숫자 5개로 증명하되 직접 고백 금지
  source_basis: operator-provided excerpt
```
```yaml
craft_finding:
  id: CF-011
  language: Korean
  genre_lane: ballad
  function_name: Stage loneliness
  problem_it_solves: 공연/무대 소재가 메타 설명이 되는 문제
  speaker_pressure: 박수 속에서도 혼자 남는다
  vocabulary_attachment: 불·막·손뼉·무대·퇴장 같은 공연 사물을 감정 구조로 쓴다
  hook_or_refrain_function: 후렴은 관객과의 일시적 사랑
  section_progression: lights on→communion→lights off→alone
  rhyme_or_prosody: 넓은 모음과 긴 잔향
  particle_or_ending_behavior: -고 나면 반복으로 구조화
  failure_if_misused: 무대 설명만 하면 뮤지컬 해설
  yuny_rule: 공연 사물은 관계의 시작과 종료를 동시에 맡겨라
  acceptance_test: 섹션마다 불/막/박수의 의미가 바뀌면 통과
  rewrite_drill: 무대 사물 3개로 사랑의 시작/끝 쓰기
  source_basis: operator-provided excerpt
```
```yaml
craft_finding:
  id: CF-012
  language: Korean
  genre_lane: folk / indie / literary
  function_name: Plain detail turn
  problem_it_solves: 문학적이려다 흐릿해지는 문제
  speaker_pressure: 사소한 일을 보고도 말하지 못한다
  vocabulary_attachment: 생활 사물+낮은 동사+여백
  hook_or_refrain_function: 후렴은 관찰문이 의미를 바꿔 돌아옴
  section_progression: small detail→social/private pressure→quiet refrain→residue
  rhyme_or_prosody: 평문 행갈이, 과한 운율 금지
  particle_or_ending_behavior: -더라, -는데, 명사종결
  failure_if_misused: 예쁜 비유만 있으면 안 남음
  yuny_rule: 디테일 하나가 전체 정서를 대신하게 하라
  acceptance_test: 줄거리 없이도 장면이 보이면 통과
  rewrite_drill: 편의점/버스/식탁 중 하나로 그리움 쓰기
  source_basis: genre convention
```
```yaml
craft_finding:
  id: CF-013
  language: Korean
  genre_lane: folk / indie / literary
  function_name: Social observation
  problem_it_solves: 개인 감정이 자기연민에 갇히는 문제
  speaker_pressure: 나의 감정이 사회적 장면에 비친다
  vocabulary_attachment: 일·집·동네·표정·뉴스·계절을 연결
  hook_or_refrain_function: 후렴은 개인 고백보다 관찰의 반복
  section_progression: public detail→private recognition→small turn
  rhyme_or_prosody: 말맛 중심, 라임 낮음
  particle_or_ending_behavior: 은/는으로 주제화, 도로 잔여감
  failure_if_misused: 설교가 되면 실패
  yuny_rule: 사회어는 한 사람의 행동으로 축소하라
  acceptance_test: 큰 주제가 작은 행동에 담기면 통과
  rewrite_drill: ‘세상’ 금지하고 사회 압력을 4행
  source_basis: genre convention
```
```yaml
craft_finding:
  id: CF-014
  language: Korean
  genre_lane: folk / indie / literary
  function_name: Image return
  problem_it_solves: 이미지가 장식으로만 쓰이는 문제
  speaker_pressure: 말하지 않은 감정이 사물에 남는다
  vocabulary_attachment: 같은 사물을 V1/Chorus/Outro에서 다르게 처리
  hook_or_refrain_function: 후렴은 이미지 회귀
  section_progression: first sight→changed handling→return→left object
  rhyme_or_prosody: 반복어미보다 이미지 변주
  particle_or_ending_behavior: 조사는 바뀌어야 의미도 바뀜
  failure_if_misused: 같은 사물 반복인데 변화 없으면 실패
  yuny_rule: 반복 사물은 매번 기능이 달라야 한다
  acceptance_test: 사물이 돌아올 때 관계가 바뀌면 통과
  rewrite_drill: 우산 하나를 세 번 다른 의미로 쓰기
  source_basis: literary craft observation
```
```yaml
craft_finding:
  id: CF-015
  language: Korean
  genre_lane: rock / band
  function_name: Body voltage
  problem_it_solves: 록 가사가 구호만 되는 문제
  speaker_pressure: 몸이 먼저 한계에 닿는다
  vocabulary_attachment: 숨·피·목·팔·발·무대·길을 강한 동사와 붙인다
  hook_or_refrain_function: 후렴은 선언/거부/상승
  section_progression: pressure→declaration→instrumental rupture→final vow
  rhyme_or_prosody: 열린 모음 피크, 강한 자음
  particle_or_ending_behavior: 명령형/평서형의 대비
  failure_if_misused: 저항/자유 같은 단어만 외치면 실패
  yuny_rule: 추상 구호 전 몸의 증거를 둬라
  acceptance_test: 고음 단어가 몸/행동이면 통과
  rewrite_drill: ‘자유’ 없이 자유를 몸으로 쓰기
  source_basis: genre convention
```
```yaml
craft_finding:
  id: CF-016
  language: Korean
  genre_lane: rock / band
  function_name: Existential machine
  problem_it_solves: 철학이 산문처럼 되는 문제
  speaker_pressure: 나는 세계와 싸우지만 정확한 대상이 없다
  vocabulary_attachment: 기계·도시·밤·엔진·불빛을 움직이게 한다
  hook_or_refrain_function: 후렴은 질문이 아니라 절단된 선언
  section_progression: world pressure→self split→bridge crack→final phrase
  rhyme_or_prosody: 반복 리프형 문장
  particle_or_ending_behavior: 명사종결과 짧은 부정
  failure_if_misused: 철학명사 나열
  yuny_rule: 철학은 움직이는 사물로 번역하라
  acceptance_test: 철학어를 빼도 압력이 남으면 통과
  rewrite_drill: ‘존재’ 금지하고 존재 불안을 6행
  source_basis: genre convention
```
```yaml
craft_finding:
  id: CF-017
  language: Korean
  genre_lane: K-pop / dance
  function_name: Mouth-first hook
  problem_it_solves: K-pop 훅이 의미 없는 구호가 되는 문제
  speaker_pressure: 무대 위 집단 화자가 즉시 기억되어야 한다
  vocabulary_attachment: 짧은 동작동사+색/숫자/소리 셀
  hook_or_refrain_function: 후렴은 입동작/몸동작/콜응답
  section_progression: verse hint→pre lift→hook cell→post variation
  rhyme_or_prosody: 모음 반복, 파열음 위치
  particle_or_ending_behavior: 어미보다 셀 리듬 우선
  failure_if_misused: 의미 0 반복은 금방 피로
  yuny_rule: 훅은 뜻보다 먼저 입이 하고 싶은가를 본다
  acceptance_test: 3회 반복해도 지루하지 않으면 통과
  rewrite_drill: 2음절/3음절/4음절 hook cell 5개씩 만들기
  source_basis: genre convention
```
```yaml
craft_finding:
  id: CF-018
  language: Korean
  genre_lane: K-pop / dance
  function_name: Identity slogan with evidence
  problem_it_solves: 아이덴티티 슬로건이 허공에 뜨는 문제
  speaker_pressure: 우리는 누구인지 선언해야 한다
  vocabulary_attachment: 색·동작·위치·규칙 위반을 짧게 붙인다
  hook_or_refrain_function: 후렴은 선언+응답
  section_progression: self-name→rule break→chant→dance proof
  rhyme_or_prosody: 강세가 선명한 단어
  particle_or_ending_behavior: 반말/명령형/영어셀 기능분리
  failure_if_misused: 멋진 단어만 나열
  yuny_rule: 슬로건 전 행동 증거를 넣어라
  acceptance_test: 슬로건을 빼도 캐릭터가 보이면 통과
  rewrite_drill: ‘나는 특별해’ 금지하고 특별함을 동작으로 쓰기
  source_basis: genre convention
```
```yaml
craft_finding:
  id: CF-019
  language: Korean
  genre_lane: K-pop / dance
  function_name: Bilingual seam
  problem_it_solves: 이중언어가 흐트러지는 문제
  speaker_pressure: 한국어 감정과 글로벌 훅이 충돌한다
  vocabulary_attachment: 한국어는 상황, 영어는 hook texture나 slogan 담당
  hook_or_refrain_function: 후렴은 언어 전환 자체가 이벤트
  section_progression: Korean setup→English/Korean cell→Korean final turn
  rhyme_or_prosody: 공유 모음/강세
  particle_or_ending_behavior: 섹션 단위 언어 지도
  failure_if_misused: 문장 중간 무작위 영어
  yuny_rule: 언어는 섹션 기능으로 나눈다
  acceptance_test: 언어를 지워도 구조가 무너지지 않으면 통과
  rewrite_drill: 한국어 벌스+짧은 영어 셀 후렴 설계
  source_basis: language/prosody reasoning
```
```yaml
craft_finding:
  id: CF-020
  language: Korean
  genre_lane: trot / public song
  function_name: Direct address force
  problem_it_solves: 트로트가 낡은 단어 모음이 되는 문제
  speaker_pressure: 한 사람에게 말하지만 모두가 알아듣는다
  vocabulary_attachment: 님·당신·어머니·고향·길·강 같은 공통명사와 호명
  hook_or_refrain_function: 후렴은 호명/탄식/다짐
  section_progression: address→shared wound→large refrain→release
  rhyme_or_prosody: 큰 모음, 반복 가능한 2행
  particle_or_ending_behavior: -아/-요/-네/-구나 온도
  failure_if_misused: 옛말 장식
  yuny_rule: 낡은 단어보다 현재의 호명 압력이 중요하다
  acceptance_test: 처음 듣는 사람이 바로 따라 부를 수 있으면 통과
  rewrite_drill: 호명 하나로 4가지 감정 만들기
  source_basis: genre convention
```
```yaml
craft_finding:
  id: CF-021
  language: Korean
  genre_lane: trot / public song
  function_name: Public grief container
  problem_it_solves: 개인 슬픔이 너무 사적으로만 갇히는 문제
  speaker_pressure: 내 사연이 공공의 한으로 넓어진다
  vocabulary_attachment: 길·강·밤·고향·부모·운명을 단순 동사와 붙인다
  hook_or_refrain_function: 후렴은 모두의 탄식
  section_progression: private loss→public noun→refrain→communal release
  rhyme_or_prosody: 모음 개방, 반복 명료성
  particle_or_ending_behavior: -네/-구나/-아라 등 장르 온도
  failure_if_misused: 구식 과장
  yuny_rule: 큰 명사는 작은 현대 물건으로 현재화하라
  acceptance_test: 고향/운명 없이도 트로트 압력이 있으면 통과
  rewrite_drill: 현대 물건 하나로 한을 쓰기
  source_basis: genre convention
```
```yaml
craft_finding:
  id: CF-022
  language: Korean
  genre_lane: 7080 / legacy
  function_name: Era air without museum
  problem_it_solves: 복고를 표면 소품으로만 쓰는 문제
  speaker_pressure: 과거의 공기가 현재의 목소리에 닿는다
  vocabulary_attachment: 거리·바람·청춘·편지·기차·친구를 현재 행동과 묶는다
  hook_or_refrain_function: 후렴은 세대 기억이 아니라 지금의 말
  section_progression: time object→memory→public refrain→current residue
  rhyme_or_prosody: 긴 멜로디 호흡
  particle_or_ending_behavior: 평서/명사종결 절제
  failure_if_misused: 시대 단어 나열
  yuny_rule: 복고는 단어가 아니라 문장의 시야다
  acceptance_test: 지금 들어도 화자가 현재형이면 통과
  rewrite_drill: 오래된 사물 하나를 오늘의 행동으로 쓰기
  source_basis: genre convention
```
```yaml
craft_finding:
  id: CF-023
  language: Korean
  genre_lane: modern life folk
  function_name: Awkward small confession
  problem_it_solves: 생활형 가사가 너무 가벼워지는 문제
  speaker_pressure: 농담처럼 말하지만 숨은 진심이 있다
  vocabulary_attachment: 카페·편의점·원룸·우산·영수증을 민망한 행동과 붙인다
  hook_or_refrain_function: 후렴은 작고 반복 가능한 고백
  section_progression: daily scene→awkward line→soft hook→tiny final shift
  rhyme_or_prosody: 말하듯 짧게, 과운율 금지
  particle_or_ending_behavior: -더라/-는데/-거든 온도
  failure_if_misused: 귀여움만 남음
  yuny_rule: 생활어에는 반드시 말 못한 압력을 심어라
  acceptance_test: 웃긴데 조금 아프면 통과
  rewrite_drill: 편의점 사물로 이별 6행 쓰기
  source_basis: genre convention
```
```yaml
craft_finding:
  id: CF-024
  language: Korean
  genre_lane: indie_literary
  function_name: Controlled strangeness
  problem_it_solves: 난해함이 이미지 쓰레기가 되는 문제
  speaker_pressure: 현실을 비틀되 감정실 하나는 남긴다
  vocabulary_attachment: 불가능한 이미지+구체 사물+반복 규칙
  hook_or_refrain_function: 후렴은 이미지 규칙의 반복/변형
  section_progression: rule→recurrence→bend→final residue
  rhyme_or_prosody: 소리 반복보다 이미지 규칙
  particle_or_ending_behavior: 조사는 비현실을 현실 문법에 고정
  failure_if_misused: 상징 랜덤 나열
  yuny_rule: 초현실도 규칙이 있어야 한다
  acceptance_test: 이미지 3개가 같은 법칙을 따르면 통과
  rewrite_drill: 불가능한 물건 하나에 규칙 붙이기
  source_basis: literary craft observation
```
```yaml
craft_finding:
  id: CF-025
  language: Korean
  genre_lane: lyricist_producer
  function_name: Title as function not noun
  problem_it_solves: 제목이 그냥 반복되는 문제
  speaker_pressure: 곡의 중심 화행이 제목에 갇힌다
  vocabulary_attachment: 제목어를 행동/명령/부정/질문으로 변환
  hook_or_refrain_function: 후렴은 제목을 수행한다
  section_progression: setup→title function→V2 complication→final title change
  rhyme_or_prosody: 제목 위치 강세
  particle_or_ending_behavior: 제목 주변 어미 변화
  failure_if_misused: 제목만 외치면 약함
  yuny_rule: 제목은 물건이 아니라 동사처럼 작동해야 한다
  acceptance_test: 제목 없이도 후렴 기능이 보이면 통과
  rewrite_drill: 명사 제목 5개를 화행으로 바꾸기
  source_basis: songwriting reasoning
```
```yaml
craft_finding:
  id: CF-026
  language: Korean
  genre_lane: lyricist_producer
  function_name: Verse2 escalation
  problem_it_solves: V2가 V1 반복이 되는 문제
  speaker_pressure: 같은 감정이 다른 증거를 요구한다
  vocabulary_attachment: V1 사물과 다른 시간/장소/관계 사물 도입
  hook_or_refrain_function: 후렴 전 의미를 조금 손상시킨다
  section_progression: V1 evidence→chorus claim→V2 contradiction→bridge turn
  rhyme_or_prosody: 반복하되 단어군 교체
  particle_or_ending_behavior: 어미 온도 변화
  failure_if_misused: V2 정보 없음
  yuny_rule: V2는 같은 말이 아니라 새로운 증거다
  acceptance_test: V2 첫 2행이 V1을 다시 해석하면 통과
  rewrite_drill: V1과 같은 감정, 다른 사물 5개로 V2 쓰기
  source_basis: songwriting reasoning
```
```yaml
craft_finding:
  id: CF-027
  language: Korean
  genre_lane: lyricist_producer
  function_name: Bridge truth crack
  problem_it_solves: 브릿지가 장식 파트가 되는 문제
  speaker_pressure: 가장 숨긴 말이 잠깐 새어 나온다
  vocabulary_attachment: 기존 object를 뒤집거나 빈 공간을 만든다
  hook_or_refrain_function: 후렴 기능이 잠시 실패한다
  section_progression: chorus certainty→bridge crack→final altered chorus
  rhyme_or_prosody: 리듬 축소/호흡 확대
  particle_or_ending_behavior: 짧은 사실문, 명사종결
  failure_if_misused: 브릿지가 새 주제 발표
  yuny_rule: 브릿지는 설명이 아니라 균열이다
  acceptance_test: 브릿지 뒤 후렴 의미가 바뀌면 통과
  rewrite_drill: 후렴의 주장 하나를 브릿지에서 깨기
  source_basis: songwriting reasoning
```
```yaml
craft_finding:
  id: CF-028
  language: Korean
  genre_lane: lyricist_producer
  function_name: Outro residue
  problem_it_solves: 엔딩이 갑자기 끝나는 문제
  speaker_pressure: 말은 끝났지만 물건이 남는다
  vocabulary_attachment: 마지막 사물/소리/행동 하나만 남긴다
  hook_or_refrain_function: 후렴 후 잔상
  section_progression: final chorus→subtraction→object residue
  rhyme_or_prosody: 짧은 호흡, 낮은 반복
  particle_or_ending_behavior: 명사종결/미완종결
  failure_if_misused: 새 주제 도입
  yuny_rule: Outro는 결론이 아니라 남는 물건이다
  acceptance_test: 마지막 행이 새 설명 없이 남으면 통과
  rewrite_drill: 사물 하나만 남기는 outro 5개
  source_basis: songwriting reasoning
```
```yaml
craft_finding:
  id: CF-029
  language: Japanese
  genre_lane: Japanese lyric craft
  function_name: Mora-first phrasing
  problem_it_solves: 일본어가 한국어 직역처럼 무거워지는 문제
  speaker_pressure: 말보다 호흡과 생략이 먼저다
  vocabulary_attachment: 계절/빛/거리/몸짓을 짧은 모라군으로 묶는다
  hook_or_refrain_function: 후렴은 이미지 회귀 또는 짧은 결심
  section_progression: image→omission→return→changed silence
  rhyme_or_prosody: 모라, 장음, 촉음, ん 계산
  particle_or_ending_behavior: 조사 최소화, 체언종지 가능
  failure_if_misused: 한국어 문장 논리 강제
  yuny_rule: 일본어는 의미량보다 모라 호흡이 먼저다
  acceptance_test: 큰 의미를 줄여도 노래가 자연스러우면 통과
  rewrite_drill: 한국어 1문장을 일본어 이미지 2행으로 변환
  source_basis: language/prosody reasoning
```
```yaml
craft_finding:
  id: CF-030
  language: Japanese
  genre_lane: Japanese lyric craft
  function_name: Register lock
  problem_it_solves: 일본어 말투가 섞여 가짜가 되는 문제
  speaker_pressure: 화자의 사회적 거리와 장르가 말투를 결정한다
  vocabulary_attachment: 캐주얼/문학/아이돌/밴드 레지스터 중 하나
  hook_or_refrain_function: 후렴은 선택한 register 안에서만 변화
  section_progression: setup→consistent register→final subtle shift
  rhyme_or_prosody: 모라와 문말 질감
  particle_or_ending_behavior: だ/です/ない/たい/体言止め 혼합 제한
  failure_if_misused: 말투 샐러드
  yuny_rule: 일본어는 register 먼저, 감정은 그 다음
  acceptance_test: 3연속 행이 같은 화자 말투면 통과
  rewrite_drill: 같은 내용 3개 register로 따로 쓰기
  source_basis: language/prosody reasoning
```
```yaml
craft_finding:
  id: CF-031
  language: Japanese
  genre_lane: Japanese lyric craft
  function_name: Image return silence
  problem_it_solves: 일본어 후렴이 설명적이 되는 문제
  speaker_pressure: 말하지 않는 것이 감정의 일부다
  vocabulary_attachment: 작은 자연물/거리 사물이 돌아오며 의미 변화
  hook_or_refrain_function: 후렴은 이미지 또는 미완의 잔향
  section_progression: image field→return→cut→residue
  rhyme_or_prosody: 여백, 장음 지속
  particle_or_ending_behavior: 체언종지/미완 종결
  failure_if_misused: 설명문 후렴
  yuny_rule: 후렴에서 해설하지 말고 이미지를 돌아오게 하라
  acceptance_test: 청자가 감정을 추론하면 통과
  rewrite_drill: 한 이미지가 세 번 돌아오는 구조 만들기
  source_basis: literary/prosody reasoning
```
```yaml
craft_finding:
  id: CF-032
  language: English
  genre_lane: English/global pop lyric craft
  function_name: Stress peak content word
  problem_it_solves: 영어 훅이 발음상 약해지는 문제
  speaker_pressure: 가장 센 박에 약한 단어가 오면 훅이 죽는다
  vocabulary_attachment: strong verb/concrete noun을 peak에 둔다
  hook_or_refrain_function: 후렴은 title action 또는 emotional spike
  section_progression: setup→pre lift→hook payoff→bridge reframe
  rhyme_or_prosody: stress alignment, family rhyme
  particle_or_ending_behavior: particles 없음, grammar compression
  failure_if_misused: tonight/alright류 cliché
  yuny_rule: 영어 peak에는 content word를 놓아라
  acceptance_test: 강박 단어만 읽어도 의미가 남으면 통과
  rewrite_drill: 후렴 한 줄의 stress 표시 후 재작성
  source_basis: language/prosody reasoning
```
```yaml
craft_finding:
  id: CF-033
  language: English
  genre_lane: English/global pop lyric craft
  function_name: Idiom safety
  problem_it_solves: 글로벌 가사가 어색한 콜로케이션이 되는 문제
  speaker_pressure: 자연스러운 관용과 새 표현 사이 균형
  vocabulary_attachment: 평범한 idiom을 비틀되 문법은 안전하게
  hook_or_refrain_function: 후렴은 쉽게 이해되는 행동
  section_progression: plain setup→twist phrase→hook clarity
  rhyme_or_prosody: family rhyme/assonance
  particle_or_ending_behavior: N/A
  failure_if_misused: 발명 idiom
  yuny_rule: 낯선 이미지는 문법이 안전할 때만 통한다
  acceptance_test: 원어민이 의미를 즉시 복원하면 통과
  rewrite_drill: 한국어 직역 표현 10개를 자연 영어로 고치기
  source_basis: language reasoning
```
```yaml
craft_finding:
  id: CF-034
  language: English
  genre_lane: English/global pop lyric craft
  function_name: Rhyme stability choice
  problem_it_solves: 라임이 감정과 충돌하는 문제
  speaker_pressure: 화자가 안정/불안정 중 어디에 있는지 정해야 한다
  vocabulary_attachment: closure는 perfect, 불안은 assonance/family
  hook_or_refrain_function: 후렴은 라임 안정도 변화
  section_progression: verse loose→pre tension→chorus stable/unstable
  rhyme_or_prosody: rhyme family hierarchy
  particle_or_ending_behavior: N/A
  failure_if_misused: 라임을 맞추려고 진부한 단어 사용
  yuny_rule: 라임 종류도 감정 상태다
  acceptance_test: 라임을 바꿨을 때 정서가 바뀌면 통과
  rewrite_drill: 같은 후렴을 perfect/as 시리즈로 바꿔보기
  source_basis: songwriting/prosody reasoning
```
```yaml
craft_finding:
  id: CF-035
  language: Global
  genre_lane: Multilingual
  function_name: Section-level translation
  problem_it_solves: 다국어가 줄단위 번역처럼 되는 문제
  speaker_pressure: 언어마다 부르는 방식이 다르다
  vocabulary_attachment: 섹션별 의미 목표와 소리 목표를 분리
  hook_or_refrain_function: 후렴은 언어 seam 또는 sound identity
  section_progression: Korean verse→global hook→Korean emotional return
  rhyme_or_prosody: 공통 모음, stress/mora 대비
  particle_or_ending_behavior: 언어마다 종결 감각 다름
  failure_if_misused: 줄마다 직역
  yuny_rule: 번역이 아니라 섹션 기능을 이식하라
  acceptance_test: 줄 수가 달라도 기능이 같으면 통과
  rewrite_drill: 한국어 후렴을 영어 훅/일본어 훅으로 기능만 변환
  source_basis: multilingual craft reasoning
```
```yaml
craft_finding:
  id: CF-036
  language: Global
  genre_lane: Multilingual
  function_name: Korean identity retention
  problem_it_solves: 글로벌화하다 한국어 정체성이 사라지는 문제
  speaker_pressure: 소리는 넓히되 화자 압력은 유지한다
  vocabulary_attachment: 한국어 사물/조사/어미를 핵심 정서에 남긴다
  hook_or_refrain_function: 영어/일본어는 훅 소리 또는 대비
  section_progression: Korean evidence→global sound cell→Korean final residue
  rhyme_or_prosody: 공유 vowel seam
  particle_or_ending_behavior: 한국어 섹션은 조사/어미 연기 유지
  failure_if_misused: 무국적 pop 문장
  yuny_rule: 글로벌 장치를 넣어도 한국어 장면은 보존하라
  acceptance_test: 한국어 벌스만 읽어도 곡의 정체가 보이면 통과
  rewrite_drill: 글로벌 훅 붙이되 한국어 사물 3개 유지
  source_basis: multilingual reasoning
```
```yaml
craft_finding:
  id: CF-037
  language: Korean
  genre_lane: all lanes
  function_name: Josa acting gate
  problem_it_solves: 조사가 무작위 문법으로만 쓰이는 문제
  speaker_pressure: 화자의 거리/초점/접촉이 흐려진다
  vocabulary_attachment: 은/는/이/가/을/를/도/만/까지를 감정 연기로 선택
  hook_or_refrain_function: 후렴의 조사 변화로 의미 변화
  section_progression: same phrase→particle shift→new stance
  rhyme_or_prosody: 조사 위치가 박자 약점에 걸리지 않게
  particle_or_ending_behavior: 조사=연기
  failure_if_misused: 문법은 맞지만 태도 없음
  yuny_rule: 중요 행의 조사는 반드시 이유를 가져라
  acceptance_test: 조사를 바꾸면 정서가 바뀌어야 통과
  rewrite_drill: 한 문장을 조사만 바꿔 5가지 감정 만들기
  source_basis: Korean grammar reasoning
```
```yaml
craft_finding:
  id: CF-038
  language: Korean
  genre_lane: all lanes
  function_name: Eomi temperature gate
  problem_it_solves: 어미가 단조로워 AI처럼 들리는 문제
  speaker_pressure: 말끝이 태도를 만든다
  vocabulary_attachment: -더라/-는데/-지/-잖아/-요/-다/명사종결을 기능별 배치
  hook_or_refrain_function: 후렴은 어미 온도가 가장 선명해야 한다
  section_progression: verse observation→pre unfinished→chorus claim→final altered ending
  rhyme_or_prosody: 행끝 모음/받침 설계
  particle_or_ending_behavior: 어미 분포 3연속 금지 unless chant
  failure_if_misused: 같은 어미 남발
  yuny_rule: 어미는 문장 끝 장식이 아니라 연기다
  acceptance_test: 어미만 읽어도 화자 온도가 느껴지면 통과
  rewrite_drill: 같은 후렴을 체념/분노/위로 어미로 바꾸기
  source_basis: Korean prosody reasoning
```
```yaml
craft_finding:
  id: CF-039
  language: Korean
  genre_lane: all lanes
  function_name: Subject economy
  problem_it_solves: 나는/내가 반복으로 둔해지는 문제
  speaker_pressure: 화자가 너무 설명적이다
  vocabulary_attachment: 주어 생략 후 필요한 곳에만 복귀
  hook_or_refrain_function: 후렴에서 주어 복귀가 고백/책임이 된다
  section_progression: omit→object evidence→subject return
  rhyme_or_prosody: 주어 반복 리듬 체크
  particle_or_ending_behavior: 은/는으로 자기분리
  failure_if_misused: 주어 과다=번역투
  yuny_rule: 주어는 필요할 때 등장해야 세다
  acceptance_test: 주어 삭제 후 더 자연스러우면 삭제
  rewrite_drill: 나는/내가 5개 중 3개 지우기
  source_basis: Korean language reasoning
```
```yaml
craft_finding:
  id: CF-040
  language: Korean
  genre_lane: all lanes
  function_name: Abstract delay
  problem_it_solves: 가사가 개념어로 시작하는 문제
  speaker_pressure: 정서가 증거 없이 선언된다
  vocabulary_attachment: 사물/행동/몸 반응 뒤 추상어
  hook_or_refrain_function: 후렴에서 추상어가 보상처럼 등장
  section_progression: evidence→pressure→abstract naming→residue
  rhyme_or_prosody: 구체명사와 추상명사 간격
  particle_or_ending_behavior: 추상어 앞 어미 완충
  failure_if_misused: 첫 줄부터 사랑/외로움/희망
  yuny_rule: 감정 이름은 늦게 부를수록 강하다
  acceptance_test: 첫 4행 추상어 0개면 통과
  rewrite_drill: 감정명사 5개를 사물행동으로 변환
  source_basis: universal lyric craft reasoning
```
```yaml
craft_finding:
  id: CF-041
  language: Korean
  genre_lane: all lanes
  function_name: Naked lyric survival
  problem_it_solves: 큐가 없으면 죽는 가사 문제
  speaker_pressure: 퍼포먼스 지시가 이야기를 대신한다
  vocabulary_attachment: 텍스트 자체에 화자/장면/행동을 둔다
  hook_or_refrain_function: 후렴 기능이 cue 없이 보인다
  section_progression: plain readthrough→section shift→final residue
  rhyme_or_prosody: 호흡은 텍스트에도 있어야 함
  particle_or_ending_behavior: N/A
  failure_if_misused: 큐가 감정을 설명
  yuny_rule: 가사는 cue 이전에 살아 있어야 한다
  acceptance_test: 모든 bracket 제거 후에도 노래면 통과
  rewrite_drill: 큐를 지우고 약한 줄 5개 고치기
  source_basis: YUNY runtime reasoning
```
```yaml
craft_finding:
  id: CF-042
  language: Korean
  genre_lane: all lanes
  function_name: Final residue object
  problem_it_solves: 마지막이 결론문으로 닫히는 문제
  speaker_pressure: 청자에게 남을 물체/소리/행동이 필요하다
  vocabulary_attachment: 마지막에 새 설명 대신 돌아온 사물
  hook_or_refrain_function: 후렴 후 작은 잔상
  section_progression: final claim→subtraction→residue
  rhyme_or_prosody: 짧은 행, 모음 잔향
  particle_or_ending_behavior: 명사종결/미완종결
  failure_if_misused: 교훈으로 끝남
  yuny_rule: 마지막은 답이 아니라 남은 물건이다
  acceptance_test: 마지막 행이 요약문이면 실패
  rewrite_drill: 결론문을 사물 잔상으로 바꾸기
  source_basis: songwriting reasoning
```
```yaml
craft_finding:
  id: CF-043
  language: Korean
  genre_lane: all lanes
  function_name: Rhyme as meaning pressure
  problem_it_solves: 라임이 말장난으로만 쓰이는 문제
  speaker_pressure: 반복 소리가 생각의 감옥이 되거나 탈출구가 된다
  vocabulary_attachment: 같은 모음/받침을 의미군과 묶는다
  hook_or_refrain_function: 후렴 반복은 소리+의미 기능 동시
  section_progression: sound pattern→semantic pressure→break pattern
  rhyme_or_prosody: 내부운, 모음색, 받침마찰
  particle_or_ending_behavior: 어미 반복은 의도적으로만
  failure_if_misused: 라임 때문에 문장이 가짜
  yuny_rule: 소리 반복은 의미 반복과 연결되어야 한다
  acceptance_test: 라임이 없어도 문장이 살고, 있으면 압력이 생겨야 통과
  rewrite_drill: 같은 모음으로 압박 4행 쓰고 마지막에 깨기
  source_basis: prosody reasoning
```
```yaml
craft_finding:
  id: CF-044
  language: Korean
  genre_lane: all lanes
  function_name: Object bank lane lock
  problem_it_solves: 장르별 어휘가 뒤섞여 흐려지는 문제
  speaker_pressure: 곡의 세계가 불안정하다
  vocabulary_attachment: 장르 레인별 사물 5-9개만 허용
  hook_or_refrain_function: 후렴 사물은 레인의 대표 물체
  section_progression: lane object→section variation→final return
  rhyme_or_prosody: 어휘군 음색 통일
  particle_or_ending_behavior: 조사/어미도 레인에 맞춤
  failure_if_misused: 무작위 예쁜 사물
  yuny_rule: 처음 정한 세계 밖 사물은 금지 unless bridge rupture
  acceptance_test: 사물만 봐도 장르 세계가 보이면 통과
  rewrite_drill: 발라드/R&B/랩 각각 object bank 만들기
  source_basis: operator-provided pool + genre reasoning
```
```yaml
craft_finding:
  id: CF-045
  language: Korean
  genre_lane: all lanes
  function_name: Listener relation lock
  problem_it_solves: 청자가 없어 가사가 허공에 뜨는 문제
  speaker_pressure: 누구에게 말하는지가 곡의 행동을 결정한다
  vocabulary_attachment: 너/우리/세상/나/관객/부재자를 구분
  hook_or_refrain_function: 후렴은 청자에게 하는 행동
  section_progression: listener setup→pressure→hook action→final relation
  rhyme_or_prosody: 호명 위치와 강세
  particle_or_ending_behavior: 존댓말/반말/공적말투
  failure_if_misused: 대상 없는 감정 독백
  yuny_rule: 후렴 전에 청자를 확정하라
  acceptance_test: 후렴을 말하는 대상이 선명하면 통과
  rewrite_drill: 같은 후렴을 연인/관객/자기자신에게 바꾸기
  source_basis: lyric craft reasoning
```
```yaml
craft_finding:
  id: CF-046
  language: Korean
  genre_lane: all lanes
  function_name: Completion spine
  problem_it_solves: 곡 전체가 예쁜 조각 모음이 되는 문제
  speaker_pressure: 감정이 진행되지 않는다
  vocabulary_attachment: 사물/행동/어미가 섹션별로 변화
  hook_or_refrain_function: 후렴 반복이 마지막에 다른 뜻
  section_progression: V1 proof→Pre pressure→Chorus claim→V2 contradiction→Bridge crack→Final changed claim→Outro residue
  rhyme_or_prosody: 반복과 변주의 균형
  particle_or_ending_behavior: 어미 온도 단계화
  failure_if_misused: V2/Bridge/Final 무변화
  yuny_rule: 섹션마다 새 기능이 있어야 한다
  acceptance_test: 각 섹션 한 문장 요약이 서로 다르면 통과
  rewrite_drill: 같은 후렴을 final에서 의미 바꾸기
  source_basis: songwriting reasoning
```
```yaml
craft_finding:
  id: CF-047
  language: Korean
  genre_lane: all lanes
  function_name: AI-summary detector
  problem_it_solves: AI 같은 한국어를 잡는 문제
  speaker_pressure: 주제만 있고 사람/상황이 없다
  vocabulary_attachment: 개념어를 사물/행동/관계로 환원
  hook_or_refrain_function: 후렴은 slogan이 아니라 행동
  section_progression: summary→object repair→speaker action
  rhyme_or_prosody: 문장 균형 과다 경계
  particle_or_ending_behavior: -것이다/-합니다 과다 주의
  failure_if_misused: 깔끔한 교훈, 예쁜 추상
  yuny_rule: 깔끔하면 의심하고 부끄러운 디테일을 넣어라
  acceptance_test: 한 줄에 누가/어디서/무엇을 했는지 복원되면 통과
  rewrite_drill: 가장 예쁜 3행을 가장 구체적인 3행으로 바꾸기
  source_basis: YUNY failure analysis
```

## 6. Line-level writing tools

### 6.1 20 vocabulary attachment patterns

1. 사물+처리동사: 컵/우산/영수증 같은 물건을 들다·접다·버리다·숨기다로 움직인다.
2. 몸+침묵: 목/손/눈/어깨/숨이 말하지 못한 감정을 대신하게 한다.
3. 시간+사물: 새벽/겨울/오래된 방/버스 시간을 사물과 붙여 거리감을 만든다.
4. 장소+관계: 역/계단/주방/문/무대를 누가 말할 수 있는 자리인지로 만든다.
5. 사회어+상처: 이름/소문/점수/빚/약속을 사적 상처의 표면으로 쓴다.
6. 소리+행동: 비/벨/박수/신발소리/문닫힘을 섹션 전환 신호로 쓴다.
7. 숫자+강박: 횟수/시간/순서를 기억 집착의 증거로 쓴다.
8. 계절+책임회피: 계절/시간이 화자의 죄책감을 완충하는 장치가 된다.
9. 빛+거리: 불빛/형광등/달빛을 친밀함 또는 멀어짐의 거리로 쓴다.
10. 의복+기억: 코트/셔츠/신발을 관계가 몸에 남긴 흔적으로 쓴다.
11. 음식+생활압력: 밥/커피/라면을 사소함으로 위장한 결핍으로 쓴다.
12. 교통+기다림: 버스/열차/택시/신호등을 타이밍과 미련의 장치로 쓴다.
13. 무대+일시적 사랑: 불/막/손뼉/퇴장을 사랑의 시작과 종료 구조로 쓴다.
14. 날씨+행동: 비/바람/눈을 감정 배경이 아니라 행동을 막거나 밀게 한다.
15. 방+접촉회피: 침대/문/잔/창문으로 가까운데 닿지 못하는 압력을 만든다.
16. 도로+선언: 길/차선/터널/엔진을 록/밴드형 돌파감으로 쓴다.
17. 공공명사+개인상처: 고향/강/길/운명을 한 사람의 지금 물건과 붙인다.
18. 소문+이름: 힙합/랩에서 외부 시선이 자기 이름을 어떻게 바꾸는지 쓴다.
19. 색+동작: K-pop 훅에서 색은 분위기가 아니라 동작과 짝지어야 한다.
20. 남은 물건+Outro: 마지막에는 설명보다 돌아온 사물 하나를 둔다.

### 6.2 20 Korean eomi/josa decision rules

1. 은/는은 대비·거리두기·자기분리에 쓴다. 단순 주제표지로 남발하지 않는다.
2. 이/가는 새롭게 보인 사실, 초점, 깨달음에 쓴다.
3. 을/를은 만짐·처리·욕망·비난의 대상으로 쓴다.
4. 도는 남은 감정, 양보, ‘이것마저’의 정서에 쓴다.
5. 만은 축소·핑계·제한의 태도에 쓴다.
6. 까지는 감정이나 사건이 예상보다 멀리 갔을 때 쓴다.
7. -는데는 말끝을 열어 압력을 남길 때 쓴다.
8. -더라는 뒤늦은 목격, 회상, 인정에 쓴다.
9. -지는 체념·방어·가벼운 인정에 쓴다.
10. -잖아는 공유된 사실을 무기로 쓰거나 핑계로 쓴다.
11. -요/-예요는 거리와 부드러움을 만들지만 과하면 해설이 된다.
12. 명사종결은 이미지 잔상과 final weight에 쓰되 산문처럼 남발하지 않는다.
13. 같은 어미 3연속은 chant가 아니면 실패로 본다.
14. 후렴 어미는 곡의 핵심 태도와 직접 연결되어야 한다.
15. Bridge에는 기존 어미 패턴을 깨는 짧은 사실문을 하나 둘 수 있다.
16. 랩에서는 종결어미보다 행끝 명사/동사 강세가 더 중요할 수 있다.
17. R&B에서는 미완 어미와 호흡이 과하면 흐릿해지므로 접촉 행동을 붙인다.
18. 트로트/공중가요는 직접 호명 어미를 쓰되 현대 압력 없이 옛말만 쓰지 않는다.
19. 일본어로 옮길 때 한국어 어미 기능을 일본어 register와 문말 질감으로 재설계한다.
20. 어미 선택 전 화자가 누구에게 말하는지 먼저 정한다.

### 6.3 20 hook function templates

1. 위로명령: 상대에게 행동을 시키지만 화자의 죄책감이 숨어 있다.
2. 부정후렴: ‘아니다’ 계열로 시작하지만 반복될수록 사실을 인정한다.
3. 자기선언: 나는/우리는 누구인지 말하고 다음 줄에서 비용을 보여준다.
4. 이미지회귀: 같은 사물이 후렴마다 돌아오며 의미가 바뀐다.
5. 챈트셀: 2-4음절 소리 단위를 반복하되 한 번은 의미가 꺾인다.
6. 콜앤리스폰스: lead가 claim, group이 짧은 응답을 준다.
7. 속삭인 고백: 짧은 phrase만 남기고 주변을 비운다.
8. 공적 호명: 한 사람에게 부르지만 모두가 따라 부를 수 있다.
9. 반문후렴: 질문처럼 보이지만 사실은 답을 알고 있다.
10. 계산후렴: 숫자/횟수를 세다가 감정이 새어 나온다.
11. 장소후렴: 한 장소명이 관계 전체를 대표한다.
12. 몸후렴: 목/손/숨 같은 신체 반응이 title function을 대신한다.
13. 명령형 훅: 춤/도망/멈춤/기다림 같은 동작을 직접 건다.
14. 사물처리 훅: 버려/접어/닫아/들어 같은 처리동사가 중심이다.
15. 침묵후렴: 말하지 않겠다는 말이 반복된다.
16. 반복파괴 훅: 3회 반복 후 마지막 반복에서 조사/어미/대상만 바꾼다.
17. 영어소리셀 훅: 영어는 의미보다 stress와 vowel을 담당한다.
18. 일본어이미지 훅: 짧은 이미지와 미완 여운으로 돌아온다.
19. 록선언 훅: 몸의 한계 뒤에 선언이 온다.
20. 트로트탄식 훅: 호명+큰 모음+공통명사가 즉시 따라 부르게 한다.

### 6.4 20 section-progression templates

1. V1 object proof → Pre pressure → Chorus claim → V2 contradiction → Bridge crack → Final altered claim → Outro residue
2. V1 public scene → Chorus private admission → V2 social cost → Bridge silence → Final public/private merge
3. V1 room detail → Pre breath gap → Chorus short request → V2 touch avoided → Bridge one true line → Final less words
4. V1 self-claim → V2 self-attack → Bridge target flips inward → Final claim becomes scarred
5. V1 waiting place → Chorus promise/lie → V2 time passes → Bridge body freezes → Final same place changed
6. V1 stage lights on → Chorus communion → V2 applause cost → Bridge lights off → Outro alone object
7. V1 daily object → Chorus awkward confession → V2 object repeats wrong → Bridge joke fails → Final small action
8. V1 city pressure → Chorus identity chant → V2 rumor/name pressure → Bridge stripped name → Final louder chant
9. V1 road/body tension → Pre ignition → Chorus declaration → Bridge stop/breakdown → Final open vowel peak
10. V1 memory list → Chorus counting cell → V2 numbers get smaller → Bridge count stops → Outro one number/object
11. V1 image rule → Chorus image return → V2 rule bends → Bridge impossible anchor → Final residue
12. V1 public grief → Chorus direct address → V2 personal object → Bridge fate questioned → Final communal release
13. V1 Korean scene → Pre shared vowel → Chorus global sound cell → V2 Korean consequence → Final bilingual seam
14. V1 observation → Chorus refrain → V2 same object from new angle → Bridge missing subject → Final object left
15. V1 denial → Pre leak → Chorus denial phrase → V2 proof against denial → Bridge admission → Final denial changed
16. V1 place → Pre movement blocked → Chorus command → V2 place empty → Bridge one body detail → Final leave/return
17. V1 small comedy → Chorus punch phrase → V2 embarrassment worsens → Bridge sincerity → Final laugh with hurt
18. V1 slogan seed → Pre lift → Chorus chant → Post sound cell → V2 rule break → Final one new lift
19. V1 historical/legacy object → Chorus broad memory → V2 current action → Bridge time fold → Final present residue
20. V1 listener address → Chorus request → V2 speaker cost → Bridge unsaid truth → Final request becomes farewell

### 6.5 20 rhyme/prosody/mouthfeel tests

1. Peak syllable test: 가장 높은 음/강박에 조사나 약한 연결어가 놓이면 실패.
2. Open vowel hold test: 길게 끌 단어는 가능하면 ㅏ/ㅓ/ㅗ/ㅜ/이 열린 소리로 둔다.
3. Coda friction test: ㄱ/ㄷ/ㅂ/ㅈ 받침은 빠른 훅에서 리듬감, 느린 발라드 피크에서는 부담.
4. Breath phrase test: 한 행이 한 호흡 안에 말해지는지 소리내어 읽는다.
5. Internal rhyme purpose test: 같은 모음 반복이 의미 압력과 연결되는지 본다.
6. Ending diversity test: 같은 어미 3연속은 chant/minimal이 아니면 수정.
7. Rap bar stress test: 행끝 단어가 status/accusation/cost 중 하나를 갖는지 본다.
8. R&B softness test: 부드러운 소리가 관계 압력을 지우지 않는지 본다.
9. K-pop mouth test: 후렴 셀을 5번 반복해도 입이 피곤하지 않아야 한다.
10. Trot sing-along test: 처음 듣는 사람이 후렴 2행을 따라 할 수 있어야 한다.
11. Japanese mora test: 장음/촉음/ん을 시간 단위로 세고 의미를 줄인다.
12. English stress test: strong beat에 content word가 놓였는지 확인한다.
13. Bilingual seam test: 언어 전환 지점의 모음색이 충돌하지 않는지 본다.
14. Naked read test: 반주 없이 읽어도 문장 압력이 살아야 한다.
15. Fast BPM clutter test: 조사/접속어가 박자를 잡아먹으면 줄인다.
16. Slow BPM essay test: 느린 곡에서 문장이 산문으로 길어지면 사물 중심으로 자른다.
17. Final residue sound test: 마지막 단어가 닫힌 받침으로 너무 뚝 끊기면 의도인지 확인.
18. Call-response gap test: 응답이 들어갈 박자가 실제로 비어 있는지 본다.
19. Bridge contrast test: Bridge prosody가 이전 섹션과 다르게 숨을 쉬는지 본다.
20. Title stress test: 제목어가 반복된다면 매번 같은 의미인지, 변하는지 확인한다.

### 6.6 20 failure repairs for bland Korean

1. 추상어 시작 → 첫 행을 사물+행동으로 교체.
2. 가짜 시적 표현 → 이미지가 관계를 어떻게 바꾸는지 추가.
3. V2 반복 → V1과 다른 시간/장소/증거 사물 도입.
4. 후렴 무기능 → confession/command/denial/chant/image-return 중 하나로 재지정.
5. 어미 단조 → verse/pre/chorus/bridge/final별 어미 온도 배치.
6. 조사 무색 → 핵심 행의 은/는/이/가/을/를/도/만/까지 이유 지정.
7. 라임 억지 → 라임보다 speaker truth 우선, 소리군만 남김.
8. 랩 빈 플렉스 → 비용/상처/반박 줄 추가.
9. R&B 무드 과다 → 관계 행동 하나 추가.
10. 발라드 철학 과다 → 물건 처리 행 하나 추가.
11. 인디 일기화 → 카메라처럼 본 행동만 남기고 해설 삭제.
12. 록 구호화 → 몸/장소/충돌 증거 추가.
13. K-pop 의미 0 → hook cell 안에 semantic spike 하나 삽입.
14. 트로트 박물관화 → 현대 사물 하나로 현재 압력 부여.
15. 영어 직역 → idiom-safe phrase와 stress 재배치.
16. 일본어 직역 → 의미량 줄이고 모라/레지스터 재설계.
17. 큐 의존 → bracket 삭제 후 약한 줄부터 rewrite.
18. Outro 설명문 → 남은 사물/소리/행동 하나로 교체.
19. 주어 반복 → 나는/내가 50% 삭제하고 필요 지점만 복귀.
20. 예쁜데 안 남음 → 가장 구체적인 부끄러운 디테일 하나 추가.

## 7. Test suite

### 7.1 naked lyric test
- pass condition: 모든 cue를 제거해도 화자·장면·후렴 기능·final residue가 남는다
- fail signal: cue가 감정/서사를 설명한다
- repair action: 텍스트 줄을 먼저 고치고 cue는 나중에 다시 설계

### 7.2 Korean naturalness test
- pass condition: 인접 2행이 실제 한국어 말/노래 호흡으로 복원된다
- fail signal: 번역투, 주어 과다, 어미 단조
- repair action: 주어 삭제, 어미 온도 재배치, 사물+행동으로 rewrite

### 7.3 genre lane test
- pass condition: 사물군·어미·호흡·훅 기능이 선택한 장르 레인과 맞는다
- fail signal: 예쁜 사물 랜덤 혼합
- repair action: 레인별 object bank를 다시 잠근다

### 7.4 hook function test
- pass condition: 후렴이 고백/명령/부정/챈트/이미지회귀 등 하나의 일을 한다
- fail signal: 제목만 반복하거나 주제 요약
- repair action: hook speech-act를 먼저 고르고 후렴 재작성

### 7.5 Verse2/Bridge/Final completion test
- pass condition: V2는 새 증거, Bridge는 균열, Final은 변한 반복을 제공한다
- fail signal: V1 반복, Bridge 새 주제, Final 복붙
- repair action: section job 한 줄 요약 후 가장 약한 섹션 재작성

### 7.6 rhyme/prosody test
- pass condition: 강박/피크/모음/받침/호흡이 뜻과 맞다
- fail signal: 조사 피크, 받침 충돌, 라임 억지
- repair action: peak word 교체, 행갈이 조정, 라임 압력 재설계

### 7.7 non-imitation test
- pass condition: 기능만 남고 특정 artist surface가 없다
- fail signal: 이름/대표 표현/유명한 어법을 떠올리게 한다
- repair action: 새 화자·새 사물·새 장면으로 재구축

### 7.8 multilingual transfer test
- pass condition: 언어별 prosody와 register를 다시 설계한다
- fail signal: 한국어 문장 논리 직역
- repair action: 섹션 기능만 유지하고 일본어/영어 구조로 재작성


## 8. Import recommendations

### Project Instructions
Add a compact **Korean Lyric Goal Law**:
- Lyric craft begins with lyric function, not wording.
- Artist pools are craft-diversity material, never imitation instructions.
- Every Korean lyric locks speaker pressure, object bank, josa/eomi temperature, hook function, and section completion before cueing.

### Knowledge 05: lyric dossier / 5000 script
Import:
- universal lyric function map
- section completion spine
- object-before-abstraction discipline
- dual runway relation to lyric function

### Knowledge 06: Korean lyric prosody / hook
Import:
- josa/eomi acting gate
- vowel/coda/mouthfeel tests
- internal rhyme as meaning pressure
- naked lyric survival and AI-summary detector

### Knowledge 07: multilingual lyric cards
Import:
- Japanese mora-first phrasing, register lock, image return silence
- English stress/content-word peak, idiom safety, rhyme stability choice
- multilingual section-level transfer

### Knowledge 10: reference assimilation
Import:
- artist/writer pool = craft-diversity map
- function extraction schema, not style imitation
- genre lane craft map and non-imitation test

### Knowledge 20: installation tests
Import:
- AT-KR-LYRIC-GOAL: naked lyric, genre lane, hook function, V2/Bridge/Final, josa/eomi, prosody, non-imitation, multilingual transfer.

### lyric-craft folder
Create:
- `KOREAN_LYRIC_CRAFT_FUNCTION_ENGINE.md`
- `KOREAN_JOSA_EOMI_ACTING_BANK.md`
- `LYRIC_FUNCTION_FINDINGS_YUNY_WAVE1.md`

### prompt-patterns folder
Create:
- `korean-expression/README.md`
- `korean-expression/hook_function_templates.md`
- `korean-expression/bland_korean_repair_patterns.md`

### tests folder
Create:
- `AT_KR_LYRIC_FUNCTION_01_naked_survival.md`
- `AT_KR_LYRIC_FUNCTION_02_genre_lane.md`
- `AT_KR_LYRIC_FUNCTION_03_josa_eomi.md`
- `AT_KR_LYRIC_FUNCTION_04_section_completion.md`
- `AT_MULTI_LYRIC_TRANSFER_01_japanese_global.md`

## 9. YUNY immediate operating rule

Before writing any serious Korean lyric, YUNY must fill this internal lock:

```yaml
lyric_function_lock:
  language:
  genre_lane:
  lyric_mode:
  speaker_pressure:
  listener_target:
  scene_world_allowed_nouns:
  banned_nouns:
  object_bank:
  vocabulary_attachment_patterns:
  josa_strategy:
  eomi_temperature:
  hook_function:
  section_spine:
  rhyme_prosody_plan:
  final_residue:
  non_imitation_check:
```

If this lock is absent, the draft is underbuilt.
