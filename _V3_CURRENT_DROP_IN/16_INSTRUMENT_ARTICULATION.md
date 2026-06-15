# 16. INSTRUMENT ARTICULATION — 악기 주법 종합 레퍼런스
# Version: 1.0 (NEW v2.2 / 2026-05-09)
# Engine Target: Suno v5.5
# Load Trigger: 악기 주법 / 시대별 사운드 / 장르별 악기 활용
#               결정이 필요할 때. 또는 "올드한 사운드가 나옴"
#               진단 시.
# Companion Files: 11_PRODUCTION_DESIGN.md (믹스 설계),
#                  15_NATURAL_LANGUAGE_DIRECTION.md (Suno 어법),
#                  06_VOCAL_PRODUCTION.md (보컬 디렉티브),
#                  05_GENRE_LIBRARY.md (장르별 정통 어법)

---

## SECTION 0. 목적과 범위

### 0.1 이 파일이 다루는 것

회의록 트리거: "악기들 주법에 대해서도 연출이 가능한지
어떤 용어가 필요한지. 프롬프트에 악기만 어떻게 주법을
하는거고 어떤 장르에서는 어떤 악기들이 주로 쓰이고
최신 음악들에서는 어떤 악기들 EDM 이든 뭐든 하여간
악기가 아니라 어떻게 연출하느냐에 따라서 곡 자체가
완전 최신이 되잖아."

이 파일은 **악기를 어떻게 연출하느냐**를 다룬다.
같은 기타라도 palm-mute / chicken-pickin' / tapping은
완전히 다른 사운드. 같은 신스라도 supersaw / FM bell /
granular는 완전히 다른 결.

악기 자체의 선택보다 **주법(articulation)**이 곡의
시대성과 장르 정체성을 결정한다.

### 0.2 다른 파일과의 차이

- **05 (Genre Library)**: 장르별로 어떤 악기를 쓰는가
- **11 (Production Design)**: 주파수·스테레오·다이내믹 설계
- **15 (Natural Language Direction)**: Suno 프롬프트 어법
- **16 (이 파일)**: 주법 자체의 이론 + 장르별 활용 + 시대성

15 파일이 "Suno에 어떻게 박는가"라면, 16 파일은
"주법을 왜·언제·어떻게 선택하는가"의 의사결정 자료.

### 0.3 사용 워크플로우

```
새 곡 작업 시:
   │
   ├── 컨셉 결정 후 악기 hierarchy 설계 단계
   │      → 16 파일 §1-§7 카테고리별 주법 검토
   │      → 어떤 주법이 컨셉과 맞는가 결정
   │
   ├── 시대성 결정 단계
   │      → 16 파일 §8 시대별 주법 결 검토
   │      → 의도된 시대성 + 의도하지 않은 시대성 분리
   │
   ├── Style Box 작성 단계
   │      → 결정된 주법 → 15 파일 어법 키워드로 변환
   │      → CREATE / COVER 위치별 배치
   │
   └── 출력 후 진단 단계
         → "올드한 사운드" 발생 시 §9 트러블슈팅 활용
```

---

## SECTION 1. GUITAR ARTICULATION

### 1.1 어쿠스틱 기타 주법

#### Fingerpicking (핑거피킹)
- **Travis Picking**: 엄지로 alternating bass + 다른 손가락
  멜로디. Country / folk / Americana 표준.
- **Classical Style**: PIMA 손가락 분담 (Pulgar / Indice /
  Medio / Anular). 클래식 / 라틴 어쿠스틱.
- **Tony Rice Style**: Bluegrass 핑거피킹, 빠른 16th-note
  멜로디.
- **John Mayer Style**: 모던 어쿠스틱 핑거피킹, jazzy 화성
  + 멜로딕 라인.

**Suno 어법** (15 §16.1 참조):
```
"fingerpicked acoustic guitar Travis-style alternating bass"
"classical PIMA fingerstyle nylon string"
"delicate fingerpicking low velocity soft touch no strum attack"
```

#### Strumming (스트러밍)
- **D-DU-UDU**: Folk 표준 strum 패턴
- **Carter Family**: Bass-strum-strum (boom-chick-chick)
- **Reggae Skank**: Off-beat 스트럼만 (and-of-1, and-of-2...)
- **Funk Choke**: 16th 스트럼 + palm mute로 percussive
- **Flamenco Rasgueado**: 손가락 펼치며 빠른 스트럼

**Suno 어법**:
```
"strummed acoustic D-DU-UDU folk pattern"
"Carter-family alternating bass-strum acoustic guitar pattern"
"off-beat skanking electric guitar reggae signature"
```

#### Hybrid Picking (하이브리드 피킹)
- **Chicken Pickin'**: 컨트리 시그니처. 피크 + 손가락
  동시 사용으로 percussive snap.
- **Mark Knopfler Style**: 손가락만으로 멜로딕 + 리듬 동시.

**Suno 어법**:
```
"chicken pickin hybrid pick + fingers country lead"
"chicken-scratch percussive muted strums funk"
```

#### Special Techniques
- **Slide / Bottleneck**: 슬라이드 바로 노트 사이 글라이드
- **Capo**: 카포로 키 변경, 오픈 보이싱 활용
- **Open Tuning**: DADGAD (Celtic), Open G (slide blues),
  Drop D (folk-rock)
- **Percussive Acoustic**: Body tapping + strums (Andy
  McKee style)

### 1.2 일렉트릭 기타 주법

#### 피킹 기법

**Alternate Picking (얼터네이트 피킹)**:
- 다운-업-다운-업 정확한 피킹
- 메탈 / 펑크 / 스피드 메탈 표준
- 모든 노트 같은 어택

**Economy Picking**:
- 같은 방향 연속 피킹으로 효율성
- Frank Gambale style
- 재즈-퓨전

**Sweep Picking**:
- 한 방향으로 여러 줄 연주 (스윕)
- 네오클래시컬 메탈 (Yngwie, Jason Becker)
- 아르페지오 빠른 연주

**Tremolo Picking**:
- 한 노트 빠른 반복
- Death metal / surf rock / shoegaze
- "Trem-pick" 또는 "tremolo picked"

**Hybrid Picking** (일렉트릭):
- 피크 + 손가락 동시
- Country lead, 모던 록 (Tim Henson - Polyphia)

#### 핑거링 기법

**Hammer-on / Pull-off**:
- 피킹 없이 손가락 압력으로 노트 생성
- Legato 라인 만들기
- Allan Holdsworth, John Petrucci

**Tapping**:
- 양손 태핑 (right-hand tapping)
- 8-finger tapping (Stanley Jordan, Tim Henson)
- 화성 + 멜로디 동시 가능

**Bending / Vibrato**:
- 노트 벤드 (반음, 온음, microtonal)
- 비브라토 (wide / narrow / fast / slow)
- 블루스 / 록 표현의 핵심

**String Skipping**:
- 줄 건너뛰며 wider interval 연주
- Modern metal lead

#### 화성 / 텍스처 기법

**Power Chords**:
- 1-5 (또는 1-5-옥타브) dyads
- 록 / 메탈 / 펑크 표준
- "fifth chords" 또는 "power chords"

**Open Chords**:
- 오픈 스트링 활용 보이싱
- Folk / pop / indie

**Barre Chords**:
- 검지로 fret 전체 누르는 코드
- Pop / rock 표준

**Drop Tunings**:
- Drop D, Drop C, Drop B
- Modern metal 시그니처
- 무거운 sub-bass-like 기타 톤

**7-String / 8-String**:
- 추가 저음 줄
- Djent, modern progressive metal

**Palm Muting**:
- 피킹 손바닥으로 줄 살짝 누름
- Tight rhythmic chugging
- 메탈 / 펑크 / funk

#### Effect 기반 주법

