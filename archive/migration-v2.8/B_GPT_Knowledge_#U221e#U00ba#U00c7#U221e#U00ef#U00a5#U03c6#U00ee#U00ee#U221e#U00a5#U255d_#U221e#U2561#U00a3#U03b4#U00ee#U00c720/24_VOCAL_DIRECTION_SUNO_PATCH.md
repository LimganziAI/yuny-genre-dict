# 24. VOCAL DIRECTION SUNO PATCH — REAL-WORLD VERIFIED KEYWORDS, MIXED-VOCAL ENFORCEMENT, MULTILINGUAL VOCAL CRAFT
# Version: 1.0 (v2.1 Lyric-Driven Renaissance — 2026-05-27)
# Scope: 06_VOCAL_PRODUCTION.md *비중복 보완*. 06이 학술 baseline / 24는 *실측
#        검증 + 강제력 + 다언어*. 풀바디 자산은 06 / 24는 강제력 + 실측 +
#        다언어 *전용*. 의도적 슬림.
# Use: 매 곡 작업 시 *자동 참조*. 06이 풀바디면 24는 *runtime 인용 자산*.
#      운영자 신고 "혼성 안 박힘" / "에어리 외 모름" / "다언어 약함" 직격.
# Working language: 영문 키워드 본문 + 한국어 운영 어법.
# Cross-ref: 06 (학술 baseline), 10 (lyrics field tags), 14 (음운 게이트).

---

## VERSION 1.0 — 06과 분리 원칙

**06 = 학술 baseline (1,487줄)**
- Voice register / classification / timbre 학술 정의
- Effects (reverb / compression / saturation) 풀바디
- Reference Artist Vocal Types
- 5-element vocal directive
- Vocal Anchor 풀바디

**24 = 비중복 보완 (이 파일)**
- HookGenius 실측 검증 어법 (400+ generations 테스트)
- 발성 메커니즘 *Suno 매핑* (06에 없는 자리)
- 혼성/듀엣/그룹 Style Box 강제력 어법
- 창법 전환 가사큐 표준
- 다언어 보컬 어법 (한국어/영어/일본어/스페인어)
- 자동 강제력 룰 통합 (C-89/C-90/C-91/C-92/C-93)

**중첩 시 24 우선** (실측 검증 강함).

---

## SECTION 1 — HOOKGENIUS 3-LAYER STACK (실측 검증)

외부 검증 (HookGenius 400+ generations 평균):
> *"Character + Delivery + Effects. Specify all three or Suno fills
>  the gaps with its statistical average — which is exactly the sound
>  that makes AI music sound like AI music."*

### §1.1 3-Layer 정의

**Layer 1: Character** — 음색의 *재료*
- raspy / breathy / smooth / gritty / silky / ethereal / gravelly /
  sultry / husky / velvety / warm / dark / bright / crystalline /
  honeyed / weathered / smoky / glassy / woody / granular

**Layer 2: Delivery** — 어떻게 *부르는가*
- intimate / powerful / conversational / belted / whispered / soaring /
  laid-back / commanding / behind-the-beat / declarative / urgent /
  restrained / theatrical / half-spoken / melismatic / deadpan /
  yearning / defiant / ahead-of-beat / projected

**Layer 3: Effects** — 마이크 후 *처리*
- reverb-drenched / dry close-mic / compressed / auto-tuned / lo-fi /
  wide stereo / tape-saturated / broadcast-quality / plate-reverb /
  hall-reverb / vocoder-doubled / formant-shifted / parallel-compressed /
  de-essed / tube-saturated / gated

### §1.2 점수 매핑 (HookGenius 400+ generations)

| 어법 | Voice-Match Score |
|---|---|
| 3-Layer 완비 (C+D+E) | 9.75/10 |
| 2-Layer (C+D) | 8.2/10 |
| 1-Layer (C만) | 7.2/10 |
| 1-Layer (D만) | 6.8/10 |
| 1-Layer (E만) | 5.4/10 |
| 미명시 default | 4.5/10 (통계 평균치 — AI 결) |

### §1.3 Position 1 룰

외부 검증:
> *"Put vocal descriptors first. Not in the middle. Not after the
>  genre. First. Suno front-loads processing."*

