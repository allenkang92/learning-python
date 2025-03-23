### 1. 파이썬 클래스 (Python Class) 와 객체 지향 프로그래밍 (Object-Oriented Programming, OOP) 재확인

- **객체 지향 프로그래밍 (OOP) 역사**: 1960년대 등장, 현재 주류 프로그래밍 패러다임.
- **클래스 == 데이터 타입**: 파이썬 2.2 버전부터 클래스가 **사용자 정의 데이터 타입** 을 만드는 메커니즘으로 확립. int, str, list 등 내장 타입도 클래스.
- **type(a)**: 변수 a 의 타입 (클래스) 확인. type(1) 은 <class 'int'>. int 는 클래스 (데이터 타입).
- **class A: pass**: A 라는 이름의 **새로운 클래스 정의**. pass 는 빈 블록.
- **a = A()**: A() 는 클래스 A 의 **인스턴스 (객체)** 생성. a 는 인스턴스 객체 식별자.
- **type(a)**: a 의 타입 확인. <class '__main__.A'>. A 클래스로부터 생성된 인스턴스.
- **__main__**: 현재 파일 (main 모듈) 에서 정의된 클래스임을 나타냄.
- **클래스 생성 == 새로운 데이터 타입 생성**: 클래스 정의 = 사용자 정의 데이터 타입 정의. TensorFlow Keras, 딥러닝 모델 클래스 (새로운 데이터 타입) 제공.

### 2. 객체 지향 프로그래밍 (OOP) 장점 및 OOP 원칙 복습

- **OOP 장점**: 코드 재사용성, 모듈화, 유지보수성, 협업 용이, 설계 중심 개발, 코드 가독성 향상, 버그 감소, 확장성.
- **OOP 원칙 - 클래스 (Class) 와 객체 (Object) 재확인**:
    - **클래스 (Class):** 객체 생성을 위한 설계도, 템플릿. 데이터 (속성) 와 메소드 정의.
    - **객체 (Object):** 클래스의 인스턴스, 클래스 설계도 기반으로 생성된 실체.

### 3. 캡슐화 (Encapsulation), 상속 (Inheritance), 다형성 (Polymorphism) OOP 핵심 원칙 복습

- **캡슐화 (Encapsulation):**
    - **데이터와 메소드 묶음**: 관련 데이터 (속성) 와 메소드를 **하나의 단위 (클래스)** 로 묶는 것.
    - **정보 은닉 (Information Hiding):** 클래스 내부 구현 детали 숨기고, 외부에는 필요한 인터페이스 (메소드) 만 노출.
    - **데이터 보호**: 외부의 잘못된 접근, 수정으로부터 객체 데이터 보호.
    - **낮은 결합도 (Loose Coupling):** 객체 내부 구현 변경 시 외부 코드 영향 최소화, 모듈화, 유지보수성 향상.
    - **파이썬 캡슐화 한계**: 파이썬은 완벽한 정보 은닉 (private) 지원 X. "Consenting adult" (본인 책임) 철학.
- **상속 (Inheritance):**
    - **코드 재사용성**: 기존 클래스 (부모 클래스) 코드 재사용, 중복 코드 감소.
    - **클래스 확장**: 부모 클래스 기능 확장, 새로운 기능 추가, 기존 기능 수정 (오버라이딩).
    - **계층 구조**: 클래스 계층 구조 형성, 코드 구조화, 관리 용이.
    - **다형성 (Polymorphism) 기반**: 상속은 다형성 구현의 기반.
- **다형성 (Polymorphism):**
    - **"하나의 인터페이스, 다양한 구현"**: 동일한 메소드 호출에 대해 객체 타입 (클래스) 에 따라 **다르게 동작**하도록 구현.
    - **유연성, 확장성**: 코드 유연성, 확장성 향상. 새로운 클래스 추가, 기존 코드 수정 없이 기능 확장 가능.
    - **연산자 오버로딩 (Operator Overloading)**: 연산자를 다형적으로 동작하도록 재정의하는 것도 다형성의 한 형태.
    - **tips.describe() 예시**: Pandas DataFrame 의 describe() 메소드는 Series (열 데이터 타입) 타입에 따라 다른 통계 정보 (수치형, 범주형) 제공 (다형성).