**Wah-Wah**:
- 페달로 필터 휩쓸기
- Funk (envelope follower 자동 wah)
- 사이키델릭 록 (Hendrix style)

**Whammy / Tremolo Bar**:
- 브릿지 막대로 피치 흔들기
- Dive bombs (강한 다운)
- Subtle vibrato (가벼운 흔들림)

**Feedback**:
- 앰프와 기타 사이 피드백 활용
- Sustain 무한 가능
- Shoegaze / 노이즈 록

**Harmonics**:
- Natural harmonics (12fret, 7fret 등)
- Pinch harmonics (squealing)
- Artificial harmonics

### 1.3 장르별 기타 주법 매핑

| 장르 | 주요 주법 | 톤 character |
|------|-----------|------------|
| Folk | Fingerpicking, strumming | 어쿠스틱 클린 warm |
| Country | Chicken pickin, hybrid, slide | Telecaster bright twang |
| Blues | Bending, slide, vibrato | Tube amp warm overdrive |
| Funk | 16th strum + palm mute, wah | Single-coil clean wah |
| Reggae | Off-beat skank | Clean spring reverb |
| Rock | Power chords, alternate pick | Tube overdrive |
| Metal | Palm mute chug, sweep, tap | High gain distortion |
| Jazz | Comping, single-line lead | Clean hollow body warm |
| Indie | Jangly arpeggios, reverb | Clean chorus reverb |
| Math rock | Tapping, hybrid, polyrhythm | Clean compressed |
| Shoegaze | Tremolo pick, wall of distortion | Heavy reverb fuzz |
| K-Indie | Telecaster funk choke, fingerpicked acoustic | Clean modern bright |

### 1.4 모던 기타 시그니처 (2020s)

**Polyphia (Tim Henson)**:
- 8-finger tapping
- Hybrid picking with Latin influence
- Modern progressive instrumental

**Plini / Animals as Leaders**:
- Djent palm-muted polyrhythmic
- 7-string / 8-string
- Modern progressive metal

**Modern K-Indie 표준**:
- Palm-muted Telecaster 16th funk choke
- Fingerpicked clean acoustic primary
- Telecaster pair L60/R60 chorus only

---

## SECTION 2. SYNTHESIZER ARTICULATION

### 2.1 Synthesis Type별 캐릭터

#### Subtractive (감산 합성)
- **원리**: 풍부한 파형(saw, pulse) 시작 → 필터로 깎기
- **캐릭터**: 따뜻함, 아날로그 풍성함
- **대표 신스**: Moog, Prophet, Juno, Arturia OB-X
- **장르**: Synth-pop, classic EDM, retro

#### FM (주파수 변조)
- **원리**: Carrier × Modulator 주파수 비율
- **캐릭터**: Bell, metallic, glassy, aggressive
- **대표 신스**: Yamaha DX7, Native Instruments FM8
- **장르**: 80s pop (DX7 piano), modern bass (FM bass)

#### Wavetable (웨이브테이블)
- **원리**: 여러 단일 사이클 파형을 모핑
- **캐릭터**: Evolving, complex, modern
- **대표 신스**: Serum, Vital, Massive
- **장르**: Modern EDM, hyperpop, future bass

#### Granular (그래뉼러)
- **원리**: 짧은 grain (5-200ms)을 layered
- **캐릭터**: Texture, atmospheric, alien
- **대표 신스**: Output Portal, Granulator II
- **장르**: Ambient, sound design, experimental

#### Additive (가산 합성)
- **원리**: Sine wave 누적해서 복잡한 파형 생성
- **캐릭터**: Bell-like, controllable harmonics
- **대표 신스**: Image-Line Harmor, Loomer Aspect
- **장르**: Sound design, experimental

#### Physical Modeling
- **원리**: 실제 악기 물리 시뮬레이션
- **캐릭터**: Plucked string, blown wind, struck mallet
- **대표 신스**: AAS Modelers, Logic Sculpture
- **장르**: Hybrid acoustic/electronic

### 2.2 신스 음색 카테고리

#### Pad (패드)
정의: 길게 sustained, harmonic body 채우는 역할

**서브카테고리**:
- **Warm Analog Pad**: Juno-style, ARP, Moog
- **Lush String Pad**: Vintage strings emulation
- **Shimmer Pad**: 옥타브-up reverb 결합
- **Evolving Pad**: 시간에 따라 음색 변화
- **Cinematic Pad**: 영화 score용 large texture
- **Glass Pad**: 5kHz+ shimmer, 모던 K-pop

#### Lead (리드)
정의: 멜로디 라인 담당, 청자 시선 끌기

**서브카테고리**:
- **Saw Lead**: 가장 흔한 신스 리드
- **Square / Pulse Lead**: 8-bit, 80s arcade
- **Supersaw Lead**: 7-voice detuned (trance)
- **FM Bell Lead**: DX7 metallic
- **Acid Lead**: TB-303 squelchy resonant
- **Vocoder Lead**: Robotic processed voice
- **Pluck Lead**: Short envelope melodic stab

#### Bass (베이스 신스)
- **Sub Bass**: Mono 20-80Hz, felt
- **Reese Bass**: 복잡한 modulated (DnB)
- **Acid Bass**: TB-303 squelchy
- **FM Bass**: Aggressive metallic growl
- **Wobble Bass**: Dubstep modulation
- **Sliding 808**: Pitched sub-bass with glide (drill)

#### Pluck / Stab
- **Pluck**: Short envelope, melodic stab
- **Chord Stab**: Punchy syncopated rhythm
- **Plucky Arp**: 16th-note sequenced

#### Sequencer / Arpeggiator
- **16th Sequence**: Locked rhythmic pattern
- **Arpeggiator Up/Down**: Note 자동 펼침
- **Random Arp**: 무작위 노트 선택

### 2.3 시대별 신스 결

#### 1970s
- **Moog modular**: Warm analog, monophonic
- **ARP 2600**: Phasey filter, semi-modular
- **Mellotron**: Tape-based string emulation
- **Prophet-5**: 첫 polyphonic analog (1978)

#### 1980s
- **Yamaha DX7**: FM bell, 디지털 시대 개막
- **Roland Juno-60/106**: Lush analog pad
- **Roland Jupiter-8**: Premium 80s polyphonic
- **LinnDrum**: Programmed drum machine
- **Oberheim OB-Xa**: Van Halen "Jump" 톤

#### 1990s
- **Korg M1**: 90s preset 시대 (M1 piano, organ)
- **Roland JD-800**: 디지털 종합
- **Access Virus**: Trance / techno virtual analog
- **Nord Lead**: VA 합성 시대

#### 2000s-2010s
- **Native Instruments Massive**: EDM / dubstep 표준
- **Sylenth1**: Trance / progressive house
- **Serum (2014)**: Wavetable 혁명
- **Diva**: Analog modeling 정점

#### 2020s
- **Vital (free)**: Modern wavetable
- **Pigments**: Hybrid synthesis modern
- **Phase Plant**: Modular routing complex
- **Hardware revival**: Behringer 리이슈, ARP 2600 복각

### 2.4 모던 신스 시그니처 (2024-2026)

**Modern K-pop 4-5세대**:
- Crystal clear synth pluck (modern, no vintage warmth)
- Layered synth pad bright airy crystalline
- Future-bass chord stabs pitched vocal-style
- Sub-bass 808 with subtle pitch glide

**Modern Pop (Cirkut / Antonoff era)**:
- Warm analog-modeled synth (modern polish)
- Retro 80s synth revival with modern clarity
- Layered synth pads cinematic texture

**Hyperpop / Digicore**:
- Glitchy stuttered synth chops
- Pitched-up vocal sample chord stabs
- Clipping intentional distortion creative
- Extreme sidechain 95% pump

**Bedroom Pop / Lo-fi**:
- Warm fuzzy synth pad lo-fi character
- Detuned synth ±12 cents organic imperfection
- Vintage synth recorded through cassette

