Descriptor Guide
Author:
Raymond Hettinger

Contact:
<python at rcn dot com>

Contents

Descriptor Guide

Primer

Simple example: A descriptor that returns a constant

Dynamic lookups

Managed attributes

Customized names

Closing thoughts

Complete Practical Example

Validator class

Custom validators

Practical application

Technical Tutorial

Abstract

Definition and introduction

Descriptor protocol

Overview of descriptor invocation

Invocation from an instance

Invocation from a class

Invocation from super

Summary of invocation logic

Automatic name notification

ORM example

Pure Python Equivalents

Properties

Functions and methods

Kinds of methods

Static methods

Class methods

Member objects and __slots__

Descriptors let objects customize attribute lookup, storage, and deletion.

This guide has four major sections:

The “primer” gives a basic overview, moving gently from simple examples, adding one feature at a time. Start here if you’re new to descriptors.

The second section shows a complete, practical descriptor example. If you already know the basics, start there.

The third section provides a more technical tutorial that goes into the detailed mechanics of how descriptors work. Most people don’t need this level of detail.

The last section has pure Python equivalents for built-in descriptors that are written in C. Read this if you’re curious about how functions turn into bound methods or about the implementation of common tools like classmethod(), staticmethod(), property(), and __slots__.

# Understanding Descriptors in Python

# Python의 디스크립터 이해하기

## Introduction

Descriptors are a powerful feature in Python that enables fine-grained control over attribute access. They form the foundation for many built-in features like `property`, `classmethod`, and `staticmethod`. Understanding descriptors is essential for advanced Python programming and creating robust, maintainable code.

## 소개

디스크립터는 Python에서 속성 접근에 대한 세밀한 제어를 가능하게 하는 강력한 기능입니다. 이는 `property`, `classmethod`, `staticmethod`와 같은 많은 내장 기능의 기반을 형성합니다. 디스크립터를 이해하는 것은 고급 Python 프로그래밍과 견고하고 유지보수 가능한 코드를 작성하는 데 필수적입니다.

## What is a Descriptor?

A descriptor is an object attribute with "binding behavior" - specifically, an object whose attribute access has been overridden by methods in the descriptor protocol. These methods are `__get__`, `__set__`, and `__delete__`. If any of these methods are defined for an object, it is a descriptor.

## 디스크립터란 무엇인가?

디스크립터는 "바인딩 동작"을 가진 객체 속성입니다 - 특히, 디스크립터 프로토콜의 메서드에 의해 속성 접근이 재정의된 객체입니다. 이러한 메서드에는 `__get__`, `__set__`, `__delete__`가 있습니다. 이 메서드 중 하나라도 객체에 정의되어 있으면 그것은 디스크립터입니다.

## The Descriptor Protocol

The descriptor protocol consists of three methods:

1. `__get__(self, obj, type=None) -> value` - Called when the attribute is accessed
2. `__set__(self, obj, value) -> None` - Called when the attribute is assigned a value
3. `__delete__(self, obj) -> None` - Called when the attribute is deleted

Depending on which methods are defined, descriptors can be categorized as:

- **Data descriptors**: Define both `__get__` and `__set__`
- **Non-data descriptors**: Define only `__get__`

## 디스크립터 프로토콜

디스크립터 프로토콜은 세 가지 메서드로 구성됩니다:

1. `__get__(self, obj, type=None) -> value` - 속성에 접근할 때 호출됨
2. `__set__(self, obj, value) -> None` - 속성에 값이 할당될 때 호출됨
3. `__delete__(self, obj) -> None` - 속성이 삭제될 때 호출됨

정의된 메서드에 따라 디스크립터는 다음과 같이 분류할 수 있습니다:

- **데이터 디스크립터**: `__get__`과 `__set__` 모두 정의
- **비데이터 디스크립터**: `__get__`만 정의

## How Descriptors Work

When you access an attribute on an object, Python follows a specific lookup chain:

1. Check if it's a data descriptor on the class
2. Check the instance dictionary
3. Check if it's a non-data descriptor on the class
4. Check the class dictionary
5. Call `__getattr__` if defined

This priority order is important as it determines when descriptors are invoked.

## 디스크립터는 어떻게 작동하는가?

객체의 속성에 접근할 때, Python은 특정 조회 체인을 따릅니다:

1. 클래스에 데이터 디스크립터인지 확인
2. 인스턴스 사전 확인
3. 클래스에 비데이터 디스크립터인지 확인
4. 클래스 사전 확인
5. 정의된 경우 `__getattr__` 호출

이 우선순위 순서는 디스크립터가 언제 호출되는지 결정하므로 중요합니다.

## Built-in Descriptors

Python has several built-in descriptors that you use regularly:

### property

The `property` function creates a data descriptor that invokes user-provided functions for getting, setting, and deleting:

```python
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        """Get the person's name."""
        return self._name
        
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value
        
    @name.deleter
    def name(self):
        del self._name

# Usage
person = Person("Alice")
print(person.name)  # Calls the getter
person.name = "Bob"  # Calls the setter
del person.name  # Calls the deleter
```

### classmethod and staticmethod

These are implemented as non-data descriptors:

```python
class MyClass:
    def __init__(self, value):
        self.value = value
        
    @classmethod
    def from_string(cls, string):
        """Create an instance from a string."""
        return cls(int(string))
        
    @staticmethod
    def is_valid(value):
        """Check if a value is valid."""
        return isinstance(value, int) and value > 0

# Usage
obj = MyClass.from_string("42")  # Calls the classmethod
print(MyClass.is_valid(42))  # Calls the staticmethod
```

## 내장 디스크립터

Python에는 일상적으로 사용하는 여러 내장 디스크립터가 있습니다:

### property

`property` 함수는 가져오기, 설정하기, 삭제하기 위한 사용자 제공 함수를 호출하는 데이터 디스크립터를 생성합니다:

```python
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        """사람의 이름을 가져옵니다."""
        return self._name
        
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("이름은 문자열이어야 합니다")
        self._name = value
        
    @name.deleter
    def name(self):
        del self._name

# 사용법
person = Person("Alice")
print(person.name)  # getter 호출
person.name = "Bob"  # setter 호출
del person.name  # deleter 호출
```

### classmethod와 staticmethod

이들은 비데이터 디스크립터로 구현됩니다:

```python
class MyClass:
    def __init__(self, value):
        self.value = value
        
    @classmethod
    def from_string(cls, string):
        """문자열에서 인스턴스를 생성합니다."""
        return cls(int(string))
        
    @staticmethod
    def is_valid(value):
        """값이 유효한지 확인합니다."""
        return isinstance(value, int) and value > 0

# 사용법
obj = MyClass.from_string("42")  # classmethod 호출
print(MyClass.is_valid(42))  # staticmethod 호출
```

## Creating Custom Descriptors

Let's create some custom descriptors to demonstrate their power:

### A Type-Checking Descriptor

```python
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
        
    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return obj.__dict__[self.name]
        
    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type}")
        obj.__dict__[self.name] = value
        
    def __delete__(self, obj):
        del obj.__dict__[self.name]

# Usage
class Person:
    name = Typed("name", str)
    age = Typed("age", int)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(person.name, person.age)  # Alice 30

try:
    person.age = "thirty"  # Will raise TypeError
except TypeError as e:
    print(e)  # Expected <class 'int'>
```

### A Validation Descriptor

```python
class ValidatedProperty:
    def __init__(self, name, validator):
        self.name = name
        self.validator = validator
        
    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, None)
        
    def __set__(self, obj, value):
        if not self.validator(value):
            raise ValueError(f"Invalid value for {self.name}")
        obj.__dict__[self.name] = value

# Usage with a custom validator
def is_positive(value):
    return isinstance(value, (int, float)) and value > 0

class Product:
    price = ValidatedProperty("price", is_positive)
    
    def __init__(self, price):
        self.price = price

product = Product(10.99)
print(product.price)  # 10.99

try:
    product.price = -5  # Will raise ValueError
except ValueError as e:
    print(e)  # Invalid value for price
```

## 사용자 정의 디스크립터 만들기

디스크립터의 강력함을 보여주기 위해 몇 가지 사용자 정의 디스크립터를 만들어 보겠습니다:

### 타입 검사 디스크립터

```python
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
        
    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return obj.__dict__[self.name]
        
    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.expected_type} 타입이 필요합니다")
        obj.__dict__[self.name] = value
        
    def __delete__(self, obj):
        del obj.__dict__[self.name]

# 사용법
class Person:
    name = Typed("name", str)
    age = Typed("age", int)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(person.name, person.age)  # Alice 30

try:
    person.age = "thirty"  # TypeError 발생
except TypeError as e:
    print(e)  # <class 'int'> 타입이 필요합니다
```

### 유효성 검사 디스크립터

