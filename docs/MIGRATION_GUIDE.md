# MIGRATION GUIDE — v4.0 설치와 판정표

## 1. v3.3 가안 판정 (채택/폐기)
| 항목 | 판정 | 근거 |
|---|---|---|
| v3.3 Instructions (6,483자) | **채택+강화** | L0-L3/G1-G5/평가물리/STOP/큐-대체/off-center/VOICE-LORE를 정확히 반영. v4.0은 여기에 사고-스파인·후렴 선행·자기합리화 문법·삭제 패스·AI 결정표·보컬부하 기본·스택 사다리·fetch 예산·큐 쿼터를 주입해 7,995자(실측) |
| v3.3 변경 13장 (01,02,05,06,08,09,11,12,14,15,17,19,20) | **채택+갭 패치** | 리뷰 장치 대부분 반영 확인. 누락분만 패치: 01 에스컬레이션 / 06 합리화 문법·문학 정의·스파인 / 08 device 쿼터 / 09 fetch 예산 / 14 AI 결정표·anti-strain / 19 장면명사 대조 |
| v3.3 무변경 7장 (03,04,07,10,13,16,18) | 라이브판 채택+선별 패치 | 03 G4 훅+삭제 패스 / 07 충돌 룰 / 18 승격 사다리·HOTFIX 만료 / **10은 전면 재작성**(참고→기능분해→원본구현 적극 활용 독트린) / 04·13·16 무수정 |
| v3.3 AT/runbook/case | 폐기(본 패키지로 대체) | AT-v3.md가 12 필수 실패+신설 4를 모두 커버, 런북은 docs/RUNBOOK.md로 통합 |

## 2. 기존 시스템 keep / replace / move
| 대상 | 처분 |
|---|---|
| v3.2 핫픽스 Instructions | **교체** — 한국어 오버라이드(~40% 점유)를 L0-L1 일반 구조로 흡수, 언어 도구는 카드 06/07로 환원 |
| 라이브 20장 | **전량 교체** — 본 패키지 01_KNOWLEDGE_20이 최종본(유지 카드도 패키지에 포함돼 있음, 그대로 업로드) |
| 장르 사전(Knowledge 외부) | **GitHub 유지** + GENRE_CARD_SCHEMA_v2로 점진 보강 |
| 보컬 팔레트 파일들 | **GitHub에서 [VOICE]/[LORE] 분할 작업 필요**(운영자, PALETTE_SCHEMA 참조) — 분할 전까지 GPT는 lore 문단 적재 금지 규칙으로 방어 |
| vault | 위치 불변, Knowledge 업로드 영구 금지 |
| 기존 cases/tests | 유지 + C-20260611-01 추가, AT는 AT-v3로 대체 |

## 3. 적용 순서 (5단계)
1. **Instructions**: 00_GPT_BUILDER/00_INSTRUCTIONS_UNDER_8000_FULL_REPLACE.txt 전문을 GPT Builder Instructions에 덮어쓰기 (7,995자 실측 — 한도 내).
2. **Knowledge 20**: 기존 20장 전부 삭제 → 01_KNOWLEDGE_20/의 20장 업로드 (파일명 동일 — 교체 누락 방지).
3. **GitHub support**: 02_GITHUB_SUPPORT/ 내용을 repo의 대응 경로(knowledge-evolving/, docs/, tests/, cases/)에 커밋.
4. **Acceptance tests**: tests/acceptance/AT-v3.md 전수 1회(새 창에서 입력만 던지고 거동 채점).
5. **First smoke**: SMOKE-v3 4종(G1·G8·N2·N3) 통과 확인 → 통과 시 v3.2 핫픽스 문구 공식 은퇴(케이스 C-20260611-01에 ratified 기록).

## 4. 롤백
어느 단계든 실패 시: Instructions만 v3.2로 되돌리면 시스템은 동작한다(카드 v4는 v3.2와 호환 — 게이트가 더 강할 뿐). 카드 롤백은 불필요.
