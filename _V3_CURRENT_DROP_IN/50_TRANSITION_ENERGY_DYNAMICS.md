# 50. TRANSITION & ENERGY DYNAMICS — 전이·에너지 다이내믹 (아크 설계 + 텐션-릴리즈)
# VERSION: v1.0 (2026-06-15) — 이력 CHANGELOG.txt
# 근거: 39(곡구성·전이 어휘)·§7(컨투어)·§8(큐)·§5(강약 매트릭스)·47(훅 기대-보상) + 현행 편곡 전이/다이내믹 web 검증(2026-06)
# 위상: 39(전이 *어휘*: riser/fill/impact/sweep/tape-stop·레이어링)를 *전제*하고, 그 위에 **곡 전체 에너지 아크 설계 + 텐션-릴리즈 메커니즘 + 전이타입→Suno 큐 심화 + 고급 무브**를 더함. 39 반복 X.
# 발동: 곡 에너지 설계·"밋밋해/전이가 어색/드롭이 약해/빌드업"·댄스/일렉/시네마틱 다이내믹.
# ★핵심: 곡은 *에너지 아크*다 — 빌드(텐션)→릴리즈(드롭/후렴)→휴식→반복. 전이는 그 사이를 *매끄럽게+극적으로* 잇는다. Suno는 DAW 오토메이션이 없으니 *가사 큐+[Singing:] 백킹+Style 아크 서술*로 실현.

## §0. 원리 — 에너지가 흐르면 안 놓는다
정적인 곡은 지루. 텐션 빌드 → 릴리즈가 청자를 붙든다(47 기대-보상과 동근). 전이 어휘(riser·fill 등)는 39 — 여기선 *언제/어떻게
배치해 아크를 만드나*. Suno엔 오토메이션 레인이 없음 → 전이를 *Lyrics 브래킷 + [Singing:] 백킹 이벤트 + Style 에너지 서술*로 박는다.

## §1. 곡 전체 에너지 아크 (섹션별 에너지 레벨 설계)
```
섹션          에너지   편곡 처리                          Suno 실현
──────────────────────────────────────────────────────────────
Intro         낮음     스트립트(pad/단일 악기)             [Short Instrumental Intro], 성긴 편성
Verse 1       중하     레이어 시작(리듬+베이스)             "stripped verse, building"
Pre-Chorus    중상     ★빌드(텐션 상승)                    [Build] / riser 큐 / "rising tension into chorus"
Chorus        높음     풀 편성(릴리즈/폭발)                 [Drop] 느낌 / "full explosive chorus", 47 훅
Verse 2       중       대비(살짝 빼서 숨)                   "pull back, sparser than chorus"
Bridge        가변     ★대비(브레이크다운 또는 정점)        [Breakdown] 또는 정점 / 39 §보컬
Final Chorus  최고     최대(증폭)                          "biggest, layered, lifted"
Outro         하강     여운(페이드/단일 악기)               [Outro]/[End], 여운(§9.5)
```
- 아크 = 레이어 *추가/제거*로 만든다(39 레이어링). 매 섹션 같은 밀도 = 평면 → 의도적 빼고 채움.

## §2. 텐션-릴리즈 메커니즘 (빌드→드롭의 물리)
- **빌드(텐션 축적):** 레이어 점증 + 리듬 세분화(스네어 1/4→1/8→1/16 롤 = 부서질 파도) + 하이패스(저역 점차 제거 = 저역 복귀 신호) + 리버브 증가.
- **드롭/릴리즈(폭발):** 풀 저역 복귀 + 임팩트/서브 히트 + 타이트 다이내믹. 빌드의 텐션이 클수록 드롭이 강하다.
- **휴식(rest):** 드롭 후 빼서 숨 → 다음 빌드 여지. (텐션만 계속 = 피로.)
- Suno 큐: "snare roll building into the drop" / "high-pass filter sweep rising" / "everything drops out then hits full" / "sub-bass impact on the downbeat".

