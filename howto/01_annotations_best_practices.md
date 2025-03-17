# Python Annotations Best Practices (Python 주석 모범 사례)

## Abstract

1. This document is designed to encapsulate the best practices for working with annotations dicts. If you write Python code that examines `__annotations__` on Python objects, we encourage you to follow the guidelines described below.

이 문서는 주석(annotations) 딕셔너리로 작업하는 모범 사례를 포함하기 위해 설계되었습니다. Python 객체의 `__annotations__`를 검사하는 Python 코드를 작성하는 경우, 아래에 설명된 가이드라인을 따르는 것이 좋습니다.

2. The document is organized into four sections: best practices for accessing the annotations of an object in Python versions 3.10 and newer, best practices for accessing the annotations of an object in Python versions 3.9 and older, other best practices for `__annotations__` that apply to any Python version, and quirks of `__annotations__`.

이 문서는 네 섹션으로 구성되어 있습니다: Python 버전 3.10 이상에서 객체의 주석에 접근하기 위한 모범 사례, Python 버전 3.9 이하에서 객체의 주석에 접근하기 위한 모범 사례, 모든 Python 버전에 적용되는 `__annotations__`에 대한 기타 모범 사례, 그리고 `__annotations__`의 특이점입니다.

3. Note that this document is specifically about working with `__annotations__`, not uses for annotations. If you're looking for information on how to use "type hints" in your code, please see the typing module.

이 문서는 특별히 `__annotations__`로 작업하는 것에 관한 것이며, 주석의 용도에 관한 것이 아닙니다. 코드에서 "타입 힌트"를 사용하는 방법에 대한 정보를 찾고 있다면, typing 모듈을 참조하십시오.

## Accessing The Annotations Dict Of An Object In Python 3.10 And Newer

## Python 3.10 이상에서 객체의 주석 딕셔너리 접근하기

4. Python 3.10 adds a new function to the standard library: `inspect.get_annotations()`. In Python versions 3.10 and newer, calling this function is the best practice for accessing the annotations dict of any object that supports annotations. This function can also "un-stringize" stringized annotations for you.

Python 3.10은 표준 라이브러리에 새로운 함수를 추가했습니다: `inspect.get_annotations()`. Python 버전 3.10 이상에서는 이 함수를 호출하는 것이 주석을 지원하는 모든 객체의 주석 딕셔너리에 접근하기 위한 모범 사례입니다. 이 함수는 문자열화된 주석을 "문자열 해제"할 수도 있습니다.

5. If for some reason `inspect.get_annotations()` isn't viable for your use case, you may access the `__annotations__` data member manually. Best practice for this changed in Python 3.10 as well: as of Python 3.10, `o.__annotations__` is guaranteed to always work on Python functions, classes, and modules. If you're certain the object you're examining is one of these three specific objects, you may simply use `o.__annotations__` to get at the object's annotations dict.

어떤 이유로든 `inspect.get_annotations()`가 사용 사례에 적합하지 않은 경우, `__annotations__` 데이터 멤버에 수동으로 접근할 수 있습니다. 이에 대한 모범 사례도 Python 3.10에서 변경되었습니다: Python 3.10부터는 `o.__annotations__`가 Python 함수, 클래스 및 모듈에서 항상 작동하도록 보장됩니다. 검사 중인 객체가 이 세 가지 특정 객체 중 하나라고 확신하는 경우, 단순히 `o.__annotations__`를 사용하여 객체의 주석 딕셔너리에 접근할 수 있습니다.

6. However, other types of callables–for example, callables created by `functools.partial()`–may not have an `__annotations__` attribute defined. When accessing the `__annotations__` of a possibly unknown object, best practice in Python versions 3.10 and newer is to call `getattr()` with three arguments, for example `getattr(o, '__annotations__', None)`.

그러나 다른 유형의 호출 가능한 객체(예: `functools.partial()`로 생성된 호출 가능한 객체)는 `__annotations__` 속성이 정의되어 있지 않을 수 있습니다. 알 수 없는 객체의 `__annotations__`에 접근할 때, Python 버전 3.10 이상에서의 모범 사례는 세 개의 인수를 사용하여 `getattr()`를 호출하는 것입니다. 예: `getattr(o, '__annotations__', None)`.

7. Before Python 3.10, accessing `__annotations__` on a class that defines no annotations but that has a parent class with annotations would return the parent's `__annotations__`. In Python 3.10 and newer, the child class's annotations will be an empty dict instead.

