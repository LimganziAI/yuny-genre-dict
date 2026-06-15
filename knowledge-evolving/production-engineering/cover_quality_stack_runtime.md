# COVER Quality Stack Runtime

Use for final-quality COVER prompts, especially when the user reports harsh, muddy, thin, buried, painful, distorted, artificial, or unfinished output.

## Core doctrine

COVER is the final record body. It should not be a vague polish request. It should describe the production architecture that protects the song identity.

## Required quality dimensions

### Vocal
- forward, human lead vocal;
- natural breath texture restored;
- remove digital artifacts and mechanical edge;
- warm analog tube saturation on vocal bus when useful;
- vocal corridor 500Hz-3kHz protected;
- de-esser 5-8kHz;
- optional organic width such as slight detune L/R when appropriate;
- harmony stack supports rather than masks the lead.

### Low end
- mono sub-bass 20-80Hz;
- separated kick and bass center;
- sidechain bass to kick around 80ms for dance/EDM when useful;
- avoid smeared 100-250Hz bass body.

### Low-mids
- carve 200-400Hz mud;
- keep instrument body warm but not cloudy;
- prevent acoustic guitar/piano/pads from masking vocal chest.

### High-mids and air
- smooth 2-5kHz high-mids;
- control painful edge;
- controlled 8-14kHz air without brittle fizz;
- cymbals and vocal air should open the mix, not pierce it.

### Stereo and depth
- clear L/R placement;
- center reserved for lead vocal, kick, bass, and main hook elements;
- reverb and delay tails controlled;
- depth changes by section.

### Dynamics and finish
- transient punch preserved;
- bus glue compression;
- tape saturation 1-2% or master tape saturation when useful;
- loudness target matched to genre: streaming-safe -14 LUFS / -1 dBTP, or club/dance -6 to -8 LUFS only when desired.

## Placement in COVER prompt

For Genre-Transform:

```text
target genre → preserve map → substitution map → vocal identity → section events → quality stack → final/outro preservation
```

For Texture-Refine / repair:

```text
preserve identity → repair target → production quality stack → section-specific fixes → final/outro preservation
```

## Failure risks

- Quality stack too early in Genre-Transform weakens target genre identity.
- Quality stack too short produces generic polish.
- Too much air without high-mid control creates pain.
- Sub without center separation creates mud.
- Wide instruments without corridor protection bury the vocal.
