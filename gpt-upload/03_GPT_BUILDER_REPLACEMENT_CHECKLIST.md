# GPT Builder Replacement Checklist

## Instructions

- [ ] Open `_GPT_BUILDER_UPLOAD/00_COPY_TO_GPT_INSTRUCTIONS_FINAL.txt`
- [ ] Select all
- [ ] Replace current GPT Instructions
- [ ] Save

## Knowledge

Recommended:

- [ ] Delete/replace the old 20 knowledge files
- [ ] Upload all 20 files from `_GPT_BUILDER_UPLOAD/knowledge-upload-set-20-files-recommended/`

Optional:

- [ ] Upload `_GPT_BUILDER_UPLOAD/optional-extra-knowledge-bridge/00_GITHUB_BRIDGE_FOR_GPT_KNOWLEDGE.md` only if extra knowledge files are allowed

## GitHub connector

- [ ] Connect repo `playwithlawkr/yuny-suno-os`
- [ ] Confirm the GPT can fetch files from the repo
- [ ] Test with a system audit request:
  “GitHub OS 연결 상태 점검해줘”
- [ ] Test with a genre request that uses `knowledge-evolving/genre-dictionary/index/GENRE_INDEX.md`

## First regression tests

1. “Tech Para / テクパラ CREATE+COVER 만들어줘”
2. “가사큐가 약해. 듀엣 구분 살려서 다시 진단해줘”
3. “COVER가 보컬이 묻히고 하이가 아파. 기존 멜로디 보존해서 고쳐줘”
4. “내 결/99 케이스 기반으로 시스템 흐름 점검해줘”