```python
class ValidatedProperty:
    def __init__(self, name, validator):
        self.name = name
        self.validator = validator
        
    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, None)
        
    def __set__(self, obj, value):
        if not self.validator(value):
            raise ValueError(f"{self.name}에 대한 잘못된 값")
        obj.__dict__[self.name] = value

# 사용자 정의 검증기와 함께 사용
def is_positive(value):
    return isinstance(value, (int, float)) and value > 0

class Product:
    price = ValidatedProperty("price", is_positive)
    
    def __init__(self, price):
        self.price = price

product = Product(10.99)
print(product.price)  # 10.99

try:
    product.price = -5  # ValueError 발생
except ValueError as e:
    print(e)  # price에 대한 잘못된 값
```

## Advanced Descriptor Patterns

### Lazy Properties

```python
class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__
        
    def __get__(self, obj, type=None):
        if obj is None:
            return self
        
        # Calculate value and store in instance dict
        value = self.function(obj)
        obj.__dict__[self.name] = value
        return value

# Usage
class DataProcessor:
    def __init__(self, data):
        self.data = data
        
    @LazyProperty
    def processed_data(self):
        print("Processing data (expensive operation)...")
        # Simulate expensive processing
        import time
        time.sleep(1)
        return [x * 2 for x in self.data]

processor = DataProcessor([1, 2, 3, 4, 5])
# First access calculates the value
print(processor.processed_data)  # Prints processing message and [2, 4, 6, 8, 10]
# Second access uses cached value
print(processor.processed_data)  # Directly prints [2, 4, 6, 8, 10] without processing message
```

### Unit Descriptors

```python
class Unit:
    def __init__(self, name, conversion_factor):
        self.name = name
        self.conversion_factor = conversion_factor
        
    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return obj.value * self.conversion_factor
        
    def __set__(self, obj, value):
        obj.value = value / self.conversion_factor

# Usage
class Distance:
    value = 0  # Base value in meters
    meters = Unit('meters', 1)
    kilometers = Unit('kilometers', 1000)
    miles = Unit('miles', 1609.34)
    
    def __init__(self, value=0, unit='meters'):
        setattr(self, unit, value)

# Create a distance of 1 kilometer
distance = Distance(1, 'kilometers')
print(f"{distance.meters:.2f} meters")  # 1000.00 meters
print(f"{distance.kilometers:.2f} kilometers")  # 1.00 kilometers
print(f"{distance.miles:.2f} miles")  # 0.62 miles

# Change to 2 miles
distance.miles = 2
print(f"{distance.meters:.2f} meters")  # 3218.68 meters
print(f"{distance.kilometers:.2f} kilometers")  # 3.22 kilometers
```

## 고급 디스크립터 패턴

### 지연 속성(Lazy Properties)

```python
class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__
        
    def __get__(self, obj, type=None):
        if obj is None:
            return self
        
        # 값을 계산하고 인스턴스 사전에 저장
        value = self.function(obj)
        obj.__dict__[self.name] = value
        return value

# 사용법
class DataProcessor:
    def __init__(self, data):
        self.data = data
        
    @LazyProperty
    def processed_data(self):
        print("데이터 처리 중 (비용이 많이 드는 작업)...")
        # 비용이 많이 드는 처리 시뮬레이션
        import time
        time.sleep(1)
        return [x * 2 for x in self.data]

processor = DataProcessor([1, 2, 3, 4, 5])
# 첫 번째 접근은 값을 계산
print(processor.processed_data)  # 처리 메시지와 [2, 4, 6, 8, 10] 출력
# 두 번째 접근은 캐시된 값 사용
print(processor.processed_data)  # 처리 메시지 없이 바로 [2, 4, 6, 8, 10] 출력
```

### 단위 디스크립터

```python
class Unit:
    def __init__(self, name, conversion_factor):
        self.name = name
        self.conversion_factor = conversion_factor
        
    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return obj.value * self.conversion_factor
        
    def __set__(self, obj, value):
        obj.value = value / self.conversion_factor

# 사용법
class Distance:
    value = 0  # 미터 단위의 기본값
    meters = Unit('meters', 1)
    kilometers = Unit('kilometers', 1000)
    miles = Unit('miles', 1609.34)
    
    def __init__(self, value=0, unit='meters'):
        setattr(self, unit, value)

# 1 킬로미터 거리 생성
distance = Distance(1, 'kilometers')
print(f"{distance.meters:.2f} 미터")  # 1000.00 미터
print(f"{distance.kilometers:.2f} 킬로미터")  # 1.00 킬로미터
print(f"{distance.miles:.2f} 마일")  # 0.62 마일

# 2 마일로 변경
distance.miles = 2
print(f"{distance.meters:.2f} 미터")  # 3218.68 미터
print(f"{distance.kilometers:.2f} 킬로미터")  # 3.22 킬로미터
```

## Best Practices and Considerations

1. **Understand descriptor priority**: Data descriptors have higher priority than instance attributes, while non-data descriptors have lower priority.

2. **Avoid naming conflicts**: The name used in `self.__dict__[name]` should match the attribute name in the class to prevent confusion.

3. **Use descriptors for class-wide behaviors**: Descriptors are most useful when you want to reuse behavior across multiple attributes or classes.

4. **Consider using `__set_name__`**: In Python 3.6+, descriptors can implement `__set_name__(self, owner, name)` to automatically capture their attribute name:

   ```python
   class Descriptor:
       def __set_name__(self, owner, name):
           self.name = name
       
       def __get__(self, obj, type=None):
           if obj is None:
               return self
           return obj.__dict__.get(self.name)
       
       def __set__(self, obj, value):
           obj.__dict__[self.name] = value
   
   class MyClass:
       # No need to specify the name explicitly
       x = Descriptor()
       y = Descriptor()
   ```

5. **Remember the descriptor is shared**: The descriptor object itself is shared among all instances of the class, so don't store instance-specific state on the descriptor.

## 모범 사례 및 고려사항

1. **디스크립터 우선순위 이해하기**: 데이터 디스크립터는 인스턴스 속성보다 우선순위가 높고, 비데이터 디스크립터는 우선순위가 낮습니다.

2. **이름 충돌 피하기**: `self.__dict__[name]`에 사용되는 이름은 혼란을 방지하기 위해 클래스의 속성 이름과 일치해야 합니다.

3. **클래스 전체 동작에 디스크립터 사용하기**: 디스크립터는 여러 속성이나 클래스에서 동작을 재사용하고자 할 때 가장 유용합니다.

4. **`__set_name__` 사용 고려하기**: Python 3.6 이상에서는 디스크립터가 `__set_name__(self, owner, name)`을 구현하여 자동으로 속성 이름을 캡처할 수 있습니다:

   ```python
   class Descriptor:
       def __set_name__(self, owner, name):
           self.name = name
       
       def __get__(self, obj, type=None):
           if obj is None:
               return self
           return obj.__dict__.get(self.name)
       
       def __set__(self, obj, value):
           obj.__dict__[self.name] = value
   
   class MyClass:
       # 이름을 명시적으로 지정할 필요 없음
       x = Descriptor()
       y = Descriptor()
   ```

5. **디스크립터가 공유된다는 점 기억하기**: 디스크립터 객체 자체는 클래스의 모든 인스턴스 간에 공유되므로, 디스크립터에 인스턴스별 상태를 저장하지 마세요.

Primer
In this primer, we start with the most basic possible example and then we'll add new capabilities one by one.

프라이머
이 프라이머에서는 가장 기본적인 예제로 시작하여 하나씩 새로운 기능을 추가해 나갈 것입니다.

Simple example: A descriptor that returns a constant
The Ten class is a descriptor whose __get__() method always returns the constant 10:

간단한 예제: 상수를 반환하는 디스크립터
Ten 클래스는 __get__() 메서드가 항상 상수 10을 반환하는 디스크립터입니다:

class Ten:
    def __get__(self, obj, objtype=None):
        return 10
To use the descriptor, it must be stored as a class variable in another class:

디스크립터를 사용하려면 다른 클래스의 클래스 변수로 저장해야 합니다:

class A:
    x = 5                       # Regular class attribute
    y = Ten()                   # Descriptor instance
An interactive session shows the difference between normal attribute lookup and descriptor lookup:

대화형 세션에서 일반 속성 조회와 디스크립터 조회의 차이를 보여줍니다:

>>>
a = A()                     # Make an instance of class A
a.x                         # Normal attribute lookup
5
a.y                         # Descriptor lookup
10
In the a.x attribute lookup, the dot operator finds 'x': 5 in the class dictionary. In the a.y lookup, the dot operator finds a descriptor instance, recognized by its __get__ method. Calling that method returns 10.

a.x 속성 조회에서 점 연산자는 클래스 사전에서 'x': 5를 찾습니다. a.y 조회에서 점 연산자는 __get__ 메서드로 인식되는 디스크립터 인스턴스를 찾습니다. 해당 메서드를 호출하면 10이 반환됩니다.

Note that the value 10 is not stored in either the class dictionary or the instance dictionary. Instead, the value 10 is computed on demand.

값 10은 클래스 사전이나 인스턴스 사전 어디에도 저장되지 않습니다. 대신, 값 10은 필요할 때마다 계산됩니다.

This example shows how a simple descriptor works, but it isn't very useful. For retrieving constants, normal attribute lookup would be better.

이 예제는 간단한 디스크립터가 어떻게 작동하는지 보여주지만, 그리 유용하진 않습니다. 상수를 검색하는 경우, 일반 속성 조회가 더 좋을 것입니다.

