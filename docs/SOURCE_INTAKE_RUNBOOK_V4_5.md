# YUNY Source Intake Runbook — v4.5 RC

## Purpose
User-supplied research material should become YUNY-usable craft material without forcing the user to manually curate every file.

The goal is not to copy source sentences. The goal is to convert sources into:
- lyric mode evidence
- Korean register and diction gates
- poetic/image-function gates
- translationese detectors
- K-pop line/section/repetition priors
- Suno CREATE/COVER prompt patterns
- cue/render behavior tests
- failure-case diagnostics

## User-side workflow

1. Put files or URLs in a folder or a `urls.txt`.
2. Run:

```bash
python tools/yuny_source_intake_packager.py prepare ./SOURCE_FOLDER --out ./yuny_intake --max-mb 450
```

or:

```bash
python tools/yuny_source_intake_packager.py prepare urls.txt ./SOURCE_FOLDER --out ./yuny_intake --max-mb 450
```

3. Upload these first:
- `yuny_intake/manifest.csv`
- `yuny_intake/manifest.jsonl`
- `yuny_intake/YUNY_SOURCE_INTAKE_REPORT.md`
- `yuny_intake/upload_batches/yuny_upload_batch_001.zip`

4. Upload original large archives only when YUNY asks for targeted inspection.

## YUNY-side workflow

1. Read manifest first.
2. Classify material by use:
   - lyric-craft / literature / poetry / dialogue / corpus / K-pop analytics / translation / Suno metadata / music theory / production / tool
3. Extract function, not wording.
4. Promote only stable findings:
   source observation → case → pattern-candidate → support doc → knowledge addendum → instructions only if routing changes.
5. Never claim live Project update until the user applies the package.

## Large-file rule
If one file exceeds upload limits, split it outside ChatGPT or upload the manifest first. YUNY should not require whole-corpus ingestion when a manifest and samples are enough to derive gates.

## Protected-text rule
Protected poems, lyrics, fiction, and corpora are not output text. They are only evidence for:
- how images function
- how register shifts
- how repetition works
- how line breaks carry pressure
- how translation sacrifices literal meaning for singability
- how Korean syllables and endings behave in lyric contexts
