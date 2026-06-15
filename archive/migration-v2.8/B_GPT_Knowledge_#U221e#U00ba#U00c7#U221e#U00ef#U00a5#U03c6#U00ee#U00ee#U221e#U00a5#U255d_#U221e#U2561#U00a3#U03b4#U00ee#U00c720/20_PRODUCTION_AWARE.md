# ============================================================
# 20_PRODUCTION_AWARE.md
# Frequency Architecture + LUFS Mapping + Mastering
# YUNY v2.0 "Complete Renaissance Edition"
# Source: SJY051 arrangement-for-mix + bitwize/reference/mastering
# ============================================================

COVER Style Box / Final 마스터링 단계에서 자동 발동. C-59 (7-zone)
+ C-17 (LUFS) + Phase 8 (Master Workflow) 통합.


## §1. 7-Zone Frequency Architecture (C-59)

곡 작업 시 *7-zone* 자동 점검. COVER Style Box 박을 때 충돌 자리
EQ separation 큐 자동 보강.

### §1.1 Zone 정의 + 주요 악기

| Zone | Hz | 주요 악기 |
|---|---|---|
| ① Sub | 20-60 | Sub-bass synth / Kick fundamental (60Hz) / 808 sub |
| ② Bass | 60-250 | Bass guitar / Synth bass / Kick body / Low strings |
| ③ Low-mid | 250-500 | Body warmth / Chest voice / Guitar body / Snare body |
| ④ Mid | 500-2k | **Vocal corridor** / Guitar lead / Keys / Snare crack |
| ⑤ Upper-mid | 2k-4k | Vocal presence / Snare attack / Guitar bite |
| ⑥ Presence | 4k-8k | Hi-hat / Cymbal attack / Vocal sibilance / Strings air |
| ⑦ Air | 8k-20k | Sparkle / Air / Cymbal shimmer / Vocal breath |

### §1.2 Zone별 EQ 처리 표준

```
Zone ①  | High-pass filter 30Hz (rumble cut)
        | Sub-bass mono fold 20-80Hz
        | Sidechain to kick 80ms tightened

Zone ②  | Bass + Kick 분리: Bass 80Hz-200Hz / Kick 60-80Hz
        | Compression 4:1 medium attack
        | LPF 250Hz (mud cut)

Zone ③  | Mud zone — careful cut at 300Hz
        | Body 자리 (vocal chest / guitar body)
        | -2~-3dB at 400Hz when crowded

Zone ④  | Vocal corridor 500Hz-3kHz **보호**
        | Other instruments -2dB cut at 1-2kHz
        | Vocal +1dB at 1.5kHz (presence)

Zone ⑤  | Vocal presence + Snare attack
        | De-esser 5-8kHz on vocal
        | Snare +1dB at 3kHz (crack)

Zone ⑥  | Hi-hat / Cymbal / Vocal sibilance
        | -2dB at 6-8kHz if harsh
        | Vocal de-essing primary zone

Zone ⑦  | Sparkle / Air
        | High shelf +1-2dB at 12kHz (taste)
        | LPF 18kHz (mastering)
```

### §1.3 자동 점검 룰 (출력 전)

COVER Style Box 출력 직전 7-zone 1차 점검:

- 동일 zone 3+ 악기 겹침 → conflict 경고
- 충돌 자리 EQ separation 큐 자동 보강
- Vocal corridor 침범 악기 → -2dB cut 큐 박음
- Sub mono fold 누락 → "sub-bass mono 20-80Hz" 추가

### §1.4 Kick-Bass 관계 결정

가장 흔한 충돌 → 명시 처방:

```
Option A (Pop/EDM 표준):
- Kick fundamental: 60Hz
- Bass: 80-150Hz
- Sidechain bass to kick, 80ms

Option B (Hip-hop/Trap):
- 808: 30-60Hz (sub + body)
- Kick top: 60-100Hz (click)
- Bass 거의 없음 또는 808와 통합

Option C (Rock):
- Kick: 60-80Hz (punchy)
- Bass: 80-250Hz (full body)
- No sidechain (natural overlap)

Option D (Acoustic / Jazz):
- Upright bass: 50-200Hz
- Kick: 60-100Hz (soft)
- Natural overlap, no aggressive separation
```

### §1.5 Stereo Image Architecture

