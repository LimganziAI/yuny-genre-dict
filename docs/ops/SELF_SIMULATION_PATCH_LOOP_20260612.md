# SELF SIMULATION PATCH LOOP — YUNY Runtime

## purpose
Define how YUNY uses the GitHub mirror as a working runtime to test, diagnose, and improve itself before asking the user to apply a Builder replacement package.

## premise
The GitHub repo is the active working area. GPT Builder UI remains user-applied, but Builder Instructions/Knowledge source mirrors are maintained in GitHub.

YUNY can use the repo to:
- read current runtime md files
- run simulated acceptance prompts in the current chat session
- judge the result against tests
- log failure cases
- update design docs, tests, and runtime mirrors
- prepare a Builder replacement ZIP only when the patch is stable enough

## limitation
YUNY does not run continuously in the background. A simulation loop runs when invoked in a chat session or through an explicit repo/CI mechanism.

Do not claim that unattended background testing happened unless there is an actual GitHub Action, CI run, issue, PR, or commit proving it.

## loop

### 1. Load runtime source
Read the relevant files:
- builder-runtime/instructions/current/00_INSTRUCTIONS_FULL_REPLACE_UNDER_8000.txt
- builder-runtime/knowledge/current/05_lyric_dossier_and_5000_script_engine.md
- builder-runtime/knowledge/current/06_korean_lyric_prosody_hook.md
- builder-runtime/knowledge/current/20_installation_tests_update_policy.md
- related design docs
- related tests/acceptance files
- related failure cases

### 2. Select scenario
Choose a test from acceptance tests or failure cases.

Required scenario set before release:
- Korean sentence-driven narrative lyric
- Korean phonetic/dance hook lyric
- Korean hybrid verse plus hook lyric
- user-provided lyric repair case
- Suno 8-field delivery format case
- CREATE/COVER prompt practicality case

### 3. Simulate output
Generate the output as the current runtime would produce it.

Do not skip producer judgment:
- song thesis
- macro arc
- section jobs
- lyric mode by section
- targeted gates only
- Suno delivery fields only at the end

### 4. Judge result
Evaluate the simulated output against the relevant acceptance test.

For Korean lyric tests, include:
- worst 3 line-pairs
- prose sanity check
- speaker truth check
- section function check
- hook function check
- final shift check

For Suno prompt tests, include:
- exact 8 fields
- prompt length under 1000 chars
- lyric plus cue length under 5000 chars
- positive CREATE language
- practical COVER transformation language
- EXCLUDE separation
- slider sanity

### 5. Classify failure
Use one primary failure layer:
- producer judgment failure
- macro arc failure
- lyric mode routing failure
- Korean sentence failure
- hook function failure
- cue freezing failure
- CREATE/COVER prompt failure
- format/field failure
- update-policy failure

### 6. Patch highest broken layer
Patch the highest broken layer first.

Examples:
- If macro arc is wrong, do not patch line rules first.
- If lyric mode routing is wrong, do not add more Korean grammar checks first.
- If CREATE/COVER wording is bloated, patch prompt doctrine before EXCLUDE.

### 7. Re-run targeted simulation
Run the same scenario again after patching.

A patch is not promotion-ready unless the failure case improves without breaking the other required test types.

### 8. Promote to Builder mirror
Only after tests pass, update:
- builder-runtime/instructions/current/...
- builder-runtime/knowledge/current/05...
- builder-runtime/knowledge/current/06...
- builder-runtime/knowledge/current/20...

### 9. Prepare deployment package
Only create a ZIP when the Builder mirror is coherent and the user needs to apply it.

## output policy
When reporting to user, keep it short:
- what was tested
- what failed
- what changed
- what still needs Builder replacement
- commit SHAs

## status
Operational loop defined. Next step is to implement the first simulation matrix and then promote stable changes into Builder runtime mirrors.
