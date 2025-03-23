**1. 제너레이터 (Generators)**

- **개념:**
    - 이터레이터(Iterator)를 생성하는 특별한 종류의 함수.
    - yield 키워드를 사용하여 값을 반환하고, 함수의 상태를 저장하여 다음 호출 시 그 지점부터 실행을 재개.
    - Lazy evaluation (지연 평가): 값을 미리 생성하지 않고 필요할 때마다 생성하여 메모리 효율성을 높임.
- **예시:**
    
          `def get_primes():
        """소수를 무한히 생성하는 제너레이터"""
        candidate = 2
        found = []
        while True:
            if all(candidate % prime != 0 for prime in found):
                yield candidate  # 소수를 반환하고 대기
                found.append(candidate)
            candidate += 1
    
    primes = get_primes()
    print(next(primes))  # 2
    print(next(primes))  # 3
    print(next(primes))  # 5`
    
- **sys.maxsize:** 시스템에서 표현 가능한 가장 큰 정수. (메모리 크기와 관련)
- **Iterable, Iterator:**
    - **Iterable:** iter() 함수를 사용하여 이터레이터를 얻을 수 있는 객체 (예: 리스트, 튜플, 문자열).
    - **Iterator:** next() 함수를 사용하여 값을 순차적으로 반환하는 객체.
- **Comprehension:** 리스트, 집합, 딕셔너리를 간결하게 생성하는 방법 (예: [x**2 for x in range(10)]).

**2. 싱글 디스패치 (Single Dispatch)와 멀티플 디스패치 (Multiple Dispatch)**

- **싱글 디스패치:**
    - 함수의 첫 번째 인자(일반적으로 self)의 타입에 따라 다른 동작을 수행.
    - 파이썬은 functools.singledispatch 데코레이터를 통해 싱글 디스패치를 지원.
    - 제네릭 함수(Generic Function): 싱글 디스패치를 사용하는 함수.
- **멀티플 디스패치:**
    - 여러 인자의 타입 조합에 따라 다른 동작을 수행.
    - 파이썬은 기본적으로 지원하지 않으며, 외부 라이브러리(예: multipledispatch)를 사용해야 함.
- **덕 타이핑 (Duck Typing):** "만약 오리처럼 걷고, 오리처럼 꽥꽥거린다면, 그것은 오리다." 즉, 객체의 실제 타입보다는 객체가 어떤 메서드와 속성을 가지고 있는지가 중요.
- **다형성 (Polymorphism):** 동일한 인터페이스(메서드)가 다른 타입의 객체에서 다르게 동작하는 것.

**3. 프로토콜 (Protocols)과 덕 타이핑**

- **프로토콜:** 특정 동작을 지원하기 위해 객체가 구현해야 하는 메서드 집합 (비공식적인 인터페이스).
- **예시:**
    - 시퀀스 프로토콜: __len__, __getitem__을 구현하면 시퀀스처럼 동작 (인덱싱, 슬라이싱 가능).
    - 이터레이터 프로토콜: __iter__, __next__를 구현하면 반복 가능.
- **inspect.getsource():** 함수의 소스 코드를 얻는 함수.

**4. 추상화 (Abstraction)와 추상 기본 클래스 (Abstract Base Classes, ABCs)**

- **추상화:**
    - 복잡한 시스템의 핵심적인 특징만 추출하여 단순화하는 과정.
    - 객체 지향 프로그래밍에서 인터페이스와 구현을 분리하는 데 사용.
- **추상 기본 클래스 (ABCs):**
    - 추상 메서드(구현이 없는 메서드)를 하나 이상 포함하는 클래스.
    - 직접 인스턴스화할 수 없으며, 상속을 통해 구체적인 클래스를 만들어 사용.
    - abc 모듈의 ABCMeta 메타클래스를 사용하여 정의.
    - 추상 메서드는 @abstractmethod 데코레이터를 사용하여 표시.
    - 추상 클래스를 상속받는 하위 클래스는 추상 메서드를 반드시 구현해야 함.
- **추상화 구현 방법:**
    1. **상속:** 추상 클래스를 상속하여 구체적인 클래스를 만듦.
    2. **메타클래스:** ABCMeta를 사용하여 추상 클래스를 정의.

**5. 객체 지향 프로그래밍 (OOP) 개념**