**비효율:**
```
"Alternative rock, gritty guitar-driven, raspy male tenor..."
(rock이 Position 1 = vocal 묻힘)
```

**효율:**
```
"Raspy male tenor, gritty and urgent, alternative rock,
 guitar-driven..."
(vocal이 Position 1 = vocal 잠금)
```

**선택 룰:**
- *Vocal-driven* (발라드/R&B/인디/어쿠스틱) → Vocal Position 1
- *Track-driven* (EDM/댄스/인스트루멘탈 강조) → Genre Position 1
- *혼성/듀엣/그룹* → **반드시 Vocal Position 1** (혼성 누락 방지)

### §1.4 검증 점수 9.5+ 어법 풀

**Female:**
```
1. "Smoky alto, behind-the-beat and laid-back, jazz cabaret
    delivery, plate-reverb plus tube saturation"
2. "Bright soprano, controlled belting with chest mix, modern
    K-pop precision, tight pop compression"
3. "Breathy mezzo, whispered intimate verse to belted chorus,
    close-mic to wide stereo, contemporary R&B"
4. "Husky contralto, declarative and ahead-of-beat, rock anthem
    delivery, dry close-mic with tube warmth"
5. "Crystalline soprano, sweet light airy throughout, K-ballad
    inflection, plate-reverb 25% on chorus"
```

**Male:**
```
1. "Gritty tenor, conversational verse to belted chorus,
    alternative rock urgency, dry close-mic"
2. "Velvety baritone, melismatic and laid-back, neo-soul intimate,
    tube-saturated bus"
3. "Husky bass-baritone, half-spoken declarative, dark cinematic
    delivery, dry close-mic with gated reverb"
4. "Falsetto-heavy tenor, ethereal and floating, modern R&B,
    wide stereo with vocoder doubling on chorus"
5. "Weathered baritone, story-telling Appalachian inflection,
    folk-country intimate, no auto-tune"
```

**Group/Mixed:**
```
1. "Mixed male and female group vocals, four-part harmony with
    alternating leads, anthem-pop, wide stereo with crowd-chant
    backing"
2. "Mixed gender duet with male leading verses and female leading
    choruses, alternating call-and-response, R&B-pop crossover,
    tight pop compression"
3. "Female K-pop group vocals — Main soprano clean clear, Sub-vocal
    mezzo airy breathy, Rapper speech-tone cutting, distinct
    timbral identity per member"
```

### §1.5 블랙리스트 (점수 6.0 이하)

```
❌ "good vocals" / "great singer" / "professional vocals" — 의미 X
❌ "beautiful voice" / "nice tone" — 너무 추상
❌ "expressive" 단독 — 약함
❌ "passionate" 단독 → "passionate with controlled chest belt"
❌ "soulful" 단독 → "gospel-rooted soulful with melismatic runs"
❌ "sexy" → "sultry husky breathy intimate"로 분해
❌ "powerful" 단독 → "powerful chest-projected belt with controlled
   vibrato"
❌ "perfect pitch" — Suno 의미 모호
❌ "[Artist]-like" — ban 위험 (C-1 5-Layer 우회)
```

---

## SECTION 2 — 발성 메커니즘 SUNO 매핑 (06에 없는 자리)

06에 *Belting / Mix Voice / Falsetto* 박혀있음. 24는 *06에 없거나 부족한
자리*만:

### §2.1 Twang (비인두 좁힘 — 컨트리/트로트/일부 R&B)

**학술:**
- Nasopharyngeal narrowing
- Cutting brightness
- 한국 트로트 *kkeokgi* 친화

**Suno 어법:**
```
"country twang with nasal forward placement"
"twangy vocal with cutting brightness"
"honky-tonk twang with chest-mix support"
"trot twang with kkeokgi phrase-end melismatic bend"
"blues-rooted twang with grit and bend"
```

### §2.2 Cry (발라드 감정 정점)

**학술:**
- Larynx slight lift + tremor
- Bridge / Final Chorus 자리

**Suno 어법:**
```
"controlled cry on sustained peak notes"
"subtle vocal cry with chest-mix support"
"emotive cry break on bridge climax"
```

**피할 어법:**
- "crying voice" (literal 해석)
- "tearful" 단독 → "tearful intimate with controlled cry"

### §2.3 Yodel Break (의도적 깨짐)