Python 3.10 이전에는, 주석을 정의하지 않지만 주석이 있는 부모 클래스를 가진 클래스에서 `__annotations__`에 접근하면 부모의 `__annotations__`가 반환되었습니다. Python 3.10 이상에서는 자식 클래스의 주석이 대신 빈 딕셔너리가 됩니다.

## Accessing The Annotations Dict Of An Object In Python 3.9 And Older

## Python 3.9 이하에서 객체의 주석 딕셔너리 접근하기

8. In Python 3.9 and older, accessing the annotations dict of an object is much more complicated than in newer versions. The problem is a design flaw in these older versions of Python, specifically to do with class annotations.

Python 3.9 이하에서는 객체의 주석 딕셔너리에 접근하는 것이 최신 버전보다 훨씬 복잡합니다. 문제는 이러한 이전 버전의 Python에서의 설계 결함으로, 특히 클래스 주석과 관련이 있습니다.

9. Best practice for accessing the annotations dict of other objects–functions, other callables, and modules–is the same as best practice for 3.10, assuming you aren't calling `inspect.get_annotations()`: you should use three-argument `getattr()` to access the object's `__annotations__` attribute.

다른 객체(함수, 다른 호출 가능한 객체 및 모듈)의 주석 딕셔너리에 접근하기 위한 모범 사례는 `inspect.get_annotations()`을 호출하지 않는다고 가정할 때 3.10에 대한 모범 사례와 동일합니다: 객체의 `__annotations__` 속성에 접근하기 위해 세 인수 `getattr()`을 사용해야 합니다.

10. Unfortunately, this isn't best practice for classes. The problem is that, since `__annotations__` is optional on classes, and because classes can inherit attributes from their base classes, accessing the `__annotations__` attribute of a class may inadvertently return the annotations dict of a base class. As an example:

안타깝게도, 이는 클래스에 대한 모범 사례가 아닙니다. 문제는 클래스에서 `__annotations__`가 선택적이고, 클래스가 기본 클래스에서 속성을 상속할 수 있기 때문에, 클래스의 `__annotations__` 속성에 접근하면 실수로 기본 클래스의 주석 딕셔너리를 반환할 수 있다는 것입니다. 예를 들어:

```python
class Base:
    a: int = 3
    b: str = 'abc'

class Derived(Base):
    pass

print(Derived.__annotations__)
```

11. This will print the annotations dict from `Base`, not `Derived`.

이는 `Derived`가 아닌 `Base`의 주석 딕셔너리를 출력합니다.

12. Your code will have to have a separate code path if the object you're examining is a class (`isinstance(o, type)`). In that case, best practice relies on an implementation detail of Python 3.9 and before: if a class has annotations defined, they are stored in the class's `__dict__` dictionary. Since the class may or may not have annotations defined, best practice is to call the `get()` method on the class dict.

검사 중인 객체가 클래스(`isinstance(o, type)`)인 경우 코드는 별도의 코드 경로를 가져야 합니다. 이 경우, 모범 사례는 Python 3.9 이전의 구현 세부 사항에 의존합니다: 클래스에 주석이 정의되어 있으면, 이는 클래스의 `__dict__` 딕셔너리에 저장됩니다. 클래스에 주석이 정의되어 있을 수도 있고 없을 수도 있으므로, 모범 사례는 클래스 딕셔너리에서 `get()` 메서드를 호출하는 것입니다.

13. To put it all together, here is some sample code that safely accesses the `__annotations__` attribute on an arbitrary object in Python 3.9 and before:

모든 것을 종합하면, 다음은 Python 3.9 이전에서 임의의 객체의 `__annotations__` 속성에 안전하게 액세스하는 샘플 코드입니다:

```python
if isinstance(o, type):
    ann = o.__dict__.get('__annotations__', None)
else:
    ann = getattr(o, '__annotations__', None)
```

14. After running this code, `ann` should be either a dictionary or `None`. You're encouraged to double-check the type of `ann` using `isinstance()` before further examination.

이 코드를 실행한 후, `ann`은 딕셔너리이거나 `None`이어야 합니다. 추가 검사 전에 `isinstance()`를 사용하여 `ann`의 유형을 이중 확인하는 것이 좋습니다.

15. Note that some exotic or malformed type objects may not have a `__dict__` attribute, so for extra safety you may also wish to use `getattr()` to access `__dict__`.