- **객체 (Object):** 데이터(속성)와 그 데이터를 조작하는 절차(메서드)를 묶은 것.
- **클래스 (Class):** 객체를 생성하기 위한 틀.
- **인스턴스 (Instance):** 클래스로부터 생성된 구체적인 객체.
- **상속 (Inheritance):** 기존 클래스의 속성과 메서드를 물려받아 새로운 클래스를 정의.
- **합성 (Composition):** 다른 클래스의 인스턴스를 자신의 속성으로 포함하여 객체를 구성.
- **위임 (Delegation):** 객체가 특정 작업을 다른 객체에게 맡기는 것.
    - **명시적 위임 (Explicit Delegation):** 합성 (Composition).
    - **암시적 위임 (Implicit Delegation):** 상속 (Inheritance).
- **__dict__:** 객체의 속성들을 저장하는 딕셔너리.
- **__getattribute__:** 속성 접근 시 호출되는 특별 메서드.
- **__getattr__:** 객체에 없는 속성에 접근할 때 호출되는 특별 메서드.
- **getattr():** 문자열로 주어진 속성 이름을 사용하여 객체의 속성 값을 가져오는 내장 함수.
- **vars():** 객체의 __dict__ 속성을 반환하는 내장 함수.
- **super():** 부모 클래스의 메서드를 호출하는 데 사용.
- **__mro__ (Method Resolution Order):** 메서드 탐색 순서를 나타내는 튜플.
- **mro():** 클래스의 메서드 탐색 순서를 반환하는 메서드.
- **dir():** 객체가 가지고 있는 속성과 메서드의 목록을 반환하는 내장 함수.
- **__dir__():** dir() 함수가 호출될 때 실행되는 특별 메서드.

**6. 메타클래스 (Metaclasses)**

- **개념:** 클래스의 클래스. 즉, 클래스를 생성하는 객체.
- **type:** 파이썬의 기본 메타클래스.
- **싱글톤 (Singleton):** 메타클래스를 사용하여 클래스의 인스턴스를 하나만 생성하도록 제한하는 디자인 패턴.

**7. 딥러닝에서의 컴포지션**

- **합성 함수 (Composite Function):** 여러 함수를 결합하여 새로운 함수를 만드는 것.
- **딥러닝 모델:** 여러 레이어(함수)를 합성하여 구성.
- **__call__:** 객체를 함수처럼 호출할 수 있게 해주는 특별 메서드.

**핵심 요약**

- **제너레이터:** 메모리 효율적인 이터레이터 생성.
- **싱글/멀티플 디스패치:** 인자 타입에 따른 함수 동작 제어.
- **프로토콜, 덕 타이핑:** 유연한 객체 인터페이스 정의.
- **추상화, ABCs:** 인터페이스와 구현 분리.
- **상속, 합성, 위임:** 코드 재사용 및 유연성 확보.
- **메타클래스:** 클래스 생성 제어.
- **딥러닝:** 컴포지션을 통한 복잡한 모델 구축.

**1. 데코레이터 (Decorators) 기본**

- **정의:**
    - 함수나 클래스의 기능을 수정하거나 확장하는 데 사용되는 디자인 패턴.
    - 다른 함수(또는 클래스)를 인자로 받아 새로운 함수(또는 클래스)를 반환하는 호출 가능한 객체(callable).
    - @ 기호를 사용하여 간결하게 표현.
- **목적:**
    - 코드 중복 감소.
    - 가독성 향상.
    - 기존 코드 변경 없이 기능 추가/변경.
    - 관점 지향 프로그래밍 (Aspect-Oriented Programming, AOP) 지원.
- **함수 데코레이터 기본 구조:**
    
          `def decorator(func):  # 데코레이터 함수
        def wrapper(*args, **kwargs):  # 래퍼 함수
            # 함수 실행 전 추가 작업
            result = func(*args, **kwargs)  # 원래 함수 실행
            # 함수 실행 후 추가 작업
            return result
        return wrapper
    
    @decorator  # 데코레이터 적용
    def my_function():
        # ...
        pass`
    
- **@ syntax:** @decorator는 my_function = decorator(my_function)과 동일.
- **함수 클로저 (Function Closure):** 내부 함수가 외부 함수의 변수(스코프)에 접근할 수 있는 기능. 데코레이터에서 래퍼 함수가 원래 함수를 호출하고 그 결과를 반환하는 데 사용.
- **functools.wraps:** 데코레이터로 인해 원래 함수의 메타데이터(이름, 독스트링 등)가 손실되는 것을 방지하기 위해 사용.

