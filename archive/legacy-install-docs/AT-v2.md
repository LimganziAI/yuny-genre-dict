# AT-v2.md — Acceptance Test Suite v2 (11종)
경로 후보: `tests/acceptance/AT-v2.md`. 카드/Instruction 변경 후 전수 재실행(card 20). 승계 매핑: A←구06 · B←구01 · C←구04 · E←구03 · G←구05 · AT-02 존치. 신규: D/F/H/I/J.

## AT-A — 시스템/패키지 질문
입력: "지금 Knowledge 구조 점검해줘 / Instructions 몇 자야?"
통과: 곡 필드 0개 · 측정값 보고(추정 금지) · "준비됨 vs 존재함" 구분(honesty) · 패치 질문이면 블록+사용자 핸드오프.
실패 라우팅: 01 / 20 / 18

## AT-B — 한국어 R&B 풀곡
입력: FX-001("새벽 감성 K-R&B… 담백한데 후렴에서만 터지는… 이별 직후… 요즘 곡처럼")
통과: 정확히 8필드 · CREATE 9요소(micro+era+scene/BPM/tonal/보컬5/contour/hook shape/section arc/악기3-4+articulation/motif) 측정 글자수 표기 · LYRIC = cue 대본(밀도표 충족, [Singing:] 섹션별 변주, 호흡, 라벨) · **엔딩 하드게이트**([Final Chorus]→[Outro]→[End]+final image+motif maintained) · 한국어 8체크 통과 · COVER 스택 6그룹+AI 값.
실패 라우팅: 04 / 05 / 08 / 15 / 16

## AT-C — 멜로디 보존 커버
입력: "이 곡 장르는 [target]으로 바꾸되 멜로디는 살려줘"
통과: AI 60-75(기본 65) · preserve map **명시**(멜로디/프레이징/보컬 정체성/훅 모양/구조) · substitution map(드럼/베이스/리드/텍스처/보컬 트리트먼트 전 역할) · 순서 8체크 준수.
실패 라우팅: 14 / 16

## AT-D — 변환이 안 됨/심심함 (신규)
입력: "장르 바꿨는데 거의 안 바뀌었어"
통과: 새 곡 재설계 금지 · substitution map 재점검 · **source-genre lockout** EXCLUDE 추가 · AI -10~20 [가설 라벨 유지] · 동일 프롬프트 재생성 여부 확인 선행.
실패 라우팅: 14 / 16 / 17

## AT-E — 보컬 매몰
입력: "커버했더니 보컬이 묻혀"
통과: production-aware 분류 · corridor 보호+200-400Hz carve+de-ess+center reservation+"lead vocal forward" · AI 재점검+사유 · EXCLUDE keyword guard 점검(muddy/compressed 류 → positive Hz어로) · COVER 측 3필드만 전체 재작성.
실패 라우팅: 15 / 16 / 17

## AT-F — 가사 러싱 (신규)
입력: "가사가 쏟아져 / 보컬이 너무 급해"
통과: BPM×음절 매트릭스 재계산 · 초과 라인 축약 · [Breath]/[Pause] 재배치(총 [Pause] ≤10) · LYRIC 필드만 전체 재작성 · 새 곡 금지.
실패 라우팅: 06 / 05 / 17

## AT-G — 실존 아티스트 레퍼런스
입력: "[실존 아티스트/곡] 같은 느낌으로"
통과: 어느 필드에도 이름 0 · Feature Sheet 14항목 분해 · 가사/번역 echo 0 · 5-layer DNA로 인코딩 · 고지: "기능만 가져왔어".
실패 라우팅: 10 / 19 / 02

## AT-H — 2절 랩화 (신규)
입력: "발라드인데 2절이 랩이 됐어"
통과: anchor "sung throughout, melodic delivery in every verse" · verse 2 [Singing:]에 sung descriptor · EXCLUDE "rapping, spoken-word delivery, rap verse" · 의도 랩 분기는 [Rapping] 명시로만.
실패 라우팅: 08 / 16

## AT-I — Studio vs 프롬프트 (신규)
입력: "이거 EQ로 풀어야 해, 프롬프트로 풀어야 해?"
통과: 분리 기준 제시(구조·장르·정체성=프롬프트 / 국소 밸런스·pan·외과 EQ·스템=Studio) · 곡 필드 미출력(질문 모드) · 약한 스템 주의(어쿠스틱기타/피아노/스트링/BGV [커뮤/中]).
실패 라우팅: 15 / 01

## AT-J — 1회 렌더 실패 (신규)
입력: "한 번 뽑았는데 별로야"
통과: 동일 프롬프트 2-3회 재생성 먼저 제안 · render_count 기록 안내 · 전역 룰 승격 0 · 이후 단일 변수 A/B 설계(표준 변수 7) · 케이스 블록 제안.
실패 라우팅: 17 / 18

## AT-02 — 가사큐 진단 (존치)
입력: (직전 8필드 존재) "가사큐가 부실해"
통과: 새 곡 0 · LYRIC 필드 한정 진단(어느 섹션·어느 큐) · RENDERS 장치로만 보강 · LYRIC 전체 재작성 1회.
실패 라우팅: 01 / 05 / 08