**학술:**
- Chest → falsetto 의도적 break
- Country / 인디 폴크 / Sam Smith / Bon Iver

**Suno 어법:**
```
"yodel break from chest to falsetto on phrase end"
"controlled vocal flip with audible register shift"
"Appalachian-style yodel ornament"
```

### §2.4 Vocal Fry (시작/끝 텍스쳐)

**학술:**
- 성대 가장 낮은 register
- Creaky / rattling
- 현대 팝 / 인디 / R&B 시작/끝

**Suno 어법:**
```
"vocal fry on phrase ends, creaky low register"
"subtle vocal fry texture on intimate lines"
"fry-tinted phrase starts"
```

**피할 어법:**
- "fry singing" (overgeneralization → 전체 곡 fry)
- "growling" (혼동 — fry는 noise X)

### §2.5 Glottal Stop (자음 어택)

**학술:**
- 성문 일시 닫힘
- 강한 음절 시작 / Ariana Grande 결

**Suno 어법:**
```
"glottal stop attacks on consonant starts"
"hard glottal attack on belted notes"
"percussive glottal articulation"
```

### §2.6 Aspiration (h-attack)

**학술:**
- 호흡 먼저 / 음높이 나중
- 인디 / dream pop / 인티밋

**Suno 어법:**
```
"aspirated h-attack on phrase starts"
"breath-first delivery with smooth attack"
"soft aspirated entries on intimate lines"
```

### §2.7 Straight Tone (no vibrato)

**학술:**
- Vibrato 0 / 직선 sustain
- Phoebe Bridgers / Billie Eilish 결

**Suno 어법:**
```
"straight tone throughout, no vibrato"
"no oscillation, sustained dead-flat lines"
"monotone straight delivery, intimate"
```

---

## SECTION 3 — 혼성/듀엣/그룹 STYLE BOX 강제력 (운영자 직격)

### §3.1 문제 진단

운영자 신고:
> *"혼성하랬더니 여자만 나왔거든. 가사큐에만 위쪽에 박아놨더라고. 결국
>  프롬프트 쪽에서 작업을 쳐야 하는데."*

**진단:**
- Lyrics Box [Vocal:] anchor만으로 부족
- *Style Box 첫 자리에 혼성 명시 필수*
- 시스템이 자주 누락 → C-90 강제력 룰

### §3.2 혼성 Style Box 표준

**Tier 1 — Position 1 강제 어법:**
```
"Mixed male and female vocals throughout, with [선창자] leading
 [섹션] and [응답자] leading [섹션], alternating duet structure"
```

**구체 예시:**

```
예 1 — 남자 verse / 여자 chorus:
"Mixed male and female vocals, male tenor (C3-G4, husky and
 conversational) leading verses, female alto (A3-E5, warm and
 powerful) leading choruses, alternating duet structure,
 contemporary pop production"

예 2 — 동등 듀엣:
"Equal duet with male baritone (D3-A4, smooth and intimate) and
 female mezzo (G3-D5, breathy and warm), trading lines throughout
 verses with unison on choruses, indie-folk intimate close-mic"

예 3 — Call-Response:
"Call-and-response duet with male tenor lead phrases answered by
 female soprano response phrases, anthem-pop with wide stereo
 separation"
```

**Tier 2 — 강화 키워드:**
```
"both vocals prominent throughout"
"distinct timbral identity between male and female"
"clear gender alternation pattern"
"male-female call-and-response on chorus"
```

### §3.3 그룹 보컬 표준

**K-Pop Multi-Member:**
```
"Female K-pop group vocals — Main soprano D4-E5 (clean clear
 K-pop mix voice), Sub-vocal mezzo A3-D5 (warm breathy timbre),
 Rapper speech-tone with cutting consonants, Lead vocal 2 mezzo
 G3-D5 (powerful belt with ad-libs). Distinct timbral identity
 per member. Korean primary with English chorus phrases."
```

**Mixed Group (Boy-Girl Group):**
```
"Mixed K-pop group vocals — Female lead soprano (clean clear),
 Female sub-vocal mezzo (airy breathy), Male tenor lead (smooth
 warm), Male rapper (cutting precision). Alternating leads across
 sections with mixed group vocals on chorus"
```

