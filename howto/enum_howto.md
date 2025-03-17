# Python Enum How-To Guide (Python Enum 활용 가이드)

## Introduction

1. The `enum` module was added to the standard library in Python 3.4 (PEP 435) to provide a way to create symbolic names (members) that are bound to unique, constant values. An enumeration is a set of symbolic names bound to unique values.

`enum` 모듈은 고유하고 상수인 값에 바인딩된 기호 이름(멤버)을 생성하는 방법을 제공하기 위해 Python 3.4(PEP 435)에서 표준 라이브러리에 추가되었습니다. 열거형은 고유한 값에 바인딩된 기호 이름 집합입니다.

2. Enums are useful when you need to define a set of related constants, improving code readability and providing better type safety compared to using raw strings or integers.

열거형은 관련 상수 집합을 정의해야 할 때 유용하며, 원시 문자열이나 정수를 사용하는 것보다 코드 가독성을 향상시키고 더 나은 타입 안전성을 제공합니다.

## Basic Usage

3. To create an enumeration, you can use the `Enum` class from the `enum` module:

열거형을 생성하려면 `enum` 모듈에서 `Enum` 클래스를 사용할 수 있습니다:

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

4. This creates a new enumeration class with three members: RED, GREEN, and BLUE. Each member has a name and a value:

이것은 RED, GREEN, BLUE 세 멤버를 가진 새로운 열거형 클래스를 생성합니다. 각 멤버는 이름과 값을 가집니다:

```python
>>> Color.RED
<Color.RED: 1>
>>> Color.GREEN
<Color.GREEN: 2>
>>> Color.RED.name
'RED'
>>> Color.RED.value
1
```

## Accessing Enum Members

5. There are several ways to access enum members:

열거형 멤버에 접근하는 여러 가지 방법이 있습니다:

```python
# By attribute
color = Color.RED

# By value (returns the member with that value)
same_color = Color(1)
assert color is same_color

# By name (using string)
also_red = Color['RED']
assert color is also_red
```

6. Enum members are hashable, so they can be used as dictionary keys:

열거형 멤버는 해시 가능하므로 딕셔너리 키로 사용될 수 있습니다:

```python
colors_rgb = {
    Color.RED: (255, 0, 0),
    Color.GREEN: (0, 255, 0),
    Color.BLUE: (0, 0, 255)
}

print(colors_rgb[Color.RED])  # (255, 0, 0)
```

## Iteration and Comparison

7. Enum classes are iterable, allowing you to loop through their members:

열거형 클래스는 반복 가능하므로 멤버를 반복할 수 있습니다:

```python
for color in Color:
    print(color)
# Output:
# Color.RED
# Color.GREEN
# Color.BLUE
```

8. You can also check if a variable is a member of a specific enum class:

특정 열거형 클래스의 멤버인지 확인할 수도 있습니다:

```python
>>> color = Color.RED
>>> isinstance(color, Color)
True
```

9. Enum members are comparable only to themselves and other members of the same enumeration:

열거형 멤버는 자기 자신과 동일한 열거형의 다른 멤버에만 비교 가능합니다:

```python
>>> Color.RED is Color.RED
True
>>> Color.RED == Color.RED
True
>>> Color.RED == Color.BLUE
False
>>> Color.RED == 1  # Cannot compare to raw values
False

# Ordering is not supported by default
>>> Color.RED < Color.BLUE  
Traceback (most recent call last):
  ...
TypeError: '<' not supported between instances of 'Color' and 'Color'
```

## Auto-Values and Aliases

10. The `auto()` function can be used to automatically assign values to enum members:

`auto()` 함수를 사용하여 열거형 멤버에 값을 자동으로 할당할 수 있습니다:

```python
from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

print(Direction.NORTH.value)  # 1
print(Direction.EAST.value)   # 2
```

11. By default, multiple enum members cannot have the same value. If you try to assign the same value to multiple members, they become aliases:

기본적으로 여러 열거형 멤버는 동일한 값을 가질 수 없습니다. 동일한 값을 여러 멤버에 할당하려고 하면 별칭이 됩니다:

```python
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    CRIMSON = 1  # Alias for RED
```

12. When iterating over a enum, aliases are skipped:

열거형을 반복할 때 별칭은 건너뜁니다:

```python
for color in Color:
    print(color)
# Output:
# Color.RED
# Color.GREEN
# Color.BLUE
```

13. If you need to include aliases in iteration, you can use the `__members__` attribute:

반복에 별칭을 포함해야 하는 경우 `__members__` 속성을 사용할 수 있습니다:

```python
for name, member in Color.__members__.items():
    print(name, member)
# Output:
# RED Color.RED
# GREEN Color.GREEN
# BLUE Color.BLUE
# CRIMSON Color.RED
```

## Specialized Enum Types

### IntEnum

14. `IntEnum` creates enum members that are also integers, allowing comparison with integers:

`IntEnum`은 정수이기도 한 열거형 멤버를 생성하여 정수와의 비교를 허용합니다:

```python
from enum import IntEnum

class Status(IntEnum):
    OK = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404
    SERVER_ERROR = 500

# Can compare with integers
print(Status.OK < 300)  # True
print(Status.NOT_FOUND > Status.OK)  # True

# Can use anywhere an int is expected
def check_status(status_code):
    if status_code == Status.OK:
        return "Everything is fine"
    return "There was an error"

print(check_status(200))  # "Everything is fine"
```

### Flag

15. `Flag` is designed for creating enum members that can be combined using bitwise operations:

`Flag`는 비트 연산을 사용하여 결합할 수 있는 열거형 멤버를 생성하기 위해 설계되었습니다:

```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()      # 1
    WRITE = auto()     # 2
    EXECUTE = auto()   # 4
    ALL = READ | WRITE | EXECUTE  # 7

# Combine flags using bitwise operators
user_permissions = Permission.READ | Permission.WRITE

# Test for flags
if Permission.READ in user_permissions:
    print("User has read permission")

if Permission.EXECUTE in user_permissions:
    print("User does not have execute permission")
else:
    print("User does not have execute permission")

# Output:
# User has read permission
# User does not have execute permission
```

### IntFlag

16. `IntFlag` combines the properties of `IntEnum` and `Flag`, creating integer-based enum members that can be combined with bitwise operations:

`IntFlag`는 `IntEnum`과 `Flag`의 속성을 결합하여 비트 연산으로 결합할 수 있는 정수 기반 열거형 멤버를 생성합니다:

```python
from enum import IntFlag

class FileMode(IntFlag):
    READ = 4
    WRITE = 2
    EXECUTE = 1
    
# Can combine with bitwise operators
mode = FileMode.READ | FileMode.WRITE  # 6

# Can compare directly with integers
if mode & FileMode.READ:  # True
    print("Read permission granted")
```

### Unique and Frozen Decorators

17. The `@unique` decorator ensures that no duplicate values exist in the enumeration:

`@unique` 데코레이터는 열거형에 중복 값이 없도록 보장합니다:

```python
from enum import Enum, unique

@unique
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    # CRIMSON = 1  # This would raise a ValueError
```

18. The `@property` decorator can be used with enum classes to add custom properties to all members:

`@property` 데코레이터를 열거형 클래스와 함께 사용하여 모든 멤버에 사용자 정의 속성을 추가할 수 있습니다:

```python
class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    
    def __init__(self, rgb):
        self.rgb = rgb
        
    @property
    def hex(self):
        return '#{:02x}{:02x}{:02x}'.format(*self.rgb)

print(Color.RED.hex)  # '#ff0000'
```

## Functional API

19. The `enum` module also provides a functional API for creating enumerations:

`enum` 모듈은 열거형을 생성하기 위한 함수형 API도 제공합니다:

```python
from enum import Enum

# Functional API
Animal = Enum('Animal', 'ANT BEE CAT DOG')
# Equivalent to:
# class Animal(Enum):
#     ANT = 1
#     BEE = 2
#     CAT = 3
#     DOG = 4

print(Animal.ANT.value)  # 1

# With custom values
Animal2 = Enum('Animal2', {'ANT': 10, 'BEE': 20, 'CAT': 30, 'DOG': 40})
print(Animal2.ANT.value)  # 10
```

