# Python Functional Programming How-To Guide (Python 함수형 프로그래밍 가이드)

## Introduction to Functional Programming

1. Functional programming is a programming paradigm where programs are constructed by applying and composing functions. It emphasizes the application of functions, avoids changing state and mutable data, and treats computation as the evaluation of mathematical functions.

함수형 프로그래밍은 함수를 적용하고 합성하여 프로그램을 구성하는 프로그래밍 패러다임입니다. 함수의 적용을 강조하고, 상태 변경과 가변 데이터를 피하며, 계산을 수학적 함수의 평가로 취급합니다.

2. While Python is not a purely functional programming language like Haskell or Clojure, it does support many functional programming features that allow you to adopt functional programming techniques in your code.

Python은 Haskell이나 Clojure와 같은 순수 함수형 프로그래밍 언어는 아니지만, 코드에서 함수형 프로그래밍 기법을 채택할 수 있는 많은 함수형 프로그래밍 기능을 지원합니다.

## First-class Functions

3. In Python, functions are first-class citizens, which means they can be passed as arguments to other functions, returned from other functions, and assigned to variables.

Python에서 함수는 일급 시민(first-class citizens)으로, 다른 함수에 인자로 전달되거나, 다른 함수에서 반환되거나, 변수에 할당될 수 있습니다.

```python
def greet(name):
    return f"Hello, {name}!"

# Assigning a function to a variable
greeter = greet
print(greeter("Alice"))  # Output: Hello, Alice!

# Passing a function as an argument
def apply_function(func, value):
    return func(value)

print(apply_function(greet, "Bob"))  # Output: Hello, Bob!

# Returning a function
def create_greeter():
    def greeter(name):
        return f"Welcome, {name}!"
    return greeter

new_greeter = create_greeter()
print(new_greeter("Charlie"))  # Output: Welcome, Charlie!
```

## Pure Functions

4. A pure function is a function that always returns the same result given the same arguments and has no side effects. It doesn't modify external state or variables.

순수 함수는 같은 인자가 주어지면 항상 같은 결과를 반환하고 부작용이 없는 함수입니다. 외부 상태나 변수를 수정하지 않습니다.

```python
# Pure function
def add(a, b):
    return a + b

# Impure function (has side effects)
total = 0
def add_to_total(value):
    global total
    total += value
    return total
```

5. Pure functions make code easier to test, debug, and reason about, since they don't depend on or change the state of the program.

순수 함수는 프로그램의 상태에 의존하거나 변경하지 않기 때문에 코드를 테스트하고, 디버깅하고, 추론하기 쉽게 만듭니다.

## Higher-order Functions

6. A higher-order function is a function that takes one or more functions as arguments or returns a function as its result. Python has several built-in higher-order functions.

고차 함수는 하나 이상의 함수를 인자로 받거나 함수를 결과로 반환하는 함수입니다. Python에는 여러 내장 고차 함수가 있습니다.

```python
# map applies a function to each item in an iterable
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# filter selects items from an iterable based on a function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# functools.reduce applies a function cumulatively to items in an iterable
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120 (1 * 2 * 3 * 4 * 5)
```

## Function Composition

7. Function composition is the process of combining two or more functions to create a new function. In mathematical notation, (f ∘ g)(x) = f(g(x)).

함수 합성은 두 개 이상의 함수를 결합하여 새 함수를 만드는 과정입니다. 수학적 표기로는, (f ∘ g)(x) = f(g(x))입니다.

```python
def compose(f, g):
    """Compose two functions: f(g(x))"""
    return lambda x: f(g(x))

# Example functions
def double(x):
    return x * 2

def increment(x):
    return x + 1

# Composition
double_then_increment = compose(increment, double)
print(double_then_increment(5))  # Output: 11 (5 * 2 + 1)

increment_then_double = compose(double, increment)
print(increment_then_double(5))  # Output: 12 ((5 + 1) * 2)
```

8. For more complex compositions, you can use the `compose` function from the `toolz` library or implement your own to chain multiple functions together.