### 4. 파이썬 상속 특징: 델리게이션 (Delegation) 관점

- **파이썬 상속 != "물려받는다"**: 파이썬 상속은 부모 클래스 기능을 **그대로 복사**하는 것이 아니라, **"위임 (Delegation)"** 에 더 가까운 개념.
- **델리게이션 (Delegation):** 객체가 특정 작업을 직접 수행하지 않고, **다른 객체에게 위임**하여 처리하는 방식. 코드 재사용성, 유연성 향상.
- **상속 vs 델리게이션**: 상속은 **암묵적 델리게이션 (Implicit Delegation)**, 컴포지션은 **명시적 델리게이션 (Explicit Delegation)**.
- **B.a 예시**: B 클래스가 A 클래스 상속 시, B.a 는 A.a 와 **동일한 객체** (메모리 주소 동일). B 클래스가 a 속성 접근을 A 클래스에게 **위임**하는 형태.
- **오버라이딩 (Overriding) 도 델리게이션**: 자식 클래스에서 메소드 오버라이딩은 부모 클래스 메소드 호출을 **막고**, 자식 클래스 메소드 **우선 호출** (델리게이션 순서 변경).

### 5. 다중 상속 (Multiple Inheritance) 심화 및 MRO (Method Resolution Order)

- **다중 상속 재확인**: 파이썬 클래스는 여러 부모 클래스 상속 가능.
- **다이아몬드 상속 문제**: 다중 상속 시 메소드 탐색 순서 모호성 문제 발생 가능.
- **MRO (Method Resolution Order) 중요성**: 메소드 탐색 순서 (MRO) 를 통해 다중 상속 문제 해결. 파이썬 C3 선형화 알고리즘 사용.
- **D.mro()**: 클래스 D 의 MRO 확인. MRO 리스트 순서대로 메소드 탐색.
- **TypeError: Cannot create a consistent method resolution order (MRO)**: 다중 상속 관계 모순 시 MRO 생성 불가능 에러 발생.

### 6. super() 심화: 다중 상속 환경에서의 부모 클래스 메소드 호출

- **super() 의 역할**: 다중 상속 환경에서 **MRO** 를 기반으로 **정확한 부모 클래스 메소드 호출** 보장. 다이아몬드 상속 문제 해결 핵심.
- **super().__init__()**: 자식 클래스 __init__ 에서 부모 클래스 __init__ 호출 시 super() 사용 권장.
- **super(SubClass, self)**: super() 함수의 인자: 첫 번째 인자 - **자신 (SubClass)**, 두 번째 인자 - **인스턴스 (self)**.
- **super() 동작 방식**: MRO 상에서 SubClass 다음 부모 클래스를 찾아 메소드 호출.
- **중복 호출 방지**: super() 를 사용하면 다중 상속 계층에서 부모 클래스 메소드 **중복 호출 방지**. MRO 순서대로 각 부모 클래스 __init__ 한 번씩만 호출.
- **TensorFlow Keras, PyTorch 다중 상속 활용**: 딥러닝 프레임워크 (TensorFlow, PyTorch) 에서 복잡한 다중 상속 구조 활용. MRO, super() 이해 필수.

### 7. 클래스 메소드, 스태틱 메소드 활용: 네임스페이스, 유틸리티 함수 (재확인)

- **클래스 메소드, 스태틱 메소드 재확인**: 클래스 네임스페이스 활용, 유틸리티 함수 묶음, 클래스 레벨 연산 등에 활용.
- **pd.DataFrame.from_dict**: Pandas DataFrame 클래스의 from_dict 클래스 메소드 예시. 딕셔너리로부터 DataFrame 객체 생성하는 팩토리 메소드.

### 8. 객체 지향 프로그래밍 (OOP) vs. 함수형 프로그래밍 (FP) 특징 비교 (심층 분석) 재확인

- **OOP**:
    - **장점**: 코드 재사용성, 유지보수성, 모듈화, 협업, 현실 세계 모델링.
    - **단점**: 복잡성, side effect, 상태 관리 어려움.
- **FP**:
    - **장점**: 간결성, 가독성, side effect 감소, 테스트 용이, 병렬 처리.
    - **단점**: 러닝 커브, 특정 문제 비효율, OOP 에 비해 코드 구조화 어려울 수 있음.