```
Center (mono):
- Lead vocal
- Kick + Snare
- Bass (20-80Hz mono fold)
- Lead instrument (solo 자리)

L far:
- Rhythm guitar L
- Pad L wide
- Backing vocals L

L near:
- Percussion L
- Synth L mid-width
- Doubled vocal L

R near:
- Percussion R
- Synth R mid-width
- Doubled vocal R

R far:
- Rhythm guitar R
- Pad R wide
- Backing vocals R
```


## §2. LUFS Mapping (C-17)

### §2.1 우리 시스템 매핑 (생성 자체 + 곡 결)

```
Modern Dance/EDM:        -6 ~ -8 LUFS
Modern Pop:              -7 ~ -9 LUFS
Modern Trot/Crossover:   -8 ~ -10 LUFS (warm not loud)
Modern Ballad/R&B:       -9 ~ -11 LUFS
Indie/Acoustic:         -10 ~ -13 LUFS
Jazz/Classical:         -12 ~ -14 LUFS
Vintage (70-80s):       -14 ~ -16 LUFS
Lo-fi/Ambient:          -14 ~ -18 LUFS
```

### §2.2 마스터링 최종 (외부 검증 — bitwize 풀바디)

**Streaming Standard: -14 LUFS / -1.0 dBTP**

장르별 정밀 매핑 (bitwize genre-specific-presets 247줄 통합):

#### Pop & Mainstream
| 장르 | LUFS | High-Mid Cut | Notes |
|---|---|---|---|
| pop | -14 | -1.0 dB | Bright, polished, radio-ready |
| k-pop | -14 | -1.0 dB | Crisp, punchy, vocal-forward |
| hyperpop | -14 | -1.5 dB | Aggressive brightness, taming |

#### Hip-Hop & Rap
| 장르 | LUFS | High-Mid Cut | Notes |
|---|---|---|---|
| hip-hop | -14 | -1.0 dB | Standard, bass-forward |
| rap | -14 | -1.0 dB | Same as hip-hop |
| trap | -14 | -1.0 dB | Keep hi-hat brightness |
| drill | -14 | -1.5 dB | Dark, aggressive |
| phonk | -14 | -1.5 dB | Lo-fi aesthetic, warmer |
| grime | -14 | -1.0 dB | UK sound, punchy |
| nerdcore | -14 | -1.0 dB | Clear vocals, nerdy themes |

#### R&B, Soul & Funk
| 장르 | LUFS | High-Mid Cut | Notes |
|---|---|---|---|
| rnb | -14 | -1.5 dB | Smooth, vocal clarity |
| soul | -14 | -1.5 dB | Warm, analog feel |
| funk | -14 | -1.5 dB | Punchy, groove-focused |
| disco | -14 | -1.5 dB | Bright but not harsh |
| gospel | -14 | -1.5 dB | Vocal warmth, choir clarity |

#### Rock
| 장르 | LUFS | High-Mid Cut | Notes |
|---|---|---|---|
| rock | -14 | -2.0 dB | Standard, tame guitar harshness |
| indie-rock | -14 | -1.5 dB | Less aggressive |
| alternative | -14 | -2.0 dB | Safe middle ground |
| grunge | -14 | -2.5 dB | Gritty but controlled |
| garage-rock | -14 | -2.0 dB | Raw energy |
| surf-rock | -14 | -1.5 dB | Bright twang |

#### Dynamic Rock (More Headroom)
| 장르 | LUFS | High-Mid Cut |
|---|---|---|
| jazz-rock | -16 | -1.0 dB |
| classic-rock | -14 | -1.5 dB |
| psychedelic | -14 | -1.5 dB |
| prog-rock | -16 | -1.0 dB |

#### Electronic
| 장르 | LUFS | High-Mid Cut |
|---|---|---|
| electronic | -14 | -1.5 dB |
| edm | -14 | -1.5 dB |
| house | -14 | -1.5 dB |
| techno | -14 | -1.5 dB |
| trance | -14 | -1.5 dB |
| dubstep | -14 | -2.0 dB |
| drum-and-bass | -14 | -1.5 dB |
| ambient | -16 | -0.5 dB (warm) |
| lofi | -16 | -2.0 dB (vintage) |

#### Folk, Acoustic & Country
| 장르 | LUFS | High-Mid Cut |
|---|---|---|
| folk | -16 | -1.0 dB |
| acoustic | -16 | -1.0 dB |
| country | -14 | -1.0 dB |
| bluegrass | -16 | -1.0 dB |
| americana | -14 | -1.0 dB |
| singer-songwriter | -16 | -1.0 dB |