---

## SECTION 3. DRUM ARTICULATION

### 3.1 Kick (킥) 디자인

#### 어쿠스틱 킥
- **Tight Pop Kick**: 60-100Hz fundamental, 5kHz click
- **Roomy Live Kick**: Natural ambience
- **Boom Kick**: 80Hz body 강조
- **Punch Kick**: Transient 강조

#### 일렉트로닉 킥
- **TR-808 Kick**: Sustained sub-bass pitched
- **TR-909 Kick**: Punchy techno, 60Hz attack
- **Trap 808**: Sustained pitched bass kick
- **EDM Big-Room Kick**: Crushed loudness, sidechain pump
- **Drill Sliding 808**: Pitched glide between roots

#### 시대별 킥 결
- **70s Funk**: Live kick, 100Hz body, dry
- **80s Pop**: Gated reverb kick massive
- **90s Hip-Hop**: MPC sample kick lo-fi
- **2000s**: Polished pop kick layered
- **2010s EDM**: Crushed big-room four-on-floor
- **2020s K-pop**: Layered punch + sub clarity

### 3.2 Snare (스네어) 디자인

#### 어쿠스틱 스네어
- **Crisp Snare**: 200-300Hz body, 5kHz crack
- **Brushed Snare**: Subtle texture, jazz
- **Rim Click**: Cross-stick, 보사노바 / 인디
- **Backbeat Snare**: 2 and 4, 록 / 팝 표준

#### 일렉트로닉 스네어
- **Trap Snare**: 강한 펀치, beat 3 only (half-time feel)
- **Drill Snare**: Sharp crack, beat 3
- **EDM Snare**: Layered sample + designed
- **Clap Stack**: Snare 대신 clap layered
- **Ghost Note Snare**: 16th 그리드 quiet velocity

#### 처리법
- **Layered Snare**: 어쿠스틱 + 샘플 + transient designer
- **Plate Reverb**: 1.5초 decay 빈티지
- **Gated Reverb**: 80s 시그니처
- **Compression**: NY-style parallel

### 3.3 Hi-Hat (하이햇) 디자인

#### 어쿠스틱 하이햇
- **Closed Hi-Hat**: 8th note 표준
- **Open Hi-Hat**: Off-beat (and-of-beat)
- **Foot Hi-Hat**: 발로 닫기, 재즈 스윙
- **Ride Cymbal**: Ding-da-ding swing pattern

#### 일렉트로닉 하이햇
- **Trap Hi-Hat**: 16th 트리플렛 + 32nd skitter
- **Drill Hi-Hat**: Off-grid 16th + 트리플렛 rolls
- **House Hi-Hat**: Off-beat opening
- **Shuffled Hi-Hat**: Swung feel hip-hop

#### 모던 트랩/드릴 어법
- 트리플렛 rolls (3:2 polyrhythm)
- 32nd skitters in transitions
- Pitch automation (rising rolls)
- Reverb tail on opening hat

### 3.4 Percussion Layer

#### Latin Percussion (주의: §3.7 anti-trigger 참조)
- **Conga**: Hand drum, deep tone
- **Bongo**: 작은 hand drum, high tone
- **Timbales**: Metal-rim drums
- **Cowbell**: 80s rock 시그니처
- **Clave**: 3-2 son pattern
- **Güiro**: Scraping percussion

#### Universal Percussion
- **Shaker**: 16th grid filling
- **Tambourine**: Backbeat layer
- **Woodblock**: Crisp accent
- **Hand Claps**: Doubled with snare
- **Finger Snaps**: Modern pop top layer

#### Specialized Percussion
- **Log Drum**: Amapiano signature pitched bass
- **Tabla**: Indian classical
- **Djembe**: African
- **Taiko**: Japanese 큰 북
- **Hand Pan**: Steel tongue drum

### 3.5 시대별 드럼 결

#### 1970s
- Loose live drums, natural dynamics
- Dry 70s soul drums
- Vintage warm analog room

#### 1980s
- LinnDrum / Roland TR-707 programmed
- Gated reverb snare massive
- DX7 drum samples digital crisp
- Simmons electronic toms

#### 1990s
- MPC-sampled boom-bap shuffled
- Breakbeat amen break chopped
- Grunge live roomy raw
- Trip-hop dusty drum break vinyl

#### 2000s-2010s
- Polished pop tight compressed
- EDM big-room crushed
- Trap 808 + triplet hats
- Dubstep half-time heavy

#### 2020s
- Modern pop layered punch + clarity
- Afrobeats clave-derived 3-2 son
- Amapiano log drum + deep house kick
- Drill sliding 808 + snare beat 3
- Hyperpop clipping kick + accelerated hats

### 3.6 모던 드럼 트릭 (2024-2026)

#### Layered Drums (모던 표준)
모든 메인 드럼 element를 3-4 레이어로 stack:
- **Kick**: 808 sub + acoustic body + click attack
- **Snare**: 어쿠스틱 + 샘플 + transient designer
- **Hi-hat**: Closed 정밀 + open 텍스처
- **Clap**: 프로그램 + recorded crowd hand claps

#### Dynamic Processing
- Transient designer +3dB punch
- Parallel compression NY-style
- Saturation on drum bus glue
- Sidechain pumping breathing
- Micro-groove humanization 80% quantize

#### Spatial Drum Processing
- Drum room mic ambient natural
- Close-mic drums tight modern
- Plate reverb on snare 1.5s
- Drum bus reverb subtle 8% wet
- Stereo overheads wide L/R

### 3.7 Anti-Pattern: Latin Percussion Trigger

**Case 19 검증된 함정**:

모던 b-boy 사운드 추구하면서 conga / bongo / cowbell /
clave 박으면 자메이카 댄스홀 / Afrobeat / Caribbean 색채로
빠짐.

**원인**: Suno 학습 분포에서 이 악기들이 Latin / Caribbean
클러스터에 강하게 묶여 있음.

**처방**:
- 모던 b-boy 추구 시 Latin percussion 명시 회피
- EXCLUDE 필수: "conga, bongo, cowbell, clave, Latin
  percussion, reggae, dancehall, Afrobeat, Caribbean rhythm"
- "Apache-style break loop" 키워드도 같은 트리거
- 대신 "modern punchy chopped breakbeat" 사용

옛날 b-boy 정통 어법 ≠ 모던 b-boy 사운드. 두 결 명확히 분리.

---

## SECTION 4. BASS ARTICULATION

### 4.1 일렉트릭 베이스 주법

#### Fingerstyle
- **Pluck**: 검지 + 중지 alternating
- **Walking Bass**: Quarter-note 진행 (jazz)
- **Melodic Bass**: 멜로디 라인 보조

#### Slap Bass
- **Slap**: 엄지로 줄 때림 (low strings)
- **Pop**: 검지로 줄 끌어올림 (high strings)
- **Hammer-on / Pull-off**: Funk fills
- **Larry Graham / Marcus Miller**: 슬랩 정통

#### Pick (피크 사용)
- **Down picking**: 펑크 / 록 시그니처
- **Alternate picking**: 메탈 / 모던 록
- **Tight rhythmic**: Punk, hardcore

#### Specialized
- **Fretless Bass**: Pitch slide 가능, 재즈/네오소울
- **Tapping**: Two-handed bass tapping
- **Chordal Bass**: 화음 연주 (modern jazz)

### 4.2 베이스 톤 / 처리법

```
"upright bass walking quarters jazz acoustic"
"fretless bass smooth glide R&B neo-soul"
"slap bass funk syncopated"
"pick bass tight rhythmic punk-rock"
"sub bass mono 20-80Hz round warm"
"distorted bass aggressive drive"
"bass with chorus modulation 80s wide"
```

### 4.3 시대별 / 장르별 베이스