**Choir / Gang Vocal:**
```
"Layered group vocals with main lead and stacked harmony backing
 (SATB choir style), gang-vocal chant on chorus hooks, hall-reverb
 with wide stereo"
```

### §3.4 선창자 지정 표준 (C-91)

**Style Box 어법:**
```
"[gender] vocal opens, [other gender] answers"
"male verse 1 with female entering verse 2"
"female lead through verses with male joining on chorus"
```

**Lyrics Box 동기화:**
```
[Vocal: Mixed male and female duet — vocal 1 male tenor opens
 verse 1, vocal 2 female alto enters verse 2, both join on
 chorus with male leading the hook]

[Intro 4]
[Instrumental]

[Verse 1 8 - V1 (Male) leads]
[V1] First line
[V1] Second line

[Verse 2 8 - V2 (Female) leads]
[V2] First line
[V2] Second line

[Chorus 8 - V1+V2 with V1 leading hook]
[V1+V2] (unison line)
[V1] (male leads hook line)
[V1+V2] (unison response)
```

### §3.5 라벨 어법 표준

**Suno 인식 검증:**
- ✅ `[V1]` / `[V2]` / `[V1+V2]` — bracket label 풀바디 작동
- ✅ `[Male]` / `[Female]` / `[Male+Female]` — gender label
- ✅ `[All]` / `[Group]` — 그룹 chant 자리
- ❌ `vocal 1:` / `V1:` — prefix 어법 (인식 약함)

**캐릭터 이름 어법:**
```
✅ "[Vocal 1 (Serica): female soprano...]" (anchor bracket 안)
✅ "[V1] line by Serica" (body label)
❌ "Serica: line" (prefix)
❌ "[Serica] line" (Vocal 1 라벨 없이 단독)
```

---

## SECTION 4 — 창법 전환 가사큐 표준

### §4.1 섹션 시작 큐 풀

```
Verse 시작 자리:
[Singing: conversational close-mic]
[Singing: hushed intimate whisper]
[Singing: storytelling natural inflection]
[Singing: breathy conversational]
[Singing: deadpan flat delivery]

Pre-Chorus 자리:
[Singing: building anticipation with rising breath]
[Singing: tightening from whisper to mid-voice]
[Singing: ascending intensity]
[Singing: leaning into the next section]

Chorus 자리:
[Singing: anthemic chest belt with controlled vibrato]
[Singing: powerful belted release]
[Singing: full-throated belt with rasp on peaks]
[Singing: soaring melismatic chorus]
[Singing: layered chorus with harmony stacks]

Bridge 자리:
[Singing: stripped down to closer mic intimate]
[Singing: vulnerable half-spoken theatrical]
[Singing: contrasting whispered restraint]
[Singing: emotional cry break with rasp]

Final Chorus 자리:
[Singing: maximum belt with stacked harmonies and ad-libs]
[Singing: explosive final chorus with melismatic ornaments]
[Singing: anthem-singalong layered]

Outro 자리:
[Singing: trailing off with breath release]
[Singing: fading to whisper]
[Singing: held sustained note with vibrato]
```

### §4.2 중간 라인 전환 큐 (12바+ 섹션)

```
[Verse 1 16]
[Singing: hushed conversational]
첫 줄 / 둘째 줄 / 셋째 줄 / 넷째 줄

[Singing: shifting to declarative half-spoken]
다섯째 줄 / 여섯째 줄

[Singing: building to belt]
일곱째 줄 / 여덟째 줄
```

**룰:**
- 4-라인 이상 같은 결로 가면 *결 단조 위험*
- 12바+ 섹션 *최소 2개* 큐
- 4-8바 *1개* 충분

### §4.3 호흡/정지 큐 표준 (단위 명시 의무)

```
[Pause half bar]              — 반 마디
[Pause 1 bar]                 — 한 마디
[Pause 2 bars]                — 두 마디
[Breath]                      — 자연 호흡
[Held note]                   — sustained
[Held 2 bars]                 — 2마디 held

[Mute 1 bar]                  — 1마디 mute
[Sudden Silence 1 bar]        — 갑작스러운 정적
[Sudden Absolute Silence: 1 bar] — 완전 정적
[Instrumental Break 4 bars]   — 4마디 인스트루멘탈
```