더 복잡한 합성의 경우, `toolz` 라이브러리의 `compose` 함수를 사용하거나 여러 함수를 함께 연결하기 위해 자신만의 함수를 구현할 수 있습니다.

## Map, Filter, and Reduce

9. These three functions are the cornerstones of functional programming in many languages, and Python provides them as well:

이 세 함수는 많은 언어의 함수형 프로그래밍의 근간이며, Python도 이를 제공합니다:

10. `map(func, iterable)` applies `func` to each element of `iterable` and returns an iterator of the results.

`map(func, iterable)`은 `iterable`의 각 요소에 `func`를 적용하고 결과의 이터레이터를 반환합니다.

```python
prices = [10.5, 8.75, 15.99, 20.0]
tax_rate = 0.07
prices_with_tax = map(lambda price: price * (1 + tax_rate), prices)
print(list(prices_with_tax))  # [11.235, 9.3625, 17.1093, 21.4]
```

11. `filter(func, iterable)` constructs an iterator from elements of `iterable` for which `func` returns True.

`filter(func, iterable)`는 `func`가 True를 반환하는 `iterable`의 요소로부터 이터레이터를 구성합니다.

```python
def is_premium(price):
    return price >= 10.0

premium_prices = filter(is_premium, prices)
print(list(premium_prices))  # [10.5, 15.99, 20.0]
```

12. `reduce(func, iterable[, initializer])` applies `func` of two arguments cumulatively to the items of `iterable`, reducing it to a single value.

`reduce(func, iterable[, initializer])`는 `iterable`의 항목에 두 인자의 `func`을 누적적으로 적용하여 단일 값으로 줄입니다.

```python
from functools import reduce

total = reduce(lambda x, y: x + y, prices)
print(total)  # 55.24

# With initializer
total_with_init = reduce(lambda x, y: x + y, prices, 100)
print(total_with_init)  # 155.24
```

## Lambda Expressions

13. Lambda expressions in Python allow you to create small, anonymous functions without a name.

Python의 람다 표현식을 사용하면 이름 없이 작은 익명 함수를 만들 수 있습니다.

```python
# Regular function
def square(x):
    return x * x

# Equivalent lambda function
square_lambda = lambda x: x * x

print(square(5))       # 25
print(square_lambda(5))  # 25

# Lambdas are often used with higher-order functions
sorted_names = sorted(['Alice', 'Bob', 'Charlie', 'Dave'], key=lambda name: len(name))
print(sorted_names)  # ['Bob', 'Dave', 'Alice', 'Charlie']
```

14. While lambda functions are useful for short operations, they should not be overused. For more complex functions, it's better to use regular function definitions for clarity.

람다 함수는 짧은 작업에 유용하지만 과도하게 사용해서는 안 됩니다. 더 복잡한 함수의 경우, 명확성을 위해 일반 함수 정의를 사용하는 것이 좋습니다.

## List Comprehensions

15. List comprehensions provide a concise way to create lists based on existing lists, and they align well with functional programming principles.

리스트 컴프리헨션은 기존 리스트를 기반으로 리스트를 만드는 간결한 방법을 제공하며, 함수형 프로그래밍 원칙과 잘 맞습니다.

```python
# Traditional approach using map and filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_evens_map_filter = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

# Equivalent list comprehension
squared_evens_comp = [x**2 for x in numbers if x % 2 == 0]

print(squared_evens_map_filter)  # [4, 16, 36, 64, 100]
print(squared_evens_comp)        # [4, 16, 36, 64, 100]
```

16. List comprehensions are often more readable and faster than equivalent combinations of map and filter.

리스트 컴프리헨션은 종종 map과 filter의 동등한 조합보다 더 읽기 쉽고 빠릅니다.

## Immutability and Avoiding Side Effects

17. Functional programming emphasizes immutable data structures and avoiding side effects. In Python, you can use tuples, frozensets, and other immutable data types.

함수형 프로그래밍은 불변 데이터 구조와 부작용 회피를 강조합니다. Python에서는 튜플, frozenset 및 기타 불변 데이터 유형을 사용할 수 있습니다.