| 시대/장르 | 베이스 캐릭터 |
|----------|-------------|
| Jazz | Upright walking, fingerstyle |
| Motown | James Jamerson fingerstyle melodic |
| Funk | Slap bass syncopated |
| Disco | Octave bass driving |
| Punk | Pick down-picking aggressive |
| Reggae | Heavy melodic syncopated dub |
| Hip-Hop 90s | MPC-sampled boom-bap bass |
| Trap | 808 sustained sub-bass |
| Drill | Sliding 808 dn-dn-dn |
| K-pop modern | Sub-bass 808 + subtle slide |
| Neo-soul | Fretless smooth melodic |
| Modern indie | Pick bass clean rhythmic |

---

## SECTION 5. KEYBOARD ARTICULATION

### 5.1 어쿠스틱 피아노

#### 주법
- **Block Chords**: Hands together rhythmic chords
- **Stride Piano**: Left hand bass-chord-bass-chord
- **Comping**: Jazz rhythm chord support
- **Arpeggiation**: 화음 분산 연주
- **Ornamentation**: Trills, grace notes

#### 톤 / 처리
```
"grand piano warm vintage tube"
"upright piano intimate close-mic"
"prepared piano experimental dampened"
"jazz piano comping rootless voicings"
"classical piano expressive dynamic"
```

### 5.2 일렉트릭 피아노

#### Rhodes
- **Warm Tine**: 둥근 따뜻함
- **Chorus Effect**: 70s 시그니처 워블
- **Tremolo**: Stereo amplitude modulation

#### Wurlitzer
- **Bark**: 강한 어택
- **Bite**: Distortion-friendly
- Soul / Motown 시그니처

#### Clavinet
- **Funk Clav**: Stevie Wonder "Superstition"
- **Wah envelope**: 자동 wah filter
- 70s funk

#### CP-70
- **Yamaha CP-70**: 80s pop / soft rock
- **Bright tine**: 어쿠스틱 + electric hybrid

### 5.3 오르간

#### Hammond B3
- **Drawbars**: 9개 슬라이더 harmonic balance
- **Leslie Speaker**: Rotating 스피커 chorus
- **Percussion**: 어택 색채 추가
- Gospel / soul / blues / jazz 표준

#### Vox Continental / Farfisa
- **60s rock organ**: Bright 톤
- **Doors / Animals 시그니처**

#### Pipe Organ
- **Church organ**: Massive sustained
- Cinematic / classical

### 5.4 신스 키보드 (§2와 별개)

이 카테고리는 §2 신스 articulation 참조.

---

## SECTION 6. ORCHESTRAL & CINEMATIC

### 6.1 String Section

#### 주법
- **Arco**: Bow 사용 sustained
- **Pizzicato**: 손가락으로 plucking
- **Spiccato**: Bouncing bow 짧은 reset
- **Staccato**: 짧고 detached
- **Legato**: 연결된 smooth
- **Tremolo**: 빠른 bow 반복
- **Sul ponticello**: Bridge 가까이 (메탈릭)
- **Sul tasto**: Fingerboard 위 (소프트)
- **Col legno**: Bow 나무로 때림 (percussive)

#### Suno 어법
```
"sweeping orchestral strings legato sustained"
"pizzicato strings 16th note staccato"
"tremolo strings tense suspenseful"
"string section spiccato bouncing"
"violin solo expressive vibrato"
```

### 6.2 Brass

#### 주법
- **Stab**: 짧은 punch
- **Sustained**: 긴 음
- **Glissando**: 슬라이드
- **Mute**: Wah / harmon / cup mute
- **Growl**: 거친 톤 (jazz)
- **Doits**: 짧은 상승 슬라이드
- **Falls**: 짧은 하강 슬라이드

```
"brass section stabs syncopated punch"
"muted trumpet jazz cool"
"trombone glissando comedic"
"horn section sustained chord pad"
"sax solo expressive growl"
```

### 6.3 Woodwind

- **Flute**: Airy, melodic, classical
- **Bansuri / Shakuhachi**: Asian traditional
- **Clarinet**: Warm, woody, jazz
- **Oboe**: Penetrating, melancholic
- **Bassoon**: Deep, comedic potential

### 6.4 Percussion (Orchestral)

- **Timpani**: Tuned drums, dramatic
- **Snare Drum**: Military / orchestral
- **Cymbals**: Crash, suspended swell
- **Triangle**: Subtle accent
- **Gong / Tam-tam**: Massive resonance
- **Glockenspiel / Celesta**: Bell-like high

### 6.4b Mallet Percussion — 4종 구분 (Case 40 정립)

말렛 타악기 4종은 Suno에서 한 끗 차이로 갈리므로 정확히
구분해 지시. 무드 정합성이 키워드 선택을 좌우.

- **Vibraphone (비브라폰)**: 금속 바 + 모터 트레몰로. 긴
  잔향이 공기 중에 떠돎. 차가움·도시·멜랑콜리. 한낮 공기
  떨림, 네오 시티팝 시그니처에 정합.
  키워드: "vibraphone soft mallet motor tremolo metallic warm,
  long decay tail floating"
- **Marimba (마림바)**: 나무 바. 둥글고 짧은 잔향, 따뜻함.
  시골·온기. 키워드: "marimba warm wooden round, short decay"
  주의 — "Latin warm" 붙이면 라틴 그루브로 끌림. 무드곡에선
  EXCLUDE 처리.
- **Xylophone (실로폰)**: 나무/합성 바. 잔향 거의 없음 —
  톡 끊김. 단호·건조. 매미 그친 직후 적막 묘사 등.
  키워드: "xylophone dry hard mallet, no sustain"
- **Glockenspiel (글로켄슈필)**: 금속 바. 높고 쨍한 종소리.
  장난감 톤. 키워드: "glockenspiel toy bell bright"

요약축: 비브라폰=쇠·차가움·도시 / 마림바=나무·따뜻함·시골
/ 실로폰=잔향없음·단호·건조 / 글로켄=쇠·장난감·높음.
재질(쇠/나무)과 잔향(있음/없음) 2축으로 기억.

### 6.5 Cinematic Modern Tricks

```
"hybrid orchestral electronic Hans Zimmer-style"
"massive brass swells with sub-bass support"
"cinematic strings with electronic drone underneath"
"taiko drums + orchestra modern epic"
"vocal choir + synthetic pad layered"
```

---

## SECTION 7. WORLD / ETHNIC INSTRUMENTS

### 7.1 Korean Traditional (Gugak)

#### 현악기
- **Gayageum (가야금)**: 12-string zither, 손가락 plucking
- **Geomungo (거문고)**: 6-string zither, stick plucking
- **Haegeum (해금)**: 2-string fiddle

#### 관악기
- **Daegeum (대금)**: Large bamboo flute
- **Piri (피리)**: Reed instrument

#### 타악기
- **Janggu (장구)**: Hourglass drum
- **Buk (북)**: Barrel drum
- **Ggwaenggwari (꽹과리)**: Small gong

```
"Korean traditional gugak gayageum plucking"
"haegeum melodic line traditional Korean"
"janggu rhythm pattern jangdan"
```

### 7.2 Japanese Traditional

- **Koto**: 13-string zither
- **Shamisen**: 3-string lute
- **Shakuhachi**: Bamboo flute
- **Taiko**: Drums (various sizes)

### 7.3 Indian Classical

- **Sitar**: Long-necked lute, drone strings
- **Tabla**: Pair of hand drums
- **Tanpura**: Drone string instrument
- **Bansuri**: Bamboo flute
- **Sarangi**: Bowed string

### 7.4 Middle Eastern

- **Oud**: Short-necked lute
- **Qanun**: Box zither
- **Ney**: End-blown flute
- **Darbuka**: Goblet drum

### 7.5 African

