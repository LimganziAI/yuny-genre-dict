# READ ME FIRST — GitHub 업로드용

이 폴더는 GitHub 레포 `playwithlawkr/yuny-suno-os`의 **루트(root)** 에 그대로 올리는 패키지입니다.

## 업로드 위치

GitHub 레포:

```text
https://github.com/playwithlawkr/yuny-suno-os
```

업로드 위치:

```text
repo root /
```

즉, 이 폴더 안의 아래 항목들이 GitHub 루트에 바로 보여야 합니다.

```text
README.md
instructions/
gpt-upload/
knowledge-static/
knowledge-evolving/
archive/
vault/
docs/
schemas/
cases/
tests/
changelog/
```

## 업로드 방법

1. 이 ZIP을 풉니다.
2. `YUNY_01_GITHUB_REPO_ROOT_UPLOAD_20260609` 폴더를 엽니다.
3. 폴더 **자체**가 아니라, 폴더 안의 내용물 전체를 선택합니다.
4. GitHub `playwithlawkr/yuny-suno-os` 레포 루트에서 `Add file → Upload files`.
5. 선택한 내용물을 드래그합니다.
6. 이미 있는 파일은 overwrite/replace로 진행합니다.
7. commit message 예시:

```text
import: YUNY Suno OS full repository package 20260609
```

## 폴더 역할

| GitHub 폴더 | 역할 |
|---|---|
| `instructions/` | GPT 지침 패치 원본 보관. GPT Builder에 직접 붙이는 파일의 repo 보관본 |
| `gpt-upload/` | GPT Builder에 붙이거나 업로드할 파일의 백업본 |
| `knowledge-static/current-20/` | 현행 GPT 지식 20개 mirror |
| `knowledge-evolving/genre-dictionary/` | 장르사전 fullbody + genre index |
| `knowledge-evolving/kpop-artist-dna/` | K-pop/아티스트/프로듀서 DNA |
| `knowledge-evolving/reference-dna/` | 레퍼런스 카드와 sonic moment |
| `knowledge-evolving/prompt-patterns/` | CREATE/COVER, 가사큐, EXCLUDE, slider 패턴 |
| `archive/migration-v2.8/` | Claude migration 원본 보존 |
| `vault/operator-private/` | 99_OPERATOR_VAULT, 99z_SESSION_LOG 등 운영자 경험층 |
| `cases/` | success/failure/neutral case 기록 |
| `schemas/` | case 기록 양식 |
| `tests/` | regression gate, QA checklist |
| `docs/` | 운영 정책, import audit, workflow |
| `changelog/` | 변경 이력 |

## 주의

- GPT Builder에 붙이는 txt/md는 이 ZIP이 아니라 별도 `YUNY_02_GPT_BUILDER...zip`을 사용하세요.
- 이 ZIP은 GitHub 보관/연동/검색/성장형 지식용입니다.
