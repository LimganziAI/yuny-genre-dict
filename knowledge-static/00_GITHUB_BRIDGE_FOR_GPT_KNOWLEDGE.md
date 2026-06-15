# YUNY GitHub OS Bridge for GPT Knowledge

Use this file to connect the stable 20-file GPT Knowledge pack with the GitHub repository:

`playwithlawkr/yuny-suno-os`

This file is a routing bridge, not a replacement for the 20 core knowledge files.

---

## 1. Canon stack

Resolve conflicts in this order:

1. User goal, safety, legal boundaries
2. GPT Instructions
3. Current 20 GPT Knowledge files
4. This bridge
5. GitHub evolving knowledge and cases
6. Conversation context

GitHub is the living memory and update layer. It is not the highest authority.

---

## 2. Repository map

```text
instructions/                  paste-ready GPT instruction patches
gpt-upload/                    GPT Builder copy/upload files
docs/                          workflow, storage policy, update governance
knowledge-static/current-20/    stable GPT knowledge mirror
knowledge-evolving/
  genre-dictionary/             full genre dictionary + index
  kpop-artist-dna/              K-pop / artist / producer / vocal DNA
  reference-dna/                reference cards and sonic moment breakdowns
  prompt-patterns/              CREATE/COVER, lyric cue, exclude, slider patterns
cases/
  success/                      outputs that worked and why
  failure/                      failed outputs, diagnosis, corrected pattern
  neutral-observations/         observations not yet promoted
schemas/                       case and pattern schemas
tests/                         regression gates and prompt QA
vault/operator-private/         99 memory files and session logs
archive/                       migrated source material, not current routing
```

---

## 3. Activation triggers

Use this bridge when the user asks for or implies:

- system/package improvement
- GitHub workflow or repository use
- genre dictionary lookup/update
- K-pop / artist / producer DNA management
- reference card reuse
- repeated success/failure memory
- weak lyric cues
- final quality improvement
- audio/COVER quality repair
- adding a new genre, case, pattern, or SOP
- checking whether knowledge routing is working

For ordinary one-off songwriting, use GitHub only if the task needs evolving, large, or exact external material.

---

## 4. Fetch protocol

When using GitHub:

1. Fetch index first.
2. Fetch only 1 to 3 targeted entries/cards/cases.
3. Convert retrieved material into craft decisions.
4. Do not paste long source text into normal song outputs.
5. Mention repository work only in system/package audits or when user asks.
6. Never claim a file was fetched, checked, or updated unless it actually was.

---

## 5. Genre workflow

```text
genre request
→ genre index
→ exact slug
→ adjacent slug
→ fallback DNA
→ prompt encoding
→ result feedback
→ case if useful
```

Never rely on a broad macro genre alone when a specific microgenre or scene anchor can be found.

If exact genre entry is missing, use adjacent DNA and record the gap if likely to recur.

---

## 6. K-pop / artist DNA workflow

Artist names and song references are analyzed into craft variables.

Extract:

- vocal role and range
- timbre and delivery
- groove and rhythmic behavior
- arrangement density
- instrument substitution habits
- hook structure
- production texture
- safe decomposed signature language
- failure risks

Final prompts should encode craft variables rather than copying melodies, lyrics, samples, or protected arrangement.

---

## 7. Failure workflow

```text
failure signal
→ classify failure type
→ lock what worked
→ search similar cases if useful
→ route upstream
→ rebuild full output
→ record/update case if useful
```

Common failure routes:

- weak lyric cue: 03 + 16 + language lyric file + cases
- thin lyric: language lyric file + 16 + 17 + cases
- bad COVER quality: 19 → 02 + 05 + 06 + cases
- generic genre: 07 + GitHub genre dictionary + reference DNA
- weak final polish: 05 + 06 + prompt pattern cases
- singer confusion: 03 + 12 + cue cases
- ending failure: 03 + 11 + 19 + cases

---

## 8. Success workflow

When the user reports that something worked:

1. Save what was preserved.
2. Save the prompt/lyric/cue pattern if available.
3. Identify the transferable principle.
4. Do not over-promote from one success.
5. Promote only after repetition.

---

## 9. 99 memory workflow

`99_OPERATOR_VAULT.md` and `99z_SESSION_LOG.md` are on-demand memory files.

Use them when:

- user invokes “내 결”
- a case number is mentioned
- a named character/pattern is invoked
- user asks to restore Claude-era workflow
- system audit requires migration analysis

Do not auto-apply 99 memory to neutral users.

---

## 10. Promotion ladder

```text
observation
→ case
→ repeated pattern
→ knowledge patch
→ instruction patch
```

A single case does not become a global rule. A repeated cross-context pattern may become a knowledge patch. Only high-level workflow changes become instruction patches.

---

## 11. Output discipline

For normal music work, do not explain this bridge. Use it silently.

For system audits, package updates, or repository work, explain:

- what was checked
- what was changed
- what remains incomplete
- what should be used in GPT Instructions or Knowledge
