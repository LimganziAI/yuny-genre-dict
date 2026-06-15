# ============================================================
# 25. LYRIC SOUND ENGINE
# 가사가 '소리로 들리게' 만드는 통합 레이어
# 강세 · 연음 · 세련된 딕션 · Suno 실현 가능성 — 4언어 (한글/영어 최深)
# Version 1.0 (YUNY v2.6 — 2026-05-29)
# ============================================================
# 자리: 06/07/08/10/14가 *각 음운·작법*을 담당. 본 파일은 그것들이
#       "Suno에서 실제 소리로 어떻게 실현되나"를 *통합·판정*. 중복 X, 라우팅 O.
#       호출 트리거: "가사 흐름/연음/강세/세련된 발음" · 번역 후 가사 · 수정단계 사운드.
# ============================================================


## §0. 중복 방지 라우팅 맵 (이미 있는 건 그 파일로)

```
이미 다루는 것                         →  정본 파일 (본 파일은 호출만)
──────────────────────────────────────────────────────────────────
한국어 받침 연음 (꽃이→꼬치)            →  07 §UE-7.3 + 14 §UE-40.3
한국어 받침 부담·자음변동·모음조화      →  07 §UE-7.2~7.6 / 14 §2.3~2.4
스페인어 sinalefa (모음 elision)        →  14 §4bis.5
거장 세련 어휘·이미지 (김이나/8 거장)    →  07 SEC12 / 08 §UE-22
CAPS·늘림·BGV·pipe·stutter·adlib        →  10 §18 (Grenar Dirty Tricks)
stress-kick 정렬 (trochaic landing)     →  14 §2.7 / 10 §21.3
5단계 강세 표기 체계 (* ** Word WORD)    →  지침 §8 / C-102
BPM × 음절 매트릭스                      →  14 §2.2·3.3·4.3·4bis.4 / 지침 §5
검증 [bracket] 보컬 큐 목록              →  10 §17.3
```

**본 파일이 *새로* 박는 것 (진짜 빈자리):**
1. §1 — Suno **실현 가능성 마스터 판정표** (RENDERS / MARGINAL / DECORATIVE)
2. §3.2 — **영어 connected speech 엔진** (catenation·elision·flap-T·linking — 라이브러리 부재였음)
3. §2 — 강세 표기를 *언어 음운 stress에 정렬* + Suno 실현 묶기
4. §4 — accent 처방(06 흡수) + 세련 = '소리로 서는 법'
5. §5 — flow / anti-짜집기 (수정단계 직격)
6. §6 — 번역 후 + 수정단계 사운드 게이트


## §1. ★ SUNO REALIZATION FILTER — 실현 가능성 마스터 판정표 (핵심)

> 운영자 직격: *"실제로 프롬프트에 표현되는지 + Suno가 표현할 수 있는지."*
> 가사 사운드 기법을 3등급으로 — 무엇을 믿고, 무엇을 보강하고, 무엇을 버릴지.

### §1.1 RENDERS — Suno가 확실히 뱉음 (믿고 써라)

```
기법                          실현 메커니즘                              근거
──────────────────────────────────────────────────────────────────────────
ALL CAPS 라인/단어            볼륨↑ · 감정 정점 (1-2회/곡, 대비 필수)     10 §18.5 Tier S
대시 늘림 (lo-o-ove)          모음 sustain (음 길게 끎)                   10 §18.6 Tier S
대시 더듬 (B-b-baby)          rapid attack (빠른 어택)                    10 §18.6 Tier S
철자 분리 (L-O-V-E)           letter-by-letter 발음                       10 §18.6 Tier S
(괄호 텍스트)                 background vocal / 콜앤리스폰스             10 §18.7
[bracket] 보컬 큐             [Whispered][Belted][Held][Airy][Raspy]…    10 §17.3
  - 섹션 헤더 다음 줄          → 섹션 전체 적용
  - 라인 끝                    → 그 라인만 적용
하이픈 runs (rap)             빠른 음절 cadence                          10 §18.4
연음형 철자 (gonna/wanna)     실제 축약 발음으로 노래                     §3.2 (신규)
쉼표 · em-dash (—)            micro-pause (호흡)                          §5
[Pause N bar] (단위 명시)     명시 정지                                  지침 §8
개음절 모음에 sustain         자연스러운 긴 음 (사랑 → 사~)              14 §2.3
EXCLUDE 별도 필드             부정 처리 (Style Box "no"보다 신뢰↑)        10 §17.4
```

### §1.2 MARGINAL — 조건부 · 랜덤 (반드시 RENDERS로 이중 보강)