In the next section, we'll create something more useful, a dynamic lookup.

다음 섹션에서는 동적 조회와 같은 더 유용한 것을 만들어 보겠습니다.

Dynamic lookups
Interesting descriptors typically run computations instead of returning constants:

동적 조회
흥미로운 디스크립터는 일반적으로 상수를 반환하는 대신 계산을 수행합니다:

import os

class DirectorySize:

    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))

class Directory:

    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute
An interactive session shows that the lookup is dynamic — it computes different, updated answers each time:

대화형 세션에서 조회가 동적임을 보여줍니다 — 매번 다르고 업데이트된 답변을 계산합니다:

>>>
s = Directory('songs')
g = Directory('games')
s.size                              # The songs directory has twenty files
20
g.size                              # The games directory has three files
3
os.remove('games/chess')            # Delete a game
g.size                              # File count is automatically updated
2
Besides showing how descriptors can run computations, this example also reveals the purpose of the parameters to __get__(). The self parameter is size, an instance of DirectorySize. The obj parameter is either g or s, an instance of Directory. It is the obj parameter that lets the __get__() method learn the target directory. The objtype parameter is the class Directory.

디스크립터가 계산을 실행할 수 있는 방법을 보여주는 것 외에도, 이 예제는 __get__()의 매개변수 목적을 보여줍니다. self 매개변수는 DirectorySize의 인스턴스인 size입니다. obj 매개변수는 g 또는 s로, Directory의 인스턴스입니다. __get__() 메서드가 대상 디렉토리를 알 수 있게 해주는 것이 바로 obj 매개변수입니다. objtype 매개변수는 Directory 클래스입니다.

Managed attributes
A popular use for descriptors is managing access to instance data. The descriptor is assigned to a public attribute in the class dictionary while the actual data is stored as a private attribute in the instance dictionary. The descriptor's __get__() and __set__() methods are triggered when the public attribute is accessed.

관리되는 속성
디스크립터의 인기 있는 용도는 인스턴스 데이터에 대한 접근을 관리하는 것입니다. 디스크립터는 클래스 사전의 공개 속성에 할당되는 반면, 실제 데이터는 인스턴스 사전의 비공개 속성으로 저장됩니다. 공개 속성에 접근할 때 디스크립터의 __get__() 및 __set__() 메서드가 트리거됩니다.

In the following example, age is the public attribute and _age is the private attribute. When the public attribute is accessed, the descriptor logs the lookup or update:

다음 예제에서 age는 공개 속성이고 _age는 비공개 속성입니다. 공개 속성에 접근할 때, 디스크립터는 조회나 업데이트를 로깅합니다:

import logging

logging.basicConfig(level=logging.INFO)

