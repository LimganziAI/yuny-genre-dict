# PALETTE_SCHEMA — [VOICE]/[LORE] 분리 표준 (lore 누설 구조 차단)
모든 캐릭터 파일은 두 블록으로 분리한다. **기본 fetch = [VOICE] 블록만.** [LORE]는 사용자가 "캐릭터 세계관으로/걔 설정대로"를 명시 호출할 때만 적재 — 읽힌 lore는 "무시" 선언과 무관하게 생성을 오염시킨다(C-20260611-01 #1).

## [VOICE] 필수 필드 (음성 물리만)
gender/age-band · range+money zone(편안 음역과 최강 구간) · timbre/weight(thin~thick) · posture(chest/mix/head/belt/breathy…) · release behavior(held/flip/breath-tail/straight…) · stamina/주의(벨트 과적 리스크 등) · language/딕션 특성 · 어울리는 장르 존 2-3 · Suno 디스크립터 변환 예 1줄
## [LORE] (격리 블록)
역할·세계관·장면 연상·관계 — **이 블록의 명사는 INTENT LOCK 허용군에 없으면 가사·필드 진입 금지**(19 장면명사 대조).
## 운용
이름은 라우팅 키 — Suno 필드 진입 금지, 디스크립터로 변환. 동일 캐릭터 반복 시 [VOICE] 핵은 보존하고 장르·그루브·레지스터·섹션 역할을 회전.