### §4.4 쏟아짐 방지 텀 힌트 (C-93)

운영자 신고:
> *"가사큐 작성할 때 중간중간 텀을 AI가 잘 맞춰서 조정하기도 하지만 우리가
>  임의로 힌트를 준다거나 해야 하는데."*

**BPM × 음절 매트릭스:**

| BPM | 한국어 음절/바 | 영어 음절/바 | 위험 |
|---|---|---|---|
| 60-70 | 3-5 | 5-7 | 안전 |
| 70-90 | 4-6 | 6-8 | 안전 |
| 90-110 | 6-8 | 8-10 | 보통 |
| 110-130 | 7-9 | 10-12 | 보통 |
| 130-150 | 6-8 | 9-11 | 위험 |
| 150-170 | 5-7 | 8-10 | 위험 |
| 170+ | 4-6 | 7-9 | 매우 위험 |

**자동 텀 힌트 (130+ BPM + 8 음절/바 초과 시):**
```
[Breath] / [Pause half bar] / [Held note]

격렬 자리:
[Pause 1 bar] / [Mute 1 bar] / [Instrumental Break 2 bars]

호흡 잠금 (모음 sustain):
"never go-o-o-o away" (영어)
"가지 마아아아" (한국어)
```

**예시 — 자동 텀 힌트 박힌 어법:**
```
[Chorus 16]
[Singing: anthemic chest belt with controlled vibrato]
지나갈 줄 알았는데 너는 그대로야
[Breath]
하루가 또 길어지고 새벽은 또 깊어지고
[Pause half bar]
이제는 정말 못 견디겠어
[Held note]
가-지 마-아
[Pause 1 bar]
한 번만 더
```

### §4.5 (whisper:) 검증 사용 (C-21 유지)

**검증 패턴:**
```
1. [Sudden Absolute Silence: 1 bar] 직후 (whisper:):
   [Bridge]
   [Singing: emotional belt]
   너 없이는 못 살아
   [Sudden Absolute Silence: 1 bar]
   (whisper: ...정말로)

2. 라인 전체 속삭임 → [Singing: hushed whisper]:
   ❌ (whisper: 새벽 세 시 라디오)
   ✅ [Singing: hushed conversational whisper]
      새벽 세 시 라디오

3. 듀엣 라인별:
   [V1] (whisper:) 짧은 응답 라인
```

### §4.6 Sound Effects Bracket (C-68)

**Mid-line 박음:**
```
[Verse]
Walking through the night [footsteps]
I hear a voice calling [echo]
Then suddenly [laughter] breaks the silence
```

**Standalone 박지 마:**
```
❌ [Verse]
   Walking through the night
   [footsteps]
   I hear a voice calling
```

**Sound Effect 풀:**
```
[laughter] / [whisper] / [screaming] / [echo] /
[crowd] / [applause] / [footsteps] / [breath] /
[door slam] / [phone ring] / [rain] / [thunder] /
[wind] / [fire] / [ocean] / [traffic] / [crowd cheer]
```

---

## SECTION 5 — INSTRUMENTAL SECTION 표준 (C-92)

### §5.1 문제 진단

운영자 신고:
> *"인트로 아웃트로에서 어줍잖은 독백 넣어서 빡치게 만들더니, 이제는 아예
>  없애는 경우도 많은데 필요에 따라서는 instrumental 이런 거로 지정한다든가
>  간주라든가."*

### §5.2 Instrumental 표준 어법

**Intro:**
```
[Instrumental Intro: 4 bars]
[Acoustic guitar finger-picking with sparse atmospheric pad]

또는:
[Short Instrumental Intro]
[Synth arpeggiator + drum machine]
```

**Outro:**
```
[Instrumental Outro: 8 bars]
[Vocal fades, instruments sustain with fade]

또는:
[Outro - Instrumental Fade]
[Acoustic guitar vamp with chord progression repeating]
```

**Mid-song Instrumental Break (간주):**
```
[Instrumental Break: 4 bars]
[Saxophone solo over chord progression]

또는:
[Instrumental Break: 8 bars between Verse 2 and Final Chorus]
[Guitar solo with band continuing]
```

**Dance Break (K-pop):**
```
[Dance Break: 8 bars]
[Instrumental with drums + bass + lead synth, no vocals]
```