class LoggedAgeAccess:

    def __get__(self, obj, objtype=None):
        value = obj._age
        logging.info('Accessing %r giving %r', 'age', value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', 'age', value)
        obj._age = value

class Person:

    age = LoggedAgeAccess()             # Descriptor instance

    def __init__(self, name, age):
        self.name = name                # Regular instance attribute
        self.age = age                  # Calls __set__()

    def birthday(self):
        self.age += 1                   # Calls both __get__() and __set__()
An interactive session shows that all access to the managed attribute age is logged, but that the regular attribute name is not logged:

대화형 세션에서 관리되는 속성 age에 대한 모든 접근은 로깅되지만, 일반 속성 name은 로깅되지 않음을 보여줍니다:

>>>
mary = Person('Mary M', 30)         # The initial age update is logged
INFO:root:Updating 'age' to 30
dave = Person('David D', 40)
INFO:root:Updating 'age' to 40

vars(mary)                          # The actual data is in a private attribute
{'name': 'Mary M', '_age': 30}
vars(dave)
{'name': 'David D', '_age': 40}

mary.age                            # Access the data and log the lookup
INFO:root:Accessing 'age' giving 30
30
mary.birthday()                     # Updates are logged as well
INFO:root:Accessing 'age' giving 30
INFO:root:Updating 'age' to 31

dave.name                           # Regular attribute lookup isn't logged
'David D'
dave.age                            # Only the managed attribute is logged
INFO:root:Accessing 'age' giving 40
40
One major issue with this example is that the private name _age is hardwired in the LoggedAgeAccess class. That means that each instance can only have one logged attribute and that its name is unchangeable. In the next example, we'll fix that problem.

이 예제의 주요 문제점 중 하나는 비공개 이름 _age가 LoggedAgeAccess 클래스에 하드코딩되어 있다는 것입니다. 이는 각 인스턴스가 하나의 로깅된 속성만 가질 수 있고 그 이름을 변경할 수 없다는 것을 의미합니다. 다음 예제에서는 이 문제를 해결해 보겠습니다.

Customized names
When a class uses descriptors, it can inform each descriptor about which variable name was used.

사용자 정의 이름
클래스가 디스크립터를 사용할 때, 각 디스크립터에게 어떤 변수 이름이 사용되었는지 알려줄 수 있습니다.

In this example, the Person class has two descriptor instances, name and age. When the Person class is defined, it makes a callback to __set_name__() in LoggedAccess so that the field names can be recorded, giving each descriptor its own public_name and private_name:

이 예제에서 Person 클래스에는 name과 age라는 두 개의 디스크립터 인스턴스가 있습니다. Person 클래스가 정의될 때, LoggedAccess의 __set_name__()에 콜백을 수행하여 필드 이름이 기록될 수 있도록 하고, 각 디스크립터에게 고유한 public_name과 private_name을 제공합니다:

import logging

logging.basicConfig(level=logging.INFO)

class LoggedAccess:

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        logging.info('Accessing %r giving %r', self.public_name, value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', self.public_name, value)
        setattr(obj, self.private_name, value)

class Person:

    name = LoggedAccess()                # First descriptor instance
    age = LoggedAccess()                 # Second descriptor instance

    def __init__(self, name, age):
        self.name = name                 # Calls the first descriptor
        self.age = age                   # Calls the second descriptor

    def birthday(self):
        self.age += 1
An interactive session shows that the Person class has called __set_name__() so that the field names would be recorded. Here we call vars() to look up the descriptor without triggering it:

대화형 세션에서 Person 클래스가 __set_name__()을 호출하여 필드 이름이 기록되었음을 보여줍니다. 여기서는 디스크립터를 트리거하지 않고 조회하기 위해 vars()를 호출합니다:

>>>
vars(vars(Person)['name'])
{'public_name': 'name', 'private_name': '_name'}
vars(vars(Person)['age'])
{'public_name': 'age', 'private_name': '_age'}
The new class now logs access to both name and age:

새로운 클래스는 이제 name과 age 모두에 대한 접근을 로깅합니다:

>>>
pete = Person('Peter P', 10)
INFO:root:Updating 'name' to 'Peter P'
INFO:root:Updating 'age' to 10
kate = Person('Catherine C', 20)
INFO:root:Updating 'name' to 'Catherine C'
INFO:root:Updating 'age' to 20
The two Person instances contain only the private names:

두 Person 인스턴스는 비공개 이름만 포함합니다:

>>>
vars(pete)
{'_name': 'Peter P', '_age': 10}
vars(kate)
{'_name': 'Catherine C', '_age': 20}
Closing thoughts
A descriptor is what we call any object that defines __get__(), __set__(), or __delete__().

마치며
디스크립터는 __get__(), __set__() 또는 __delete__()를 정의하는 모든 객체를 일컫는 용어입니다.

Optionally, descriptors can have a __set_name__() method. This is only used in cases where a descriptor needs to know either the class where it was created or the name of class variable it was assigned to. (This method, if present, is called even if the class is not a descriptor.)

선택적으로, 디스크립터는 __set_name__() 메서드를 가질 수 있습니다. 이는 디스크립터가 생성된 클래스나 할당된 클래스 변수의 이름을 알아야 하는 경우에만 사용됩니다. (이 메서드가 있으면, 클래스가 디스크립터가 아니더라도 호출됩니다.)

Descriptors get invoked by the dot operator during attribute lookup. If a descriptor is accessed indirectly with vars(some_class)[descriptor_name], the descriptor instance is returned without invoking it.

디스크립터는 속성 조회 중에 점 연산자에 의해 호출됩니다. 디스크립터가 vars(some_class)[descriptor_name]으로 간접적으로 접근되면, 디스크립터 인스턴스는 호출되지 않고 반환됩니다.

Descriptors only work when used as class variables. When put in instances, they have no effect.

디스크립터는 클래스 변수로 사용될 때만 작동합니다. 인스턴스에 넣으면 아무 효과가 없습니다.

The main motivation for descriptors is to provide a hook allowing objects stored in class variables to control what happens during attribute lookup.

디스크립터의 주요 동기는 클래스 변수에 저장된 객체가 속성 조회 중에 발생하는 일을 제어할 수 있는 훅을 제공하는 것입니다.

Traditionally, the calling class controls what happens during lookup. Descriptors invert that relationship and allow the data being looked-up to have a say in the matter.

전통적으로, 호출 클래스는 조회 중에 발생하는 일을 제어합니다. 디스크립터는 그 관계를 역전시켜 조회되는 데이터가 이 문제에 대해 발언권을 갖도록 합니다.

Descriptors are used throughout the language. It is how functions turn into bound methods. Common tools like classmethod(), staticmethod(), property(), and functools.cached_property() are all implemented as descriptors.

디스크립터는 언어 전체에서 사용됩니다. 이것은 함수가 바인딩된 메서드로 변하는 방식입니다. classmethod(), staticmethod(), property(), 그리고 functools.cached_property()와 같은 일반적인 도구들은 모두 디스크립터로 구현되어 있습니다.

Complete Practical Example
In this example, we create a practical and powerful tool for locating notoriously hard to find data corruption bugs.

완전한 실용 예제
이 예제에서는 악명 높게 찾기 어려운 데이터 손상 버그를 찾기 위한 실용적이고 강력한 도구를 만듭니다.

Validator class
A validator is a descriptor for managed attribute access. Prior to storing any data, it verifies that the new value meets various type and range restrictions. If those restrictions aren't met, it raises an exception to prevent data corruption at its source.

검증자 클래스
검증자는 관리되는 속성 접근을 위한 디스크립터입니다. 데이터를 저장하기 전에, 새 값이 다양한 타입과 범위 제한 조건을 충족하는지 확인합니다. 이러한 제한 조건이 충족되지 않으면, 데이터 손상을 원천에서 방지하기 위해 예외를 발생시킵니다.

This Validator class is both an abstract base class and a managed attribute descriptor:

이 Validator 클래스는 추상 기본 클래스이자 관리되는 속성 디스크립터입니다:

from abc import ABC, abstractmethod

class Validator(ABC):

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass
Custom validators need to inherit from Validator and must supply a validate() method to test various restrictions as needed.

사용자 정의 검증자는 Validator에서 상속받아야 하며, 필요에 따라 다양한 제한 조건을 테스트하기 위한 validate() 메서드를 제공해야 합니다.

Custom validators
Here are three practical data validation utilities:

사용자 정의 검증자
다음은 세 가지 실용적인 데이터 검증 유틸리티입니다:

OneOf verifies that a value is one of a restricted set of options.

Number verifies that a value is either an int or float. Optionally, it verifies that a value is between a given minimum or maximum.

String verifies that a value is a str. Optionally, it validates a given minimum or maximum length. It can validate a user-defined predicate as well.

OneOf는 값이 제한된 옵션 집합 중 하나인지 확인합니다.

Number는 값이 int 또는 float인지 확인합니다. 선택적으로, 값이 주어진 최소값과 최대값 사이에 있는지 확인합니다.

String은 값이 str인지 확인합니다. 선택적으로, 주어진 최소 또는 최대 길이를 검증합니다. 또한 사용자 정의 조건자를 검증할 수도 있습니다.

class OneOf(Validator):

    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError(
                f'Expected {value!r} to be one of {self.options!r}'
            )

class Number(Validator):

    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Expected {value!r} to be an int or float')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(
                f'Expected {value!r} to be at least {self.minvalue!r}'
            )
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(
                f'Expected {value!r} to be no more than {self.maxvalue!r}'
            )

class String(Validator):

    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Expected {value!r} to be an str')
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(
                f'Expected {value!r} to be no smaller than {self.minsize!r}'
            )
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(
                f'Expected {value!r} to be no bigger than {self.maxsize!r}'
            )
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(
                f'Expected {self.predicate} to be true for {value!r}'
            )
Practical application
Here's how the data validators can be used in a real class:

실용적 적용
여기에 실제 클래스에서 데이터 검증자를 사용하는 방법이 있습니다:

class Component:

    name = String(minsize=3, maxsize=10, predicate=str.isupper)
    kind = OneOf('wood', 'metal', 'plastic')
    quantity = Number(minvalue=0)

    def __init__(self, name, kind, quantity):
        self.name = name
        self.kind = kind
        self.quantity = quantity
The descriptors prevent invalid instances from being created:

디스크립터는 유효하지 않은 인스턴스가 생성되는 것을 방지합니다:

>>>
Component('Widget', 'metal', 5)      # Blocked: 'Widget' is not all uppercase
Traceback (most recent call last):
    ...
ValueError: Expected <method 'isupper' of 'str' objects> to be true for 'Widget'

Component('WIDGET', 'metle', 5)      # Blocked: 'metle' is misspelled
Traceback (most recent call last):
    ...
ValueError: Expected 'metle' to be one of {'metal', 'plastic', 'wood'}

Component('WIDGET', 'metal', -5)     # Blocked: -5 is negative
Traceback (most recent call last):
    ...
ValueError: Expected -5 to be at least 0

Component('WIDGET', 'metal', 'V')    # Blocked: 'V' isn't a number
Traceback (most recent call last):
    ...
TypeError: Expected 'V' to be an int or float

c = Component('WIDGET', 'metal', 5)  # Allowed:  The inputs are valid
Technical Tutorial
What follows is a more technical tutorial for the mechanics and details of how descriptors work.

기술적 튜토리얼
다음은 디스크립터가 어떻게 작동하는지에 대한 메커니즘과 세부사항에 관한 더 기술적인 튜토리얼입니다.

Abstract
Defines descriptors, summarizes the protocol, and shows how descriptors are called. Provides an example showing how object relational mappings work.

요약
디스크립터를 정의하고, 프로토콜을 요약하며, 디스크립터가 어떻게 호출되는지 보여줍니다. 객체 관계형 매핑이 어떻게 작동하는지 보여주는 예제를 제공합니다.

Learning about descriptors not only provides access to a larger toolset, it creates a deeper understanding of how Python works.

디스크립터에 대해 배우는 것은 더 큰 도구 세트에 대한 접근을 제공할 뿐만 아니라, Python이 어떻게 작동하는지에 대한 더 깊은 이해를 생성합니다.

Definition and introduction
In general, a descriptor is an attribute value that has one of the methods in the descriptor protocol. Those methods are __get__(), __set__(), and __delete__(). If any of those methods are defined for an attribute, it is said to be a descriptor.

정의 및 소개
일반적으로, 디스크립터는 디스크립터 프로토콜의 메서드 중 하나를 가진 속성 값입니다. 이러한 메서드는 __get__(), __set__(), 그리고 __delete__()입니다. 속성에 대해 이러한 메서드 중 하나라도 정의되어 있으면, 그것은 디스크립터라고 합니다.

The default behavior for attribute access is to get, set, or delete the attribute from an object's dictionary. For instance, a.x has a lookup chain starting with a.__dict__['x'], then type(a).__dict__['x'], and continuing through the method resolution order of type(a). If the looked-up value is an object defining one of the descriptor methods, then Python may override the default behavior and invoke the descriptor method instead. Where this occurs in the precedence chain depends on which descriptor methods were defined.

속성 접근에 대한 기본 동작은 객체의 사전에서 속성을 가져오거나, 설정하거나, 삭제하는 것입니다. 예를 들어, a.x는 a.__dict__['x']로 시작하는 조회 체인을 가지고, 그 다음은 type(a).__dict__['x'], 그리고 type(a)의 메서드 해결 순서를 통해 계속됩니다. 조회된 값이 디스크립터 메서드 중 하나를 정의하는 객체라면, Python은 기본 동작을 재정의하고 대신 디스크립터 메서드를 호출할 수 있습니다. 이것이 우선순위 체인에서 발생하는 위치는 어떤 디스크립터 메서드가 정의되었는지에 달려 있습니다.

Descriptors are a powerful, general purpose protocol. They are the mechanism behind properties, methods, static methods, class methods, and super(). They are used throughout Python itself. Descriptors simplify the underlying C code and offer a flexible set of new tools for everyday Python programs.

디스크립터는 강력하고 범용적인 프로토콜입니다. 이것들은 프로퍼티, 메서드, 정적 메서드, 클래스 메서드, 그리고 super() 뒤에 있는 메커니즘입니다. 이것들은 Python 자체 전체에서 사용됩니다. 디스크립터는 기본 C 코드를 단순화하고 일상적인 Python 프로그램을 위한 유연한 새로운 도구 세트를 제공합니다.

Descriptor protocol
descr.__get__(self, obj, type=None)

descr.__set__(self, obj, value)

descr.__delete__(self, obj)

That is all there is to it. Define any of these methods and an object is considered a descriptor and can override default behavior upon being looked up as an attribute.

디스크립터 프로토콜
descr.__get__(self, obj, type=None)

descr.__set__(self, obj, value)

descr.__delete__(self, obj)

그게 전부입니다. 이러한 메서드 중 하나라도 정의하면 객체는 디스크립터로 간주되며 속성으로 조회될 때 기본 동작을 재정의할 수 있습니다.

If an object defines __set__() or __delete__(), it is considered a data descriptor. Descriptors that only define __get__() are called non-data descriptors (they are often used for methods but other uses are possible).

객체가 __set__() 또는 __delete__()를 정의하면, 그것은 데이터 디스크립터로 간주됩니다. __get__()만 정의하는 디스크립터는 비데이터 디스크립터라고 합니다(이들은 종종 메서드에 사용되지만 다른 용도도 가능합니다).

Data and non-data descriptors differ in how overrides are calculated with respect to entries in an instance's dictionary. If an instance's dictionary has an entry with the same name as a data descriptor, the data descriptor takes precedence. If an instance's dictionary has an entry with the same name as a non-data descriptor, the dictionary entry takes precedence.

데이터 디스크립터와 비데이터 디스크립터는 인스턴스 사전의 항목과 관련하여 재정의가 계산되는 방식이 다릅니다. 인스턴스 사전에 데이터 디스크립터와 동일한 이름의 항목이 있는 경우, 데이터 디스크립터가 우선합니다. 인스턴스 사전에 비데이터 디스크립터와 동일한 이름의 항목이 있는 경우, 사전 항목이 우선합니다.

To make a read-only data descriptor, define both __get__() and __set__() with the __set__() raising an AttributeError when called. Defining the __set__() method with an exception raising placeholder is enough to make it a data descriptor.

읽기 전용 데이터 디스크립터를 만들려면, __set__()이 호출될 때 AttributeError를 발생시키는 __get__()과 __set__() 모두를 정의하세요. 예외를 발생시키는 자리 표시자로 __set__() 메서드를 정의하는 것만으로도 데이터 디스크립터가 됩니다.

Overview of descriptor invocation
A descriptor can be called directly with desc.__get__(obj) or desc.__get__(None, cls).

디스크립터 호출 개요
디스크립터는 desc.__get__(obj) 또는 desc.__get__(None, cls)로 직접 호출할 수 있습니다.

But it is more common for a descriptor to be invoked automatically from attribute access.

하지만 디스크립터가 속성 접근에서 자동으로 호출되는 것이 더 일반적입니다.

The expression obj.x looks up the attribute x in the chain of namespaces for obj. If the search finds a descriptor outside of the instance __dict__, its __get__() method is invoked according to the precedence rules listed below.

표현식 obj.x는 obj에 대한 네임스페이스 체인에서 속성 x를 조회합니다. 검색이 인스턴스 __dict__ 외부에서 디스크립터를 찾으면, 아래 나열된 우선순위 규칙에 따라 그것의 __get__() 메서드가 호출됩니다.

The details of invocation depend on whether obj is an object, class, or instance of super.

호출의 세부 사항은 obj가 객체, 클래스, 또는 super의 인스턴스인지에 따라 달라집니다.

Invocation from an instance
Instance lookup scans through a chain of namespaces giving data descriptors the highest priority, followed by instance variables, then non-data descriptors, then class variables, and lastly __getattr__() if it is provided.

인스턴스에서의 호출
인스턴스 조회는 데이터 디스크립터에게 가장 높은 우선순위를 부여하는 네임스페이스 체인을 스캔하고, 그 다음으로 인스턴스 변수, 비데이터 디스크립터, 클래스 변수, 그리고 마지막으로 제공된 경우 __getattr__()을 따릅니다.

If a descriptor is found for a.x, then it is invoked with: desc.__get__(a, type(a)).

a.x에 대한 디스크립터가 발견되면, 다음과 같이 호출됩니다: desc.__get__(a, type(a)).

The logic for a dotted lookup is in object.__getattribute__(). Here is a pure Python equivalent:

점 표기법 조회의 로직은 object.__getattribute__()에 있습니다. 다음은 순수 Python 등가물입니다:

def find_name_in_mro(cls, name, default):
    "Emulate _PyType_Lookup() in Objects/typeobject.c"
    for base in cls.__mro__:
        if name in vars(base):
            return vars(base)[name]
    return default

def object_getattribute(obj, name):
    "Emulate PyObject_GenericGetAttr() in Objects/object.c"
    null = object()
    objtype = type(obj)
    cls_var = find_name_in_mro(objtype, name, null)
    descr_get = getattr(type(cls_var), '__get__', null)
    if descr_get is not null:
        if (hasattr(type(cls_var), '__set__')
            or hasattr(type(cls_var), '__delete__')):
            return descr_get(cls_var, obj, objtype)     # data descriptor
    if hasattr(obj, '__dict__') and name in vars(obj):
        return vars(obj)[name]                          # instance variable
    if descr_get is not null:
        return descr_get(cls_var, obj, objtype)         # non-data descriptor
    if cls_var is not null:
        return cls_var                                  # class variable
    raise AttributeError(name)
Note, there is no __getattr__() hook in the __getattribute__() code. That is why calling __getattribute__() directly or with super().__getattribute__ will bypass __getattr__() entirely.

참고로, __getattribute__() 코드에는 __getattr__() 훅이 없습니다. 그래서 __getattribute__()를 직접 호출하거나 super().__getattribute__로 호출하면 __getattr__()을 완전히 우회합니다.

Instead, it is the dot operator and the getattr() function that are responsible for invoking __getattr__() whenever __getattribute__() raises an AttributeError. Their logic is encapsulated in a helper function:

대신, 점 연산자와 getattr() 함수가 __getattribute__()가 AttributeError를 발생시킬 때마다 __getattr__()을 호출하는 역할을 합니다. 그들의 로직은 헬퍼 함수에 캡슐화되어 있습니다:

def getattr_hook(obj, name):
    "Emulate slot_tp_getattr_hook() in Objects/typeobject.c"
    try:
        return obj.__getattribute__(name)
    except AttributeError:
        if not hasattr(type(obj), '__getattr__'):
            raise
    return type(obj).__getattr__(obj, name)             # __getattr__
Invocation from a class
The logic for a dotted lookup such as A.x is in type.__getattribute__(). The steps are similar to those for object.__getattribute__() but the instance dictionary lookup is replaced by a search through the class's method resolution order.

클래스에서의 호출
A.x와 같은 점 표기법 조회의 로직은 type.__getattribute__()에 있습니다. 단계는 object.__getattribute__()와 유사하지만 인스턴스 사전 조회가 클래스의 메서드 해결 순서를 통한 검색으로 대체됩니다.

If a descriptor is found, it is invoked with desc.__get__(None, A).

디스크립터가 발견되면, desc.__get__(None, A)로 호출됩니다.

The full C implementation can be found in type_getattro() and _PyType_Lookup() in Objects/typeobject.c.

전체 C 구현은 Objects/typeobject.c의 type_getattro()와 _PyType_Lookup()에서 찾을 수 있습니다.

Invocation from super
The logic for super's dotted lookup is in the __getattribute__() method for object returned by super().

super에서의 호출
super의 점 표기법 조회의 로직은 super()에 의해 반환된 객체의 __getattribute__() 메서드에 있습니다.

A dotted lookup such as super(A, obj).m searches obj.__class__.__mro__ for the base class B immediately following A and then returns B.__dict__['m'].__get__(obj, A). If not a descriptor, m is returned unchanged.

super(A, obj).m과 같은 점 표기법 조회는 obj.__class__.__mro__에서 A 바로 다음에 오는 기본 클래스 B를 검색한 다음 B.__dict__['m'].__get__(obj, A)를 반환합니다. 디스크립터가 아니면, m은 변경되지 않고 반환됩니다.

The full C implementation can be found in super_getattro() in Objects/typeobject.c. A pure Python equivalent can be found in Guido's Tutorial.

전체 C 구현은 Objects/typeobject.c의 super_getattro()에서 찾을 수 있습니다. 순수 Python 등가물은 Guido의 튜토리얼에서 찾을 수 있습니다.

Summary of invocation logic
The mechanism for descriptors is embedded in the __getattribute__() methods for object, type, and super().

호출 로직 요약
디스크립터의 메커니즘은 object, type, 그리고 super()의 __getattribute__() 메서드에 내장되어 있습니다.

The important points to remember are:

Descriptors are invoked by the __getattribute__() method.

Classes inherit this machinery from object, type, or super().

Overriding __getattribute__() prevents automatic descriptor calls because all the descriptor logic is in that method.

object.__getattribute__() and type.__getattribute__() make different calls to __get__(). The first includes the instance and may include the class. The second puts in None for the instance and always includes the class.

Data descriptors always override instance dictionaries.

Non-data descriptors may be overridden by instance dictionaries.

기억해야 할 중요한 점은 다음과 같습니다:

디스크립터는 __getattribute__() 메서드에 의해 호출됩니다.

클래스는 이 메커니즘을 object, type, 또는 super()로부터 상속받습니다.

__getattribute__()를 재정의하면 모든 디스크립터 로직이 해당 메서드에 있기 때문에 자동 디스크립터 호출이 방지됩니다.

object.__getattribute__()와 type.__getattribute__()는 __get__()에 다른 호출을 합니다. 첫 번째는 인스턴스를 포함하고 클래스를 포함할 수 있습니다. 두 번째는 인스턴스에 None을 넣고 항상 클래스를 포함합니다.

데이터 디스크립터는 항상 인스턴스 사전을 재정의합니다.

비데이터 디스크립터는 인스턴스 사전에 의해 재정의될 수 있습니다.

Automatic name notification
Sometimes it is desirable for a descriptor to know what class variable name it was assigned to. When a new class is created, the type metaclass scans the dictionary of the new class. If any of the entries are descriptors and if they define __set_name__(), that method is called with two arguments. The owner is the class where the descriptor is used, and the name is the class variable the descriptor was assigned to.

자동 이름 통지
때로는 디스크립터가 자신이 할당된 클래스 변수 이름을 알기를 원할 수 있습니다. 새 클래스가 생성될 때, type 메타클래스는 새 클래스의 사전을 스캔합니다. 항목 중 하나라도 디스크립터이고 __set_name__()을 정의하면, 해당 메서드는 두 인수와 함께 호출됩니다. owner는 디스크립터가 사용되는 클래스이고, name은 디스크립터가 할당된 클래스 변수입니다.

The implementation details are in type_new() and set_names() in Objects/typeobject.c.

구현 세부 사항은 Objects/typeobject.c의 type_new()와 set_names()에 있습니다.

Since the update logic is in type.__new__(), notifications only take place at the time of class creation. If descriptors are added to the class afterwards, __set_name__() will need to be called manually.

업데이트 로직이 type.__new__()에 있기 때문에, 통지는 클래스 생성 시에만 발생합니다. 디스크립터가 나중에 클래스에 추가되면, __set_name__()을 수동으로 호출해야 합니다.

ORM example
The following code is a simplified skeleton showing how data descriptors could be used to implement an object relational mapping.

ORM 예제
다음 코드는 데이터 디스크립터가 객체 관계형 매핑을 구현하는 데 어떻게 사용될 수 있는지 보여주는 단순화된 골격입니다.

The essential idea is that the data is stored in an external database. The Python instances only hold keys to the database's tables. Descriptors take care of lookups or updates:

핵심 아이디어는 데이터가 외부 데이터베이스에 저장된다는 것입니다. Python 인스턴스는 데이터베이스 테이블에 대한 키만 보유합니다. 디스크립터는 조회나 업데이트를 처리합니다:

class Field:

    def __set_name__(self, owner, name):
        self.fetch = f'SELECT {name} FROM {owner.table} WHERE {owner.key}=?;'
        self.store = f'UPDATE {owner.table} SET {name}=? WHERE {owner.key}=?;'

    def __get__(self, obj, objtype=None):
        return conn.execute(self.fetch, [obj.key]).fetchone()[0]

    def __set__(self, obj, value):
        conn.execute(self.store, [value, obj.key])
        conn.commit()
We can use the Field class to define models that describe the schema for each table in a database:

Field 클래스를 사용하여 데이터베이스의 각 테이블에 대한 스키마를 설명하는 모델을 정의할 수 있습니다:

class Movie:
    table = 'Movies'                    # Table name
    key = 'title'                       # Primary key
    director = Field()
    year = Field()

    def __init__(self, key):
        self.key = key

class Song:
    table = 'Music'
    key = 'title'
    artist = Field()
    year = Field()
    genre = Field()

    def __init__(self, key):
        self.key = key
To use the models, first connect to the database:

모델을 사용하려면, 먼저 데이터베이스에 연결하세요:

>>>
import sqlite3
conn = sqlite3.connect('entertainment.db')
An interactive session shows how data is retrieved from the database and how it can be updated:

대화형 세션에서 데이터베이스에서 데이터를 검색하는 방법과 업데이트하는 방법을 보여줍니다:

>>>
Movie('Star Wars').director
'George Lucas'
jaws = Movie('Jaws')
f'Released in {jaws.year} by {jaws.director}'
'Released in 1975 by Steven Spielberg'

Song('Country Roads').artist
'John Denver'

Movie('Star Wars').director = 'J.J. Abrams'
Movie('Star Wars').director
'J.J. Abrams'

Pure Python Equivalents
The descriptor protocol is simple and offers exciting possibilities. Several use cases are so common that they have been prepackaged into built-in tools. Properties, bound methods, static methods, class methods, and __slots__ are all based on the descriptor protocol.

순수 Python 등가물
디스크립터 프로토콜은 단순하면서도 흥미로운 가능성을 제공합니다. 몇 가지 사용 사례는 매우 일반적이어서 내장 도구로 미리 패키징되어 있습니다. Properties, 바인딩된 메서드, 정적 메서드, 클래스 메서드, 그리고 __slots__는 모두 디스크립터 프로토콜을 기반으로 합니다.

Properties
Calling property() is a succinct way of building a data descriptor that triggers a function call upon access to an attribute. Its signature is:

property(fget=None, fset=None, fdel=None, doc=None) -> property
The documentation shows a typical use to define a managed attribute x:

class C:
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x = property(getx, setx, delx, "I'm the 'x' property.")
To see how property() is implemented in terms of the descriptor protocol, here is a pure Python equivalent that implements most of the core functionality:

Properties
property()를 호출하는 것은 속성 접근 시 함수 호출을 트리거하는 데이터 디스크립터를 구축하는 간결한 방법입니다. 그 서명은 다음과 같습니다:

property(fget=None, fset=None, fdel=None, doc=None) -> property
문서에는 관리되는 속성 x를 정의하는 전형적인 사용법이 나와 있습니다:

class C:
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x = property(getx, setx, delx, "I'm the 'x' property.")
디스크립터 프로토콜 측면에서 property()가 어떻게 구현되는지 보려면, 다음은 핵심 기능의 대부분을 구현하는 순수 Python 등가물입니다:

class Property:
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __set_name__(self, owner, name):
        self.__name__ = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)
