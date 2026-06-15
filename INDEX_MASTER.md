# INDEX_MASTER — 필요→경로 라우터 (repo 루트 배치용)
원칙: 많이 읽기가 아니라 정확히 골라 쓰기. 곡당 fetch 예산 = 장르 fullbody 1 + 보컬 팔레트 [VOICE] 1 + 필요 시 케이스/크래프트. 순서는 항상 intent → 내 설계 초안 → fetch 검증/보강.

| 필요 | 경로 | 언제 |
|---|---|---|
| 장르 결정·fullbody | genre-dictionary/ (인덱스→정확 slug→인접) | 모든 곡 1회 — off-center 2-3 채택, 폐기 목록 |
| 보컬 캐릭터 | vocal-palette/<이름>.md **[VOICE]만** | 캐릭터 지명 시; [LORE]는 명시 호출만 |
| 한국어 정식 가사 | lyric-craft/korean_lyric_master_craft.md | STAGED 한국어 곡 필수 |
| 가사 모드 판정·보정 | lyric-craft/lyric_mode_lock.md | 기본 모드 밖 결(시적/난해/챈트/스캣 등) |
| 훅 설계·앵글 | lyric-craft/hook_design_engine.md | S3 훅 thesis·업리프트 수렴 시 |
| 감정→행동 변환 | lyric-craft/korean_emotional_subtext_playbook.md | 감정 단어가 행에 보일 때 |
| 합리화 구문 | lyric-craft/self_rationalization_bank_ko.md | 부정·변명 컨셉 |
| 사고-스파인 | lyric-craft/thought_spine_method.md | S3 매 곡 |
| 영/일/스 가사 | lyric-craft/{english,japanese,spanish}_lyric_engine.md | 해당 언어 곡 |
| 큐 디바이스 기준 | suno-render-behavior/cue_device_library.md | S8 큐 패스 |
| 렌더 가설·v5.5 | suno-render-behavior/ | 이상 거동·모델 업데이트 |
| 음질 스택·주파수 언어 | production-engineering/ | COVER 빌드·"묻혀/뭉개져" |
| 실패 패턴·모범 예 | prompt-patterns/ (PP-*, exemplars/EX-*) | 비슷한 증상·모듈 작성 전 |
| 과거 케이스 | cases/ | 같은 증상 재발·승격 판단 |
| 새 곡 절차 | docs/RUNBOOK.md | 새 창 시작 |
| 운영자 결·all_videos·작업 히스토리 | operator-history/ 4파일 + vault/operator-private/ | "내 결로" 호출 시 |
| 한국어 가사 시연·실패 부검 | lyric-craft/KOREAN_LYRIC_MASTER_DEMONSTRATION.md + LYRIC_FAILURE_AUTOPSY_* | 한국어 정식 가사 착수·품질 불만 |
| Project 동기화(지침+지식 20 미러) | project-sync/ | 설치·교체·감사 시 단일 진실 |



## KR lyric draft-origin additions
| 필요 | 경로 | 언제 |
|---|---|---|
| 한국어 가사 초안 출처 강제 | lyric-craft/KOREAN_DRAFT_ORIGIN_RUNTIME.md | 말맛·자연스러움·가사 중심 곡 |
| 한국어 훅 채굴 | lyric-craft/KOREAN_SPEECH_ACT_HOOK_MINING.md | 후렴이 주제 요약처럼 느껴질 때 |
| 한국어 음운/가창성 | lyric-craft/KOREAN_PHONEME_SINGABILITY_GATE.md | hook peak, 빠른 곡, 고음/held note 설계 |
| AI식 죽은 가사 필터 | lyric-craft/KOREAN_AI_LYRIC_FAILURE_FILTER.md | "그럴듯한데 사람 같지 않음" 진단 |
| 연구 종합 근거 | docs/research/KR_LYRIC_DRAFT_ORIGIN_RESEARCH_SYNTHESIS_20260612.md | 시스템 패치·검수·다음 릴리즈 |
| 딸기스무디 실패 재현 테스트 | tests/acceptance/AT-KR-DRAFT-ORIGIN-STRAWBERRY.md | Korean lyric release gate |
| 코퍼스 수치 기준 | docs/research/KR_LYRIC_CORPUS_METRICS_RUNTIME_20260612.md | 길이·반복 극단값 검사, 숫자 최적화 금지 |
| 업로드 자료→게이트 매핑 | docs/research/KR_LYRIC_SOURCE_INGESTION_MAP_20260612.md | 새 자료를 Knowledge 패치로 바꿀 때 |
| 최강 한국어 작사 룸 | lyric-craft/KOREAN_PRO_WRITER_ROOM_RUNTIME.md | 말맛/후렴/한국어 품질이 핵심인 곡 |
| 사물·감각 초안 랩 | lyric-craft/KOREAN_OBJECT_SENSE_TO_LYRIC_LAB.md | 추상 감정·예쁜 척 이미지가 보일 때 |
| 다단계 가사 퇴고 사다리 | lyric-craft/KOREAN_LYRIC_REVISION_LADDER_MAX.md | 초안은 맞는데 사람이 쓴 맛이 약할 때 |
| XLSX 조사팩 라우팅 | docs/research/KR_LYRIC_XLSX_SOURCE_PACK_20260612.md | 외부 논문·도구·자료 축 적용 |
| 업로드 데이터셋 사용 지도 | docs/research/KR_LYRIC_DATASET_CORPUS_USE_MAP_20260612.md | K-pop/멜론/모델 자료를 게이트로 전환 |