**2. 매개변수가 있는 데코레이터 (Decorators with Parameters)**

- **구조:** 데코레이터 함수를 한 번 더 감싸는 함수를 추가.
    
          `def decorator_with_param(param):  # 매개변수를 받는 함수
        def decorator(func):  # 실제 데코레이터 함수
            def wrapper(*args, **kwargs):
                # param 사용
                result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator
    
    @decorator_with_param(value)  # 매개변수와 함께 데코레이터 사용
    def my_function():
        # ...
        pass`
    
- **@ syntax:** @decorator_with_param(value)는 my_function = decorator_with_param(value)(my_function)와 동일.

**3. 데코레이터 체이닝 (Chaining Decorators)**

- **개념:** 여러 데코레이터를 하나의 함수에 적용.
    
          `@decorator1
    @decorator2
    def my_function():
        # ...
        pass`
    
- **@ syntax:** my_function = decorator1(decorator2(my_function))와 동일.
- **실행 순서:**
    - **데코레이터 적용 시:** 함수에 가까운 데코레이터부터 순서대로 실행 (안쪽에서 바깥쪽).
    - **함수 호출 시:** 가장 바깥쪽 데코레이터의 래퍼 함수부터 순서대로 실행 (바깥쪽에서 안쪽).

**4. 클래스 데코레이터 (Class Decorators)**

- **개념:** 클래스를 사용하여 데코레이터를 구현.
- **구조:**
    
          `class MyDecorator:
        def __init__(self, func):
            self.func = func
            # 초기화 작업
    
        def __call__(self, *args, **kwargs):
            # 함수 실행 전 추가 작업
            result = self.func(*args, **kwargs)
            # 함수 실행 후 추가 작업
            return result
    
    @MyDecorator
    def my_function():
        # ...
        pass`
    
- **__init__:** 데코레이터가 적용될 함수를 인자로 받음.
- **__call__:** 데코레이터가 적용된 함수가 호출될 때 실행되는 메서드.
- **장점:** 상태(state)를 유지해야 하는 데코레이터에 유용 (예: 호출 횟수 추적).

**5. 추가 내용**

- **getattr(object, name[, default]):** 객체의 속성 값을 문자열 이름으로 가져오는 내장 함수.
- **연산자 오버로딩 (Operator Overloading):** 연산자의 기본 동작을 재정의하는 것 (예: __add__, __getitem__).
- **NotImplementedError:** 추상 메서드를 구현하지 않았을 때 발생시키는 예외.
- **itertools, functools, operator:** 함수형 프로그래밍을 지원하는 유용한 모듈.
- **chain:** 여러 이터러블을 연결.
- **count:** 무한히 증가하는 숫자 생성.
- **cycle:** 이터러블을 무한 반복.
- **combinations:** 조합 생성.
- **combinations_with_replacement:** 중복 조합 생성.
- **add:** 덧셈 함수 (operator 모듈).
- **partial:** 함수의 일부 인자를 고정하여 새로운 함수 생성.
- **고차 함수 (Higher-Order Functions):** 함수를 인자로 받거나 함수를 반환하는 함수.
- **compose:** 여러 함수를 합성하여 새로운 함수 생성.
- **all_pred, any_pred:** 여러 조건(predicate)을 한 번에 검사.
- **juxt:** 여러 함수를 같은 인자로 호출하고 결과를 튜플로 반환.
- **관점 지향 프로그래밍 (Aspect-Oriented Programming, AOP):** 핵심 기능과 부가 기능(cross-cutting concerns)을 분리하여 모듈화하는 프로그래밍 패러다임.
- **믹스인 (Mixins):** 다중 상속에서 코드 재사용을 위해 사용되는 클래스. 일반적으로 단일 책임을 가지며, 독립적으로 인스턴스화되지 않음.

**핵심 요약**

- **데코레이터:** 함수/클래스 기능을 쉽게 확장/변경.
- **@ syntax:** 데코레이터 적용을 간결하게 표현.
- **함수 클로저:** 데코레이터 내부 동작의 핵심.
- **functools.wraps:** 메타데이터 손실 방지.
- **매개변수, 체이닝, 클래스:** 데코레이터 활용 다양화.
- **AOP, 믹스인:** 데코레이터와 관련된 고급 개념.