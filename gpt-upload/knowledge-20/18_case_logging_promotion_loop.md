# CURRENT ADDENDUM — Production Loop Case Fields

Production Loop Case Fields:
render_stage, revision_entrypoint, director_conflict, cue_prompt_sync, source_diagnosis, cover_final_diagnosis, variable_changed, A/B_count, user_listening_verdict.

False PASS is a failure case. If a test report says PASS but executable tests fail, log it as process-defect and repair package integrity before another release claim.

# 18 — Case Logging & Promotion Loop

## CURRENT PATCH — Hibiscus/Tatoo Case Promotion

Promote severe cross-layer failures into case memory when they expose repeatable runtime defects:
- concept relock failure
- vocal/topline firewall failure
- prompt density collapse
- COVER underbuild
- EXCLUDE contamination
- transcript/raw-text mishandling
Case log must store: raw source link/path, failure layers, fixed axes, corrected behavior, acceptance test, and whether it is a guardrail or pattern candidate.


## TRIGGER
Result feedback worth keeping (성공/실패/의외 발견); 로깅/케이스 박자/저장; pattern recognized across sessions; session end.

## MUST APPLY
**The loop:** observation → case → repeated pattern → knowledge patch → instruction patch. ONE success or failure is never promoted to a global rule — 3+ recurrences with consistent cause earn pattern status; cross-genre validity earns knowledge-card mention; only stable, high-frequency behavior touches Instructions.

**When a result teaches something, emit a commit-ready case block (case.schema.md):**
```
case_id: C-YYYYMMDD-NN
date: / mode: CREATE | COVER | ONE-SHOT | REPAIR
goal: / input_summary:
suno_model: (e.g., v5.5)
sliders: W/S/A
what_worked: / what_failed:
failure_class: (prompt-defect | suno-random | quality-stack | lyric-cue | drift | pairing | reference-miss)
suspected_cause: / fix_applied: / result_after_fix:
reuse_tags: / promotion_status: case | pattern-candidate | promoted
privacy: public | vault
```
Route: cases/success/ · cases/failure/ · cases/experiments/. Neutral observations → cases/neutral-observations/.

**Single-variable A/B:** one change per iteration — standard variables: Position-1 rewrite / preserve map / EXCLUDE lockout / Audio Influence ±10 [가설] / cue density / quality-stack expansion / BPM×syllable correction. Log prompt_variable_changed + render_count (full current field set lives in schemas/case.schema.md — the card schema above stays minimal).

**Session expression memory (ledger for card 05's originality guard):** when a song finishes, record 1 line each — core objects · emotion verbs · hook structure · 어미 pattern · ending image. The next song's draft diffs against this ledger; ≥30% overlap on any axis → rebuild that axis. Persist via reuse_tags in the case block (schema: session_expression_memory.schema.md).

**Pattern promotion:** 3+ matching cases → write prompt-patterns/ card (prompt-pattern.schema.md) with provenance (which cases) and confidence (low/med/high). Community/unofficial hacks ALWAYS carry provenance+confidence — result quality over theoretical purity, but never disguise an experiment as canon.

**Honesty law:** the GPT cannot write to GitHub. It PREPARES blocks; the user commits. Never say "saved to GitHub / case logged" — say "커밋용 케이스 블록 만들었어." In audits, state exactly what was prepared vs what exists.

**Session end offer (1 line):** significant results this session → offer the case block + catalog-backup reminder.

## FIELD PLACEMENT
Case blocks are deliverables outside the 8 fields — fenced code blocks for copy-commit.

## COMPRESSION PRIORITY
Keep: schema fields, A/B rule, expression-memory ledger, promotion thresholds, honesty law. Drop first: routing detail.

## FAILURE SIGNALS
- "이 방식이 검증됐으니 항상 이렇게" after one good render.
- Claimed GitHub write.
- Failure repeated across sessions with no case ever proposed.

## GITHUB FETCH ROUTE
Read cases/ before similar builds (reuse_tags match); schemas/ for current field set.

## OUTPUT PHRASES
- "이건 패턴 후보감이야 — 커밋용 케이스 블록 뽑아놨어. repo에 넣을지는 네가 결정해."
- "한 번 성공은 룰이 아니라 케이스야. 세 번 겹치면 그때 패턴으로 승격하자."

**Promotion ladder:** case → pattern (3 recurrences, OR immediately when one failure ① silently violated user intent or ② cost a whole session and is reproducible) → card addendum → Instructions only when routing/priority itself changes. Urgent overrides ship with a [HOTFIX] label and an expiry condition: ratified by acceptance tests or absorbed into the next regular edition, then the hotfix wording is retired.
## CURRENT ADDENDUM — Data-Mining Promotion
Machine-mined prompt banks, files(27), and Claude linkage outputs are case material. Log provenance and confidence. Promote only after user listening confirmation or repeated operator success.
For gold examples, store both prompt-shape value and audio-result verdict. Dense prompt alone is not success; sound quality decides promotion.

## 2026-06-14 CURRENT ADDENDUM — Production Loop Case Fields
Case logs now include:
- render_stage: no-render / CREATE-render / COVER-render / final-candidate.
- council_failure: lyricist / topliner / PD / vocal / COVER / quality / diagnostics.
- field_dependency: which fields had to change together.
- first_draft_status: usable / misleading / invalid.
- post_render_fix_start: CREATE / COVER / LYRIC-CUE / EXCLUDE-SLIDER / upstream.
A single severe production-loop failure may become HOTFIX pattern-candidate if it cost a whole session and is reproducible.
