# Python Method Resolution Order (MRO)

# Python 메서드 해석 순서 (MRO)

## Introduction

Method Resolution Order (MRO) in Python is the order in which Python looks for methods and attributes in a hierarchy of classes. It becomes especially important when dealing with multiple inheritance. Python uses the C3 Linearization algorithm to determine this order, ensuring method resolution is consistent and predictable.

## 소개

Python의 메서드 해석 순서(MRO)는 Python이 클래스 계층 구조에서 메서드와 속성을 찾는 순서입니다. 이는 특히 다중 상속을 다룰 때 중요해집니다. Python은 C3 선형화 알고리즘을 사용하여 이 순서를 결정하고, 메서드 해석이 일관되고 예측 가능하도록 합니다.

## Understanding the Problem

To understand why MRO is necessary, let's consider a simple example of multiple inheritance:

```python
class A:
    def method(self):
        return "Method from A"

class B(A):
    def method(self):
        return "Method from B"

class C(A):
    def method(self):
        return "Method from C"

class D(B, C):
    pass

d = D()
print(d.method())  # Which method is called?
```

When we call `d.method()`, Python needs to determine whether to use the method from class B or class C. This is where MRO comes into play.

## 문제 이해하기

MRO가 왜 필요한지 이해하기 위해, 다중 상속의 간단한 예를 살펴보겠습니다:

```python
class A:
    def method(self):
        return "Method from A"

class B(A):
    def method(self):
        return "Method from B"

class C(A):
    def method(self):
        return "Method from C"

class D(B, C):
    pass

d = D()
print(d.method())  # 어떤 메서드가 호출될까요?
```

`d.method()`를 호출할 때, Python은 클래스 B의 메서드를 사용할지 클래스 C의 메서드를 사용할지 결정해야 합니다. 이때 MRO가 작동합니다.

## The C3 Linearization Algorithm

Python 2.3 and later use the C3 linearization algorithm for determining the MRO. The C3 algorithm ensures that:

1. A subclass appears before its parents
2. If a class inherits from multiple classes, their order in the MRO preserves the order specified in the class definition

The algorithm is complex, but you can think of it as a way to create a consistent linear ordering of classes that respects both local precedence ordering and the monotonicity principle.

## C3 선형화 알고리즘

Python 2.3 이후 버전은 MRO를 결정하기 위해 C3 선형화 알고리즘을 사용합니다. C3 알고리즘은 다음을 보장합니다:

1. 서브클래스가 부모 클래스보다 먼저 나타남
2. 클래스가 여러 클래스를 상속할 경우, MRO에서의 순서는 클래스 정의에 지정된 순서를 유지함

알고리즘은 복잡하지만, 이를 로컬 우선 순위 순서와 단조성 원칙을 모두 존중하는 일관된 선형 클래스 순서를 만드는 방법으로 생각할 수 있습니다.

## Inspecting MRO

Python provides a way to inspect the MRO of a class using the `__mro__` attribute or the `mro()` method:

```python
class A: pass
class B: pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# Alternatively
print(D.mro())
# Same output
```

The MRO is represented as a tuple of classes, starting with the class itself, followed by its base classes in the order they should be searched for methods.

## MRO 검사하기

Python은 `__mro__` 속성이나 `mro()` 메서드를 사용하여 클래스의 MRO를 검사하는 방법을 제공합니다:

```python
class A: pass
class B: pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)
# 출력: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# 대안적으로
print(D.mro())
# 동일한 출력
```

MRO는 클래스 자체로 시작하여 메서드를 검색해야 하는 순서대로 기본 클래스가 뒤따르는 클래스 튜플로 표현됩니다.

## The Diamond Problem

The classic inheritance issue that MRO solves is the "diamond problem," where a class inherits from two classes that both inherit from a common base class:

```python
class A:
    def method(self):
        return "Method from A"

class B(A):
    def method(self):
        return "Method from B"

class C(A):
    def method(self):
        return "Method from C"

class D(B, C):
    pass

d = D()
print(d.method())  # Which method is called?
```

When we call `d.method()`, Python needs to determine whether to use the method from class B or class C. This is where MRO comes into play.

## 문제 이해하기

MRO가 왜 필요한지 이해하기 위해, 다중 상속의 간단한 예를 살펴보겠습니다:

```python
class A:
    def method(self):
        return "Method from A"

class B(A):
    def method(self):
        return "Method from B"

class C(A):
    def method(self):
        return "Method from C"

class D(B, C):
    pass

d = D()
print(d.method())  # 어떤 메서드가 호출될까요?
```

`d.method()`를 호출할 때, Python은 클래스 B의 메서드를 사용할지 클래스 C의 메서드를 사용할지 결정해야 합니다. 이때 MRO가 작동합니다.

## The C3 Linearization Algorithm

