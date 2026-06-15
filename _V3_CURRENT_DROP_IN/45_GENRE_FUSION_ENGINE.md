# 45. GENRE FUSION ENGINE — 장르 융합 엔진 (요소-슬롯·비율·충돌해소·레시피)
# VERSION: v1.0 (2026-06-15) — 이력 CHANGELOG.txt
# 근거: §15(장르 프로토콜)·§1(Substitution Map)·§10(평균회귀·2장르 한계)·05/42(장르) + 현행 융합/하이브리드 프로덕션 web 검증(2026-06)
# 위상: §15(컴포넌트 fetch·지배장르)·§1(치환)을 *요소-슬롯 배정 + 비율 제어 + 충돌해소 + 검증 레시피*로 심화.
# 발동: 융합/퓨전/하이브리드 요청·"A에 B 섞어"·"A인데 B 느낌"·비율 지정·East-West/장르 크로스오버.
# ★핵심: 융합 = *의도적 요소 배정*이지 뭉뚱그림(mud)이 아니다. 각 장르 *본질을 먼저 알고* 슬롯에 배정한다. 규칙을 알아야 맛깔나게 깬다.

## §0. 원리 — 융합은 슬롯 배정이다
"A+B"를 그냥 합치면 평균치 머드(§10). 대신 곡을 *요소 슬롯*으로 쪼개고 각 슬롯을 *어느 장르가 채울지* 배정한다.
이게 의도적 블렌드를 만든다. 예: jazztronica = 화성(재즈) + 리듬(일렉/broken-beat) + 텍스처(재즈 악기+신스) + 프로덕션(일렉).

## §1. 요소-슬롯 메서드 (★핵심 — 각 슬롯을 소스 장르에 배정)
```
슬롯              무엇                          배정 예 (A=trap, B=jazz, C=folk 융합)
──────────────────────────────────────────────────────────────
Rhythm/Groove     비트·그루브·스윙·808          A(trap): 808 glide + triplet hats
Harmony           코드·진행·색                  B(jazz): extended ninths, ii-V color
Instrumentation   악기 팔레트·텍스처            B+C: Rhodes + fingerpicked nylon
Vocal style       보컬 결·딜리버리              A 또는 컨셉: melodic conversational
Production        믹스·공간·음질 미학           A(trap): sub-forward, spacious
Structure/Form    섹션·아크                     컨셉 또는 지배 장르
```
- **배정 원칙:** 각 슬롯 = *주로 한 장르*(2개까지 섞되 셋은 분리, §10). 충돌 슬롯은 §4로 해소.
- **불필요 요소 차단:** 안 가져온 장르의 마커는 EXCLUDE로(§6) — 안 그러면 Suno가 평균으로 끌어감.

## §2. 지배 장르 제어 + 비율 (한 장르가 리드)
```
비율(예)        의미                              Suno 반영
──────────────────────────────────────────────────────
60/30/10        A 지배 / B 보조 / C 액센트         A가 Position 1·키워드 밀도·그루브 주도(§15)
50/50           동등 — 충돌 위험↑                 슬롯 분리 엄격(리듬 A·화성 B), 한쪽 EXCLUDE로 균형
70/30           A 강 지배 / B 색만                 B는 텍스처·색 슬롯만(groove는 A)
```
- **지배 장르 = Position 1 + 키워드 밀도 + 그루브/구조 주도**(§15). 보조 장르 = 특정 슬롯만 기여.
- 비율 미지정 시: 발화로 추정("A에 B *살짝*"=70/30 / "A랑 B 반반"=50/50) + 1확인. 50/50 충돌 위험 경고.

## §3. 블렌딩 기법 (Suno 서술 번역)
- **Layering(겹치기):** 두 장르 요소 동시 스택(서로 다른 슬롯). "trap 808 under jazz Rhodes chords".
- **Harmonic bridging(화성 다리):** *공유 코드 진행*으로 연결(folk↔electronic은 같은 화성으로 자연 연결). "shared chord progression bridging folk and electronic".
- **Beat matching(비트 조율):** 다른 장르 리듬을 한 템포/그리드로 화해(§4 템포). "the swing of jazz reconciled to a trap grid".
- **Crossfading/Section(섹션 전이):** 섹션마다 장르 비중 전환(verse=A, chorus=B). 모드b COVER 또는 섹션 큐(39 트랜지션).