```
기법                          왜 불안정                    보강책 (RENDERS로 덧대기)
──────────────────────────────────────────────────────────────────────────
*single-asterisk* 강세        마크다운 — Suno 인식 들쭉    → CAPS 또는 [Belted]/[Held] 동반
받침 연음 자동 (꼬치)         Suno가 또렷발음 할 수도      → [Vocal: smooth liaison] metatag (14§UE-40.3)
정확한 stress *위치*          근사만 함                    → 강세 음절을 다운비트 라인에 + CAPS
일본어 pitch-accent (고저)    강약으로 근사                → 핵심 mora에 살짝 늘림
[Soft]                        warm 계열로 끌릴 수 있음     → [Hushed]/[Intimate]로 대체 (10 §17.3 warm계열 함정)
자연 철자의 영어 연음          Suno가 알아서 근사 (운random)→ 핵심부는 연음형 철자로 명시 (§3.2)
```

### §1.3 DECORATIVE — 사람 편집 표시용 (Suno엔 무의미 · 프롬프트 글자수 먹지 마)

```
**double-asterisk** / 이탤릭 / 따옴표(자기인용)* / 숫자 강세표기 / 들여쓰기
→ Suno는 평문으로 읽음. *작가 메모는 가사 박스 밖*에 두고, 박스엔 RENDERS만.
  (*따옴표는 발음엔 무영향이나 자기인용·콜아웃 *의미* 연출엔 유효 — 지침 §8d)
```

### §1.4 운영 룰
- **MARGINAL 단독 금지** — 강세를 `*word*`만으로 주지 마. CAPS/[bracket]/늘림 중 1개 동반.
- **DECORATIVE는 글자수 차지 금지** — `**`·이탤릭으로 프롬프트 채우지 마(글자수 낭비 + 무효).
- 한 기법이 RENDERS면 끝. MARGINAL이면 +1 RENDERS. DECORATIVE면 박스에서 빼라.
- 출력 직전 §7 체크.


## §2. STRESS-AS-SOUND — 강세를 Suno가 '듣게' (언어별 정렬)

> 5단계 *표기*는 지침 §8. 여기선 그 표기를 *언어의 음운 stress에 정렬* + RENDERS 실현.

**보편 3원칙:** (a) 강세 음절 = 강박/킥 정렬(14 §2.7) (b) 표시는 RENDERS 수단으로
(c) `*` 표기는 MARGINAL이니 보강.

```
언어        강세 성격              Suno 실현 어법
──────────────────────────────────────────────────────────────────
English     stress-timed          강세 음절을 다운비트에. 약세는 *함축(reduce)* —
            (강약 뚜렷)            과발음 X. 정점어 CAPS 또는 [Belted].
                                   예: "I DON'T need your VER-sion" (강세 2개만 띄움)
Korean      강세 자유 (07 §2.5)    어절 *첫 음절* + 의미 핵심어에 무게. 표시는
                                   [bracket]/CAPS(영어부분). 자음 강세 = 된소리·
                                   파열음 활용(빠/따/꽝). 예: "[Belted] 다 가져가"
Japanese    pitch-accent (고저)    강약 아님 → Suno는 강약 근사. 핵심 mora에 살짝
                                   늘림으로 고저 흉내. 평탄 위험 → 라인 끝 [Held].
Spanish     규칙적 (끝 2음절)      자연 정렬됨. sinalefa로 흐름 만들고 핵심어 CAPS.
```


## §3. CONNECTED SPEECH / 연음 — '어절 사운드'가 들리게

> 운영자 직격: *"가사 자체가 가지고 있는 어절 사운드가 들리기 위해서 연음."*

### §3.1 한국어 — 흐름(flow) 통합 레시피 (기존 호출 + 묶기)
받침 연음 이론·예시는 **07 §UE-7.3 / 14 §UE-40.3** (꽃이[꼬치]·옷을[오슬]). 본 절은 *운용*:
- **흐름 좋은 연음**(legato·자연): 개음절↔폐음절 교차로 연결감. `[Vocal: connected legato, smooth liaison]`
- **무너짐 위험**: 연음 자리 *3개+/한 줄* → 발음 뭉갬. 줄 쪼개거나 또렷 모드 `[crisp diction]`.
- **의미 깨짐 위험어**: 연음 발음을 철자로 바꾸지 마(꽃이→꼬치로 *쓰면* 의미 상실). 철자는 그대로, 발음은 metatag로.
- **섹션 흐름 강약**: Verse 자연연음(흐름) → Chorus 또렷+강세(전달) → Bridge 다시 연결.
- 흐름이 안 잡히면(운영자 "몇 번 쫘야") → 14 §2.7.3 어절 강세위치 + §2.2 음절수 재점검 후 재배치.