일부 이색적이거나 잘못 형성된 유형 객체에는 `__dict__` 속성이 없을 수 있으므로, 추가 안전을 위해 `__dict__`에 접근하기 위해 `getattr()`를 사용하는 것이 좋습니다.

## Manually Un-Stringizing Stringized Annotations

## 문자열화된 주석 수동으로 문자열 해제하기

16. In situations where some annotations may be "stringized", and you wish to evaluate those strings to produce the Python values they represent, it really is best to call `inspect.get_annotations()` to do this work for you.

일부 주석이 "문자열화"될 수 있는 상황에서, 이러한 문자열을 평가하여 그들이 나타내는 Python 값을 생성하려는 경우, 이 작업을 대신 수행하기 위해 `inspect.get_annotations()`을 호출하는 것이 가장 좋습니다.

17. If you're using Python 3.9 or older, or if for some reason you can't use `inspect.get_annotations()`, you'll need to duplicate its logic. You're encouraged to examine the implementation of `inspect.get_annotations()` in the current Python version and follow a similar approach.

Python 3.9 이하를 사용하고 있거나, 어떤 이유로든 `inspect.get_annotations()`을 사용할 수 없는 경우, 해당 로직을 복제해야 합니다. 현재 Python 버전에서 `inspect.get_annotations()`의 구현을 검사하고 유사한 접근 방식을 따르는 것이 좋습니다.

18. In a nutshell, if you wish to evaluate a stringized annotation on an arbitrary object `o`:

간단히 말해, 임의의 객체 `o`에서 문자열화된 주석을 평가하려면:

19. If `o` is a module, use `o.__dict__` as the globals when calling `eval()`.

`o`가 모듈인 경우, `eval()`을 호출할 때 전역 변수로 `o.__dict__`를 사용합니다.

20. If `o` is a class, use `sys.modules[o.__module__].__dict__` as the globals, and `dict(vars(o))` as the locals, when calling `eval()`.

`o`가 클래스인 경우, `eval()`을 호출할 때 전역 변수로 `sys.modules[o.__module__].__dict__`를, 지역 변수로 `dict(vars(o))`를 사용합니다.

21. If `o` is a wrapped callable using `functools.update_wrapper()`, `functools.wraps()`, or `functools.partial()`, iteratively unwrap it by accessing either `o.__wrapped__` or `o.func` as appropriate, until you have found the root unwrapped function.

`o`가 `functools.update_wrapper()`, `functools.wraps()`, 또는 `functools.partial()`을 사용하는 래핑된 호출 가능한 객체인 경우, 루트 래핑되지 않은 함수를 찾을 때까지 적절하게 `o.__wrapped__` 또는 `o.func`에 접근하여 반복적으로 언래핑합니다.

22. If `o` is a callable (but not a class), use `o.__globals__` as the globals when calling `eval()`.

`o`가 호출 가능한 객체(클래스가 아닌)인 경우, `eval()`을 호출할 때 전역 변수로 `o.__globals__`를 사용합니다.

23. However, not all string values used as annotations can be successfully turned into Python values by `eval()`. String values could theoretically contain any valid string, and in practice there are valid use cases for type hints that require annotating with string values that specifically can't be evaluated. For example:

그러나, 주석으로 사용되는 모든 문자열 값이 `eval()`에 의해 성공적으로 Python 값으로 변환될 수 있는 것은 아닙니다. 문자열 값은 이론적으로 모든 유효한 문자열을 포함할 수 있으며, 실제로 특별히 평가될 수 없는 문자열 값으로 주석을 달아야 하는 타입 힌트에 대한 유효한 사용 사례가 있습니다. 예를 들어:

24. PEP 604 union types using `|`, before support for this was added to Python 3.10.

Python 3.10에 지원이 추가되기 전의 `|`를 사용하는 PEP 604 유니온 타입.

25. Definitions that aren't needed at runtime, only imported when `typing.TYPE_CHECKING` is true.

런타임에 필요하지 않고 `typing.TYPE_CHECKING`이 참일 때만 임포트되는 정의.

26. If `eval()` attempts to evaluate such values, it will fail and raise an exception. So, when designing a library API that works with annotations, it's recommended to only attempt to evaluate string values when explicitly requested to by the caller.

`eval()`이 그러한 값을 평가하려고 시도하면 실패하고 예외를 발생시킵니다. 따라서 주석으로 작업하는 라이브러리 API를 설계할 때, 호출자가 명시적으로 요청할 때만 문자열 값을 평가하려고 시도하는 것이 좋습니다.

