# SIM-20260612-KR-BUS-SEARCH-ROUND1

## scenario
Korean indie R&B, 92 BPM, close-mic male vocal. After work, last bus, speaker sees a stop name tied to an ex, thinks the number was deleted, but search behavior returns.

## tested against
- AT-KR-PLAIN-SENTENCE-SANITY
- AT-KR-MACRO-ARC-LYRIC-COHERENCE
- AT-KR-HYBRID-SECTION-ROUTING where applicable
- practical Suno CREATE/COVER runtime

## current failing pattern
The old output looked like a complete Suno package but failed the record.

## round 1 judgment

### 1. sentence comprehension
Fail.
Some adjacent line-pairs were not natural Korean prose. Subject-predicate relations and physical action handoff were unclear.

### 2. macro arc
Fail.
The song had a premise but no earned movement. V1 placed objects instead of establishing the speaker's behavior. V2 did not reveal enough new angle. Bridge explained the thesis rather than changing the speaker's defense.

### 3. section function
Fail.
Sections existed, but their jobs were weak:
- V1 should show the speaker trying to stay ordinary.
- Pre should show the hand/search behavior beginning before the speaker admits it.
- Chorus should make the central contradiction memorable.
- V2 should disclose that deletion did not remove memory because the body retained sequence.
- Bridge should shift from blaming the phone/contact to admitting intention.
- Final should change from stopping by accident to stopping as a conscious defense.

### 4. metaphor / creative expression
Fail.
The lyric was too literal in some places and accidentally strange in others. Metaphor did not grow from action. Good metaphor candidates should come from bus movement, stop announcements, thumb sequence, search field, screen light, route passing, door closing, or card tap residue, not from decorative stock imagery.

### 5. hook function
Partial.
`지운 줄 알았는데 / 또 네 이름부터 쳤어` has a usable central contradiction, but it needs more natural surrounding lines and a final chorus shift.

### 6. CREATE/COVER prompt
Partial.
CREATE contained useful production descriptors but may overpack. COVER used redundant target-language and should be shorter: preserve/change map only.

## repaired macro arc candidate
SONG THESIS: The speaker did not fail because the number remained; he failed because the route through the body remained.

LISTENER JOURNEY: ordinary commute → involuntary recognition → self-excuse → body memory revealed → conscious non-action → residue.

MACRO ARC:
- Opening: speaker boards as if this is just a commute.
- V1: stop name interrupts the ordinary ride.
- Pre: search behavior begins before intention is admitted.
- Chorus: deleted contact returns as typed name or hand sequence.
- V2: phone is not the archive; the body is.
- Bridge: speaker stops blaming accident/time/checking.
- Final: not pressing call becomes a chosen defense, not a victory.
- Outro: screen is closed, but the hand remains delayed.

## repaired section mode map
- V1: narrative prose lyric, grounded observation
- Pre: narrative pressure, shorter breath
- Chorus: sentence hook, repeatable confession
- V2: narrative disclosure
- Bridge: direct spoken self-recognition
- Final: same hook shape with changed stance
- Outro: minimal action residue

## required runtime patch
Promote macro arc and section-job requirement before lyric drafting. Plain Korean sanity alone is not enough.

## status
round 1 diagnosis complete. Needs runtime patch and round 2 lyric simulation.