The property() builtin helps whenever a user interface has granted attribute access and then subsequent changes require the intervention of a method.

For instance, a spreadsheet class may grant access to a cell value through Cell('b10').value. Subsequent improvements to the program require the cell to be recalculated on every access; however, the programmer does not want to affect existing client code accessing the attribute directly. The solution is to wrap access to the value attribute in a property data descriptor:

class Cell:
    ...

    @property
    def value(self):
        "Recalculate the cell before returning value"
        self.recalc()
        return self._value
Either the built-in property() or our Property() equivalent would work in this example.

property() 내장 함수는 사용자 인터페이스가 속성 접근을 허용한 다음 후속 변경에 메서드 개입이 필요할 때마다 도움이 됩니다.

예를 들어, 스프레드시트 클래스는 Cell('b10').value를 통해 셀 값에 접근할 수 있게 할 수 있습니다. 프로그램의 후속 개선 사항은 모든 접근 시 셀을 재계산해야 합니다. 그러나 프로그래머는 속성에 직접 접근하는 기존 클라이언트 코드에 영향을 주고 싶지 않습니다. 해결책은 value 속성에 대한 접근을 property 데이터 디스크립터로 감싸는 것입니다:

class Cell:
    ...

    @property
    def value(self):
        "셀을 반환하기 전에 재계산"
        self.recalc()
        return self._value
