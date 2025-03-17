# Python Descriptor Guide (Python 디스크립터 가이드)

## Introduction

1. Descriptors are a powerful feature in Python that allows you to customize what happens when an attribute is accessed, modified, or deleted. They're the mechanism behind many of Python's built-in features such as properties, methods, class methods, and static methods.

디스크립터는 속성에 접근하거나, 수정하거나, 삭제할 때 어떤 일이 일어나는지 사용자 정의할 수 있게 해주는 Python의 강력한 기능입니다. 디스크립터는 프로퍼티, 메서드, 클래스 메서드, 정적 메서드와 같은 Python 내장 기능의 기반이 되는 메커니즘입니다.

2. This guide explores descriptors in detail, from basic concepts to advanced usage patterns, helping you understand and leverage this feature in your own code.

이 가이드는 디스크립터를 기본 개념부터 고급 사용 패턴까지 자세히 살펴보고, 자신의 코드에서 이 기능을 이해하고 활용하는 데 도움을 줍니다.

## Understanding Descriptors

3. A descriptor is any object that implements at least one of the methods in the descriptor protocol: `__get__`, `__set__`, or `__delete__`. These methods allow you to control what happens when attributes are accessed, modified, or deleted.

디스크립터는 디스크립터 프로토콜의 메서드 중 하나 이상을 구현하는 모든 객체입니다: `__get__`, `__set__` 또는 `__delete__`. 이 메서드들은 속성에 접근하거나, 수정하거나, 삭제할 때 어떤 일이 일어나는지 제어할 수 있게 해줍니다.

4. The descriptor protocol methods are defined as follows:

디스크립터 프로토콜 메서드는 다음과 같이 정의됩니다:

```python
__get__(self, obj, type=None) -> value
__set__(self, obj, value) -> None
__delete__(self, obj) -> None
```

5. When a descriptor is assigned to a class attribute, its special methods will be invoked for any reference to that attribute by instances of the class.

디스크립터가 클래스 속성에 할당되면, 해당 클래스의 인스턴스에 의한 그 속성에 대한 모든 참조에 대해 특수 메서드가 호출됩니다.

## Basic Descriptor Example

6. Let's start with a simple descriptor example:

간단한 디스크립터 예제로 시작해 보겠습니다:

```python
class Verbose:
    def __get__(self, obj, objtype=None):
        print(f"Getting {self.__class__.__name__}")
        return 42
    
    def __set__(self, obj, value):
        print(f"Setting {self.__class__.__name__} to {value}")
    
    def __delete__(self, obj):
        print(f"Deleting {self.__class__.__name__}")

class MyClass:
    x = Verbose()  # Descriptor instance as class attribute

# Using the descriptor
instance = MyClass()
print(instance.x)   # Calls __get__
instance.x = 10     # Calls __set__
del instance.x      # Calls __delete__
```

7. When you run this code, you'll see output showing each descriptor method being called:

이 코드를 실행하면 각 디스크립터 메서드가 호출되는 것을 보여주는 출력이 표시됩니다:

```
Getting Verbose
42
Setting Verbose to 10
Deleting Verbose
```

## Data vs. Non-Data Descriptors

8. Descriptors are categorized as either data or non-data descriptors:

디스크립터는 데이터 디스크립터와 비데이터 디스크립터로 분류됩니다:

9. **Data Descriptors**: Implement both `__get__` and `__set__` methods. They take precedence over instance dictionary entries.

**데이터 디스크립터**: `__get__`과 `__set__` 메서드를 모두 구현합니다. 인스턴스 사전 항목보다 우선합니다.

10. **Non-Data Descriptors**: Implement only `__get__`. Instance dictionary entries take precedence over non-data descriptors.

**비데이터 디스크립터**: `__get__`만 구현합니다. 인스턴스 사전 항목이 비데이터 디스크립터보다 우선합니다.

11. This distinction is important for understanding method resolution order in Python:

이 구분은 Python의 메서드 해석 순서를 이해하는 데 중요합니다:

```python
class NonDataDescriptor:
    def __get__(self, obj, objtype=None):
        return "Non-data descriptor"

class DataDescriptor:
    def __get__(self, obj, objtype=None):
        return "Data descriptor"
    
    def __set__(self, obj, value):
        pass  # Just having this makes it a data descriptor

class MyClass:
    non_data = NonDataDescriptor()
    data = DataDescriptor()

instance = MyClass()
instance.__dict__['non_data'] = "Instance attribute"
instance.__dict__['data'] = "Instance attribute"

print(instance.non_data)  # Will print "Instance attribute"
print(instance.data)      # Will print "Data descriptor"
```

## Application: Type Validation

12. One common use of descriptors is attribute type validation:

디스크립터의 일반적인 사용 중 하나는 속성 타입 검증입니다:

```python
class Typed:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__[self.name]
    
    def __set__(self, obj, value):
        if not isinstance(value, self.type):
            raise TypeError(f"Expected {self.type}, got {type(value)}")
        obj.__dict__[self.name] = value

class Person:
    name = Typed("name", str)
    age = Typed("age", int)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# This works
person = Person("John", 30)

# This raises TypeError
try:
    person.age = "thirty"
except TypeError as e:
    print(e)  # Expected <class 'int'>, got <class 'str'>
```

## Descriptors in Python's Built-in Features

13. Many of Python's built-in features use descriptors behind the scenes:

Python의 많은 내장 기능은 뒤에서 디스크립터를 사용합니다:

14. **Properties**: The `property` built-in is a descriptor:

**프로퍼티**: `property` 내장 함수는 디스크립터입니다:

```python
class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value
```

15. **Methods**: Functions in a class become method descriptors:

**메서드**: 클래스 내의 함수는 메서드 디스크립터가 됩니다:

```python
class MyClass:
    def method(self):  # This is actually a descriptor
        return "method called"

print(MyClass.method)  # <function MyClass.method at ...>
print(MyClass().method)  # method called
```

16. **Class and Static Methods**: The `classmethod` and `staticmethod` decorators create descriptors:

**클래스 및 정적 메서드**: `classmethod` 및 `staticmethod` 데코레이터는 디스크립터를 생성합니다:

```python
class MyClass:
    @classmethod
    def class_method(cls):
        return f"Class method of {cls.__name__}"
    
    @staticmethod
    def static_method():
        return "Static method"
```

## Advanced Usage: Cached Properties

17. Descriptors can be used to create efficient caching properties:

디스크립터를 사용하여 효율적인 캐싱 프로퍼티를 만들 수 있습니다:

```python
class cached_property:
    def __init__(self, func):
        self.func = func
        self.__doc__ = func.__doc__
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = self.func(obj)
        obj.__dict__[self.func.__name__] = value  # Cache the result
        return value

class ExpensiveCalculation:
    def __init__(self, data):
        self.data = data
    
    @cached_property
    def result(self):
        print("Performing expensive calculation...")
        # Simulate expensive computation
        import time
        time.sleep(1)
        return sum(self.data)

calc = ExpensiveCalculation([1, 2, 3, 4, 5])
print(calc.result)  # First access: slow (calculates and caches)
print(calc.result)  # Second access: fast (uses cached value)
```

## Managing Instance Attributes

18. A key challenge with descriptors is managing instance attributes. There are several approaches:

디스크립터의 주요 과제 중 하나는 인스턴스 속성 관리입니다. 여러 가지 접근 방식이 있습니다:

19. **Using instance dict**: Store values in the instance's `__dict__` using a unique key:

**인스턴스 dict 사용**: 고유한 키를 사용하여 인스턴스의 `__dict__`에 값을 저장합니다:

```python
class Descriptor:
    def __init__(self, name=None):
        self.name = name
    
    def __set_name__(self, owner, name):
        # This is called when the descriptor is defined in a class
        # Automatically sets the name if not explicitly provided
        if self.name is None:
            self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        obj.__dict__[self.name] = value
```

20. **Using per-instance storage**: An alternative is to use a separate storage for each descriptor:

**인스턴스별 저장소 사용**: 대안은 각 디스크립터에 대해 별도의 저장소를 사용하는 것입니다:

```python
class Descriptor:
    def __init__(self):
        self.storage = WeakKeyDictionary()
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self.storage.get(obj)
    
    def __set__(self, obj, value):
        self.storage[obj] = value
```

## The `__set_name__` Method

21. Python 3.6 introduced the `__set_name__` method to the descriptor protocol, which is automatically called at the time a descriptor is assigned to a class variable:

Python 3.6은 디스크립터 프로토콜에 `__set_name__` 메서드를 도입했습니다. 이 메서드는 디스크립터가 클래스 변수에 할당될 때 자동으로 호출됩니다:

```python
class Field:
    def __set_name__(self, owner, name):
        print(f"Descriptor {self} assigned to {owner} with name '{name}'")
        self.name = name

class Model:
    first_name = Field()
    last_name = Field()

# Creating a Model class automatically calls __set_name__ on both Field instances
```

22. This makes it easier to create descriptors that automatically know their attribute names:

이를 통해 속성 이름을 자동으로 알고 있는 디스크립터를 더 쉽게 만들 수 있습니다:

## Implementing Custom Attribute Access

23. Combining descriptors with `__getattribute__` allows for powerful custom attribute access patterns:

디스크립터와 `__getattribute__`를 결합하면 강력한 사용자 정의 속성 접근 패턴을 만들 수 있습니다:

```python
class Model:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __getattribute__(self, name):
        # Special processing before the regular attribute lookup
        print(f"Accessing {name}")
        return super().__getattribute__(name)

class Field:
    def __init__(self, default=None):
        self.default = default
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, self.default)
    
    def __set__(self, obj, value):
        obj.__dict__[self.name] = value

class User(Model):
    name = Field(default="Anonymous")
    age = Field(default=0)

user = User(name="John")
print(user.name)  # Outputs: Accessing name, then John
print(user.age)   # Outputs: Accessing age, then 0
```