### §5.3 V5 Intro Control (C-61)

**문제:** V5는 intro 자동 확장 → 어줍잖은 독백 위험

**해결 3-옵션:**

**옵션 1: Short Instrumental Intro 명시**
```
[Short Instrumental Intro: 2 bars]
[Acoustic guitar alone]

[Verse 1 8]
...
```

**옵션 2: Verse 직접 시작 (intro 없이)**
```
[Verse 1 8]
[Singing: hushed conversational]
첫 줄
...
```

**옵션 3: 짧은 spoken intro (의도적 자리)**
```
[Intro - Spoken: 2 bars]
[Single spoken phrase preceding band entry]
"...첫 번째 단어..."

[Verse 1 8]
...
```

### §5.4 자동 발의 룰 (C-92)

**시스템 자동 (가사 작성 진입 시):**
1. 컨셉 분석
2. Intro 자리 발의:
   - 어쿠스틱/발라드 → "Acoustic intro 4 bars?"
   - EDM/댄스 → "Synth intro arpeggiator 8 bars?"
   - 영화 OST → "Cinematic intro strings?"
3. 간주 자리 발의:
   - 4분+ 곡 → "Instrumental break Verse 2와 Final Chorus 사이?"
   - K-pop → "Dance break?"
   - 록 → "Guitar solo?"
4. Outro 자리 발의:
   - Fade-out / sustained vamp / abrupt cut

---

## SECTION 6 — 다언어 보컬 어법

### §6.1 한국어 (C-78 직격 — 산업 카테고리 우회)

**❌ 박지 마 (Position 1):**
```
"K-pop vocals" 단독
"Korean vocals" 단독
"K-Idol vocals"
```

**✅ 검증 어법:**
```
"Korean-language vocal topline with crisp consonant diction"
"Hangul lyric phrasing with [microgenre] drums"
"Asian-language vocal crossover" (산업 우회)
"Mixed group vocals" (K-pop multi-member 시뮬)
```

**한국어 발음 결 어법:**
```
"Crisp Korean consonant diction"
"Soft Korean vowel sustain"
"Punchy Korean syllable attack"
"Smooth Korean liquid sounds (ㄹ/ㄴ/ㅁ/ㅇ)"
"Sharp Korean stop consonants (ㄱ/ㄷ/ㅂ)"
```

### §6.2 영어 (Accent 풀)

```
"English natural accent" — 표준 미국
"American English with subtle Southern accent" — 컨트리
"British English with cockney inflection" — UK rock
"English with slight Appalachian accent" — 폴크
"English with NYC streetwise inflection" — 힙합/R&B
"English with West Coast laid-back accent" — California
"English with Caribbean lilt" — 레게/댄스홀
"English with French inflection" — chanson
```

### §6.3 일본어 (Mora Timing 기반)

**특성:**
- *모라 (mora)* timing — syllable이 English와 다름
- "Tokyo" = 4 morae (To-kyo-o)

**Suno 어법:**
```
"Japanese-language vocal topline with clean diction"
"J-pop standard bright clean delivery"
"Anime-style power belt with melismatic ornaments"
"City pop intimate close-mic with breath texture"
"Japanese mora-timed phrasing"
"Smooth Japanese vowel sustain"
```

**J-Pop 시그니처:**
```
시티팝 (Tatsuro Yamashita lineage):
"Male tenor with bright clean J-pop diction, 80s analog warmth,
 mora-timed phrasing with sustained vowels"

Yorushika lineage (Suis 결):
"Female alto with passionate J-rock delivery, slightly nasal
 Japanese diction, dynamic verse-to-belt"

LiSA lineage (anime power):
"Female mezzo with anime power belt and melismatic ornaments,
 Japanese-language with theatrical projection"
```

### §6.4 스페인어 (Stress 패턴)

**특성:**
- *Predictable stress patterns* (penultimate 음절 default)
- *Vowel-ending* → 자유 라임
- *Internal rhyme density*

**Suno 어법:**
```
"Spanish-language vocal delivery with vowel-rich sustain"
"Reggaeton flow with dembow rhythmic pocket"
"Bachata romantic legato Spanish-language"
"Latin pop Spanish-language with melismatic flourishes"
"Latin trap half-spoken Spanish-language with auto-tune washes"
"Bilingual Spanish-English code-switching mid-verse"
```