이 예제에서는 내장 property() 또는 우리의 Property() 등가물 둘 다 작동할 것입니다.

Functions and methods
Python's object oriented features are built upon a function based environment. Using non-data descriptors, the two are merged seamlessly.

Functions stored in class dictionaries get turned into methods when invoked. Methods only differ from regular functions in that the object instance is prepended to the other arguments. By convention, the instance is called self but could be called this or any other variable name.

Methods can be created manually with types.MethodType which is roughly equivalent to:

함수와 메서드
Python의 객체 지향 기능은 함수 기반 환경 위에 구축되어 있습니다. 비데이터 디스크립터를 사용하면 두 가지가 원활하게 병합됩니다.

클래스 사전에 저장된 함수는 호출될 때 메서드로 전환됩니다. 메서드는 객체 인스턴스가 다른 인수 앞에 추가된다는 점에서만 일반 함수와 다릅니다. 관례적으로 인스턴스는 self라고 불리지만 this나 다른 변수 이름으로 불릴 수도 있습니다.

메서드는 types.MethodType으로 수동으로 생성될 수 있으며, 대략 다음과 같습니다:

class MethodType:
    "Emulate PyMethod_Type in Objects/classobject.c"

    def __init__(self, func, obj):
        self.__func__ = func
        self.__self__ = obj

    def __call__(self, *args, **kwargs):
        func = self.__func__
        obj = self.__self__
        return func(obj, *args, **kwargs)

    def __getattribute__(self, name):
        "Emulate method_getset() in Objects/classobject.c"
        if name == '__doc__':
            return self.__func__.__doc__
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        "Emulate method_getattro() in Objects/classobject.c"
        return getattr(self.__func__, name)

    def __get__(self, obj, objtype=None):
        "Emulate method_descr_get() in Objects/classobject.c"
        return self
To support automatic creation of methods, functions include the __get__() method for binding methods during attribute access. This means that functions are non-data descriptors that return bound methods during dotted lookup from an instance. Here's how it works:

메서드의 자동 생성을 지원하기 위해, 함수는 속성 접근 중에 메서드를 바인딩하기 위한 __get__() 메서드를 포함합니다. 이는 함수가 인스턴스에서 점 표기법 조회 중에 바인딩된 메서드를 반환하는 비데이터 디스크립터임을 의미합니다. 작동 방식은 다음과 같습니다:

class Function:
    ...

    def __get__(self, obj, objtype=None):
        "Simulate func_descr_get() in Objects/funcobject.c"
        if obj is None:
            return self
        return MethodType(self, obj)
Running the following class in the interpreter shows how the function descriptor works in practice:

다음 클래스를 인터프리터에서 실행하면 함수 디스크립터가 실제로 어떻게 작동하는지 보여줍니다:

class D:
    def f(self):
         return self

class D2:
    pass
The function has a qualified name attribute to support introspection:

함수는 인트로스펙션을 지원하기 위한 정규화된 이름 속성을 가지고 있습니다:

>>>
D.f.__qualname__
'D.f'
Accessing the function through the class dictionary does not invoke __get__(). Instead, it just returns the underlying function object:

클래스 사전을 통해 함수에 접근하는 것은 __get__()을 호출하지 않습니다. 대신, 기본 함수 객체를 반환합니다:

>>>
D.__dict__['f']
<function D.f at 0x00C45070>
Dotted access from a class calls __get__() which just returns the underlying function unchanged:

클래스에서의 점 표기법 접근은 __get__()을 호출하며, 이는 기본 함수를 변경하지 않고 반환합니다:

>>>
D.f
<function D.f at 0x00C45070>
The interesting behavior occurs during dotted access from an instance. The dotted lookup calls __get__() which returns a bound method object:

흥미로운 동작은 인스턴스에서의 점 표기법 접근 중에 발생합니다. 점 표기법 조회는 __get__()을 호출하며, 이는 바인딩된 메서드 객체를 반환합니다:

>>>
d = D()
d.f
<bound method D.f of <__main__.D object at 0x00B18C90>>
Internally, the bound method stores the underlying function and the bound instance:

내부적으로, 바인딩된 메서드는 기본 함수와 바인딩된 인스턴스를 저장합니다:

>>>
d.f.__func__
<function D.f at 0x00C45070>

d.f.__self__
<__main__.D object at 0x00B18C90>
If you have ever wondered where self comes from in regular methods or where cls comes from in class methods, this is it!

일반 메서드에서 self가 어디서 오는지 또는 클래스 메서드에서 cls가 어디서 오는지 궁금했다면, 바로 이것입니다!

Kinds of methods
Non-data descriptors provide a simple mechanism for variations on the usual patterns of binding functions into methods.

To recap, functions have a __get__() method so that they can be converted to a method when accessed as attributes. The non-data descriptor transforms an obj.f(*args) call into f(obj, *args). Calling cls.f(*args) becomes f(*args).

This chart summarizes the binding and its two most useful variants:

Transformation | Called from an object | Called from a class
-------------- | --------------------- | ------------------
function       | f(obj, *args)         | f(*args)
staticmethod   | f(*args)              | f(*args)
classmethod    | f(type(obj), *args)   | f(cls, *args)

메서드의 종류
비데이터 디스크립터는 함수를 메서드로 바인딩하는 일반적인 패턴에 대한 변형을 위한 간단한 메커니즘을 제공합니다.

요약하자면, 함수는 속성으로 접근될 때 메서드로 변환될 수 있도록 __get__() 메서드를 가지고 있습니다. 비데이터 디스크립터는 obj.f(*args) 호출을 f(obj, *args)로 변환합니다. cls.f(*args) 호출은 f(*args)가 됩니다.

이 차트는 바인딩과 그것의 가장 유용한 두 가지 변형을 요약합니다:

변환          | 객체에서 호출          | 클래스에서 호출
------------- | --------------------- | ---------------
함수          | f(obj, *args)         | f(*args)
정적 메서드   | f(*args)              | f(*args)
클래스 메서드 | f(type(obj), *args)   | f(cls, *args)

Static methods
Static methods return the underlying function without changes. Calling either c.f or C.f is the equivalent of a direct lookup into object.__getattribute__(c, "f") or object.__getattribute__(C, "f"). As a result, the function becomes identically accessible from either an object or a class.

Good candidates for static methods are methods that do not reference the self variable.

For instance, a statistics package may include a container class for experimental data. The class provides normal methods for computing the average, mean, median, and other descriptive statistics that depend on the data. However, there may be useful functions which are conceptually related but do not depend on the data. For instance, erf(x) is handy conversion routine that comes up in statistical work but does not directly depend on a particular dataset. It can be called either from an object or the class: s.erf(1.5) --> 0.9332 or Sample.erf(1.5) --> 0.9332.

Since static methods return the underlying function with no changes, the example calls are unexciting:

정적 메서드
정적 메서드는 기본 함수를 변경 없이 반환합니다. c.f 또는 C.f를 호출하는 것은 object.__getattribute__(c, "f") 또는 object.__getattribute__(C, "f")로 직접 조회하는 것과 동일합니다. 결과적으로, 함수는 객체나 클래스 어느 쪽에서도 동일하게 접근 가능합니다.

정적 메서드의 좋은 후보는 self 변수를 참조하지 않는 메서드입니다.

예를 들어, 통계 패키지는 실험 데이터를 위한 컨테이너 클래스를 포함할 수 있습니다. 클래스는 데이터에 의존하는 평균, 중앙값, 그리고 다른 설명 통계를 계산하기 위한 일반 메서드를 제공합니다. 그러나 개념적으로 관련되어 있지만 데이터에 의존하지 않는 유용한 함수들이 있을 수 있습니다. 예를 들어, erf(x)는 통계 작업에서 유용한 변환 루틴이지만 특정 데이터셋에 직접 의존하지 않습니다. 이는 객체나 클래스에서 호출될 수 있습니다: s.erf(1.5) --> 0.9332 또는 Sample.erf(1.5) --> 0.9332.

정적 메서드는 기본 함수를 변경 없이 반환하기 때문에, 예시 호출은 흥미롭지 않습니다:

class E:
    @staticmethod
    def f(x):
        return x * 10
>>>
E.f(3)
30
E().f(3)
30
Using the non-data descriptor protocol, a pure Python version of staticmethod() would look like this:

비데이터 디스크립터 프로토콜을 사용하면, staticmethod()의 순수 Python 버전은 다음과 같습니다:

import functools

class StaticMethod:
    "Emulate PyStaticMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f
        functools.update_wrapper(self, f)

    def __get__(self, obj, objtype=None):
        return self.f

    def __call__(self, *args, **kwds):
        return self.f(*args, **kwds)
The functools.update_wrapper() call adds a __wrapped__ attribute that refers to the underlying function. Also it carries forward the attributes necessary to make the wrapper look like the wrapped function: __name__, __qualname__, __doc__, and __annotations__.

functools.update_wrapper() 호출은 기본 함수를 참조하는 __wrapped__ 속성을 추가합니다. 또한 래퍼가 래핑된 함수처럼 보이게 하는 데 필요한 속성을 전달합니다: __name__, __qualname__, __doc__, 그리고 __annotations__.

Class methods
Unlike static methods, class methods prepend the class reference to the argument list before calling the function. This format is the same for whether the caller is an object or a class:

클래스 메서드
정적 메서드와 달리, 클래스 메서드는 함수를 호출하기 전에 클래스 참조를 인수 목록 앞에 추가합니다. 이 형식은 호출자가 객체이든 클래스이든 동일합니다:

class F:
    @classmethod
    def f(cls, x):
        return cls.__name__, x
>>>
F.f(3)
('F', 3)
F().f(3)
('F', 3)
This behavior is useful whenever the method only needs to have a class reference and does not rely on data stored in a specific instance. One use for class methods is to create alternate class constructors. For example, the classmethod dict.fromkeys() creates a new dictionary from a list of keys. The pure Python equivalent is:

이 동작은 메서드가 클래스 참조만 필요로 하고 특정 인스턴스에 저장된 데이터에 의존하지 않을 때마다 유용합니다. 클래스 메서드의 한 가지 용도는 대체 클래스 생성자를 만드는 것입니다. 예를 들어, classmethod dict.fromkeys()는 키 목록에서 새 사전을 생성합니다. 순수 Python 등가물은 다음과 같습니다:

class Dict(dict):
    @classmethod
    def fromkeys(cls, iterable, value=None):
        "Emulate dict_fromkeys() in Objects/dictobject.c"
        d = cls()
        for key in iterable:
            d[key] = value
        return d
Now a new dictionary of unique keys can be constructed like this:

이제 고유 키의 새 사전이 다음과 같이 생성될 수 있습니다:

>>>
d = Dict.fromkeys('abracadabra')
type(d) is Dict
True
d
{'a': None, 'b': None, 'r': None, 'c': None, 'd': None}
Using the non-data descriptor protocol, a pure Python version of classmethod() would look like this:

비데이터 디스크립터 프로토콜을 사용하면, classmethod()의 순수 Python 버전은 다음과 같습니다:

import functools

class ClassMethod:
    "Emulate PyClassMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f
        functools.update_wrapper(self, f)

    def __get__(self, obj, cls=None):
        if cls is None:
            cls = type(obj)
        return MethodType(self.f, cls)
The functools.update_wrapper() call in ClassMethod adds a __wrapped__ attribute that refers to the underlying function. Also it carries forward the attributes necessary to make the wrapper look like the wrapped function: __name__, __qualname__, __doc__, and __annotations__.