- **Djembe**: Hand drum
- **Kora**: 21-string harp-lute
- **Talking Drum**: Pitch-modulating
- **Mbira**: Thumb piano

### 7.6 Latin

- **Cuatro**: Small 4-string guitar
- **Tres**: Cuban 3-pair guitar
- **Charango**: Andean small lute
- **Pandeiro**: Brazilian frame drum

### 7.7 Suno 어법 (World Instruments)

```
"Korean gugak gayageum plucking traditional ornamental"
"Japanese koto melodic line meditative"
"Indian sitar drone with raga melody"
"Middle Eastern oud taqsim improvisation"
"African djembe polyrhythmic ensemble"
"Latin cuatro strumming bossa rhythm"
```

**주의**: World instrument 사용 시 학습 데이터 한계로
근사 결과 발생 가능. "in the spirit of" 형식 권장:

```
"in the spirit of Korean traditional gugak,
modal melodic ornamentation,
gayageum-influenced plucking texture"
```

---

## SECTION 8. 시대별 사운드 결 종합

### 8.1 시대성 결정 요인

곡의 시대성은 다음 요소들의 종합:

1. **악기 선택** (어떤 악기를 쓰는가)
2. **주법** (어떻게 연주하는가)
3. **톤 / 처리** (사운드 캐릭터)
4. **믹스 / 마스터링** (다이내믹 + 라우드니스)
5. **편곡 밀도** (몇 개 악기 동시 사용)
6. **보컬 처리** (auto-tune, compression 등)

### 8.2 시대별 종합 결 (악기 articulation 중심)

#### 1970s
- **Drums**: Live, dry, natural ambience
- **Bass**: Fingerstyle, melodic, prominent in mix
- **Guitar**: Tube amp warm, light overdrive
- **Keys**: Rhodes, Wurlitzer, Hammond B3
- **Synth**: Moog mono lead, ARP pads
- **Vocals**: Natural, minimal compression
- **Mix**: Wide stereo, open dynamics

#### 1980s
- **Drums**: LinnDrum / programmed, gated reverb snare
- **Bass**: Slap bass funk OR synth bass
- **Guitar**: Chorus modulation, clean clean digital amp
- **Keys**: DX7 FM e-piano, Yamaha CS-80
- **Synth**: Juno, Jupiter analog poly
- **Vocals**: Big reverb, heavy compression
- **Mix**: Big room reverb, gated everything

#### 1990s
- **Drums**: MPC sampled boom-bap, breakbeats, grunge live
- **Bass**: Pick bass punk, sub-bass hip-hop
- **Guitar**: Big Muff fuzz, grunge distortion
- **Keys**: Korg M1 preset, organ revival
- **Synth**: Roland JD-800, early VA
- **Vocals**: Lo-fi indie OR polished pop
- **Mix**: Loudness war start, more aggressive

#### 2000s
- **Drums**: Polished pop tight compressed, programmed
- **Bass**: Sub-bass dominant, sidechain duck
- **Guitar**: Pop-punk distortion, indie clean
- **Keys**: Vintage revival, virtual instruments
- **Synth**: Massive, Sylenth1 EDM presets
- **Vocals**: Auto-tune mainstream adoption
- **Mix**: Loudness war peak, crushed

#### 2010s
- **Drums**: Trap 808 + triplet hats, EDM big-room
- **Bass**: 808 sustained, sliding bass drill
- **Guitar**: Indie reverb-soaked, jangly clean
- **Keys**: Lo-fi hip-hop revival
- **Synth**: Serum wavetable, future bass
- **Vocals**: Heavy auto-tune T-Pain era
- **Mix**: Streaming-loudness adapted

#### 2020s
- **Drums**: Layered (3-4 layers), modern punch + clarity
- **Bass**: Sub-bass + slide, layered
- **Guitar**: Modern clean bright, precise reverb
- **Keys**: Hybrid acoustic/electric warm
- **Synth**: Vital wavetable, hybrid synthesis
- **Vocals**: Natural human texture, organic
- **Mix**: Dynamic restored, controlled loudness

### 8.3 의도된 시대성 vs 의도하지 않은 시대성

**의도된 시대성**: 명확히 era anchor 명시
- "1985-1988 LA studio synth-funk"
- "early-1990s Tokyo city-pop revival"

**의도하지 않은 시대성** (피해야 함):
- Vague era word ("vintage", "retro") → Suno 디폴트 평균
- Era anchor 없음 → 학습 데이터 평균값 (보통 2010s)
- 충돌하는 era 키워드 ("modern" + "vintage tape" + "8-bit")

**처방**: COVER Style Box 첫 200자 안에 구체 era anchor 의무

---

## SECTION 9. "올드한 사운드" 트러블슈팅

회의록 직격: "최근 프로듀서들이나 음악 스튜디오들이 어떤
것들은 어떻게 해서 사운드를 구현하는지도 조사하고 보완해야할게
많아. 사운드가 계속 올드한게 나오면 안되니까."

### 9.1 "올드함" 진단

**Symptom A: 보컬이 90s/2000s 같음**
- 원인: Auto-tune T-Pain era 트리거 키워드 잔존
- 처방:
  - Style Box: "natural human breath, organic phrasing,
    no auto-tune residue, modern controlled subtle correction"
  - Exclude: "auto-tune T-Pain heavy, vocoder, robotic vocal"

**Symptom B: 신스가 80s 같음 (의도 아닌데)**
- 원인: "synth pad", "analog warmth" 같은 일반 키워드만 사용
- 처방: 모던 신스 명시
  - "Vital wavetable modern pluck"
  - "modern crystalline synth pad bright airy"
  - "polished modern synth lead, no vintage warmth"
  - Exclude: "DX7", "Juno-style", "vintage analog warmth"

**Symptom C: 드럼이 boom-bap 90s 같음**
- 원인: "drums" 일반 명시 → 학습 평균이 boom-bap
- 처방: 모던 드럼 명시
  - "modern layered drums: 808 sub + acoustic body + click"
  - "2020s K-pop drums punchy bright crisp"
  - "transient designer +3dB punch modern"

**Symptom D: 기타가 indie 2010s reverb-soaked 같음**
- 원인: "reverb" 사용으로 indie 2010s 디폴트
- 처방: 모던 기타 명시
  - "modern bright clean Telecaster precise reverb"
  - "tight modern guitar production no vintage warmth"
  - "2024-2026 modern pop guitar clarity"

**Symptom E: 믹스가 loudness war 2000s 같음**
- 원인: "polished", "loud" 키워드 → 2000s 트리거
- 처방: 모던 믹스 명시
  - "modern controlled loudness -10 LUFS streaming"
  - "open dynamics, transient preservation,
    no aggressive limiting"

### 9.2 모던 사운드 강제 키워드 묶음

**Style Box 첫 200자에 의무 포함**:
```
"2024-2026 modern production polish"
"contemporary cutting-edge sound design"
"polished modern with organic warmth"
"current era streaming-optimized mix"
```

**Exclude 의무 묶음**:
```
"vintage tape hiss, 80s gated reverb, 90s boom-bap drums,
2000s loudness war master, 2010s heavy auto-tune,
generic dated production"
```

### 9.3 모던 vs 빈티지 의도적 사용

빈티지 결을 의도적으로 추구할 때 (Lo-fi, retro pop 등):

**올바른 빈티지 어법**:
```
"deliberate 1985-1988 LA synth-funk era,
DX7 FM e-piano + Juno pad analog warmth,
gated reverb snare massive 80s,
LinnDrum programmed pattern,
intentional vintage character"
```

핵심: **"deliberate" / "intentional" / 구체 시대 명시**.
"vintage" 단독 키워드는 Suno 평균값으로 흐려짐.

### 9.4 시대성 디버깅 체크리스트

