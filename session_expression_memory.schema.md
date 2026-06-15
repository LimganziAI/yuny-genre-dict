# session_expression_memory.schema.md — 세션 표현 장부
경로 후보: `schemas/session_expression_memory.schema.md`
카드 05 originality guard ↔ 카드 18 ledger의 스키마. 곡 1개 완성 = 1엔트리. 다음 곡 draft 전 대조.

```yaml
song_ref:            # 제목/케이스 ID
core_objects:        # 핵심 사물 5-8 (예: 빙수, 스푼, 연유, 진동, 냅킨)
emotion_verbs:       # 감정을 진 동사들 (예: 녹다, 쥐다, 내려놓다)
hook_structure:      # 후렴 구조 한 줄 (예: "선호 고백 → 반대 선택" 대구)
ending_pattern:      # 어미 팔레트 + 빈출 어미
ending_image:        # 마지막 이미지 (예: 자국만 남는 그릇)
```

대조 규칙: 새 곡이 직전 N곡(기본 3)과 5축 중 **어느 한 축이라도 30%+ 겹치면** 그 축 재작성. "녹다"가 두 곡 연속 감정 동사면 세 번째 곡에서는 금지어. 엔딩 이미지 중복은 0% 원칙(한 세션에서 같은 끝그림 두 번 금지).