```python
# Immutable data types
immutable_tuple = (1, 2, 3)
immutable_set = frozenset([1, 2, 3])

# Creating new data instead of modifying existing data
original_list = [1, 2, 3]
new_list = original_list + [4]  # Creates a new list instead of modifying the original
doubled_list = [x * 2 for x in original_list]  # Creates a new transformed list

print(original_list)  # Still [1, 2, 3]
print(new_list)       # [1, 2, 3, 4]
print(doubled_list)   # [2, 4, 6]
```

18. To maintain immutability with more complex data structures, you can use libraries like `pyrsistent` which provides persistent (immutable) data structures.

더 복잡한 데이터 구조로 불변성을 유지하려면 영구적(불변) 데이터 구조를 제공하는 `pyrsistent`와 같은 라이브러리를 사용할 수 있습니다.

## Recursion

19. Recursion is a technique where a function calls itself. It's a common approach in functional programming for tasks like traversing tree structures or solving problems that can be broken down into smaller, similar subproblems.

재귀는 함수가 자기 자신을 호출하는 기법입니다. 이는 트리 구조를 순회하거나 더 작고 유사한 하위 문제로 분해할 수 있는 문제를 해결하는 데 함수형 프로그래밍에서 일반적인 접근법입니다.

```python
def factorial(n):
    """Calculate factorial of n recursively"""
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120

def fibonacci(n):
    """Calculate the nth Fibonacci number recursively"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # 55
```

20. Note that Python has a default recursion limit of 1000. For deeply recursive functions, consider using `tail recursion optimization` or iterative approaches.

Python의 기본 재귀 제한은 1000입니다. 깊은 재귀 함수의 경우, `꼬리 재귀 최적화` 또는 반복적 접근법을 고려하세요.

## Decorators

21. Decorators allow you to modify the behavior of functions without changing their code. They are higher-order functions that take a function and return a new function.

데코레이터를 사용하면 코드를 변경하지 않고도 함수의 동작을 수정할 수 있습니다. 이는 함수를 받아 새 함수를 반환하는 고차 함수입니다.

```python
def log_function_call(func):
    """Log when a function is called"""
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

result = add(3, 5)
# Output:
# Calling function: add
# Function add returned: 8
```

22. Decorators are a powerful tool for separating cross-cutting concerns like logging, timing, or authentication from your main business logic.

데코레이터는 로깅, 타이밍 또는 인증과 같은 횡단 관심사를 주요 비즈니스 로직에서 분리하는 강력한 도구입니다.

## Partial Functions

23. Partial functions allow you to fix a certain number of arguments of a function and generate a new function. Python's `functools.partial` makes this easy.

부분 함수는 함수의 특정 수의 인자를 고정하고 새 함수를 생성할 수 있게 합니다. Python의 `functools.partial`은 이를 쉽게 만듭니다.

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

# Create a function that squares a number
square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(4))  # 16
print(cube(4))    # 64

# Partial application with positional arguments
def greet(greeting, name):
    return f"{greeting}, {name}!"

hello = partial(greet, "Hello")
hi = partial(greet, "Hi")

print(hello("Alice"))  # Hello, Alice!
print(hi("Bob"))       # Hi, Bob!
```

## Closures

24. A closure is a function object that remembers values in the enclosing lexical scope even when the scope has finished execution. Closures are used to implement function factories and maintain state.

클로저는 스코프가 실행을 마친 후에도 둘러싸는 어휘적 스코프의 값을 기억하는 함수 객체입니다. 클로저는 함수 팩토리를 구현하고 상태를 유지하는 데 사용됩니다.

```python
def make_multiplier(factor):
    """Create a function that multiplies by the given factor."""
    def multiply(number):
        return number * factor  # 'factor' is remembered from the enclosing scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

25. Closures are a way to achieve data encapsulation and can be used as an alternative to classes for simple cases.