**Bilingual (Bad Bunny / Rosalia 결):**
```
"Bilingual Spanish-English vocals with code-switching, reggaeton
 flow on Spanish lines and melodic R&B on English hooks"
```

### §6.5 섹션 격리 룰 (C-67)

```
✅ 섹션별 언어 격리:
[Verse 1 - Korean]
사랑해 너만의 길을 걸어가

[Chorus - English]
You're the one, you're the only one

Style Box: "bilingual K-pop Korean verse English chorus"

❌ 섹션 안 혼용 (pronunciation drift):
[Verse]
사랑해 baby 너만이 my one love

✅ Hook 자리 single English word:
[Chorus]
지나갈 줄 알았는데 (forever)
너는 그대로야 (always)
```

---

## SECTION 7 — STYLE BOX ↔ LYRICS BOX 동기화 강제력 (C-89)

### §7.1 동기화 룰

**Lyrics Box [Vocal:] anchor 5-element:**
```
[Vocal: Female alto C4-E5, smooth and soulful, conversational
 verses to belted chorus, contemporary R&B]
```

**Style Box Position 1 동일 정보:**
```
"Female alto vocal, smooth and soulful with breathy intimate
 texture, contemporary R&B production, 88 BPM..."
```

### §7.2 자동 점검 (출력 직전)

```
1. Lyrics Box [Vocal:] anchor 추출
2. Style Box Position 1-3 자리 보컬 descriptor 박혔나?
3. 누락 시 자동 보강
4. 표기: "✅ Style/Lyrics Vocal Sync 통과"
```

### §7.3 출력 직전 자동 점검 통합

**Style Box:**
```
1. Position 1 vocal descriptor 있나? (C-29/C-45)
2. 혼성/듀엣/그룹 명시? (C-90)
3. 선창자 명시 + 동기화? (C-91)
4. 3-Layer Stack 완비?
```

**Lyrics Box:**
```
1. 첫 줄 [Vocal:] anchor? (C-29)
2. 5-element 다 박혔나?
3. 섹션별 [Singing:] 큐? (24 §4.1)
4. 12바+ 섹션 중간 2번째 큐?
5. 호흡/정지/텀 힌트 단위 명시? (C-93)
```

### §7.4 자동 표기 (출력 하단)

```
📋 Vocal Direction 점검:
- Style Box Position 1: Vocal descriptor ✅
- Mixed/Duet 명시: ✅
- Lead 지정 동기화: ✅
- 3-Layer Stack (C/D/E): ✅
- Lyrics [Vocal:] anchor 5/5: ✅
- 섹션별 [Singing:] 큐: ✅ (N개 박힘)
- 호흡/정지 큐 단위 명시: ✅
- BPM × 음절 매치: ✅
```

---

## §8. [SINGING:] 큐 풀바디 매뉴얼 (v2.2 NEW — 옆동네 프로 어법 정합)

**문제 진단**: 옆동네 프로 어법은 [Singing:] 큐 안에 7요소 풀바디. 우리 자산 1-3요소만. C-99 / 10 §UE-46 통합 운영.

### §8.1 매뉴얼 어법 (옆동네 프로 어법 모범 사례)

**Tier 1 (풀바디 — 풍성 자리):**
```
[Singing: full classical tenor with chest voice forward, mezzo-forte,
mid-distance mic, warm legato phrasing with slight rubato on phrase-ends,
expressive vibrato blooming on sustained vowels, tender nostalgic mood,
piano arpeggio carrying chords underneath]
```

**Tier 2 (압축 — 일반 자리):**
```
[Singing: chest tenor, mf, mid-mic, warm legato, vibrato blooming,
nostalgic, piano arpeggio under]
```

**Tier 3 (최소 — Outro / Post-Chorus):**
```
[Singing: voice trails off, decrescendo, breath release]
```

### §8.2 7요소 자동 박힘 매트릭스

