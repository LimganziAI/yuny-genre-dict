# KR Lyric Corpus + Dataset Runtime Map

## source roles
- kpop-lyrics-analytics-main: aggregate K-pop line count, character length, average line length, repeat ratio.
- Kpop-lyric-datasets-main: Melon historical chart JSON; use for corpus-level structure only, not copied lyrics.
- videos_basic_stats.csv: operator catalogue metadata; use for operator context routing, not lyric-line imitation.
- korean-lyrics-generator / KoGPT2 / lt_dataset / parallel corpora: implementation references and negative baselines; do not treat generated examples as taste target.
- hate-speech corpus: toxicity/safety filter only; never use as style source.

## measured K-pop lyric metrics from uploaded analytics csv
```json
{
  "all": {
    "line_count": {
      "mean": 42.41475998205473,
      "median": 37.0,
      "q25": 26.0,
      "q75": 55.0
    },
    "char_len": {
      "mean": 597.0601166442351,
      "median": 486.0,
      "q25": 346.25,
      "q75": 748.75
    },
    "avg_line_len": {
      "mean": 14.144550751820827,
      "median": 13.484582542694497,
      "q25": 11.818993506493506,
      "q75": 15.738558352402746
    },
    "repeat_ratio": {
      "mean": 0.3039404910742315,
      "median": 0.3023255813953488,
      "q25": 0.1964285714285714,
      "q75": 0.4101513240857503
    }
  },
  "2010+": {
    "line_count": {
      "mean": 56.854838709677416,
      "median": 54.0,
      "q25": 40.0,
      "q75": 71.0
    },
    "char_len": {
      "mean": 846.7653958944281,
      "median": 753.0,
      "q25": 527.0,
      "q75": 1090.5
    },
    "avg_line_len": {
      "mean": 14.762512857094924,
      "median": 14.17483108108108,
      "q25": 12.69468438538206,
      "q75": 16.053258145363408
    },
    "repeat_ratio": {
      "mean": 0.30853952315166694,
      "median": 0.30247858017135865,
      "q25": 0.21621621621621623,
      "q75": 0.39481806367771277
    }
  },
  "2020+": {
    "line_count": {
      "mean": 53.954887218045116,
      "median": 50.0,
      "q25": 37.0,
      "q75": 68.0
    },
    "char_len": {
      "mean": 872.7568922305765,
      "median": 696.0,
      "q25": 507.5,
      "q75": 1173.5
    },
    "avg_line_len": {
      "mean": 15.88676143770525,
      "median": 14.567567567567568,
      "q25": 12.98913043478261,
      "q75": 17.36764705882353
    },
    "repeat_ratio": {
      "mean": 0.31119328957125175,
      "median": 0.2978723404255319,
      "q25": 0.20833333333333337,
      "q75": 0.403125
    }
  }
}
```

## use as system gates
- Do not use count as target. Use as calibration for whether a song is unusually sparse/dense.
- 2020+ K-pop median line count is about 50; median repeat ratio is about 0.30. This means repetition is normal, but repetition must have function.
- Team/artist/operator material outranks generic K-pop metrics for serious Korean lyric requests.
- Metrics cannot prove quality; they only flag abnormal density, repetition, and line-length risk.