클로저는 데이터 캡슐화를 달성하는 방법이며 간단한 경우에 클래스에 대한 대안으로 사용될 수 있습니다.

## The functools Module

26. The `functools` module provides higher-order functions and operations on callable objects. We've already seen `partial` and `reduce`, but there are other useful tools:

`functools` 모듈은 호출 가능한 객체에 대한 고차 함수와 연산을 제공합니다. 이미 `partial`과 `reduce`를 보았지만, 다른 유용한 도구도 있습니다:

```python
from functools import lru_cache, wraps, singledispatch

# lru_cache implements memoization, caching the results of function calls
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(30))  # Very fast despite the naive implementation

# wraps helps to preserve function metadata when creating decorators
def my_decorator(func):
    @wraps(func)  # Preserves func's __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

# singledispatch enables function overloading by type
@singledispatch
def process(obj):
    print("Default implementation")

@process.register
def _(obj: int):
    print(f"Processing an integer: {obj}")

@process.register
def _(obj: str):
    print(f"Processing a string: {obj}")

process(42)      # Processing an integer: 42
process("hello") # Processing a string: hello
process([1, 2])  # Default implementation
```

## The itertools Module

27. The `itertools` module provides a collection of functions for working with iterators in a functional style. These functions can be combined to create complex iterator pipelines.

`itertools` 모듈은 함수형 스타일로 이터레이터를 다루기 위한 함수 모음을 제공합니다. 이러한 함수들은 복잡한 이터레이터 파이프라인을 만들기 위해 결합될 수 있습니다.

```python
import itertools as it

# Generate an infinite sequence of numbers
counter = it.count(start=1, step=2)  # 1, 3, 5, ...
print(next(counter), next(counter), next(counter))  # 1 3 5

# Cycle through elements indefinitely
cycler = it.cycle(["A", "B", "C"])
print(next(cycler), next(cycler), next(cycler), next(cycler))  # A B C A

# Repeat an element
repeater = it.repeat("X", 3)
print(list(repeater))  # ['X', 'X', 'X']

# Combinatorial generators
print(list(it.combinations([1, 2, 3], 2)))  # [(1, 2), (1, 3), (2, 3)]
print(list(it.permutations([1, 2, 3], 2)))  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# Chaining iterables
print(list(it.chain([1, 2], [3, 4])))  # [1, 2, 3, 4]

# Group consecutive elements
data = [1, 1, 1, 2, 2, 3, 3, 3, 3]
for key, group in it.groupby(data):
    print(key, "->", list(group))
# 1 -> [1, 1, 1]
# 2 -> [2, 2]
# 3 -> [3, 3, 3, 3]
```

## Best Practices

28. Here are some best practices for functional programming in Python:

다음은 Python의 함수형 프로그래밍에 대한 몇 가지 모범 사례입니다:

29. Prefer pure functions where possible, as they are easier to test, debug, and reason about.

가능한 순수 함수를 선호하세요. 테스트, 디버깅 및 추론이 더 쉽습니다.

30. Use immutable data structures to avoid unexpected side effects and bugs related to shared mutable state.

공유된 가변 상태와 관련된 예상치 못한 부작용과 버그를 피하기 위해 불변 데이터 구조를 사용하세요.

31. Compose small, focused functions that do one thing well, rather than large, complex functions.

하나의 일을 잘하는 작고 집중된 함수를 구성하세요, 크고 복잡한 함수보다는 말이죠.

32. Use higher-order functions like `map`, `filter`, and `reduce` when appropriate, but don't force a functional style where an imperative approach might be clearer.

적절한 경우 `map`, `filter`, `reduce`와 같은 고차 함수를 사용하되, 명령형 접근법이 더 명확할 수 있는 곳에 함수형 스타일을 억지로 적용하지 마세요.

33. Leverage list comprehensions for their readability and performance when transforming data.

데이터를 변환할 때 가독성과 성능을 위해 리스트 컴프리헨션을 활용하세요.

34. Keep recursion depth in mind in Python, as it has a default limit. Consider tail recursion optimization or iterative approaches for deep recursion.

