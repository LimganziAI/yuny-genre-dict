# Live Interview Index — YouTube ↔ Suno Operator History

Date: 2026-06-13
Purpose: Index current live interview logs and maintain the working queue for YouTube-final ↔ Suno CREATE/COVER reconstruction.

## Locked workflow

1. Use YouTube final upload as public/canonical anchor.
2. Treat YouTube title as canonical title; Suno title is metadata-only unless user confirms otherwise.
3. Match by YouTube description lyrics ↔ Suno metadata lyrics after cue cleanup.
4. Assume post-early-v4/v5-beginning workflow is usually CREATE + COVER.
5. If final candidate is cover, show parent/source create. If parent id is missing from current export, mark it missing, not nonexistent.
6. If workbook top match is gen/create but user remembers cover, treat top match as source/create evidence and run second-pass cover search.
7. Store metadata inference and user memory separately; user confirmation controls profile promotion.
8. Character labels are voice/palette/archive seeds, not fixed presets.
9. x-character titles do not guarantee audible duet; store intended pair, audible duet reality, and archive label separately.
10. Prompt anomalies, especially literal negations in positive prompt fields, must be flagged and rewritten into positive prompt + EXCLUDE.

## Saved logs

- operator-history/interviews/20260613_youtube_suno_operator_interview_rounds_001.md
  - Rounds 1-3 interview notes: Marie / Martina / Mitchell x Martina
- operator-history/interviews/20260613_correction_rounds_001_003_cover_lineage.md
  - Correction: Rounds 1-3 need CREATE↔COVER re-link because user confirms they likely used cover workflow.
- operator-history/interviews/20260613_round_004_launchpad_ground.md
  - Round 4: Park Bongnam — Launchpad Ground
- operator-history/interviews/20260613_round_005_koori_mitai_ni_atsuku_nare.md
  - Round 5: Marie x Nerh — 氷みたいに熱くなれ
- operator-history/interviews/20260613_round_006_sore_ichi_ni_san.md
  - Round 6: Rebecca x Luke — それ、いち、に、さん

## Working queue / useful next probes

Recent / current cluster:
- [ラン・サルラ・ラン] 'ゴーイング マッド! (GOING MAD!)' [JA]
  - no character in YouTube title, TechPara/ParaPara cluster, likely useful for character assignment and no-character archive logic.
- [デルビル P.I.D.] シスタトゥー x シスターウナ - '平熱でレア' [JA]
  - likely character-pair/vocal mapping probe.
- [Run Sarura Run!] Luke x Kreather - 'On a Two-Dollar Day' [EN]
  - Luke vocal-gender clarification plus English workflow probe.
- [ラン・サルラ・ラン] サリーxレイニー - 'ギャルちゃんたち、再デビュー!（ミラーボールを回して）' [JA]
  - gyaru / pair / revival theme, likely relevant to ParaPara/club branch.

Revisit required:
- [ラン・サルラ・ラン] マリー - '濡れた靴で踊ろう' [JA]
- [デルビル P.I.D.] マルティナ - '夏が笑うほど' [JA]
- [Derville Pen is dead!] 미첼 x 마르티나 - '바람, 풀내음 그리고' [KO]

## Confirmed emerging rules

- Marie/Nerh/Martina/Bongnam/etc. values are starting points, not fixed one-size prompts.
- A good final song can be assigned to a character after hearing if vocal/lyric/genre fit.
- Foreign-language lyrics often rely on AI expression, while user controls concept and accepts after naturalness/sound checks.
- Bongnam: raspy, fast, kinetic, hard-rock/breakbeat cover success branch.
- Luke: setting_gender male, but Suno vocal route should generally be female/feminine unless user explicitly requests otherwise.
- Rebecca x Luke: radio-exercise/childhood cue can be made non-childish through TechPara cover and mature airy voice protection.
- TechPara/ParaPara is a recent Japanese production exploration branch and should be tracked as intent, not accidental genre.

## Status

This index is a live working note. Final compressed profiles should be generated after enough rounds are user-confirmed.