## Best Practices For `__annotations__` In Any Python Version

## 모든 Python 버전에서 `__annotations__`에 대한 모범 사례

27. You should avoid assigning to the `__annotations__` member of objects directly. Let Python manage setting `__annotations__`.

객체의 `__annotations__` 멤버에 직접 할당하는 것을 피해야 합니다. Python이 `__annotations__`를 설정하도록 두세요.

28. If you do assign directly to the `__annotations__` member of an object, you should always set it to a dict object.

객체의 `__annotations__` 멤버에 직접 할당하는 경우, 항상 dict 객체로 설정해야 합니다.

29. If you directly access the `__annotations__` member of an object, you should ensure that it's a dictionary before attempting to examine its contents.

객체의 `__annotations__` 멤버에 직접 접근하는 경우, 내용을 검사하기 전에 그것이 딕셔너리인지 확인해야 합니다.

30. You should avoid modifying `__annotations__` dicts.

`__annotations__` 딕셔너리를 수정하는 것을 피해야 합니다.

31. You should avoid deleting the `__annotations__` attribute of an object.

객체의 `__annotations__` 속성을 삭제하는 것을 피해야 합니다.

## `__annotations__` Quirks

## `__annotations__` 특이점

32. In all versions of Python 3, function objects lazy-create an annotations dict if no annotations are defined on that object. You can delete the `__annotations__` attribute using `del fn.__annotations__`, but if you then access `fn.__annotations__` the object will create a new empty dict that it will store and return as its annotations. Deleting the annotations on a function before it has lazily created its annotations dict will throw an AttributeError; using `del fn.__annotations__` twice in a row is guaranteed to always throw an AttributeError.

Python 3의 모든 버전에서 함수 객체는 해당 객체에 주석이 정의되어 있지 않은 경우 주석 딕셔너리를 지연 생성합니다. `del fn.__annotations__`을 사용하여 `__annotations__` 속성을 삭제할 수 있지만, 그 후에 `fn.__annotations__`에 접근하면 객체는 새로운 빈 딕셔너리를 생성하여 주석으로 저장하고 반환합니다. 함수가 주석 딕셔너리를 지연 생성하기 전에 함수의 주석을 삭제하면 AttributeError가 발생합니다; 연속으로 두 번 `del fn.__annotations__`을 사용하면 항상 AttributeError가 발생합니다.

33. Everything in the above paragraph also applies to class and module objects in Python 3.10 and newer.

위 단락의 모든 내용은 Python 3.10 이상의 클래스 및 모듈 객체에도 적용됩니다.

34. In all versions of Python 3, you can set `__annotations__` on a function object to None. However, subsequently accessing the annotations on that object using `fn.__annotations__` will lazy-create an empty dictionary as per the first paragraph of this section. This is not true of modules and classes, in any Python version; those objects permit setting `__annotations__` to any Python value, and will retain whatever value is set.

Python 3의 모든 버전에서 함수 객체의 `__annotations__`를 None으로 설정할 수 있습니다. 그러나, 이후에 `fn.__annotations__`를 사용하여 해당 객체의 주석에 접근하면 이 섹션의 첫 번째 단락대로 빈 딕셔너리를 지연 생성합니다. 이는 모든 Python 버전의 모듈과 클래스에는 해당되지 않습니다; 그러한 객체는 `__annotations__`를 모든 Python 값으로 설정할 수 있으며, 설정된 어떤 값이든 유지합니다.

35. If Python stringizes your annotations for you (using `from __future__ import annotations`), and you specify a string as an annotation, the string will itself be quoted. In effect the annotation is quoted twice. For example:

Python이 (`from __future__ import annotations`를 사용하여) 주석을 문자열화하고, 문자열을 주석으로 지정하면, 문자열 자체가 인용됩니다. 사실상 주석은 두 번 인용됩니다. 예를 들어:

```python
from __future__ import annotations
def foo(a: "str"): pass

print(foo.__annotations__)
```

36. This prints `{'a': "'str'"}`. This shouldn't really be considered a "quirk"; it's mentioned here simply because it might be surprising.

이는 `{'a': "'str'"}`를 출력합니다. 이는 정말로 "특이점"으로 간주되어서는 안 됩니다; 이는 단지 놀라울 수 있기 때문에 여기에 언급됩니다.