- **파이썬, Multiparadigm Language**: OOP, FP 모두 지원. 상황과 목적에 따라 **적절한 패러다임 선택** 또는 **혼합** 사용.
- **딥러닝**: 함수형 프로그래밍 (FP) 패러다임 적극 활용. TensorFlow, PyTorch 함수형 인터페이스 제공.

### 9. 데이터 (Data), 값 (Value), 타입 (Type), 객체 (Object) 개념 재정립

- **데이터 (Data):** 문맥에 따라 의미 달라짐, 프로그래밍 관점 - 메모리 상의 **연속된 비트** (0과 1의 나열). 자체적으로는 의미 없음.
- **값 (Value):** 데이터에 **의미 (해석)** 를 부여한 것. 데이터 + 해석. 해석 없이는 데이터는 무의미. 모든 값은 메모리 상의 데이터와 연관.
- **데이터 타입 (Data Type) == 클래스 (Class):** **공통적인 해석** 을 공유하는 **값의 집합**. 데이터 타입 (클래스) 에 따라 데이터 해석 방식, 연산 방식 결정.
- **객체 (Object):** 특정 **데이터 타입 (클래스) 에 속하는 값** 이 저장된 메모리 공간. 객체 == 값 (value).

### 10. 프로그래밍 패러다임 (Programming Paradigm) 재정립

- **패러다임 (Paradigm):** 문제 해결 방식, 프로그래밍 스타일, 사고 방식.
- **선언형 프로그래밍 (Declarative Programming):** "What (무엇)" 에 집중, 문제 해결 방식 **선언**. 함수형 프로그래밍 (FP) 대표적.
- **명령형 프로그래밍 (Imperative Programming):** "How (어떻게)" 에 집중, 문제 해결 **과정 (절차)** 구현. 객체 지향 프로그래밍 (OOP) 도 명령형 패러다임에 속함.
- **파이썬, 객체 지향 + 명령형 패러다임**: 파이썬은 객체 지향 패러다임 기반 명령형 언어. OOP 기능 활용하여 프로그램 구조화, 객체 간 상호작용 통해 문제 해결.

### 11. 파이썬 코딩 스타일: "The Zen of Python" (파이썬의 선) 재확인

- **"There should be one-- and preferably only one --obvious way to do it."**: 파이썬 철학 핵심 문장. "어떤 일을 하는 **명확하고, 가장 좋은 방법은 하나**여야 한다".
- **Multiparadigm Python**: 파이썬은 다양한 패러다임 지원, 문제 해결 방법 다양. But, "The Zen of Python" 에 따라 **가장 명확하고, Pythonic 한 방법** 선택 중요.

### 12. 객체 지향 프로그래밍 (OOP) 장점 재강조

- **생산성 향상**: 코드 재사용성, 모듈화, 개발 속도 향상.
- **재사용성**: 상속, 다형성 활용, 기존 코드 확장, 수정 용이.
- **제약 (Constraints):** 캡슐화, 정보 은닉 통해 실수로 인한 **취약점 감소**. But, "Consenting adult" (본인 책임) 철학.
- **유지보수성, 테스트 용이성, 협업**: 코드 구조화, 모듈화, 관심사 분리 (SoC, Separation of Concerns) 통해 유지보수, 테스트, 협업 효율 증대.

### 13. 데이터 전처리 (Data Preprocessing) 와 함수형 프로그래밍

- **데이터 분석, 머신러닝**: 데이터 전처리 (Data Preprocessing) 중요. Garbage In, Garbage Out (GIGO) 방지.
- **map(), reduce(), filter()**: 데이터 전처리, 데이터 변환, 통계 분석 등 데이터 처리 작업에 유용한 함수형 프로그래밍 도구.
- **seaborn tips 데이터셋**: 데이터 분석 실습 예제 데이터셋. sns.load_dataset('tips') 로 로드.

### 14. 함수 시그니처 (Function Signature) vs. 클래스 __init__ 시그니처

