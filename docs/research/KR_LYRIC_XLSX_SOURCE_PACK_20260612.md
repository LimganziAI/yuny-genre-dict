# KR Lyric Source Pack — XLSX Ingestion Map

## purpose
This file ingests the uploaded `한국어_작사_작문_AI_자료수집_팩.xlsx` as a routing map, not as a pile of raw text.
The material must feed system gates: draft origin, speech-act hook, Korean morpheme/register, phoneme singability, K-pop form, human-AI revision, and source-grounded tests.

## roadmap distilled
|축|핵심 질문|수집/학습 대상|AI 작사·작문에 바로 연결하는 법|
|---|---|---|---|
|한국어 음운·발음·가창성|이 문장이 노래로 불릴 때 자연스러운가?|음절 구조, 받침, 모음, 끊어읽기, 고음/빠른 구간 발화성|고음은 열린 모음, 빠른 구간은 받침 충돌 최소화, 1줄 음절 수를 제한|
|K-pop 노랫말 운율|실제 K-pop은 문장을 어떻게 리듬화하는가?|후렴 반복, 훅, 영어 코드전환, 세대별 가사 길이/어휘 변화|AI에게 섹션별 기능(verse/pre/pre-chorus/hook)을 명확히 부여|
|한국어 창작·문학|테마와 분위기를 한국어 장면으로 어떻게 그리는가?|시, 소설, 산문, 상징, 계절감, 공간감, 관계의 미묘함|감정어 대신 장면·사물·시점·시간대·거리감을 입력|
|한국어교육 쓰기 연구|AI가 초안·피드백·재구성을 어떻게 도울 수 있는가?|쓰기 피드백, 읽기-쓰기 통합, 질문 생성, 과정 중심 글쓰기|초안 생성 → 사람의 구조 수정 → AI 재생성 → 발화성 점검 루프|
|AI 창작·공동창작|AI를 작가가 아니라 어떤 도구로 써야 하는가?|Human-AI co-creation, lyric generation, multimodal inspiration|AI를 초안 생성기·변형 엔진·검토자·대안 제안자로 분업|
|한국문화·자료원|한국적 정서와 어휘 감각은 어디서 확보할까?|모두의 말뭉치, AI Hub, 고전/근현대 텍스트 DB, 문학 목록|참고 텍스트를 분석해 어휘장·장면장·정서 코드를 만든 뒤 프롬프트에 투입|

## prompt/checklist distilled
|용도|프롬프트 템플릿|후처리 체크|
|---|---|---|
|한국어 가사 초안|한국어 K-pop 가사 초안을 써줘. 장르는 [장르], BPM 느낌은 [느림/중간/빠름], 정서는 [정서], 장면은 [장소/시간/사물], 화자는 [1인칭/관찰자/회상형]. Verse 1은 장면 제시, Pre-chorus는 감정 상승, Chorus는 4줄 반복 훅. 한 줄 6~8음절 중심, 영어는 10% 이하, 직접적인 사랑/이별 단어는 피하고 사물과 행동으로 표현해.|음절 수, 받침 충돌, 후렴 반복 가능성, 추상어 비율 점검|
|문학적 장면 묘사|아래 테마를 한국어 산문/시적 장면으로 바꿔줘. 감정어를 직접 쓰지 말고, 시간대·공간·빛·소리·냄새·거리감·사물로 보여줘. 문장은 짧게, 은유는 과하지 않게. 테마: [테마]. 장면: [장면]. 금지어: [금지어].|감정 단어를 사물/행동으로 바꿨는지 확인|
|후렴 훅 만들기|아래 장면에서 반복 가능한 한국어 후렴 훅 10개를 만들어줘. 조건: 4~7음절, 열린 모음이 많은 단어 우선, 받침이 연속으로 부딪히는 표현 제외, 기억하기 쉬운 반복 구조, 과한 영어 금지. 장면: [장면]. 정서: [정서].|소리 내어 읽고 고음에서 입이 열리는지 확인|
|AI 재작성|이 가사를 의미는 유지하되 3가지 버전으로 바꿔줘. 1) 더 구어적인 버전, 2) 더 문학적인 버전, 3) 노래로 부르기 쉬운 버전. 각 줄마다 음절 수를 표시하고, 발음이 어려운 지점을 지적해줘.|버전별 장단점 비교 후 혼합|
|한국적 정서 강화|아래 가사/문장을 한국적 계절감과 장소감이 느껴지도록 바꿔줘. 단, 전통 소재를 억지로 넣지 말고 일상 사물, 거리, 날씨, 관계의 미묘한 거리감으로 표현해. 원문: [원문].|클리셰 전통어휘 남발 여부 확인|
|구조 분석|아래 가사를 Verse/Pre/Chorus/Bridge로 나누고 각 섹션의 기능, 정서 곡선, 반복어, 이미지, 발음 리스크를 표로 분석해줘. 이후 개선안을 제시해줘.|분석 결과를 다음 프롬프트 조건으로 재투입|