#### Jazz & Blues
| 장르 | LUFS | High-Mid Cut |
|---|---|---|
| jazz | -18 | -0.5 dB (preserve dynamics) |
| blues | -16 | -1.0 dB |
| smooth-jazz | -16 | -1.0 dB |
| bebop | -18 | -0.5 dB |

#### Classical & Orchestral
| 장르 | LUFS | High-Mid Cut |
|---|---|---|
| classical | -23 | 0 dB (no cut) |
| orchestral | -18 | -0.5 dB |
| chamber | -20 | 0 dB |
| neo-classical | -18 | -0.5 dB |

#### Metal & Heavy
| 장르 | LUFS | High-Mid Cut |
|---|---|---|
| metal | -10 | -3.0 dB |
| heavy-metal | -10 | -3.0 dB |
| death-metal | -10 | -3.5 dB (extreme taming) |
| metalcore | -10 | -3.0 dB |
| djent | -10 | -3.0 dB |

### §2.3 LUFS 측정 도구

외부 자료 검증:
- **Free**: analyze_tracks.py (bitwize), Youlean Loudness Meter, MeterMatch
- **Paid**: iZotope Insight 2, Waves WLM Plus
- **DAW Built-in**: Logic Pro Loudness Meter, Pro Tools Loudness Analyzer

### §2.4 True Peak 한도

```
True Peak > 0 dBTP   → Clipping on playback → 왜곡
True Peak at -0.5 dBTP → 인코딩 후 클립 가능성
True Peak at -1.0 dBTP → 안전 헤드룸 (권장)
True Peak at -2.0 dBTP → 매우 안전 (잡음 적은 환경 권장)
```

### §2.5 Dynamic Range 권장치

```
| 장르 | 권장 LRA (LU) |
|---|---|
| Classical | 15-25 |
| Jazz/Folk | 10-15 |
| Rock/Pop | 6-12 |
| EDM/Hip-Hop | 4-8 |
```

LRA 4 미만 = over-compressed (피로감)
LRA 10 초과 = 평탄 (loudness 부족)


## §3. Suno Output Loudness (Pre-Mastering)

**외부 검증 (v5-best-practices §Suno Output Loudness):**

*"These are typical loudness levels Suno generates — not final mastering targets."*

| 장르 | Typical Suno Output |
|---|---|
| Pop/EDM | -9 to -7 LUFS |
| Lo-Fi | -12 to -11 LUFS |
| Podcast/Spoken | -16 to -14 LUFS |

**원칙:**
- Suno 생성 자체는 *프로 마스터링 X*
- 운영자가 *외부 mastering 거치고* 스트리밍 배포
- Suno 출력 → Stem extract → DAW mix → Master → -14 LUFS


## §4. Compression 처방

### §4.1 Bus Compression (믹스 글루)

```
Master Bus (Glue Compression):
- Ratio 2:1 ~ 4:1
- Threshold 2-3dB GR
- Attack 30-50ms (slow)
- Release 100-200ms (fast)
- Knee soft
```

**v2.0 외부 검증 (v5-best-practices §Troubleshooting):**
*"Mix feels flat" → "bus compression 2–3 dB, slow attack/fast release"*

### §4.2 Sidechain Compression

```
Bass sidechain to Kick:
- Ratio 4:1 ~ 8:1
- Threshold -10dB
- Attack 1-5ms (fast)
- Release 80-100ms (medium)
- Source: kick
- Target: bass
```

### §4.3 Vocal Compression

```
Lead Vocal:
- Stage 1 (controller): Ratio 3:1, Attack 5ms, Release 50ms, 3-4dB GR
- Stage 2 (color): Ratio 2:1, Attack 30ms, Release 150ms, 2dB GR
- Total GR: 5-6dB
```

### §4.4 Drum Compression

```
Snare:
- Ratio 4:1
- Attack 5-10ms
- Release 50-100ms
- 3-5dB GR

Kick:
- Ratio 3:1
- Attack 20-30ms (preserve attack)
- Release 80-100ms
- 2-3dB GR
```


## §5. Mastering Chain (Final Stage)

### §5.1 Standard Chain Order

