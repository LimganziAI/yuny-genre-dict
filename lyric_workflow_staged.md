# lyric_workflow_staged.md — STAGE 0-10 운영 전문
경로 후보: `knowledge-evolving/lyric-expression-banks/lyric_workflow_staged.md`
카드 05 STAGE 파이프라인의 풀바디 — 단계별 질문/추정/출력금지 규칙.

| STAGE | 내용 | 사용자 질문 | 출력 규칙 |
|---|---|---|---|
| S0 | Mode·risk lock (card 01) | 모드 모호 시 1회만 | 8필드 금지 |
| S1 | Research Brief — 조사 항목 식별+웹 검증(현행 어법/장면 어휘/장르 관습) | 질문 없음(조사로 해결) | 8필드 금지 |
| S2 | Speaker card·어미 팔레트·object bank (card 06/07) + 샘플 10줄 | 화자 핵심값 충돌 시 1회 | 8필드 금지 |
| S3 | Hook thesis + 곡형/BPM/음절 grid | 추정+1줄 표기 | 8필드 금지 |
| S4 | Draft (곡 언어로, 한 호흡 금지 — 섹션별) | 없음 | 8필드 금지 |
| S5 | R1 의미·서사 (아크/왜 지금/화자 동기) | 서사 분기 진짜일 때 1회 | 8필드 금지 |
| S6 | R2 언어·말투 (팔레트/일상어/조어/메타/산문 sweep) | 없음 | 8필드 금지 |
| S7 | R3 운율·가창 (BPM×음절/peak/열린모음/소리내 읽기) | 없음 | 8필드 금지 |
| S8 | Cue pass (card 08 — 가사 동결 후) | 없음 | **LYRIC만 출력 가능 지점** (LYRIC-CRAFT 종료점 / STAGED-FULL 중간 확인 요청 시) |
| S9 | CREATE/COVER build (card 03/09/11/14/15) | 진짜 분기 2-3안일 때만 | 8필드 금지 |
| S10 | EXCLUDE/SLIDERS + 정합성 감사 + 실측 글자수 | 없음 | **여기서만 8필드** |

정합성 감사(S10): 가사↔CREATE(보컬 anchor 동기화, 컨투어↔큐), 가사↔COVER(이벤트 큐↔substitution), EXCLUDE↔딜리버리(rap lockout 등), SLIDERS↔모드. 불일치 1개 = S9 회귀.
복귀 규칙: 가사 승인(명시 or 무지적 진행) 후에만 S9-10. LYRIC-REPAIR는 S2-S8 루프만 돈다. LYRIC-LOCK은 S8부터 시작(가사 동결 상태).
질문 총량: 전 파이프라인에서 최대 2회 — 그 외 전부 추정+1줄 표기. 질문 남발 = 결함, 질문 0회로 오답 = 더 큰 결함.
