# Python Annotations Best Practices (Python 주석 모범 사례)

## Introduction

1. Python 3.0 introduced function annotations in PEP 3107, and Python 3.6 added variable annotations in PEP 526. While annotations can be used for any purpose, they are predominantly used for type hints as described in PEP 484.

Python 3.0은 PEP 3107에서 함수 주석을 도입했으며, Python 3.6은 PEP 526에서 변수 주석을 추가했습니다. 주석은 어떤 목적으로도 사용할 수 있지만, 주로 PEP 484에서 설명된 대로 타입 힌트에 사용됩니다.

2. This document outlines best practices for working with annotations dicts. If you write Python code that examines `__annotations__` on Python objects, you should follow these guidelines to ensure your code works correctly across different Python versions.

이 문서는 주석 딕셔너리로 작업하는 모범 사례를 설명합니다. Python 객체의 `__annotations__`를 검사하는 Python 코드를 작성하는 경우, 코드가 다양한 Python 버전에서 올바르게 작동하도록 이러한 가이드라인을 따라야 합니다.

## Accessing Annotations in Python 3.10 and Newer

3. In Python 3.10 and newer, the recommended way to access annotations is to use the `inspect.get_annotations()` function, which was specifically designed for this purpose:

Python 3.10 이상에서는 이 목적을 위해 특별히 설계된 `inspect.get_annotations()` 함수를 사용하는 것이 주석에 접근하는 권장 방법입니다:

```python
import inspect

def example(x: int, y: str) -> bool:
    return isinstance(y, str) and x > 0

# Get annotations with the recommended method
annotations = inspect.get_annotations(example)
print(annotations)  # {'x': <class 'int'>, 'y': <class 'str'>, 'return': <class 'bool'>}
```

4. The `inspect.get_annotations()` function handles many edge cases automatically, including "stringized" annotations (from using `from __future__ import annotations`).

`inspect.get_annotations()` 함수는 `from __future__ import annotations`를 사용한 "문자열화된" 주석을 포함한 많은 엣지 케이스를 자동으로 처리합니다.

5. If you cannot use `inspect.get_annotations()`, you can directly access the `__annotations__` attribute. In Python 3.10+, this attribute is guaranteed to exist on functions, classes, and modules:

`inspect.get_annotations()`를 사용할 수 없는 경우, `__annotations__` 속성에 직접 접근할 수 있습니다. Python 3.10 이상에서는 이 속성이 함수, 클래스, 모듈에 존재하는 것이 보장됩니다:

```python
# Direct access for functions, classes, and modules in Python 3.10+
func_annotations = example.__annotations__
```

6. However, when dealing with arbitrary objects that might be callables but not functions (like `functools.partial` objects), you should use `getattr` with a default value:

그러나 함수가 아닌 호출 가능한 객체(`functools.partial` 객체 같은)일 수 있는 임의의 객체를 처리할 때는 기본값과 함께 `getattr`를 사용해야 합니다:

```python
# Safe access for any object
annotations = getattr(obj, '__annotations__', None)
```

## Accessing Annotations in Python 3.9 and Older

7. In Python 3.9 and older versions, accessing annotations is more complex, especially for class objects. This is because a class without annotations might inherit the `__annotations__` attribute from its parent class:

Python 3.9 이하 버전에서는 특히 클래스 객체에 대한 주석 접근이 더 복잡합니다. 이는 주석이 없는 클래스가 부모 클래스로부터 `__annotations__` 속성을 상속받을 수 있기 때문입니다:

```python
class Base:
    a: int = 3
    b: str = 'abc'

class Derived(Base):
    pass

print(Derived.__annotations__)  # Prints Base's annotations, not Derived's
```

8. The best practice for accessing annotations in Python 3.9 and older is to use different approaches depending on the object type:

Python 3.9 이하에서 주석에 접근하는 모범 사례는 객체 유형에 따라 다른 접근 방식을 사용하는 것입니다:

```python
def get_annotations(obj):
    if isinstance(obj, type):  # If it's a class
        # Access class dict directly to avoid inheritance issues
        return obj.__dict__.get('__annotations__', {})
    else:  # For functions, modules, and other objects
        return getattr(obj, '__annotations__', {})
```

9. This approach ensures you get the annotations defined directly on the class, not inherited annotations.

이 접근 방식은 상속된 주석이 아닌, 클래스에 직접 정의된 주석을 가져오도록 보장합니다.

## Handling Stringized Annotations

10. When using `from __future__ import annotations`, annotations are stored as strings rather than evaluated expressions. To convert these strings back to their Python values, use `inspect.get_annotations(obj, eval_str=True)` in Python 3.10+:

`from __future__ import annotations`를 사용할 때, 주석은 평가된 표현식이 아닌 문자열로 저장됩니다. 이러한 문자열을 다시 Python 값으로 변환하려면 Python 3.10 이상에서 `inspect.get_annotations(obj, eval_str=True)`를 사용하세요:

```python
from __future__ import annotations
import inspect

class Example:
    x: list[int]  # Stored as the string 'list[int]'

# Get evaluated annotations
annotations = inspect.get_annotations(Example, eval_str=True)
print(annotations)  # {'x': list[int]} (evaluated to the actual type)
```

11. For Python 3.9 and older, you need to manually evaluate the strings. The evaluation context depends on the type of object:

Python 3.9 이하의 경우 문자열을 수동으로 평가해야 합니다. 평가 컨텍스트는 객체 유형에 따라 달라집니다:

```python
import sys
import types

def eval_annotations(obj, annotations):
    if not annotations:
        return annotations
    
    # Determine the appropriate globals for evaluation
    if isinstance(obj, types.ModuleType):
        globals_dict = obj.__dict__
    elif isinstance(obj, type):
        module_name = obj.__module__
        globals_dict = sys.modules[module_name].__dict__
        locals_dict = dict(vars(obj))
        return {k: eval(v, globals_dict, locals_dict) 
                if isinstance(v, str) else v 
                for k, v in annotations.items()}
    else:  # Function or other callable
        try:
            globals_dict = getattr(obj, '__globals__', {})
        except AttributeError:
            globals_dict = {}
    
    # Evaluate string annotations
    return {k: eval(v, globals_dict) 
            if isinstance(v, str) else v 
            for k, v in annotations.items()}
```

12. Note that not all string annotations can be successfully evaluated. Some annotations may use syntax from newer Python versions or types that aren't imported in the module's scope.

모든 문자열 주석이 성공적으로 평가될 수 있는 것은 아닙니다. 일부 주석은 새로운 Python 버전의 구문을 사용하거나 모듈 범위에 가져오지 않은 타입을 사용할 수 있습니다.

## Best Practices for All Python Versions

13. Avoid directly assigning to `__annotations__` on objects. Let Python manage this attribute:

객체의 `__annotations__`에 직접 할당하지 마세요. Python이 이 속성을 관리하도록 하세요:

```python
# Good - let Python handle annotations
def good(x: int): pass

# Bad - manually setting annotations
def bad(x): pass
bad.__annotations__ = {'x': int}
```

14. If you must assign to `__annotations__`, always set it to a dictionary:

`__annotations__`에 할당해야 한다면, 항상 딕셔너리로 설정하세요:

```python
obj.__annotations__ = {'param': int}  # Good
obj.__annotations__ = None  # Bad - may cause issues
```

15. When accessing `__annotations__`, always verify it's a dictionary before using it:

`__annotations__`에 접근할 때는 사용하기 전에 항상 딕셔너리인지 확인하세요:

```python
annotations = getattr(obj, '__annotations__', None)
if isinstance(annotations, dict):
    # Safe to use annotations
    pass
```

16. Avoid modifying existing annotation dictionaries. If you need a modified version, create a copy:

기존 주석 딕셔너리를 수정하지 마세요. 수정된 버전이 필요하면 복사본을 만드세요:

```python
# Good - create a copy for modifications
annotations = dict(getattr(obj, '__annotations__', {}))
annotations['new_key'] = some_type

# Bad - modifying in-place
obj.__annotations__['new_key'] = some_type
```

17. Avoid deleting the `__annotations__` attribute. This can lead to unexpected behavior:

`__annotations__` 속성을 삭제하지 마세요. 이는 예상치 못한 동작을 초래할 수 있습니다:

```python
# Bad - can cause issues
del obj.__annotations__
```

## Understanding `__annotations__` Quirks

18. Function objects lazy-create an empty annotations dict if you access `__annotations__` when no annotations were defined:

함수 객체는 주석이 정의되지 않았을 때 `__annotations__`에 접근하면 빈 주석 딕셔너리를 지연 생성합니다:

```python
def func(): pass
print(func.__annotations__)  # {} - empty dict created on first access
```

19. In Python 3.10+, this lazy-creation behavior also applies to classes and modules. Before Python 3.10, classes and modules would raise an `AttributeError` if no annotations were defined.

Python 3.10 이상에서는 이 지연 생성 동작이 클래스와 모듈에도 적용됩니다. Python 3.10 이전에는 주석이 정의되지 않은 경우 클래스와 모듈에서 `AttributeError`가 발생했습니다.

20. You can set `__annotations__` to `None` on function objects, but accessing it afterwards will create a new empty dict:

함수 객체의 `__annotations__`을 `None`으로 설정할 수 있지만, 이후에 접근하면 새로운 빈 딕셔너리가 생성됩니다:

```python
def func(): pass
func.__annotations__ = None
print(func.__annotations__)  # {} - new empty dict created
```

21. When using `from __future__ import annotations`, string annotations are quoted twice:

`from __future__ import annotations`를 사용할 때, 문자열 주석은 두 번 인용됩니다:

```python
from __future__ import annotations
def foo(a: "str"): pass

print(foo.__annotations__)  # {'a': "'str'"} - notice the double quotes
```

## Conclusion

22. Working with annotations correctly across different Python versions requires careful handling. The safest and most reliable approach in modern Python is to use the `inspect.get_annotations()` function.

다양한 Python 버전에서 주석을 올바르게 다루려면 신중한 처리가 필요합니다. 현대 Python에서 가장 안전하고 신뢰할 수 있는 접근 방식은 `inspect.get_annotations()` 함수를 사용하는 것입니다.

23. For code that needs to support older Python versions, use version-specific approaches and carefully handle the different behaviors of classes, functions, and modules when accessing and manipulating annotations.

이전 Python 버전을 지원해야 하는 코드의 경우, 버전별 접근 방식을 사용하고 주석에 접근하거나 조작할 때 클래스, 함수 및 모듈의 다른 동작을 신중하게 처리하세요.

24. By following these best practices, you can ensure your code works consistently across different Python versions and avoids common pitfalls related to annotations.

이러한 모범 사례를 따르면 코드가 다양한 Python 버전에서 일관되게 작동하고 주석과 관련된 일반적인 함정을 피할 수 있습니다.