### 1. 중첩 함수 (Nested Function) 와 클로저 (Closure)

- **중첩 함수 (Nested Function):** 함수 내부에 정의된 함수. 내부 함수는 외부 함수의 스코프에 접근 가능.
- **클로저 (Closure):**
    - **함수 + 자유 변수 (free variable)** 의 조합.
    - **자유 변수:** 함수 스코프 밖에서 정의되었지만, 함수 내부에서 참조되는 변수.
    - **클로저 생성 조건:**
        1. **중첩 함수** (내부 함수가 외부 함수 안에 정의).
        2. **외부 함수** 가 **내부 함수** 를 **반환**.
        3. **내부 함수** 가 외부 함수의 **자유 변수** 를 **참조**.
    - **LEGB 규칙과 클로저:** 클로저는 LEGB 규칙의 Enclosing 스코프 활용. 데코레이터는 클로저의 대표적인 활용 예시.
    
    ```python
    ```python
    t = 1 # 글로벌 변수
    
    def x():
        global t # t 를 글로벌 변수로 선언
        t = t + 1 # 글로벌 변수 t 값 변경
        return t
    
    x() # 글로벌 변수 t 값 변경 (1 -> 2)
    print(t) # 글로벌 변수 t 값 확인 (2)
    ```
    ```
    

### 2. 스코프 (Scope) 심화: global, nonlocal 키워드

- **LEGB 규칙 복습:** Local -> Enclosing -> Global -> Built-in 순으로 변수 검색.
- **UnboundLocalError**: 함수 내에서 로컬 변수 할당 전에 참조 시 발생하는 에러.
    - t = t + 1 예시: 함수 내 t 를 로컬 변수로 취급, 할당 전에 참조하려 해서 에러 발생.
- **global 키워드:** 함수 내부에서 **전역 변수** 를 **수정**하고자 할 때 사용. 전역 변수를 함수 스코프 안으로 가져와서 전역 변수 자체를 변경.
    
    ```python
    ```python
    t = 1 # 글로벌 변수
    
    def x():
        global t # t 를 글로벌 변수로 선언
        t = t + 1 # 글로벌 변수 t 값 변경
        return t
    
    x() # 글로벌 변수 t 값 변경 (1 -> 2)
    print(t) # 글로벌 변수 t 값 확인 (2)
    ```
    ```
    
- **nonlocal 키워드:** 중첩 함수에서 **Enclosing 함수 스코프** 의 변수를 **수정**하고자 할 때 사용. Enclosing 함수 스코프 변수를 내부 함수 스코프 안으로 가져와서 Enclosing 함수 변수 자체를 변경.
    
    ```python
    ```python
    t = 1 # 글로벌 변수
    def x():
        t= 2 # Enclosing 변수
        def y():
            nonlocal t # t 를 Enclosing 변수로 선언
            t = t + 1 # Enclosing 변수 t 값 변경
            return t
        return y
    
    my_closure_y = x() # x() 호출 -> 클로저 y() 반환
    print(my_closure_y()) # 클로저 y() 호출 -> Enclosing 변수 t 값 변경 (2 -> 3)
    ```
    ```
    
- **global, nonlocal 주의**: 코드 **가독성 저하**, **side effect 증가** 시킬 수 있으므로 **신중하게 사용**해야 함. "Consenting adult" (본인 책임) 개념.

### 3. 예약어 (Keywords) 심층 분석

- **keyword.kwlist**: 파이썬 예약어 목록 확인.
- **예약어 특징**: 파이썬 문법 요소, 식별자로 사용 불가.
- **예약어 종류별 특징**:
    - **False, None, True**: 불리언 값, Null 값.
    - **and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield**: 제어 흐름, 함수/클래스 정의, 예외 처리, import 등 파이썬 문법 구성 요소.
    - **async, await**: 코루틴 관련 예약어 (비동기 프로그래밍).

### 4. 특수 객체: None, NotImplemented, Ellipsis

- **None**: Null 값, 값의 부재 (absence of value) 표현. 함수가 명시적 return 없을 때 반환. 존재론적 False.
- **pass**: 아무것도 하지 않는 문장. 코드 **구문 오류 방지** 위한 placeholder. 함수, 클래스, 조건문 등 코드 블록 필요하지만 내용이 아직 없을 때 사용.
- **NotImplemented**: 연산이 해당 타입에 대해 **구현되지 않았음**을 나타내는 특수 값. 숫자 메소드, rich comparison 메소드에서 반환. 추상 클래스, 오버라이딩 시 활용.
- **Ellipsis**: ... 리터럴 또는 Ellipsis 객체. **생략** 또는 **미완성** 나타낼 때 사용. 슬라이싱, 타입 힌팅, stub 코드 등에서 활용.

