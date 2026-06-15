# NIKL CONTEXT INFERENCE ENGINE — 맥락 복원 게이트

대상 자료:
- NIKL_CI_2024 / NIKL_CI_2025: 대화에서 원인·동기·전제·반응·후속 사건을 추론하는 구조
- NIKL Cooperative Dialogue Summary Corpus: 대화의 topic/sub-topic/main summary/reference sentence 구조

## 가사 적용
가사 한 줄은 혼자 예쁘면 안 된다. 다음 중 하나를 반드시 이어받아야 한다.

- cause: 그래서 왜 그런 말을 하는가
- prerequisite: 그 말을 가능하게 만든 전제는 무엇인가
- motivation: 화자는 무엇을 얻으려는가
- reaction: 상대/몸/공간이 어떻게 반응했는가
- subsequent event: 그래서 다음 행동이 무엇인가

## 맥락 흐트러짐 검수
인접 2행을 바꿔도 의미 손실이 없으면 조립 가사다.
섹션을 바꿔도 같은 말을 하면 section pressure가 죽은 것이다.
Bridge 뒤 Final이 같은 뜻이면 raw paste다.

## 적용 위치
S4 carving 뒤, S5 meaning pass 전에 실행한다.
