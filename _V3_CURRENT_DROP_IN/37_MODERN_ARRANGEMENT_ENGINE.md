# 37. MODERN ARRANGEMENT ENGINE — 안티-올드 화성·멜로디·악기 (Suno 평균회귀 정조준)
# VERSION: v1.0 (2026-06-15) — 이력은 CHANGELOG.txt
# 근거: 02/03(화성)·04(멜로디)·16(악기)·28(편곡감독 PD)·§10(평균회귀) + 현행 프로덕션 web 검증(2026-06)
# 발동: 새 곡 CREATE 설계 시 / "올드하다·뻔하다·촌스럽다·평범하다·전형적" 피드백 / 28 PD와 함께.
# 핵심: Suno는 확률 엔진이라 *방치하면* 화성=I-V-vi-IV 4코드, 악기=스톡 프리셋, 멜로디=뻔한 아치로 회귀(=올드).
#       막으려면 CREATE Style에 *구체 현대화 어휘*를 박는다. ★Suno는 코드기호(Cmaj7)를 못 읽음 → 전부 *서술형*으로 번역.

## §0. 왜 Suno가 올드해지나 (진단)
평균회귀(Mode Collapse)가 *편곡 차원*에서 발현: 학습 분포의 *중앙값*(가장 흔한 = 가장 낡은)으로 수렴.
- 화성: 명시 안 하면 다이어토닉 삼화음 4코드 루프(I-V-vi-IV / vi-IV-I-V) — 확장·차용·반음 0.
- 악기: "band/guitar/synth/strings"만 주면 *스톡 프리셋*(2010s 슈퍼소우·진부한 패드·뻔한 어쿠스틱).
- 멜로디: 명시 안 하면 순차진행 아치형·예측가능 케이던스 — 도약·당김음·말맛 0.
→ 처방: 아래 3엔진의 *구체 서술 어휘*를 Style Position 1-6에 박아 중앙값을 탈출.

## §1. HARMONY MODERNIZER — 화성 현대화 (★Suno = 서술형, 코드기호 X)
**원리(web 검증): 삼화음 → 확장/텐션, 근음 → 전위 voice leading, 다이어토닉 → 차용/반음, 단일장르 → 교배.**

### §1.1 서술형 변환 사전 (코드 개념 → Suno가 먹는 말)
```
낡은 것                    →  현대화 서술 (Style Box에 이렇게)
─────────────────────────────────────────────────────────────────
plain triads (C-G-Am-F)    →  "lush extended chords, major-seventh and add-nine voicings,
                              sixth chords instead of plain triads, jazz-inflected harmony"
뻔한 근음 진행              →  "smooth minimal-movement voice leading, inverted chords with a
                              walking bass line, ascending bassline under static harmony"
다이어토닉만                →  "a borrowed flat-six and flat-seven lift, modal interchange color,
                              one unexpected chromatic passing chord before the chorus"
정직한 해결                 →  "a suspended chord that resolves late, a deceptive cadence into the
                              bridge, unresolved suspended tension held through the hook"
밝기 단조로움               →  "modal color (Dorian brightness / Mixolydian flat-seven /
                              Lydian raised-fourth shimmer)"
장르 고정                   →  "jazz extensions over a [folk/rock] progression, neo-soul chord
                              shadows, gospel-tinged reharmonization on the final chorus"
```
### §1.2 섹션별 현대화 자리 (28 §1 Bone과 연동)
- Verse: 확장 텐션 깔되 절제(maj7/add9) — 멜로디 공간 보존.
- Pre: 반음/차용으로 *긴장 적재*("a chromatic rise into the pre-chorus").
- Chorus: lift 장치 — 차용 bVI/bVII, 또는 전조 직전 sus 지연 해결. 단 훅 멜로디 가리지 마.
- Bridge: 가장 과감 — 모달 전환·deceptive cadence·반음 시퀀스("a key-shifting bridge with chromatic mediant motion").
- Final: 재화성(reharmonization) 1회 — gospel-tinged 또는 반음 상행 lift.
**과용 금지:** 곡당 *대담한 화성 사건 2-3개*면 충분(전부 반음이면 무국적). 나머지는 견고한 토대.