### §3.2 ENGLISH — Connected Speech 엔진 (★ 라이브러리 부재 → 신규 정본)
영어는 stress-timed라 *약세를 뭉개고 강세를 띄우는* 연결발음이 핵심. 자연 철자면 Suno가
근사(MARGINAL)하지만, **핵심부는 연음형으로 명시(RENDERS)**해야 그 '결'이 확실히 산다.

```
현상              설명                          Suno 실현 (RENDERS 명시법)
──────────────────────────────────────────────────────────────────────────
Catenation        자음+모음 연결                자연철자→근사 / 강조시 붙여쓰기 느낌
(자음→모음 연결)   "an apple"→"a-napple"         은 피하고 [legato, connected] cue로
Elision           약모음 탈락                    철자 축약: every→"ev'ry", heaven→"heav'n",
(약음절 탈락)      comfortable→[comf-ta-bul]      'cause(because), 'em(them), o'er(over)
Contraction       구어 축약 — *가장 강력*        gonna/wanna/gotta/kinda/dunno/lemme/
(축약형)           (RENDERS, 구어결 직격)         gimme/ain't/'til → 그대로 쓰면 그대로 노래
Assimilation      인접음 동화                    "didja"(did you) "whatcha"(what you)
                                                 "gotcha" — 캐주얼·랩에 RENDERS
Flap-T (미국식)    t→d (모음 사이)               자연 발생. 강조시 "water"→"wadder"
                  water→[wadder], city→[ciddy]   (US accent 처방시, 06 연동)
Linking-R (영국식) 모음+모음 사이 r              far away→"fa-raway". RP/UK accent 처방시
Yod-coalescence   "Tuesday"→"Chooz-day" (UK)    accent 결 살릴 때만
```
- **실현 원칙**: 캐주얼·R&B·랩 = 축약형 적극(gonna/wanna/gotcha = RENDERS). 발라드·시적 = elision 절제(ev'ry 정도). Sustain은 *open vowel*(go, sky, flow)에 — 자음종결(stop, dark)엔 길게 못 끎.
- **강세 정렬**: 축약은 약세 음절에서 — 강세어는 풀발음 유지. "I'm GONNA make it RIGHT" (강세 2개 풀, 약세 축약).
- **accent별 선택**: US=flap-T / UK=linking-R·yod → §4 accent 처방과 묶어 결정.

### §3.3 JAPANESE — 최소 보강 (mora 균등은 14 §4)
- **母音無声化(devoicing)**: i/u가 무성자음 사이서 약화 — です→[des], した→[shta], すき→[ski]. Suno 자연 근사(MARGINAL). romaji 입력시 무성화 자리 의식.
- **母音融合·連声**: 인접 모음 축약. mora 균등 유지가 1순위(14 §4.3) — 무성화는 결만.
- **라임/대구**는 14 §4.2 호출.

### §3.4 SPANISH — sinalefa 확장 (14 §4bis.5 호출)
- 모음+모음 across words = 1음절: "mi alma"→[mial-ma], "tu amor"→[tua-mor]. 자연 RENDERS.
- 지역 결: seseo(c/z→s, 중남미) / yeísmo(ll→y). accent 처방시 명시.

### §3.5 CROSS-LANG / 번역 후 — 연음 재점검 (운영자 직격: "번역 이후로도 적용")
**번역하면 음절 경계가 바뀌어 연음이 깨진다.** 변환 직후 *해당 언어 §3 패스 1회 필수*.
- 한→영 hook (08 §UE-18): 영어 연음(§3.2) 재설계 — 한국어 음절수 ≠ 영어.
- 영→한 (08 §UE-23): 받침 연음(§3.1) 재점검 — 직역 음절 깨짐 + 받침 과부하 위험.
- 외→한 (일/라→한, 07 §UE-12): 톤 유지하되 받침·연음 한국어 결로 재배치.
- 산출 1줄: `🔊 번역 후 연음 재점검 완료 ([언어] §3.N)`.


## §4. SLEEK DICTION — 세련된 표현이 '소리로' 서게

> 거장 *어휘·이미지*는 07 SEC12 / 08 §UE-22. 본 절은 그게 *발음·강세로 어떻게 세련되게 들리나*.

### §4.1 Accent 처방 by 캐릭터 아키타입 (06 흡수 — 무명시=neutral=억양없음)
```
지적·세련 여성     → "educated California English accent"
차갑고 건조한 톤    → "Pacific Northwest soft educated"
영국 팝 딕션        → "RP-adjacent" / "London-inflected"
스토리텔링·내러티브 → 지역 accent ("Appalachian" / "Southern drawl")
※ Suno엔 accent 슬라이더 없음 → Style Box accent 태그 + 킬링라인 IPA-like
  발음 오버라이드(섹션당 1개+) *2중*. accent 무명시 시 1줄 경고 후 neutral.
```

### §4.2 세련 = 발음의 절제 (담백 ≠ 화려)
- 약세 음절 *함축* — 또박또박 과발음은 촌스러움. (영어 §3.2 elision / 한국어 자연연음)
- 자음 또렷하되 부드럽게: `[crisp but smooth diction]`. 거친 결이면 `[gritty]` 별도.
- 킬링 라인 1개 발음 오버라이드로 시그니처 — 곡 전체 X.
- 과한 vibrato·melisma 절제 = 세련(담백). 폭발 자리만 `[melismatic run]`. (06 §4.4 vibrato)
- 클리셰 발음 회피 (지나친 R&B "yeah-eah" runs 남발 등).


## §5. FLOW / ANTI-짜집기 (수정단계 직격 — A-2 흡수)

> 단절감(짜집기) = Suno 가사 사운드 최대 적. 연결이 흐름을 만든다.
- **Pause 총량 ≤ 10/곡** — Bridge 직전 `[Sudden Absolute Silence:1 bar]` 직후만 밀집 허용.
- 라인 연결은 **대시(—)·쉼표 우선** — `[Pause]`로 호흡 대체 금지(끊김 누적).
- `[Singing: connected phrases, flowing monologue]` 섹션당 1개+ (흐름 강제).
- Instrumental Break 큐에 *서사 연속성 1줄* (앞뒤 단절 방지).
- 머드는 `[Pause]` 남발로 풀지 마 → Hz 분배 strict(14/20) + `[open dynamics]` 긍정.
- **흐름 아크**: Verse 자연연음(흐름) → Pre 빌드 → Chorus 또렷+강세폭발 → Bridge 반전 → Final 변형+폭발 → Outro 여운.


## §6. REVISION-STAGE LYRIC-SOUND GATE (수정단계 — 운영자 "수정단계에서도 그렇고")

> 지침 §18 Cascade Map과 *연동*. 수정 발화 시 사운드 차원 자동 재점검:
```
운영자가 바꾸면          →  사운드 재점검 (출력 前)
──────────────────────────────────────────────────────────────
보컬 톤 / 페르소나        →  §4.1 accent 재처방 + §2 강세 재정렬 + §3 연음 패스
Key / BPM               →  §3 연음·받침 밀도 재계산(14) + sustain=개음절 재배치
언어 전환 / 번역          →  §3.5 연음 재점검 *필수*
장르 점프                →  §4.2 딕션 결(담백↔화려) 재조정 + §1 강세수단 재선택
가사 "흐름이 안 잡혀"     →  §5 anti-짜집기 + 14 §2.7 어절강세 + 음절 재배치
가사 "발음이 뭉개져"      →  §3 연음 자리 ≤3/줄 + §1.2 metatag 보강
```
- 수정 출력 1줄: `🔊 Sound: 연음 [N자리/줄] · 강세 [RENDERS수단] · 딕션 [accent]`


## §7. 출력 직전 LYRIC-SOUND 체크 (지침 9-체크리스트 보조)

```
□ 강세 표시가 RENDERS급인가? (*단독 X → CAPS/[bracket]/늘림 동반)        [§1]
□ 연음 자리 ≤ 3/줄? (초과 → 줄 쪼개기 or [crisp diction])                [§3]
□ Sustain = 개음절 모음에? (자음종결 길게 X)                              [§1/§3]
□ accent 명시됨? (무명시 → 1줄 경고 후 neutral)                          [§4]
□ 번역곡이면 §3.5 연음 재점검 1회 돌았나?                                 [§3.5]
□ Pause ≤ 10/곡? 연결은 대시·쉼표 우선?                                  [§5]
□ DECORATIVE(** 이탤릭)가 프롬프트 글자수 먹고 있지 않나?                 [§1.3]
```


## §8. CROSS-REFERENCE (정합)

```
06  VOCAL_PRODUCTION       — accent 태그(411-450)·vibrato §4.4 (§4 연동)
24  VOCAL_DIRECTION_PATCH   — 발성 메커니즘 §2(twang/cry/fry)·혼성 §3
07  LYRIC_CRAFT_KOREAN     — 받침 연음 §UE-7.3 / 거장 SEC12 / 어미 §UE-12.3
08  LYRIC_CRAFT_ENGLISH    — 거장 §UE-22 / 한↔영 변환 §UE-18·23
10  SUNO_LYRICS_TAGS       — Grenar §18 / 검증 bracket §17.3 / stress-kick §21.3
14  PROSODY_AND_PHONETICS  — 받침/sinalefa/mora 게이트 / BPM×음절 매트릭스
지침 §8 (가사큐) · §18 (Cascade) · D (라우팅)
```

# ============================================================
# END OF 25_LYRIC_SOUND_ENGINE.md (v1.0)
# ============================================================