## §3. 전이 타입 → Suno 큐 심화 (39 어휘의 실전 배치)
```
전이 타입         효과                  Suno 큐 (Lyrics 브래킷 + [Singing:] 백킹)
──────────────────────────────────────────────────────────────
Riser/sweep      상승 텐션              "riser sweeping up into the chorus" / [Build]
Drum fill        파도 직전 롤            "snare fill rolling into the chorus" / [Drum fill]
Impact/sub hit   드롭 강조(릴리즈)       "impact hit on the downbeat of the chorus"
Reverse reverb   빨려드는 흡입           "reverse cymbal swell before the drop"
Filter sweep     주파수 텐션            "low-end filtered out then slams back in"
Drop-out/mute    극적 정적(pull)        [Band drops out] / "everything cuts for one bar"
Half-time        무게감 전환            [Drums cut to half-time]
Build layering   점증                  "layers stacking — add hats, then synth, then full"
Tape-stop        급정지 효과            "tape-stop into the breakdown"
```
→ 백킹 큐는 [Singing:] 안에 동반(§6/39): "strings swell underneath +6dB into the chorus".

## §4. 고급 무브 (의외성 = 기억)
- **Pull/Push:** riser로 밀고(push) + kick 제거로 당김(pull) → 드롭 직전 극대 텐션. "riser builds while the kick drops out, then everything slams back".
- **지연된 드롭:** 첫 후렴/드롭을 *기대보다 늦게* 또는 *한 번 페이크* → 텐션 서프라이즈(47 기대-보상). "the first chorus holds back, full drop only on the second".
- **브레이크다운→빌드업:** 하이패스 kick + 앰비언트 → 스네어 롤·riser 점증 → 드롭. (트랜스/EDM 코어.)
- **머니노트 동기화:** 멜로딕 정점(47 머니노트)을 드롭/후렴 폭발과 *같은 지점*에 → 음악+보컬 정점 일치(44).

## §5. 장르별 다이내믹 경향
```
장르          에너지 패턴
──────────────────────────────────────────────
EDM/댄스       빌드-드롭-휴식 사이클, riser·임팩트 강, 8/16바 패턴
트랜스         인트로-브레이크다운-빌드업-드롭-아웃트로(긴 아크, 6-9분)
팝             verse 낮음→pre 빌드→chorus 폭발(간결 아크), 지연 드롭 가끔
발라드         느린 빌드, 브릿지 정점, 다이내믹 대비(작게→크게)
힙합/트랩       비트 스위치·드롭, 하프타임 전환, 미니멀↔풀
록             verse↔chorus 다이내믹, 브릿지 브레이크다운→라스트 코러스 폭발
시네마틱        장대한 빌드, 정점 1회 크게, 긴 여운
```

## §6. YUNY 연동
- **Style:** 에너지 아크 1줄("builds from a stripped verse to an explosive chorus drop, biggest on the final"). §5 강약 매트릭스 동기화.
- **Lyrics:** 섹션 전이 큐([Build]/[Drop]/[Breakdown]/[Drums cut]/[Band drops out]) + [Singing:] 백킹 이벤트(39/§6). 39 전이 어휘 활용.
- **47 훅·44 보컬·§7 컨투어와 동기화:** 음악 정점 = 머니노트 = 보컬 cry/belt 정점 = 드롭, 한 지점에.
- 단순/잔잔 곡은 아크 과설계 X(컨셉 우선) — 다이내믹은 장르·컨셉에 비례(39 응집).

## §7. 출력 직전 다이내믹 체크 (내부)
```
□ 에너지 아크 있나? (섹션별 레벨 — 평면 X, 빼고 채움)
□ 빌드→릴리즈 메커니즘? (Pre 빌드→Chorus 드롭, 텐션 후 폭발)
□ 전이 큐 배치? ([Build]/[Drop]/riser/fill/[Band drops out] 실위치)
□ 음악 정점=머니노트=보컬 정점 동기화(47/44/§7)?
□ 휴식 자리(드롭 후 빼기)? 텐션만 연속 X?
□ 고급 무브(pull/push·지연 드롭) 적절? (의외성)
□ 장르 다이내믹 경향 반영? 잔잔 곡은 과설계 X?
□ 39 전이 어휘 + 50 아크/메커니즘 둘 다 작동?
```
하나라도 빠지면 보강 후 출력(표면 보고 X). ★곡 = 에너지 아크 — 빌드로 쌓고 드롭으로 터뜨리고 빼서 숨. 전이가 그 사이를 잇는다.