## Programmatic Enum Creation

20. Sometimes you need to create enumerations programmatically. Here's how you can do that:

때로는 프로그래매틱하게 열거형을 생성해야 합니다. 방법은 다음과 같습니다:

```python
from enum import Enum

# Create enum from a dictionary
colors_dict = {'RED': 1, 'GREEN': 2, 'BLUE': 3}
Colors = Enum('Colors', colors_dict)

# Create enum from a list of names (values will be automatically assigned)
sizes_list = ['SMALL', 'MEDIUM', 'LARGE', 'X_LARGE']
Sizes = Enum('Sizes', sizes_list)

print(Colors.RED.value)  # 1
print(Sizes.MEDIUM.value)  # 2
```

## Advanced Customization

21. You can customize enum classes by overriding methods and adding custom behavior:

메서드를 오버라이드하고 사용자 정의 동작을 추가하여 열거형 클래스를 사용자 정의할 수 있습니다:

```python
class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    VENUS   = (4.869e+24, 6.0518e6)
    EARTH   = (5.976e+24, 6.37814e6)
    MARS    = (6.421e+23, 3.3972e6)
    JUPITER = (1.9e+27,   7.1492e7)
    SATURN  = (5.688e+26, 6.0268e7)
    URANUS  = (8.686e+25, 2.5559e7)
    NEPTUNE = (1.024e+26, 2.4746e7)
    
    def __init__(self, mass, radius):
        self.mass = mass        # kg
        self.radius = radius    # meters
    
    @property
    def surface_gravity(self):
        # Universal gravitational constant G
        G = 6.67430e-11  # m^3 kg^-1 s^-2
        return G * self.mass / (self.radius ** 2)
    
    def __str__(self):
        return f'{self.name} has a surface gravity of {self.surface_gravity:.2f} m/s²'

print(Planet.EARTH)  # EARTH has a surface gravity of 9.80 m/s²
```

## Enum Metadata

22. Adding metadata and documentation to enums improves their usability:

열거형에 메타데이터와 문서화를 추가하면 사용성이 향상됩니다:

```python
class HttpStatus(Enum):
    """HTTP Status Codes as defined in RFC 2616"""
    
    # Informational 1xx
    CONTINUE = (100, 'Continue')
    SWITCHING_PROTOCOLS = (101, 'Switching Protocols')
    
    # Successful 2xx
    OK = (200, 'OK')
    CREATED = (201, 'Created')
    
    # Redirection 3xx
    MOVED_PERMANENTLY = (301, 'Moved Permanently')
    FOUND = (302, 'Found')
    
    # Client Error 4xx
    BAD_REQUEST = (400, 'Bad Request')
    UNAUTHORIZED = (401, 'Unauthorized')
    FORBIDDEN = (403, 'Forbidden')
    NOT_FOUND = (404, 'Not Found')
    
    # Server Error 5xx
    INTERNAL_SERVER_ERROR = (500, 'Internal Server Error')
    NOT_IMPLEMENTED = (501, 'Not Implemented')
    
    def __init__(self, code, description):
        self.code = code
        self.description = description
    
    def __str__(self):
        return f'{self.code} {self.description}'
    
    @property
    def is_success(self):
        """Return True if this is a successful status code (2xx)"""
        return 200 <= self.code < 300
    
    @property
    def is_error(self):
        """Return True if this is an error status code (4xx, 5xx)"""
        return self.code >= 400

# Usage
status = HttpStatus.NOT_FOUND
print(status)  # 404 Not Found
print(f"Is success: {status.is_success}")  # Is success: False
print(f"Is error: {status.is_error}")      # Is error: True
```

## Best Practices

23. Use enums to replace constants and magic values in your code. This makes your code more maintainable and self-documenting.

열거형을 사용하여 코드의 상수와 매직 값을 대체하세요. 이는 코드를 더 유지 관리하기 쉽고 자체 문서화되게 만듭니다.

