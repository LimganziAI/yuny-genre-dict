# 장르사전 외부화 — 셋업 가이드 (YUNY v2.7)

목표: 풀바디 장르사전(23b–k, ~4MB)을 프로젝트에서 빼 **public GitHub**에 두고,
프로젝트엔 **슬림 인덱스만** 남겨 장르 발화 시 해당 장르 1개만 `web_fetch`.
→ 프로젝트 ~4MB 확보 + 친구한테 줄 때 커넥터 없이 즉시 사전식 조회.

라우팅 3곳은 동봉한 **활성화 버전 시스템 지침**(`00_SYSTEM_INSTRUCTION_for_YUNY.txt`)에 이미 반영됨.
아래는 네가 GitHub에 올리고 프로젝트 파일만 교체하면 끝.

================================================================
## 1. 들어가는/나가는 파일
================================================================
| 위치 | 파일 | 처리 |
|---|---|---|
| 프로젝트 유지 | `23a_GENRE_INDEX_MASTER.md` | **파일명 그대로**, 내용만 새 슬림 인덱스로 덮어쓰기 |
| 프로젝트 제거 | `23b`–`23k` (슬림 구버전) | GitHub로 이전 → 용량 확보 (풀버전이 대체) |
| GitHub(public) | `23_GENRE_FULLBODY/` + `README.md` | 277 장르 + 인트로 10 + 부록 1 |

⚠️ GitHub엔 이번에 올린 **확장 풀버전**을 올림(프로젝트의 슬림 구버전 아님).

================================================================
## 2. GitHub 올리기 — 계정 LimganziAI
================================================================
### A) repo 생성
1. github.com 로그인 → 우상단 `+` → **New repository**
2. Owner `LimganziAI` / Name `yuny-genre-dict` / **Public** / (Add README 체크 해제) → Create

### B) 파일 올리기 — 방법 1: 웹 드래그(설치 X)
1. `23_GENRE_FULLBODY.zip` 압축 풀기 → `23_GENRE_FULLBODY/` 폴더 + 동봉 `README.md` 준비
2. repo 페이지 → **Add file ▸ Upload files** → 폴더와 README 드래그 → **Commit changes**
3. 파일 288개라 한 번에 안 올라가면 카테고리 폴더(rock-metal 등) 단위로 나눠 드래그

### B) 방법 2: git CLI(288개 한 방 — 안정적). repo는 A에서 빈 상태로 만든 뒤:
```
cd <압축 푼 자리>
git init
git remote add origin https://github.com/LimganziAI/yuny-genre-dict.git
git add 23_GENRE_FULLBODY README.md
git commit -m "Add genre full-body dictionary (277 genres)"
git branch -M main
git push -u origin main
```
(GitHub Desktop 앱이면 GUI로 동일 — 폴더 끌어다 commit→push)

### C) 확인: 아무 장르 raw URL 열어보기
`https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/dream-pop.md`
→ 본문 뜨면 성공.

================================================================
## 3. 출처 표기 (CC BY 4.0) — 이미 처리됨
================================================================
동봉 `README.md`에 아래가 들어있음. repo에 그 파일만 올리면 표기 끝(추가 작업 0):

  Based on "Music Composition Agent Skill v1.0" by SJY051 and contributors
  (https://github.com/SJY051/music-composition), licensed under CC BY 4.0.
  Changes made: expanded ~5–6× and restructured into per-genre files with
  Suno-specific prompt keywords. This adapted work is likewise CC BY 4.0.

CC BY 4.0은 상업 포함 개작·재배포를 허용 — 이 한 줄(출처+라이선스+변경표시)만 있으면 완전 합법.

================================================================
## 4. 연동 — 어떻게 작동하나 (커넥터 0)
================================================================
1. 프로젝트엔 `23a_GENRE_INDEX_MASTER.md`(슬림, 각 장르 경로 + BASE_URL) 상주.
2. "[장르] 결로" 발화 → 인덱스에서 장르명/[slug] 매칭 → 전체 URL = BASE_URL + "/" + 경로
3. `web_fetch(URL)` → 그 장르 본문만 로드(~4–16K). 통짜 789K fetch 문제 해소.
4. public raw URL이라 인증·커넥터 불필요. 친구는 "프로젝트 + 인덱스"만 받으면 동일 작동.
5. BASE_URL은 인덱스 맨 위 한 줄(LimganziAI/yuny-genre-dict로 박아둠 — repo명 바꾸면 그 줄만 수정).

================================================================
## 5. 시스템 지침 라우팅 — 반영된 3곳 (참고)
================================================================
- §15 fetch: `장르→05·23a INDEX(슬림,프로젝트)→web_fetch 장르파일(GitHub)`
- D 인덱스: `장르 "[장르] 결로" → 05 / 23a INDEX(슬림) → slug 매칭 → web_fetch(BASE+경로) / 없으면 web_search`
- 로스터: `23a 장르인덱스(슬림; 23b-k 본문=외부 public GitHub)`

================================================================
## 6. 중복 slug 8개 (정상 — 2개 카테고리 교차 등재)
================================================================
indie-folk, acid-jazz, grime, hyperpop, phonk, reggaeton, latin-trap, bossa-nova
→ 카테고리 폴더로 분리돼 충돌 없음. 인덱스에 둘 다 등재.