## §4. 충돌 해소 (어떤 쌍이 부딪히나 + 어떻게)
```
충돌              증상                    해소
──────────────────────────────────────────────────
템포 미스매치      A 빠름 vs B 느림         한 템포 선택 + 다른 장르의 *feel만* 차용(하프타임/더블타임 큐)
화성 충돌          모달 vs 기능 화성        Harmonic bridge(공유 진행) 또는 섹션 분리(verse A화성/chorus B화성)
밀도 충돌          둘 다 꽉 참(머드)        요소-슬롯 규율(전부 스택 X) — 슬롯당 한 장르만(§1)
Pop Gravity(§10)   약장르가 pop로 빨림      지배 장르 EXCLUDE에 "pop chorus/radio polish" 차단
미학 충돌          raw vs polished         의도적 대비로 살리거나(41 §4 모순해소) 한쪽 프로덕션 우선
정체성 소실        뭉뚱그려 둘 다 흐려짐     "본질 먼저" — 각 장르 시그니처 1개씩 사수, 나머지 양보
```
→ 충돌은 *거절이 아니라 슬롯 재배정·브리지·섹션분리*로 푼다(41 §4 연동).

## §5. 검증 융합 레시피 (요소-슬롯 분해 — 라이브러리)
```
융합             슬롯 분해 (Rhythm / Harmony / Texture / Production)
──────────────────────────────────────────────────────────────
Jazztronica      broken-beat·일렉 / 재즈 확장화성·재화성 / Rhodes+신스+혼 / 일렉 공간·sidechain
Afrotrap         trap 808+아프로 퍼커션 / 단순 마이너 / 아프로 멜로디+신스 / sub-forward
Cinematic synthwave 80s 게이트 드럼 / 마이너 아르페지오 / analog 신스+오케스트라 / 와이드 시네마틱
Lo-fi swing      스윙 드럼+vinyl / 재즈 7th/9th / dusty Rhodes+업라이트 / 테이프 새츄
Lo-fi classical  느린 비트·노이즈 / 클래식 화성 / 피아노+현+vinyl crackle / 따뜻 로파이
East-West(sitar+trap) trap hats+타블라 / 라가 선법 / 시타르·구정+808 / 모던 sub
Neo-soul         느슨 스윙 / 풍부 확장화성 / 오르간 instr+신스 하모니 / 따뜻 organic
Folktronica      일렉 비트 / 포크 화성 / 어쿠스틱 기타+신스 패드 / 몽환 텍스처
Country-trap     trap 808 / 컨트리 I-IV-V / 밴조+슬라이드+808 / 크로스오버 폴리시
Orchestral-electronic 일렉 펄스 / 오케스트라 화성 / 현+브라스+신스 / 시네마틱 와이드
Jersey-club R&B  jersey 킥+vocal chop / R&B 화성 / 소울 보컬+클럽 신스 / 펀치+sub
```
→ 레시피는 출발점 — 컨셉 맞춰 슬롯 조정. 매번 같은 레시피 X(다양화 §10).

## §6. Suno 적용 (융합이 어떻게 박히나)
- **Position 1** = 지배 장르 + *융합 시그니처 앵커*(예: "jazztronica, broken-beat under jazz Rhodes" — 거시 "jazz+electronic" 단독 X, §3).
- **Position 2-3** = 보조 장르 기여 슬롯(텍스처·화성 색).
- **EXCLUDE** = 각 소스 장르의 *안 가져온 마커* 명시 차단(예: Afrotrap이면 "rock guitar, four-on-the-floor house" 차단) + Pop Gravity 차단(§4).
- **30% Rule(§1):** 융합은 장르가 다양해 CREATE/COVER 중복 자연히 낮음 — 모드b 변환과 시너지.
- 비율은 키워드 밀도로(지배 장르 디스크립터 多, 보조 少). 40/41 화성·리듬 어휘로 슬롯 서술 정밀화.

## §7. 출력 직전 융합 체크 (내부)
```
□ 요소 슬롯 배정했나? (리듬·화성·텍스처·보컬·프로덕션 각각 어느 장르)
□ 지배 장르 + 비율 정함? (Position 1·키워드 밀도 주도)
□ 슬롯당 ≤2 장르? (셋은 섹션 분리 — 머드 방지 §10)
□ 충돌(템포/화성/밀도/Pop Gravity) 해소? (브리지/섹션분리/EXCLUDE)
□ 안 가져온 장르 마커 EXCLUDE 차단? (평균회귀 방지)
□ Position 1 = 융합 시그니처 앵커(거시 'A+B' 단독 X)?
□ 각 장르 본질 시그니처 1개씩 사수(정체성 소실 방지)?
□ 레시피 그대로 X — 컨셉 맞춤 조정?
```
하나라도 빠지면 보강 후 출력(표면 보고 X). ★융합 = 슬롯 배정 — 뭉뚱그리면 머드, 배정하면 새 사운드.