24. Choose appropriate enum types based on your needs:
   - Use `Enum` for most cases
   - Use `IntEnum` when comparing with integers is important
   - Use `Flag` for bit fields and combinations
   - Use `IntFlag` for integer-based bit fields

필요에 따라 적절한 열거형 유형을 선택하세요:
   - 대부분의 경우 `Enum` 사용
   - 정수와의 비교가 중요한 경우 `IntEnum` 사용
   - 비트 필드 및 조합은 `Flag` 사용
   - 정수 기반 비트 필드는 `IntFlag` 사용

25. Use the `@unique` decorator to prevent unintended member value duplication.

의도하지 않은 멤버 값 중복을 방지하려면 `@unique` 데코레이터를 사용하세요.

26. Choose descriptive names for enum members and use uppercase to follow the convention for constants.

열거형 멤버에는 설명적인 이름을 선택하고 상수에 대한 규칙을 따르기 위해 대문자를 사용하세요.

## Real-World Examples

27. Enum for state management in a state machine:

상태 머신의 상태 관리를 위한 열거형:

```python
class State(Enum):
    IDLE = auto()
    RUNNING = auto()
    PAUSED = auto()
    STOPPED = auto()
    ERROR = auto()

class StateMachine:
    def __init__(self):
        self.state = State.IDLE
    
    def start(self):
        if self.state == State.IDLE:
            self.state = State.RUNNING
            return True
        return False
    
    def pause(self):
        if self.state == State.RUNNING:
            self.state = State.PAUSED
            return True
        return False
    
    def resume(self):
        if self.state == State.PAUSED:
            self.state = State.RUNNING
            return True
        return False
    
    def stop(self):
        if self.state in (State.RUNNING, State.PAUSED):
            self.state = State.STOPPED
            return True
        return False

machine = StateMachine()
machine.start()
print(machine.state)  # State.RUNNING
```

28. Enum for configuration options:

구성 옵션을 위한 열거형:

```python
class LogLevel(IntEnum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

class Config:
    def __init__(self):
        self.log_level = LogLevel.INFO
        self.debug_mode = False
    
    def set_log_level(self, level):
        if isinstance(level, LogLevel):
            self.log_level = level
        elif isinstance(level, int):
            try:
                self.log_level = LogLevel(level)
            except ValueError:
                # Find closest valid level
                valid_levels = sorted(item.value for item in LogLevel)
                closest = min(valid_levels, key=lambda x: abs(x - level))
                self.log_level = LogLevel(closest)
        elif isinstance(level, str):
            try:
                self.log_level = LogLevel[level.upper()]
            except KeyError:
                raise ValueError(f"Unknown log level: {level}")
    
    def log(self, level, message):
        if level >= self.log_level:
            print(f"[{LogLevel(level).name}] {message}")

# Usage
config = Config()
config.set_log_level(LogLevel.WARNING)
config.log(LogLevel.INFO, "This won't be logged")    # Not shown
config.log(LogLevel.ERROR, "This will be logged")    # [ERROR] This will be logged

# Can also set by string
config.set_log_level("DEBUG")
config.log(LogLevel.INFO, "Now this will be logged") # [INFO] Now this will be logged
```

## Conclusion

29. Python's enum module provides a powerful way to create constants with named values. Enums help make your code more readable, type-safe, and maintainable by replacing magic numbers and strings with meaningful names.

Python의 enum 모듈은 명명된 값을 가진 상수를 생성하는 강력한 방법을 제공합니다. 열거형은 매직 넘버와 문자열을 의미 있는 이름으로 대체하여 코드를 더 읽기 쉽고, 타입 안전하며, 유지 관리하기 쉽게 만듭니다.

30. By leveraging the different types of enumerations (`Enum`, `IntEnum`, `Flag`, `IntFlag`) and their features, you can create cleaner interfaces and more robust code that clearly communicates its intent.

다양한 유형의 열거형(`Enum`, `IntEnum`, `Flag`, `IntFlag`)과 그 기능을 활용함으로써, 의도를 명확히 전달하는 더 깔끔한 인터페이스와 견고한 코드를 만들 수 있습니다.