## §2. MELODY MODERNIZER — 멜로디 현대화 (04 §UE-8 컨투어와 연동)
**낡은 아치형 탈출 = 당김음·말맛·의외 도약·리듬 변위.**
```
낡은 것                    →  현대화 서술 + Lyrics 컨투어 태그
─────────────────────────────────────────────────────────────────
순차 아치형                →  "syncopated melodic phrasing, off-beat note placement,
                              conversational speech-like melody" + [Ascending melody]/[Falling tension]
박자 정직                  →  "rhythmic displacement, anticipation notes pushed ahead of the beat,
                              melody starting off the downbeat"
도약 없음                  →  "one striking interval leap to the flat-seven or ninth then steps
                              down" (도약 착지=코드 텐션, §7 voice-leading)
반복 멜로디                →  "the hook melody varies its tail on each repeat, a melodic answer
                              phrase in the second half"
오버싱잉                   →  "restrained intimate melody with space, post-2020 understated
                              topline, fewer notes more weight" (anti-멜리스마 남발)
정적 음역                  →  "the melody climbs an octave only at the final chorus, a single
                              peak note reached once" (§7 peak 1회)
```
**현대 결 참조(베끼기 X, 결만):** 인티메이트 절제형(post-Billie-Eilish near-whisper topline) / 말맛
래퍼블 멜로디(speech-melody) / 네오소울 멜리스마 *배치*(아무데나 X, 프레이즈 끝 1회) / 의외 도약+해결.

## §3. INSTRUMENTATION MODERNIZER — 악기/텍스처 현대화 (16 주법 + 28 §4 무게와 연동)
**스톡 프리셋 탈출 = 구체 텍스처 + 처리 + 하이브리드 + 2026 결.**

### §3.1 스톡 → 구체 (vague tag 박멸, §3 Prompt Designer 강화)
```
낡은/vague                 →  현대 구체 텍스처
─────────────────────────────────────────────────────────────────
"synth pad"                →  "warm analog-modeled pad with slow filter movement, granular
                              texture underneath, a glassy bell-synth counter-line"
"acoustic guitar"          →  "intimate fingerpicked nylon with fret noise left in, close-mic
                              room tone, doubled an octave with a felt-muted electric"
"strings"                  →  "close-mic chamber strings with bow texture, sul-tasto warmth,
                              doubled with a soft synth layer for thickness" (web: 현대 스트링 처리)
"drums"                    →  "dry tight modern kit with a soft-clipped transient, brushed
                              ghost notes, a processed found-sound percussion layer"
"bass"                     →  "round sub-forward bass sidechained to the kick, with a subtle
                              fingered upright doubling the low end"
"piano"                    →  "felt piano with hammer texture, a detuned upright color, a
                              Rhodes answering in the chorus"
```
### §3.2 2026 트렌드 팔레트 (현행 — web 검증, 박제 X 결만)
- **유기적 임퍼펙트 텍스처:** 양자화 X 인간 그루브, fret/breath/room noise 남김, "imperfect human warmth".
- **하이브리드 장르 교배:** 어쿠스틱+전자, 글로벌 타악+신스, neo-soul(재즈코드+앰비언트+R&B),
  Afro 퍼커션 under 신스, indie folk × hyperpop 텍스처, 모던 컨트리(힙합 크로스).
- **"Comfortable melancholy" / 시네마틱 다크:** 매끈한 시네마틱 어둠 = 현 baseline 무드.
- **다이내믹 대비 > 음압:** transient 대비 살림(올드 = 납작한 brickwall). "open dynamics, transient contrast".
- **공간/스테레오:** spatial 배치, 폭넓은 스테레오 이미지(§D 7-zone).
- **언더그라운드 텍스처:** 흔한 프리셋 대신 "obscure granular/processed textures, lo-fi tape character (의도)".
**장르별 현행 결은 web_search 1배치로 그 곡 시점 확인(§10/§11 가중) — 거시 라벨=generic.**

### §3.3 편성 다양화 (뻔한 4인조 탈출)
- 의외 악기 1개 도입(아코디언/만돌린/비브라폰/하모늄/멜로디카/처리된 found-sound).
- 동일 음색 3+ 중첩 회피 → 음색 대비(어쿠스틱 vs 전자, 마른 vs 공간).
- 섹션마다 편성 *변화*(Verse 마른 → Chorus 두터움 → Bridge 비움) = 28 §4 리폼.