## source list
|분류|제목|상세/서지|URL/위치|왜 필요한가|접근|우선순위|
|---|---|---|---|---|---|---|
|핵심|첨부 메모|사용자 첨부 메모: 한국어 작사/작문/문학/AI 창작 자료 축|현재 대화 첨부|이미 모은 참고문헌·분류축·프롬프트 방향의 기준점|첨부파일|내부|
|작사·운율|서근영, K-Pop 노랫말의 운율구조 변화 현상: 댄스음악을 중심으로|한국엔터테인먼트산업학회논문지 14(7), 343-362, 2020|https://dl.nanet.go.kr/detail/KINX2021007992|K-pop 댄스음악 노랫말 운율 구조 변화를 분석. 음절·리듬·후렴 설계의 핵심 자료|국회도서관/KCI|상|
|작사·운율|서근영, 이중언어 사용자와 K-Pop 노랫말 딕션과의 연관성|한국엔터테인먼트산업학회, 13(8):267-280, 2019|국회도서관 논문 참고문헌 내 확인|영어/한국어 혼용, 재미교포 힙합가수 딕션, K-pop 발화성 참고|논문DB 검색 필요|중|
|작사·운율|서근영, K-Pop 딕션 변화 연구: 빌보드 진입 가수의 딕션을 중심으로|경희대학교 대학원 박사학위논문, 2020|국회도서관 논문 참고문헌 내 확인|빌보드 진입 K-pop 가수의 발음·딕션 변화 연구. 글로벌 발화 전략 참고|RISS/국회도서관 검색 필요|중|
|작사·언어혼종|박준언, K-Pop 노랫말들의 언어 혼종: 영어 변이형들과 코드전환 사용|이중언어학회, 61:95-124, 2015|국회도서관 논문 참고문헌 내 확인|한국어 가사 안에서 영어 변이형/코드전환을 어떻게 쓰는지 분석|논문DB 검색 필요|중|
|K-pop 분석|디지털 미디어 환경 변화에 따른 케이팝 가사의 언어적 특성|KCI 등재 논문|https://dspace.kci.go.kr/handle/kci/2241691|세대 변화에 따라 곡 길이 감소, 영어 가사 증가, 어휘 다양성 확대 등을 분석|KCI DSpace|상|
|K-pop 분석|이승연·장민호, K-pop 음악의 글로벌 성공 요인 분석|한국엔터테인먼트산업학회, 13(4):1-15, 2019|국회도서관 논문 참고문헌 내 확인|가사만이 아니라 글로벌 성공 요인을 맥락화할 때 참고|논문DB 검색 필요|중|
|대중가요사|장유정, 대중가요 작사가 금능인의 생애와 작품 세계|KCI 논문, 2011|https://dspace.kci.go.kr/handle/kci/1716770|한국 대중가요 작사가의 작품 세계와 가사 특징을 역사적으로 보는 자료|KCI DSpace|상|
|AI 한국어 쓰기|생성형 AI를 활용한 한국어 쓰기 피드백 방안|ChatGPT와 한국어 교사의 쓰기 피드백 비교, KCI 2024|https://dspace.kci.go.kr/handle/kci/2200708|언어·내용·구조·정의적 피드백에서 AI/교사 역할 분업을 볼 수 있음|KCI DSpace|상|
|AI 한국어 수업|생성형 AI를 활용한 한국어 수업 방안: 읽기와 쓰기 능력 향상을 중심으로|DBpia 학술논문|https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE12017019|수준별 맞춤 텍스트, 즉각 피드백, 창의적 표현 확장 사례|DBpia|상|
|AI 작문교육|챗GPT가 바꾸어 놓은 작문교육의 미래: 인공지능 시대, 작문교육의 대응|DBpia 학술논문|https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11604440|AI 시대 글쓰기 역량: 질문 생성, 메타적 읽기, 출처 확인, 회귀적 쓰기|DBpia|상|
|AI 작문교육|ChatGPT 글쓰기 표절 대응과 교육적 활용 전략|국어교육연구, DBpia|https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11440191|AI 표절 우려를 단순 금지가 아니라 과제 설계와 교육 전환으로 다루는 자료|DBpia|상|
|AI 대학글쓰기|생성형 AI 시대의 대학 글쓰기 교육 방향|논증적 글쓰기에서 생성형 AI 사용 가능성 탐색|https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11827304|AI를 글쓰기 사고·표현 과정의 조력자로 배치하는 관점|DBpia|상|
|AI 교육 일반|생성형 AI의 교육적 활용 방안 연구: ChatGPT 활용을 중심으로|정보교육학회논문지 27(6), 691-704, 2023|https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11774459|교육 현장에서 생성형 AI 활용 실태·인식·활용 방안|DBpia|중|
|AI 인식|Chat GPT 활용 수업을 통한 대학생의 생성형 AI에 대한 인식 및 자기주도학습 역량 변화|DBpia/교보문고스콜라|https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11741767|AI 활용 전후 학습자 인식 변화를 보여주는 참고 자료|DBpia|중|
|AI 질문생성|생성형 인공지능은 교사의 교육적 질문 생성 역할을 대신할 수 있는가|새국어교육 136, DBpia|https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11728440|텍스트 해석 질문 생성에서 인간/AI 차이를 보는 자료. 창작 프롬프트 질문 설계에 응용|DBpia|중|
|AI 공동작곡|Amuse: Human-AI Collaborative Songwriting with Multimodal Inspirations|arXiv 2412.18940 / CHI 2025|https://arxiv.org/abs/2412.18940|이미지·텍스트·오디오 영감을 코드 진행으로 바꾸는 인간-AI 공동작곡 시스템|arXiv|상|
|AI 공동작곡|Amuse Project Page|KAIST/CMU 프로젝트 페이지|https://yewon-kim.com/amuse/|논문·코드·데모를 함께 확인 가능. 멀티모달 영감→음악 구조 흐름 참고|Project page|상|
|AI 공동작곡|Amuse 공식 구현 GitHub|Official Implementation|https://github.com/elianakim/Amuse|코드 진행 생성 방법과 데이터/모델 구조 확인|GitHub|상|
|AI 공동작곡|KAIST 어뮤즈 보도|헬로디디, 2025.05|https://www.hellodd.com/news/articleView.html?idxno=107813|텍스트·이미지·오디오 입력을 화성 구조로 바꾸는 창작자 중심 AI 설명|기사|중|
|AI 가사 생성|Youling: an AI-Assisted Lyrics Creation System|arXiv 2201.06724, 2022|https://arxiv.org/abs/2201.06724|한 번에 생성이 아니라 후보 선택·수정·속성 제어를 지원하는 인간 중심 가사 생성 시스템|arXiv|상|
|AI 가사 생성|Rhyme-aware Chinese lyric generator based on GPT|arXiv 2408.10130, 2024|https://arxiv.org/abs/2408.10130|가사 생성에서 라임 정보의 중요성을 모델에 통합. 한국어 운율 설계에도 참고|arXiv|중|
|멀티모달 텍스트|Language Models Can See: Plugging Visual Controls in Text Generation|arXiv 2205.02655|https://arxiv.org/abs/2205.02655|이미지 기반 텍스트 생성/스토리 생성. 장면 사진→가사/시/산문 프롬프트에 응용|arXiv|중|
|생성형 AI 개관|A Comprehensive Survey of AI-Generated Content|arXiv 2303.04226|https://arxiv.org/abs/2303.04226|AIGC 전체 흐름과 텍스트·이미지·멀티모달 생성 개관|arXiv|중|
|한국어 말뭉치|국립국어원 모두의 말뭉치|국립국어원 언어자원|https://kli.korean.go.kr/corpus/|한국어 텍스트·대화·요약 등 AI/언어 연구용 자원. 어휘장/문체 분석용|공공자원|상|
|한국어 말뭉치|국립국어원 2026년 1분기 말뭉치 공개 보도자료|대화 맥락 추론·요약 말뭉치 등 신규 언어자원 공개|https://korean.go.kr/front/board/boardStandardView.do?b_seq=1046&board_id=6&mn_id=183|AI가 한국어 맥락 이해와 추론 능력을 높일 수 있는 자원|공공자원|상|
|한국어 데이터|AI Hub 한국어 말뭉치 데이터|문어체·구어체 한국어 말뭉치 데이터 패키지|https://aihub.or.kr/aihubdata/data/view.do?aihubDataSe=dataPckage&currMenu=511&dataPckageSn=1&topMenu=100|문어/구어 한국어 데이터. 문체·구어성·대화성 분석에 사용 가능|공공데이터|상|
|한국 고전/문화|한국고전종합DB|한국고전번역원 제공 고전 원문·번역문 검색|https://db.itkc.or.kr/|한국적 정서, 고전 어휘, 시적 이미지, 역사/인물/공간 코드 추출|공공자원|상|
|한국 고전/문화|규장각 원문검색서비스|서울대 규장각한국학연구원|https://kyudb.snu.ac.kr/|고도서·고문서·고지도 등 한국 문화 장면화의 1차 자료|공공자원|상|
|한국학|한국학 디지털 아카이브|한국학중앙연구원 제공 한국학 기초자료·고문헌 서비스|https://yoksa.aks.ac.kr/main.jsp|문학·역사·시각자료 기반의 한국적 소재 수집|공공자원|상|
|한국 문학|세계 속의 한국문학|서울대 K-연구소식/K-MOOC 강좌 자료|https://ckl.snu.ac.kr/ko/k-%EC%97%B0%EA%B5%AC%EC%86%8C%EC%8B%9D-%EA%B2%8C%EC%8B%9C%ED%8C%90/document/90/?mod=document&uid=132|한국 고전문학을 세계문학 관점에서 이해하는 강의 자료|강의/자료|중|
|AI 도구 사례|Canva Magic Write|OpenAI 기반 AI 글쓰기 도구|https://www.canva.com/ko_kr/magic-write/|프롬프트→초안→편집 워크플로 사례|도구|중|
|AI 도구 사례|Canva AI Assistant|텍스트·시각화·디자인 생성 통합 도구|https://www.canva.com/ko_kr/ai-assistant/|창작 프롬프트를 텍스트/이미지 자료화하는 사례|도구|중|
|AI 도구 사례|EasyMusic AI Lyrics Generator|주제·스타일·분위기·키워드 입력형 가사 생성기|https://easymusic.ai/ko/tools/ai-lyrics-generator|상용 AI 가사 생성기가 어떤 입력 필드를 요구하는지 참고|도구|중|
|AI 도구 사례|Suno AI 음악 생성기|AI 음악 생성 플랫폼|https://suno.com/ko|가사/분위기/스타일을 곡으로 확장하는 도구 사례|도구|중|
|AI 도구 사례|Suno AI Song Lyrics Generator|가사 아이디어를 전체 트랙으로 연결|https://suno.com/hub/ai-song-lyrics-generator|가사→보컬·음악 생성 워크플로 참고|도구|중|

## system use
- 작사·운율 / K-pop 분석: inform hook rhythm, diction, section density, repetition dose.
- AI 한국어 쓰기 / 작문교육: enforce iterative feedback and reflection rather than one-shot generation.
- AI 공동작곡 / 가사 생성: treat AI as candidate engine, critic, rewriter, not final author.
- 한국어 말뭉치 / 데이터: support speech register, familiar syllables, dialogue-like phrasing.
- 한국 고전/문학/문화: supply scene, relation, object-world, but never force traditional imagery.
- AI 도구 사례: compare external UI input fields; do not copy their generic prompt patterns.

## ingestion rule
No source is pasted into a lyric. Every source must be converted into one of:
1. routing condition
2. draft generation step
3. failure filter
4. rewrite drill
5. acceptance test
6. GitHub research note