Python 2.3 and later use the C3 linearization algorithm for determining the MRO. The C3 algorithm ensures that:

1. A subclass appears before its parents
2. If a class inherits from multiple classes, their order in the MRO preserves the order specified in the class definition

The algorithm is complex, but you can think of it as a way to create a consistent linear ordering of classes that respects both local precedence ordering and the monotonicity principle.

## C3 선형화 알고리즘

Python 2.3 이후 버전은 MRO를 결정하기 위해 C3 선형화 알고리즘을 사용합니다. C3 알고리즘은 다음을 보장합니다:

1. 서브클래스가 부모 클래스보다 먼저 나타남
2. 클래스가 여러 클래스를 상속할 경우, MRO에서의 순서는 클래스 정의에 지정된 순서를 유지함

알고리즘은 복잡하지만, 이를 로컬 우선 순위 순서와 단조성 원칙을 모두 존중하는 일관된 선형 클래스 순서를 만드는 방법으로 생각할 수 있습니다.

## Inspecting MRO

Python provides a way to inspect the MRO of a class using the `__mro__` attribute or the `mro()` method:

```python
class A: pass
class B: pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# Alternatively
print(D.mro())
# Same output
```

The MRO is represented as a tuple of classes, starting with the class itself, followed by its base classes in the order they should be searched for methods.

## MRO 검사하기

Python은 `__mro__` 속성이나 `mro()` 메서드를 사용하여 클래스의 MRO를 검사하는 방법을 제공합니다:

```python
class A: pass
class B: pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)
# 출력: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# 대안적으로
print(D.mro())
# 동일한 출력
```

MRO는 클래스 자체로 시작하여 메서드를 검색해야 하는 순서대로 기본 클래스가 뒤따르는 클래스 튜플로 표현됩니다.

## The Diamond Problem

The classic inheritance issue that MRO solves is the "diamond problem," where a class inherits from two classes that both inherit from a common base class:

```python
class A:
    def method(self):
        return "Method from A"

class B(A):
    def method(self):
        return "Method from B"

class C(A):
    def method(self):
        return "Method from C"

class D(B, C):
    pass

d = D()
print(d.method())  # Which method is called?
```

When we call `d.method()`, Python needs to determine whether to use the method from class B or class C. This is where MRO comes into play.

## 문제 이해하기

MRO가 왜 필요한지 이해하기 위해, 다중 상속의 간단한 예를 살펴보겠습니다:

```python
class A:
    def method(self):
        return "Method from A"

class B(A):
    def method(self):
        return "Method from B"

class C(A):
    def method(self):
        return "Method from C"

class D(B, C):
    pass

d = D()
print(d.method())  # 어떤 메서드가 호출될까요?
```

`d.method()`를 호출할 때, Python은 클래스 B의 메서드를 사용할지 클래스 C의 메서드를 사용할지 결정해야 합니다. 이때 MRO가 작동합니다.

## The C3 Linearization Algorithm

Python 2.3 and later use the C3 linearization algorithm for determining the MRO. The C3 algorithm ensures that:

1. A subclass appears before its parents
2. If a class inherits from multiple classes, their order in the MRO preserves the order specified in the class definition

The algorithm is complex, but you can think of it as a way to create a consistent linear ordering of classes that respects both local precedence ordering and the monotonicity principle.

## C3 선형화 알고리즘

Python 2.3 이후 버전은 MRO를 결정하기 위해 C3 선형화 알고리즘을 사용합니다. C3 알고리즘은 다음을 보장합니다:

1. 서브클래스가 부모 클래스보다 먼저 나타남
2. 클래스가 여러 클래스를 상속할 경우, MRO에서의 순서는 클래스 정의에 지정된 순서를 유지함

알고리즘은 복잡하지만, 이를 로컬 우선 순위 순서와 단조성 원칙을 모두 존중하는 일관된 선형 클래스 순서를 만드는 방법으로 생각할 수 있습니다.

## Inspecting MRO

Python provides a way to inspect the MRO of a class using the `__mro__` attribute or the `mro()` method:

```python
class A: pass
class B: pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# Alternatively
print(D.mro())
# Same output
```

The MRO is represented as a tuple of classes, starting with the class itself, followed by its base classes in the order they should be searched for methods.

## MRO 검사하기

Python은 `__mro__` 속성이나 `mro()` 메서드를 사용하여 클래스의 MRO를 검사하는 방법을 제공합니다:

```python
class A: pass
class B: pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)
# 출력: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# 대안적으로
print(D.mro())
# 동일한 출력
```

MRO는 클래스 자체로 시작하여 메서드를 검색해야 하는 순서대로 기본 클래스가 뒤따르는 클래스 튜플로 표현됩니다.

## The Diamond Problem

The classic inheritance issue that MRO solves is the "diamond problem," where a class inherits from two classes that both inherit from a common base class:
`

