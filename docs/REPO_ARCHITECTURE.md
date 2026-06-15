# GitHub 최종 권장 구조 — Knowledge(런타임 게이트) vs GitHub(살아있는 소재)

## 분리 원칙
- **Knowledge 20장** = 매 턴 적용되는 런타임 게이트·라우팅·문법. 작고 안정적이어야 한다. 20슬롯은 하드 제한.
- **GitHub** = 살아있는 소재 라이브러리. 크고, 자라고, 곡마다 필요한 부분만 fetch한다. "많이 읽기"가 목적이 아니라 **정확히 골라 쓰기**가 목적 — off-center 채택 룰이 여기 걸린다.
- **장르 사전 배치 판정: GitHub living material이 정답.** 277+ 파일을 Knowledge에 넣으면 RAG 검색이 흐려지고 갱신이 죽는다. Knowledge 09는 인덱스 경로·사용법·off-center 룰만 든다.

## 최종 트리
```
yuny-suno-os/
  instructions/00_INSTRUCTIONS_UNDER_8000_FULL_REPLACE.txt   # 현행 사본(원본은 GPT Builder)
  knowledge-static/current-20/                               # 20장 사본(원본은 GPT Builder)
  knowledge-evolving/
    genre-dictionary/        # GENRE_CARD_SCHEMA_v2 13-field 카드 — 성장 레이어
    vocal-palette/           # 캐릭터 = [VOICE]/[LORE] 분리 + INDEX. 기본 fetch=[VOICE]
    lyric-craft/             # 작사 공학 풀바디(화자 엔진·스파인·합리화 은행·훅 설계·언어별 엔진·표현 은행)
    production-engineering/  # 음질 사다리·주파수 언어 사전·페어링 리스크
    prompt-patterns/         # 실패→패턴(PP-) + 모듈별 모범/반례(exemplars/EX-)
    reference-dna/           # 웹 검증 완료 feature sheet 보관(card 10 산출물)
    suno-render-behavior/    # 렌더 가설 H1-H4·Cover/Remaster 라우팅·Exclude 거동·v5.5 노트
  cases/{failure,success,experiments,neutral-observations}/  # 케이스 → 패턴 승격의 원천
  schemas/                   # case·prompt-pattern·genre-card·vocal_palette·feature-sheet·lyric-dossier
  tests/{acceptance,smoke}/
  docs/                      # 본 문서들(SUNO_GENERATION_MODEL·RUNBOOK·MIGRATION_GUIDE·RED_TEAM 등)
  vault/                     # 운영자 비공개 — Knowledge 업로드 절대 금지(Code Interpreter 노출 경로)
```

## 배치 판정표
| 자료 | 위치 | 이유 |
|---|---|---|
| 게이트·문법·라우팅·모드·우선순위 스택 | Knowledge | 매 턴 필요, 안정 |
| 장르 사전 전체 | GitHub | 거대·성장·선택적 fetch |
| 보컬 팔레트 | GitHub ([VOICE] 기본 fetch) | lore 격리가 구조적으로 필요 |
| 작사 재료·표현 은행·언어 엔진 | GitHub | 곡마다 다른 1-3파일만 fetch |
| 케이스·패턴·exemplar | GitHub | 누적 학습 레이어 |
| 렌더 거동 연구 | GitHub | 모델 업데이트마다 재검 |
| 운영자 vault | GitHub private | Knowledge 노출 금지 |

## 운용 규칙
1. fetch는 raw.githubusercontent.com 경로로, 곡당 예산(장르 1 + 팔레트 1 + 케이스 필요 시) 안에서.
2. GPT는 GitHub에 직접 쓰지 못한다 — 커밋 블록을 준비하고 운영자가 적용한다(정직 법칙).
3. 새 파일은 반드시 해당 schema를 따른다. 케이스 3회 재발 또는 의도 무성 위반 1회 = 패턴 승격.