- **함수 시그니처**: 함수 이름, 파라미터 목록, 반환 타입 (type hint) 등 함수 정의 핵심 정보. 함수 사용법, 역할 이해에 중요.
- **클래스 __init__ 시그니처**: 클래스 생성자 (__init__ 메소드) 파라미터 목록. 인스턴스 생성 시 필요한 인자, 인스턴스 초기화 방식 정의. 클래스 사용법 이해에 중요.
- **시그니처 확인 중요**: 함수, 클래스 사용 전에 시그니처 (help(), inspect.signature() 활용) 를 통해 사용법, 인자, 역할 **명확히 파악** 중요.

---

추상화 (Abstraction) 심화: 상속 vs 메타클래스
추상화 (Abstraction) 구현 방식: 파이썬에서 추상화는 주로 상속 (Inheritance) 과 메타클래스 (Metaclass) 두 가지 메커니즘으로 구현.

상속 (Inheritance) 기반 추상화:

추상 클래스 (Abstract Base Class, ABC): abc 모듈 활용, 추상 메소드, 추상 속성 정의. 자식 클래스에서 추상 멤버 구현 강제. 인터페이스 정의, 구현 강제.

템플릿 메소드 패턴 (Template Method Pattern): 알고리즘 뼈대 (template) 를 부모 클래스에 정의, 세부 구현 자식 클래스에 위임. 코드 재사용성, 알고리즘 구조 유지.

메타클래스 (Metaclass) 기반 추상화:

클래스의 클래스: 클래스 생성 과정 제어, 클래스 동작 방식 커스터마이징.

싱글톤 (Singleton) 패턴: 메타클래스를 사용하여 싱글톤 패턴 구현 가능 (클래스 인스턴스 하나만 생성 제한).

사이킷런 (scikit-learn) ABCMeta: sklearn.naive_bayes.ABCMeta 예시. 사이킷런 라이브러리에서 메타클래스 활용 사례. 나이브 베이즈 (Naive Bayes) 분류기 추상화.

**컴포지션 (Composition) 상세 추가: 명시적 델리게이션, 유연성 상승시킴**

- **컴포지션 (Composition) 이란?**:
    - 객체가 다른 객체를 **속성 (attribute) 으로 포함** (has-a 관계).
    - 객체가 **직접 처리하지 않는 작업** 을 **포함된 다른 객체에게 명시적으로 위임 (delegate)** 하는 객체 지향 디자인 패턴.
    - **명시적 델리게이션 (Explicit Delegation)**: 델리게이션 관계가 코드에 명확하게 드러남.
    - **코드 재사용성, 유연성, 낮은 결합도** 확보에 효과적.
- **컴포지션 vs 상속 (Composition vs Inheritance) 비교**:

| **특징** | **컴포지션 (Composition)** | **상속 (Inheritance)** |
| --- | --- | --- |
| 델리게이션 | **명시적 델리게이션 (Explicit Delegation)** | **암묵적 델리게이션 (Implicit Delegation)** |
| 관계 | **Has-a 관계** (객체가 다른 객체를 "가지고 있다") | **Is-a 관계** (객체가 다른 객체의 "일종이다") |
| 결합도 | **낮은 결합도 (Loose Coupling)** | **높은 결합도 (Tight Coupling)** |
| 유연성 | **높은 유연성**: 런타임에 객체 조합 변경 용이, 기능 선택적 위임 가능 | **낮은 유연성**: 컴파일 타임에 상속 관계 결정, 기능 마스킹 어려움 |
| 코드 재사용성 | **높음**: 다양한 객체 조합, 코드 재사용 용이 | **높음**: 부모 클래스 코드 재사용, but 상속 계층 구조 제한적 |
| 다형성 | **유연한 다형성**: 인터페이스 기반 다형성 구현 용이 | **상속 계층 기반 다형성**: 상속 관계에 종속적인 다형성 |
| 메모리 효율성 | 일반적으로 상속보다 메모리 사용량 **약간 증가** 가능성 | 상속보다 메모리 사용량 **적을 수 있음** (구현에 따라 다름) |
| 적합한 상황 | 유연성, 재사용성, 낮은 결합도 중요시되는 경우, 복잡한 객체 관계 모델링 | 코드 구조 단순화, Is-a 관계 명확한 경우, 계층적인 타입 분류 |
- **컴포지션 구현 방식 (Python):**
    - **속성으로 객체 포함**: 클래스 내 __init__ 메소드에서 다른 클래스의 인스턴스를 **인스턴스 속성**으로 포함 (self.door = Door(number, status)).
    - **메소드 호출 위임**: 필요한 기능은 포함된 객체의 메소드를 **명시적으로 호출**하여 처리 (self.door.open()).
