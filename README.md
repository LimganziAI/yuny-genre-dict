# YUNY SUNO OS — Master Repo (LimganziAI/yuny-genre-dict)

이 repo 하나로 YUNY 전체를 총괄 관리한다. (이름은 yuny-genre-dict지만 OS·지식·장르사전 통합 마스터.)

## ★ 절대 주의 — 장르사전 보존
`23_GENRE_FULLBODY/<카테고리>/<slug>.md` (277개 장르 파일)은 YUNY 시스템이 **런타임에 실시간 fetch**한다:
  https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/...
→ 이 폴더를 절대 지우지 마라. 배포는 **ADD(병합) 방식**으로만 (deploy 스크립트 기본값 = WipeExisting:$false).

## 현재 시스템 (v3.0 GOAL CHAIN, 54 레이어)
- `_V3_CURRENT_DROP_IN/` — ★현재 권위본 전체. Claude Project에 올리는 파일들:
    - `00_SYSTEM_INSTRUCTION_for_YUNY.txt` = 지침 (Project instruction 칸 또는 지식파일로)
    - `02~53_*.md` + `00_ROUTER.md` `01_OPERATING_RULES.md` `99_*.md` `99z_*.md` `CHANGELOG.txt` = 지식파일 (Project 지식칸에 통째로)
- 그 외 폴더(cases/ schemas/ tests/ knowledge-evolving/ archive/ 등) = 조직·백업·레거시. 런타임 영향 없음.

## 배포 (로컬 → 이 repo main, ADD 방식)
1. `_V3_CURRENT_DROP_IN/` 외 구조 그대로 C:\uploadc 에 풀기
2. deploy 스크립트 실행 (WipeExisting:$false 확인) → 장르사전 보존하며 병합 push
