# KR LYRIC SYSTEM ACCEPTANCE REVIEW BRIEF — 2026-06-12

## 목적
새 채팅방에서 한국어 가사 시스템이 실제로 좋아졌는지 검수한다. 목표는 칭찬이 아니라 결함 발견이다. Instructions, Builder Knowledge 05/06/20, GitHub lyric-craft 자료가 한 파이프라인으로 작동하는지 확인한다.

## 전제
1. Builder Knowledge는 전체 20장 교체가 아니라 05, 06, 20만 교체 완료.
2. Builder Instructions는 8,000자 이하 전체교체본으로 교체 완료.
3. GitHub repo에는 `3_GITHUB_OVERWRITE_ADD_ONLY/` 내용이 root 기준으로 반영되어 있음.
4. 기존 01-04, 07-19 Knowledge와 기존 GitHub 자료는 삭제되지 않았음.
5. 테스트 대상은 한국어 가사 품질, 맥락, 일상어, 큐 순서, 8필드 정합성이다.

---

## 새 채팅방 첫 메시지 — 그대로 붙여넣기

```text
지금부터 너는 방금 설치된 YUNY SUNO OS 한국어 가사 핫픽스가 제대로 작동하는지 검수한다.

목표는 칭찬이 아니라 결함 발견이다. 결과가 좋아졌는지, 아직 누덕누덕 충돌이 있는지, 어떤 파일/지침/프로세스가 서로 안 맞는지 보고해야 한다.

검수 범위:
1. Instructions가 05/06/20 Knowledge와 충돌 없이 같은 순서를 강제하는지
2. 05 카드의 독백→훅 채굴→조각→STOP→cue-after-lyric 순서가 실제로 지켜지는지
3. 06 카드의 한국어 말맛, 어미 분포, 일상어, 번역투 제거, V2/Final 전개가 살아있는지
4. GitHub lyric-craft 자료가 장식이 아니라 실제 S1/S6/S8에서 쓰이는지
5. 8필드 포맷, CREATE/COVER, EXCLUDE, SLIDERS가 기존 기능을 잃지 않았는지
6. 문제가 있으면 증상 / 원인 추정 / 관련 파일 / 수정 제안 / 재테스트 방법으로 보고한다.

먼저 시스템 설명부터 해라. 곡 필드 뽑지 말고, 현재 한국어 가사 생성 프로세스를 12줄 이하로 설명하고, 네가 실제로 지킬 검사 게이트를 나열해라.
```

### 합격 기준
- 8필드가 나오면 실패.
- 한국어 가사는 S1 corpus prior → speaker card → ugly monologue → hook mining → carving → STOP → register repair → cue pass 순서가 나와야 함.
- cue가 가사보다 먼저 오면 실패.
- 자료는 원문 복사가 아니라 구조/말맛/맥락 수리로 쓴다는 취지가 나와야 함.

---

## TEST 1 — 한국어 LYRIC-CRAFT 품질

```text
한국어 가사 테스트를 한다.

조건:
- 곡 전체는 아직 8필드 말고, 먼저 LYRIC-CRAFT 단계만 보여줘.
- 장르: 2026 Korean indie R&B, 92 BPM, close-mic male vocal, 말하듯 부르지만 끝까지 sung.
- 상황: 퇴근 후 막차 버스를 탔는데, 전 애인 번호를 지운 줄 알았지만 정류장 이름을 보고 다시 검색창에 치려는 사람.
- 금지: 편의점, 카페, 네온, 비, 지하철, 별, 그림자, 빛나, 달려가, 괜찮아.
- 목표: 일상어인데 허술하지 않고, 후렴은 한 문장으로 다시 부를 수 있어야 한다.

출력 순서:
1. INTENT LOCK 5줄 이하
2. speaker card 6줄 이하
3. ugly monologue 12문장만
4. hook candidates 5개 + 선택 이유
5. cue 없는 plain lyric draft
6. STOP-1/STOP-2/STOP-C 자가검수 표

아직 [Singing:] cue 붙이지 마라.
```

### 합격 기준
- 금지 오브젝트가 새로 나오면 실패.
- 후렴 후보가 독백에서 캐낸 말이어야 함.
- cue 없이도 가사로 읽혀야 함.
- 전 행이 명언/표어처럼 보이면 실패.
- 어미가 3연속 반복되면 실패.
- V2가 V1 재서술이면 실패.
- Final이 raw paste면 실패.
- “나/너/마음/사랑/상처”가 행을 혼자 멜 경우 실패.

---

## TEST 2 — cue-after-lyric 정합성

TEST 1 결과가 통과하면 아래를 붙인다.

