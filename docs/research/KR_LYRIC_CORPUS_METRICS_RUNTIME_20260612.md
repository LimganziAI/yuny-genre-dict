# KR_LYRIC_CORPUS_METRICS_RUNTIME_20260612

## user/team video lyric corpus
- files: videos_basic_stats.csv / videos_titles_lyrics.csv
- rows inspected: 459
- descriptions with Korean: 337
- median description chars: 895
- median non-empty line count: 47
- Korean line count: 15466
- median Korean line length: 16
- common endings: !:2579, ]:992, ):864, .:811, 어:654, 고:519, ?:432, 아:400, 야:287, 지:284, 데:259, 서:239

Runtime use:
This corpus is not copied into lyrics. Use it as a baseline for line pressure, object ownership, ending variety, and repeat dose. It confirms the operator's preferred output tends to longer scene-bearing lines and lower mechanical repetition than generic pop averages.

## K-pop analytics corpus
- rows: 4666
- Korean lyric rows: 4439
- all-era median line count: 37
- all-era median average line length: 12.5
- all-era median repeat ratio: 0.30
- 2010+ Korean rows: 1350
- 2010+ median line count: 54
- 2010+ median average line length: 13.1
- 2010+ median repeat ratio: 0.30

Runtime use:
K-pop data is a calibration reference, not a style target. It supports section/repeat awareness, but the operator/team corpus remains the higher bar for scene specificity and speech-origin lyrics.

## rule
Do not optimize for these numbers directly. Use metrics to catch extremes only. Length is a result; a good line is not created by median matching.