## Best Practices

24. Here are some best practices when working with descriptors:

디스크립터로 작업할 때 몇 가지 모범 사례는 다음과 같습니다:

25. **Use `__set_name__`** when possible to automatically capture the attribute name.

가능하면 속성 이름을 자동으로 캡처하기 위해 **`__set_name__`을 사용하세요**.

26. **Be aware of method resolution order**: Data descriptors take precedence over instance attributes, but non-data descriptors don't.

**메서드 해석 순서를 알고 있어야 합니다**: 데이터 디스크립터는 인스턴스 속성보다 우선하지만, 비데이터 디스크립터는 그렇지 않습니다.

27. **Decide on a storage strategy**: Choose between instance dictionary, per-descriptor storage, or other options based on your specific needs.

**저장소 전략을 결정하세요**: 특정 요구 사항에 따라 인스턴스 딕셔너리, 디스크립터별 저장소 또는 다른 옵션 중 선택하세요.

28. **Document behavior**: Make sure users of your classes understand the descriptor behavior, especially when it might not be obvious.

**동작을 문서화하세요**: 특히 명확하지 않을 수 있는 경우, 클래스 사용자가 디스크립터 동작을 이해하도록 하세요.

29. **Use properties for simple cases**: If you just need getters and setters, the built-in `property` decorator is often simpler than writing a full descriptor class.

**간단한 경우에는 프로퍼티를 사용하세요**: 단순히 게터와 세터가 필요한 경우, 내장된 `property` 데코레이터는 종종 전체 디스크립터 클래스를 작성하는 것보다 더 간단합니다.

## Real-World Example: ORM-Like System

30. Here's a more substantial example showing how descriptors can be used to create an ORM-like system:

여기에 디스크립터를 사용하여 ORM과 유사한 시스템을 만드는 방법을 보여주는 보다 실질적인 예가 있습니다:

```python
class Field:
    def __init__(self, field_type, required=False, default=None):
        self.field_type = field_type
        self.required = required
        self.default = default
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, self.default)
    
    def __set__(self, obj, value):
        if value is None and self.required:
            raise ValueError(f"{self.name} is required")
        if value is not None and not isinstance(value, self.field_type):
            raise TypeError(f"{self.name} must be of type {self.field_type.__name__}")
        obj.__dict__[self.name] = value

class ModelMeta(type):
    def __new__(mcs, name, bases, attrs):
        fields = {key: value for key, value in attrs.items() 
                 if isinstance(value, Field)}
        attrs['_fields'] = fields
        return super().__new__(mcs, name, bases, attrs)

class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for field_name, field in self._fields.items():
            value = kwargs.get(field_name, field.default)
            setattr(self, field_name, value)
    
    def validate(self):
        for field_name, field in self._fields.items():
            value = getattr(self, field_name)
            if field.required and value is None:
                raise ValueError(f"{field_name} is required")
    
    def to_dict(self):
        return {field_name: getattr(self, field_name) 
                for field_name in self._fields}

# Example usage
class User(Model):
    name = Field(str, required=True)
    email = Field(str, required=True)
    age = Field(int, default=0)

# Create a valid user
user = User(name="John Doe", email="john@example.com", age=30)
print(user.to_dict())

# This will raise a ValueError because email is required
try:
    invalid_user = User(name="Jane Doe")
    invalid_user.validate()
except ValueError as e:
    print(f"Validation error: {e}")

# This will raise a TypeError because age should be an integer
try:
    user_with_wrong_age = User(name="Bob", email="bob@example.com", age="twenty")
except TypeError as e:
    print(f"Type error: {e}")
```

## Conclusion

31. Descriptors are a powerful feature in Python that enables fine-grained control over attribute access. They are the foundation for many of Python's built-in features and can be used to create elegant, reusable solutions for your own code.

디스크립터는 Python의 강력한 기능으로, 속성 접근에 대한 세밀한 제어를 가능하게 합니다. 디스크립터는 Python 내장 기능의 기반이며, 자신의 코드에 대한 우아하고 재사용 가능한 솔루션을 만드는 데 사용될 수 있습니다.

32. Understanding descriptors enhances your understanding of how Python works and gives you more options for designing clean, expressive APIs. While they can be complex, descriptors are worth mastering for any Python developer working on libraries or frameworks.

디스크립터를 이해하면 Python이 작동하는 방식에 대한 이해가 향상되고 깨끗하고 표현력 있는 API를 설계하는 데 더 많은 옵션을 제공합니다. 디스크립터는 복잡할 수 있지만, 라이브러리나 프레임워크를 작업하는 모든 Python 개발자가 숙달할 가치가 있습니다.
