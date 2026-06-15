# builder-runtime — GPT Builder 교체본 원본 작업장

## 목적
GPT Builder UI에 직접 넣어야 하는 Instructions / Knowledge 교체본도 GitHub에서 원본을 관리한다.

YUNY는 GitHub repo 안의 이 폴더를 직접 수정할 수 있다. 사용자는 매번 ZIP을 받지 않아도 되고, 평소에는 이 폴더에 누적된 원본을 기준으로 검수한다. 사용자가 “배포본 줘 / 업데이트 해놓으라고 해 / 이건 교체해야 한다고 판단되면 줘”라고 하면 그때만 Builder 업로드용 ZIP을 만든다.

## 원칙
- GitHub에서 직접 고칠 수 있는 자료는 즉시 repo에 반영한다.
- Builder UI에 들어가는 자료도 `builder-runtime/`에 mirror 원본을 둔다.
- 실제 Builder 반영은 사용자가 한다. YUNY는 Builder UI에 직접 업로드했다고 말하지 않는다.
- hotfix는 먼저 `drafts/` 또는 `patches/`에 누적하고, acceptance test 통과 후 `release/`로 승격한다.
- Knowledge는 번호 단위로 관리한다. “05 교체”는 05만 교체한다. 20장 전체 재설치는 clean install일 때만 한다.

## 폴더 구조
```text
builder-runtime/
  instructions/
    current/00_INSTRUCTIONS_FULL_REPLACE_UNDER_8000.txt
    drafts/
    history/
  knowledge/
    current/05_lyric_dossier_and_5000_script_engine.md
    current/06_korean_lyric_prosody_hook.md
    current/20_installation_tests_update_policy.md
    drafts/
    history/
  release/
    README_RELEASE_NOTES.md
  patches/
    YYYY-MM-DD_<topic>/
```

## 운영 흐름
1. 새 문제 발견
2. GitHub에 case 또는 review report 작성
3. GitHub-only 문제면 바로 `lyric-craft/`, `tests/`, `docs/`, `prompt-patterns/` 등을 수정
4. Builder 교체가 필요한 문제면 `builder-runtime/instructions/drafts/` 또는 `builder-runtime/knowledge/drafts/` 수정
5. acceptance test 추가 또는 갱신
6. 충분히 안정화되면 `current/`로 승격
7. 사용자가 요청하면 `release/` 기준으로 Builder 교체 ZIP 생성

## 직접 수정 가능 / 사용자 교체 필요 구분

### YUNY가 직접 GitHub에서 고칠 수 있음
- `lyric-craft/`
- `tests/acceptance/`
- `docs/review/`
- `prompt-patterns/`
- `cases/`
- `builder-runtime/` mirror 원본
- `changelog/`

### 사용자가 Builder UI에서 반영해야 함
- GPT Builder Instructions 실제 교체
- GPT Builder Knowledge 실제 업로드/삭제
- Capabilities ON/OFF

## 승격 조건
- 단일 불만 1회: case만 기록
- 동일 원인 2회: draft patch 작성
- 동일 원인 3회 또는 큰 시스템 결함 1회: Knowledge/Instructions 패치 후보
- acceptance test 통과 후 current 승격

## 금지
- GitHub에 mirror만 고쳐놓고 Builder에 반영됐다고 말하지 않는다.
- raw corpus 원문을 Builder Knowledge에 넣지 않는다.
- vault/private 내용을 Builder Knowledge나 public case에 넣지 않는다.
- 05/06/20 hotfix를 전체 20장 재설치로 말하지 않는다.
