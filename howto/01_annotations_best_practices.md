# Type Annotations Best Practices in Python

# Python에서의 타입 어노테이션 모범 사례

## Introduction

Type annotations were introduced in Python 3.5 via [PEP 484](https://www.python.org/dev/peps/pep-0484/) and have since become an essential tool for many Python developers. While Python remains a dynamically typed language, type annotations provide a way to indicate expected types, improving code readability, enabling better IDE support, and allowing static type checking tools to catch potential bugs before runtime.

This guide covers best practices for using type annotations in Python projects.

## 소개

타입 어노테이션은 [PEP 484](https://www.python.org/dev/peps/pep-0484/)를 통해 Python 3.5에 도입되었으며, 이후 많은 Python 개발자에게 필수적인 도구가 되었습니다. Python은 여전히 동적 타입 언어이지만, 타입 어노테이션은 예상되는 타입을 표시하는 방법을 제공하여 코드 가독성을 향상시키고, IDE 지원을 개선하며, 정적 타입 검사 도구가 런타임 전에 잠재적인 버그를 발견할 수 있게 합니다.

이 가이드는 Python 프로젝트에서 타입 어노테이션을 사용하는 모범 사례를 다룹니다.

## Basic Syntax

### Function Annotations

```python
def greeting(name: str) -> str:
    return f"Hello, {name}"
```

### Variable Annotations

```python
age: int = 25
names: list[str] = ["Alice", "Bob", "Charlie"]
```

### Class Annotations

```python
class Person:
    name: str
    age: int
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
```

## 기본 구문

### 함수 어노테이션

```python
def greeting(name: str) -> str:
    return f"Hello, {name}"
```

### 변수 어노테이션

```python
age: int = 25
names: list[str] = ["Alice", "Bob", "Charlie"]
```

### 클래스 어노테이션

```python
class Person:
    name: str
    age: int
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
```

## Best Practices

### 1. Start Gradually

If you're adding type annotations to an existing project, start with the most critical parts or public APIs. You don't need to annotate everything at once.

```python
# Start with clearly defined interfaces
def calculate_total(items: list[dict[str, float]]) -> float:
    return sum(item.get("price", 0) for item in items)
```

### 2. Use Type Aliases for Complex Types

```python
from typing import TypeAlias, Dict, List, Union

# Before
def process_data(data: Dict[str, Union[List[int], Dict[str, float]]]) -> None:
    pass

# After
JsonDict: TypeAlias = Dict[str, Union[List[int], Dict[str, float]]]
def process_data(data: JsonDict) -> None:
    pass
```

### 3. Take Advantage of Optional and Union

```python
from typing import Optional, Union

# Use Optional for values that could be None
def find_user(user_id: Optional[int] = None) -> Optional[dict]:
    if user_id is None:
        return None
    # Find user...

# Use Union for values that could be one of several types
def process_input(data: Union[str, bytes, list[int]]) -> None:
    # Process data...
```

### 4. Consider Using TypedDict for Dictionaries with Known Keys

```python
from typing import TypedDict

class MovieDict(TypedDict):
    title: str
    year: int
    rating: float

def print_movie(movie: MovieDict) -> None:
    print(f"{movie['title']} ({movie['year']}): {movie['rating']}/10")
```

### 5. Use Protocols for Duck Typing

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

def render(item: Drawable) -> None:
    item.draw()
```

## 모범 사례

### 1. 점진적으로 시작하기

기존 프로젝트에 타입 어노테이션을 추가하는 경우, 가장 중요한 부분이나 공개 API부터 시작하세요. 모든 것을 한 번에 어노테이션할 필요는 없습니다.

```python
# 명확하게 정의된 인터페이스부터 시작
def calculate_total(items: list[dict[str, float]]) -> float:
    return sum(item.get("price", 0) for item in items)
```

### 2. 복잡한 타입에는 타입 별칭 사용하기

```python
from typing import TypeAlias, Dict, List, Union

# 이전
def process_data(data: Dict[str, Union[List[int], Dict[str, float]]]) -> None:
    pass

# 이후
JsonDict: TypeAlias = Dict[str, Union[List[int], Dict[str, float]]]
def process_data(data: JsonDict) -> None:
    pass
```

### 3. Optional과 Union 활용하기

```python
from typing import Optional, Union

# None이 될 수 있는 값에는 Optional 사용
def find_user(user_id: Optional[int] = None) -> Optional[dict]:
    if user_id is None:
        return None
    # 사용자 찾기...

# 여러 타입 중 하나일 수 있는 값에는 Union 사용
def process_input(data: Union[str, bytes, list[int]]) -> None:
    # 데이터 처리...
```

### 4. 알려진 키가 있는 딕셔너리에는 TypedDict 사용 고려하기

```python
from typing import TypedDict

class MovieDict(TypedDict):
    title: str
    year: int
    rating: float

def print_movie(movie: MovieDict) -> None:
    print(f"{movie['title']} ({movie['year']}): {movie['rating']}/10")
```

### 5. 덕 타이핑에는 Protocol 사용하기

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

def render(item: Drawable) -> None:
    item.draw()
```

## Common Pitfalls to Avoid

### 1. Avoid Forward References Without Quotes

```python
# Problematic - Tree isn't defined yet
class Tree:
    left: Tree  # Error!
    right: Tree  # Error!

# Correct - Use string literals for forward references
class Tree:
    left: "Tree"  # Works!
    right: "Tree"  # Works!
```

### 2. Be Careful with Mutable Default Arguments

```python
# Misleading - Default value is created only once
def append_to(element: int, target: list[int] = []) -> list[int]:  # Dangerous!
    target.append(element)
    return target

# Better - Use None and create a new list each time
def append_to(element: int, target: Optional[list[int]] = None) -> list[int]:
    if target is None:
        target = []
    target.append(element)
    return target
```

### 3. Don't Mix `Any` with Other Types in Unions

```python
# Avoid this - Any makes the Union redundant
items: Union[Any, str, int] = get_items()  # Equivalent to just Any

# Unless you're using type narrowing
items: Union[Any, str, int] = get_items()
if isinstance(items, str):
    # Here items is treated as str
    print(items.upper())
```

### 4. Don't Forget Generic Types Parameters

```python
# Bad - Missing type parameter
values: list = [1, 2, 3]  # What type of list?

# Good - Specify the type parameter
values: list[int] = [1, 2, 3]  # Clearly a list of integers
```

## 피해야 할 일반적인 함정

### 1. 인용 부호 없이 순환 참조 피하기

```python
# 문제 있음 - Tree가 아직 정의되지 않음
class Tree:
    left: Tree  # 오류!
    right: Tree  # 오류!

# 올바름 - 순환 참조에는 문자열 리터럴 사용
class Tree:
    left: "Tree"  # 작동!
    right: "Tree"  # 작동!
```

### 2. 가변 기본 인수에 주의하기

```python
# 오해의 소지가 있음 - 기본값은 한 번만 생성됨
def append_to(element: int, target: list[int] = []) -> list[int]:  # 위험!
    target.append(element)
    return target

# 더 나음 - None을 사용하고 매번 새 리스트 생성
def append_to(element: int, target: Optional[list[int]] = None) -> list[int]:
    if target is None:
        target = []
    target.append(element)
    return target
```

### 3. Union에서 `Any`와 다른 타입을 혼합하지 않기

```python
# 이것은 피하세요 - Any는 Union을 무의미하게 만듦
items: Union[Any, str, int] = get_items()  # 사실상 Any와 동일

# 단, 타입 좁히기를 사용하는 경우는 제외
items: Union[Any, str, int] = get_items()
if isinstance(items, str):
    # 여기서 items는 str로 처리됨
    print(items.upper())
```

### 4. 제네릭 타입 매개변수를 잊지 않기

```python
# 나쁨 - 타입 매개변수 누락
values: list = [1, 2, 3]  # 어떤 타입의 리스트?

# 좋음 - 타입 매개변수 지정
values: list[int] = [1, 2, 3]  # 명확하게 정수 리스트
```

## Type Checking Tools

### mypy

[mypy](http://mypy-lang.org/) is the original type checker for Python and remains the most widely used.

```bash
# Install
pip install mypy

# Basic usage
mypy your_script.py
```

### pyright/Pylance

[pyright](https://github.com/microsoft/pyright) is Microsoft's type checker, also used in VS Code's Pylance extension.

```bash
# Install
pip install pyright

# Basic usage
pyright your_script.py
```

### Other Tools

- **pyre-check**: Facebook's type checker
- **pytype**: Google's type checker
- **Pyright in VS Code**: VS Code's built-in type checking with Pylance extension

## 타입 검사 도구

### mypy

[mypy](http://mypy-lang.org/)는 Python용 원조 타입 검사기이며 가장 널리 사용됩니다.

```bash
# 설치
pip install mypy

# 기본 사용법
mypy your_script.py
```

### pyright/Pylance

[pyright](https://github.com/microsoft/pyright)는 Microsoft의 타입 검사기로, VS Code의 Pylance 확장에서도 사용됩니다.

```bash
# 설치
pip install pyright

# 기본 사용법
pyright your_script.py
```

### 기타 도구

- **pyre-check**: Facebook의 타입 검사기
- **pytype**: Google의 타입 검사기
- **VS Code의 Pyright**: VS Code의 Pylance 확장을 통한 내장 타입 검사

## Advanced Examples

### Generic Functions and Classes

```python
from typing import TypeVar, Generic, Sequence

T = TypeVar('T')

def first_element(sequence: Sequence[T]) -> T:
    if not sequence:
        raise ValueError("Sequence is empty")
    return sequence[0]

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []
        
    def push(self, item: T) -> None:
        self.items.append(item)
        
    def pop(self) -> T:
        if not self.items:
            raise IndexError("Pop from empty stack")
        return self.items.pop()
```

### Type Guards and Narrowing

```python
from typing import TypeGuard, Union, List, Dict

def is_string_list(val: List[object]) -> TypeGuard[List[str]]:
    return all(isinstance(x, str) for x in val)

def process_items(items: Union[List[object], Dict[str, object]]) -> None:
    if isinstance(items, list) and is_string_list(items):
        # Now TypeGuard ensures items is List[str]
        print(", ".join(items))
    else:
        # Handle the dictionary case or non-string lists
        pass
```

## 고급 예제

### 제네릭 함수와 클래스

```python
from typing import TypeVar, Generic, Sequence

T = TypeVar('T')

def first_element(sequence: Sequence[T]) -> T:
    if not sequence:
        raise ValueError("Sequence is empty")
    return sequence[0]

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []
        
    def push(self, item: T) -> None:
        self.items.append(item)
        
    def pop(self) -> T:
        if not self.items:
            raise IndexError("Pop from empty stack")
        return self.items.pop()
```

### 타입 가드와 타입 좁히기

```python
from typing import TypeGuard, Union, List, Dict

def is_string_list(val: List[object]) -> TypeGuard[List[str]]:
    return all(isinstance(x, str) for x in val)

def process_items(items: Union[List[object], Dict[str, object]]) -> None:
    if isinstance(items, list) and is_string_list(items):
        # 이제 TypeGuard가 items가 List[str]임을 보장
        print(", ".join(items))
    else:
        # 딕셔너리 케이스나 문자열이 아닌 리스트 처리
        pass
```

## Conclusion

Type annotations in Python serve as documentation, enable better tooling support, and help catch bugs early. By following these best practices, you can get the most benefit from type annotations while avoiding common issues.

Remember that Python's type system is gradual and optional. You can add types incrementally to your codebase and decide how strict or lenient you want your type checking to be.

## 결론

Python의 타입 어노테이션은 문서화 역할을 하고, 더 나은 도구 지원을 가능하게 하며, 초기에 버그를 잡는 데 도움을 줍니다. 이러한 모범 사례를 따르면 일반적인 문제를 피하면서 타입 어노테이션의 이점을 최대한 활용할 수 있습니다.

Python의 타입 시스템은 점진적이고 선택적임을 기억하세요. 코드베이스에 점진적으로 타입을 추가할 수 있으며, 타입 검사를 얼마나 엄격하게 또는 관대하게 할지 결정할 수 있습니다.
