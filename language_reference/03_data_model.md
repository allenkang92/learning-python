# 3. Data model

# 3. 데이터 모델

## 3.1. Objects, values and types

## 1. 객체, 값 및 타입

Objects are Python's abstraction for data. All data in a Python program is represented by objects or by relations between objects. (In a sense, and in conformance to Von Neumann's model of a "stored program computer", code is also represented by objects.)

객체는 파이썬의 데이터에 대한 추상화입니다. 파이썬 프로그램의 모든 데이터는 객체나 객체 간의 관계로 표현됩니다. (어떤 의미에서, 그리고 폰 노이만의 "저장 프로그램 컴퓨터" 모델에 부합하여, 코드도 객체로 표현됩니다.)

Every object has an identity, a type and a value. An object's identity never changes once it has been created; you may think of it as the object's address in memory. The `is` operator compares the identity of two objects; the `id()` function returns an integer representing its identity.

모든 객체는 식별자(identity), 타입, 값을 가집니다. 객체의 식별자는 생성된 후에는 절대 변하지 않습니다. 이것을 메모리 상의 객체 주소라고 생각할 수 있습니다. `is` 연산자는 두 객체의 식별자를 비교합니다. `id()` 함수는 객체의 식별자를 나타내는 정수를 반환합니다.

CPython implementation detail: For CPython, `id(x)` is the memory address where x is stored.

CPython 구현 세부 사항: CPython에서 `id(x)`는 x가 저장된 메모리 주소입니다.

An object's type determines the operations that the object supports (e.g., "does it have a length?") and also defines the possible values for objects of that type. The `type()` function returns an object's type (which is an object itself). Like its identity, an object's type is also unchangeable. [1]

객체의 타입은 객체가 지원하는 연산(예: "길이가 있나요?")을 결정하고 해당 타입의 객체에 대해 가능한 값을 정의합니다. `type()` 함수는 객체의 타입(이 자체도 객체임)을 반환합니다. 식별자와 마찬가지로 객체의 타입도 변경할 수 없습니다. [1]

