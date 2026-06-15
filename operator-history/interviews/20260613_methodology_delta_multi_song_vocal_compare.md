# Methodology Delta — Multi-Song Vocal / Prompt / Lineage Comparison Mode

Date: 2026-06-13
Context: User confirmed that the interview should not be locked to a rigid per-song form. The method should evolve as more YouTube-final songs, Suno create/cover records, lyrics, prompts, vocal traits, and user memories are compared.

## User direction

- Keep using YouTube final uploads as the anchor.
- Work across all songs, not only one-by-one in a fixed order.
- Move back and forth between recent songs, older songs, Korean/Japanese/English songs, character clusters, and genre clusters as needed.
- Revisit already-interviewed songs when new comparison axes appear.
- Compare multiple songs at once when it helps identify vocal lineage, prompt behavior, character branches, or cover transformation patterns.
- Let the schema grow. Do not force all songs into one rigid template.
- Ask different questions depending on what the data needs: vocal, lyric, create/cover, prompt anomaly, character fit, selection reason, genre intent, cultural intent, user editing level, etc.
- Store confirmed changes and evolving method in GitHub to avoid losing working memory.

## Method update

The interview system now has three simultaneous modes:

1. Per-song reconstruction
- YouTube final title/lyrics
- Suno source/create candidate
- Suno final cover candidate
- parent id / missing parent status
- prompt and lyric summary
- user confirmation
- GitHub round log

2. Multi-song comparative cluster
- Compare several songs around one axis:
  - vocal seed
  - character branch
  - genre/scene
  - TechPara vs modernized dance
  - male/female/feminine vocal routing
  - duet reality vs archive label
  - AI lyric usage vs user-planned concept
  - create bone vs cover skin
  - prompt anomalies and repair rules

3. Profile compression pass
- After enough confirmed rounds, compress into:
  - character voice cards
  - IP genre/scene cards
  - vocal routing rules
  - prompt-positive rewrite banks
  - EXCLUDE banks
  - create/cover lineage heuristics
  - user taste / selection reason patterns

## Schema should remain expandable

Base fields:
- canonical_title
- youtube_title
- visible_character_label
- inferred_or_confirmed_character
- ip
- language
- final_likely_from
- source_create_candidate
- final_cover_candidate
- parent_status
- lyric_origin_edit_level
- selection_reason
- profile_promotion_level
- user_confirmed_notes

Expandable fields:
- setting_gender
- suno_vocal_gender
- branch_age
- main_canon_age
- branch_voice_relation_to_main
- audible_duet_reality
- intended_pair
- archive_label
- title_character_absent
- inferred_branch_character
- orthodox_vs_modernized_genre
- prompt_anomaly
- intended_negative_meaning
- positive_rewrite
- exclude_rewrite
- create_bone_role
- cover_skin_role
- user_planned_concept_vs_ai_expression
- cultural_reference_intent
- popularity_response

## Immediate comparative axes to build

- Luke / Kreather / Kashas male-female routing comparison.
- Sally vs ex-Sally vs ex-Teppi teenage branch comparison.
- Marie vs Nerh rock/feminine vocal boundary comparison.
- Martina core Latin/elegant branch vs lighter Japanese dance branch.
- Bongnam raspy/fast hard-rock-breakbeat branch.
- TechPara cluster: orthodox TechPara, modernized TechPara, texture-refine cover, destructive genre-transform cover.
- Pair-vocal reality: x-title but one/overlapped vocal vs true duet-like renders.
- Prompt anomaly bank: literal negations in prompt fields, over-age/under-age vocal wording, gender mismatch, AI-inserted wrong assumptions.

## Operating rule

Do not treat the current schema as final. Every round may add a new field if it improves future Suno execution or character/profile accuracy.

When enough local evidence exists, switch from single-song interview to comparative question packs, for example:
- "These three songs all use Luke; which one is closest to Luke's actual voice route?"
- "These two are both TechPara, but which is orthodox and which is modernized?"
- "This prompt says two vocals; can you hear two, or is it only an archive-pair label?"
- "This cover changed the skin; did the create already have the melody/lyric, or did cover create the final identity?"

Status: active methodology update.