곡 출력 후 시대성 검증:
- [ ] Era anchor 첫 200자 안에 구체 명시?
  ("modern 2024-2026" / "late-2010s" / "1985-1988 LA")
- [ ] 악기별 시대 일치? (의도 외 mix-era 없음?)
- [ ] 보컬 처리가 시대에 맞음?
- [ ] 믹스 라우드니스가 시대에 맞음?
  (모던 -10 LUFS / 빈티지 -14 LUFS)
- [ ] Anti-drift Exclude에 시대 트리거 차단?

---

## SECTION 10. 악기 활용 의사결정 워크플로우

새 곡 작업 시 악기 hierarchy 결정 절차:

### Step 1: 컨셉 → Foundation 선택
컨셉의 emotional 코어에 맞는 foundation instrument 1-2개:
- 친밀 / 인디 → 어쿠스틱 기타 + 보컬
- 댄스 / 클럽 → 808 / kick + 베이스 신스
- 시네마틱 → 오케스트라 strings + 피아노
- 모던 K-pop → 808 + plucky synth + bright pad

### Step 2: Foundation에 Color 추가
1-2개 색채 악기로 정체성 강화:
- Telecaster (K-indie) / Rhodes (R&B) / sitar (East Asian fusion)

### Step 3: Texture / Atmosphere
- Pad / strings / reverb tail
- 빈 frequency 채우기

### Step 4: Rhythm / Percussion 결정
- Foundation drum kit + percussion layers
- 시대성 매칭 검증

### Step 5: Lead / Hook 악기
- 보컬 외 lead 멜로디 담당 (signature instrument)

### Step 6: 주법 결정
각 악기의 주법을 §1-§7에서 픽업

### Step 7: 시대성 검증
§8 시대별 결 매트릭스로 일관성 확인

### Step 8: Style Box 어법 변환
15 파일 §14-§16 어법으로 변환

### Step 9: 출력 후 §9 트러블슈팅 적용

---

## SECTION 11. 관련 파일

- `05_GENRE_LIBRARY.md` — 장르별 정통 악기 어법
- `11_PRODUCTION_DESIGN.md` — 믹스 / 주파수 / 다이내믹 설계
- `15_NATURAL_LANGUAGE_DIRECTION.md` — Suno 어법 변환
  특히 §14 (synth) §15 (drums) §16 (guitar)
- `06_VOCAL_PRODUCTION.md` — 보컬 디렉티브
- `99_PERSONAL_OPTIONAL.md` — 검증된 케이스별 악기 활용

---
---

## SECTION 17 — EFFECTS PROCESSING BANK (NEW v2.3 / 2026-XX)

### 17.0 이 섹션이 다루는 것

회의록 트리거: "이펙터 같은 지식을 얻었거든. 이걸 Suno에
자연스럽게 프롬프트화해야 하는데."

5계열 이펙터 + 각 계열의 작동 원리 + Suno 어법 + CREATE/COVER
분배 의사결정. 15 §19 (Suno 어법 라이브러리)와 짝.

15 = "어떻게 박는가" (키워드 라이브러리)
16 §17 = "왜·언제·어디 박는가" (의사결정)

### 17.1 5대 이펙터 계열 개요

| 계열 | 작동 원리 | 청각 효과 | 주 사용 위치 |
|------|----------|----------|------------|
| Modulation | LFO로 신호 주기적 변조 | 떨림·확산·휩쓸림 | 악기 톤 정체성 |
| Time-based | 시간 지연으로 공간감 생성 | 잔향·반복·깊이 | 공간 설계 |
| Dynamics | 볼륨·트랜지언트 제어 | 펀치·밀도·글루 | 모던 사운드 코어 |
| Distortion | 신호 비선형 왜곡 | 따뜻함·거침·공격성 | 록·일렉트로닉 캐릭터 |
| Spatial | 스테레오 이미지 조작 | 넓이·위치·깊이 | 믹스 아키텍처 |

### 17.2 Modulation 5종 (회의록 직격)

#### Vibrato
- **원리**: LFO가 피치를 주기적 변조 (보통 4-7Hz)
- **효과**: 음정 미세 떨림 (자연 보컬 비브라토)
- **악기 매칭**: 보컬 (디폴트), 기타 솔로, 스트링, 신스 리드
- **시대성**: 시대 무관, 강도가 시대성 결정
  - Wide slow: 클래식 / 가스펠 / K-trot
  - Subtle: 모던 팝 (디폴트)
  - No vibrato: 인디 / 모던 K-pop

#### Tremolo
- **원리**: LFO가 볼륨을 주기적 변조
- **효과**: 음정 고정, 볼륨 끊김 (리듬감)
- **악기 매칭**: 일렉트릭 기타 (Surf rock), Wurlitzer, 빈티지 일렉피아노
- **시대성**: 60s 서프 / 70s 소울 / 90s 트립합 부활
- **주의**: Vibrato와 헷갈리지 말 것 (피치 vs 볼륨)

#### Chorus (이펙터)
- **원리**: 15-30ms 지연 + 미세 변조 신호 + 원본 믹스
- **효과**: 한 명이 여러 명처럼, 두툼한 확산감
- **악기 매칭**: 80s 클린 기타, Juno 패드, Rhodes
- **시대성**: 80s synth-pop 시그니처, 모던 indie 부활
- **충돌 주의**: 곡 구조 [Chorus](후렴)와 이름 충돌
  → Style Box에 자연어로 박거나
  → Lyrics Box는 `[Chorus effect on guitar]` 식으로 명시

#### Phaser
- **원리**: 올패스 필터로 위상 어긋난 신호 + 원본 믹스
- **효과**: 쉬익~ 휩쓸리는 우주적 느낌
- **악기 매칭**: 70s 펑크 기타, 사이키델릭, 재즈 일렉피아노
- **시대성**: 70s 펑크/소울 / 90s G-funk / 모던 네오소울

#### Flanger
- **원리**: 1-10ms 짧은 지연 + 변조 신호 + 원본 믹스
- **효과**: 제트기 스월, 더 격렬한 휩쓸림
- **악기 매칭**: 록 기타 솔로, 드럼 필, 트랜지션
- **시대성**: 70s 사이키 / 80s 록 / 모던 트랩 트랜지션

#### Bonus: Rotary Speaker (Leslie)
- **원리**: 회전 스피커로 자연스러운 doppler + 변조
- **효과**: Hammond B3의 시그니처 회전감
- **악기 매칭**: Hammond 오르간 (필수), Rhodes (변형)
- **시대성**: 60s-70s 소울/가스펠/재즈 / 모던 부활

### 17.3 Time-based 계열 (Reverb / Delay)

#### Reverb 종류별 결
| 종류 | 캐릭터 | 사용 |
|------|--------|------|
| Plate | 메탈릭 빈티지, 스무스 | 빈티지 팝/소울/재즈 보컬 |
| Hall | 자연 큰 공간, 길고 넓음 | 발라드 / 시네마틱 / 클래식 |
| Room | 친밀 작은 공간 | 인디 / 어쿠스틱 / 모던 팝 |
| Spring | 빈티지 메탈릭 스프링 | Surf / 더브 / 빈티지 컨트리 |
| Shimmer | 옥타브-up + 리버브 | 드림 팝 / 앰비언트 / 시네마 |
| Gated | 80s 시그니처 (리버브 + 게이트) | 80s 록 / 신스팝 / 모던 부활 |

#### Delay 종류별 결
| 종류 | 캐릭터 | 사용 |
|------|--------|------|
| Slap-back | 80-150ms 단일 에코 | 로커빌리 / 빈티지 록 |
| Tape Echo | 아날로그 wow/flutter | 더브 / 사이키 / 빈티지 |
| Ping-Pong | L/R 교차 | 모던 팝 / EDM / 댄스 |
| 1/8 Dotted | 점8분음표 리듬 동기화 | EDM / Future bass / 디스코 |
| Reverse | 역재생 | 드림팝 / 트랜지션 / 시네마 |

