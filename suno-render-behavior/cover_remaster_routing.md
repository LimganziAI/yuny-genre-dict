# Cover vs Remaster 라우팅
- **Cover** [공식]: 소스 오디오를 조건으로 멜로디·구조를 유지하며 스타일 재해석 — 우리의 2-pass 최종 공정. 모드 a(동장르 refine: 음질·밀도·보컬 전진) / 모드 b(장르 transform: 스킨 교체, 베이스 음질은 CREATE 책임).
- **Remaster** [공식]: 편곡 불변, 음질만 끌어올림 — "다 좋은데 소리만 좋아지면 돼"일 때의 정답. preserve/substitution 맵 불필요.
- 라우팅 질문 1개: **편곡·텍스처를 바꾸고 싶은가?** No → Remaster. Yes → Cover(a/b 판정 → AI 결정표).
- 흔한 오용: 음질 불만에 Cover 재프롬프트 반복(텍스처가 미세 표류) — Remaster가 정답인 케이스.