Python은 기본 제한이 있으므로 재귀 깊이에 유의하세요. 깊은 재귀에는 꼬리 재귀 최적화 또는 반복적 접근법을 고려하세요.

## Real-world Example: Data Processing Pipeline

35. Here's an example of how functional programming can be used to create a data processing pipeline:

다음은 함수형 프로그래밍을 사용하여 데이터 처리 파이프라인을 만드는 방법의 예입니다:

```python
from functools import reduce
import json
from datetime import datetime

# Sample data: daily sales records
sales_data = [
    {"date": "2023-01-01", "product": "Widget A", "amount": 100, "quantity": 2},
    {"date": "2023-01-01", "product": "Widget B", "amount": 200, "quantity": 1},
    {"date": "2023-01-02", "product": "Widget A", "amount": 150, "quantity": 3},
    {"date": "2023-01-02", "product": "Widget B", "amount": 100, "quantity": 1},
    {"date": "2023-01-03", "product": "Widget C", "amount": 300, "quantity": 2}
]

# Pure functions for data transformation
def parse_date(record):
    """Convert date string to datetime object."""
    record_copy = record.copy()  # Create a copy to avoid modifying the original
    record_copy["date"] = datetime.strptime(record["date"], "%Y-%m-%d")
    return record_copy

def calculate_unit_price(record):
    """Add unit_price field to the record."""
    record_copy = record.copy()
    record_copy["unit_price"] = record["amount"] / record["quantity"]
    return record_copy

def filter_expensive_items(record):
    """Filter items with unit price > 100."""
    return record["unit_price"] > 100

def group_by_date(grouped_data, record):
    """Group records by date."""
    date_str = record["date"].strftime("%Y-%m-%d")
    if date_str not in grouped_data:
        grouped_data[date_str] = []
    grouped_data[date_str].append(record)
    return grouped_data

# Functional data processing pipeline
processed_data = (
    # Step 1: Apply transformations to each record
    map(lambda r: calculate_unit_price(parse_date(r)), sales_data),
    
    # Step 2: Filter records
    filter(filter_expensive_items),
    
    # Step 3: Convert to list
    list,
    
    # Step 4: Group by date
    lambda data: reduce(group_by_date, data, {})
)

# Execute pipeline and get result
result = processed_data[3](processed_data[2](processed_data[1](processed_data[0])))

print(json.dumps(
    {k: [{"product": r["product"], "unit_price": r["unit_price"]} for r in v] 
     for k, v in result.items()}, 
    indent=2
))
```

36. In a more advanced implementation, you could use libraries like `toolz` or `fntools` to create more composable and elegant pipelines.

더 고급 구현에서는 `toolz`나 `fntools`와 같은 라이브러리를 사용하여 더 구성 가능하고 우아한 파이프라인을 만들 수 있습니다.

## Conclusion

37. Functional programming in Python offers a powerful paradigm that can make your code more maintainable, testable, and in many cases, more concise. While Python is not purely functional, it provides many features that allow you to leverage functional concepts effectively.

Python의 함수형 프로그래밍은 코드를 더 유지 관리하기 쉽고, 테스트하기 쉽고, 많은 경우에 더 간결하게 만들 수 있는 강력한 패러다임을 제공합니다. Python이 순수하게 함수형은 아니지만, 함수형 개념을 효과적으로 활용할 수 있는 많은 기능을 제공합니다.

38. By understanding and applying these functional programming techniques, you can write cleaner, more modular, and more robust Python code. Remember that the goal isn't to force a functional style everywhere, but to recognize when functional approaches can simplify your code and make it more readable.

이러한 함수형 프로그래밍 기법을 이해하고 적용함으로써, 더 깔끔하고, 더 모듈화되고, 더 견고한 Python 코드를 작성할 수 있습니다. 목표는 모든 곳에 함수형 스타일을 강제하는 것이 아니라, 함수형 접근법이 코드를 단순화하고 더 읽기 쉽게 만들 수 있는 시점을 인식하는 것임을 기억하세요.