The value of some objects can change. Objects whose value can change are said to be mutable; objects whose value is unchangeable once they are created are called immutable. (The value of an immutable container object that contains a reference to a mutable object can change when the latter's value is changed; however the container is still considered immutable, because the collection of objects it contains cannot be changed. So, immutability is not strictly the same as having an unchangeable value, it is more subtle.) An object's mutability is determined by its type; for instance, numbers, strings and tuples are immutable, while dictionaries and lists are mutable.

일부 객체의 값은 변경될 수 있습니다. 값이 변경될 수 있는 객체는 가변(mutable)이라고 하며, 생성된 후 값이 변경될 수 없는 객체는 불변(immutable)이라고 합니다. (가변 객체에 대한 참조를 포함하는 불변 컨테이너 객체의 값은 가변 객체의 값이 변경될 때 변경될 수 있습니다. 그러나 컨테이너는 여전히 불변으로 간주됩니다. 왜냐하면 컨테이너가 포함하는 객체의 집합은 변경할 수 없기 때문입니다. 따라서 불변성은 값이 변경 불가능하다는 것과 엄밀히 같은 개념이 아니며, 더 미묘합니다.) 객체의 가변성은 타입에 의해 결정됩니다. 예를 들어, 숫자, 문자열, 튜플은 불변이고, 딕셔너리와 리스트는 가변입니다.

Objects are never explicitly destroyed; however, when they become unreachable they may be garbage-collected. An implementation is allowed to postpone garbage collection or omit it altogether — it is a matter of implementation quality how garbage collection is implemented, as long as no objects are collected that are still reachable.

객체는 명시적으로 파괴되지 않습니다. 그러나 도달할 수 없게 되면 가비지 컬렉션될 수 있습니다. 구현은 가비지 컬렉션을 연기하거나 완전히 생략할 수 있습니다. 여전히 도달 가능한 객체가 수집되지 않는 한, 가비지 컬렉션이 어떻게 구현되는지는 구현 품질의 문제입니다.

CPython implementation detail: CPython currently uses a reference-counting scheme with (optional) delayed detection of cyclically linked garbage, which collects most objects as soon as they become unreachable, but is not guaranteed to collect garbage containing circular references. See the documentation of the `gc` module for information on controlling the collection of cyclic garbage. Other implementations act differently and CPython may change. Do not depend on immediate finalization of objects when they become unreachable (so you should always close files explicitly).

CPython 구현 세부 사항: CPython은 현재 순환적으로 연결된 가비지의 (선택적) 지연 감지와 함께 참조 카운팅 방식을 사용합니다. 이는 대부분의 객체가 도달할 수 없게 되자마자 수집되지만, 순환 참조를 포함하는 가비지를 수집한다고 보장하지는 않습니다. 순환 가비지 수집을 제어하는 방법에 대한 정보는 `gc` 모듈 문서를 참조하세요. 다른 구현은 다르게 작동할 수 있으며 CPython도 변경될 수 있습니다. 객체가 도달 불가능해졌을 때 즉각적인 종료에 의존하지 마세요(따라서 항상 파일을 명시적으로 닫아야 합니다).

Note that the use of the implementation's tracing or debugging facilities may keep objects alive that would normally be collectable. Also note that catching an exception with a `try…except` statement may keep objects alive.

구현의 추적 또는 디버깅 기능을 사용하면 일반적으로 수집될 수 있는 객체가 살아있을 수 있습니다. 또한 `try…except` 문으로 예외를 잡으면 객체가 살아있을 수 있다는 점에 유의하세요.

Some objects contain references to "external" resources such as open files or windows. It is understood that these resources are freed when the object is garbage-collected, but since garbage collection is not guaranteed to happen, such objects also provide an explicit way to release the external resource, usually a `close()` method. Programs are strongly recommended to explicitly close such objects. The `try…finally` statement and the `with` statement provide convenient ways to do this.

일부 객체는 열린 파일이나 창과 같은 "외부" 리소스에 대한 참조를 포함합니다. 이러한 리소스는 객체가 가비지 컬렉션될 때 해제되지만, 가비지 컬렉션이 발생한다는 보장이 없으므로, 이러한 객체는 일반적으로 `close()` 메서드와 같은 외부 리소스를 해제하는 명시적인 방법을 제공합니다. 프로그램은 이러한 객체를 명시적으로 닫는 것이 강력히 권장됩니다. `try…finally` 문과 `with` 문은 이를 수행하는 편리한 방법을 제공합니다.

Some objects contain references to other objects; these are called containers. Examples of containers are tuples, lists and dictionaries. The references are part of a container's value. In most cases, when we talk about the value of a container, we imply the values, not the identities of the contained objects; however, when we talk about the mutability of a container, only the identities of the immediately contained objects are implied. So, if an immutable container (like a tuple) contains a reference to a mutable object, its value changes if that mutable object is changed.

일부 객체는 다른 객체에 대한 참조를 포함합니다. 이를 컨테이너라고 합니다. 컨테이너의 예로는 튜플, 리스트, 딕셔너리가 있습니다. 이러한 참조는 컨테이너 값의 일부입니다. 대부분의 경우 컨테이너의 값에 대해 이야기할 때, 우리는 포함된 객체의 식별자가 아닌 값을 의미합니다. 그러나 컨테이너의 가변성에 대해 이야기할 때는 직접 포함된 객체의 식별자만 의미합니다. 따라서 불변 컨테이너(튜플과 같은)가 가변 객체에 대한 참조를 포함하는 경우, 해당 가변 객체가 변경되면 불변 컨테이너의 값도 변경됩니다.

Types affect almost all aspects of object behavior. Even the importance of object identity is affected in some sense: for immutable types, operations that compute new values may actually return a reference to any existing object with the same type and value, while for mutable objects this is not allowed. For example, after `a = 1; b = 1`, `a` and `b` may or may not refer to the same object with the value one, depending on the implementation. This is because `int` is an immutable type, so the reference to 1 can be reused. This behaviour depends on the implementation used, so should not be relied upon, but is something to be aware of when making use of object identity tests. However, after `c = []; d = []`, `c` and `d` are guaranteed to refer to two different, unique, newly created empty lists. (Note that `e = f = []` assigns the same object to both `e` and `f`.)

타입은 객체 동작의 거의 모든 측면에 영향을 미칩니다. 심지어 객체 식별자의 중요성도 어떤 의미에서 영향을 받습니다. 불변 타입의 경우, 새 값을 계산하는 연산은 실제로 동일한 타입과 값을 가진 기존 객체에 대한 참조를 반환할 수 있지만, 가변 객체의 경우에는 이것이 허용되지 않습니다. 예를 들어, `a = 1; b = 1` 후에 `a`와 `b`는 구현에 따라 값이 1인 동일한 객체를 참조할 수도 있고 아닐 수도 있습니다. 이는 `int`가 불변 타입이므로 1에 대한 참조를 재사용할 수 있기 때문입니다. 이 동작은 사용된 구현에 따라 달라지므로 의존해서는 안 되지만, 객체 식별자 테스트를 사용할 때 알아두어야 할 사항입니다. 그러나 `c = []; d = []` 후에 `c`와 `d`는 두 개의 서로 다른, 고유한, 새로 생성된 빈 리스트를 참조한다고 보장됩니다. (`e = f = []`는 `e`와 `f` 모두에 동일한 객체를 할당한다는 점에 유의하세요.)

## 3.2. The standard type hierarchy

## 3.2. 표준 타입 계층

Below is a list of the types that are built into Python. Extension modules (written in C, Java, or other languages, depending on the implementation) can define additional types. Future versions of Python may add types to the type hierarchy (e.g., rational numbers, efficiently stored arrays of integers, etc.), although such additions will often be provided via the standard library instead.

다음은 파이썬에 내장된 타입의 목록입니다. 확장 모듈(구현에 따라 C, Java 또는 기타 언어로 작성됨)은 추가 타입을 정의할 수 있습니다. 향후 파이썬 버전에서는 타입 계층에 타입을 추가할 수 있습니다(예: 유리수, 효율적으로 저장된 정수 배열 등). 그러한 추가는 대신 표준 라이브러리를 통해 제공되는 경우가 많습니다.

Some of the type descriptions below contain a paragraph listing 'special attributes.' These are attributes that provide access to the implementation and are not intended for general use. Their definition may change in the future.

아래의 일부 타입 설명에는 '특별 속성'을 나열한 단락이 포함되어 있습니다. 이러한 속성은 구현에 대한 액세스를 제공하며 일반적인 사용을 위한 것이 아닙니다. 그 정의는 향후 변경될 수 있습니다.

### 3.2.1. None

### 3.2.1. None

This type has a single value. There is a single object with this value. This object is accessed through the built-in name `None`. It is used to signify the absence of a value in many situations, e.g., it is returned from functions that don't explicitly return anything. Its truth value is false.

이 타입은 단일 값을 가집니다. 이 값을 가진 단일 객체가 있습니다. 이 객체는 내장 이름 `None`을 통해 접근됩니다. 많은 상황에서 값의 부재를 나타내는 데 사용됩니다. 예를 들어, 명시적으로 아무것도 반환하지 않는 함수에서 반환됩니다. 그 진리값은 거짓입니다.

### 3.2.2. NotImplemented

### 3.2.2. NotImplemented

This type has a single value. There is a single object with this value. This object is accessed through the built-in name `NotImplemented`. Numeric methods and rich comparison methods should return this value if they do not implement the operation for the operands provided. (The interpreter will then try the reflected operation, or some other fallback, depending on the operator.) It should not be evaluated in a boolean context.

이 타입은 단일 값을 가집니다. 이 값을 가진 단일 객체가 있습니다. 이 객체는 내장 이름 `NotImplemented`를 통해 접근됩니다. 숫자 메서드와 풍부한 비교 메서드는 제공된 피연산자에 대한 연산을 구현하지 않은 경우 이 값을 반환해야 합니다. (그런 다음 인터프리터는 연산자에 따라 반영된 연산이나 다른 대체 방법을 시도합니다.) 이것은 불리언 컨텍스트에서 평가되어서는 안 됩니다.

See Implementing the arithmetic operations for more details.

자세한 내용은 산술 연산 구현을 참조하세요.

Changed in version 3.9: Evaluating `NotImplemented` in a boolean context is deprecated. While it currently evaluates as true, it will emit a DeprecationWarning. It will raise a TypeError in a future version of Python.

버전 3.9에서 변경됨: 불리언 컨텍스트에서 `NotImplemented`를 평가하는 것은 더 이상 사용되지 않습니다. 현재는 참으로 평가되지만 DeprecationWarning을 발생시킵니다. 향후 파이썬 버전에서는 TypeError를 발생시킬 것입니다.

### 3.2.3. Ellipsis

### 3.2.3. Ellipsis

This type has a single value. There is a single object with this value. This object is accessed through the literal `...` or the built-in name `Ellipsis`. Its truth value is true.

이 타입은 단일 값을 가집니다. 이 값을 가진 단일 객체가 있습니다. 이 객체는 리터럴 `...` 또는 내장 이름 `Ellipsis`를 통해 접근됩니다. 그 진리값은 참입니다.

### 3.2.4. numbers.Number

### 3.2.4. numbers.Number

These are created by numeric literals and returned as results by arithmetic operators and arithmetic built-in functions. Numeric objects are immutable; once created their value never changes. Python numbers are of course strongly related to mathematical numbers, but subject to the limitations of numerical representation in computers.

이들은 숫자 리터럴에 의해 생성되고 산술 연산자 및 산술 내장 함수에 의해 결과로 반환됩니다. 숫자 객체는 불변입니다. 한 번 생성되면 그 값은 절대 변하지 않습니다. 파이썬 숫자는 물론 수학적 숫자와 강하게 연관되어 있지만, 컴퓨터에서의 수치 표현의 제한을 받습니다.

The string representations of the numeric classes, computed by `__repr__()` and `__str__()`, have the following properties:

`__repr__()`과 `__str__()`에 의해 계산되는 숫자 클래스의 문자열 표현은 다음과 같은 속성을 갖습니다:

- They are valid numeric literals which, when passed to their class constructor, produce an object having the value of the original numeric.

- 이들은 유효한 숫자 리터럴로, 클래스 생성자에 전달되면 원래 숫자의 값을 가진 객체를 생성합니다.

- The representation is in base 10, when possible.

- 가능한 경우 표현은 10진수입니다.

- Leading zeros, possibly excepting a single zero before a decimal point, are not shown.

- 소수점 앞의 단일 0을 제외하고, 선행 0은 표시되지 않습니다.

- Trailing zeros, possibly excepting a single zero after a decimal point, are not shown.

- 소수점 뒤의 단일 0을 제외하고, 후행 0은 표시되지 않습니다.

- A sign is shown only when the number is negative.

- 부호는 숫자가 음수일 때만 표시됩니다.

Python distinguishes between integers, floating-point numbers, and complex numbers:

파이썬은 정수, 부동 소수점 수, 복소수를 구분합니다:

#### 3.2.4.1. numbers.Integral

#### 3.2.4.1. numbers.Integral

These represent elements from the mathematical set of integers (positive and negative).

이들은 수학적 정수 집합(양수 및 음수)의 원소를 나타냅니다.

Note: The rules for integer representation are intended to give the most meaningful interpretation of shift and mask operations involving negative integers.

참고: 정수 표현에 대한 규칙은 음수를 포함하는 시프트 및 마스크 연산의 가장 의미 있는 해석을 제공하기 위한 것입니다.

There are two types of integers:

정수에는 두 가지 유형이 있습니다:

Integers (`int`)

정수 (`int`)

These represent numbers in an unlimited range, subject to available (virtual) memory only. For the purpose of shift and mask operations, a binary representation is assumed, and negative numbers are represented in a variant of 2's complement which gives the illusion of an infinite string of sign bits extending to the left.

이들은 사용 가능한 (가상) 메모리에만 제한되는 무제한 범위의 숫자를 나타냅니다. 시프트 및 마스크 연산의 목적을 위해 이진 표현이 가정되며, 음수는 왼쪽으로 확장되는 무한한 부호 비트 문자열의 환상을 제공하는 2의 보수 변형으로 표현됩니다.

Booleans (`bool`)

불리언 (`bool`)

These represent the truth values False and True. The two objects representing the values False and True are the only Boolean objects. The Boolean type is a subtype of the integer type, and Boolean values behave like the values 0 and 1, respectively, in almost all contexts, the exception being that when converted to a string, the strings "False" or "True" are returned, respectively.

이들은 진리값 False와 True를 나타냅니다. 값 False와 True를 나타내는 두 객체는 유일한 불리언 객체입니다. 불리언 타입은 정수 타입의 하위 타입이며, 불리언 값은 거의 모든 컨텍스트에서 각각 값 0과 1처럼 동작합니다. 예외적으로 문자열로 변환될 때는 각각 "False" 또는 "True" 문자열이 반환됩니다.

#### 3.2.4.2. numbers.Real (float)

#### 3.2.4.2. numbers.Real (float)

These represent machine-level double precision floating-point numbers. You are at the mercy of the underlying machine architecture (and C or Java implementation) for the accepted range and handling of overflow. Python does not support single-precision floating-point numbers; the savings in processor and memory usage that are usually the reason for using these are dwarfed by the overhead of using objects in Python, so there is no reason to complicate the language with two kinds of floating-point numbers.

이들은 기계 수준의 배정밀도 부동 소수점 수를 나타냅니다. 허용 범위와 오버플로 처리는 기본 기계 아키텍처(및 C 또는 Java 구현)에 따릅니다. 파이썬은 단정밀도 부동 소수점 수를 지원하지 않습니다. 이를 사용하는 이유가 되는 프로세서 및 메모리 사용의 절약은 파이썬에서 객체를 사용하는 오버헤드에 비해 미미하므로, 두 종류의 부동 소수점 수로 언어를 복잡하게 할 이유가 없습니다.

#### 3.2.4.3. numbers.Complex (complex)

#### 3.2.4.3. numbers.Complex (complex)

These represent complex numbers as a pair of machine-level double precision floating-point numbers. The same caveats apply as for floating-point numbers. The real and imaginary parts of a complex number z can be retrieved through the read-only attributes z.real and z.imag.

이들은 복소수를 기계 수준의 배정밀도 부동 소수점 수 쌍으로 나타냅니다. 부동 소수점 수와 동일한 주의 사항이 적용됩니다. 복소수 z의 실수 부분과 허수 부분은 읽기 전용 속성 z.real과 z.imag를 통해 검색할 수 있습니다.

### 3.2.5. Sequences

### 3.2.5. 시퀀스

These represent finite ordered sets indexed by non-negative numbers. The built-in function `len()` returns the number of items of a sequence. When the length of a sequence is n, the index set contains the numbers 0, 1, …, n-1. Item i of sequence a is selected by `a[i]`. Some sequences, including built-in sequences, interpret negative subscripts by adding the sequence length. For example, a[-2] equals a[n-2], the second to last item of sequence a with length n.

이들은 음이 아닌 숫자로 인덱싱된 유한한 순서가 있는 집합을 나타냅니다. 내장 함수 `len()`은 시퀀스의 항목 수를 반환합니다. 시퀀스의 길이가 n일 때, 인덱스 집합은 숫자 0, 1, …, n-1을 포함합니다. 시퀀스 a의 i번째 항목은 `a[i]`로 선택됩니다. 내장 시퀀스를 포함한 일부 시퀀스는 시퀀스 길이를 더해 음수 첨자를 해석합니다. 예를 들어, a[-2]는 a[n-2]와 같으며, 이는 길이가 n인 시퀀스 a의 뒤에서 두 번째 항목입니다.

Sequences also support slicing: `a[i:j]` selects all items with index k such that i <= k < j. When used as an expression, a slice is a sequence of the same type. The comment above about negative indexes also applies to negative slice positions.

시퀀스는 또한 슬라이싱을 지원합니다: `a[i:j]`는 i <= k < j를 만족하는 인덱스 k를 가진 모든 항목을 선택합니다. 표현식으로 사용될 때 슬라이스는 동일한 타입의 시퀀스입니다. 음수 인덱스에 관한 위의 설명은 음수 슬라이스 위치에도 적용됩니다.

Some sequences also support "extended slicing" with a third "step" parameter: `a[i:j:k]` selects all items of a with index x where x = i + n*k, n >= 0 and i <= x < j.

일부 시퀀스는 세 번째 "단계" 매개변수를 사용한 "확장 슬라이싱"도 지원합니다: `a[i:j:k]`는 x = i + n*k, n >= 0 및 i <= x < j인 인덱스 x를 가진 a의 모든 항목을 선택합니다.

Sequences are distinguished according to their mutability:

시퀀스는 가변성에 따라 구분됩니다:

#### 3.2.5.1. Immutable sequences

#### 3.2.5.1. 불변 시퀀스

An object of an immutable sequence type cannot change once it is created. (If the object contains references to other objects, these other objects may be mutable and may be changed; however, the collection of objects directly referenced by an immutable object cannot change.)

불변 시퀀스 타입의 객체는 생성된 후에는 변경될 수 없습니다. (객체가 다른 객체에 대한 참조를 포함하는 경우, 이러한 다른 객체는 가변일 수 있으며 변경될 수 있습니다. 그러나 불변 객체에 의해 직접 참조되는 객체의 집합은 변경될 수 없습니다.)

The following types are immutable sequences:

다음 타입은 불변 시퀀스입니다:

Strings

문자열

A string is a sequence of values that represent Unicode code points. All the code points in the range U+0000 - U+10FFFF can be represented in a string. Python doesn't have a char type; instead, every code point in the string is represented as a string object with length 1. The built-in function `ord()` converts a code point from its string form to an integer in the range 0 - 10FFFF; `chr()` converts an integer in the range 0 - 10FFFF to the corresponding length 1 string object. `str.encode()` can be used to convert a str to bytes using the given text encoding, and `bytes.decode()` can be used to achieve the opposite.

문자열은 유니코드 코드 포인트를 나타내는 값의 시퀀스입니다. U+0000 - U+10FFFF 범위의 모든 코드 포인트는 문자열에서 표현될 수 있습니다. 파이썬에는 char 타입이 없습니다. 대신, 문자열의 모든 코드 포인트는 길이가 1인 문자열 객체로 표현됩니다. 내장 함수 `ord()`는 코드 포인트를 문자열 형태에서 0 - 10FFFF 범위의 정수로 변환합니다. `chr()`는 0 - 10FFFF 범위의 정수를 해당하는 길이 1의 문자열 객체로 변환합니다. `str.encode()`는 주어진 텍스트 인코딩을 사용하여 str을 bytes로 변환하는 데 사용할 수 있으며, `bytes.decode()`는 그 반대를 달성하는 데 사용할 수 있습니다.

Tuples

튜플

The items of a tuple are arbitrary Python objects. Tuples of two or more items are formed by comma-separated lists of expressions. A tuple of one item (a 'singleton') can be formed by affixing a comma to an expression (an expression by itself does not create a tuple, since parentheses must be usable for grouping of expressions). An empty tuple can be formed by an empty pair of parentheses.

튜플의 항목은 임의의 파이썬 객체입니다. 두 개 이상의 항목을 가진 튜플은 쉼표로 구분된 표현식 목록으로 형성됩니다. 한 항목(싱글톤)의 튜플은 표현식에 쉼표를 붙여 형성할 수 있습니다(표현식 자체는 튜플을 생성하지 않습니다. 괄호는 표현식의 그룹화에 사용할 수 있어야 하기 때문입니다). 빈 튜플은 빈 괄호 쌍으로 형성될 수 있습니다.

Bytes

바이트

A bytes object is an immutable array. The items are 8-bit bytes, represented by integers in the range 0 <= x < 256. Bytes literals (like b'abc') and the built-in `bytes()` constructor can be used to create bytes objects. Also, bytes objects can be decoded to strings via the `decode()` method.

bytes 객체는 불변 배열입니다. 항목은 8비트 바이트로, 0 <= x < 256 범위의 정수로 표현됩니다. 바이트 리터럴(b'abc'와 같은) 및 내장 `bytes()` 생성자는 bytes 객체를 생성하는 데 사용할 수 있습니다. 또한, bytes 객체는 `decode()` 메서드를 통해 문자열로 디코딩될 수 있습니다.

#### 3.2.5.2. Mutable sequences

#### 3.2.5.2. 가변 시퀀스

Mutable sequences can be changed after they are created. The subscription and slicing notations can be used as the target of assignment and del (delete) statements.

가변 시퀀스는 생성된 후 변경될 수 있습니다. 첨자 및 슬라이싱 표기법은 할당 및 del(삭제) 문의 대상으로 사용될 수 있습니다.

Note: The collections and array module provide additional examples of mutable sequence types.

참고: collections 및 array 모듈은 가변 시퀀스 타입의 추가 예를 제공합니다.

There are currently two intrinsic mutable sequence types:

현재 두 가지 내장 가변 시퀀스 타입이 있습니다:

Lists

리스트

The items of a list are arbitrary Python objects. Lists are formed by placing a comma-separated list of expressions in square brackets. (Note that there are no special cases needed to form lists of length 0 or 1.)

리스트의 항목은 임의의 파이썬 객체입니다. 리스트는 대괄호 안에 쉼표로 구분된 표현식 목록을 배치하여 형성됩니다. (길이가 0 또는 1인 리스트를 형성하기 위해 특별한 경우가 필요하지 않다는 점에 유의하세요.)

Byte Arrays

바이트 배열

A bytearray object is a mutable array. They are created by the built-in `bytearray()` constructor. Aside from being mutable (and hence unhashable), byte arrays otherwise provide the same interface and functionality as immutable bytes objects.

bytearray 객체는 가변 배열입니다. 이들은 내장 `bytearray()` 생성자에 의해 생성됩니다. 가변(따라서 해시 불가능)이라는 점을 제외하면, 바이트 배열은 불변 bytes 객체와 동일한 인터페이스 및 기능을 제공합니다.

### 3.2.6. Set types

### 3.2.6. 집합 타입

These represent unordered, finite sets of unique, immutable objects. As such, they cannot be indexed by any subscript. However, they can be iterated over, and the built-in function `len()` returns the number of items in a set. Common uses for sets are fast membership testing, removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference, and symmetric difference.

이들은 고유하고 불변인 객체의 순서가 없는 유한 집합을 나타냅니다. 따라서 어떤 첨자로도 인덱싱할 수 없습니다. 그러나 반복할 수 있으며, 내장 함수 `len()`은 집합의 항목 수를 반환합니다. 집합의 일반적인 사용법으로는 빠른 멤버십 테스트, 시퀀스에서 중복 제거, 교집합, 합집합, 차집합 및 대칭 차집합과 같은 수학적 연산 계산 등이 있습니다.

For set elements, the same immutability rules apply as for dictionary keys. Note that numeric types obey the normal rules for numeric comparison: if two numbers compare equal (e.g., 1 and 1.0), only one of them can be contained in a set.

집합 요소에 대해서는 딕셔너리 키와 동일한 불변성 규칙이 적용됩니다. 숫자 타입은 숫자 비교에 대한 일반적인 규칙을 따른다는 점에 유의하세요. 두 숫자가 동일하게 비교되면(예: 1과 1.0), 집합에는 그 중 하나만 포함될 수 있습니다.

There are currently two intrinsic set types:

현재 두 가지 내장 집합 타입이 있습니다:

Sets

집합

These represent a mutable set. They are created by the built-in `set()` constructor and can be modified afterwards by several methods, such as `add()`.

이들은 가변 집합을 나타냅니다. 내장 `set()` 생성자에 의해 생성되며 이후 `add()`와 같은 여러 메서드로 수정될 수 있습니다.

Frozen sets

고정 집합

These represent an immutable set. They are created by the built-in `frozenset()` constructor. As a frozenset is immutable and hashable, it can be used again as an element of another set, or as a dictionary key.

이들은 불변 집합을 나타냅니다. 내장 `frozenset()` 생성자에 의해 생성됩니다. frozenset은 불변이며 해시 가능하므로, 다른 집합의 요소나 딕셔너리 키로 다시 사용될 수 있습니다.

### 3.2.7. Mappings

### 3.2.7. 매핑

These represent finite sets of objects indexed by arbitrary index sets. The subscript notation `a[k]` selects the item indexed by k from the mapping a; this can be used in expressions and as the target of assignments or del statements. The built-in function `len()` returns the number of items in a mapping.

이들은 임의의 인덱스 집합으로 인덱싱된 유한한 객체 집합을 나타냅니다. 첨자 표기법 `a[k]`는 매핑 a에서 k로 인덱싱된 항목을 선택합니다. 이는 표현식에서 사용될 수 있으며 할당이나 del 문의 대상으로도 사용될 수 있습니다. 내장 함수 `len()`은 매핑의 항목 수를 반환합니다.

There is currently a single intrinsic mapping type:

현재 단일 내장 매핑 타입이 있습니다:

#### 3.2.7.1. Dictionaries

#### 3.2.7.1. 딕셔너리

These represent finite sets of objects indexed by nearly arbitrary values. The only types of values not acceptable as keys are values containing lists or dictionaries or other mutable types that are compared by value rather than by object identity, the reason being that the efficient implementation of dictionaries requires a key's hash value to remain constant. Numeric types used for keys obey the normal rules for numeric comparison: if two numbers compare equal (e.g., 1 and 1.0) then they can be used interchangeably to index the same dictionary entry.

이들은 거의 임의의 값으로 인덱싱된 유한한 객체 집합을 나타냅니다. 키로 허용되지 않는 유일한 값 타입은 리스트나 딕셔너리 또는 객체 식별자가 아닌 값으로 비교되는 다른 가변 타입을 포함하는 값입니다. 그 이유는 딕셔너리의 효율적인 구현을 위해 키의 해시 값이 일정하게 유지되어야 하기 때문입니다. 키로 사용되는 숫자 타입은 숫자 비교에 대한 일반적인 규칙을 따릅니다: 두 숫자가 동일하게 비교되면(예: 1과 1.0) 동일한 딕셔너리 항목을 인덱싱하는 데 서로 바꿔 사용할 수 있습니다.

Dictionaries preserve insertion order, meaning that keys will be produced in the same order they were added sequentially over the dictionary. Replacing an existing key does not change the order, however removing a key and re-inserting it will add it to the end instead of keeping its old place.

딕셔너리는 삽입 순서를 유지합니다. 즉, 키는 딕셔너리에 순차적으로 추가된 순서와 동일한 순서로 생성됩니다. 기존 키를 교체해도 순서는 변경되지 않지만, 키를 제거하고 다시 삽입하면 이전 위치를 유지하는 대신 끝에 추가됩니다.

Dictionaries are mutable; they can be created by the `{}` notation (see section Dictionary displays).

딕셔너리는 가변입니다. `{}` 표기법으로 생성할 수 있습니다(딕셔너리 표시 섹션 참조).

The extension modules dbm.ndbm and dbm.gnu provide additional examples of mapping types, as does the collections module.

확장 모듈 dbm.ndbm 및 dbm.gnu는 매핑 타입의 추가 예를 제공하며, collections 모듈도 마찬가지입니다.

Changed in version 3.7: Dictionaries did not preserve insertion order in versions of Python before 3.6. In CPython 3.6, insertion order was preserved, but it was considered an implementation detail at that time rather than a language guarantee.

버전 3.7에서 변경됨: 파이썬 3.6 이전 버전에서는 딕셔너리가 삽입 순서를 유지하지 않았습니다. CPython 3.6에서는 삽입 순서가 유지되었지만, 당시에는 언어적 보장이 아닌 구현 세부 사항으로 간주되었습니다.

### 3.2.8. Callable types

### 3.2.8. 호출 가능 타입

These are the types to which the function call operation (see section Calls) can be applied:

이들은 함수 호출 연산(Calls 섹션 참조)을 적용할 수 있는 타입들입니다:

#### 3.2.8.1. User-defined functions

#### 3.2.8.1. 사용자 정의 함수

A user-defined function object is created by a function definition (see section Function definitions). It should be called with an argument list containing the same number of items as the function's formal parameter list.

사용자 정의 함수 객체는 함수 정의(함수 정의 섹션 참조)에 의해 생성됩니다. 함수의 형식 매개변수 목록과 동일한 수의 항목을 포함하는 인수 목록으로 호출해야 합니다.

##### 3.2.8.1.1. Special read-only attributes

##### 3.2.8.1.1. 특수 읽기 전용 속성

Attribute

속성

Meaning

의미

function.__globals__
A reference to the dictionary that holds the function's global variables – the global namespace of the module in which the function was defined.

function.__globals__
함수의 전역 변수를 보유하는 딕셔너리에 대한 참조 - 함수가 정의된 모듈의 전역 네임스페이스입니다.

function.__closure__
None or a tuple of cells that contain bindings for the names specified in the co_freevars attribute of the function's code object.

function.__closure__
None 또는 함수의 코드 객체의 co_freevars 속성에 지정된 이름에 대한 바인딩을 포함하는 셀의 튜플입니다.

A cell object has the attribute cell_contents. This can be used to get the value of the cell, as well as set the value.

셀 객체에는 cell_contents 속성이 있습니다. 이를 사용하여 셀의 값을 가져오거나 값을 설정할 수 있습니다.

##### 3.2.8.1.2. Special writable attributes

##### 3.2.8.1.2. 특수 쓰기 가능 속성

Most of these attributes check the type of the assigned value:

이러한 속성의 대부분은 할당된 값의 타입을 확인합니다:

Attribute

속성

Meaning

의미

function.__doc__
The function's documentation string, or None if unavailable.

function.__doc__
함수의 문서화 문자열 또는 사용할 수 없는 경우 None입니다.

function.__name__
The function's name. See also: __name__ attributes.

function.__name__
함수의 이름입니다. 참조: __name__ 속성.

function.__qualname__
The function's qualified name. See also: __qualname__ attributes.

function.__qualname__
함수의 정규화된 이름입니다. 참조: __qualname__ 속성.

Added in version 3.3.

버전 3.3에서 추가됨.

function.__module__
The name of the module the function was defined in, or None if unavailable.

function.__module__
함수가 정의된 모듈의 이름 또는 사용할 수 없는 경우 None입니다.

function.__defaults__
A tuple containing default parameter values for those parameters that have defaults, or None if no parameters have a default value.

function.__defaults__
기본값이 있는 매개변수에 대한 기본 매개변수 값을 포함하는 튜플 또는 기본값을 가진 매개변수가 없는 경우 None입니다.

function.__code__
The code object representing the compiled function body.

function.__code__
컴파일된 함수 본문을 나타내는 코드 객체입니다.

function.__dict__
The namespace supporting arbitrary function attributes. See also: __dict__ attributes.

function.__dict__
임의의 함수 속성을 지원하는 네임스페이스입니다. 참조: __dict__ 속성.

function.__annotations__
A dictionary containing annotations of parameters. The keys of the dictionary are the parameter names, and 'return' for the return annotation, if provided. See also: Annotations Best Practices.

function.__annotations__
매개변수의 주석을 포함하는 딕셔너리입니다. 딕셔너리의 키는 매개변수 이름이며, 반환 주석이 제공된 경우 'return'입니다. 참조: 주석 모범 사례.

function.__kwdefaults__
A dictionary containing defaults for keyword-only parameters.

function.__kwdefaults__
키워드 전용 매개변수에 대한 기본값을 포함하는 딕셔너리입니다.

function.__type_params__
A tuple containing the type parameters of a generic function.

function.__type_params__
제네릭 함수의 타입 매개변수를 포함하는 튜플입니다.

Added in version 3.12.

버전 3.12에서 추가됨.

Function objects also support getting and setting arbitrary attributes, which can be used, for example, to attach metadata to functions. Regular attribute dot-notation is used to get and set such attributes.

함수 객체는 또한 임의의 속성을 가져오고 설정하는 것을 지원합니다. 이는 예를 들어 함수에 메타데이터를 첨부하는 데 사용할 수 있습니다. 일반 속성 점 표기법이 이러한 속성을 가져오고 설정하는 데 사용됩니다.

CPython implementation detail: CPython's current implementation only supports function attributes on user-defined functions. Function attributes on built-in functions may be supported in the future.

CPython 구현 세부 사항: CPython의 현재 구현은 사용자 정의 함수에 대한 함수 속성만 지원합니다. 내장 함수에 대한 함수 속성은 향후에 지원될 수 있습니다.

Additional information about a function's definition can be retrieved from its code object (accessible via the __code__ attribute).

함수 정의에 관한 추가 정보는 코드 객체(__code__ 속성을 통해 접근 가능)에서 검색할 수 있습니다.

#### 3.2.8.2. Instance methods

#### 3.2.8.2. 인스턴스 메서드

An instance method object combines a class, a class instance and any callable object (normally a user-defined function).

인스턴스 메서드 객체는 클래스, 클래스 인스턴스 및 호출 가능한 객체(일반적으로 사용자 정의 함수)를 결합합니다.

Special read-only attributes:

특수 읽기 전용 속성:

method.__self__
Refers to the class instance object to which the method is bound

method.__self__
메서드가 바인딩된 클래스 인스턴스 객체를 참조합니다.

method.__func__
Refers to the original function object

method.__func__
원래 함수 객체를 참조합니다.

method.__doc__
The method's documentation (same as method.__func__.__doc__). A string if the original function had a docstring, else None.

method.__doc__
메서드의 문서화(method.__func__.__doc__와 동일). 원래 함수에 docstring이 있었다면 문자열, 그렇지 않으면 None입니다.

method.__name__
The name of the method (same as method.__func__.__name__)

method.__name__
메서드의 이름(method.__func__.__name__와 동일).

method.__module__
The name of the module the method was defined in, or None if unavailable.

method.__module__
메서드가 정의된 모듈의 이름 또는 사용할 수 없는 경우 None입니다.

Methods also support accessing (but not setting) the arbitrary function attributes on the underlying function object.

메서드는 또한 기본 함수 객체의 임의 함수 속성에 접근(설정은 불가)하는 것을 지원합니다.

User-defined method objects may be created when getting an attribute of a class (perhaps via an instance of that class), if that attribute is a user-defined function object or a classmethod object.

사용자 정의 메서드 객체는 클래스의 속성(아마도 그 클래스의 인스턴스를 통해)을 가져올 때 생성될 수 있으며, 그 속성이 사용자 정의 함수 객체 또는 classmethod 객체인 경우에 해당됩니다.

When an instance method object is created by retrieving a user-defined function object from a class via one of its instances, its `__self__` attribute is the instance, and the method object is said to be bound. The new method's `__func__` attribute is the original function object.

인스턴스 메서드 객체가 클래스에서 인스턴스 중 하나를 통해 사용자 정의 함수 객체를 검색하여 생성되면, 그 `__self__` 속성은 인스턴스이며, 메서드 객체는 바인딩되었다고 합니다. 새 메서드의 `__func__` 속성은 원래 함수 객체입니다.

When an instance method object is created by retrieving a classmethod object from a class or instance, its `__self__` attribute is the class itself, and its `__func__` attribute is the function object underlying the class method.

인스턴스 메서드 객체가 클래스나 인스턴스에서 classmethod 객체를 검색하여 생성되면, 그 `__self__` 속성은 클래스 자체이고, `__func__` 속성은 클래스 메서드 기반의 함수 객체입니다.

When an instance method object is called, the underlying function (`__func__`) is called, inserting the class instance (`__self__`) in front of the argument list. For instance, when C is a class which contains a definition for a function f(), and x is an instance of C, calling x.f(1) is equivalent to calling C.f(x, 1).

인스턴스 메서드 객체가 호출되면, 기본 함수(`__func__`)가 호출되고, 인수 목록 앞에 클래스 인스턴스(`__self__`)가 삽입됩니다. 예를 들어, C가 함수 f()에 대한 정의를 포함하는 클래스이고 x가 C의 인스턴스일 때, x.f(1)을 호출하는 것은 C.f(x, 1)을 호출하는 것과 동일합니다.

When an instance method object is derived from a classmethod object, the "class instance" stored in `__self__` will actually be the class itself, so that calling either x.f(1) or C.f(1) is equivalent to calling f(C,1) where f is the underlying function.

인스턴스 메서드 객체가 classmethod 객체에서 파생된 경우, `__self__`에 저장된 "클래스 인스턴스"는 실제로 클래스 자체가 됩니다. 따라서 x.f(1) 또는 C.f(1)을 호출하는 것은 f(C,1)을 호출하는 것과 동일하며, 여기서 f는 기본 함수입니다.

It is important to note that user-defined functions which are attributes of a class instance are not converted to bound methods; this only happens when the function is an attribute of the class.

클래스 인스턴스의 속성인 사용자 정의 함수는 바인딩된 메서드로 변환되지 않는다는 점에 유의하는 것이 중요합니다. 이는 함수가 클래스의 속성일 때만 발생합니다.

#### 3.2.8.3. Generator functions

#### 3.2.8.3. 제네레이터 함수

A function or method which uses the yield statement (see section The yield statement) is called a generator function. Such a function, when called, always returns an iterator object which can be used to execute the body of the function: calling the iterator's iterator.__next__() method will cause the function to execute until it provides a value using the yield statement. When the function executes a return statement or falls off the end, a StopIteration exception is raised and the iterator will have reached the end of the set of values to be returned.

yield 문을 사용하는 함수 또는 메서드(yield 문 섹션 참조)를 제네레이터 함수라고 합니다. 이러한 함수가 호출되면 항상 함수 본문을 실행하는 데 사용할 수 있는 반복자 객체를 반환합니다. 반복자의 iterator.__next__() 메서드를 호출하면 함수는 yield 문을 사용하여 값을 제공할 때까지 실행됩니다. 함수가 return 문을 실행하거나 끝까지 실행되면 StopIteration 예외가 발생하고 반복자는 반환될 값 집합의 끝에 도달하게 됩니다.

#### 3.2.8.4. Coroutine functions

#### 3.2.8.4. 코루틴 함수

A function or method which is defined using async def is called a coroutine function. Such a function, when called, returns a coroutine object. It may contain await expressions, as well as async with and async for statements. See also the Coroutine Objects section.

async def를 사용하여 정의된 함수 또는 메서드를 코루틴 함수라고 합니다. 이러한 함수가 호출되면 코루틴 객체를 반환합니다. await 표현식뿐만 아니라 async with 및 async for 문도 포함할 수 있습니다. 코루틴 객체 섹션도 참조하세요.

#### 3.2.8.5. Asynchronous generator functions

#### 3.2.8.5. 비동기 제네레이터 함수

A function or method which is defined using async def and which uses the yield statement is called a asynchronous generator function. Such a function, when called, returns an asynchronous iterator object which can be used in an async for statement to execute the body of the function.

async def를 사용하여 정의되고 yield 문을 사용하는 함수 또는 메서드를 비동기 제네레이터 함수라고 합니다. 이러한 함수가 호출되면 함수 본문을 실행하기 위해 async for 문에서 사용할 수 있는 비동기 반복자 객체를 반환합니다.

Calling the asynchronous iterator's aiterator.__anext__ method will return an awaitable which when awaited will execute until it provides a value using the yield expression. When the function executes an empty return statement or falls off the end, a StopAsyncIteration exception is raised and the asynchronous iterator will have reached the end of the set of values to be yielded.

비동기 반복자의 aiterator.__anext__ 메서드를 호출하면 대기 가능한(awaitable) 객체를 반환하며, 이를 대기(await)하면 yield 표현식을 사용하여 값을 제공할 때까지 실행됩니다. 함수가 빈 return 문을 실행하거나 끝까지 실행되면 StopAsyncIteration 예외가 발생하고 비동기 반복자는 생성될 값 집합의 끝에 도달하게 됩니다.

#### 3.2.8.6. Built-in functions

#### 3.2.8.6. 내장 함수

A built-in function object is a wrapper around a C function. Examples of built-in functions are len() and math.sin() (math is a standard built-in module). The number and type of the arguments are determined by the C function. Special read-only attributes:

내장 함수 객체는 C 함수를 감싸는 래퍼입니다. 내장 함수의 예로는 len()과 math.sin()이 있습니다(math는 표준 내장 모듈임). 인수의 수와 타입은 C 함수에 의해 결정됩니다. 특별 읽기 전용 속성:

__doc__ is the function's documentation string, or None if unavailable. See function.__doc__.

__doc__은 함수의 문서화 문자열이거나, 사용할 수 없는 경우 None입니다. function.__doc__을 참조하세요.

__name__ is the function's name. See function.__name__.

__name__은 함수의 이름입니다. function.__name__을 참조하세요.

__self__ is set to None (but see the next item).

__self__는 None으로 설정됩니다(그러나 다음 항목 참조).

__module__ is the name of the module the function was defined in or None if unavailable. See function.__module__.

__module__은 함수가 정의된 모듈의 이름이거나 사용할 수 없는 경우 None입니다. function.__module__을 참조하세요.

#### 3.2.8.7. Built-in methods

#### 3.2.8.7. 내장 메서드

This is really a different disguise of a built-in function, this time containing an object passed to the C function as an implicit extra argument. An example of a built-in method is alist.append(), assuming alist is a list object. In this case, the special read-only attribute __self__ is set to the object denoted by alist. (The attribute has the same semantics as it does with other instance methods.)

이것은 실제로 내장 함수의 다른 형태로, 이번에는 C 함수에 암시적 추가 인수로 전달되는 객체를 포함합니다. 내장 메서드의 예는 alist.append()입니다(alist가 리스트 객체라고 가정). 이 경우, 특별 읽기 전용 속성 __self__는 alist로 표시된 객체로 설정됩니다. (이 속성은 다른 인스턴스 메서드와 동일한 의미를 갖습니다.)

#### 3.2.8.8. Classes

#### 3.2.8.8. 클래스

Classes are callable. These objects normally act as factories for new instances of themselves, but variations are possible for class types that override __new__(). The arguments of the call are passed to __new__() and, in the typical case, to __init__() to initialize the new instance.

클래스는 호출 가능합니다. 이 객체들은 일반적으로 자신의 새 인스턴스를 위한 팩토리 역할을 하지만, __new__()를 재정의하는 클래스 타입의 경우 변형이 가능합니다. 호출의 인수는 __new__()에 전달되며, 일반적인 경우에는 새 인스턴스를 초기화하기 위해 __init__()에도 전달됩니다.

#### 3.2.8.9. Class Instances

#### 3.2.8.9. 클래스 인스턴스

Instances of arbitrary classes can be made callable by defining a __call__() method in their class.

임의의 클래스의 인스턴스는 해당 클래스에 __call__() 메서드를 정의하여 호출 가능하게 만들 수 있습니다.

### 3.2.9. Modules

### 3.2.9. 모듈

Modules are a basic organizational unit of Python code, and are created by the import system as invoked either by the import statement, or by calling functions such as importlib.import_module() and built-in __import__(). A module object has a namespace implemented by a dictionary object (this is the dictionary referenced by the __globals__ attribute of functions defined in the module). Attribute references are translated to lookups in this dictionary, e.g., m.x is equivalent to m.__dict__["x"]. A module object does not contain the code object used to initialize the module (since it isn't needed once the initialization is done).

모듈은 파이썬 코드의 기본 조직 단위이며, import 문에 의해 호출되거나 importlib.import_module() 및 내장 __import__()와 같은 함수를 호출하여 import 시스템에 의해 생성됩니다. 모듈 객체는 딕셔너리 객체로 구현된 네임스페이스를 가지고 있습니다(이것은 모듈에 정의된 함수의 __globals__ 속성에 의해 참조되는 딕셔너리입니다). 속성 참조는 이 딕셔너리에서의 조회로 변환됩니다. 예를 들어, m.x는 m.__dict__["x"]와 동일합니다. 모듈 객체는 모듈을 초기화하는 데 사용된 코드 객체를 포함하지 않습니다(초기화가 완료되면 필요하지 않기 때문).

Attribute assignment updates the module's namespace dictionary, e.g., m.x = 1 is equivalent to m.__dict__["x"] = 1.

속성 할당은 모듈의 네임스페이스 딕셔너리를 업데이트합니다. 예를 들어, m.x = 1은 m.__dict__["x"] = 1과 동일합니다.

#### 3.2.9.1. Import-related attributes on module objects

#### 3.2.9.1. 모듈 객체의 가져오기 관련 속성

Module objects have the following attributes that relate to the import system. When a module is created using the machinery associated with the import system, these attributes are filled in based on the module's spec, before the loader executes and loads the module.

모듈 객체는 import 시스템과 관련된 다음 속성을 가집니다. import 시스템과 관련된 기계를 사용하여 모듈이 생성될 때, 이러한 속성은 로더가 실행되고 모듈을 로드하기 전에 모듈의 스펙에 기반하여 채워집니다.

To create a module dynamically rather than using the import system, it's recommended to use importlib.util.module_from_spec(), which will set the various import-controlled attributes to appropriate values. It's also possible to use the types.ModuleType constructor to create modules directly, but this technique is more error-prone, as most attributes must be manually set on the module object after it has been created when using this approach.

import 시스템을 사용하는 대신 동적으로 모듈을 생성하려면, importlib.util.module_from_spec()를 사용하는 것이 권장됩니다. 이는 다양한 import 제어 속성을 적절한 값으로 설정합니다. types.ModuleType 생성자를 사용하여 모듈을 직접 생성하는 것도 가능하지만, 이 방식은 오류가 발생하기 쉽습니다. 대부분의 속성은 이 접근 방식을 사용할 때 생성된 후 모듈 객체에 수동으로 설정해야 하기 때문입니다.

Caution With the exception of __name__, it is strongly recommended that you rely on __spec__ and its attributes instead of any of the other individual attributes listed in this subsection. Note that updating an attribute on __spec__ will not update the corresponding attribute on the module itself:

주의 __name__을 제외하고, 이 하위 섹션에 나열된 다른 개별 속성 대신 __spec__ 및 그 속성에 의존하는 것이 강력히 권장됩니다. __spec__의 속성을 업데이트해도 모듈 자체의 해당 속성이 업데이트되지 않는다는 점에 유의하세요:

```python
>>>
import typing
typing.__name__, typing.__spec__.name
('typing', 'typing')
typing.__spec__.name = 'spelling'
typing.__name__, typing.__spec__.name
('typing', 'spelling')
typing.__name__ = 'keyboard_smashing'
typing.__name__, typing.__spec__.name
('keyboard_smashing', 'spelling')
```

module.__name__
The name used to uniquely identify the module in the import system. For a directly executed module, this will be set to "__main__".

module.__name__
import 시스템에서 모듈을 고유하게 식별하는 데 사용되는 이름입니다. 직접 실행되는 모듈의 경우, 이 값은 "__main__"으로 설정됩니다.

This attribute must be set to the fully qualified name of the module. It is expected to match the value of module.__spec__.name.

이 속성은 모듈의 정규화된 이름으로 설정되어야 합니다. module.__spec__.name 값과 일치할 것으로 예상됩니다.

module.__spec__
A record of the module's import-system-related state.

module.__spec__
모듈의 import 시스템 관련 상태 기록입니다.

Set to the module spec that was used when importing the module. See Module specs for more details.

모듈을 가져올 때 사용된 모듈 스펙으로 설정됩니다. 자세한 내용은 모듈 스펙을 참조하세요.

Added in version 3.4.

버전 3.4에서 추가됨.

module.__package__
The package a module belongs to.

module.__package__
모듈이 속한 패키지입니다.

If the module is top-level (that is, not a part of any specific package) then the attribute should be set to '' (the empty string). Otherwise, it should be set to the name of the module's package (which can be equal to module.__name__ if the module itself is a package). See PEP 366 for further details.

모듈이 최상위 수준인 경우(즉, 특정 패키지의 일부가 아닌 경우) 이 속성은 ''(빈 문자열)로 설정되어야 합니다. 그렇지 않으면 모듈의 패키지 이름으로 설정되어야 합니다(모듈 자체가 패키지인 경우 module.__name__과 동일할 수 있음). 자세한 내용은 PEP 366을 참조하세요.

This attribute is used instead of __name__ to calculate explicit relative imports for main modules. It defaults to None for modules created dynamically using the types.ModuleType constructor; use importlib.util.module_from_spec() instead to ensure the attribute is set to a str.

이 속성은 메인 모듈에 대한 명시적 상대 가져오기를 계산하기 위해 __name__ 대신 사용됩니다. types.ModuleType 생성자를 사용하여 동적으로 생성된 모듈의 경우 기본값은 None입니다. 대신 importlib.util.module_from_spec()을 사용하여 속성이 str로 설정되도록 하세요.

It is strongly recommended that you use module.__spec__.parent instead of module.__package__. __package__ is now only used as a fallback if __spec__.parent is not set, and this fallback path is deprecated.

module.__spec__.parent를 module.__package__ 대신 사용하는 것이 강력히 권장됩니다. __package__는 현재 __spec__.parent가 설정되지 않은 경우에만 대체로 사용되며, 이 대체 경로는 더 이상 사용되지 않습니다.

Changed in version 3.4: This attribute now defaults to None for modules created dynamically using the types.ModuleType constructor. Previously the attribute was optional.

버전 3.4에서 변경됨: 이제 이 속성은 types.ModuleType 생성자를 사용하여 동적으로 생성된 모듈의 경우 기본값이 None입니다. 이전에는 이 속성이 선택사항이었습니다.

Changed in version 3.6: The value of __package__ is expected to be the same as __spec__.parent. __package__ is now only used as a fallback during import resolution if __spec__.parent is not defined.

버전 3.6에서 변경됨: __package__ 값은 __spec__.parent와 동일할 것으로 예상됩니다. __package__는 이제 가져오기 해결 중에 __spec__.parent가 정의되지 않은 경우에만 대체로 사용됩니다.

Changed in version 3.10: ImportWarning is raised if an import resolution falls back to __package__ instead of __spec__.parent.

버전 3.10에서 변경됨: 가져오기 해결이 __spec__.parent 대신 __package__로 대체되는 경우 ImportWarning이 발생합니다.

Changed in version 3.12: Raise DeprecationWarning instead of ImportWarning when falling back to __package__ during import resolution.

버전 3.12에서 변경됨: 가져오기 해결 중에 __package__로 대체할 때 ImportWarning 대신 DeprecationWarning을 발생시킵니다.

Deprecated since version 3.13, will be removed in version 3.15: __package__ will cease to be set or taken into consideration by the import system or standard library.

버전 3.13부터 더 이상 사용되지 않으며, 버전 3.15에서 제거될 예정: __package__는 import 시스템이나 표준 라이브러리에 의해 설정되거나 고려되지 않을 것입니다.

module.__loader__
The loader object that the import machinery used to load the module.

module.__loader__
import 기계가 모듈을 로드하는 데 사용한 로더 객체입니다.

This attribute is mostly useful for introspection, but can be used for additional loader-specific functionality, for example getting data associated with a loader.

이 속성은 주로 내부 검사에 유용하지만, 로더 관련 추가 기능(예: 로더와 관련된 데이터 가져오기)에 사용될 수 있습니다.

__loader__ defaults to None for modules created dynamically using the types.ModuleType constructor; use importlib.util.module_from_spec() instead to ensure the attribute is set to a loader object.

__loader__는 types.ModuleType 생성자를 사용하여 동적으로 생성된 모듈의 경우 기본값이 None입니다. 대신 importlib.util.module_from_spec()을 사용하여 속성이 로더 객체로 설정되도록 하세요.

It is strongly recommended that you use module.__spec__.loader instead of module.__loader__.

module.__spec__.loader를 module.__loader__ 대신 사용하는 것이 강력히 권장됩니다.

Changed in version 3.4: This attribute now defaults to None for modules created dynamically using the types.ModuleType constructor. Previously the attribute was optional.

버전 3.4에서 변경됨: 이제 이 속성은 types.ModuleType 생성자를 사용하여 동적으로 생성된 모듈의 경우 기본값이 None입니다. 이전에는 이 속성이 선택사항이었습니다.

Deprecated since version 3.12, will be removed in version 3.16: Setting __loader__ on a module while failing to set __spec__.loader is deprecated. In Python 3.16, __loader__ will cease to be set or taken into consideration by the import system or the standard library.

버전 3.12부터 더 이상 사용되지 않으며, 버전 3.16에서 제거될 예정: __spec__.loader를 설정하지 못하면서 모듈에 __loader__를 설정하는 것은 더 이상 사용되지 않습니다. 파이썬 3.16에서는 __loader__가 import 시스템이나 표준 라이브러리에 의해 설정되거나 고려되지 않을 것입니다.

module.__path__
A (possibly empty) sequence of strings enumerating the locations where the package's submodules will be found. Non-package modules should not have a __path__ attribute. See __path__ attributes on modules for more details.

module.__path__
패키지의 하위 모듈이 발견될 위치를 열거하는 문자열의 (가능한 빈) 시퀀스입니다. 패키지가 아닌 모듈은 __path__ 속성을 가지지 않아야 합니다. 자세한 내용은 모듈의 __path__ 속성을 참조하세요.

It is strongly recommended that you use module.__spec__.submodule_search_locations instead of module.__path__.

module.__spec__.submodule_search_locations를 module.__path__ 대신 사용하는 것이 강력히 권장됩니다.

module.__file__
module.__cached__
__file__ and __cached__ are both optional attributes that may or may not be set. Both attributes should be a str when they are available.

module.__file__
module.__cached__
__file__과 __cached__는 모두 설정될 수도 있고 설정되지 않을 수도 있는 선택적 속성입니다. 두 속성 모두 사용할 수 있을 때는 str이어야 합니다.

__file__ indicates the pathname of the file from which the module was loaded (if loaded from a file), or the pathname of the shared library file for extension modules loaded dynamically from a shared library. It might be missing for certain types of modules, such as C modules that are statically linked into the interpreter, and the import system may opt to leave it unset if it has no semantic meaning (for example, a module loaded from a database).

__file__은 모듈이 로드된 파일의 경로 이름(파일에서 로드된 경우) 또는 공유 라이브러리에서 동적으로 로드된 확장 모듈의 공유 라이브러리 파일의 경로 이름을 나타냅니다. 인터프리터에 정적으로 링크된 C 모듈과 같은 특정 유형의 모듈에는 없을 수 있으며, import 시스템은 의미론적 의미가 없는 경우(예: 데이터베이스에서 로드된 모듈) 설정하지 않을 수 있습니다.

If __file__ is set then the __cached__ attribute might also be set, which is the path to any compiled version of the code (for example, a byte-compiled file). The file does not need to exist to set this attribute; the path can simply point to where the compiled file would exist (see PEP 3147).

__file__이 설정된 경우 __cached__ 속성도 설정될 수 있으며, 이는 코드의 컴파일된 버전(예: 바이트 컴파일된 파일)에 대한 경로입니다. 이 속성을 설정하기 위해 파일이 존재할 필요는 없습니다. 경로는 단순히 컴파일된 파일이 존재할 위치를 가리킬 수 있습니다(PEP 3147 참조).

Note that __cached__ may be set even if __file__ is not set. However, that scenario is quite atypical. Ultimately, the loader is what makes use of the module spec provided by the finder (from which __file__ and __cached__ are derived). So if a loader can load from a cached module but otherwise does not load from a file, that atypical scenario may be appropriate.

__cached__는 __file__이 설정되지 않은 경우에도 설정될 수 있습니다. 그러나 그런 시나리오는 매우 비정상적입니다. 궁극적으로는 로더가 파인더에서 제공한 모듈 스펙을 사용합니다(여기서 __file__과 __cached__가 파생됩니다). 따라서 로더가 캐시된 모듈에서 로드할 수 있지만 파일에서 로드하지 않는 경우, 그러한 비정상적인 시나리오가 적절할 수 있습니다.

It is strongly recommended that you use module.__spec__.cached instead of module.__cached__.

module.__spec__.cached를 module.__cached__ 대신 사용하는 것이 강력히 권장됩니다.

Deprecated since version 3.13, will be removed in version 3.15: Setting __cached__ on a module while failing to set __spec__.cached is deprecated. In Python 3.15, __cached__ will cease to be set or taken into consideration by the import system or standard library.

버전 3.13부터 더 이상 사용되지 않으며, 버전 3.15에서 제거될 예정: __spec__.cached를 설정하지 못하면서 모듈에 __cached__를 설정하는 것은 더 이상 사용되지 않습니다. 파이썬 3.15에서는 __cached__가 import 시스템이나 표준 라이브러리에 의해 설정되거나 고려되지 않을 것입니다.

#### 3.2.9.2. Other writable attributes on module objects

#### 3.2.9.2. 모듈 객체의 기타 쓰기 가능 속성

As well as the import-related attributes listed above, module objects also have the following writable attributes:

위에 나열된 import 관련 속성 외에도, 모듈 객체는 다음과 같은 쓰기 가능한 속성을 가집니다:

module.__doc__
The module's documentation string, or None if unavailable. See also: __doc__ attributes.

module.__doc__
모듈의 문서화 문자열 또는 사용할 수 없는 경우 None입니다. 참고: __doc__ 속성.

module.__annotations__
A dictionary containing variable annotations collected during module body execution. For best practices on working with __annotations__, please see Annotations Best Practices.

module.__annotations__
모듈 본문 실행 중에 수집된 변수 주석을 포함하는 딕셔너리입니다. __annotations__로 작업하는 모범 사례는 주석 모범 사례를 참조하세요.

#### 3.2.9.3. Module dictionaries

#### 3.2.9.3. 모듈 딕셔너리

Module objects also have the following special read-only attribute:

모듈 객체는 또한 다음과 같은 특별 읽기 전용 속성을 가집니다:

module.__dict__
The module's namespace as a dictionary object. Uniquely among the attributes listed here, __dict__ cannot be accessed as a global variable from within a module; it can only be accessed as an attribute on module objects.

module.__dict__
딕셔너리 객체로서의 모듈의 네임스페이스입니다. 여기에 나열된 속성 중 유일하게 __dict__는 모듈 내에서 전역 변수로 접근할 수 없습니다. 모듈 객체의 속성으로만 접근할 수 있습니다.

CPython implementation detail: Because of the way CPython clears module dictionaries, the module dictionary will be cleared when the module falls out of scope even if the dictionary still has live references. To avoid this, copy the dictionary or keep the module around while using its dictionary directly.

CPython 구현 세부 사항: CPython이 모듈 딕셔너리를 정리하는 방식 때문에, 딕셔너리에 아직 살아있는 참조가 있더라도 모듈이 범위를 벗어나면 모듈 딕셔너리가 지워집니다. 이를 피하려면, 딕셔너리를 복사하거나 딕셔너리를 직접 사용하는 동안 모듈을 유지하세요.

### 3.2.10. Custom classes

### 3.2.10. 사용자 정의 클래스

Custom class types are typically created by class definitions (see section Class definitions). A class has a namespace implemented by a dictionary object. Class attribute references are translated to lookups in this dictionary, e.g., C.x is translated to C.__dict__["x"] (although there are a number of hooks which allow for other means of locating attributes). When the attribute name is not found there, the attribute search continues in the base classes. This search of the base classes uses the C3 method resolution order which behaves correctly even in the presence of 'diamond' inheritance structures where there are multiple inheritance paths leading back to a common ancestor. Additional details on the C3 MRO used by Python can be found at The Python 2.3 Method Resolution Order.

사용자 정의 클래스 타입은 일반적으로 클래스 정의에 의해 생성됩니다(클래스 정의 섹션 참조). 클래스는 딕셔너리 객체로 구현된 네임스페이스를 가집니다. 클래스 속성 참조는 이 딕셔너리에서의 조회로 변환됩니다. 예를 들어, C.x는 C.__dict__["x"]로 변환됩니다(속성을 찾는 다른 수단을 허용하는 여러 훅이 있지만). 속성 이름이 거기서 발견되지 않으면, 속성 검색이 기본 클래스에서 계속됩니다. 이 기본 클래스 검색은 C3 메서드 해결 순서를 사용하며, 이는 공통 조상으로 이어지는 여러 상속 경로가 있는 '다이아몬드' 상속 구조에서도 올바르게 작동합니다. 파이썬에서 사용하는 C3 MRO에 대한 추가 세부 사항은 파이썬 2.3 메서드 해결 순서에서 확인할 수 있습니다.

When a class attribute reference (for class C, say) would yield a class method object, it is transformed into an instance method object whose __self__ attribute is C. When it would yield a staticmethod object, it is transformed into the object wrapped by the static method object. See section Implementing Descriptors for another way in which attributes retrieved from a class may differ from those actually contained in its __dict__.

클래스 속성 참조(예를 들어 클래스 C의 경우)가 클래스 메서드 객체를 생성하면, 이는 __self__ 속성이 C인 인스턴스 메서드 객체로 변환됩니다. staticmethod 객체를 생성하는 경우, 정적 메서드 객체에 의해 래핑된 객체로 변환됩니다. 클래스에서 검색된 속성이 실제로 __dict__에 포함된 속성과 다를 수 있는 또 다른 방법은 디스크립터 구현 섹션을 참조하세요.

Class attribute assignments update the class's dictionary, never the dictionary of a base class.

클래스 속성 할당은 기본 클래스의 딕셔너리가 아닌 클래스의 딕셔너리를 업데이트합니다.

A class object can be called (see above) to yield a class instance (see below).

클래스 객체는 클래스 인스턴스를 생성하기 위해 호출될 수 있습니다(위 참조)(아래 참조).

#### 3.2.10.1. Special attributes

#### 3.2.10.1. 특수 속성

Attribute

속성

Meaning

의미

type.__name__
The class's name. See also: __name__ attributes.

type.__name__
클래스의 이름입니다. 참조: __name__ 속성.

type.__qualname__
The class's qualified name. See also: __qualname__ attributes.

type.__qualname__
클래스의 정규화된 이름입니다. 참조: __qualname__ 속성.

type.__module__
The name of the module in which the class was defined.

type.__module__
클래스가 정의된 모듈의 이름입니다.

type.__dict__
A mapping proxy providing a read-only view of the class's namespace. See also: __dict__ attributes.

type.__dict__
클래스 네임스페이스의 읽기 전용 뷰를 제공하는 매핑 프록시입니다. 참조: __dict__ 속성.

type.__bases__
A tuple containing the class's bases. In most cases, for a class defined as class X(A, B, C), X.__bases__ will be exactly equal to (A, B, C).

type.__bases__
클래스의 기본 클래스를 포함하는 튜플입니다. 대부분의 경우, class X(A, B, C)로 정의된 클래스의 경우 X.__bases__는 정확히 (A, B, C)와 같습니다.

type.__doc__
The class's documentation string, or None if undefined. Not inherited by subclasses.

type.__doc__
클래스의 문서화 문자열 또는 정의되지 않은 경우 None입니다. 하위 클래스에 의해 상속되지 않습니다.

type.__annotations__
A dictionary containing variable annotations collected during class body execution. For best practices on working with __annotations__, please see Annotations Best Practices.

type.__annotations__
클래스 본문 실행 중에 수집된 변수 주석을 포함하는 딕셔너리입니다. __annotations__로 작업하는 모범 사례는 주석 모범 사례를 참조하세요.

Caution Accessing the __annotations__ attribute of a class object directly may yield incorrect results in the presence of metaclasses. In addition, the attribute may not exist for some classes. Use inspect.get_annotations() to retrieve class annotations safely.

주의 메타클래스가 있는 경우 클래스 객체의 __annotations__ 속성에 직접 접근하면 잘못된 결과가 나올 수 있습니다. 또한 일부 클래스의 경우 이 속성이 존재하지 않을 수 있습니다. 클래스 주석을 안전하게 검색하려면 inspect.get_annotations()를 사용하세요.

type.__type_params__
A tuple containing the type parameters of a generic class.

type.__type_params__
제네릭 클래스의 타입 매개변수를 포함하는 튜플입니다.

Added in version 3.12.

버전 3.12에서 추가됨.

type.__static_attributes__
A tuple containing names of attributes of this class which are assigned through self.X from any function in its body.

type.__static_attributes__
본문의 어떤 함수에서든 self.X를 통해 할당되는 이 클래스의 속성 이름을 포함하는 튜플입니다.

Added in version 3.13.

버전 3.13에서 추가됨.

type.__firstlineno__
The line number of the first line of the class definition, including decorators. Setting the __module__ attribute removes the __firstlineno__ item from the type's dictionary.

type.__firstlineno__
데코레이터를 포함한 클래스 정의의 첫 번째 줄 번호입니다. __module__ 속성을 설정하면 타입의 딕셔너리에서 __firstlineno__ 항목이 제거됩니다.

Added in version 3.13.

버전 3.13에서 추가됨.

type.__mro__
The tuple of classes that are considered when looking for base classes during method resolution.

type.__mro__
메서드 해결 중에 기본 클래스를 찾을 때 고려되는 클래스의 튜플입니다.

#### 3.2.10.2. Special methods

#### 3.2.10.2. 특수 메서드

In addition to the special attributes described above, all Python classes also have the following two methods available:

위에서 설명한 특수 속성 외에도 모든 파이썬 클래스는 다음 두 가지 메서드를 사용할 수 있습니다:

type.mro()
This method can be overridden by a metaclass to customize the method resolution order for its instances. It is called at class instantiation, and its result is stored in __mro__.

type.mro()
이 메서드는 메타클래스에 의해 재정의되어 인스턴스의 메서드 해결 순서를 사용자 정의할 수 있습니다. 클래스 인스턴스화 시 호출되며, 그 결과는 __mro__에 저장됩니다.

type.__subclasses__()
Each class keeps a list of weak references to its immediate subclasses. This method returns a list of all those references still alive. The list is in definition order. Example:

type.__subclasses__()
각 클래스는 직계 하위 클래스에 대한 약한 참조 목록을 유지합니다. 이 메서드는 아직 살아있는 모든 참조의 목록을 반환합니다. 목록은 정의 순서대로입니다. 예:

```python
>>>
class A: pass
class B(A): pass
A.__subclasses__()
[<class 'B'>]
```

### 3.2.11. Class instances

### 3.2.11. 클래스 인스턴스

A class instance is created by calling a class object (see above). A class instance has a namespace implemented as a dictionary which is the first place in which attribute references are searched. When an attribute is not found there, and the instance's class has an attribute by that name, the search continues with the class attributes. If a class attribute is found that is a user-defined function object, it is transformed into an instance method object whose __self__ attribute is the instance. Static method and class method objects are also transformed; see above under "Classes". See section Implementing Descriptors for another way in which attributes of a class retrieved via its instances may differ from the objects actually stored in the class's __dict__. If no class attribute is found, and the object's class has a __getattr__() method, that is called to satisfy the lookup.

클래스 인스턴스는 클래스 객체를 호출하여 생성됩니다(위 참조). 클래스 인스턴스는 딕셔너리로 구현된 네임스페이스를 가지며, 이는 속성 참조가 검색되는 첫 번째 장소입니다. 속성이 거기서 발견되지 않고, 인스턴스의 클래스가 그 이름을 가진 속성을 가지고 있다면, 검색은 클래스 속성으로 계속됩니다. 사용자 정의 함수 객체인 클래스 속성이 발견되면, 그것은 __self__ 속성이 인스턴스인 인스턴스 메서드 객체로 변환됩니다. 정적 메서드와 클래스 메서드 객체도 변환됩니다. "클래스" 아래를 참조하세요. 인스턴스를 통해 검색된 클래스의 속성이 클래스의 __dict__에 실제로 저장된 객체와 다를 수 있는 또 다른 방법은 디스크립터 구현 섹션을 참조하세요. 클래스 속성이 발견되지 않고, 객체의 클래스가 __getattr__() 메서드를 가지고 있다면, 그것이 호출되어 조회를 만족시킵니다.

Attribute assignments and deletions update the instance's dictionary, never a class's dictionary. If the class has a __setattr__() or __delattr__() method, this is called instead of updating the instance dictionary directly.

속성 할당 및 삭제는 클래스의 딕셔너리가 아닌 인스턴스의 딕셔너리를 업데이트합니다. 클래스에 __setattr__() 또는 __delattr__() 메서드가 있으면, 인스턴스 딕셔너리를 직접 업데이트하는 대신 이 메서드가 호출됩니다.

Class instances can pretend to be numbers, sequences, or mappings if they have methods with certain special names. See section Special method names.

클래스 인스턴스는 특정 특수 이름을 가진 메서드가 있으면 숫자, 시퀀스 또는 매핑인 척할 수 있습니다. 특수 메서드 이름 섹션을 참조하세요.

#### 3.2.11.1. Special attributes

#### 3.2.11.1. 특수 속성

object.__class__
The class to which a class instance belongs.

object.__class__
클래스 인스턴스가 속한 클래스입니다.

object.__dict__
A dictionary or other mapping object used to store an object's (writable) attributes. Not all instances have a __dict__ attribute; see the section on __slots__ for more details.

object.__dict__
객체의 (쓰기 가능한) 속성을 저장하는 데 사용되는 딕셔너리 또는 기타 매핑 객체입니다. 모든 인스턴스가 __dict__ 속성을 가지는 것은 아닙니다. 자세한 내용은 __slots__에 관한 섹션을 참조하세요.

### 3.2.12. I/O objects (also known as file objects)

### 3.2.12. I/O 객체(파일 객체라고도 함)

A file object represents an open file. Various shortcuts are available to create file objects: the open() built-in function, and also os.popen(), os.fdopen(), and the makefile() method of socket objects (and perhaps by other functions or methods provided by extension modules).

파일 객체는 열린 파일을 나타냅니다. 파일 객체를 생성하기 위한 다양한 단축 방법이 있습니다: open() 내장 함수, 그리고 os.popen(), os.fdopen(), 소켓 객체의 makefile() 메서드(그리고 아마도 확장 모듈에서 제공하는 다른 함수나 메서드)가 있습니다.

The objects sys.stdin, sys.stdout and sys.stderr are initialized to file objects corresponding to the interpreter's standard input, output and error streams; they are all open in text mode and therefore follow the interface defined by the io.TextIOBase abstract class.

객체 sys.stdin, sys.stdout 및 sys.stderr는 인터프리터의 표준 입력, 출력 및 오류 스트림에 해당하는 파일 객체로 초기화됩니다. 이들은 모두 텍스트 모드로 열려 있으며 따라서 io.TextIOBase 추상 클래스에 의해 정의된 인터페이스를 따릅니다.

### 3.2.13. Internal types

### 3.2.13. 내부 타입

A few types used internally by the interpreter are exposed to the user. Their definitions may change with future versions of the interpreter, but they are mentioned here for completeness.

인터프리터에 의해 내부적으로 사용되는 몇 가지 타입이 사용자에게 노출됩니다. 이들의 정의는 인터프리터의 향후 버전에서 변경될 수 있지만, 완전성을 위해 여기에서 언급됩니다.

#### 3.2.13.1. Code objects

#### 3.2.13.1. 코드 객체

Code objects represent byte-compiled executable Python code, or bytecode. The difference between a code object and a function object is that the function object contains an explicit reference to the function's globals (the module in which it was defined), while a code object contains no context; also the default argument values are stored in the function object, not in the code object (because they represent values calculated at run-time). Unlike function objects, code objects are immutable and contain no references (directly or indirectly) to mutable objects.

코드 객체는 바이트 컴파일된 실행 가능한 파이썬 코드 또는 바이트코드를 나타냅니다. 코드 객체와 함수 객체의 차이점은 함수 객체는 함수의 전역 변수(정의된 모듈)에 대한 명시적 참조를 포함하는 반면, 코드 객체는 컨텍스트를 포함하지 않는다는 것입니다. 또한 기본 인수 값은 코드 객체가 아닌 함수 객체에 저장됩니다(런타임에 계산된 값을 나타내기 때문). 함수 객체와 달리, 코드 객체는 불변이며 가변 객체에 대한 참조(직접 또는 간접적으로)를 포함하지 않습니다.

##### 3.2.13.1.1. Special read-only attributes

##### 3.2.13.1.1. 특수 읽기 전용 속성

codeobject.co_name
The function name

codeobject.co_name
함수 이름

codeobject.co_qualname
The fully qualified function name

codeobject.co_qualname
정규화된 함수 이름

Added in version 3.11.

버전 3.11에서 추가됨.

codeobject.co_argcount
The total number of positional parameters (including positional-only parameters and parameters with default values) that the function has

codeobject.co_argcount
함수가 가진 위치 매개변수(위치 전용 매개변수 및 기본값이 있는 매개변수 포함)의 총 수

codeobject.co_posonlyargcount
The number of positional-only parameters (including arguments with default values) that the function has

codeobject.co_posonlyargcount
함수가 가진 위치 전용 매개변수(기본값이 있는 인수 포함)의 수

codeobject.co_kwonlyargcount
The number of keyword-only parameters (including arguments with default values) that the function has

codeobject.co_kwonlyargcount
함수가 가진 키워드 전용 매개변수(기본값이 있는 인수 포함)의 수

codeobject.co_nlocals
The number of local variables used by the function (including parameters)

codeobject.co_nlocals
함수에서 사용하는 지역 변수의 수(매개변수 포함)

codeobject.co_varnames
A tuple containing the names of the local variables in the function (starting with the parameter names)

codeobject.co_varnames
함수의 지역 변수 이름을 포함하는 튜플(매개변수 이름으로 시작)

codeobject.co_cellvars
A tuple containing the names of local variables that are referenced from at least one nested scope inside the function

codeobject.co_cellvars
함수 내의 적어도 하나의 중첩된 스코프에서 참조되는 지역 변수의 이름을 포함하는 튜플

codeobject.co_freevars
A tuple containing the names of free (closure) variables that a nested scope references in an outer scope. See also function.__closure__.

codeobject.co_freevars
중첩된 스코프가 외부 스코프에서 참조하는 자유(클로저) 변수의 이름을 포함하는 튜플입니다. function.__closure__도 참조하세요.

Note: references to global and builtin names are not included.

참고: 전역 및 내장 이름에 대한 참조는 포함되지 않습니다.

codeobject.co_code
A string representing the sequence of bytecode instructions in the function

codeobject.co_code
함수의 바이트코드 명령어 시퀀스를 나타내는 문자열

codeobject.co_consts
A tuple containing the literals used by the bytecode in the function

codeobject.co_consts
함수의 바이트코드에서 사용하는 리터럴을 포함하는 튜플

codeobject.co_names
A tuple containing the names used by the bytecode in the function

codeobject.co_names
함수의 바이트코드에서 사용하는 이름을 포함하는 튜플

codeobject.co_filename
The name of the file from which the code was compiled

codeobject.co_filename
코드가 컴파일된 파일의 이름

codeobject.co_firstlineno
The line number of the first line of the function

codeobject.co_firstlineno
함수의 첫 번째 줄 번호

codeobject.co_lnotab
A string encoding the mapping from bytecode offsets to line numbers. For details, see the source code of the interpreter.

codeobject.co_lnotab
바이트코드 오프셋에서 줄 번호로의 매핑을 인코딩한 문자열입니다. 자세한 내용은 인터프리터의 소스 코드를 참조하세요.

Deprecated since version 3.12: This attribute of code objects is deprecated, and may be removed in Python 3.15.

버전 3.12부터 더 이상 사용되지 않음: 코드 객체의 이 속성은 더 이상 사용되지 않으며 Python 3.15에서 제거될 수 있습니다.

codeobject.co_stacksize
The required stack size of the code object

codeobject.co_stacksize
코드 객체의 필요한 스택 크기

codeobject.co_flags
An integer encoding a number of flags for the interpreter.

codeobject.co_flags
인터프리터를 위한 여러 플래그를 인코딩한 정수입니다.

The following flag bits are defined for co_flags: bit 0x04 is set if the function uses the *arguments syntax to accept an arbitrary number of positional arguments; bit 0x08 is set if the function uses the **keywords syntax to accept arbitrary keyword arguments; bit 0x20 is set if the function is a generator. See Code Objects Bit Flags for details on the semantics of each flags that might be present.

co_flags에 대해 다음 플래그 비트가 정의됩니다: 함수가 임의의 수의 위치 인수를 허용하기 위해 *arguments 구문을 사용하는 경우 비트 0x04가 설정됩니다. 함수가 임의의 키워드 인수를 허용하기 위해 **keywords 구문을 사용하는 경우 비트 0x08이 설정됩니다. 함수가 제네레이터인 경우 비트 0x20이 설정됩니다. 존재할 수 있는 각 플래그의 의미론에 대한 자세한 내용은 코드 객체 비트 플래그를 참조하세요.

Future feature declarations (from __future__ import division) also use bits in co_flags to indicate whether a code object was compiled with a particular feature enabled: bit 0x2000 is set if the function was compiled with future division enabled; bits 0x10 and 0x1000 were used in earlier versions of Python.

미래 기능 선언(from __future__ import division)은 코드 객체가 특정 기능이 활성화된 상태로 컴파일되었는지 여부를 나타내기 위해 co_flags의 비트도 사용합니다: 함수가 future division이 활성화된 상태로 컴파일된 경우 비트 0x2000이 설정됩니다. 비트 0x10 및 0x1000은 이전 버전의 Python에서 사용되었습니다.

Other bits in co_flags are reserved for internal use.

co_flags의 다른 비트는 내부 사용을 위해 예약되어 있습니다.

If a code object represents a function, the first item in co_consts is the documentation string of the function, or None if undefined.

코드 객체가 함수를 나타내는 경우, co_consts의 첫 번째 항목은 함수의 문서화 문자열이거나, 정의되지 않은 경우 None입니다.

##### 3.2.13.1.2. Methods on code objects

##### 3.2.13.1.2. 코드 객체의 메서드

codeobject.co_positions()
Returns an iterable over the source code positions of each bytecode instruction in the code object.

codeobject.co_positions()
코드 객체에 있는 각 바이트코드 명령어의 소스 코드 위치에 대한 반복 가능한 객체를 반환합니다.

The iterator returns tuples containing the (start_line, end_line, start_column, end_column). The i-th tuple corresponds to the position of the source code that compiled to the i-th code unit. Column information is 0-indexed utf-8 byte offsets on the given source line.

반복자는 (start_line, end_line, start_column, end_column)을 포함하는 튜플을 반환합니다. i번째 튜플은 i번째 코드 단위로 컴파일된 소스 코드의 위치에 해당합니다. 열 정보는 주어진 소스 라인에서 0부터 시작하는 utf-8 바이트 오프셋입니다.

This positional information can be missing. A non-exhaustive lists of cases where this may happen:

이 위치 정보가 없을 수 있습니다. 이런 일이 발생할 수 있는 경우의 비포괄적 목록은 다음과 같습니다:

Running the interpreter with -X no_debug_ranges.

-X no_debug_ranges로 인터프리터를 실행하는 경우.

Loading a pyc file compiled while using -X no_debug_ranges.

-X no_debug_ranges를 사용하여 컴파일된 pyc 파일을 로드하는 경우.

Position tuples corresponding to artificial instructions.

인공 명령어에 해당하는 위치 튜플.

Line and column numbers that can't be represented due to implementation specific limitations.

구현별 제한으로 인해 표현할 수 없는 행 및 열 번호.

When this occurs, some or all of the tuple elements can be None.

이 경우 튜플 요소의 일부 또는 전부가 None일 수 있습니다.

Added in version 3.11.

버전 3.11에서 추가됨.

Note This feature requires storing column positions in code objects which may result in a small increase of disk usage of compiled Python files or interpreter memory usage. To avoid storing the extra information and/or deactivate printing the extra traceback information, the -X no_debug_ranges command line flag or the PYTHONNODEBUGRANGES environment variable can be used.

참고: 이 기능은 코드 객체에 열 위치를 저장해야 하므로 컴파일된 Python 파일의 디스크 사용량이나 인터프리터 메모리 사용량이 약간 증가할 수 있습니다. 추가 정보를 저장하지 않거나 추가 트레이스백 정보 출력을 비활성화하려면 -X no_debug_ranges 명령줄 플래그나 PYTHONNODEBUGRANGES 환경 변수를 사용할 수 있습니다.

codeobject.co_lines()
Returns an iterator that yields information about successive ranges of bytecodes. Each item yielded is a (start, end, lineno) tuple:

codeobject.co_lines()
연속적인 바이트코드 범위에 대한 정보를 생성하는 반복자를 반환합니다. 생성된 각 항목은 (start, end, lineno) 튜플입니다:

start (an int) represents the offset (inclusive) of the start of the bytecode range

start(정수)는 바이트코드 범위 시작의 오프셋(포함)을 나타냅니다.

end (an int) represents the offset (exclusive) of the end of the bytecode range

end(정수)는 바이트코드 범위 끝의 오프셋(제외)을 나타냅니다.

lineno is an int representing the line number of the bytecode range, or None if the bytecodes in the given range have no line number

lineno는 바이트코드 범위의 줄 번호를 나타내는 정수이거나, 주어진 범위의 바이트코드에 줄 번호가 없는 경우 None입니다.

The items yielded will have the following properties:

생성된 항목은 다음과 같은 속성을 가집니다:

The first range yielded will have a start of 0.

생성된 첫 번째 범위의 start는 0입니다.

The (start, end) ranges will be non-decreasing and consecutive. That is, for any pair of tuples, the start of the second will be equal to the end of the first.

(start, end) 범위는 감소하지 않고 연속적입니다. 즉, 모든 튜플 쌍에 대해, 두 번째의 start는 첫 번째의 end와 같습니다.

No range will be backwards: end >= start for all triples.

범위는 역방향이 아닙니다: 모든 트리플에 대해 end >= start입니다.

The last tuple yielded will have end equal to the size of the bytecode.

마지막으로 생성된 튜플의 end는 바이트코드의 크기와 같습니다.

Zero-width ranges, where start == end, are allowed. Zero-width ranges are used for lines that are present in the source code, but have been eliminated by the bytecode compiler.

start == end인 너비가 0인 범위도 허용됩니다. 너비가 0인 범위는 소스 코드에는 있지만 바이트코드 컴파일러에 의해 제거된 줄에 사용됩니다.

Added in version 3.10.

버전 3.10에서 추가됨.

See also
PEP 626 - Precise line numbers for debugging and other tools.
The PEP that introduced the co_lines() method.

참고
PEP 626 - 디버깅 및 기타 도구를 위한 정확한 줄 번호.
co_lines() 메서드를 도입한 PEP입니다.

codeobject.replace(**kwargs)
Return a copy of the code object with new values for the specified fields.

codeobject.replace(**kwargs)
지정된 필드에 대해 새 값을 가진 코드 객체의 복사본을 반환합니다.

Code objects are also supported by the generic function copy.replace().

코드 객체는 일반 함수 copy.replace()에서도 지원됩니다.

Added in version 3.8.

버전 3.8에서 추가됨.

#### 3.2.13.2. Frame objects

#### 3.2.13.2. 프레임 객체

Frame objects represent execution frames. They may occur in traceback objects, and are also passed to registered trace functions.

프레임 객체는 실행 프레임을 나타냅니다. 이들은 트레이스백 객체에 나타날 수 있으며, 등록된 추적 함수에도 전달됩니다.

##### 3.2.13.2.1. Special read-only attributes

##### 3.2.13.2.1. 특수 읽기 전용 속성

frame.f_back
Points to the previous stack frame (towards the caller), or None if this is the bottom stack frame

frame.f_back
이전 스택 프레임(호출자 방향)을 가리키거나, 이것이 맨 아래 스택 프레임인 경우 None입니다.

frame.f_code
The code object being executed in this frame. Accessing this attribute raises an auditing event object.__getattr__ with arguments obj and "f_code".

frame.f_code
이 프레임에서 실행 중인 코드 객체입니다. 이 속성에 액세스하면 obj와 "f_code" 인수를 사용하여 감사 이벤트 object.__getattr__가 발생합니다.

frame.f_locals
The mapping used by the frame to look up local variables. If the frame refers to an optimized scope, this may return a write-through proxy object.

frame.f_locals
프레임이 지역 변수를 조회하는 데 사용하는 매핑입니다. 프레임이 최적화된 스코프를 참조하는 경우 write-through 프록시 객체를 반환할 수 있습니다.

Changed in version 3.13: Return a proxy for optimized scopes.

버전 3.13에서 변경됨: 최적화된 스코프에 대한 프록시를 반환합니다.

frame.f_globals
The dictionary used by the frame to look up global variables

frame.f_globals
프레임이 전역 변수를 조회하는 데 사용하는 딕셔너리입니다.

frame.f_builtins
The dictionary used by the frame to look up built-in (intrinsic) names

frame.f_builtins
프레임이 내장(고유) 이름을 조회하는 데 사용하는 딕셔너리입니다.

frame.f_lasti
The "precise instruction" of the frame object (this is an index into the bytecode string of the code object)

frame.f_lasti
프레임 객체의 "정확한 명령어"(코드 객체의 바이트코드 문자열에 대한 인덱스)입니다.

##### 3.2.13.2.2. Special writable attributes

##### 3.2.13.2.2. 특수 쓰기 가능 속성

frame.f_trace
If not None, this is a function called for various events during code execution (this is used by debuggers). Normally an event is triggered for each new source line (see f_trace_lines).

frame.f_trace
None이 아닌 경우, 코드 실행 중 다양한 이벤트에 대해 호출되는 함수입니다(디버거에서 사용). 일반적으로 각 새 소스 라인에 대해 이벤트가 트리거됩니다(f_trace_lines 참조).

frame.f_trace_lines
Set this attribute to False to disable triggering a tracing event for each source line.

frame.f_trace_lines
각 소스 라인에 대한 추적 이벤트 트리거를 비활성화하려면 이 속성을 False로 설정하세요.

frame.f_trace_opcodes
Set this attribute to True to allow per-opcode events to be requested. Note that this may lead to undefined interpreter behaviour if exceptions raised by the trace function escape to the function being traced.

frame.f_trace_opcodes
명령어별 이벤트를 요청할 수 있도록 하려면 이 속성을 True로 설정하세요. 추적 함수에서 발생한 예외가 추적 중인 함수로 이스케이프하면 정의되지 않은 인터프리터 동작이 발생할 수 있음에 주의하세요.

frame.f_lineno
The current line number of the frame – writing to this from within a trace function jumps to the given line (only for the bottom-most frame). A debugger can implement a Jump command (aka Set Next Statement) by writing to this attribute.

frame.f_lineno
프레임의 현재 줄 번호 – 추적 함수 내에서 이 속성에 쓰면 지정된 줄로 점프합니다(맨 아래 프레임에만 해당). 디버거는 이 속성에 쓰기를 통해 Jump 명령(일명 Set Next Statement)을 구현할 수 있습니다.

##### 3.2.13.2.3. Frame object methods

##### 3.2.13.2.3. 프레임 객체 메서드

Frame objects support one method:

프레임 객체는 하나의 메서드를 지원합니다:

frame.clear()
This method clears all references to local variables held by the frame. Also, if the frame belonged to a generator, the generator is finalized. This helps break reference cycles involving frame objects (for example when catching an exception and storing its traceback for later use).

frame.clear()
이 메서드는 프레임이 보유한 지역 변수에 대한 모든 참조를 지웁니다. 또한, 프레임이 제네레이터에 속한 경우 제네레이터가 종료됩니다. 이는 프레임 객체와 관련된 참조 순환을 끊는 데 도움이 됩니다(예: 예외를 잡아서 나중에 사용하기 위해 트레이스백을 저장할 때).

RuntimeError is raised if the frame is currently executing or suspended.

프레임이 현재 실행 중이거나 일시 중단된 경우 RuntimeError가 발생합니다.

Added in version 3.4.

버전 3.4에서 추가됨.

Changed in version 3.13: Attempting to clear a suspended frame raises RuntimeError (as has always been the case for executing frames).

버전 3.13에서 변경됨: 일시 중단된 프레임을 지우려고 하면 RuntimeError가 발생합니다(실행 중인 프레임에서 항상 그랬던 것처럼).

#### 3.2.13.3. Traceback objects

#### 3.2.13.3. 트레이스백 객체

Traceback objects represent the stack trace of an exception. A traceback object is implicitly created when an exception occurs, and may also be explicitly created by calling types.TracebackType.

트레이스백 객체는 예외의 스택 추적을 나타냅니다. 트레이스백 객체는 예외가 발생할 때 암시적으로 생성되며, types.TracebackType을 호출하여 명시적으로 생성될 수도 있습니다.

Changed in version 3.7: Traceback objects can now be explicitly instantiated from Python code.

버전 3.7에서 변경됨: 이제 Python 코드에서 트레이스백 객체를 명시적으로 인스턴스화할 수 있습니다.

For implicitly created tracebacks, when the search for an exception handler unwinds the execution stack, at each unwound level a traceback object is inserted in front of the current traceback. When an exception handler is entered, the stack trace is made available to the program. (See section The try statement.) It is accessible as the third item of the tuple returned by sys.exc_info(), and as the __traceback__ attribute of the caught exception.

암시적으로 생성된 트레이스백의 경우, 예외 핸들러를 찾기 위해 실행 스택을 풀 때 각 풀린 수준에서 트레이스백 객체가 현재 트레이스백 앞에 삽입됩니다. 예외 핸들러가 입력되면 스택 추적이 프로그램에서 사용 가능하게 됩니다. (try 문 섹션 참조.) sys.exc_info()가 반환하는 튜플의 세 번째 항목과 잡힌 예외의 __traceback__ 속성으로 접근할 수 있습니다.

When the program contains no suitable handler, the stack trace is written (nicely formatted) to the standard error stream; if the interpreter is interactive, it is also made available to the user as sys.last_traceback.

프로그램에 적합한 핸들러가 없는 경우, 스택 추적은 표준 오류 스트림에 (보기 좋게 형식화되어) 작성됩니다. 인터프리터가 대화형인 경우 sys.last_traceback으로 사용자에게도 제공됩니다.

For explicitly created tracebacks, it is up to the creator of the traceback to determine how the tb_next attributes should be linked to form a full stack trace.

명시적으로 생성된 트레이스백의 경우, 전체 스택 추적을 형성하기 위해 tb_next 속성을 어떻게 연결해야 하는지 결정하는 것은 트레이스백 생성자에게 달려 있습니다.

Special read-only attributes:

특수 읽기 전용 속성:

traceback.tb_frame
Points to the execution frame of the current level.

traceback.tb_frame
현재 레벨의 실행 프레임을 가리킵니다.

Accessing this attribute raises an auditing event object.__getattr__ with arguments obj and "tb_frame".

이 속성에 액세스하면 obj와 "tb_frame" 인수를 사용하여 감사 이벤트 object.__getattr__가 발생합니다.

traceback.tb_lineno
Gives the line number where the exception occurred

traceback.tb_lineno
예외가 발생한 줄 번호를 제공합니다.

traceback.tb_lasti
Indicates the "precise instruction".

traceback.tb_lasti
"정확한 명령어"를 나타냅니다.

The line number and last instruction in the traceback may differ from the line number of its frame object if the exception occurred in a try statement with no matching except clause or with a finally clause.

예외가 일치하는 except 절이 없거나 finally 절이 있는 try 문에서 발생한 경우, 트레이스백의 줄 번호와 마지막 명령어는 해당 프레임 객체의 줄 번호와 다를 수 있습니다.

traceback.tb_next
The special writable attribute tb_next is the next level in the stack trace (towards the frame where the exception occurred), or None if there is no next level.

traceback.tb_next
특수 쓰기 가능 속성 tb_next는 스택 추적의 다음 레벨(예외가 발생한 프레임을 향함)이거나, 다음 레벨이 없는 경우 None입니다.

Changed in version 3.7: This attribute is now writable

버전 3.7에서 변경됨: 이 속성이 이제 쓰기 가능합니다

#### 3.2.13.4. Slice objects

#### 3.2.13.4. 슬라이스 객체

Slice objects are used to represent slices for __getitem__() methods. They are also created by the built-in slice() function.

슬라이스 객체는 __getitem__() 메서드의 슬라이스를 나타내는 데 사용됩니다. 내장 slice() 함수에 의해서도 생성됩니다.

Special read-only attributes: start is the lower bound; stop is the upper bound; step is the step value; each is None if omitted. These attributes can have any type.

특수 읽기 전용 속성: start는 하한; stop은 상한; step은 단계 값입니다. 생략된 경우 각각 None입니다. 이러한 속성은 어떤 타입도 가질 수 있습니다.

Slice objects support one method:

슬라이스 객체는 하나의 메서드를 지원합니다:

slice.indices(self, length)
This method takes a single integer argument length and computes information about the slice that the slice object would describe if applied to a sequence of length items. It returns a tuple of three integers; respectively these are the start and stop indices and the step or stride length of the slice. Missing or out-of-bounds indices are handled in a manner consistent with regular slices.

slice.indices(self, length)
이 메서드는 단일 정수 인수 length를 사용하고, 슬라이스 객체가 length 항목의 시퀀스에 적용된 경우 설명하는 슬라이스에 대한 정보를 계산합니다. 세 개의 정수로 구성된 튜플을 반환합니다. 각각 슬라이스의 시작 및 종료 인덱스와 단계 또는 스트라이드 길이입니다. 누락되거나 범위를 벗어난 인덱스는 일반 슬라이스와 일치하는 방식으로 처리됩니다.

#### 3.2.13.5. Static method objects

#### 3.2.13.5. 정적 메서드 객체

Static method objects provide a way of defeating the transformation of function objects to method objects described above. A static method object is a wrapper around any other object, usually a user-defined method object. When a static method object is retrieved from a class or a class instance, the object actually returned is the wrapped object, which is not subject to any further transformation. Static method objects are also callable. Static method objects are created by the built-in staticmethod() constructor.

정적 메서드 객체는 위에서 설명한 함수 객체에서 메서드 객체로의 변환을 무효화하는 방법을 제공합니다. 정적 메서드 객체는 다른 객체(일반적으로 사용자 정의 메서드 객체)를 감싸는 래퍼입니다. 정적 메서드 객체가 클래스나 클래스 인스턴스에서 검색될 때, 실제로 반환되는 객체는 감싸진 객체이며, 이는 더 이상의 변환 대상이 아닙니다. 정적 메서드 객체도 호출 가능합니다. 정적 메서드 객체는 내장 staticmethod() 생성자에 의해 생성됩니다.

#### 3.2.13.6. Class method objects

#### 3.2.13.6. 클래스 메서드 객체

A class method object, like a static method object, is a wrapper around another object that alters the way in which that object is retrieved from classes and class instances. The behaviour of class method objects upon such retrieval is described above, under "instance methods". Class method objects are created by the built-in classmethod() constructor.

클래스 메서드 객체는 정적 메서드 객체와 마찬가지로 다른 객체를 감싸는 래퍼로, 해당 객체가 클래스와 클래스 인스턴스에서 검색되는 방식을 변경합니다. 이러한 검색 시 클래스 메서드 객체의 동작은 위의 "인스턴스 메서드" 섹션에서 설명되었습니다. 클래스 메서드 객체는 내장 classmethod() 생성자에 의해 생성됩니다.

### 3.3. Special method names

### 3.3. 특수 메서드 이름

A class can implement certain operations that are invoked by special syntax (such as arithmetic operations or subscripting and slicing) by defining methods with special names. This is Python's approach to operator overloading, allowing classes to define their own behavior with respect to language operators. For instance, if a class defines a method named __getitem__(), and x is an instance of this class, then x[i] is roughly equivalent to type(x).__getitem__(x, i). Except where mentioned, attempts to execute an operation raise an exception when no appropriate method is defined (typically AttributeError or TypeError).

클래스는 특수 이름을 가진 메서드를 정의함으로써 특별한 구문(예: 산술 연산이나 첨자 및 슬라이싱)에 의해 호출되는 특정 연산을 구현할 수 있습니다. 이것은 연산자 오버로딩에 대한 파이썬의 접근 방식으로, 클래스가 언어 연산자에 대한 자체 동작을 정의할 수 있게 합니다. 예를 들어, 클래스가 __getitem__()이라는 메서드를 정의하고 x가 이 클래스의 인스턴스라면, x[i]는 대략 type(x).__getitem__(x, i)와 동등합니다. 언급된 경우를 제외하고, 적절한 메서드가 정의되지 않았을 때 연산을 실행하려고 하면 예외가 발생합니다(일반적으로 AttributeError 또는 TypeError).

Setting a special method to None indicates that the corresponding operation is not available. For example, if a class sets __iter__() to None, the class is not iterable, so calling iter() on its instances will raise a TypeError (without falling back to __getitem__()). [2]

특수 메서드를 None으로 설정하는 것은 해당 연산을 사용할 수 없음을 나타냅니다. 예를 들어, 클래스가 __iter__()를 None으로 설정하면, 그 클래스는 반복 가능하지 않으므로, 그 인스턴스에 대해 iter()를 호출하면 TypeError가 발생합니다(__getitem__()으로 대체하지 않음). [2]

When implementing a class that emulates any built-in type, it is important that the emulation only be implemented to the degree that it makes sense for the object being modelled. For example, some sequences may work well with retrieval of individual elements, but extracting a slice may not make sense. (One example of this is the NodeList interface in the W3C's Document Object Model.)

내장 타입을 에뮬레이션하는 클래스를 구현할 때, 모델링되는 객체에 적합한 정도로만 에뮬레이션을 구현하는 것이 중요합니다. 예를 들어, 일부 시퀀스는 개별 요소의 검색에는 잘 작동할 수 있지만, 슬라이스를 추출하는 것은 의미가 없을 수 있습니다. (이에 대한 한 예는 W3C의 문서 객체 모델에 있는 NodeList 인터페이스입니다.)

#### 3.3.1. Basic customization

#### 3.3.1. 기본 사용자 정의

object.__new__(cls[, ...])
Called to create a new instance of class cls. __new__() is a static method (special-cased so you need not declare it as such) that takes the class of which an instance was requested as its first argument. The remaining arguments are those passed to the object constructor expression (the call to the class). The return value of __new__() should be the new object instance (usually an instance of cls).

object.__new__(cls[, ...])
클래스 cls의 새 인스턴스를 생성하기 위해 호출됩니다. __new__()는 정적 메서드(특별히 처리되어 그렇게 선언할 필요가 없음)로, 인스턴스가 요청된 클래스를 첫 번째 인수로 받습니다. 나머지 인수는 객체 생성자 표현식(클래스 호출)에 전달된 것들입니다. __new__()의 반환 값은 새 객체 인스턴스여야 합니다(일반적으로 cls의 인스턴스).

Typical implementations create a new instance of the class by invoking the superclass's __new__() method using super().__new__(cls[, ...]) with appropriate arguments and then modifying the newly created instance as necessary before returning it.

일반적인 구현은 적절한 인수를 사용하여 super().__new__(cls[, ...])를 호출하여 상위 클래스의 __new__() 메서드를 호출하여 클래스의 새 인스턴스를 생성한 다음, 반환하기 전에 필요에 따라 새로 생성된 인스턴스를 수정합니다.

If __new__() is invoked during object construction and it returns an instance of cls, then the new instance's __init__() method will be invoked like __init__(self[, ...]), where self is the new instance and the remaining arguments are the same as were passed to the object constructor.

객체 생성 중에 __new__()가 호출되고 cls의 인스턴스를 반환하면, 새 인스턴스의 __init__() 메서드가 __init__(self[, ...])와 같이 호출됩니다. 여기서 self는 새 인스턴스이고 나머지 인수는 객체 생성자에 전달된 것과 동일합니다.

If __new__() does not return an instance of cls, then the new instance's __init__() method will not be invoked.

__new__()가 cls의 인스턴스를 반환하지 않으면 새 인스턴스의 __init__() 메서드는 호출되지 않습니다.

__new__() is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize instance creation. It is also commonly overridden in custom metaclasses in order to customize class creation.

__new__()는 주로 불변 타입(int, str 또는 tuple과 같은)의 하위 클래스가 인스턴스 생성을 사용자 정의할 수 있게 하기 위한 것입니다. 또한 클래스 생성을 사용자 정의하기 위해 사용자 정의 메타클래스에서도 자주 재정의됩니다.

object.__init__(self[, ...])
Called after the instance has been created (by __new__()), but before it is returned to the caller. The arguments are those passed to the class constructor expression. If a base class has an __init__() method, the derived class's __init__() method, if any, must explicitly call it to ensure proper initialization of the base class part of the instance; for example: super().__init__([args...]).

object.__init__(self[, ...])
인스턴스가 생성된 후(__new__()에 의해), 호출자에게 반환되기 전에 호출됩니다. 인수는 클래스 생성자 표현식에 전달된 것들입니다. 기본 클래스가 __init__() 메서드를 가지고 있다면, 파생 클래스의 __init__() 메서드(있는 경우)는 인스턴스의 기본 클래스 부분이 적절하게 초기화되도록 명시적으로 호출해야 합니다. 예: super().__init__([args...]).

Because __new__() and __init__() work together in constructing objects (__new__() to create it, and __init__() to customize it), no non-None value may be returned by __init__(); doing so will cause a TypeError to be raised at runtime.

__new__()와 __init__()은 객체 구성에 함께 작동하므로(__new__()는 객체를 생성하고, __init__()은 객체를 사용자 정의함), __init__()은 None이 아닌 값을 반환할 수 없습니다. 그렇게 하면 런타임에 TypeError가 발생합니다.

object.__del__(self)
Called when the instance is about to be destroyed. This is also called a finalizer or (improperly) a destructor. If a base class has a __del__() method, the derived class's __del__() method, if any, must explicitly call it to ensure proper deletion of the base class part of the instance.

object.__del__(self)
인스턴스가 파괴되려고 할 때 호출됩니다. 이것은 종결자(finalizer) 또는 (부적절하게) 소멸자(destructor)라고도 불립니다. 기본 클래스가 __del__() 메서드를 가지고 있다면, 파생 클래스의 __del__() 메서드(있는 경우)는 인스턴스의 기본 클래스 부분이 적절하게 삭제되도록 명시적으로 이를 호출해야 합니다.

It is possible (though not recommended!) for the __del__() method to postpone destruction of the instance by creating a new reference to it. This is called object resurrection. It is implementation-dependent whether __del__() is called a second time when a resurrected object is about to be destroyed; the current CPython implementation only calls it once.

__del__() 메서드가 새 참조를 생성하여 인스턴스의 파괴를 연기하는 것이 가능합니다(권장하지 않음!). 이것을 객체 부활이라고 합니다. 부활한 객체가 파괴되려고 할 때 __del__()이 두 번째로 호출되는지 여부는 구현에 따라 다릅니다. 현재 CPython 구현은 한 번만 호출합니다.

It is not guaranteed that __del__() methods are called for objects that still exist when the interpreter exits. weakref.finalize provides a straightforward way to register a cleanup function to be called when an object is garbage collected.

인터프리터가 종료될 때 여전히 존재하는 객체에 대해 __del__() 메서드가 호출된다는 보장은 없습니다. weakref.finalize는 객체가 가비지 컬렉션될 때 호출될 정리 함수를 등록하는 간단한 방법을 제공합니다.

Note del x doesn't directly call x.__del__() — the former decrements the reference count for x by one, and the latter is only called when x's reference count reaches zero.

참고: del x는 x.__del__()을 직접 호출하지 않습니다. 전자는 x의 참조 카운트를 하나 감소시키고, 후자는 x의 참조 카운트가 0에 도달할 때만 호출됩니다.

CPython implementation detail: It is possible for a reference cycle to prevent the reference count of an object from going to zero. In this case, the cycle will be later detected and deleted by the cyclic garbage collector. A common cause of reference cycles is when an exception has been caught in a local variable. The frame's locals then reference the exception, which references its own traceback, which references the locals of all frames caught in the traceback.

CPython 구현 세부 사항: 참조 주기가 객체의 참조 카운트가 0으로 내려가는 것을 방지할 수 있습니다. 이 경우, 순환 참조는 나중에 순환 가비지 컬렉터에 의해 탐지되고 삭제됩니다. 참조 주기의 흔한 원인은 예외가 지역 변수에 잡혔을 때입니다. 프레임의 로컬 변수는 그 예외를 참조하고, 예외는 자신의 트레이스백을 참조하며, 트레이스백은 트레이스백에 잡힌 모든 프레임의 로컬 변수를 참조합니다.

See also Documentation for the gc module.

gc 모듈에 대한 문서도 참조하세요.

Warning Due to the precarious circumstances under which __del__() methods are invoked, exceptions that occur during their execution are ignored, and a warning is printed to sys.stderr instead. In particular:

경고: __del__() 메서드가 호출되는 불안정한 상황으로 인해, 실행 중 발생하는 예외는 무시되고 대신 sys.stderr에 경고가 출력됩니다. 특히:

__del__() can be invoked when arbitrary code is being executed, including from any arbitrary thread. If __del__() needs to take a lock or invoke any other blocking resource, it may deadlock as the resource may already be taken by the code that gets interrupted to execute __del__().

__del__()은 임의의 코드가 실행될 때(임의의 스레드에서도) 호출될 수 있습니다. __del__()이 잠금을 취하거나 다른 차단 리소스를 호출해야 하는 경우, __del__()을 실행하기 위해 중단된 코드에 의해 해당 리소스가 이미 점유되어 있을 수 있으므로 교착 상태가 발생할 수 있습니다.

__del__() can be executed during interpreter shutdown. As a consequence, the global variables it needs to access (including other modules) may already have been deleted or set to None. Python guarantees that globals whose name begins with a single underscore are deleted from their module before other globals are deleted; if no other references to such globals exist, this may help in assuring that imported modules are still available at the time when the __del__() method is called.

__del__()은 인터프리터 종료 중에 실행될 수 있습니다. 결과적으로, 접근해야 하는 전역 변수(다른 모듈 포함)가 이미 삭제되었거나 None으로 설정되었을 수 있습니다. 파이썬은 이름이 단일 밑줄로 시작하는 전역 변수가 다른 전역 변수가 삭제되기 전에 모듈에서 삭제된다는 것을 보장합니다. 이런 전역 변수에 대한 다른 참조가 존재하지 않는다면, 이는 __del__() 메서드가 호출될 때 가져온 모듈이 여전히 사용 가능하다고 확신하는 데 도움이 될 수 있습니다.

object.__repr__(self)
Called by the repr() built-in function to compute the "official" string representation of an object. If at all possible, this should look like a valid Python expression that could be used to recreate an object with the same value (given an appropriate environment). If this is not possible, a string of the form <...some useful description...> should be returned. The return value must be a string object. If a class defines __repr__() but not __str__(), then __repr__() is also used when an "informal" string representation of instances of that class is required.

object.__repr__(self)
객체의 "공식" 문자열 표현을 계산하기 위해 내장 함수 repr()에 의해 호출됩니다. 가능하다면, 이는 (적절한 환경이 주어졌을 때) 동일한 값을 가진 객체를 재생성하는 데 사용될 수 있는 유효한 파이썬 표현식처럼 보여야 합니다. 이것이 불가능하다면, <...일부 유용한 설명...> 형식의 문자열이 반환되어야 합니다. 반환 값은 문자열 객체여야 합니다. 클래스가 __repr__()은 정의하지만 __str__()은 정의하지 않는 경우, 해당 클래스의 인스턴스에 대한 "비공식" 문자열 표현이 필요할 때도 __repr__()이 사용됩니다.

This is typically used for debugging, so it is important that the representation is information-rich and unambiguous. A default implementation is provided by the object class itself.

이것은 일반적으로 디버깅에 사용되므로, 표현이 정보가 풍부하고 모호하지 않은 것이 중요합니다. 기본 구현은 객체 클래스 자체에서 제공됩니다.

object.__str__(self)
Called by str(object), the default __format__() implementation, and the built-in function print(), to compute the "informal" or nicely printable string representation of an object. The return value must be a str object.

object.__str__(self)
str(object), 기본 __format__() 구현 및 내장 함수 print()에 의해 호출되어 객체의 "비공식" 또는 보기 좋게 출력 가능한 문자열 표현을 계산합니다. 반환 값은 str 객체여야 합니다.

This method differs from object.__repr__() in that there is no expectation that __str__() return a valid Python expression: a more convenient or concise representation can be used.

이 메서드는 __str__()이 유효한 파이썬 표현식을 반환해야 한다는 기대가 없다는 점에서 object.__repr__()과 다릅니다. 더 편리하거나 간결한 표현을 사용할 수 있습니다.

The default implementation defined by the built-in type object calls object.__repr__().

내장 타입 object에 의해 정의된 기본 구현은 object.__repr__()을 호출합니다.

object.__bytes__(self)
Called by bytes to compute a byte-string representation of an object. This should return a bytes object. The object class itself does not provide this method.

object.__bytes__(self)
객체의 바이트 문자열 표현을 계산하기 위해 bytes에 의해 호출됩니다. 이것은 bytes 객체를 반환해야 합니다. 객체 클래스 자체는 이 메서드를 제공하지 않습니다.

object.__format__(self, format_spec)
Called by the format() built-in function, and by extension, evaluation of formatted string literals and the str.format() method, to produce a "formatted" string representation of an object. The format_spec argument is a string that contains a description of the formatting options desired. The interpretation of the format_spec argument is up to the type implementing __format__(), however most classes will either delegate formatting to one of the built-in types, or use a similar formatting option syntax.

object.__format__(self, format_spec)
내장 함수 format(), 형식화된 문자열 리터럴의 평가 및 str.format() 메서드에 의해 호출되어 객체의 "형식화된" 문자열 표현을 생성합니다. format_spec 인수는 원하는 형식 옵션에 대한 설명을 포함하는 문자열입니다. format_spec 인수의 해석은 __format__()을 구현하는 타입에 달려 있지만, 대부분의 클래스는 내장 타입 중 하나에 형식화를 위임하거나 유사한 형식 옵션 구문을 사용합니다.

See Format Specification Mini-Language for a description of the standard formatting syntax.

표준 형식 구문에 대한 설명은 형식 지정 미니 언어를 참조하세요.

The return value must be a string object.

반환 값은 문자열 객체여야 합니다.

The default implementation by the object class should be given an empty format_spec string. It delegates to __str__().

객체 클래스의 기본 구현은 빈 format_spec 문자열을 받아야 합니다. 이는 __str__()에 위임합니다.

Changed in version 3.4: The __format__ method of object itself raises a TypeError if passed any non-empty string.

버전 3.4에서 변경됨: object 자체의 __format__ 메서드는 비어 있지 않은 문자열이 전달되면 TypeError를 발생시킵니다.

Changed in version 3.7: object.__format__(x, '') is now equivalent to str(x) rather than format(str(x), '')).

버전 3.7에서 변경됨: object.__format__(x, '')는 이제 format(str(x), '') 대신 str(x)와 동등합니다.

object.__lt__(self, other)
object.__le__(self, other)
object.__eq__(self, other)
object.__ne__(self, other)
object.__gt__(self, other)
object.__ge__(self, other)
These are the so-called "rich comparison" methods. The correspondence between operator symbols and method names is as follows: x<y calls x.__lt__(y), x<=y calls x.__le__(y), x==y calls x.__eq__(y), x!=y calls x.__ne__(y), x>y calls x.__gt__(y), and x>=y calls x.__ge__(y).

object.__lt__(self, other)
object.__le__(self, other)
object.__eq__(self, other)
object.__ne__(self, other)
object.__gt__(self, other)
object.__ge__(self, other)
이들은 이른바 "풍부한 비교" 메서드입니다. 연산자 기호와 메서드 이름 사이의 대응 관계는 다음과 같습니다: x<y는 x.__lt__(y)를 호출하고, x<=y는 x.__le__(y)를 호출하며, x==y는 x.__eq__(y)를 호출하고, x!=y는 x.__ne__(y)를 호출하며, x>y는 x.__gt__(y)를 호출하고, x>=y는 x.__ge__(y)를 호출합니다.

A rich comparison method may return the singleton NotImplemented if it does not implement the operation for a given pair of arguments. By convention, False and True are returned for a successful comparison. However, these methods can return any value, so if the comparison operator is used in a Boolean context (e.g., in the condition of an if statement), Python will call bool() on the value to determine if the result is true or false.

풍부한 비교 메서드는 주어진 인수 쌍에 대해 연산을 구현하지 않는 경우 싱글톤 NotImplemented를 반환할 수 있습니다. 관례적으로, 성공적인 비교에 대해서는 False와 True가 반환됩니다. 그러나, 이러한 메서드는 어떤 값이든 반환할 수 있으므로, 비교 연산자가 불리언 컨텍스트(예: if 문의 조건)에서 사용되면, 파이썬은 결과가 참인지 거짓인지 결정하기 위해 값에 bool()을 호출합니다.

By default, object implements __eq__() by using is, returning NotImplemented in the case of a false comparison: True if x is y else NotImplemented. For __ne__(), by default it delegates to __eq__() and inverts the result unless it is NotImplemented. There are no other implied relationships among the comparison operators or default implementations; for example, the truth of (x<y or x==y) does not imply x<=y. To automatically generate ordering operations from a single root operation, see functools.total_ordering().

기본적으로, object는 is를 사용하여 __eq__()를 구현하고, 거짓 비교의 경우 NotImplemented를 반환합니다: x is y이면 True, 그렇지 않으면 NotImplemented입니다. __ne__()의 경우, 기본적으로 __eq__()에 위임하고 결과가 NotImplemented가 아니면 결과를 뒤집습니다. 비교 연산자나 기본 구현 간에 다른 암시적 관계는 없습니다. 예를 들어, (x<y or x==y)의 진리값은 x<=y를 의미하지 않습니다. 단일 루트 연산에서 순서 연산을 자동으로 생성하려면 functools.total_ordering()을 참조하세요.

By default, the object class provides implementations consistent with Value comparisons: equality compares according to object identity, and order comparisons raise TypeError. Each default method may generate these results directly, but may also return NotImplemented.

기본적으로, 객체 클래스는 값 비교와 일관된 구현을 제공합니다: 동등성은 객체 식별자에 따라 비교하고, 순서 비교는 TypeError를 발생시킵니다. 각 기본 메서드는 이러한 결과를 직접 생성할 수 있지만, NotImplemented를 반환할 수도 있습니다.

See the paragraph on __hash__() for some important notes on creating hashable objects which support custom comparison operations and are usable as dictionary keys.

사용자 정의 비교 연산을 지원하고 딕셔너리 키로 사용 가능한 해시 가능한 객체를 만드는 데 관한 중요한 참고 사항은 __hash__()에 관한 단락을 참조하세요.

There are no swapped-argument versions of these methods (to be used when the left argument does not support the operation but the right argument does); rather, __lt__() and __gt__() are each other's reflection, __le__() and __ge__() are each other's reflection, and __eq__() and __ne__() are their own reflection. If the operands are of different types, and the right operand's type is a direct or indirect subclass of the left operand's type, the reflected method of the right operand has priority, otherwise the left operand's method has priority. Virtual subclassing is not considered.

이러한 메서드의 인수를 바꾼 버전은 없습니다(왼쪽 인수가 연산을 지원하지 않지만 오른쪽 인수는 지원하는 경우에 사용됨). 대신, __lt__()와 __gt__()는 서로의 반영이고, __le__()와 __ge__()는 서로의 반영이며, __eq__()와 __ne__()는 자신의 반영입니다. 피연산자의 타입이 다르고 오른쪽 피연산자의 타입이 왼쪽 피연산자 타입의 직접 또는 간접적인 하위 클래스인 경우, 오른쪽 피연산자의 반영된 메서드가 우선순위를 갖습니다. 그렇지 않으면 왼쪽 피연산자의 메서드가 우선순위를 갖습니다. 가상 하위 클래싱은 고려되지 않습니다.

When no appropriate method returns any value other than NotImplemented, the == and != operators will fall back to is and is not, respectively.

적절한 메서드가 NotImplemented 이외의 값을 반환하지 않으면, == 및 != 연산자는 각각 is 및 is not으로 대체됩니다.

object.__hash__(self)
Called by built-in function hash() and for operations on members of hashed collections including set, frozenset, and dict. The __hash__() method should return an integer. The only required property is that objects which compare equal have the same hash value; it is advised to mix together the hash values of the components of the object that also play a part in comparison of objects by packing them into a tuple and hashing the tuple. Example:

object.__hash__(self)
내장 함수 hash()와 set, frozenset, dict를 포함한 해시된 컬렉션의 멤버에 대한 연산에 의해 호출됩니다. __hash__() 메서드는 정수를 반환해야 합니다. 유일한 필수 속성은 비교 시 동일한 객체는 동일한 해시 값을 가져야 한다는 것입니다. 객체 비교에도 역할을 하는 객체 구성 요소의 해시 값을 함께 혼합하는 것이 좋으며, 이는 이들을 튜플로 묶은 다음 튜플을 해싱하면 됩니다. 예:

```python
def __hash__(self):
    return hash((self.name, self.nick, self.color))
```

Note hash() truncates the value returned from an object's custom __hash__() method to the size of a Py_ssize_t. This is typically 8 bytes on 64-bit builds and 4 bytes on 32-bit builds. If an object's __hash__() must interoperate on builds of different bit sizes, be sure to check the width on all supported builds. An easy way to do this is with python -c "import sys; print(sys.hash_info.width)".

참고: hash()는 객체의 사용자 정의 __hash__() 메서드에서 반환된 값을 Py_ssize_t 크기로 잘라냅니다. 이는 일반적으로 64비트 빌드에서는 8바이트, 32비트 빌드에서는 4바이트입니다. 객체의 __hash__()가 다른 비트 크기의 빌드에서 상호 운용되어야 하는 경우, 모든 지원되는 빌드에서 너비를 확인하세요. 이를 수행하는 쉬운 방법은 python -c "import sys; print(sys.hash_info.width)"입니다.

If a class does not define an __eq__() method it should not define a __hash__() operation either; if it defines __eq__() but not __hash__(), its instances will not be usable as items in hashable collections. If a class defines mutable objects and implements an __eq__() method, it should not implement __hash__(), since the implementation of hashable collections requires that a key's hash value is immutable (if the object's hash value changes, it will be in the wrong hash bucket).

클래스가 __eq__() 메서드를 정의하지 않으면 __hash__() 연산도 정의하지 않아야 합니다. __eq__()를 정의하지만 __hash__()를 정의하지 않으면, 그 인스턴스는 해시 가능한 컬렉션의 항목으로 사용할 수 없습니다. 클래스가 가변 객체를 정의하고 __eq__() 메서드를 구현하는 경우, __hash__()를 구현하지 않아야 합니다. 해시 가능한 컬렉션의 구현은 키의 해시 값이 불변이어야 하기 때문입니다(객체의 해시 값이 변경되면, 잘못된 해시 버킷에 있게 됩니다).

User-defined classes have __eq__() and __hash__() methods by default (inherited from the object class); with them, all objects compare unequal (except with themselves) and x.__hash__() returns an appropriate value such that x == y implies both that x is y and hash(x) == hash(y).

사용자 정의 클래스는 기본적으로 __eq__() 및 __hash__() 메서드를 가집니다(객체 클래스에서 상속). 이러한 메서드를 사용하면 모든 객체는 서로 다르게 비교되며(자기 자신과 비교할 때 제외), x.__hash__()는 x == y가 x is y와 hash(x) == hash(y)를 모두 의미하는 적절한 값을 반환합니다.

A class that overrides __eq__() and does not define __hash__() will have its __hash__() implicitly set to None. When the __hash__() method of a class is None, instances of the class will raise an appropriate TypeError when a program attempts to retrieve their hash value, and will also be correctly identified as unhashable when checking isinstance(obj, collections.abc.Hashable).

__eq__()를 오버라이드하고 __hash__()를 정의하지 않는 클래스는 __hash__()가 암묵적으로 None으로 설정됩니다. 클래스의 __hash__() 메서드가 None이면, 프로그램이 그 인스턴스의 해시 값을 검색하려고 할 때 적절한 TypeError가 발생하며, isinstance(obj, collections.abc.Hashable) 확인 시 해시 불가능한 것으로 올바르게 식별됩니다.

If a class that overrides __eq__() needs to retain the implementation of __hash__() from a parent class, the interpreter must be told this explicitly by setting __hash__ = <ParentClass>.__hash__.

__eq__()를 오버라이드하는 클래스가 부모 클래스의 __hash__() 구현을 유지해야 하는 경우, __hash__ = <ParentClass>.__hash__를 설정하여 인터프리터에 명시적으로 알려야 합니다.

If a class that does not override __eq__() wishes to suppress hash support, it should include __hash__ = None in the class definition. A class which defines its own __hash__() that explicitly raises a TypeError would be incorrectly identified as hashable by an isinstance(obj, collections.abc.Hashable) call.

__eq__()를 오버라이드하지 않는 클래스가 해시 지원을 억제하고자 하는 경우, 클래스 정의에 __hash__ = None을 포함해야 합니다. 명시적으로 TypeError를 발생시키는 자체 __hash__()를 정의하는 클래스는 isinstance(obj, collections.abc.Hashable) 호출에 의해 해시 가능한 것으로 잘못 식별됩니다.

Note By default, the __hash__() values of str and bytes objects are "salted" with an unpredictable random value. Although they remain constant within an individual Python process, they are not predictable between repeated invocations of Python.

참고: 기본적으로 str 및 bytes 객체의 __hash__() 값은 예측할 수 없는 무작위 값으로 "솔팅(salting)"됩니다. 이들은 개별 파이썬 프로세스 내에서는 일정하게 유지되지만, 반복된 파이썬 호출 간에는 예측할 수 없습니다.

This is intended to provide protection against a denial-of-service caused by carefully chosen inputs that exploit the worst case performance of a dict insertion, O(n2) complexity. See http://ocert.org/advisories/ocert-2011-003.html for details.

이는 dict 삽입의 최악의 경우 성능인 O(n²) 복잡도를 악용하는 신중하게 선택된 입력으로 인한 서비스 거부(DoS)에 대한 보호를 제공하기 위한 것입니다. 자세한 내용은 http://ocert.org/advisories/ocert-2011-003.html을 참조하세요.

Changing hash values affects the iteration order of sets. Python has never made guarantees about this ordering (and it typically varies between 32-bit and 64-bit builds).

해시 값의 변경은 집합의 반복 순서에 영향을 미칩니다. 파이썬은 이 순서에 대해 보장한 적이 없습니다(일반적으로 32비트 및 64비트 빌드 간에 차이가 있음).

See also PYTHONHASHSEED.

PYTHONHASHSEED도 참조하세요.

Changed in version 3.3: Hash randomization is enabled by default.

버전 3.3에서 변경됨: 해시 무작위화가 기본적으로 활성화되었습니다.

object.__bool__(self)
Called to implement truth value testing and the built-in operation bool(); should return False or True. When this method is not defined, __len__() is called, if it is defined, and the object is considered true if its result is nonzero. If a class defines neither __len__() nor __bool__() (which is true of the object class itself), all its instances are considered true.

object.__bool__(self)
진리값 테스트 및 내장 연산 bool()을 구현하기 위해 호출됩니다. False 또는 True를 반환해야 합니다. 이 메서드가 정의되지 않은 경우, __len__()이 정의되어 있다면 호출되며, 그 결과가 0이 아니면 객체는 참으로 간주됩니다. 클래스가 __len__()도 __bool__()도 정의하지 않은 경우(객체 클래스 자체가 그러함), 모든 인스턴스는 참으로 간주됩니다.

### 3.3.2. Customizing attribute access

### 3.3.2. 속성 접근 사용자 정의

The following methods can be defined to customize the meaning of attribute access (use of, assignment to, or deletion of x.name) for class instances.

다음 메서드는 클래스 인스턴스에 대한 속성 접근(x.name의 사용, 할당 또는 삭제)의 의미를 사용자 정의하기 위해 정의할 수 있습니다.

object.__getattr__(self, name)
Called when the default attribute access fails with an AttributeError (either __getattribute__() raises an AttributeError because name is not an instance attribute or an attribute in the class tree for self; or __get__() of a name property raises AttributeError). This method should either return the (computed) attribute value or raise an AttributeError exception. The object class itself does not provide this method.

object.__getattr__(self, name)
기본 속성 접근이 AttributeError로 실패할 때 호출됩니다(__getattribute__()가 name이 인스턴스 속성이 아니거나 self에 대한 클래스 트리의 속성이 아니기 때문에 AttributeError를 발생시키는 경우, 또는 name 속성의 __get__()이 AttributeError를 발생시키는 경우). 이 메서드는 (계산된) 속성 값을 반환하거나 AttributeError 예외를 발생시켜야 합니다. 객체 클래스 자체는 이 메서드를 제공하지 않습니다.

Note that if the attribute is found through the normal mechanism, __getattr__() is not called. (This is an intentional asymmetry between __getattr__() and __setattr__().) This is done both for efficiency reasons and because otherwise __getattr__() would have no way to access other attributes of the instance. Note that at least for instance variables, you can take total control by not inserting any values in the instance attribute dictionary (but instead inserting them in another object). See the __getattribute__() method below for a way to actually get total control over attribute access.

속성이 일반 메커니즘을 통해 발견되면 __getattr__()이 호출되지 않는다는 점에 유의하세요(__getattr__()와 __setattr__() 사이의 의도적인 비대칭). 이는 효율성 이유와 그렇지 않으면 __getattr__()이 인스턴스의 다른 속성에 접근할 방법이 없기 때문에 수행됩니다. 적어도 인스턴스 변수의 경우, 인스턴스 속성 사전에 값을 삽입하지 않고(대신 다른 객체에 삽입) 완전한 제어권을 가질 수 있습니다. 속성 접근에 대한 실제 완전한 제어권을 얻는 방법은 아래 __getattribute__() 메서드를 참조하세요.

object.__getattribute__(self, name)
Called unconditionally to implement attribute accesses for instances of the class. If the class also defines __getattr__(), the latter will not be called unless __getattribute__() either calls it explicitly or raises an AttributeError. This method should return the (computed) attribute value or raise an AttributeError exception. In order to avoid infinite recursion in this method, its implementation should always call the base class method with the same name to access any attributes it needs, for example, object.__getattribute__(self, name).

object.__getattribute__(self, name)
클래스의 인스턴스에 대한 속성 접근을 구현하기 위해 무조건 호출됩니다. 클래스가 __getattr__()도 정의한 경우, __getattribute__()가 명시적으로 호출하거나 AttributeError를 발생시키지 않는 한 후자는 호출되지 않습니다. 이 메서드는 (계산된) 속성 값을 반환하거나 AttributeError 예외를 발생시켜야 합니다. 이 메서드에서 무한 재귀를 피하기 위해, 그 구현은 항상 필요한 속성에 접근하기 위해 동일한 이름의 기본 클래스 메서드를 호출해야 합니다. 예를 들어, object.__getattribute__(self, name).

Note This method may still be bypassed when looking up special methods as the result of implicit invocation via language syntax or built-in functions. See Special method lookup.

참고: 이 메서드는 언어 구문이나 내장 함수를 통한 암시적 호출의 결과로 특수 메서드를 찾을 때 여전히 우회될 수 있습니다. 특수 메서드 조회를 참조하세요.

For certain sensitive attribute accesses, raises an auditing event object.__getattr__ with arguments obj and name.

특정 민감한 속성 접근의 경우, obj와 name 인수와 함께 감사 이벤트 object.__getattr__을 발생시킵니다.

object.__setattr__(self, name, value)
Called when an attribute assignment is attempted. This is called instead of the normal mechanism (i.e. store the value in the instance dictionary). name is the attribute name, value is the value to be assigned to it.

object.__setattr__(self, name, value)
속성 할당이 시도될 때 호출됩니다. 이것은 일반 메커니즘(즉, 인스턴스 딕셔너리에 값을 저장) 대신 호출됩니다. name은 속성 이름이고, value는 그것에 할당할 값입니다.

If __setattr__() wants to assign to an instance attribute, it should call the base class method with the same name, for example, object.__setattr__(self, name, value).

__setattr__()이 인스턴스 속성에 할당하려면, 동일한 이름의 기본 클래스 메서드를 호출해야 합니다. 예를 들어, object.__setattr__(self, name, value).

For certain sensitive attribute assignments, raises an auditing event object.__setattr__ with arguments obj, name, value.

특정 민감한 속성 할당의 경우, obj, name, value 인수와 함께 감사 이벤트 object.__setattr__을 발생시킵니다.

object.__delattr__(self, name)
Like __setattr__() but for attribute deletion instead of assignment. This should only be implemented if del obj.name is meaningful for the object.

object.__delattr__(self, name)
__setattr__()와 비슷하지만 할당 대신 속성 삭제에 관한 것입니다. 이것은 del obj.name이 객체에 의미가 있는 경우에만 구현되어야 합니다.

For certain sensitive attribute deletions, raises an auditing event object.__delattr__ with arguments obj and name.

특정 민감한 속성 삭제의 경우, obj와 name 인수와 함께 감사 이벤트 object.__delattr__을 발생시킵니다.

object.__dir__(self)
Called when dir() is called on the object. An iterable must be returned. dir() converts the returned iterable to a list and sorts it.

object.__dir__(self)
객체에 대해 dir()이 호출될 때 호출됩니다. 반복 가능한 객체를 반환해야 합니다. dir()은 반환된 반복 가능한 객체를 리스트로 변환하고 정렬합니다.

#### 3.3.2.1. Customizing module attribute access

#### 3.3.2.1. 모듈 속성 접근 사용자 정의

Special names __getattr__ and __dir__ can be also used to customize access to module attributes. The __getattr__ function at the module level should accept one argument which is the name of an attribute and return the computed value or raise an AttributeError. If an attribute is not found on a module object through the normal lookup, i.e. object.__getattribute__(), then __getattr__ is searched in the module __dict__ before raising an AttributeError. If found, it is called with the attribute name and the result is returned.

특수 이름 __getattr__과 __dir__은 모듈 속성에 대한 접근을 사용자 정의하는 데도 사용할 수 있습니다. 모듈 수준의 __getattr__ 함수는 속성의 이름인 하나의 인수를 받아들이고 계산된 값을 반환하거나 AttributeError를 발생시켜야 합니다. 일반 조회, 즉 object.__getattribute__()를 통해 모듈 객체에서 속성을 찾을 수 없는 경우, AttributeError를 발생시키기 전에 모듈 __dict__에서 __getattr__이 검색됩니다. 발견되면, 속성 이름과 함께 호출되고 결과가 반환됩니다.

The __dir__ function should accept no arguments, and return an iterable of strings that represents the names accessible on module. If present, this function overrides the standard dir() search on a module.

__dir__ 함수는 인수를 받지 않아야 하며, 모듈에서 접근 가능한 이름들을 나타내는 문자열의 반복 가능한 객체를 반환해야 합니다. 이 함수가 있으면, 모듈에 대한 표준 dir() 검색을 재정의합니다.

For a more fine grained customization of the module behavior (setting attributes, properties, etc.), one can set the __class__ attribute of a module object to a subclass of types.ModuleType. For example:

모듈 동작의 더 세밀한 사용자 정의(속성 설정, 프로퍼티 등)를 위해, 모듈 객체의 __class__ 속성을 types.ModuleType의 하위 클래스로 설정할 수 있습니다. 예를 들어:

```python
import sys
from types import ModuleType

class VerboseModule(ModuleType):
    def __repr__(self):
        return f'Verbose {self.__name__}'

    def __setattr__(self, attr, value):
        print(f'Setting {attr}...')
        super().__setattr__(attr, value)

sys.modules[__name__].__class__ = VerboseModule
```

Note Defining module __getattr__ and setting module __class__ only affect lookups made using the attribute access syntax – directly accessing the module globals (whether by code within the module, or via a reference to the module's globals dictionary) is unaffected.

참고: 모듈 __getattr__을 정의하고 모듈 __class__를 설정하는 것은 속성 접근 구문을 사용하는 조회에만 영향을 미칩니다 - 모듈 전역 변수에 직접 접근(모듈 내의 코드에 의한 것이든, 모듈의 전역 딕셔너리에 대한 참조를 통한 것이든)하는 것은 영향을 받지 않습니다.

Changed in version 3.5: __class__ module attribute is now writable.

버전 3.5에서 변경됨: __class__ 모듈 속성이 이제 쓰기 가능합니다.

Added in version 3.7: __getattr__ and __dir__ module attributes.

버전 3.7에서 추가됨: __getattr__ 및 __dir__ 모듈 속성.

See also
PEP 562 - Module __getattr__ and __dir__
Describes the __getattr__ and __dir__ functions on modules.

참고
PEP 562 - 모듈 __getattr__ 및 __dir__
모듈의 __getattr__ 및 __dir__ 함수에 대해 설명합니다.

#### 3.3.2.2. Implementing Descriptors

#### 3.3.2.2. 디스크립터 구현하기

The following methods only apply when an instance of the class containing the method (a so-called descriptor class) appears in an owner class (the descriptor must be in either the owner's class dictionary or in the class dictionary for one of its parents). In the examples below, "the attribute" refers to the attribute whose name is the key of the property in the owner class' __dict__. The object class itself does not implement any of these protocols.

다음 메서드들은 메서드를 포함하는 클래스(소위 디스크립터 클래스)의 인스턴스가 소유자 클래스에 나타날 때만 적용됩니다(디스크립터는 소유자의 클래스 딕셔너리 또는 상위 클래스 중 하나의 클래스 딕셔너리에 있어야 함). 아래 예시에서, "속성"은 소유자 클래스의 __dict__에서 프로퍼티의 키인 속성 이름을 의미합니다. 객체 클래스 자체는 이러한 프로토콜을 구현하지 않습니다.

object.__get__(self, instance, owner=None)
Called to get the attribute of the owner class (class attribute access) or of an instance of that class (instance attribute access). The optional owner argument is the owner class, while instance is the instance that the attribute was accessed through, or None when the attribute is accessed through the owner.

object.__get__(self, instance, owner=None)
소유자 클래스의 속성(클래스 속성 접근) 또는 해당 클래스의 인스턴스의 속성(인스턴스 속성 접근)을 가져오기 위해 호출됩니다. 선택적 owner 인수는 소유자 클래스이고, instance는 속성이 접근된 인스턴스입니다. 속성이 소유자를 통해 접근되면 None입니다.

This method should return the computed attribute value or raise an AttributeError exception.

이 메서드는 계산된 속성 값을 반환하거나 AttributeError 예외를 발생시켜야 합니다.

PEP 252 specifies that __get__() is callable with one or two arguments. Python's own built-in descriptors support this specification; however, it is likely that some third-party tools have descriptors that require both arguments. Python's own __getattribute__() implementation always passes in both arguments whether they are required or not.

PEP 252는 __get__()이 하나 또는 두 개의 인수와 함께 호출 가능하다고 명시합니다. 파이썬의 자체 내장 디스크립터는 이 사양을 지원합니다. 그러나 일부 서드파티 도구는 두 인수를 모두 필요로 하는 디스크립터를 가질 수 있습니다. 파이썬의 자체 __getattribute__() 구현은 필요하든 필요하지 않든 항상 두 인수를 모두 전달합니다.

object.__set__(self, instance, value)
Called to set the attribute on an instance instance of the owner class to a new value, value.

object.__set__(self, instance, value)
소유자 클래스의 인스턴스에서 속성을 새 값 value로 설정하기 위해 호출됩니다.

Note, adding __set__() or __delete__() changes the kind of descriptor to a "data descriptor". See Invoking Descriptors for more details.

참고, __set__() 또는 __delete__()를 추가하면 디스크립터의 종류가 "데이터 디스크립터"로 바뀝니다. 자세한 내용은 디스크립터 호출을 참조하세요.

object.__delete__(self, instance)
Called to delete the attribute on an instance instance of the owner class.

object.__delete__(self, instance)
소유자 클래스의 인스턴스에서 속성을 삭제하기 위해 호출됩니다.

Instances of descriptors may also have the __objclass__ attribute present:

디스크립터 인스턴스는 __objclass__ 속성도 가질 수 있습니다:

object.__objclass__
The attribute __objclass__ is interpreted by the inspect module as specifying the class where this object was defined (setting this appropriately can assist in runtime introspection of dynamic class attributes). For callables, it may indicate that an instance of the given type (or a subclass) is expected or required as the first positional argument (for example, CPython sets this attribute for unbound methods that are implemented in C).

object.__objclass__
__objclass__ 속성은 inspect 모듈에 의해 이 객체가 정의된 클래스를 지정하는 것으로 해석됩니다(이를 적절히 설정하면 동적 클래스 속성의 런타임 내부 검사를 지원할 수 있음). 호출 가능한 객체의 경우, 주어진 타입(또는 하위 클래스)의 인스턴스가 첫 번째 위치 인수로 예상되거나 필요하다는 것을 나타낼 수 있습니다(예를 들어, CPython은 C로 구현된 비바인딩 메서드에 대해 이 속성을 설정함).

#### 3.3.2.3. Invoking Descriptors

#### 3.3.2.3. 디스크립터 호출

In general, a descriptor is an object attribute with "binding behavior", one whose attribute access has been overridden by methods in the descriptor protocol: __get__(), __set__(), and __delete__(). If any of those methods are defined for an object, it is said to be a descriptor.

일반적으로, 디스크립터는 "바인딩 동작"을 가진 객체 속성으로, 디스크립터 프로토콜의 메서드에 의해 속성 접근이 재정의된 것입니다: __get__(), __set__(), __delete__(). 객체에 이러한 메서드 중 하나라도 정의되어 있으면 디스크립터라고 합니다.

The default behavior for attribute access is to get, set, or delete the attribute from an object's dictionary. For instance, a.x has a lookup chain starting with a.__dict__['x'], then type(a).__dict__['x'], and continuing through the base classes of type(a) excluding metaclasses.

속성 접근의 기본 동작은 객체의 딕셔너리에서 속성을 가져오거나, 설정하거나, 삭제하는 것입니다. 예를 들어, a.x는 a.__dict__['x']부터 시작하여 type(a).__dict__['x'], 그리고 메타클래스를 제외한 type(a)의 기본 클래스들을 통과하는 조회 체인을 가집니다.

However, if the looked-up value is an object defining one of the descriptor methods, then Python may override the default behavior and invoke the descriptor method instead. Where this occurs in the precedence chain depends on which descriptor methods were defined and how they were called.

그러나, 조회된 값이 디스크립터 메서드 중 하나를 정의하는 객체라면, 파이썬은 기본 동작을 재정의하고 대신 디스크립터 메서드를 호출할 수 있습니다. 이것이 우선 순위 체인에서 어디에서 발생하는지는 어떤 디스크립터 메서드가 정의되었고 어떻게 호출되었는지에 따라 달라집니다.

The starting point for descriptor invocation is a binding, a.x. How the arguments are assembled depends on a:

디스크립터 호출의 시작점은 바인딩 a.x입니다. 인수가 어떻게 조립되는지는 a에 따라 달라집니다:

Direct Call
The simplest and least common call is when user code directly invokes a descriptor method: x.__get__(a).

직접 호출
가장 단순하고 가장 적은 일반적인 호출은 사용자 코드가 디스크립터 메서드를 직접 호출할 때입니다: x.__get__(a).

Instance Binding
If binding to an object instance, a.x is transformed into the call: type(a).__dict__['x'].__get__(a, type(a)).

인스턴스 바인딩
객체 인스턴스에 바인딩하는 경우, a.x는 다음 호출로 변환됩니다: type(a).__dict__['x'].__get__(a, type(a)).

Class Binding
If binding to a class, A.x is transformed into the call: A.__dict__['x'].__get__(None, A).

클래스 바인딩
클래스에 바인딩하는 경우, A.x는 다음 호출로 변환됩니다: A.__dict__['x'].__get__(None, A).

Super Binding
A dotted lookup such as super(A, a).x searches a.__class__.__mro__ for a base class B following A and then returns B.__dict__['x'].__get__(a, A). If not a descriptor, x is returned unchanged.

슈퍼 바인딩
super(A, a).x와 같은 점으로 구분된 조회는 a.__class__.__mro__에서 A 다음에 오는 기본 클래스 B를 검색한 다음 B.__dict__['x'].__get__(a, A)를 반환합니다. 디스크립터가 아닌 경우, x는 변경되지 않고 반환됩니다.

For instance bindings, the precedence of descriptor invocation depends on which descriptor methods are defined. A descriptor can define any combination of __get__(), __set__() and __delete__(). If it does not define __get__(), then accessing the attribute will return the descriptor object itself unless there is a value in the object's instance dictionary. If the descriptor defines __set__() and/or __delete__(), it is a data descriptor; if it defines neither, it is a non-data descriptor. Normally, data descriptors define both __get__() and __set__(), while non-data descriptors have just the __get__() method. Data descriptors with __get__() and __set__() (and/or __delete__()) defined always override a redefinition in an instance dictionary. In contrast, non-data descriptors can be overridden by instances.

인스턴스 바인딩의 경우, 디스크립터 호출의 우선 순위는 어떤 디스크립터 메서드가 정의되었는지에 따라 달라집니다. 디스크립터는 __get__(), __set__() 및 __delete__()의 모든 조합을 정의할 수 있습니다. __get__()을 정의하지 않으면, 객체의 인스턴스 딕셔너리에 값이 없는 한 속성에 접근하면 디스크립터 객체 자체를 반환합니다. 디스크립터가 __set__() 및/또는 __delete__()를 정의하면, 그것은 데이터 디스크립터입니다; 둘 다 정의하지 않으면, 이것은 비데이터 디스크립터입니다. 일반적으로, 데이터 디스크립터는 __get__()과 __set__() 모두를 정의하고, 비데이터 디스크립터는 __get__() 메서드만 가집니다. __get__()과 __set__()(및/또는 __delete__())이 정의된 데이터 디스크립터는 항상 인스턴스 딕셔너리의 재정의를 무시합니다. 반면에, 비데이터 디스크립터는 인스턴스에 의해 재정의될 수 있습니다.

Python methods (including those decorated with @staticmethod and @classmethod) are implemented as non-data descriptors. Accordingly, instances can redefine and override methods. This allows individual instances to acquire behaviors that differ from other instances of the same class.

파이썬 메서드(@staticmethod 및 @classmethod로 장식된 것 포함)는 비데이터 디스크립터로 구현됩니다. 따라서, 인스턴스는 메서드를 재정의하고 오버라이드할 수 있습니다. 이를 통해 개별 인스턴스는 동일한 클래스의 다른 인스턴스와 다른 동작을 획득할 수 있습니다.

The property() function is implemented as a data descriptor. Accordingly, instances cannot override the behavior of a property.

property() 함수는 데이터 디스크립터로 구현됩니다. 따라서, 인스턴스는 프로퍼티의 동작을 오버라이드할 수 없습니다.

#### 3.3.2.4. __slots__

#### 3.3.2.4. __slots__

__slots__ allow us to explicitly declare data members (like properties) and deny the creation of __dict__ and __weakref__ (unless explicitly declared in __slots__ or available in a parent.)

__slots__를 사용하면 데이터 멤버(속성과 같은)를 명시적으로 선언하고 __dict__와 __weakref__의 생성을 방지할 수 있습니다(__slots__에 명시적으로 선언되거나 부모에서 사용 가능한 경우 제외).

The space saved over using __dict__ can be significant. Attribute lookup speed can be significantly improved as well.

__dict__ 사용 대비 절약되는 공간은 상당할 수 있습니다. 속성 검색 속도도 크게 향상될 수 있습니다.

object.__slots__
This class variable can be assigned a string, iterable, or sequence of strings with variable names used by instances. __slots__ reserves space for the declared variables and prevents the automatic creation of __dict__ and __weakref__ for each instance.

object.__slots__
이 클래스 변수에는 인스턴스에서 사용되는 변수 이름을 가진 문자열, 반복 가능한 객체 또는 문자열 시퀀스가 할당될 수 있습니다. __slots__는 선언된 변수를 위한 공간을 예약하고 각 인스턴스에 대한 __dict__와 __weakref__의 자동 생성을 방지합니다.

Notes on using __slots__:

__slots__ 사용 시 주의사항:

When inheriting from a class without __slots__, the __dict__ and __weakref__ attribute of the instances will always be accessible.

__slots__가 없는 클래스에서 상속받을 때, 인스턴스의 __dict__와 __weakref__ 속성은 항상 접근 가능합니다.

Without a __dict__ variable, instances cannot be assigned new variables not listed in the __slots__ definition. Attempts to assign to an unlisted variable name raises AttributeError. If dynamic assignment of new variables is desired, then add '__dict__' to the sequence of strings in the __slots__ declaration.

__dict__ 변수가 없으면, 인스턴스에 __slots__ 정의에 나열되지 않은 새 변수를 할당할 수 없습니다. 나열되지 않은 변수 이름에 할당하려고 하면 AttributeError가 발생합니다. 새 변수의 동적 할당이 필요하면 __slots__ 선언의 문자열 시퀀스에 '__dict__'를 추가하세요.

Without a __weakref__ variable for each instance, classes defining __slots__ do not support weak references to its instances. If weak reference support is needed, then add '__weakref__' to the sequence of strings in the __slots__ declaration.

각 인스턴스에 __weakref__ 변수가 없으면, __slots__를 정의하는 클래스는 자신의 인스턴스에 대한 약한 참조를 지원하지 않습니다. 약한 참조 지원이 필요하면 __slots__ 선언의 문자열 시퀀스에 '__weakref__'를 추가하세요.

__slots__ are implemented at the class level by creating descriptors for each variable name. As a result, class attributes cannot be used to set default values for instance variables defined by __slots__; otherwise, the class attribute would overwrite the descriptor assignment.

__slots__는 각 변수 이름에 대해 디스크립터를 생성하여 클래스 수준에서 구현됩니다. 따라서 클래스 속성을 사용하여 __slots__에 의해 정의된 인스턴스 변수의 기본값을 설정할 수 없습니다. 그렇지 않으면 클래스 속성이 디스크립터 할당을 덮어쓰게 됩니다.

The action of a __slots__ declaration is not limited to the class where it is defined. __slots__ declared in parents are available in child classes. However, instances of a child subclass will get a __dict__ and __weakref__ unless the subclass also defines __slots__ (which should only contain names of any additional slots).

__slots__ 선언의 작용은 정의된 클래스로 제한되지 않습니다. 부모에서 선언된 __slots__는 자식 클래스에서도 사용할 수 있습니다. 그러나 하위 클래스도 __slots__를 정의하지 않는 한(추가 슬롯의 이름만 포함해야 함) 자식 하위 클래스의 인스턴스는 __dict__와 __weakref__를 갖게 됩니다.

If a class defines a slot also defined in a base class, the instance variable defined by the base class slot is inaccessible (except by retrieving its descriptor directly from the base class). This renders the meaning of the program undefined. In the future, a check may be added to prevent this.

클래스가 기본 클래스에서도 정의된 슬롯을 정의하는 경우, 기본 클래스 슬롯에 의해 정의된 인스턴스 변수는 접근할 수 없게 됩니다(기본 클래스에서 직접 디스크립터를 검색하는 경우 제외). 이로 인해 프로그램의 의미가 정의되지 않게 됩니다. 향후에는 이를 방지하기 위한 검사가 추가될 수 있습니다.

TypeError will be raised if nonempty __slots__ are defined for a class derived from a "variable-length" built-in type such as int, bytes, and tuple.

int, bytes, tuple과 같은 "가변 길이" 내장 타입에서 파생된 클래스에 비어 있지 않은 __slots__가 정의된 경우 TypeError가 발생합니다.

Any non-string iterable may be assigned to __slots__.

문자열이 아닌 모든 반복 가능한 객체는 __slots__에 할당될 수 있습니다.

If a dictionary is used to assign __slots__, the dictionary keys will be used as the slot names. The values of the dictionary can be used to provide per-attribute docstrings that will be recognised by inspect.getdoc() and displayed in the output of help().

딕셔너리를 사용하여 __slots__를 할당하는 경우, 딕셔너리 키가 슬롯 이름으로 사용됩니다. 딕셔너리의 값은 inspect.getdoc()에 의해 인식되고 help() 출력에 표시되는 속성별 문서 문자열을 제공하는 데 사용될 수 있습니다.

__class__ assignment works only if both classes have the same __slots__.

__class__ 할당은 두 클래스가 동일한 __slots__를 가진 경우에만 작동합니다.

Multiple inheritance with multiple slotted parent classes can be used, but only one parent is allowed to have attributes created by slots (the other bases must have empty slot layouts) - violations raise TypeError.

여러 슬롯이 있는 부모 클래스를 사용한 다중 상속도 가능하지만, 슬롯에 의해 생성된 속성을 가질 수 있는 부모는 하나만 허용됩니다(다른 기본 클래스는 빈 슬롯 레이아웃을 가져야 함) - 위반 시 TypeError가 발생합니다.

If an iterator is used for __slots__ then a descriptor is created for each of the iterator's values. However, the __slots__ attribute will be an empty iterator.

반복자가 __slots__에 사용되면 반복자의 각 값에 대해 디스크립터가 생성됩니다. 그러나 __slots__ 속성은 빈 반복자가 됩니다.

### 3.3.3. Customizing class creation

### 3.3.3. 클래스 생성 사용자 정의

Whenever a class inherits from another class, __init_subclass__() is called on the parent class. This way, it is possible to write classes which change the behavior of subclasses. This is closely related to class decorators, but where class decorators only affect the specific class they're applied to, __init_subclass__ solely applies to future subclasses of the class defining the method.

클래스가 다른 클래스에서 상속할 때마다, 부모 클래스에서 __init_subclass__()가 호출됩니다. 이렇게 하면 하위 클래스의 동작을 변경하는 클래스를 작성할 수 있습니다. 이는 클래스 데코레이터와 밀접하게 관련되어 있지만, 클래스 데코레이터는 적용된 특정 클래스에만 영향을 미치는 반면, __init_subclass__는 메서드를 정의하는 클래스의 미래 하위 클래스에만 적용됩니다.

classmethod object.__init_subclass__(cls)
This method is called whenever the containing class is subclassed. cls is then the new subclass. If defined as a normal instance method, this method is implicitly converted to a class method.

classmethod object.__init_subclass__(cls)
이 메서드는 포함하는 클래스가 하위 클래스화될 때마다 호출됩니다. cls는 새로운 하위 클래스입니다. 일반 인스턴스 메서드로 정의된 경우, 이 메서드는 암시적으로 클래스 메서드로 변환됩니다.

Keyword arguments which are given to a new class are passed to the parent class's __init_subclass__. For compatibility with other classes using __init_subclass__, one should take out the needed keyword arguments and pass the others over to the base class, as in:

새 클래스에 주어진 키워드 인수는 부모 클래스의 __init_subclass__에 전달됩니다. __init_subclass__를 사용하는 다른 클래스와의 호환성을 위해, 필요한 키워드 인수를 꺼내고 나머지는 기본 클래스에 전달해야 합니다. 예:

```python
class Philosopher:
    def __init_subclass__(cls, /, default_name, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.default_name = default_name

class AustralianPhilosopher(Philosopher, default_name="Bruce"):
    pass
```

The default implementation object.__init_subclass__ does nothing, but raises an error if it is called with any arguments.

기본 구현 object.__init_subclass__는 아무 것도 하지 않지만, 인수와 함께 호출되면 오류를 발생시킵니다.

Note The metaclass hint metaclass is consumed by the rest of the type machinery, and is never passed to __init_subclass__ implementations. The actual metaclass (rather than the explicit hint) can be accessed as type(cls).

참고 메타클래스 힌트 metaclass는 나머지 타입 기계에 의해 소비되며, __init_subclass__ 구현에 전달되지 않습니다. 실제 메타클래스(명시적 힌트가 아닌)는 type(cls)로 접근할 수 있습니다.

Added in version 3.6.

버전 3.6에서 추가됨.

When a class is created, type.__new__() scans the class variables and makes callbacks to those with a __set_name__() hook.

클래스가 생성될 때, type.__new__()는 클래스 변수를 스캔하고 __set_name__() 후크가 있는 변수에 콜백을 만듭니다.

object.__set_name__(self, owner, name)
Automatically called at the time the owning class owner is created. The object has been assigned to name in that class:

object.__set_name__(self, owner, name)
소유 클래스 owner가 생성될 때 자동으로 호출됩니다. 객체는 해당 클래스의 name에 할당되었습니다:

```python
class A:
    x = C()  # Automatically calls: x.__set_name__(A, 'x')
```

If the class variable is assigned after the class is created, __set_name__() will not be called automatically. If needed, __set_name__() can be called directly:

클래스 변수가 클래스 생성 후에 할당되면, __set_name__()은 자동으로 호출되지 않습니다. 필요한 경우 __set_name__()을 직접 호출할 수 있습니다:

```python
class A:
   pass

c = C()
A.x = c                  # The hook is not called
c.__set_name__(A, 'x')   # Manually invoke the hook
```

See Creating the class object for more details.

자세한 내용은 클래스 객체 생성을 참조하세요.

Added in version 3.6.

버전 3.6에서 추가됨.

#### 3.3.3.1. Metaclasses

#### 3.3.3.1. 메타클래스

By default, classes are constructed using type(). The class body is executed in a new namespace and the class name is bound locally to the result of type(name, bases, namespace).

기본적으로 클래스는 type()을 사용하여 생성됩니다. 클래스 본문은 새 네임스페이스에서 실행되며 클래스 이름은 type(name, bases, namespace)의 결과에 지역적으로 바인딩됩니다.

The class creation process can be customized by passing the metaclass keyword argument in the class definition line, or by inheriting from an existing class that included such an argument. In the following example, both MyClass and MySubclass are instances of Meta:

클래스 생성 프로세스는 클래스 정의 줄에 metaclass 키워드 인수를 전달하거나, 이러한 인수를 포함한 기존 클래스에서 상속받음으로써 사용자 정의할 수 있습니다. 다음 예에서 MyClass와 MySubclass는 모두 Meta의 인스턴스입니다:

```python
class Meta(type):
    pass

class MyClass(metaclass=Meta):
    pass

class MySubclass(MyClass):
    pass
```

Any other keyword arguments that are specified in the class definition are passed through to all metaclass operations described below.

클래스 정의에 지정된 다른 모든 키워드 인수는 아래에 설명된 모든 메타클래스 연산에 전달됩니다.

When a class definition is executed, the following steps occur:

클래스 정의가 실행될 때 다음 단계가 발생합니다:

MRO entries are resolved;

MRO 항목이 해결됩니다;

the appropriate metaclass is determined;

적절한 메타클래스가 결정됩니다;

the class namespace is prepared;

클래스 네임스페이스가 준비됩니다;

the class body is executed;

클래스 본문이 실행됩니다;

the class object is created.

클래스 객체가 생성됩니다.

#### 3.3.3.2. Resolving MRO entries

#### 3.3.3.2. MRO 항목 해결

object.__mro_entries__(self, bases)
If a base that appears in a class definition is not an instance of type, then an __mro_entries__() method is searched on the base. If an __mro_entries__() method is found, the base is substituted with the result of a call to __mro_entries__() when creating the class. The method is called with the original bases tuple passed to the bases parameter, and must return a tuple of classes that will be used instead of the base. The returned tuple may be empty: in these cases, the original base is ignored.

object.__mro_entries__(self, bases)
클래스 정의에 나타나는 기본 클래스가 type의 인스턴스가 아닌 경우, 해당 기본 클래스에서 __mro_entries__() 메서드를 검색합니다. __mro_entries__() 메서드가 발견되면, 클래스를 생성할 때 기본 클래스는 __mro_entries__() 호출 결과로 대체됩니다. 이 메서드는 원래의 기본 클래스 튜플이 bases 매개변수로 전달되어 호출되며, 기본 클래스 대신 사용될 클래스의 튜플을 반환해야 합니다. 반환된 튜플은 비어 있을 수 있습니다. 이 경우, 원래의 기본 클래스는 무시됩니다.

See also
types.resolve_bases()
Dynamically resolve bases that are not instances of type.

참고
types.resolve_bases()
type의 인스턴스가 아닌 기본 클래스를 동적으로 해결합니다.

types.get_original_bases()
Retrieve a class's "original bases" prior to modifications by __mro_entries__().

types.get_original_bases()
__mro_entries__()에 의한 수정 이전의 클래스의 "원래 기본 클래스"를 검색합니다.

PEP 560
Core support for typing module and generic types.

PEP 560
typing 모듈 및 제네릭 타입에 대한 핵심 지원.

#### 3.3.3.3. Determining the appropriate metaclass

#### 3.3.3.3. 적절한 메타클래스 결정

The appropriate metaclass for a class definition is determined as follows:

클래스 정의에 대한 적절한 메타클래스는 다음과 같이 결정됩니다:

if no bases and no explicit metaclass are given, then type() is used;

기본 클래스와 명시적 메타클래스가 모두 지정되지 않은 경우, type()이 사용됩니다;

if an explicit metaclass is given and it is not an instance of type(), then it is used directly as the metaclass;

명시적 메타클래스가 지정되고 이것이 type()의 인스턴스가 아닌 경우, 이는 메타클래스로 직접 사용됩니다;

if an instance of type() is given as the explicit metaclass, or bases are defined, then the most derived metaclass is used.

명시적 메타클래스로 type()의 인스턴스가 지정되거나, 기본 클래스가 정의된 경우, 가장 파생된 메타클래스가 사용됩니다.

The most derived metaclass is selected from the explicitly specified metaclass (if any) and the metaclasses (i.e. type(cls)) of all specified base classes. The most derived metaclass is one which is a subtype of all of these candidate metaclasses. If none of the candidate metaclasses meets that criterion, then the class definition will fail with TypeError.

가장 파생된 메타클래스는 명시적으로 지정된 메타클래스(있는 경우)와 모든 지정된 기본 클래스의 메타클래스(즉, type(cls))에서 선택됩니다. 가장 파생된 메타클래스는 이러한 모든 후보 메타클래스의 하위 타입인 메타클래스입니다. 후보 메타클래스 중 어느 것도 이 기준을 충족하지 않으면 클래스 정의는 TypeError로 실패합니다.

#### 3.3.3.4. Preparing the class namespace

#### 3.3.3.4. 클래스 네임스페이스 준비

Once the appropriate metaclass has been identified, then the class namespace is prepared. If the metaclass has a __prepare__ attribute, it is called as namespace = metaclass.__prepare__(name, bases, **kwds) (where the additional keyword arguments, if any, come from the class definition). The __prepare__ method should be implemented as a classmethod. The namespace returned by __prepare__ is passed in to __new__, but when the final class object is created the namespace is copied into a new dict.

적절한 메타클래스가 식별되면 클래스 네임스페이스가 준비됩니다. 메타클래스에 __prepare__ 속성이 있는 경우, namespace = metaclass.__prepare__(name, bases, **kwds)로 호출됩니다 (추가 키워드 인수가 있는 경우 클래스 정의에서 옵니다). __prepare__ 메서드는 클래스 메서드로 구현되어야 합니다. __prepare__가 반환한 네임스페이스는 __new__에 전달되지만, 최종 클래스 객체가 생성될 때 네임스페이스는 새 딕셔너리에 복사됩니다.

If the metaclass has no __prepare__ attribute, then the class namespace is initialised as an empty ordered mapping.

메타클래스에 __prepare__ 속성이 없으면 클래스 네임스페이스는 빈 순서가 있는 매핑으로 초기화됩니다.

See also
PEP 3115 - Metaclasses in Python 3000
Introduced the __prepare__ namespace hook

참고
PEP 3115 - Python 3000의 메타클래스
__prepare__ 네임스페이스 후크 소개

#### 3.3.3.5. Executing the class body

#### 3.3.3.5. 클래스 본문 실행

The class body is executed (approximately) as exec(body, globals(), namespace). The key difference from a normal call to exec() is that lexical scoping allows the class body (including any methods) to reference names from the current and outer scopes when the class definition occurs inside a function.

클래스 본문은 (대략적으로) exec(body, globals(), namespace)로 실행됩니다. 일반 exec() 호출과의 주요 차이점은 어휘적 스코핑이 클래스 정의가 함수 내에서 발생할 때 클래스 본문(모든 메서드 포함)이 현재 및 외부 스코프의 이름을 참조할 수 있게 한다는 것입니다.

However, even when the class definition occurs inside the function, methods defined inside the class still cannot see names defined at the class scope. Class variables must be accessed through the first parameter of instance or class methods, or through the implicit lexically scoped __class__ reference described in the next section.

그러나 클래스 정의가 함수 내부에서 발생하더라도, 클래스 내부에 정의된 메서드는 여전히 클래스 스코프에 정의된 이름을 볼 수 없습니다. 클래스 변수는 인스턴스나 클래스 메서드의 첫 번째 매개변수를 통해, 또는 다음 섹션에서 설명하는 암시적 어휘적 스코프의 __class__ 참조를 통해 액세스해야 합니다.

#### 3.3.3.6. Creating the class object

#### 3.3.3.6. 클래스 객체 생성

Once the class namespace has been populated by executing the class body, the class object is created by calling metaclass(name, bases, namespace, **kwds) (the additional keywords passed here are the same as those passed to __prepare__).

클래스 본문을 실행하여 클래스 네임스페이스가 채워지면, metaclass(name, bases, namespace, **kwds)를 호출하여 클래스 객체가 생성됩니다 (여기서 전달되는 추가 키워드는 __prepare__에 전달되는 것과 동일합니다).

This class object is the one that will be referenced by the zero-argument form of super(). __class__ is an implicit closure reference created by the compiler if any methods in a class body refer to either __class__ or super. This allows the zero argument form of super() to correctly identify the class being defined based on lexical scoping, while the class or instance that was used to make the current call is identified based on the first argument passed to the method.

이 클래스 객체는 인수가 없는 형태의 super()에 의해 참조될 객체입니다. __class__는 클래스 본문의 메서드가 __class__ 또는 super를 참조하는 경우 컴파일러가 생성하는 암시적 클로저 참조입니다. 이렇게 하면 super()의 인수가 없는 형태가 어휘적 스코핑을 기반으로 정의되는 클래스를 올바르게 식별할 수 있으며, 현재 호출에 사용된 클래스나 인스턴스는 메서드에 전달된 첫 번째 인수를 기반으로 식별됩니다.

CPython implementation detail: In CPython 3.6 and later, the __class__ cell is passed to the metaclass as a __classcell__ entry in the class namespace. If present, this must be propagated up to the type.__new__ call in order for the class to be initialised correctly. Failing to do so will result in a RuntimeError in Python 3.8.

CPython 구현 세부 사항: CPython 3.6 이상에서 __class__ 셀은 클래스 네임스페이스의 __classcell__ 항목으로 메타클래스에 전달됩니다. 이 항목이 존재하는 경우, 클래스가 올바르게 초기화되도록 type.__new__ 호출까지 전파되어야 합니다. 그렇지 않으면 Python 3.8에서 RuntimeError가 발생합니다.

When using the default metaclass type, or any metaclass that ultimately calls type.__new__, the following additional customization steps are invoked after creating the class object:

기본 메타클래스 type 또는 최종적으로 type.__new__를 호출하는 메타클래스를 사용할 때, 클래스 객체를 생성한 후 다음과 같은 추가 사용자 정의 단계가 호출됩니다:

The type.__new__ method collects all of the attributes in the class namespace that define a __set_name__() method;

type.__new__ 메서드는 __set_name__() 메서드를 정의하는 클래스 네임스페이스의 모든 속성을 수집합니다;

Those __set_name__ methods are called with the class being defined and the assigned name of that particular attribute;

이러한 __set_name__ 메서드는 정의되는 클래스와 해당 특정 속성의 할당된 이름으로 호출됩니다;

The __init_subclass__() hook is called on the immediate parent of the new class in its method resolution order.

__init_subclass__() 훅은 메서드 해결 순서에서 새 클래스의 직계 상위 클래스에서 호출됩니다.

After the class object is created, it is passed to the class decorators included in the class definition (if any) and the resulting object is bound in the local namespace as the defined class.

클래스 객체가 생성된 후, 클래스 정의에 포함된 클래스 데코레이터(있는 경우)에 전달되고 결과 객체는 정의된 클래스로서 로컬 네임스페이스에 바인딩됩니다.

When a new class is created by type.__new__, the object provided as the namespace parameter is copied to a new ordered mapping and the original object is discarded. The new copy is wrapped in a read-only proxy, which becomes the __dict__ attribute of the class object.

type.__new__에 의해 새 클래스가 생성될 때, 네임스페이스 매개변수로 제공된 객체는 새로운 순서가 있는 매핑에 복사되고 원래 객체는 폐기됩니다. 새 복사본은 읽기 전용 프록시로 감싸지며, 이는 클래스 객체의 __dict__ 속성이 됩니다.

See also
PEP 3135 - New super
Describes the implicit __class__ closure reference

참고
PEP 3135 - 새로운 super
암시적 __class__ 클로저 참조를 설명합니다

#### 3.3.3.7. Uses for metaclasses

#### 3.3.3.7. 메타클래스의 사용 사례

The potential uses for metaclasses are boundless. Some ideas that have been explored include enum, logging, interface checking, automatic delegation, automatic property creation, proxies, frameworks, and automatic resource locking/synchronization.

메타클래스의 잠재적인 사용 사례는 무궁무진합니다. 탐색된 아이디어 중 일부는 열거형, 로깅, 인터페이스 검사, 자동 위임, 자동 속성 생성, 프록시, 프레임워크, 자동 리소스 잠금/동기화 등이 있습니다.

### 3.3.4. Customizing instance and subclass checks

### 3.3.4. 인스턴스 및 하위 클래스 검사 사용자 정의

The following methods are used to override the default behavior of the isinstance() and issubclass() built-in functions.

다음 메서드들은 isinstance()와 issubclass() 내장 함수의 기본 동작을 재정의하는 데 사용됩니다.

In particular, the metaclass abc.ABCMeta implements these methods in order to allow the addition of Abstract Base Classes (ABCs) as "virtual base classes" to any class or type (including built-in types), including other ABCs.

특히, abc.ABCMeta 메타클래스는 다른 ABC를 포함하여 모든 클래스나 타입(내장 타입 포함)에 "가상 기본 클래스"로 추상 기본 클래스(ABC)를 추가할 수 있도록 이러한 메서드를 구현합니다.

type.__instancecheck__(self, instance)
Return true if instance should be considered a (direct or indirect) instance of class. If defined, called to implement isinstance(instance, class).

type.__instancecheck__(self, instance)
instance가 클래스의 (직접 또는 간접적인) 인스턴스로 간주되어야 하는 경우 true를 반환합니다. 정의된 경우, isinstance(instance, class)를 구현하기 위해 호출됩니다.

type.__subclasscheck__(self, subclass)
Return true if subclass should be considered a (direct or indirect) subclass of class. If defined, called to implement issubclass(subclass, class).

type.__subclasscheck__(self, subclass)
subclass가 클래스의 (직접 또는 간접적인) 하위 클래스로 간주되어야 하는 경우 true를 반환합니다. 정의된 경우, issubclass(subclass, class)를 구현하기 위해 호출됩니다.

Note that these methods are looked up on the type (metaclass) of a class. They cannot be defined as class methods in the actual class. This is consistent with the lookup of special methods that are called on instances, only in this case the instance is itself a class.

이러한 메서드는 클래스의 타입(메타클래스)에서 조회된다는 점에 주의하세요. 이는 실제 클래스에서 클래스 메서드로 정의될 수 없습니다. 이는 인스턴스에서 호출되는 특수 메서드의 조회와 일관되며, 단지 이 경우 인스턴스 자체가 클래스입니다.

See also
PEP 3119 - Introducing Abstract Base Classes
Includes the specification for customizing isinstance() and issubclass() behavior through __instancecheck__() and __subclasscheck__(), with motivation for this functionality in the context of adding Abstract Base Classes (see the abc module) to the language.

참고
PEP 3119 - 추상 기본 클래스 소개
__instancecheck__()와 __subclasscheck__()를 통해 isinstance()와 issubclass() 동작을 사용자 정의하기 위한 명세를 포함하며, 언어에 추상 기본 클래스(abc 모듈 참조)를 추가하는 맥락에서 이 기능의 동기에 대해 설명합니다.

### 3.3.5. Emulating generic types

### 3.3.5. 제네릭 타입 에뮬레이션

When using type annotations, it is often useful to parameterize a generic type using Python's square-brackets notation. For example, the annotation list[int] might be used to signify a list in which all the elements are of type int.

타입 어노테이션을 사용할 때, 파이썬의 대괄호 표기법을 사용하여 제네릭 타입을 매개변수화하는 것이 유용한 경우가 많습니다. 예를 들어, list[int] 어노테이션은 모든 요소가 int 타입인 리스트를 나타내는 데 사용될 수 있습니다.

See also
PEP 484 - Type Hints
Introducing Python's framework for type annotations

참고
PEP 484 - 타입 힌트
파이썬의 타입 어노테이션 프레임워크 소개

Generic Alias Types
Documentation for objects representing parameterized generic classes

제네릭 앨리어스 타입
매개변수화된 제네릭 클래스를 나타내는 객체에 대한 문서

Generics, user-defined generics and typing.Generic
Documentation on how to implement generic classes that can be parameterized at runtime and understood by static type-checkers.

제네릭, 사용자 정의 제네릭 및 typing.Generic
런타임에 매개변수화될 수 있고 정적 타입 검사기가 이해할 수 있는 제네릭 클래스를 구현하는 방법에 대한 문서

A class can generally only be parameterized if it defines the special class method __class_getitem__().

클래스는 일반적으로 특수 클래스 메서드 __class_getitem__()을 정의한 경우에만 매개변수화될 수 있습니다.

classmethod object.__class_getitem__(cls, key)
Return an object representing the specialization of a generic class by type arguments found in key.

classmethod object.__class_getitem__(cls, key)
key에서 발견된 타입 인수에 의한 제네릭 클래스의 특수화를 나타내는 객체를 반환합니다.

When defined on a class, __class_getitem__() is automatically a class method. As such, there is no need for it to be decorated with @classmethod when it is defined.

클래스에 정의될 때, __class_getitem__()은 자동으로 클래스 메서드가 됩니다. 따라서 정의할 때 @classmethod로 장식할 필요가 없습니다.

#### 3.3.5.1. The purpose of __class_getitem__

#### 3.3.5.1. __class_getitem__의 목적

The purpose of __class_getitem__() is to allow runtime parameterization of standard-library generic classes in order to more easily apply type hints to these classes.

__class_getitem__()의 목적은 표준 라이브러리 제네릭 클래스의 런타임 매개변수화를 허용하여 이러한 클래스에 타입 힌트를 더 쉽게 적용하기 위한 것입니다.

To implement custom generic classes that can be parameterized at runtime and understood by static type-checkers, users should either inherit from a standard library class that already implements __class_getitem__(), or inherit from typing.Generic, which has its own implementation of __class_getitem__().

런타임에 매개변수화될 수 있고 정적 타입 검사기가 이해할 수 있는 사용자 정의 제네릭 클래스를 구현하려면, 사용자는 이미 __class_getitem__()을 구현하는 표준 라이브러리 클래스에서 상속받거나, 자체 __class_getitem__() 구현을 가진 typing.Generic에서 상속받아야 합니다.

Custom implementations of __class_getitem__() on classes defined outside of the standard library may not be understood by third-party type-checkers such as mypy. Using __class_getitem__() on any class for purposes other than type hinting is discouraged.

표준 라이브러리 외부에 정의된 클래스에서 __class_getitem__()의 사용자 정의 구현은 mypy와 같은 서드파티 타입 검사기에서 이해되지 않을 수 있습니다. 타입 힌팅 이외의 목적으로 어떤 클래스에서든 __class_getitem__()을 사용하는 것은 권장되지 않습니다.

#### 3.3.5.2. __class_getitem__ versus __getitem__

#### 3.3.5.2. __class_getitem__과 __getitem__ 비교

Usually, the subscription of an object using square brackets will call the __getitem__() instance method defined on the object's class. However, if the object being subscribed is itself a class, the class method __class_getitem__() may be called instead. __class_getitem__() should return a GenericAlias object if it is properly defined.

일반적으로, 대괄호를 사용한 객체의 서브스크립션은 해당 객체의 클래스에 정의된 __getitem__() 인스턴스 메서드를 호출합니다. 그러나 서브스크립션되는 객체 자체가 클래스인 경우, 대신 클래스 메서드 __class_getitem__()이 호출될 수 있습니다. __class_getitem__()은 적절하게 정의된 경우 GenericAlias 객체를 반환해야 합니다.

Presented with the expression obj[x], the Python interpreter follows something like the following process to decide whether __getitem__() or __class_getitem__() should be called:

obj[x] 표현식이 주어지면, 파이썬 인터프리터는 __getitem__() 또는 __class_getitem__() 중 어떤 것이 호출되어야 하는지 결정하기 위해 다음과 같은 과정을 따릅니다:

```python
from inspect import isclass

def subscribe(obj, x):
    """Return the result of the expression 'obj[x]'"""

    class_of_obj = type(obj)

    # If the class of obj defines __getitem__,
    # call class_of_obj.__getitem__(obj, x)
    if hasattr(class_of_obj, '__getitem__'):
        return class_of_obj.__getitem__(obj, x)

    # Else, if obj is a class and defines __class_getitem__,
    # call obj.__class_getitem__(x)
    elif isclass(obj) and hasattr(obj, '__class_getitem__'):
        return obj.__class_getitem__(x)

    # Else, raise an exception
    else:
        raise TypeError(
            f"'{class_of_obj.__name__}' object is not subscriptable"
        )
```

In Python, all classes are themselves instances of other classes. The class of a class is known as that class's metaclass, and most classes have the type class as their metaclass. type does not define __getitem__(), meaning that expressions such as list[int], dict[str, float] and tuple[str, bytes] all result in __class_getitem__() being called:

파이썬에서는 모든 클래스가 자체적으로 다른 클래스의 인스턴스입니다. 클래스의 클래스는 해당 클래스의 메타클래스로 알려져 있으며, 대부분의 클래스는 type 클래스를 메타클래스로 가지고 있습니다. type은 __getitem__()을 정의하지 않으므로, list[int], dict[str, float], tuple[str, bytes]와 같은 표현식은 모두 __class_getitem__()이 호출되는 결과를 가져옵니다:

```python
>>>
# list has class "type" as its metaclass, like most classes:
type(list)
<class 'type'>
type(dict) == type(list) == type(tuple) == type(str) == type(bytes)
True
# "list[int]" calls "list.__class_getitem__(int)"
list[int]
list[int]
# list.__class_getitem__ returns a GenericAlias object:
type(list[int])
<class 'types.GenericAlias'>
```

However, if a class has a custom metaclass that defines __getitem__(), subscribing the class may result in different behaviour. An example of this can be found in the enum module:

그러나 클래스가 __getitem__()을 정의하는 사용자 정의 메타클래스를 가지고 있다면, 클래스를 서브스크립션하면 다른 동작이 발생할 수 있습니다. 이에 대한 예는 enum 모듈에서 찾을 수 있습니다:

```python
>>>
from enum import Enum
class Menu(Enum):
    """A breakfast menu"""
    SPAM = 'spam'
    BACON = 'bacon'

# Enum classes have a custom metaclass:
type(Menu)
<class 'enum.EnumMeta'>
# EnumMeta defines __getitem__,
# so __class_getitem__ is not called,
# and the result is not a GenericAlias object:
Menu['SPAM']
<Menu.SPAM: 'spam'>
type(Menu['SPAM'])
<enum 'Menu'>
```

See also
PEP 560 - Core Support for typing module and generic types
Introducing __class_getitem__(), and outlining when a subscription results in __class_getitem__() being called instead of __getitem__()

참고
PEP 560 - typing 모듈 및 제네릭 타입에 대한 핵심 지원
__class_getitem__()을 소개하고, 언제 서브스크립션이 __getitem__() 대신 __class_getitem__()이 호출되는 결과를 가져오는지 설명

### 3.3.6. Emulating callable objects

### 3.3.6. 호출 가능한 객체 에뮬레이션

object.__call__(self[, args...])
Called when the instance is "called" as a function; if this method is defined, x(arg1, arg2, ...) roughly translates to type(x).__call__(x, arg1, ...). The object class itself does not provide this method.

object.__call__(self[, args...])
인스턴스가 함수로 "호출"될 때 호출됩니다. 이 메서드가 정의된 경우, x(arg1, arg2, ...)는 대략 type(x).__call__(x, arg1, ...)로 변환됩니다. object 클래스 자체는 이 메서드를 제공하지 않습니다.

### 3.3.7. Emulating container types

### 3.3.7. 컨테이너 타입 에뮬레이션

The following methods can be defined to implement container objects. None of them are provided by the object class itself. Containers usually are sequences (such as lists or tuples) or mappings (like dictionaries), but can represent other containers as well. The first set of methods is used either to emulate a sequence or to emulate a mapping; the difference is that for a sequence, the allowable keys should be the integers k for which 0 <= k < N where N is the length of the sequence, or slice objects, which define a range of items. It is also recommended that mappings provide the methods keys(), values(), items(), get(), clear(), setdefault(), pop(), popitem(), copy(), and update() behaving similar to those for Python's standard dictionary objects. The collections.abc module provides a MutableMapping abstract base class to help create those methods from a base set of __getitem__(), __setitem__(), __delitem__(), and keys(). Mutable sequences should provide methods append(), count(), index(), extend(), insert(), pop(), remove(), reverse() and sort(), like Python standard list objects. Finally, sequence types should implement addition (meaning concatenation) and multiplication (meaning repetition) by defining the methods __add__(), __radd__(), __iadd__(), __mul__(), __rmul__() and __imul__() described below; they should not define other numerical operators. It is recommended that both mappings and sequences implement the __contains__() method to allow efficient use of the in operator; for mappings, in should search the mapping's keys; for sequences, it should search through the values. It is further recommended that both mappings and sequences implement the __iter__() method to allow efficient iteration through the container; for mappings, __iter__() should iterate through the object's keys; for sequences, it should iterate through the values.

다음 메서드들은 컨테이너 객체를 구현하기 위해 정의될 수 있습니다. 이 중 어느 것도 object 클래스 자체에서 제공되지 않습니다. 컨테이너는 일반적으로 시퀀스(리스트나 튜플과 같은) 또는 매핑(딕셔너리와 같은)이지만, 다른 컨테이너도 표현할 수 있습니다. 첫 번째 메서드 집합은 시퀀스를 에뮬레이션하거나 매핑을 에뮬레이션하는 데 사용됩니다. 차이점은 시퀀스의 경우, 허용되는 키는 0 <= k < N인 정수 k여야 한다는 것입니다(여기서 N은 시퀀스의 길이). 또는 항목 범위를 정의하는 슬라이스 객체도 가능합니다. 또한 매핑은 Python의 표준 딕셔너리 객체와 유사하게 동작하는 keys(), values(), items(), get(), clear(), setdefault(), pop(), popitem(), copy(), update() 메서드를 제공하는 것이 권장됩니다. collections.abc 모듈은 __getitem__(), __setitem__(), __delitem__(), keys()의 기본 집합에서 이러한 메서드를 생성하는 데 도움이 되는 MutableMapping 추상 기본 클래스를 제공합니다. 가변 시퀀스는 Python 표준 리스트 객체처럼 append(), count(), index(), extend(), insert(), pop(), remove(), reverse(), sort() 메서드를 제공해야 합니다. 마지막으로, 시퀀스 타입은 아래에 설명된 __add__(), __radd__(), __iadd__(), __mul__(), __rmul__(), __imul__() 메서드를 정의하여 더하기(연결을 의미)와 곱하기(반복을 의미)를 구현해야 합니다. 다른 숫자 연산자는 정의하지 않아야 합니다. 매핑과 시퀀스 모두 in 연산자의 효율적인 사용을 위해 __contains__() 메서드를 구현하는 것이 권장됩니다. 매핑의 경우, in은 매핑의 키를 검색해야 하고, 시퀀스의 경우, 값을 검색해야 합니다. 또한 매핑과 시퀀스 모두 컨테이너를 효율적으로 반복할 수 있도록 __iter__() 메서드를 구현하는 것이 권장됩니다. 매핑의 경우 __iter__()는 객체의 키를 반복해야 하고, 시퀀스의 경우 값을 반복해야 합니다.

object.__len__(self)
Called to implement the built-in function len(). Should return the length of the object, an integer >= 0. Also, an object that doesn't define a __bool__() method and whose __len__() method returns zero is considered to be false in a Boolean context.

object.__len__(self)
내장 함수 len()을 구현하기 위해 호출됩니다. 객체의 길이, 즉 0보다 크거나 같은 정수를 반환해야 합니다. 또한, __bool__() 메서드를 정의하지 않고 __len__() 메서드가 0을 반환하는 객체는 불리언 컨텍스트에서 거짓으로 간주됩니다.

CPython implementation detail: In CPython, the length is required to be at most sys.maxsize. If the length is larger than sys.maxsize some features (such as len()) may raise OverflowError. To prevent raising OverflowError by truth value testing, an object must define a __bool__() method.

CPython 구현 세부 사항: CPython에서, 길이는 최대 sys.maxsize여야 합니다. 길이가 sys.maxsize보다 큰 경우 일부 기능(예: len())은 OverflowError를 발생시킬 수 있습니다. 진리값 테스트로 인한 OverflowError 발생을 방지하려면, 객체는 __bool__() 메서드를 정의해야 합니다.

object.__length_hint__(self)
Called to implement operator.length_hint(). Should return an estimated length for the object (which may be greater or less than the actual length). The length must be an integer >= 0. The return value may also be NotImplemented, which is treated the same as if the __length_hint__ method didn't exist at all. This method is purely an optimization and is never required for correctness.

object.__length_hint__(self)
operator.length_hint()을 구현하기 위해 호출됩니다. 객체의 추정 길이(실제 길이보다 크거나 작을 수 있음)를 반환해야 합니다. 길이는 0보다 크거나 같은 정수여야 합니다. 반환값은 NotImplemented일 수도 있으며, 이는 __length_hint__ 메서드가 전혀 존재하지 않는 것과 같이 취급됩니다. 이 메서드는 순전히 최적화를 위한 것이며 정확성을 위해 필요한 것은 아닙니다.

Added in version 3.4.

버전 3.4에서 추가됨.

Note Slicing is done exclusively with the following three methods. A call like
a[1:2] = b
is translated to

a[slice(1, 2, None)] = b
and so forth. Missing slice items are always filled in with None.

참고 슬라이싱은 다음 세 가지 메서드로만 수행됩니다. 다음과 같은 호출은
a[1:2] = b
다음과 같이 번역됩니다.

a[slice(1, 2, None)] = b
등. 누락된 슬라이스 항목은 항상 None으로 채워집니다.

object.__getitem__(self, key)
Called to implement evaluation of self[key]. For sequence types, the accepted keys should be integers. Optionally, they may support slice objects as well. Negative index support is also optional. If key is of an inappropriate type, TypeError may be raised; if key is a value outside the set of indexes for the sequence (after any special interpretation of negative values), IndexError should be raised. For mapping types, if key is missing (not in the container), KeyError should be raised.

object.__getitem__(self, key)
self[key]의 평가를 구현하기 위해 호출됩니다. 시퀀스 타입의 경우, 허용되는 키는 정수여야 합니다. 선택적으로, 슬라이스 객체도 지원할 수 있습니다. 음수 인덱스 지원도 선택 사항입니다. key가 부적절한 타입인 경우 TypeError가 발생할 수 있습니다. key가 시퀀스의 인덱스 집합을 벗어난 값인 경우(음수 값의 특별한 해석 후) IndexError가 발생해야 합니다. 매핑 타입의 경우, key가 없다면(컨테이너에 없음) KeyError가 발생해야 합니다.

Note for loops expect that an IndexError will be raised for illegal indexes to allow proper detection of the end of the sequence.

참고 for 루프는 시퀀스의 끝을 적절히 감지할 수 있도록 잘못된 인덱스에 대해 IndexError가 발생할 것으로 예상합니다.

Note When subscripting a class, the special class method __class_getitem__() may be called instead of __getitem__(). See __class_getitem__ versus __getitem__ for more details.

참고 클래스에 첨자를 사용할 때, __getitem__() 대신 특수 클래스 메서드 __class_getitem__()이 호출될 수 있습니다. 자세한 내용은 __class_getitem__과 __getitem__ 비교를 참조하세요.

object.__setitem__(self, key, value)
Called to implement assignment to self[key]. Same note as for __getitem__(). This should only be implemented for mappings if the objects support changes to the values for keys, or if new keys can be added, or for sequences if elements can be replaced. The same exceptions should be raised for improper key values as for the __getitem__() method.

object.__setitem__(self, key, value)
self[key]에 할당을 구현하기 위해 호출됩니다. __getitem__()과 동일한 참고 사항이 적용됩니다. 이는 객체가 키에 대한 값 변경을 지원하거나, 새 키를 추가할 수 있거나, 시퀀스의 경우 요소를 대체할 수 있는 경우에만 매핑에 대해 구현되어야 합니다. 부적절한 키 값에 대해 __getitem__() 메서드와 동일한 예외가 발생해야 합니다.

object.__delitem__(self, key)
Called to implement deletion of self[key]. Same note as for __getitem__(). This should only be implemented for mappings if the objects support removal of keys, or for sequences if elements can be removed from the sequence. The same exceptions should be raised for improper key values as for the __getitem__() method.

object.__delitem__(self, key)
self[key]의 삭제를 구현하기 위해 호출됩니다. __getitem__()과 동일한 참고 사항이 적용됩니다. 이는 객체가 키 제거를 지원하거나 시퀀스에서 요소를 제거할 수 있는 경우에만 매핑이나 시퀀스에 대해 구현되어야 합니다. 부적절한 키 값에 대해 __getitem__() 메서드와 동일한 예외가 발생해야 합니다.

object.__missing__(self, key)
Called by dict.__getitem__() to implement self[key] for dict subclasses when key is not in the dictionary.

object.__missing__(self, key)
key가 딕셔너리에 없을 때 dict 하위 클래스에 대해 self[key]를 구현하기 위해 dict.__getitem__()에 의해 호출됩니다.

object.__iter__(self)
This method is called when an iterator is required for a container. This method should return a new iterator object that can iterate over all the objects in the container. For mappings, it should iterate over the keys of the container.

object.__iter__(self)
컨테이너에 이터레이터가 필요할 때 이 메서드가 호출됩니다. 이 메서드는 컨테이너의 모든 객체를 반복할 수 있는 새 이터레이터 객체를 반환해야 합니다. 매핑의 경우, 컨테이너의 키를 반복해야 합니다.

object.__reversed__(self)
Called (if present) by the reversed() built-in to implement reverse iteration. It should return a new iterator object that iterates over all the objects in the container in reverse order.

object.__reversed__(self)
역방향 반복을 구현하기 위해 내장 함수 reversed()에 의해 호출됩니다(존재하는 경우). 컨테이너의 모든 객체를 역순으로 반복하는 새 이터레이터 객체를 반환해야 합니다.

If the __reversed__() method is not provided, the reversed() built-in will fall back to using the sequence protocol (__len__() and __getitem__()). Objects that support the sequence protocol should only provide __reversed__() if they can provide an implementation that is more efficient than the one provided by reversed().

__reversed__() 메서드가 제공되지 않으면, 내장 함수 reversed()는 시퀀스 프로토콜(__len__() 및 __getitem__())을 사용하는 것으로 대체됩니다. 시퀀스 프로토콜을 지원하는 객체는 reversed()에서 제공하는 것보다 더 효율적인 구현을 제공할 수 있는 경우에만 __reversed__()를 제공해야 합니다.

The membership test operators (in and not in) are normally implemented as an iteration through a container. However, container objects can supply the following special method with a more efficient implementation, which also does not require the object be iterable.

멤버십 테스트 연산자(in 및 not in)는 일반적으로 컨테이너를 통한 반복으로 구현됩니다. 그러나 컨테이너 객체는 더 효율적인 구현을 가진 다음 특수 메서드를 제공할 수 있으며, 이는 객체가 반복 가능할 필요도 없습니다.

object.__contains__(self, item)
Called to implement membership test operators. Should return true if item is in self, false otherwise. For mapping objects, this should consider the keys of the mapping rather than the values or the key-item pairs.

object.__contains__(self, item)
멤버십 테스트 연산자를 구현하기 위해 호출됩니다. item이 self에 있으면 true를, 그렇지 않으면 false를 반환해야 합니다. 매핑 객체의 경우, 값이나 키-항목 쌍이 아닌 매핑의 키를 고려해야 합니다.

For objects that don't define __contains__(), the membership test first tries iteration via __iter__(), then the old sequence iteration protocol via __getitem__(), see this section in the language reference.

__contains__()를 정의하지 않은 객체의 경우, 멤버십 테스트는 먼저 __iter__()를 통한 반복을 시도한 다음, __getitem__()을 통한 이전 시퀀스 반복 프로토콜을 시도합니다. 언어 참조의 이 섹션을 참조하세요.

### 3.3.8. Emulating numeric types

### 3.3.8. 숫자 타입 에뮬레이션

The following methods can be defined to emulate numeric objects. Methods corresponding to operations that are not supported by the particular kind of number implemented (e.g., bitwise operations for non-integral numbers) should be left undefined.

다음 메서드는 숫자 객체를 에뮬레이션하기 위해 정의할 수 있습니다. 구현된 특정 종류의 숫자에서 지원하지 않는 연산에 해당하는 메서드(예: 비정수 숫자에 대한 비트 연산)는 정의되지 않은 상태로 두어야 합니다.

object.__add__(self, other)
object.__sub__(self, other)
object.__mul__(self, other)
object.__matmul__(self, other)
object.__truediv__(self, other)
object.__floordiv__(self, other)
object.__mod__(self, other)
object.__divmod__(self, other)
object.__pow__(self, other[, modulo])
object.__lshift__(self, other)
object.__rshift__(self, other)
object.__and__(self, other)
object.__xor__(self, other)
object.__or__(self, other)
These methods are called to implement the binary arithmetic operations (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |). For instance, to evaluate the expression x + y, where x is an instance of a class that has an __add__() method, type(x).__add__(x, y) is called. The __divmod__() method should be the equivalent to using __floordiv__() and __mod__(); it should not be related to __truediv__(). Note that __pow__() should be defined to accept an optional third argument if the ternary version of the built-in pow() function is to be supported.

이러한 메서드는 이항 산술 연산(+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |)을 구현하기 위해 호출됩니다. 예를 들어, x + y 표현식을 평가하기 위해, x가 __add__() 메서드를 가진 클래스의 인스턴스인 경우 type(x).__add__(x, y)가 호출됩니다. __divmod__() 메서드는 __floordiv__()와 __mod__()를 사용하는 것과 동등해야 합니다. __truediv__()와 관련이 없어야 합니다. 내장 함수 pow()의 삼항 버전을 지원하려면 __pow__()가 선택적 세 번째 인수를 받도록 정의되어야 합니다.

If one of those methods does not support the operation with the supplied arguments, it should return NotImplemented.

이러한 메서드 중 하나가 제공된 인수로 연산을 지원하지 않는 경우, NotImplemented를 반환해야 합니다.

object.__radd__(self, other)
object.__rsub__(self, other)
object.__rmul__(self, other)
object.__rmatmul__(self, other)
object.__rtruediv__(self, other)
object.__rfloordiv__(self, other)
object.__rmod__(self, other)
object.__rdivmod__(self, other)
object.__rpow__(self, other[, modulo])
object.__rlshift__(self, other)
object.__rrshift__(self, other)
object.__rand__(self, other)
object.__rxor__(self, other)
object.__ror__(self, other)
These methods are called to implement the binary arithmetic operations (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |) with reflected (swapped) operands. These functions are only called if the left operand does not support the corresponding operation [3] and the operands are of different types. [4] For instance, to evaluate the expression x - y, where y is an instance of a class that has an __rsub__() method, type(y).__rsub__(y, x) is called if type(x).__sub__(x, y) returns NotImplemented.

이러한 메서드는 반사된(바뀐) 피연산자와 함께 이항 산술 연산(+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |)을 구현하기 위해 호출됩니다. 이 함수들은 왼쪽 피연산자가 해당 연산을 지원하지 않고[3] 피연산자가 다른 타입인 경우에만 호출됩니다[4]. 예를 들어, x - y 표현식을 평가하기 위해, y가 __rsub__() 메서드를 가진 클래스의 인스턴스인 경우, type(x).__sub__(x, y)가 NotImplemented를 반환하면 type(y).__rsub__(y, x)가 호출됩니다.

Note that ternary pow() will not try calling __rpow__() (the coercion rules would become too complicated).

삼항 pow()는 __rpow__()를 호출하지 않는다는 점에 유의하세요(강제 변환 규칙이 너무 복잡해질 수 있음).

Note If the right operand's type is a subclass of the left operand's type and that subclass provides a different implementation of the reflected method for the operation, this method will be called before the left operand's non-reflected method. This behavior allows subclasses to override their ancestors' operations.

참고 오른쪽 피연산자의 타입이 왼쪽 피연산자 타입의 하위 클래스이고 그 하위 클래스가 해당 연산에 대해 반사된 메서드의 다른 구현을 제공하는 경우, 이 메서드는 왼쪽 피연산자의 비반사 메서드보다 먼저 호출됩니다. 이 동작은 하위 클래스가 조상의 연산을 재정의할 수 있게 합니다.

object.__iadd__(self, other)
object.__isub__(self, other)
object.__imul__(self, other)
object.__imatmul__(self, other)
object.__itruediv__(self, other)
object.__ifloordiv__(self, other)
object.__imod__(self, other)
object.__ipow__(self, other[, modulo])
object.__ilshift__(self, other)
object.__irshift__(self, other)
object.__iand__(self, other)
object.__ixor__(self, other)
object.__ior__(self, other)
These methods are called to implement the augmented arithmetic assignments (+=, -=, *=, @=, /=, //=, %=, **=, <<=, >>=, &=, ^=, |=). These methods should attempt to do the operation in-place (modifying self) and return the result (which could be, but does not have to be, self). If a specific method is not defined, or if that method returns NotImplemented, the augmented assignment falls back to the normal methods. For instance, if x is an instance of a class with an __iadd__() method, x += y is equivalent to x = x.__iadd__(y) . If __iadd__() does not exist, or if x.__iadd__(y) returns NotImplemented, x.__add__(y) and y.__radd__(x) are considered, as with the evaluation of x + y. In certain situations, augmented assignment can result in unexpected errors (see Why does a_tuple[i] += ['item'] raise an exception when the addition works?), but this behavior is in fact part of the data model.

이러한 메서드는 확장 산술 할당(+=, -=, *=, @=, /=, //=, %=, **=, <<=, >>=, &=, ^=, |=)을 구현하기 위해 호출됩니다. 이 메서드들은 연산을 제자리에서 수행하고(self를 수정) 결과를 반환해야 합니다(self일 수도 있고 아닐 수도 있음). 특정 메서드가 정의되지 않았거나 해당 메서드가 NotImplemented를 반환하면, 확장 할당은 일반 메서드로 대체됩니다. 예를 들어, x가 __iadd__() 메서드를 가진 클래스의 인스턴스인 경우, x += y는 x = x.__iadd__(y)와 동등합니다. __iadd__()가 존재하지 않거나 x.__iadd__(y)가 NotImplemented를 반환하면, x.__add__(y)와 y.__radd__(x)가 고려됩니다. x + y의 평가와 마찬가지로. 특정 상황에서, 확장 할당은 예상치 못한 오류를 발생시킬 수 있지만(a_tuple[i] += ['item']이 덧셈은 작동하는데 예외를 발생시키는 이유는 무엇인가?를 참조), 이 동작은 실제로 데이터 모델의 일부입니다.

object.__neg__(self)
object.__pos__(self)
object.__abs__(self)
object.__invert__(self)
Called to implement the unary arithmetic operations (-, +, abs() and ~).

단항 산술 연산(-, +, abs() 및 ~)을 구현하기 위해 호출됩니다.

object.__complex__(self)
object.__int__(self)
object.__float__(self)
Called to implement the built-in functions complex(), int() and float(). Should return a value of the appropriate type.

내장 함수 complex(), int() 및 float()을 구현하기 위해 호출됩니다. 적절한 타입의 값을 반환해야 합니다.

object.__index__(self)
Called to implement operator.index(), and whenever Python needs to losslessly convert the numeric object to an integer object (such as in slicing, or in the built-in bin(), hex() and oct() functions). Presence of this method indicates that the numeric object is an integer type. Must return an integer.

operator.index()를 구현하기 위해 호출되며, 파이썬이 숫자 객체를 정수 객체로 무손실 변환해야 할 때마다(슬라이스나 내장 함수 bin(), hex(), oct()에서와 같이) 호출됩니다. 이 메서드의 존재는 숫자 객체가 정수 타입임을 나타냅니다. 정수를 반환해야 합니다.

If __int__(), __float__() and __complex__() are not defined then corresponding built-in functions int(), float() and complex() fall back to __index__().

__int__(), __float__() 및 __complex__()가 정의되지 않은 경우, 해당 내장 함수 int(), float() 및 complex()는 __index__()로 대체됩니다.

object.__round__(self[, ndigits])
object.__trunc__(self)
object.__floor__(self)
object.__ceil__(self)
Called to implement the built-in function round() and math functions trunc(), floor() and ceil(). Unless ndigits is passed to __round__() all these methods should return the value of the object truncated to an Integral (typically an int).

내장 함수 round()와 수학 함수 trunc(), floor() 및 ceil()을 구현하기 위해 호출됩니다. __round__()에 ndigits가 전달되지 않는 한, 이 메서드들은 Integral(일반적으로 int)로 절삭된 객체의 값을 반환해야 합니다.

The built-in function int() falls back to __trunc__() if neither __int__() nor __index__() is defined.

내장 함수 int()는 __int__()와 __index__() 모두 정의되지 않은 경우 __trunc__()로 대체됩니다.

Changed in version 3.11: The delegation of int() to __trunc__() is deprecated.

버전 3.11에서 변경됨: int()의 __trunc__()로의 위임은 더 이상 사용되지 않습니다.

### 3.3.9. With Statement Context Managers

### 3.3.9. With 문 컨텍스트 관리자

A context manager is an object that defines the runtime context to be established when executing a with statement. The context manager handles the entry into, and the exit from, the desired runtime context for the execution of the block of code. Context managers are normally invoked using the with statement (described in section The with statement), but can also be used by directly invoking their methods.

컨텍스트 관리자는 with 문을 실행할 때 설정될 런타임 컨텍스트를 정의하는 객체입니다. 컨텍스트 관리자는 코드 블록의 실행을 위해 원하는 런타임 컨텍스트로의 진입과 종료를 처리합니다. 컨텍스트 관리자는 일반적으로 with 문(with 문 섹션에서 설명)을 사용하여 호출되지만, 메서드를 직접 호출하여 사용할 수도 있습니다.

Typical uses of context managers include saving and restoring various kinds of global state, locking and unlocking resources, closing opened files, etc.

컨텍스트 관리자의 일반적인 용도에는 다양한 종류의 전역 상태 저장 및 복원, 자원 잠금 및 잠금 해제, 열린 파일 닫기 등이 있습니다.

For more information on context managers, see Context Manager Types. The object class itself does not provide the context manager methods.

컨텍스트 관리자에 대한 자세한 정보는 컨텍스트 관리자 타입을 참조하세요. object 클래스 자체는 컨텍스트 관리자 메서드를 제공하지 않습니다.

object.__enter__(self)
Enter the runtime context related to this object. The with statement will bind this method's return value to the target(s) specified in the as clause of the statement, if any.

object.__enter__(self)
이 객체와 관련된 런타임 컨텍스트에 진입합니다. with 문은 이 메서드의 반환 값을 문의 as 절에 지정된 대상(있는 경우)에 바인딩합니다.

object.__exit__(self, exc_type, exc_value, traceback)
Exit the runtime context related to this object. The parameters describe the exception that caused the context to be exited. If the context was exited without an exception, all three arguments will be None.

object.__exit__(self, exc_type, exc_value, traceback)
이 객체와 관련된 런타임 컨텍스트를 종료합니다. 매개변수는 컨텍스트가 종료되게 한 예외를 설명합니다. 컨텍스트가 예외 없이 종료된 경우, 세 인수 모두 None이 됩니다.

If an exception is supplied, and the method wishes to suppress the exception (i.e., prevent it from being propagated), it should return a true value. Otherwise, the exception will be processed normally upon exit from this method.

예외가 제공되고 메서드가 예외를 억제하려는 경우(즉, 전파되지 않도록 방지), true 값을 반환해야 합니다. 그렇지 않으면, 이 메서드에서 나갈 때 예외가 정상적으로 처리됩니다.

Note that __exit__() methods should not reraise the passed-in exception; this is the caller's responsibility.

__exit__() 메서드가 전달된 예외를 다시 발생시켜서는 안 된다는 점에 유의하세요. 이는 호출자의 책임입니다.

See also
PEP 343 - The "with" statement
The specification, background, and examples for the Python with statement.

참고
PEP 343 - "with" 문
Python with 문의 명세, 배경 및 예제입니다.