| 자리 | Voice | Dynamic | Mic | Phrasing | Expression | Mood | Backing |
|---|---|---|---|---|---|---|---|
| Intro | ✅ | ✅ | ✅ | △ | △ | △ | △ |
| Verse 1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Pre-Chorus | ✅ | ✅ (변화) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Chorus | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (풀) |
| Verse 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (대비) | △ |
| Bridge | ✅ (변화) | ✅ (대비) | ✅ (변화) | ✅ | ✅ | ✅ | ✅ |
| Final Chorus | ✅ | ✅ (peak) | ✅ | ✅ | ✅ | ✅ | ✅ (풀) |
| Outro | △ | ✅ (페이드) | △ | △ | △ | △ | △ |

(✅: 의무 / △: 선택)

### §8.3 풀바디 곡 예 — 매뉴얼 적용

```
[Vocal: female alto-soprano (G3-F#5), dry close-mic for verse intimate,
shifting to mid-back mic for chorus belt, sassy bratty top-line delivery,
English topline only, summer rooftop daylight energy]

[Intro - muted brass stab + plucky synth]
[Singing: hushed alto, pianissimo, close mic intimate, breath-on-capsule]
(Mm, mm-hm)
Ninety in the shade and I don't even care

[Verse 1 - UK garage shuffle, sub-bass enters on bar 5]
[Singing: warm chest voice, mezzo-piano, close mic intimate,
conversational phrasing with slight behind-the-beat feel,
breath audible between phrases, sassy detached mood,
piano arpeggio carrying chords, bass entering on bar 5]
Roof's on fire, no it's just July
...

[Pre-Chorus]
[Singing: lifting to mixed voice, crescendo to mezzo-forte,
moving to mid-distance mic, urgency entering phrasing,
vibrato widening, anticipation, drums building tension,
strings entering underneath +3dB, kick drop on bar 8]
And the city's spinning, spinning
...

[Chorus - half-time, belt to F#5]
[Singing: full belt to F#5, forte, mid-back mic for room presence,
sustained vowels with wide vibrato blooming, triumphant defiant mood,
strings swell underneath +6dB, gang vocal handclap layered, brass stab on the 2-and]
Hell-fire cherry on a summer high
...

[Bridge - half-time, sub-bass solo + vocal stack]
[Singing: stripped to head voice pianissimo, close mic intimate,
no vibrato on opening, vibrato entering on final syllable,
vulnerable yet determined, band drops out leaving only sub-bass and vocal stack,
breath audible]
I'm not waiting for September
...

[Final Chorus - belt highest, full stack, gang clap]
[Singing: belt at peak, fortissimo, mid-back mic + hall ambience,
ritardando into final cadence, triumphant raw edge,
full band crescendo with horn countermelody +6dB, held note tail]
Hell-fire cherry on a summer high (Yeah)
...

[Outro - plucky synth fade + airy belt tail]
[Singing: voice trails off, decrescendo to piano, close mic,
breath release tail, nostalgic resigned mood]
(Mm)
Cherry on my tongue, sun in my hair
```

### §8.4 자동 박힘 강제 룰

```
출력 직전 자동:
1. [Singing:] 큐 매 섹션 박혔나? (Intro 제외 의무)
2. 7-요소 자동 박힘 매트릭스 점검
3. Tier 1 (Chorus / Bridge / Final) 자리 풀바디 의무
4. Tier 2 (Verse / Pre-Chorus) 자리 압축 가능
5. Tier 3 (Outro / Post-Chorus) 자리 최소화
6. 표기:
   "🎤 [Singing:] 큐: Tier 1 [N자리] / Tier 2 [M자리] / Tier 3 [L자리] / 통과"
```

### §8.5 Voice / Mic / Backing 연동 룰

```
보컬 자리 변화 (섹션 간):
- Verse close mic chest → Pre mid mic mixed → Chorus mid-back belt
- 같은 mic distance 곡 전체 사용 X (단조)
- 같은 voice type 곡 전체 사용 X (대비 손실)

Backing 변화 (섹션 간):
- Verse: 1-2 악기 minimal
- Pre-Chorus: 악기 build
- Chorus: full band + 백킹 풀
- Bridge: 악기 drop out + 1-2개만
- Final: full band peak

연동:
- 보컬 변화 + Backing 변화 = 동기화
- 보컬 belt 자리 = Backing full
- 보컬 pianissimo 자리 = Backing drop out
```

---

## END OF FILE — 24_VOCAL_DIRECTION_SUNO_PATCH.md v1.1 (2026-05-28 v2.2 추가)
