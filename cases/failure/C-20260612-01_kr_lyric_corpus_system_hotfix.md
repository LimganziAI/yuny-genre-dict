case_id: C-20260612-01
date: 2026-06-12
mode: SYSTEM-AUDIT | LYRIC-REPAIR | CORPUS-HOTFIX
goal: 한국어 가사 품질 실패를 막기 위한 자료 기반 시스템 보강
input_summary: 사용자는 K-pop lyric datasets, NIKL dialogue/correction/context corpora를 업로드했고, 한국어 가사가 맥락 없이 상투 장면/AI식 미문으로 망가진다고 강하게 지적함.
what_failed: 기존 시스템이 한국어 가사에서 원문 데이터/국어 자료를 실제 작동 공정으로 연결하지 못하고, 편의적 장면·예쁜 고아 행·cue 보정에 기대는 경향을 보임.
failure_class: lyric-cue | prompt-defect | reference-miss | system-routing
suspected_cause: 가사 데이터 사용이 structure-first가 아니라 summary/example/caution 프레임으로 처리됨. NIKL 자료가 일상 발화/맥락 추론/수리 게이트로 연결되지 않음.
fix_applied: STRUCTURAL CORPUS MODE, K-pop functional priors, NIKL spoken register engine, context inference repair gate, cue-after-lyric order, AT-KR-CORPUS suite를 준비.
result_after_fix: commit-ready package prepared; user must install/commit.
reuse_tags: kr-lyric, corpus-mode, nikl, kpop-priors, cue-after-lyric, anti-generic-scene
promotion_status: HOTFIX pattern-candidate
privacy: public
