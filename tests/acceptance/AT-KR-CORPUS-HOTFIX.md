# AT-KR-CORPUS-HOTFIX — Korean Lyric Corpus Hotfix Acceptance

## AT-KR-CORPUS-01
Input: "한국어 가사 써줘. 맥락 사람답게. 큐까지."
Pass:
- no 8-field if request is system/audit
- if song route, internal order is speaker→monologue→hook→lyric→cue
- no stock convenience store/cafe/neon/stars unless user supplied
- cue does not substitute for lyric meaning

## AT-KR-CORPUS-02
Input: "가사 별로야. 한국말 같지 않아."
Pass:
- route LYRIC-REPAIR first, not fresh 8 fields
- classify failure: speaker / handoff / register / ending / context / cue
- repair only failed axis
- final lyric survives strip-cue test

## AT-KR-CORPUS-03
Input: "가사 5000자 안에 큐랑 같이."
Pass:
- no padding to target length
- lyrics+cues <= 5000 measured
- cue pass after lyric pass
- section tags and [Singing:] are render instructions, not content

## AT-KR-CORPUS-04
Input: "자료 참고해서 한국 맥락으로."
Pass:
- uses structural corpus mode
- source lines are not quoted/transplanted
- produces object bank from user scene, not generic defaults
- V2 and Final carry changed defense/meaning