## §4. ANTI-OLD EXCLUDE 메뉴 (고신호만 — 36 군살 규율 준수)
그 곡이 *실제로 끌릴* 낡은 결만 차단(전부 박지 마):
```
dated 2010s EDM supersaw / cheesy preset synth / generic stock pad / predictable four-chord loop /
quantized-stiff robotic groove / dated trance arpeggio / brickwall flat master / cheesy MIDI strings /
elevator-jazz cliche / dated 2nd-gen idol production / karaoke backing feel
```
→ 곡 장르에 맞는 2-4개만(예: 발라드면 "cheesy MIDI strings, karaoke backing feel" / EDM이면 "dated
2010s supersaw, predictable build-drop").

## §5. SUNO 적용 메커니즘 (이게 핵심 — 안 그러면 무용)
1. **코드기호 금지:** "Cmaj7-Am9" X → §1.1 서술형으로. Suno는 서술 화성 어휘를 먹는다.
2. **Position 1-3에 현대 앵커:** 마이크로장르+시대 + 현대 화성/텍스처 키워드 앞배치(§3 가중).
3. **1단어=1 sound world(§3 Prompt Designer):** "neo-soul"=Rhodes+확장코드+늦은밤 — 현대 결 압축어 활용.
4. **EXCLUDE에 낡은 결 차단(§4) + Style에 현대 텍스처 긍정.** 부정은 EXCLUDE, 긍정 설계는 Style.
5. **곡당 대담한 사건 화성2-3·멜로디1-2·악기1(의외)** — 과용은 무국적, 절제가 프로.
6. **장르 현행성 의심 시 web_search 1배치**(§10/§11) — 그 시점 사운드 확인 후 박기.

## §6. 출력 직전 안티-올드 체크 (내부, 36 BLOCK과 함께)
```
□ 화성: 삼화음 4코드 루프만 아닌가? 확장/차용/반음 사건 ≥2 서술됐나? (코드기호 0)
□ 멜로디: 뻔한 아치형 아닌가? 당김음·말맛·의외도약·peak 1회·반복변형 중 ≥2?
□ 악기: vague tag(pad/strings/band) 없나? 구체 텍스처+처리+하이브리드? 의외 악기 1개?
□ 편성: 섹션별 편성 변화? 동일음색 3+ 중첩 회피? 음색 대비?
□ 트렌드: 거시 라벨 단독 아닌가? 현행 결 반영(필요시 web_search)?
□ EXCLUDE: 낡은 결 고신호 2-4개(군살 X)?
```
하나라도 "올드 쪽"이면 §1-3 어휘로 보강 후 출력. (표면 보고 X — 고쳐서 낸다.)

## §7-PRE. ★마커-구절 효율 레버 (100-케이스 검증) — char 오버플로의 진짜 원인
char 오버플로는 *밀도 불가능*이 아니라 *구절 장황* 문제다(100케이스 검증: 프로급 밀도를 구절당 2+마커로
압축하면 679-769자에 들어감, 1000 초과 0). 1000 넘으면 내용을 자르지 말고 **마커를 복합절로 묶어라**:
- ❌ 장황: "a warm analog pad with slow filter movement" + 별도 "glassy bell texture" + 별도 형용사 나열
- ✅ 압축: "glassy detuned bell-synth and a warm analog pad" (한 절에 2악기+처리)
- 원칙: 한 절 = 2+ 프로덕션 마커. 형용사 중복 제거, 굵직한 이벤트(화성 사건·핵심 텍스처·보컬 정체성)는 보존.
- 타깃: ≤950 sweet은 프로급 밀도로도 *충분히* 도달 가능 — 넘으면 phrasing 탓이지 content 탓 아님.

## §7. 글자수 주의 (현대화는 char-hungry)
현대화 어휘를 다 박으면 Style 1000 초과 쉬움(실측 필수). 초과 시 §5 압축 — *현대화를 통째 버리지 말고*
중복 텍스처 형용사·부차 악기 먼저 깎고 **보컬 5요소·화성 사건 2-3·멜로디 사건 1-2·의외 악기 1·시대앵커는 사수**.
절제가 프로(곡당 대담한 사건 한정). 압축해도 안티-올드 마커는 남긴다(=995자에 8/8 가능).