### 17.4 Dynamics 계열 (모던 사운드 핵심)

#### Compression 종류
- **Tight Pop Compression**: 모던 팝 디폴트, 보컬·드럼 forward
- **Parallel (NY-style)**: 다이내믹 보존하면서 펀치 추가
- **Bus Glue Compression**: 트랙 전체 cohesion (마스터 단계)
- **Sidechain Compression**: 킥에 베이스/패드 ducking (EDM/모던 팝)
- **Tube Saturation**: 따뜻한 하모닉 디스토션 (보컬 버스 디폴트)

#### Transient Designer
- **원리**: 어택과 서스테인 분리 제어
- **효과**: 드럼 펀치 강조 (+3dB attack), 또는 룸 죽이기
- **모던 표준**: K-pop 5세대 / 모던 팝 드럼 처리에 거의 필수

#### Limiting / Loudness
- **현대 기준**: -8 ~ -10 LUFS (스트리밍 평준화)
- **시네마틱**: -14 ~ -16 LUFS (다이내믹 보존)
- **클럽/EDM**: -7 ~ -8 LUFS (압축 한계)

### 17.5 Distortion / Saturation 계열

| 종류 | 캐릭터 | 사용 |
|------|--------|------|
| Tape Saturation | 따뜻한 빈티지 warmth | 보컬 버스 / 마스터 (디폴트) |
| Tube Saturation | 따뜻한 하모닉 distortion | 보컬 / 기타 / 마스터 |
| Overdrive | 부드러운 클리핑 | 록 기타 / 블루스 |
| Distortion | 강한 클리핑 | 메탈 / 펑크 / 모던 록 |
| Fuzz | 거친 빈티지 distortion | 60s 사이키 / 그런지 |
| Bit-Crusher | 8/16비트 lo-fi | 하이퍼팝 / 칩튠 / 글리치 |
| Wave-Shaper | 공격적 하모닉 | 모던 일렉트로닉 |

### 17.6 Spatial 계열

- **Pan**: L/R 위치 (각도 단위 또는 % 단위)
- **Stereo Width**: 좌우 펼침 (60-100%)
- **Mid-Side Processing**: 중심/사이드 분리 처리
- **Haas Effect**: 짧은 지연으로 가짜 스테레오
- **3D Depth**: front-to-back 깊이감

---

## SECTION 18 — CREATE/COVER 마스터 분배 결정 트리

### 18.1 핵심 질문

오빠가 자주 흔들리는 지점: 이 디테일이 CREATE에 들어가야 하나,
COVER에 들어가야 하나.

답: **곡의 bone(정체성)을 결정하는가?** 결정하면 CREATE.
                                    안 하면 COVER.

### 18.2 6단계 결정 트리

이 디테일이...
악기의 시그니처 톤을 결정하는가? 예: "Chorus Rhodes" / "Tremolo guitar" / "Distorted bass" → 같은 곡을 다른 톤으로 만들면 다른 곡이 되는가? → YES → CREATE에 악기와 함께 박기 → NO → 4번으로

시대성/장르 정체성을 결정하는가? 예: 80s synth-pop의 chorus 보컬 / 70s funk의 phaser 기타 / 모던 K-pop의 808 sub → 시대 anchor와 결합되어야 의미 있는가? → YES → CREATE에 박기 → NO → 4번으로

화성/멜로디 작법에 영향을 주는가? 예: Bridge에 phaser 진입 = 시그니처 모먼트 / 코러스 진입에 reverse cymbal swell → Signature Moment로 캡처 가능한가? → YES → CREATE Signature Moments + COVER 처리법 동시 → NO → 4번으로

트랜지션·연출용인가? 예: 드럼 필 flanger / 보컬 throw delay / 섹션 간 silence → COVER 전용

주파수·공간·다이내믹 처리인가? 예: Plate reverb / pan position / sidechain pump / parallel compression / EQ tilt → COVER 전용

모던 팝 디폴트 처리인가? 예: Tube saturation / +1.5dB air shelf / vocal corridor / -10 LUFS streaming target → COVER (99_OPERATOR_VAULT Part F Suno-hacking 디폴트 묶음)


### 18.3 흔한 실수 패턴

**실수 A: CREATE에 reverb·EQ·compression 박기**
- 증상: CREATE Style Box 800자 초과, COVER와 거의 같음
- 원인: 텍스처 정보가 CREATE로 흘러 들어감
- 처방: 30% Rule (09 §3.5b) 발동 → CREATE 재작성

**실수 B: COVER에 코드 진행·BPM·키 다시 박기**
- 증상: COVER 950자 초과, 정보 중복
- 원인: COVER가 "또 다른 CREATE"가 됨
- 처방: COVER는 CREATE의 bone 보존 + 텍스처만

**실수 C: 시그니처 모먼트가 CREATE에만 있고 COVER에 없음**
- 증상: 첫 generation은 좋은데 COVER 후 모먼트 사라짐
- 원인: COVER에 "preserve [moment] from CREATE" 명시 안 됨
- 처방: COVER에 보존 명령 추가

**실수 D: 모던 디폴트 묶음을 매번 풀로 박기**
- 증상: COVER 항상 950자 한계
- 원인: 99_OPERATOR_VAULT Part F 표준 처방을 약어처럼 안 씀
- 처방: 99_OPERATOR_VAULT Part F 묶음 활용 + 곡별 특수 처방만 추가

### 18.4 분배 검증 체크리스트 (출력 직전)

- [ ] CREATE Style Box Dense 700-950자 안인가? (sketch면 Tight 250-350 / 638 부실 아닌가)
- [ ] COVER Style Box Dense 700-950자 안인가? (≤950 안전)
- [ ] CREATE에 production/mix/atmosphere 언어 0%인가?
- [ ] CREATE/COVER 디스크립터 30% 이상 겹치지 않는가?
- [ ] Signature Moments가 CREATE + COVER 양쪽에 명시됐는가?
  (CREATE = 멜로디 반영, COVER = 텍스처 처리)
- [ ] 모던 디폴트(99_OPERATOR_VAULT Part F)는 COVER에만 있는가?
- [ ] 이펙터별 분배가 결정 트리(§18.2)와 일치하는가?


## VERSION

v1.0 (2026-05-09) — 회의록 트리거로 신규 파일 생성.
악기 주법 종합 + 시대별 결 + 장르별 어법 + 트러블슈팅
정리. 16번 슬롯 점유.

---

<!-- USER EXTENSION ZONE — append additional articulation
     techniques, modern producer instrument tricks below -->



---

## SECTION 19. ANTI-SAWTOOTH VOCABULARY (NEW v2.7 / External Research)

### §19.1 The sawtooth problem

External research (Suno Field Guide / community testing): Suno
defaults to *sawtooth-heavy* synth sounds when "synth" or "synthesizer"
is mentioned. This creates *generic-sounding* electronic textures.

Operator symptom: "synth sounds generic / cheap / 80s preset."

### §19.2 Anti-sawtooth vocabulary substitutes

Replace generic synth language with *specific waveform / synth-type*
language:

| Generic | Specific |
|---|---|
| "synth" | "supersaw with 7-voice unison" / "FM sine bell" / "wavetable pad" |
| "lead synth" | "Moog Subsequent 37 lead" / "Prophet-5 brass" / "DX7 electric piano" |
| "bass synth" | "Roland TB-303 acid bass" / "Sub-37 sine bass" / "Reese bass wavetable" |
| "pad" | "Juno-106 chorused pad" / "OB-X polyphonic strings" / "Eventide H3000 shimmer" |
| "arp" | "PolyKB sequenced arp" / "Korg Volca arp pattern" / "16-step pulse arp" |

### §19.3 Synth-by-genre vocabulary