```text
방금 plain lyric draft에 cue pass를 적용해라.

조건:
- 가사 본문은 의미를 바꾸지 말고 유지한다.
- [Singing:]은 섹션마다 영어 120자 이하.
- [Whispered]는 침묵/드랍 직후 짧은 행에만.
- [Held]는 열린 모음 행 끝에만, 곡 전체 1-2회.
- device는 4개 이상, 전체 행수의 1/3 이하.
- cue는 HOW만 말하고 WHAT/서사를 대신하지 않는다.

출력:
1. cue 적용 lyric
2. cue-replacement test: cue를 지웠을 때도 가사가 사는지 판정
3. cue 수량/위치 표
```

### 합격 기준
- cue가 서사를 설명하면 실패.
- cue가 매 줄 붙으면 실패.
- [Whispered]/[Held] 위치가 조건과 안 맞으면 실패.
- cue를 제거하면 감정/맥락이 사라지면 실패.

---

## TEST 3 — 8필드 정합성

```text
이제 같은 곡을 STAGED-FULL로 완성해서 정확히 8필드로 출력해라.

조건:
- CREATE는 bone만: microgenre+era, BPM/feel, key/tonal color, vocal identity, melody contour, hook shape, section arc, 3-4 articulated instruments, signature motif.
- COVER는 CREATE 결과물을 리렌더하는 설명이어야 한다. fresh-song 설명 금지.
- COVER에는 preserve map, substitution map, vocal identity preservation, energy events, 6-group quality stack, final/outro preservation이 있어야 한다.
- EXCLUDE에는 금지 오브젝트와 delivery drift, crowd/live, robotic vocal, rapping lockout을 넣어라.
- 필드별 글자수를 실측해 표시해라.

출력은 8필드만. 설명 금지.
```

### 합격 기준
- 정확히 8필드가 아니면 실패.
- CREATE에 mix/master 문구가 있으면 실패.
- COVER가 fresh song처럼 쓰이면 실패.
- COVER Audio Influence가 숫자가 아니면 실패.
- CREATE/COVER가 같은 말 30% 이상 반복되면 실패.
- LYRIC이 5000자를 넘으면 실패.

---

## TEST 4 — 한국어 가사 불만 수리

```text
방금 결과의 한국어 가사가 아직 좀 AI 같고, 2절이 1절 반복처럼 느껴지고, 어미가 단조롭다. 새 곡 말고 LYRIC-REPAIR로만 고쳐라.

출력:
1. 문제 축 분류: 품질/분량/방향/형식 중 무엇인지
2. 실패 원인: speaker truth / handoff / listener comprehension / register / ending distribution / V2 disclosure / Final defense-shift 중 해당 축
3. 고칠 행만 표시
4. 수정 lyric만 출력
5. 왜 새 8필드를 내면 안 되는지 한 줄
```

### 합격 기준
- 새 8필드가 나오면 실패.
- 분량 조절로 품질 불만을 해결하려 하면 실패.
- 멀쩡한 행까지 전부 갈아엎으면 실패.
- 어미 분포가 개선되지 않으면 실패.

---

## TEST 5 — 시스템 정합성 보고서

```text
지금까지 TEST 1-4를 기준으로 설치 상태 정합성 보고서를 작성해라.

형식:
- PASS/FAIL 총평
- 좋아진 점 5개 이하
- 아직 위험한 점 5개 이하
- 충돌 가능성이 있는 파일/규칙
- 다음 패치가 필요하면 어떤 파일을 고쳐야 하는지
- GitHub 수정 대상과 Builder 교체 대상 분리

감정적 칭찬 말고, 냉정하게 검수해라.
```

### 보고서에서 반드시 구분할 것
- GitHub에서 직접 고칠 수 있는 것: `lyric-craft/`, `tests/`, `docs/`, `prompt-patterns/`, `cases/`, `builder-runtime/` mirror.
- Builder UI에서 사용자가 교체해야 하는 것: Knowledge 05/06/20, Instructions.
- Builder 교체 대상도 GitHub `builder-runtime/`에 원본 클론본을 유지하고, 사용자가 “배포본 줘”라고 하면 그때 ZIP으로 내보내는 방식.

---

## 결함 기록 템플릿

```md
case_id: C-20260612-KR-TEST-XX
date: 2026-06-12
mode: LYRIC-CRAFT | STAGED-FULL | LYRIC-REPAIR
goal:
input_summary:
what_worked:
what_failed:
failure_class: lyric-cue | prompt-defect | register | section-pressure | install-routing | format
suspected_cause:
related_files:
fix_proposed:
retest_prompt:
promotion_status: case | pattern-candidate | promoted
privacy: public
```

---

## 운영 원칙
검수 결과 문제가 있으면 바로 전체 ZIP부터 만들지 않는다.

1. GitHub-only 수정이면 repo에서 직접 고친다.
2. Knowledge/Instructions 수정이면 `builder-runtime/` 원본 클론본을 먼저 고친다.
3. acceptance test를 추가한다.
4. 사용자가 요청하거나 패치가 안정화되면 그때 교체용 ZIP을 만든다.