ClassMethod의 functools.update_wrapper() 호출은 기본 함수를 참조하는 __wrapped__ 속성을 추가합니다. 또한 래퍼가 래핑된 함수처럼 보이게 하는 데 필요한 속성을 전달합니다: __name__, __qualname__, __doc__, 그리고 __annotations__.

Member objects and __slots__
When a class defines __slots__, it replaces instance dictionaries with a fixed-length array of slot values. From a user point of view that has several effects:

1. Provides immediate detection of bugs due to misspelled attribute assignments. Only attribute names specified in __slots__ are allowed:

멤버 객체와 __slots__
클래스가 __slots__를 정의하면, 인스턴스 사전을 고정 길이의 슬롯 값 배열로 대체합니다. 사용자 관점에서 이는 몇 가지 효과가 있습니다:

1. 잘못된 속성 할당으로 인한 버그를 즉시 감지합니다. __slots__에 지정된 속성 이름만 허용됩니다:

class Vehicle:
    __slots__ = ('id_number', 'make', 'model')
>>>
auto = Vehicle()
auto.id_nubmer = 'VYE483814LQEX'
Traceback (most recent call last):
    ...
AttributeError: 'Vehicle' object has no attribute 'id_nubmer'
2. Helps create immutable objects where descriptors manage access to private attributes stored in __slots__:

2. 디스크립터가 __slots__에 저장된 비공개 속성에 대한 접근을 관리하는 불변 객체를 생성하는 데 도움이 됩니다:

class Immutable:

    __slots__ = ('_dept', '_name')          # Replace the instance dictionary

    def __init__(self, dept, name):
        self._dept = dept                   # Store to private attribute
        self._name = name                   # Store to private attribute

    @property                               # Read-only descriptor
    def dept(self):
        return self._dept

    @property
    def name(self):                         # Read-only descriptor
        return self._name
>>>
mark = Immutable('Botany', 'Mark Watney')
mark.dept
'Botany'
mark.dept = 'Space Pirate'
Traceback (most recent call last):
    ...
AttributeError: property 'dept' of 'Immutable' object has no setter
mark.location = 'Mars'
Traceback (most recent call last):
    ...
AttributeError: 'Immutable' object has no attribute 'location'
3. Saves memory. On a 64-bit Linux build, an instance with two attributes takes 48 bytes with __slots__ and 152 bytes without. This flyweight design pattern likely only matters when a large number of instances are going to be created.

4. Improves speed. Reading instance variables is 35% faster with __slots__ (as measured with Python 3.10 on an Apple M1 processor).

5. Blocks tools like functools.cached_property() which require an instance dictionary to function correctly:

3. 메모리를 절약합니다. 64비트 Linux 빌드에서, 두 개의 속성을 가진 인스턴스는 __slots__를 사용하면 48바이트, 사용하지 않으면 152바이트를 차지합니다. 이 플라이웨이트 디자인 패턴은 많은 수의 인스턴스가 생성될 때만 중요할 가능성이 높습니다.

4. 속도를 향상시킵니다. 인스턴스 변수 읽기는 __slots__를 사용하면 35% 더 빠릅니다(Apple M1 프로세서에서 Python 3.10으로 측정 시).

5. 인스턴스 사전이 올바르게 작동하는 데 필요한 functools.cached_property()와 같은 도구를 차단합니다:

from functools import cached_property

class CP:
    __slots__ = ()                          # Eliminates the instance dict

    @cached_property                        # Requires an instance dict
    def pi(self):
        return 4 * sum((-1.0)**n / (2.0*n + 1.0)
                       for n in reversed(range(100_000)))
>>>
CP().pi
Traceback (most recent call last):
  ...
TypeError: No '__dict__' attribute on 'CP' instance to cache 'pi' property.
It is not possible to create an exact drop-in pure Python version of __slots__ because it requires direct access to C structures and control over object memory allocation. However, we can build a mostly faithful simulation where the actual C structure for slots is emulated by a private _slotvalues list. Reads and writes to that private structure are managed by member descriptors:

__slots__의 정확한 드롭인 순수 Python 버전을 만드는 것은 불가능합니다. 왜냐하면 C 구조에 직접 접근하고 객체 메모리 할당을 제어해야 하기 때문입니다. 그러나 실제 슬롯에 대한 C 구조가 비공개 _slotvalues 목록으로 에뮬레이션되는 대부분 충실한 시뮬레이션을 구축할 수 있습니다. 그 비공개 구조에 대한 읽기와 쓰기는 멤버 디스크립터에 의해 관리됩니다:

null = object()

class Member:

    def __init__(self, name, clsname, offset):
        'Emulate PyMemberDef in Include/structmember.h'
        # Also see descr_new() in Objects/descrobject.c
        self.name = name
        self.clsname = clsname
        self.offset = offset

    def __get__(self, obj, objtype=None):
        'Emulate member_get() in Objects/descrobject.c'
        # Also see PyMember_GetOne() in Python/structmember.c
        if obj is None:
            return self
        value = obj._slotvalues[self.offset]
        if value is null:
            raise AttributeError(self.name)
        return value

    def __set__(self, obj, value):
        'Emulate member_set() in Objects/descrobject.c'
        obj._slotvalues[self.offset] = value

    def __delete__(self, obj):
        'Emulate member_delete() in Objects/descrobject.c'
        value = obj._slotvalues[self.offset]
        if value is null:
            raise AttributeError(self.name)
        obj._slotvalues[self.offset] = null

    def __repr__(self):
        'Emulate member_repr() in Objects/descrobject.c'
        return f'<Member {self.name!r} of {self.clsname!r}>'
The type.__new__() method takes care of adding member objects to class variables:

type.__new__() 메서드는 멤버 객체를 클래스 변수에 추가하는 역할을 합니다:

class Type(type):
    'Simulate how the type metaclass adds member objects for slots'

    def __new__(mcls, clsname, bases, mapping, **kwargs):
        'Emulate type_new() in Objects/typeobject.c'
        # type_new() calls PyTypeReady() which calls add_methods()
        slot_names = mapping.get('slot_names', [])
        for offset, name in enumerate(slot_names):
            mapping[name] = Member(name, clsname, offset)
        return type.__new__(mcls, clsname, bases, mapping, **kwargs)
The object.__new__() method takes care of creating instances that have slots instead of an instance dictionary. Here is a rough simulation in pure Python:

object.__new__() 메서드는 인스턴스 사전 대신 슬롯을 가진 인스턴스를 생성하는 역할을 합니다. 다음은 순수 Python에서의 대략적인 시뮬레이션입니다:

class Object:
    'Simulate how object.__new__() allocates memory for __slots__'

    def __new__(cls, *args, **kwargs):
        'Emulate object_new() in Objects/typeobject.c'
        inst = super().__new__(cls)
        if hasattr(cls, 'slot_names'):
            empty_slots = [null] * len(cls.slot_names)
            object.__setattr__(inst, '_slotvalues', empty_slots)
        return inst

    def __setattr__(self, name, value):
        'Emulate _PyObject_GenericSetAttrWithDict() Objects/object.c'
        cls = type(self)
        if hasattr(cls, 'slot_names') and name not in cls.slot_names:
            raise AttributeError(
                f'{cls.__name__!r} object has no attribute {name!r}'
            )
        super().__setattr__(name, value)

    def __delattr__(self, name):
        'Emulate _PyObject_GenericSetAttrWithDict() Objects/object.c'
        cls = type(self)
        if hasattr(cls, 'slot_names') and name not in cls.slot_names:
            raise AttributeError(
                f'{cls.__name__!r} object has no attribute {name!r}'
            )
        super().__delattr__(name)
To use the simulation in a real class, just inherit from Object and set the metaclass to Type:

실제 클래스에서 시뮬레이션을 사용하려면, Object에서 상속받고 메타클래스를 Type으로 설정하면 됩니다:

class H(Object, metaclass=Type):
    'Instance variables stored in slots'

    slot_names = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y
At this point, the metaclass has loaded member objects for x and y:

이 시점에서, 메타클래스는 x와 y에 대한 멤버 객체를 로드했습니다:

>>>
from pprint import pp
pp(dict(vars(H)))
{'__module__': '__main__',
 '__doc__': 'Instance variables stored in slots',
 'slot_names': ['x', 'y'],
 '__init__': <function H.__init__ at 0x7fb5d302f9d0>,
 'x': <Member 'x' of 'H'>,
 'y': <Member 'y' of 'H'>}
When instances are created, they have a slot_values list where the attributes are stored:

인스턴스가 생성되면, 속성이 저장되는 slot_values 목록을 가집니다:

>>>
h = H(10, 20)
vars(h)
{'_slotvalues': [10, 20]}
h.x = 55
vars(h)
{'_slotvalues': [55, 20]}
Misspelled or unassigned attributes will raise an exception:

잘못 입력되거나 할당되지 않은 속성은 예외를 발생시킵니다:

>>>
h.xz
Traceback (most recent call last):
    ...
AttributeError: 'H' object has no attribute 'xz'ㄴ