#### Synthwave / 80s
```
Juno-106 chorused brass, Moog Memorymoog lead, LinnDrum LM-1 kit,
DX7 electric piano with chorus, OBXa polyphonic strings, FM bells
```

#### Hyperpop
```
distorted supersaw, pitch-bent FM lead, crushed wavetable, glitchy
granular pad, vocoded chord stacks, sidechained square bass
```

#### House
```
analog Juno bassline, deep saw pad, white-noise riser, classic 909
hi-hats, sliced vocal chops, sub-bass sine 808
```

#### Trance
```
supersaw 7-voice unison lead, gated trance pad, sidechain-pumping
analog kick, plucked sequence, atmospheric pad swell
```

#### Lo-fi / Bedroom
```
warm Rhodes electric piano, soft Wurlitzer, slightly detuned chorus,
tape-saturated analog warmth, no harsh top end
```

### §19.4 Instrument descriptor menu (C-28.5 requirement)

Every instrument in Style Box must have a descriptor (C-28.5 auto-check).
Descriptor menu:

#### Acoustic instruments
```
fingerpicked nylon-string guitar (intimate)
strummed steel-string acoustic (rhythmic)
brushed snare with rim-click accents (jazz-folk)
upright bass plucked (acoustic / jazz)
plucked harp (delicate)
bowed cello (sustained, emotional)
muted trumpet (mellow, jazz)
breathy alto saxophone (intimate)
```

#### Electric / amplified
```
clean Telecaster with chorus pedal (Mac DeMarco-style)
overdriven Strat with vintage spring reverb (rock)
palm-muted Telecaster behind-beat (funk)
fuzz-pedal SG (garage rock)
clean Rhodes electric piano (warm, jazzy)
Wurlitzer with vibrato (R&B vintage)
Hammond B3 with Leslie cabinet (gospel, rock)
```

#### Drums
```
brushed jazz kit (intimate, soft)
boom-bap 90s hip-hop kit (mid-forward, sample-based)
contemporary trap 808 + tight hats (modern)
4-on-floor sidechained EDM kit (driving)
loose live rock kit with room mic (organic)
LinnDrum LM-1 (80s programmed)
ambient electronic minimal kit (sparse)
```

#### Synths (see §19.3 for genre-specific)

### §19.5 Physical articulation vocabulary

For instruments, *how* they're played matters:

```
gently fingerpicked (soft attack, intimate)
aggressively strummed (rhythmic drive)
muted (dampened, percussive)
sustained (long notes, emotional)
plucked (short, defined attack)
bowed (continuous tone)
hammered (percussive)
slid (glissando, expressive)
choked (cut short, funk)
palm-muted (rhythmic, punk-rock)
ghost notes (rhythmic shadow notes)
```

### §19.6 "Without descriptors" auto-flag

If Style Box mentions an instrument without descriptor:
```
"Rhodes" alone → auto-flag → suggest "dusty Rhodes" / "clean Rhodes"
/ "chorused Rhodes" / "warm Rhodes"
"sax" alone → suggest "breathy alto sax" / "muted tenor sax" /
"bright alto sax"
"guitar" alone → suggest "fingerstyle nylon" / "clean Telecaster" /
"overdriven Strat"
```

System auto-boost: "🔧 §19 Descriptor: [instrument] + [descriptor]
applied."

---

## SECTION 20. HUMANIZATION VOCABULARY (NEW v2.7)

### §20.1 The robotic problem

Suno defaults can sound *programmed / quantized / robotic* — especially
on drums and electronic instruments. Humanization vocabulary
counteracts.

### §20.2 Drum humanization

```
loose timing, behind the beat by 5ms
ghost notes scattered throughout, not quantized
human velocity variation, each hit slightly different
breath of air between hits, not relentlessly tight
slightly drunk shuffle, drag and pull
J Dilla-style timing (offbeat, broken-grid)
```

### §20.3 Vocal humanization

```
natural human breath texture (visible breath before phrases)
slight pitch wobble between sustained notes
imperfect intonation acceptable, not auto-tuned
conversational rhythm, not strict to grid
phrase-end fades natural, not chopped
audible mic technique (proximity effects, head turns)
```

### §20.4 Instrument humanization

```
analog drift on synths, slight detune throughout
acoustic instruments with finger noise audible
amplifier hum present (not totally noise-gated)
string squeaks on guitar slides
room reflection captures performer's space
```

### §20.5 Combined humanization Style Box snippet

```
Production with natural human breath texture on vocal, drums with
behind-the-beat looseness and human velocity variation, slight
analog drift on synths, audible finger noise on acoustic guitar,
room reflection medium capturing performer space, no aggressive
quantization, no robotic perfection.
```

---



## § USER EXTENSION ZONE v2.0 (2026-05-24)

SJY051 instrument-idiom 9개 풀바디 통합.


### §UE-1. 9 Instrument Idiom Library (SJY)

#### §UE-1.1 Piano Idiom

```
Pop: block chords + arpeggios
Jazz: voicings (rootless), comping
Classical: counterpoint, polyphonic
Rhodes: warm chorused, dreamy
Honky-tonk: barrelhouse, ragtime
```

#### §UE-1.2 Guitar Idiom

```
Strumming pattern (Pop): down-down-up-up-down-up
Fingerpicking (Folk): Travis picking, alternating bass
Lead lines (Rock): bends, slides, vibrato
Power chords (Punk/Rock): root + 5th
Palm mute (Metal): tight chugging
Funk: 16th note ghost note muted
Jazz: chord melody, single-line improv
```

#### §UE-1.3 Bass Idiom

```
Walking bass (Jazz): 4-note per bar, root motion
Slap bass (Funk): thumb + pop
Pumping bass (EDM): sidechain to kick
Pedal bass (Rock): root note ostinato
Melodic bass (Indie): countermelody
```

#### §UE-1.4 Drums Idiom

```
Standard pop (4/4): kick 1+3, snare 2+4
Hip-hop: kick 1, 3.5, 4 / snare 2, 4
Trap: half-time snare on 3
Reggaeton: dembow pattern
EDM: four-on-the-floor
Latin: clave (3-2 or 2-3)
Jazz: ride cymbal swing, brush
```

#### §UE-1.5 Strings Idiom

```
Pizzicato: plucked (jazz, light)
Arco: bowed (classical, full)
Tremolo: rapid bowing (suspense, drama)
Sul ponticello: bow near bridge (eerie)
Spiccato: bouncing bow (fast)
```

#### §UE-1.6 Brass Idiom

```
Stabs (Funk / Soul): short accents
Swells: crescendo build
Falls: pitch drop at end
Shake: vibrato style
Mute: harmon mute (jazz), straight mute
```

#### §UE-1.7 Synth Idiom

```
Pad: sustained chord wash
Lead: single-line melodic
Pluck: short staccato
Bass: sub bass, mid bass, growl
Arp: arpeggiated sequence
Stab: short rhythmic
Sweep: filter modulation
Drone: long sustained
```

#### §UE-1.8 Vocal Idiom (06 USER EXTENSION 참조)

#### §UE-1.9 Percussion Idiom

```
Congas: hand drums (Latin)
Bongos: hand drums (Latin, smaller)
Timbales: Latin
Cowbell: Latin / disco
Shaker: subtle rhythm
Tambourine: pop / folk
Cajón: acoustic / unplugged
Djembe: African
Tabla: Indian
Taiko: Japanese
```


### §UE-2. Articulation Tags (Suno 어법)

```
[Sudden Absolute Silence: 1 bar]
[Held Note: 4 bars]
[Pause half bar]
[Pause 1 bar]
[Pause 2 bars]
[Rest]
[Mute]
[Build-up]
[Drop]
[Breakdown]
[Solo: guitar 8 bars]
```


# === END 16 USER EXTENSION ZONE v2.0 ===