- **컴포지션 코드 예시: SecurityDoor 클래스 (Composition 버전)**

`class Door: # Door 클래스 (기본 Door 기능 제공)
    colour = 'brown'
    def __init__(self, number, status):
        self.number = number
        self.status = status
    def open(self):
        self.status = 'open'
    def close(self):
        self.status = 'closed'

class SecurityDoor: # SecurityDoor 클래스 (Composition 사용)
    colour = 'gray'
    locked = True

    def __init__(self, number, status):
        self.door = Door(number, status) # Door 객체를 속성으로 포함 (Composition)

    def open(self):
        if self.locked:
            return
        self.door.open() # Door 객체의 open() 메소드 호출 (명시적 델리게이션)

    def close(self):
        self.door.close() # Door 객체의 close() 메소드 호출 (명시적 델리게이션)

    # __getattr__ 메소드 활용 (속성 접근 위임):
    def __getattr__(self, attr):
        return getattr(self.door, attr) # Door 객체에 속성 접근 위임`

- **SecurityDoor 클래스 (Composition 버전) 분석**:
    - SecurityDoor 클래스는 Door 클래스를 **상속받지 않고**, Door 클래스의 인스턴스를 **self.door 속성**으로 포함 (**Composition**).
    - SecurityDoor 의 open(), close() 메소드는 필요한 기능 (door 열고 닫기) 을 self.door (Door 객체) 에게 **명시적으로 위임 (delegate)**.
    - SecurityDoor 는 Door 클래스와 **독립적인 객체** 가 됨. SecurityDoor is not a Door.
    - __getattr__ 메소드 활용: SecurityDoor 에서 찾을 수 없는 속성 접근 시, __getattr__ 메소드가 호출되어 self.door 객체 (Door 인스턴스) 의 속성에 접근을 **위임**. SecurityDoor 가 Door 의 속성을 "가진 것처럼" 보이게 함 (transparent delegation).
- **__getattr__ 활용 장점**:
    - **코드 간결성**: 모든 메소드 위임 코드를 일일이 작성할 필요 없이, __getattr__ 하나로 처리 가능.
    - **유연성**: 특정 속성만 선택적으로 위임하거나, 마스킹 (masking, 숨기기) 가능.
    - **상속 vs 컴포지션 경계 모호화**: __getattr__ 를 사용한 컴포지션은 상속과 유사한 효과 (자동적인 멤버 접근 위임) 를 내지만, 여전히 컴포지션은 **명시적인 델리게이션** 방식.
- **getattr(obj, 'someattr') vs. obj.someattr**:
    - getattr(obj, 'someattr'): 내장 함수 getattr(). obj.someattr 와 **동일한 속성 접근** 동작 수행. 속성 이름을 **문자열** 형태로 전달 가능.
    - obj.someattr: dotted syntax 를 사용한 속성 접근. 속성 이름 **직접 코드에 명시**.
    - __getattr__ 내부에서 getattr() 사용 이유: 속성 이름이 **문자열 변수** (attr) 에 담겨 있으므로, 문자열 변수를 사용하여 속성에 접근하기 위해 getattr() 사용.
- **컴포지션 장점**:
    - **낮은 결합도 (Loose Coupling)**: 객체 간 결합도 감소, 코드 변경에 유연하게 대처 가능.
    - **선택적 델리게이션**: 필요한 기능만 선택적으로 위임, 불필요한 기능 상속 방지.
    - **마스킹 (Masking) 가능**: 특정 속성 또는 메소드 접근 숨기거나 제어 가능.
    - **메모리 효율성**: 객체 내부에 다른 객체를 포함하더라도 메모리 overhead 크지 않음 (파이썬 참조 방식).
- **컴포지션 vs 상속 선택**:
    - **컴포지션**: 유연성, 낮은 결합도, 선택적 델리게이션, 복잡한 시스템 설계에 유리.
    - **상속**: 코드 구조 단순화, Is-a 관계 명확, 계층적인 타입 분류에 유리.
    - **파이썬**: 컴포지션, 상속 모두 강력하게 지원. 상황과 목적에 따라 **적절한 방식 선택** 중요.