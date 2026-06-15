# SIM-20260612 TEAM CORPUS REVERSE BRIEF ROUND 1

## purpose
Focus only on lyric craft: description quality, vocabulary, scene construction, speaker posture, hook function, and whole-song movement.

## baseline
The user team corpus is the primary quality baseline. K-pop corpus is secondary calibration for repetition, hook cell, and section compression.

## representative craft lanes observed

### Lane A — relational metaphor lyric
Craft pattern:
- one central relational metaphor
- simple repeated identity line
- short line length
- high repeat ratio
- emotional clarity through orbit, distance, pull, or asymmetry

Reverse brief shape:
```text
A speaker describes an unequal relationship through one stable metaphor. V1 names the other person's gravity. Pre admits involuntary pull. Chorus fixes the metaphor. V2 shows social evidence. Bridge admits the pattern is old. Final repeats with clearer self-knowledge.
```

YUNY risk:
- over-explaining the metaphor
- adding unrelated pretty images
- making final chorus a raw repeat

### Lane B — rooftop / threshold confession
Craft pattern:
- small physical distance stands for emotional inability
- repeated measure words such as one step, one word, one beat
- scene object is functional: stair, door, rail, wind, edge
- chorus repeats the failed action

Reverse brief shape:
```text
A speaker reaches the place where confession should happen but cannot cross a small threshold. Each section turns physical distance into emotional delay.
```

YUNY risk:
- making the scene melodramatic
- adding stock night images
- losing the exact bodily action

### Lane C — comic character ego hook
Craft pattern:
- first-person character entrance
- short boastful lines
- repeated catchphrase
- social setting reacts to the speaker
- hook works as identity slogan

Reverse brief shape:
```text
A self-involved character enters a familiar space and turns ordinary reactions into proof of greatness. The hook repeats the character's own myth.
```

YUNY risk:
- making the boast generic
- flattening voice into explanation
- losing spoken timing

### Lane D — domestic anxiety / seasonal comfort
Craft pattern:
- concrete room, object, temperature
- gentle second-person reassurance
- longer line length
- low-to-medium repeat
- chorus acts as care statement

Reverse brief shape:
```text
A speaker uses one warm domestic object to hold another person's cold or tired feeling. V2 slightly changes the object's appearance, showing time passing.
```

YUNY risk:
- using generic comfort phrases
- overusing uplift language
- not letting objects change across sections

### Lane E — heat/cold comic romance
Craft pattern:
- emotional temperature is literalized
- call-and-response, ad-lib, exclamation
- sickness or body symptom becomes romantic diagnosis
- hook is loud, direct, and performative

Reverse brief shape:
```text
A speaker turns the other person's mixed signals into a physical fever/cold joke. The chorus names the condition as a comic emergency.
```

YUNY risk:
- making it too poetic
- losing punchline timing
- weak body symptom vocabulary

### Lane F — action / city swipe hook
Craft pattern:
- urban motion
- hand action and speed
- English trigger phrases
- chorus turns skill into kinetic identity
- objects appear as targets, proof, or traces

Reverse brief shape:
```text
A fast character moves through the city and treats every object as a beat or target. Hook identity comes from one repeated action verb.
```

YUNY risk:
- tag-dumping action words
- losing action verbs
- making objects decorative

### Lane G — minimal threshold / chant lyric
Craft pattern:
- very short lines
- repeated command/action
- low explanation
- body and space words carry energy
- chant works by reduction

Reverse brief shape:
```text
A speaker at a threshold reduces thought into breath, floor, door, name, and step. The lyric works by minimal repeated action.
```

YUNY risk:
- applying narrative prose standards and overfilling
- making the chant vague without physical anchors

## team baseline rule extracted
Good team-level lyrics usually have:

1. a prompt-recoverable situation
2. a distinct speaker posture
3. object-action coupling
4. one hook identity
5. V2 angle change
6. final stance or function shift
7. scene-born metaphor
8. mode-specific repetition

## runtime patch implication
YUNY 05/06 must include a lyric-craft quality pass before Suno field packaging:

```text
CRAFT PASS:
- situation recoverable?
- speaker posture visible?
- object-action coupled?
- hook identity named?
- V2 changed angle?
- final shifted?
- metaphor scene-born?
- repetition mode-specific?
```

## status
Round 1 reverse brief simulation complete. Next: promote craft pass into 05/06 runtime mirror and run generation simulation from one lane.
