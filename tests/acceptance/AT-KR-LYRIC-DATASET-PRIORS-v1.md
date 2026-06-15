# AT-KR-LYRIC-DATASET-PRIORS-v1 — 장르 prior 적용 검사 (산출물 기준)
| ID | 입력 | 통과 증거 | 금지 증거 |
|---|---|---|---|
| PR-01 댄스록 | "한국어 여름 댄스락 가사부터" | 8필드 즉발 X · 고반복 합법이되 반복마다 기능 · 훅=speech act | 슬로건 훅, 무의미 EN 도피 |
| PR-02 발라드 | "한국어 발라드 풀곡" | 저반복·연속 사고, 행수 ~40 밴드, V2 새 기억 각도, 추상명사 단독 행 0 | 댄스급 반복 dose, EN 훅 무선언 |
| PR-03 sung 랩존 | "트랩 비트 위 sung 발라드" | sung-throughout 앵커 + EXCLUDE rapping + 행수 sung 밴드 | V2 랩화, 힙합 밀도(75행+) 이식 |
| PR-04 고속 BPM | "160 BPM K-pop rock" | 평문→호흡 절단, 행 그룹 이어 읽기 복원, [Breath] 배치 | 초안형 파편 |
| PR-05 Final | 모든 풀곡 | defense-shift(경로 A/B) | raw paste |
| PR-06 트로트 가드 | 20대 화자 모던 컨셉 | 트로트 어미(-구려/과잉 -네요) 0 | 레지스터 누출 |
| PR-07 era 결 | "90년대 발라드 결" 명시 | 저행수·저EN·완문장 결 | 2020s 짧은 행+코드스위치 혼입 |
원천: KOREAN_LYRIC_DATASET_PRIORS_ENGINE.md (실측 밴드). 가사 원문 복제 검출 시 즉시 fail(전 테스트 공통).
