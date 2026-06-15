# feedback.schema.md — Operator Feedback Intake Schema

Normalizes raw feedback ("보컬이 묻혀", "가사큐 부실해") into a routable diagnosis ticket before any fix is drafted (card 17).

```yaml
feedback_id: F-YYYYMMDD-NN
raw_quote: # operator's exact words
generation_ref: # which output (CREATE/COVER, which take)
symptom_class: lyric-cue | vocal-buried | drift | genre-vague | energy-flat | hook-weak | mix-harsh | structure-broken | random-suspect
layer: LYRICS | CREATE-PROMPT | COVER-PROMPT | EXCLUDE | SLIDERS | PAIRING
upstream_check: # did an earlier layer cause it? (cascade rule: fix upstream first)
randomness_check: regen_count + variance_observed # before blaming the prompt
prescription_ref: # card 17 symptom→prescription row applied
fields_touched: # exactly which fields get rewritten (full rewrite, not patch, if core)
expected_delta: # what should audibly change
case_link: # C-... if this becomes a case
```

Rules:
- No new song on diagnostic feedback — fix the named layer (AT-02).
- One symptom may have multiple layers; list all, fix upstream-first.
- 2+ identical-prompt regens before `random-suspect` is accepted.
