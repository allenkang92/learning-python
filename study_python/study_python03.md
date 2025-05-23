Python PEP 8 스타일 가이드 정리
1. 코드 레이아웃
들여쓰기: 스페이스 4칸 사용
한 줄 최대 길이: 79자 (코드), 72자 (주석/문서)
함수/클래스 사이: 빈 줄 2개
클래스 내 메소드 사이: 빈 줄 1개
import 문은 파일 상단에 배치
import 문 그룹화: 표준 라이브러리 → 서드파티 → 로컬 애플리케이션
문자열 따옴표: 일관성 유지 (작은따옴표 또는 큰따옴표)
2. 공백 사용
괄호/브라켓/중괄호 내부: 불필요한 공백 없음
쉼표/콜론/세미콜론 앞: 공백 없음
함수 호출 괄호 앞: 공백 없음
인덱싱/슬라이싱 괄호 앞: 공백 없음
할당 연산자(=) 주변: 공백 1개씩
연산자 주변: 공백 1개씩 (가독성 위해)
3. 네이밍 컨벤션
함수/변수/모듈: lowercase_with_underscores (스네이크 케이스)
클래스: CapitalizedWords (파스칼 케이스)
상수: ALL_CAPS_WITH_UNDERSCORES
메소드 첫 인자: self (인스턴스 메소드), cls (클래스 메소드)
4. 주석 및 문서화
주석: 완전한 문장으로, 첫 글자 대문자
인라인 주석: 코드와 최소 2칸 띄우고 # 뒤에 공백
블록 주석: 각 줄 # 시작, 코드와 동일한 들여쓰기
독스트링: 모든 공개 모듈/함수/클래스/메소드에 작성
5. 프로그래밍 권장사항
None 비교: is None, is not None 사용
참/거짓 테스트: 암시적 방식 사용 (if seq:, if not seq:)
bool 값 비교: 직접 비교보다 암시적 방식 사용 (if condition:)
try/except 블록: 예외 범위를 최소화하여 사용
컨텍스트 관리자: 리소스 관리에 with 문 사용