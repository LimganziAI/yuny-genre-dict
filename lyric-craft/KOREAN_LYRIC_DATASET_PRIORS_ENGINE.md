# K-POP LYRIC FUNCTION PRIORS — 원문 없는 구조 요약

분석 대상: `Kpop-lyric-datasets-main.zip`의 melon JSON.

## 비원문 구조 지표
```json
{
  "songs_analyzed_nonverbatim": 25236,
  "line_count_p25_median_p75": [
    36,
    48.0,
    67
  ],
  "median_hangul_syllables_per_line": 8.25,
  "median_repeated_line_ratio": 0.276,
  "median_english_char_share": 0.058,
  "ending_class_top10": {
    "other": 545590,
    "english_end": 290140,
    "plain_open": 188741,
    "connector_cut": 107309,
    "question_open": 79267,
    "direct_speech": 58485,
    "polite": 44774,
    "statement_da": 21542,
    "empty": 3576
  },
  "genre_top15": [
    [
      "발라드",
      8470
    ],
    [
      "댄스",
      5905
    ],
    [
      "랩/힙합",
      3184
    ],
    [
      "R&B/Soul",
      1977
    ],
    [
      "발라드, 국내드라마",
      1575
    ],
    [
      "록/메탈",
      1539
    ],
    [
      "POP",
      289
    ],
    [
      "인디음악, 포크/블루스",
      258
    ],
    [
      "인디음악, 록/메탈",
      240
    ],
    [
      "포크/블루스",
      182
    ],
    [
      "성인가요/트로트",
      171
    ],
    [
      "발라드, 인디음악",
      166
    ],
    [
      "댄스, 랩/힙합",
      134
    ],
    [
      "록/메탈, 국내드라마",
      132
    ],
    [
      "국내드라마",
      88
    ]
  ],
  "note": "No lyric line is exported. Metrics are structural only."
}
```

## 이 지표를 쓰는 법
- median line count와 repeated-line ratio는 “길이 목표”가 아니라 섹션 압력의 기준선이다.
- repeated-line ratio가 높아도 Final Chorus는 의미 변화가 있어야 한다.
- English share는 자동 영어 삽입 허가가 아니다. 화자/장르/훅 기능이 요구할 때만 쓴다.
- ending class는 “예쁘게 운 맞추기”가 아니라 같은 어미 3연속, 같은 문장 종결 50% 초과를 막는 감시다.
- genre top은 데이터 분포일 뿐, 사용자가 준 곡의 장르를 덮지 않는다.

## 실패 방지 룰
- 발라드 prior로 댄스 훅을 쓰지 않는다.
- 댄스 반복 dose로 독백형 발라드를 늘리지 않는다.
- 랩/힙합 데이터가 섞였다고 sung 곡 Verse2를 랩으로 drift시키지 않는다.
- 후렴 후보는 데이터 표면이 아니라 현재 화자의 독백에서 캔다.