### 5. Boolean 연산자 (and, or) 심화

- **and 연산자:**
    - **Short-circuit evaluation (단축 평가):** 좌항 (x) 먼저 평가. 좌항이 **False** 이면 **좌항 값 반환** (우항 평가 X). 좌항이 **True** 이면 **우항 (y) 평가 후 우항 값 반환**.
    - **True/False 판별**: 존재론적 True/False 관점에서 판별.
- **or 연산자:**
    - **Short-circuit evaluation (단축 평가):** 좌항 (x) 먼저 평가. 좌항이 **True** 이면 **좌항 값 반환** (우항 평가 X). 좌항이 **False** 이면 **우항 (y) 평가 후 우항 값 반환**.
    - **Default 값 설정**: value = user_input or 'default_value' 와 같이 default 값 설정에 유용하게 활용 가능.
- **반환 값**: and, or 연산자는 False, True 불리언 값 대신 **마지막으로 평가된 인자 값** 을 그대로 반환.

### 6. in, not in 연산자: 멤버십 테스트

- **in 연산자:** 컨테이너 (시퀀스, 셋, 딕셔너리 등) 에 특정 요소가 **존재하는지** 여부 **(True/False)** 반환.
- **not in 연산자:** 컨테이너에 특정 요소가 **존재하지 않는지** 여부 **(True/False)** 반환.
- **컨테이너 타입별 동작 방식:**
    - **리스트, 튜플, 문자열:** 요소 값 순차적으로 비교.
    - **셋:** 해시 기반 멤버십 테스트 (빠른 검색).
    - **딕셔너리:** **키 (Key) 멤버십 테스트**. 값 (Value) 은 검색하지 않음.

### 7. 딕셔너리 뷰 (Dictionary View) 활용

- **dict.keys(), dict.values(), dict.items()**: 딕셔너리의 키, 값, 키-값 쌍에 대한 **뷰 객체** 반환.
- **뷰 객체 특징**: 딕셔너리 변경 반영 (동적 뷰), 순회 가능.
- **딕셔너리 순회**: 딕셔너리 기본 순회는 키 (key) 순회. 값 (value) 또는 키-값 쌍 순회 시 뷰 객체 활용 필요.
    - for key in x: (키 순회)
    - for key, value in x.items(): (키-값 쌍 순회, 언패킹 활용)

### 8. TensorFlow Keras MNIST 데이터셋 활용

- **tf.keras.datasets.mnist.load_data()**: MNIST 손글씨 숫자 이미지 데이터셋 로드 함수.
- **반환값**: 튜플 ((x_train, y_train), (x_test, y_test)) 형태.
    - x_train, x_test: 학습/테스트 이미지 데이터 (numpy array).
    - y_train, y_test: 학습/테스트 레이블 (정답) 데이터 (numpy array).
- **데이터 언패킹**: 언패킹을 통해 train/test 데이터 분리.
- **데이터 형태**: 이미지 데이터는 3차원 텐서 (height, width, channel), 레이블 데이터는 1차원 텐서.
- **데이터 분석, 딥러닝 활용**: 행렬 형태 데이터 처리, 선형대수 중요성 강조.

### 9. 반복문 (for) 심화 및 dis 모듈 활용

- **for 루프 최적화**: 파이썬 for 루프는 **효율적인 반복** 구조. 메모리 효율성, 성능 우수.
- **while 루프 vs. for 루프**: while 루프는 무한 루프 등 특정 조건 기반 반복에 주로 사용, for 루프는 시퀀스 순회에 최적화.
- **dis 모듈**: 파이썬 bytecode disassembler. dis.dis(함수) 로 함수 bytecode 분석 가능.
- **dis.dis(x) 분석**: for 루프 bytecode 분석을 통해 FOR_ITER opcode 확인, for 루프의 효율성 확인.
- **for-else 구문**: for 루프가 break 없이 정상 종료 시 else 블록 실행.
- **for-continue 구문**: continue 문은 현재 iteration 중단, 다음 iteration 시작. else 블록은 continue 와 무관하게 루프 정상 종료 시 실행.

### 10. 예외 처리 (Exception Handling) 심화