```
1. Corrective EQ (cleanup)
   - HPF 30Hz (rumble cut)
   - Notch 100Hz mud
   - LPF 18kHz (anti-aliasing)
   
2. Multiband Compression (선택)
   - Low band: 4:1 (bass control)
   - Mid band: 2:1 (gentle glue)
   - High band: 2:1 (de-essing master)
   
3. Glue Compression (single band)
   - 2:1, slow attack, 2-3dB GR
   
4. Saturation / Harmonic Exciter (선택)
   - Tape saturation 1-2%
   - Tube warmth
   
5. Stereo Imager (선택)
   - Low frequency mono fold (under 80-100Hz)
   - High frequency widen
   
6. Final EQ (tonal balance)
   - Genre-specific shelf adjustments
   - High-mid cut from genre preset table
   
7. Limiter (Peak Control)
   - Threshold to hit target LUFS
   - True Peak -1.0 dBTP
   - Release medium
   
8. Output Stage
   - Final LUFS measurement
   - True Peak verification
```

### §5.2 Genre-Specific Mastering Recipes (bitwize 통합)

#### Modern Pop / K-Pop
```
1. HPF 35Hz
2. Notch 250Hz (mud)
3. Saturation 1% (warmth)
4. Glue comp 2-3dB GR
5. High-mid cut -1dB at 3.5kHz
6. High shelf +1dB at 12kHz (air)
7. Limit to -14 LUFS / -1.0 dBTP
```

#### Modern Hip-Hop / Trap
```
1. HPF 25Hz (preserve 808 sub)
2. Bass tilt +2dB at 60Hz
3. Saturation 1.5% (analog warmth)
4. Glue comp 2dB GR
5. High-mid cut -1dB at 3.5kHz
6. Limit to -14 LUFS / -1.0 dBTP
```

#### Indie / Acoustic
```
1. HPF 40Hz
2. Subtle warmth boost +1dB at 250Hz
3. Glue comp 1-2dB GR (preserve dynamics)
4. High shelf +1dB at 10kHz (air)
5. Limit to -16 LUFS / -1.0 dBTP
```

#### EDM / Dance
```
1. HPF 30Hz
2. Bass boost +2dB at 80Hz
3. Mid scoop -1dB at 400Hz
4. Multiband comp on low 3:1
5. Glue comp 3dB GR
6. Stereo widen high
7. Limit to -10 LUFS (club master) or -14 LUFS (streaming)
```

#### Jazz / Classical
```
1. HPF 25Hz (minimal)
2. No saturation (preserve transient)
3. Glue comp 1dB GR or none
4. No multiband
5. Tonal balance shelf adjustments only
6. Limit to -18 LUFS / -1.0 dBTP (preserve dynamics)
```


## §6. Mastering 7-Point QC (19 §20 통합)

```
1. LUFS Target 달성?
2. Peak < -1.0 dBTP?
3. Dynamic Range 적정?
4. Frequency Balance 양호?
5. Stereo Image 균형?
6. Vocal Presence 충분?
7. Mastering Chain 일관성?
```

**자동 발의:** 운영자 *마스터링* 발화 시 7-Point QC 풀바디 +
19 §20 통합 진단.


## §7. COVER Style Box 자동 보강

운영자 COVER 작성 시 본 파일 자동 발동:

1. 마이크로 장르 인식 → LUFS target 결정
2. 7-zone 점검 → EQ separation 큐 보강
3. Throughout discipline (C-5) 의무
4. v2.0 외부 검증 (v5-best-practices) 보조 어법 추가:
   - "Vocal too buried" → "lead vocal 1–2 dB louder than band"
   - "Mix feels flat" → "bus compression 2–3 dB, slow attack/fast release"
   - "Arrangement too busy" → "verse 2: bass rests for 4 bars"
   - "Chorus not lifting" → "double-time hats; octave guitars"


## §8. 외부 검증 통합

- SJY051 references/production-aware/arrangement-for-mix.md (7-zone 원천)
- bitwize/reference/mastering/genre-specific-presets.md (247줄 풀바디)
- bitwize/reference/mastering/loudness-measurement.md (313줄)
- bitwize/reference/mastering/mastering-checklist.md (269줄)
- bitwize/reference/mastering/mastering-workflow.md (527줄)
- bitwize/skills/mastering-engineer/SKILL.md (15KB)
- v5-best-practices §Suno Output Loudness

# ============================================================
# END OF 20_PRODUCTION_AWARE.md
# ============================================================
