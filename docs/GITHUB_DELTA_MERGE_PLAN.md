# GITHUB DELTA / MERGE PLAN — main(554파일·12MB) 기준 overlay
대원칙: **기존 main은 품질 자산이다 — 삭제가 아니라 보존/정리/이동/overlay.** 본 패키지 02_GITHUB_SUPPORT/ 는 main 위에 얹는 overlay다.

## 처분표
| main 영역 | 처분 | 행동 |
|---|---|---|
| genre-dictionary/ (fullbody·legacy·index) | **보존 전체** | 손대지 않음. GENRE_CARD_SCHEMA_v2.md만 추가, 신규·보강 엔트리 6종 추가 — 기존 277+ 파일은 점진 보강 대상이지 재작성 대상 아님 |
| lyric-craft/ (기존: 화자 엔진, 은행, 워크플로) | **보존+overlay** | 기존 파일 유지. 신규 추가: korean_lyric_master_craft / lyric_mode_lock / hook_design_engine / korean_emotional_subtext_playbook / self_rationalization_bank_ko / thought_spine_method / 언어별 엔진 3종 / multilingual_gate_template (동명 파일 있으면 본 패키지가 신판 — 덮어쓰기) |
| vocal-palette/ | **보존+구조 전환** | 기존 캐릭터 파일 유지하되 [VOICE]/[LORE] 분할은 운영자 작업(PALETTE_SCHEMA·INDEX·nerh 예시 추가). 분할 전 GPT는 lore 문단 비적재로 방어 |
| production-engineering/, suno-render-behavior/ | **보존+overlay** | 신규 3+5 파일 추가(cue_device_library 포함), 동명 구판은 덮어쓰기 |
| prompt-patterns/ (create-cover·diagnostics·lyric-cues·response-templates) | **보존+추가** | 기존 4 디렉터리 그대로 + PP-001~007, exemplars/EX-01~07 추가 |
| cases/, schemas/, changelog/, vault/ | **보존** | C-20260611-01.md 추가만. vault는 Knowledge 업로드 영구 금지 유지 |
| tests/ | **정리** | 구 AT(AT-01~06, AT-v2, 구 lyric suite)는 archive/tests_pre_v4/로 이동, AT-v3.md + SMOKE-v3.md가 현행. 회귀는 스모크 4종만 평시 |
| docs/ | **교체+추가** | RUNBOOK.md(신판이 구판 대체), MIGRATION·ARCHITECTURE·SUNO_GENERATION_MODEL·RED_TEAM·TRACES·본 문서 추가. 구 INSTALL_GUIDE는 archive/ |
| gpt-upload/, knowledge-static/, instructions/ | **교체** | 본 패키지의 Instructions(7,717자)와 20장 사본으로 갱신 — Builder가 원본, repo는 사본 |
| archive/ | **활용** | 구판은 삭제 대신 여기로 — 이력 보존 |
| 루트 | **추가** | INDEX_MASTER.md (필요→경로 라우터) |

## 적용 순서 (간단)
① Builder Instructions 교체(7,717자) → ② Knowledge 20장 교체(동일 파일명) → ③ repo에 overlay 커밋(위 표) → ④ 스모크 4종 → ⑤ 통과 시 구 핫픽스·구 AT를 archive/로.
