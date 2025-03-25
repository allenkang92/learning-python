# Enum HowTo Guide

# Enum 사용 가이드

## Introduction to Enums

An enumeration is a set of symbolic names bound to unique, constant values. Within an enumeration, the values can be compared by identity, and the enumeration itself can be iterated over. Enumerations were added to Python in version 3.4 through [PEP 435](https://www.python.org/dev/peps/pep-0435/).

## Enum 소개

열거형(enumeration)은 고유하고 상수인 값에 바인딩된 기호 이름의 집합입니다. 열거형 내에서 값은 ID로 비교할 수 있으며, 열거형 자체를 반복할 수 있습니다. 열거형은 [PEP 435](https://www.python.org/dev/peps/pep-0435/)를 통해 Python 3.4 버전에 추가되었습니다.

## Module Contents

The `enum` module defines the following enumerations:

* `Enum`: Base class for creating enumerated constants
* `IntEnum`: Base class for creating enumerated constants that are also subclasses of `int`
* `IntFlag`: Base class for creating enumerated constants that can be combined using the bitwise operations
* `Flag`: Base class for creating enumerated constants that can be combined using the bitwise operations without an inherited `int` type
* `auto`: Provides values for enumerations based on a counter
* `unique`: Decorator that ensures only one name is bound to any one value
* `EnumType`: The metaclass for Enum

## 모듈 내용

`enum` 모듈은 다음 열거형들을 정의합니다:

* `Enum`: 열거된 상수를 만들기 위한 기본 클래스
* `IntEnum`: `int`의 서브클래스이기도 한 열거된 상수를 만들기 위한 기본 클래스
* `IntFlag`: 비트 단위 연산자를 사용하여 결합할 수 있는 열거된 상수를 만들기 위한 기본 클래스
* `Flag`: 상속된 `int` 타입 없이 비트 단위 연산자를 사용하여 결합할 수 있는 열거된 상수를 만들기 위한 기본 클래스
* `auto`: 카운터를 기반으로 열거형에 값을 제공합니다
* `unique`: 하나의 값에 하나의 이름만 바인딩되도록 보장하는 데코레이터
* `EnumType`: Enum의 메타클래스

## Creating an Enum

Enumerations are created using the `class` syntax, which makes them easy to read and write. An alternative creation method is described in the "Functional API" section. To define an enumeration, subclass `Enum` as follows:

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

## Enum 생성하기

열거형은 `class` 구문을 사용하여 생성되므로 읽고 쓰기가 쉽습니다. 대체 생성 방법은 "함수형 API" 섹션에 설명되어 있습니다. 열거형을 정의하려면 다음과 같이 `Enum`을 상속받으세요:

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

## Accessing Enum Members

Enum members can be accessed by:
1. Their name as an attribute
2. Iteration
3. Their value using a lookup

```python
# By name
blue = Color.BLUE
print(blue)  # Color.BLUE

# By iteration
for color in Color:
    print(color)
# Output:
# Color.RED
# Color.GREEN
# Color.BLUE

# By value
blue_by_value = Color(3)
print(blue_by_value)  # Color.BLUE
```

## Enum 멤버 접근하기

Enum 멤버는 다음과 같은 방법으로 접근할 수 있습니다:
1. 속성으로서의 이름
2. 반복
3. 값을 사용한 조회

```python
# 이름으로
blue = Color.BLUE
print(blue)  # Color.BLUE

# 반복으로
for color in Color:
    print(color)
# 출력:
# Color.RED
# Color.GREEN
# Color.BLUE

# 값으로
blue_by_value = Color(3)
print(blue_by_value)  # Color.BLUE
```

## Enum Member Properties

Enum members have properties that you can access:
* `.name`: The name of the member
* `.value`: The value assigned to the member

```python
print(Color.RED.name)  # RED
print(Color.RED.value)  # 1
```

## Enum 멤버 속성

Enum 멤버에는 접근할 수 있는 속성이 있습니다:
* `.name`: 멤버의 이름
* `.value`: 멤버에 할당된 값

```python
print(Color.RED.name)  # RED
print(Color.RED.value)  # 1
```

## Comparisons

Enum members are compared by identity, not by value:

```python
print(Color.RED is Color.RED)  # True
print(Color.RED is Color.BLUE)  # False
print(Color.RED == Color.RED)  # True
print(Color.RED == Color.BLUE)  # False
print(Color.RED == 1)  # False
```

To compare by value, create an `IntEnum`:

```python
from enum import IntEnum

class Size(IntEnum):
    S = 1
    M = 2
    L = 3

print(Size.S == 1)  # True
```

## 비교

Enum 멤버는 값이 아닌 ID로 비교됩니다:

```python
print(Color.RED is Color.RED)  # True
print(Color.RED is Color.BLUE)  # False
print(Color.RED == Color.RED)  # True
print(Color.RED == Color.BLUE)  # False
print(Color.RED == 1)  # False
```

값으로 비교하려면 `IntEnum`을 만드세요:

```python
from enum import IntEnum

class Size(IntEnum):
    S = 1
    M = 2
    L = 3

print(Size.S == 1)  # True
```

## Ensuring Unique Values

By default, Enum allows multiple names to have the same value. If you want to ensure unique values, use the `@unique` decorator:

```python
from enum import Enum, unique

@unique
class Status(Enum):
    PENDING = 1
    RUNNING = 2
    COMPLETED = 3
    # ERROR = 3  # This would raise a ValueError
```

## 고유한 값 보장하기

기본적으로 Enum은 여러 이름이 같은 값을 가질 수 있습니다. 고유한 값을 보장하려면 `@unique` 데코레이터를 사용하세요:

```python
from enum import Enum, unique

@unique
class Status(Enum):
    PENDING = 1
    RUNNING = 2
    COMPLETED = 3
    # ERROR = 3  # 이렇게 하면 ValueError가 발생합니다
```

## Automatic Values with auto()

If you don't care about the specific values and just need unique values, use `auto()`:

```python
from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

print(list(Direction))
# [<Direction.NORTH: 1>, <Direction.SOUTH: 2>, <Direction.EAST: 3>, <Direction.WEST: 4>]
```

## auto()를 사용한 자동 값

특정 값에 신경 쓰지 않고 고유한 값만 필요한 경우 `auto()`를 사용하세요:

```python
from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

print(list(Direction))
# [<Direction.NORTH: 1>, <Direction.SOUTH: 2>, <Direction.EAST: 3>, <Direction.WEST: 4>]
```

## Customizing auto() Values

You can customize how `auto()` chooses values by implementing `_generate_next_value_` in your enum class:

```python
from enum import Enum, auto

class CustomAuto(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

class Element(CustomAuto):
    FIRE = auto()
    WATER = auto()
    EARTH = auto()
    AIR = auto()

print(Element.FIRE.value)  # "fire"
```

## auto() 값 사용자 정의하기

열거형 클래스에서 `_generate_next_value_`를 구현하여 `auto()`가 값을 선택하는 방법을 사용자 정의할 수 있습니다:

```python
from enum import Enum, auto

class CustomAuto(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

class Element(CustomAuto):
    FIRE = auto()
    WATER = auto()
    EARTH = auto()
    AIR = auto()

print(Element.FIRE.value)  # "fire"
```

## Composite Enums with Flag

The `Flag` enum type allows for creating enumeration values that can be combined using the bitwise operations (`|`, `&`, `^`):

```python
from enum import Flag, auto

class Permissions(Flag):
    NONE = 0
    READ = auto()      # 1
    WRITE = auto()     # 2
    EXECUTE = auto()   # 4
    
    ALL = READ | WRITE | EXECUTE

# Combining permissions
read_write = Permissions.READ | Permissions.WRITE
print(read_write)  # Permissions.READ|WRITE

# Checking permissions
print(Permissions.READ in read_write)  # True
print(Permissions.EXECUTE in read_write)  # False
```

## Flag를 사용한 복합 열거형

`Flag` 열거형 타입을 사용하면 비트 단위 연산(`|`, `&`, `^`)을 사용하여 결합할 수 있는 열거형 값을 만들 수 있습니다:

```python
from enum import Flag, auto

class Permissions(Flag):
    NONE = 0
    READ = auto()      # 1
    WRITE = auto()     # 2
    EXECUTE = auto()   # 4
    
    ALL = READ | WRITE | EXECUTE

# 권한 결합하기
read_write = Permissions.READ | Permissions.WRITE
print(read_write)  # Permissions.READ|WRITE

# 권한 확인하기
print(Permissions.READ in read_write)  # True
print(Permissions.EXECUTE in read_write)  # False
```

## Using IntFlag for Integer Operations

`IntFlag` is similar to `Flag` but it also inherits from `int` and supports all integer operations:

```python
from enum import IntFlag, auto

class FileMode(IntFlag):
    READ = auto()      # 1
    WRITE = auto()     # 2
    EXECUTE = auto()   # 4
    
    # IntFlag members can be used in integer contexts
    DEFAULT = READ | WRITE  # 3

# Using in integer operations
print(FileMode.READ + 1)  # 2
print(FileMode.DEFAULT * 2)  # 6
```

## 정수 연산을 위한 IntFlag 사용하기

`IntFlag`는 `Flag`와 유사하지만 `int`를 상속받고 모든 정수 연산을 지원합니다:

```python
from enum import IntFlag, auto

class FileMode(IntFlag):
    READ = auto()      # 1
    WRITE = auto()     # 2
    EXECUTE = auto()   # 4
    
    # IntFlag 멤버는 정수 컨텍스트에서 사용될 수 있습니다
    DEFAULT = READ | WRITE  # 3

# 정수 연산에서 사용하기
print(FileMode.READ + 1)  # 2
print(FileMode.DEFAULT * 2)  # 6
```

## Extending Enums with Methods

You can add methods to an enum just like any other class:

```python
class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    VENUS   = (4.869e+24, 6.0518e6)
    EARTH   = (5.976e+24, 6.37814e6)
    MARS    = (6.421e+23, 3.3972e6)
    
    def __init__(self, mass, radius):
        self.mass = mass       # kg
        self.radius = radius   # meters
    
    @property
    def surface_gravity(self):
        # gravitational constant G
        G = 6.67430e-11  # m³ kg⁻¹ s⁻²
        return G * self.mass / (self.radius * self.radius)
        
print(Planet.EARTH.surface_gravity)  # 9.80665...
```

## 메서드로 Enum 확장하기

다른 클래스처럼 열거형에 메서드를 추가할 수 있습니다:

```python
class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    VENUS   = (4.869e+24, 6.0518e6)
    EARTH   = (5.976e+24, 6.37814e6)
    MARS    = (6.421e+23, 3.3972e6)
    
    def __init__(self, mass, radius):
        self.mass = mass       # kg
        self.radius = radius   # meters
    
    @property
    def surface_gravity(self):
        # 중력 상수 G
        G = 6.67430e-11  # m³ kg⁻¹ s⁻²
        return G * self.mass / (self.radius * self.radius)
        
print(Planet.EARTH.surface_gravity)  # 9.80665...
```

## Functional API

The `Enum` class also has a functional API that can be used to create enumerations:

```python
from enum import Enum

# The first argument is the name of the enum
# The second argument can be:
# 1. A string of comma-separated names: 'RED, GREEN, BLUE'
# 2. A list of names: ['RED', 'GREEN', 'BLUE']
# 3. A dict mapping names to values: {'RED': 1, 'GREEN': 2, 'BLUE': 3}

# Using a string
Colors = Enum('Colors', 'RED GREEN BLUE')

# Using a list
Shapes = Enum('Shapes', ['CIRCLE', 'SQUARE', 'TRIANGLE'])

# Using a dict
Sizes = Enum('Sizes', {'SMALL': 1, 'MEDIUM': 2, 'LARGE': 3})

print(Colors.RED.value)  # 1
print(Shapes.CIRCLE.value)  # 1
print(Sizes.SMALL.value)  # 1
```

## 함수형 API

`Enum` 클래스에는 열거형을 만드는 데 사용할 수 있는 함수형 API도 있습니다:

```python
from enum import Enum

# 첫 번째 인수는 열거형의 이름입니다
# 두 번째 인수는 다음 중 하나일 수 있습니다:
# 1. 쉼표로 구분된 이름 문자열: 'RED, GREEN, BLUE'
# 2. 이름 목록: ['RED', 'GREEN', 'BLUE']
# 3. 이름과 값을 매핑하는 dict: {'RED': 1, 'GREEN': 2, 'BLUE': 3}

# 문자열 사용
Colors = Enum('Colors', 'RED GREEN BLUE')

# 리스트 사용
Shapes = Enum('Shapes', ['CIRCLE', 'SQUARE', 'TRIANGLE'])

# Dict 사용
Sizes = Enum('Sizes', {'SMALL': 1, 'MEDIUM': 2, 'LARGE': 3})

print(Colors.RED.value)  # 1
print(Shapes.CIRCLE.value)  # 1
print(Sizes.SMALL.value)  # 1
```

## Aliasing Enum Members

If multiple enum members have the same value, the duplicates become aliases of the first name:

```python
from enum import Enum

class Status(Enum):
    PENDING = 1
    STARTED = 1  # Alias for PENDING
    RUNNING = 2
    FINISHED = 3
    COMPLETED = 3  # Alias for FINISHED

print(Status.PENDING is Status.STARTED)  # True
print(Status.PENDING.name)  # PENDING
print(Status.STARTED.name)  # STARTED
print(Status.PENDING == Status.STARTED)  # True
```

To iterate over only unique enum members (skipping aliases), use `__members__`:

```python
for status in Status:
    print(status)
# Status.PENDING
# Status.RUNNING
# Status.FINISHED

# To include aliases, use __members__
for name, member in Status.__members__.items():
    print(name, member)
# PENDING Status.PENDING
# STARTED Status.PENDING
# RUNNING Status.RUNNING
# FINISHED Status.FINISHED
# COMPLETED Status.FINISHED
```

## Enum 멤버 별칭 지정하기

여러 열거형 멤버가 동일한 값을 가지면 중복은 첫 번째 이름의 별칭이 됩니다:

```python
from enum import Enum

class Status(Enum):
    PENDING = 1
    STARTED = 1  # PENDING의 별칭
    RUNNING = 2
    FINISHED = 3
    COMPLETED = 3  # FINISHED의 별칭

print(Status.PENDING is Status.STARTED)  # True
print(Status.PENDING.name)  # PENDING
print(Status.STARTED.name)  # STARTED
print(Status.PENDING == Status.STARTED)  # True
```

고유한 열거형 멤버만 반복하려면(별칭 건너뛰기) `__members__`를 사용하세요:

```python
for status in Status:
    print(status)
# Status.PENDING
# Status.RUNNING
# Status.FINISHED

# 별칭을 포함하려면 __members__를 사용하세요
for name, member in Status.__members__.items():
    print(name, member)
# PENDING Status.PENDING
# STARTED Status.PENDING
# RUNNING Status.RUNNING
# FINISHED Status.FINISHED
# COMPLETED Status.FINISHED
```

## Programmatically Accessing Enum Members

Enum classes have a `__members__` attribute that maps names to members, providing dictionary-like access:

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Access a member by name
print(Color.__members__["RED"])  # Color.RED

# Iterate through all members
for name, member in Color.__members__.items():
    print(name, member, member.value)
# RED Color.RED 1
# GREEN Color.GREEN 2
# BLUE Color.BLUE 3
```

## 프로그래밍 방식으로 Enum 멤버에 접근하기

Enum 클래스에는 이름을 멤버에 매핑하는 `__members__` 속성이 있어 사전과 같은 접근을 제공합니다:

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# 이름으로 멤버에 접근하기
print(Color.__members__["RED"])  # Color.RED

# 모든 멤버를 반복하기
for name, member in Color.__members__.items():
    print(name, member, member.value)
# RED Color.RED 1
# GREEN Color.GREEN 2
# BLUE Color.BLUE 3
```

## Using Enums with Dataclasses

Enums work well with dataclasses for type-safe structured data:

```python
from enum import Enum, auto
from dataclasses import dataclass

class TaskStatus(Enum):
    TODO = auto()
    IN_PROGRESS = auto()
    DONE = auto()

@dataclass
class Task:
    id: int
    name: str
    status: TaskStatus
    
task = Task(1, "Write documentation", TaskStatus.TODO)
print(task)
# Task(id=1, name='Write documentation', status=<TaskStatus.TODO: 1>)

# Update the task status
task.status = TaskStatus.IN_PROGRESS
```

## 데이터클래스와 함께 Enum 사용하기

Enum은 타입 안전한 구조화된 데이터를 위해 데이터클래스와 잘 작동합니다:

```python
from enum import Enum, auto
from dataclasses import dataclass

class TaskStatus(Enum):
    TODO = auto()
    IN_PROGRESS = auto()
    DONE = auto()

@dataclass
class Task:
    id: int
    name: str
    status: TaskStatus
    
task = Task(1, "Write documentation", TaskStatus.TODO)
print(task)
# Task(id=1, name='Write documentation', status=<TaskStatus.TODO: 1>)

# 작업 상태 업데이트하기
task.status = TaskStatus.IN_PROGRESS
```

## Enum with Type Hints

You can use enums with type hints for clearer code:

```python
from enum import Enum, auto
from typing import List, Dict

class UserRole(Enum):
    ADMIN = auto()
    EDITOR = auto()
    VIEWER = auto()

def check_access(user_id: int, role: UserRole) -> bool:
    """Check if a user has the required role."""
    # Some logic here
    return True

# In usage
user_role = UserRole.EDITOR
if check_access(42, user_role):
    print("Access granted")
```

## 타입 힌트와 함께 Enum 사용하기

더 명확한 코드를 위해 타입 힌트와 함께 열거형을 사용할 수 있습니다:

```python
from enum import Enum, auto
from typing import List, Dict

class UserRole(Enum):
    ADMIN = auto()
    EDITOR = auto()
    VIEWER = auto()

def check_access(user_id: int, role: UserRole) -> bool:
    """사용자가 필요한 역할을 가지고 있는지 확인합니다."""
    # 여기에 로직이 있습니다
    return True

# 사용 예
user_role = UserRole.EDITOR
if check_access(42, user_role):
    print("접근 허용됨")
```

## Pickle Support

Enum members are picklable, which makes them suitable for serialization and data persistence:

```python
import pickle
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Pickle an enum member
serialized = pickle.dumps(Color.RED)
print(serialized)  # b'\x80\x04\x95...'

# Unpickle back to the same object
deserialized = pickle.loads(serialized)
print(deserialized)  # Color.RED
print(deserialized is Color.RED)  # True
```

## 피클 지원

Enum 멤버는 피클링 가능하므로 직렬화 및 데이터 지속성에 적합합니다:

```python
import pickle
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Enum 멤버 피클링하기
serialized = pickle.dumps(Color.RED)
print(serialized)  # b'\x80\x04\x95...'

# 동일한 객체로 다시 언피클링하기
deserialized = pickle.loads(serialized)
print(deserialized)  # Color.RED
print(deserialized is Color.RED)  # True
```

## Note Case of Enum Members

Because Enums are used to represent constants, and to help avoid issues with name clashes between mixin-class methods/attributes and enum names, we strongly recommend using UPPER_CASE names for members, and will be using that style in our examples.

Depending on the nature of the enum a member’s value may or may not be important, but either way that value can be used to get the corresponding member:

```python
Weekday(3)
<Weekday.WEDNESDAY: 3>
```

As you can see, the repr() of a member shows the enum name, the member name, and the value. The str() of a member shows only the enum name and member name:

```python
print(Weekday.THURSDAY)
Weekday.THURSDAY
```

## Enum 멤버의 표기법 참고사항

열거형은 상수를 나타내는 데 사용되며, 믹스인 클래스 메서드/속성과 열거형 이름 간의 이름 충돌 문제를 방지하기 위해, 우리는 멤버에 대해 대문자(UPPER_CASE) 이름 사용을 강력히 권장하며, 예제에서도 이 스타일을 사용할 것입니다.

열거형의 특성에 따라 멤버의 값이 중요할 수도 있고 그렇지 않을 수도 있지만, 어느 경우든 해당 값을 사용하여 해당 멤버를 가져올 수 있습니다:

```python
Weekday(3)
<Weekday.WEDNESDAY: 3>
```

보시다시피, 멤버의 repr()은 열거형 이름, 멤버 이름 및 값을 보여줍니다. 멤버의 str()은 열거형 이름과 멤버 이름만 보여줍니다:

```python
print(Weekday.THURSDAY)
Weekday.THURSDAY
```

The type of an enumeration member is the enum it belongs to:

```python
type(Weekday.MONDAY)
<enum 'Weekday'>
isinstance(Weekday.FRIDAY, Weekday)
True
```

Enum members have an attribute that contains just their name:

```python
print(Weekday.TUESDAY.name)
TUESDAY
```

Likewise, they have an attribute for their value:

```python
Weekday.WEDNESDAY.value
3
```

열거형 멤버의 타입은 그것이 속한 열거형입니다:

```python
type(Weekday.MONDAY)
<enum 'Weekday'>
isinstance(Weekday.FRIDAY, Weekday)
True
```

열거형 멤버에는 이름만 포함하는 속성이 있습니다:

```python
print(Weekday.TUESDAY.name)
TUESDAY
```

마찬가지로, 값에 대한 속성도 있습니다:

```python
Weekday.WEDNESDAY.value
3
```

Unlike many languages that treat enumerations solely as name/value pairs, Python Enums can have behavior added. For example, datetime.date has two methods for returning the weekday: weekday() and isoweekday(). The difference is that one of them counts from 0-6 and the other from 1-7. Rather than keep track of that ourselves we can add a method to the Weekday enum to extract the day from the date instance and return the matching enum member:

```python
@classmethod
def from_date(cls, date):
    return cls(date.isoweekday())
```

The complete Weekday enum now looks like this:

```python
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    #
    @classmethod
    def from_date(cls, date):
        return cls(date.isoweekday())
```

많은 언어가 열거형을 단순히 이름/값 쌍으로 취급하는 것과 달리, Python Enum에는 동작을 추가할 수 있습니다. 예를 들어, datetime.date에는 요일을 반환하는 두 가지 메서드가 있습니다: weekday()와 isoweekday(). 차이점은 하나는 0-6부터 카운트하고 다른 하나는 1-7부터 카운트한다는 것입니다. 우리가 직접 그것을 추적하는 대신, Weekday 열거형에 메서드를 추가하여 날짜 인스턴스에서 요일을 추출하고 일치하는 열거형 멤버를 반환할 수 있습니다:

```python
@classmethod
def from_date(cls, date):
    return cls(date.isoweekday())
```

이제 완전한 Weekday 열거형은 다음과 같습니다:

```python
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    #
    @classmethod
    def from_date(cls, date):
        return cls(date.isoweekday())
```

Now we can find out what today is! Observe:

```python
from datetime import date
Weekday.from_date(date.today())
<Weekday.TUESDAY: 2>
```

Of course, if you're reading this on some other day, you'll see that day instead.

This Weekday enum is great if our variable only needs one day, but what if we need several? Maybe we're writing a function to plot chores during a week, and don't want to use a list – we could use a different type of Enum:

```python
from enum import Flag
class Weekday(Flag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    THURSDAY = 8
    FRIDAY = 16
    SATURDAY = 32
    SUNDAY = 64
```

We've changed two things: we're inherited from Flag, and the values are all powers of 2.

Just like the original Weekday enum above, we can have a single selection:

```python
first_week_day = Weekday.MONDAY
first_week_day
<Weekday.MONDAY: 1>
```

이제 오늘이 무슨 요일인지 알아낼 수 있습니다! 살펴보세요:

```python
from datetime import date
Weekday.from_date(date.today())
<Weekday.TUESDAY: 2>
```

물론, 다른 날에 이것을 읽고 있다면, 해당 날짜를 대신 볼 수 있을 것입니다.

이 Weekday 열거형은 변수에 하나의 요일만 필요한 경우에 좋지만, 여러 요일이 필요하면 어떨까요? 아마도 우리는 일주일 동안의 집안일을 계획하는 함수를 작성하고 있고, 리스트를 사용하고 싶지 않을 수 있습니다 - 다른 유형의 Enum을 사용할 수 있습니다:

```python
from enum import Flag
class Weekday(Flag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    THURSDAY = 8
    FRIDAY = 16
    SATURDAY = 32
    SUNDAY = 64
```

두 가지를 변경했습니다: Flag에서 상속받았으며, 값은 모두 2의 거듭제곱입니다.

위의 원래 Weekday 열거형과 마찬가지로, 단일 선택을 할 수 있습니다:

```python
first_week_day = Weekday.MONDAY
first_week_day
<Weekday.MONDAY: 1>
```

But Flag also allows us to combine several members into a single variable:

```python
weekend = Weekday.SATURDAY | Weekday.SUNDAY
weekend
<Weekday.SATURDAY|SUNDAY: 96>
```

You can even iterate over a Flag variable:

```python
for day in weekend:
    print(day)
Weekday.SATURDAY
Weekday.SUNDAY
```

Okay, let's get some chores set up:

```python
chores_for_ethan = {
    'feed the cat': Weekday.MONDAY | Weekday.WEDNESDAY | Weekday.FRIDAY,
    'do the dishes': Weekday.TUESDAY | Weekday.THURSDAY,
    'answer SO questions': Weekday.SATURDAY,
    }
```

And a function to display the chores for a given day:

```python
def show_chores(chores, day):
    for chore, days in chores.items():
        if day in days:
            print(chore)

show_chores(chores_for_ethan, Weekday.SATURDAY)
answer SO questions
```

그러나 Flag를 사용하면 여러 멤버를 하나의 변수로 결합할 수도 있습니다:

```python
weekend = Weekday.SATURDAY | Weekday.SUNDAY
weekend
<Weekday.SATURDAY|SUNDAY: 96>
```

심지어 Flag 변수를 반복할 수도 있습니다:

```python
for day in weekend:
    print(day)
Weekday.SATURDAY
Weekday.SUNDAY
```

좋아요, 이제 몇 가지 집안일을 설정해 봅시다:

```python
chores_for_ethan = {
    'feed the cat': Weekday.MONDAY | Weekday.WEDNESDAY | Weekday.FRIDAY,
    'do the dishes': Weekday.TUESDAY | Weekday.THURSDAY,
    'answer SO questions': Weekday.SATURDAY,
    }
```

그리고 주어진 날짜에 대한 집안일을 표시하는 함수도 만들어 봅시다:

```python
def show_chores(chores, day):
    for chore, days in chores.items():
        if day in days:
            print(chore)

show_chores(chores_for_ethan, Weekday.SATURDAY)
answer SO questions
```

In cases where the actual values of the members do not matter, you can save yourself some work and use auto() for the values:

```python
from enum import auto
class Weekday(Flag):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()
    WEEKEND = SATURDAY | SUNDAY
```

## Programmatic access to enumeration members and their attributes

Sometimes it's useful to access members in enumerations programmatically (i.e. situations where Color.RED won't do because the exact color is not known at program-writing time). Enum allows such access:

```python
Color(1)
<Color.RED: 1>
Color(3)
<Color.BLUE: 3>
```

멤버의 실제 값이 중요하지 않은 경우, auto()를 사용하여 값을 지정하면 작업을 줄일 수 있습니다:

```python
from enum import auto
class Weekday(Flag):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()
    WEEKEND = SATURDAY | SUNDAY
```

## 열거형 멤버와 속성에 프로그래밍 방식으로 접근하기

때로는 열거형의 멤버에 프로그래밍 방식으로 접근하는 것이 유용합니다(즉, 프로그램 작성 시점에 정확한 색상을 알 수 없기 때문에 Color.RED가 작동하지 않는 상황). Enum은 그러한 접근을 허용합니다:

```python
Color(1)
<Color.RED: 1>
Color(3)
<Color.BLUE: 3>
```

If you want to access enum members by name, use item access:

```python
Color['RED']
<Color.RED: 1>
Color['GREEN']
<Color.GREEN: 2>
```

If you have an enum member and need its name or value:

```python
member = Color.RED
member.name
'RED'
member.value
1
```

## Duplicating enum members and values

Having two enum members with the same name is invalid:

```python
class Shape(Enum):
    SQUARE = 2
    SQUARE = 3

Traceback (most recent call last):
...
TypeError: 'SQUARE' already defined as 2
```

이름으로 열거형 멤버에 접근하려면 항목 접근을 사용하세요:

```python
Color['RED']
<Color.RED: 1>
Color['GREEN']
<Color.GREEN: 2>
```

열거형 멤버가 있고 그 이름이나 값이 필요한 경우:

```python
member = Color.RED
member.name
'RED'
member.value
1
```

## 열거형 멤버 및 값 중복하기

같은 이름을 가진 두 개의 열거형 멤버를 갖는 것은 유효하지 않습니다:

```python
class Shape(Enum):
    SQUARE = 2
    SQUARE = 3

Traceback (most recent call last):
...
TypeError: 'SQUARE' already defined as 2
```

However, an enum member can have other names associated with it. Given two entries A and B with the same value (and A defined first), B is an alias for the member A. By-value lookup of the value of A will return the member A. By-name lookup of A will return the member A. By-name lookup of B will also return the member A:

```python
class Shape(Enum):
    SQUARE = 2
    DIAMOND = 1
    CIRCLE = 3
    ALIAS_FOR_SQUARE = 2

Shape.SQUARE
<Shape.SQUARE: 2>
Shape.ALIAS_FOR_SQUARE
<Shape.SQUARE: 2>
Shape(2)
<Shape.SQUARE: 2>
```

Note Attempting to create a member with the same name as an already defined attribute (another member, a method, etc.) or attempting to create an attribute with the same name as a member is not allowed.

## Ensuring unique enumeration values

By default, enumerations allow multiple names as aliases for the same value. When this behavior isn't desired, you can use the unique() decorator:

```python
from enum import Enum, unique
@unique
class Mistake(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 3

Traceback (most recent call last):
...
ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE
```

하지만, 열거형 멤버는 그것과 연관된 다른 이름을 가질 수 있습니다. 같은 값을 가진 두 항목 A와 B가 있고(A가 먼저 정의됨), B는 멤버 A의 별칭입니다. A의 값으로 조회하면 멤버 A가 반환됩니다. A의 이름으로 조회하면 멤버 A가 반환됩니다. B의 이름으로 조회해도 멤버 A가 반환됩니다:

```python
class Shape(Enum):
    SQUARE = 2
    DIAMOND = 1
    CIRCLE = 3
    ALIAS_FOR_SQUARE = 2

Shape.SQUARE
<Shape.SQUARE: 2>
Shape.ALIAS_FOR_SQUARE
<Shape.SQUARE: 2>
Shape(2)
<Shape.SQUARE: 2>
```

참고: 이미 정의된 속성(다른 멤버, 메서드 등)과 같은 이름을 가진 멤버를 만들거나 멤버와 같은 이름을 가진 속성을 만들려고 시도하는 것은 허용되지 않습니다.

## 고유한 열거형 값 보장하기

기본적으로 열거형은 같은 값에 대해 여러 이름을 별칭으로 허용합니다. 이 동작이 원하지 않는 경우, unique() 데코레이터를 사용할 수 있습니다:

```python
from enum import Enum, unique
@unique
class Mistake(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 3

Traceback (most recent call last):
...
ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE
```

## Using automatic values

If the exact value is unimportant you can use auto:

```python
from enum import Enum, auto
class Color(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()

[member.value for member in Color]
[1, 2, 3]
```

The values are chosen by _generate_next_value_(), which can be overridden:

```python
class AutoName(Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name

class Ordinal(AutoName):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

[member.value for member in Ordinal]
['NORTH', 'SOUTH', 'EAST', 'WEST']
```

Note The _generate_next_value_() method must be defined before any members.

## 자동 값 사용하기

정확한 값이 중요하지 않은 경우 auto를 사용할 수 있습니다:

```python
from enum import Enum, auto
class Color(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()

[member.value for member in Color]
[1, 2, 3]
```

값은 _generate_next_value_()에 의해 선택되며, 이는 재정의할 수 있습니다:

```python
class AutoName(Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name

class Ordinal(AutoName):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

[member.value for member in Ordinal]
['NORTH', 'SOUTH', 'EAST', 'WEST']
```

참고: _generate_next_value_() 메서드는 모든 멤버보다 먼저 정의되어야 합니다.

## Iteration

Iterating over the members of an enum does not provide the aliases:

```python
list(Shape)
[<Shape.SQUARE: 2>, <Shape.DIAMOND: 1>, <Shape.CIRCLE: 3>]
list(Weekday)
[<Weekday.MONDAY: 1>, <Weekday.TUESDAY: 2>, <Weekday.WEDNESDAY: 4>, <Weekday.THURSDAY: 8>, <Weekday.FRIDAY: 16>, <Weekday.SATURDAY: 32>, <Weekday.SUNDAY: 64>]
```

Note that the aliases Shape.ALIAS_FOR_SQUARE and Weekday.WEEKEND aren't shown.

The special attribute __members__ is a read-only ordered mapping of names to members. It includes all names defined in the enumeration, including the aliases:

```python
for name, member in Shape.__members__.items():
    name, member

('SQUARE', <Shape.SQUARE: 2>)
('DIAMOND', <Shape.DIAMOND: 1>)
('CIRCLE', <Shape.CIRCLE: 3>)
('ALIAS_FOR_SQUARE', <Shape.SQUARE: 2>)
```

## 반복

열거형의 멤버를 반복해도 별칭은 제공되지 않습니다:

```python
list(Shape)
[<Shape.SQUARE: 2>, <Shape.DIAMOND: 1>, <Shape.CIRCLE: 3>]
list(Weekday)
[<Weekday.MONDAY: 1>, <Weekday.TUESDAY: 2>, <Weekday.WEDNESDAY: 4>, <Weekday.THURSDAY: 8>, <Weekday.FRIDAY: 16>, <Weekday.SATURDAY: 32>, <Weekday.SUNDAY: 64>]
```

Shape.ALIAS_FOR_SQUARE와 Weekday.WEEKEND 별칭은 표시되지 않습니다.

특수 속성 __members__는 이름에서 멤버로의 읽기 전용 순서 매핑입니다. 여기에는 별칭을 포함하여 열거형에 정의된 모든 이름이 포함됩니다:

```python
for name, member in Shape.__members__.items():
    name, member

('SQUARE', <Shape.SQUARE: 2>)
('DIAMOND', <Shape.DIAMOND: 1>)
('CIRCLE', <Shape.CIRCLE: 3>)
('ALIAS_FOR_SQUARE', <Shape.SQUARE: 2>)
```

The __members__ attribute can be used for detailed programmatic access to the enumeration members. For example, finding all the aliases:

```python
[name for name, member in Shape.__members__.items() if member.name != name]
['ALIAS_FOR_SQUARE']
```

Note Aliases for flags include values with multiple flags set, such as 3, and no flags set, i.e. 0.

## Comparisons

Enumeration members are compared by identity:

```python
Color.RED is Color.RED
True
Color.RED is Color.BLUE
False
Color.RED is not Color.BLUE
True
```

__members__ 속성은 열거형 멤버에 대한 상세한 프로그래밍 방식 접근에 사용될 수 있습니다. 예를 들어, 모든 별칭을 찾는 방법:

```python
[name for name, member in Shape.__members__.items() if member.name != name]
['ALIAS_FOR_SQUARE']
```

참고: 플래그의 별칭에는 여러 플래그가 설정된 값(예: 3)과 플래그가 설정되지 않은 값(즉, 0)이 포함됩니다.

## 비교

열거형 멤버는 ID로 비교됩니다:

```python
Color.RED is Color.RED
True
Color.RED is Color.BLUE
False
Color.RED is not Color.BLUE
True
```

Ordered comparisons between enumeration values are not supported. Enum members are not integers (but see IntEnum below):

```python
Color.RED < Color.BLUE
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'Color' and 'Color'
```

Equality comparisons are defined though:

```python
Color.BLUE == Color.RED
False
Color.BLUE != Color.RED
True
Color.BLUE == Color.BLUE
True
```

Comparisons against non-enumeration values will always compare not equal (again, IntEnum was explicitly designed to behave differently, see below):

```python
Color.BLUE == 2
False
```

Warning It is possible to reload modules – if a reloaded module contains enums, they will be recreated, and the new members may not compare identical/equal to the original members.

열거형 값 간의 순서 비교는 지원되지 않습니다. Enum 멤버는 정수가 아닙니다(하지만 아래의 IntEnum 참조):

```python
Color.RED < Color.BLUE
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'Color' and 'Color'
```

그러나 동등성 비교는 정의되어 있습니다:

```python
Color.BLUE == Color.RED
False
Color.BLUE != Color.RED
True
Color.BLUE == Color.BLUE
True
```

비열거형 값과의 비교는 항상 같지 않음으로 비교됩니다(다시 말하지만, IntEnum은 명시적으로 다르게 동작하도록 설계되었습니다. 아래 참조):

```python
Color.BLUE == 2
False
```

경고: 모듈을 다시 로드하는 것이 가능합니다 - 다시 로드된 모듈에 열거형이 포함되어 있으면, 그것들은 다시 생성되고, 새 멤버는 원래 멤버와 동일하게/동등하게 비교되지 않을 수 있습니다.

## Allowed members and attributes of enumerations

Most of the examples above use integers for enumeration values. Using integers is short and handy (and provided by default by the Functional API), but not strictly enforced. In the vast majority of use-cases, one doesn't care what the actual value of an enumeration is. But if the value is important, enumerations can have arbitrary values.

Enumerations are Python classes, and can have methods and special methods as usual. If we have this enumeration:

```python
class Mood(Enum):
    FUNKY = 1
    HAPPY = 3

    def describe(self):
        # self is the member here
        return self.name, self.value

    def __str__(self):
        return 'my custom str! {0}'.format(self.value)

    @classmethod
    def favorite_mood(cls):
        # cls here is the enumeration
        return cls.HAPPY
```

Then:

```python
Mood.favorite_mood()
<Mood.HAPPY: 3>
Mood.HAPPY.describe()
('HAPPY', 3)
str(Mood.FUNKY)
'my custom str! 1'
```

## 열거형의 허용된 멤버 및 속성

위의 대부분의 예제는 열거형 값에 정수를 사용합니다. 정수를 사용하는 것은 짧고 편리하며(기능적 API에서 기본적으로 제공), 엄격하게 강제되지는 않습니다. 대부분의 사용 사례에서는 열거형의 실제 값이 무엇인지 신경 쓰지 않습니다. 그러나 값이 중요한 경우, 열거형은 임의의 값을 가질 수 있습니다.

열거형은 Python 클래스이며, 일반적으로 메서드와 특수 메서드를 가질 수 있습니다. 이러한 열거형이 있다면:

```python
class Mood(Enum):
    FUNKY = 1
    HAPPY = 3

    def describe(self):
        # self는 여기서 멤버입니다
        return self.name, self.value

    def __str__(self):
        return 'my custom str! {0}'.format(self.value)

    @classmethod
    def favorite_mood(cls):
        # cls는 여기서 열거형입니다
        return cls.HAPPY
```

그러면:

```python
Mood.favorite_mood()
<Mood.HAPPY: 3>
Mood.HAPPY.describe()
('HAPPY', 3)
str(Mood.FUNKY)
'my custom str! 1'
```

The rules for what is allowed are as follows: names that start and end with a single underscore are reserved by enum and cannot be used; all other attributes defined within an enumeration will become members of this enumeration, with the exception of special methods (__str__(), __add__(), etc.), descriptors (methods are also descriptors), and variable names listed in _ignore_.

Note: if your enumeration defines __new__() and/or __init__(), any value(s) given to the enum member will be passed into those methods. See Planet for an example.

Note The __new__() method, if defined, is used during creation of the Enum members; it is then replaced by Enum's __new__() which is used after class creation for lookup of existing members. See When to use __new__() vs. __init__() for more details.

## Restricted Enum subclassing

A new Enum class must have one base enum class, up to one concrete data type, and as many object-based mixin classes as needed. The order of these base classes is:

```python
class EnumName([mix-in, ...,] [data-type,] base-enum):
    pass
```

허용되는 항목에 대한 규칙은 다음과 같습니다: 단일 밑줄로 시작하고 끝나는 이름은 enum에 의해 예약되어 있으며 사용할 수 없습니다. 열거형 내에 정의된 다른 모든 속성은 특수 메서드(__str__(), __add__() 등), 디스크립터(메서드도 디스크립터입니다), 그리고 _ignore_에 나열된 변수 이름을 제외하고 이 열거형의 멤버가 됩니다.

참고: 열거형이 __new__() 및/또는 __init__()을 정의하는 경우, 열거형 멤버에 제공된 모든 값은 이러한 메서드에 전달됩니다. 예제는 Planet을 참조하세요.

참고: __new__() 메서드가 정의된 경우, Enum 멤버 생성 중에 사용됩니다. 그런 다음 기존 멤버 조회를 위해 클래스 생성 후 사용되는 Enum의 __new__()로 대체됩니다. 자세한 내용은 __new__() vs. __init__() 사용 시점을 참조하세요.

## 제한된 Enum 서브클래싱

새로운 Enum 클래스는 하나의 기본 enum 클래스, 최대 하나의 구체적인 데이터 타입, 그리고 필요한 만큼 많은 객체 기반 mixin 클래스를 가져야 합니다. 이러한 기본 클래스의 순서는 다음과 같습니다:

```python
class EnumName([mix-in, ...,] [data-type,] base-enum):
    pass
```

Also, subclassing an enumeration is allowed only if the enumeration does not define any members. So this is forbidden:

```python
class MoreColor(Color):
    PINK = 17

Traceback (most recent call last):
...
TypeError: <enum 'MoreColor'> cannot extend <enum 'Color'>
```

But this is allowed:

```python
class Foo(Enum):
    def some_behavior(self):
        pass

class Bar(Foo):
    HAPPY = 1
    SAD = 2
```

Allowing subclassing of enums that define members would lead to a violation of some important invariants of types and instances. On the other hand, it makes sense to allow sharing some common behavior between a group of enumerations. (See OrderedEnum for an example.)

또한, 열거형의 서브클래싱은 열거형이 어떤 멤버도 정의하지 않는 경우에만 허용됩니다. 따라서 이것은 금지됩니다:

```python
class MoreColor(Color):
    PINK = 17

Traceback (most recent call last):
...
TypeError: <enum 'MoreColor'> cannot extend <enum 'Color'>
```

하지만 이것은 허용됩니다:

```python
class Foo(Enum):
    def some_behavior(self):
        pass

class Bar(Foo):
    HAPPY = 1
    SAD = 2
```

멤버를 정의하는 열거형의 서브클래싱을 허용하면 타입과 인스턴스의 중요한 불변성이 위반될 수 있습니다. 반면에, 열거형 그룹 간에 일부 공통 동작을 공유할 수 있도록 하는 것은 합리적입니다. (예제는 OrderedEnum을 참조하세요.)

## Dataclass support

When inheriting from a dataclass, the __repr__() omits the inherited class' name. For example:

```python
from dataclasses import dataclass, field
@dataclass
class CreatureDataMixin:
    size: str
    legs: int
    tail: bool = field(repr=False, default=True)

class Creature(CreatureDataMixin, Enum):
    BEETLE = 'small', 6
    DOG = 'medium', 4

Creature.DOG
<Creature.DOG: size='medium', legs=4>
```

Use the dataclass() argument repr=False to use the standard repr().

Changed in version 3.12: Only the dataclass fields are shown in the value area, not the dataclass' name.

## 데이터클래스 지원

데이터클래스에서 상속할 때, __repr__()는 상속된 클래스의 이름을 생략합니다. 예를 들어:

```python
from dataclasses import dataclass, field
@dataclass
class CreatureDataMixin:
    size: str
    legs: int
    tail: bool = field(repr=False, default=True)

class Creature(CreatureDataMixin, Enum):
    BEETLE = 'small', 6
    DOG = 'medium', 4

Creature.DOG
<Creature.DOG: size='medium', legs=4>
```

표준 repr()을 사용하려면 dataclass() 인수 repr=False를 사용하세요.

버전 3.12에서 변경됨: 값 영역에는 데이터클래스의 이름이 아닌 데이터클래스 필드만 표시됩니다.

Note Adding dataclass() decorator to Enum and its subclasses is not supported. It will not raise any errors, but it will produce very strange results at runtime, such as members being equal to each other:

```python
@dataclass               # don't do this: it does not make any sense
class Color(Enum):
   RED = 1
   BLUE = 2

Color.RED is Color.BLUE
False
Color.RED == Color.BLUE  # problem is here: they should not be equal
True
```

## Pickling

Enumerations can be pickled and unpickled:

```python
from test.test_enum import Fruit
from pickle import dumps, loads
Fruit.TOMATO is loads(dumps(Fruit.TOMATO))
True
```

The usual restrictions for pickling apply: picklable enums must be defined in the top level of a module, since unpickling requires them to be importable from that module.

참고: Enum 및 그 서브클래스에 dataclass() 데코레이터를 추가하는 것은 지원되지 않습니다. 오류는 발생하지 않지만 실행 시 멤버가 서로 동일하다는 등 매우 이상한 결과가 발생합니다:

```python
@dataclass               # 이렇게 하지 마세요: 전혀 의미가 없습니다
class Color(Enum):
   RED = 1
   BLUE = 2

Color.RED is Color.BLUE
False
Color.RED == Color.BLUE  # 문제는 여기에 있습니다: 동일하지 않아야 합니다
True
```

## 피클링

열거형은 피클링 및 언피클링될 수 있습니다:

```python
from test.test_enum import Fruit
from pickle import dumps, loads
Fruit.TOMATO is loads(dumps(Fruit.TOMATO))
True
```

피클링에 대한 일반적인 제한 사항이 적용됩니다: 피클링 가능한 열거형은 모듈의 최상위 레벨에 정의되어야 합니다. 언피클링 시 해당 모듈에서 가져올 수 있어야 하기 때문입니다.

