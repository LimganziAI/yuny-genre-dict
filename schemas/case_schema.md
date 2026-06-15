# Case Schema

Use this schema for both success and failure cases.

```yaml
case_id: YYYYMMDD_short_slug
date: YYYY-MM-DD
type: success | failure | neutral
task_type: create | cover | genre-transform | lyric | cue | diagnosis | system
language:
genre_request:
reference:
source_material:
  create_prompt:
  cover_prompt:
  lyric:
  exclude:
  sliders:
result:
  what_worked:
  what_failed:
  user_feedback:
diagnosis:
  failure_class:
  upstream_route:
  root_cause:
preserve_map:
  hook:
  topline:
  lyric_phrasing:
  singer_roles:
  section_order:
  modulation:
  micro_bends:
  signature_motif:
correction:
  prompt_change:
  lyric_change:
  cue_change:
  production_change:
  slider_change:
transferable_pattern:
promotion_status: observation | case | repeated_pattern | knowledge_patch | instruction_patch
related_files:
tags:
```