- **예외 처리 목적**: 프로그램 **비정상 종료 방지**, **에러 핸들링**, **robustness (강건성)** 확보.
- **try-except 블록**: 예외 발생 가능 코드 try 블록에, 예외 처리 코드 except 블록에 작성.
- **사용자 입력 예외 처리**: input() 함수 사용자 입력, int() 변환 시 ValueError 발생 가능성 예외 처리 예시.
- **while True + try-except-else-break**: 사용자 입력 유효성 검증 루프 패턴. 유효한 입력 받을 때까지 반복.
    - try: 사용자 입력 시도, 예외 발생 가능 코드.
    - except: 예외 발생 시 처리 (continue).
    - else: 예외 없을 시 실행 (break).
    - else 블록 break 시 루프 종료. else 블록 없으면 무한 루프.
- **continue 지양 (AI 분야):** 인공지능 (AI) 분야에서는 continue 문 사용 **빈도 낮음**. 코드 흐름 복잡성 증가 우려.

### 11. Accumulation Pattern (누적 패턴)

- **알고리즘 기본 패턴**: 초기값 설정, 루프를 통해 값 누적, 최종 결과 도출하는 프로그래밍 패턴.
- **초기값 설정**: temp = 0 와 같이 누적 변수 초기화.
- **루프**: for 루프 등을 사용하여 데이터 순회.
- **누적 연산**: temp += i 와 같이 누적 변수에 값 더하기/곱하기 등 연산 수행.
- **목표값 도출**: 루프 종료 후 누적 변수에 최종 결과값 저장.
- **다양한 활용**: 숫자 합계, 카운팅, 통계 계산 등 다양한 알고리즘 구현에 활용. 문자열, 리스트 등 컨테이너 처리에도 응용 가능.
- **자동화 (Automation) 핵심**: 반복 작업을 자동화하는 프로그래밍의 핵심 원리.

### 12. 함수형 프로그래밍 (Functional Programming) 특징 복습

- **David Mertz 정의**: 함수형 프로그래밍 특징 요약 (재복습).
    - **First-class functions (일급 함수):** 함수를 값처럼 취급.
    - **Recursion (재귀):** 주요 제어 구조.
    - **List processing (리스트 처리):** 리스트 중심 연산.
    - **Pure functions (순수 함수):** Side effect 배제.
    - **Expressions over statements (표현식 중심):** 문장 대신 표현식 사용.
    - **Higher-order functions (고차 함수):** 함수를 인자로 받거나 반환하는 함수 활용.
- **파이썬, 다중 패러다임 언어**: 함수형 프로그래밍 **지원**하지만, **순수 함수형 언어는 아님**. 명령형, 객체지향 등 다양한 패러다임 **혼용 가능**.
- **함수형 프로그래밍 장점**: 간결성, 가독성, 테스트 용이성, 동시성, 형식적 증명 가능성 (수학적 기반).
- **함수형 프로그래밍 활용 분야**: 데이터 분석, 인공지능 (딥러닝).

### 13. 캡슐화 (Encapsulation) 복습

- **"What" 에 집중**: 데이터 구축 "how" (어떻게) 보다는 데이터 "what" (무엇) 에 집중하는 프로그래밍 방식.
- **함수 캡슐화**: 데이터 구축 코드 함수로 묶어 **구현 детали 숨김**, **추상화 수준 향상**. 코드 가독성, 유지보수성 향상.
- **클래스 vs 함수 캡슐화**: 클래스는 정보 은닉 (information hiding) 완벽하게 지원 X, 함수는 캡슐화에 더 효과적일 수 있음. 모듈화 장점.

### 14. 컴프리헨션 (Comprehension) 복습 및 성능 비교

- **컴프리헨션 장점**: 코드 **간결성**, **가독성**, **성능 향상**. "How" 대신 "What" 에 집중.
- **다양한 컴프리헨션**: 리스트 컴프리헨션 ([]), 셋 컴프리헨션 ({}), 딕셔너리 컴프리헨션 ({key:value}), 제너레이터 컴프리헨션 (()).
- **리스트 컴프리헨션 vs. 명령형 루프 성능 비교**: %time 매직 명령어 사용, 리스트 컴프리헨션이 명령형 루프보다 **빠른** 성능 확인.
- **컴프리헨션 메모리 효율성**: 리스트 컴프리헨션은 결과 리스트를 **메모리에 모두 로드**, 대용량 데이터 처리 시 **메모리 부족** 문제 발생 가능.
- **제너레이터 컴프리헨션 메모리 효율성**: 제너레이터 컴프리헨션은 **lazy evaluation (지연 평가)**, 데이터 **요청 시점에 생성**, 메모리 효율적. 딥러닝, 대용량 데이터 처리에 필수적.