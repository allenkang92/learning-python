# 4. More Control Flow Tools

1. As well as the while statement just introduced, Python uses a few more that we will encounter in this chapter.

이전에 소개한 while 문과 마찬가지로, 파이썬은 이 장에서 살펴볼 몇 가지 더 많은 구문을 사용합니다.

## 4.1. if Statements

2. Perhaps the most well-known statement type is the if statement. For example:

아마도 가장 잘 알려진 구문 유형은 if 구문일 것입니다. 예를 들어:

```python
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More
```

3. There can be zero or more elif parts, and the else part is optional. The keyword 'elif' is short for 'else if', and is useful to avoid excessive indentation. An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages.

elif 부분은 없거나 여러 개일 수 있으며, else 부분은 선택 사항입니다. 'elif' 키워드는 'else if'의 줄임말이며, 과도한 들여쓰기를 방지하는 데 유용합니다. if ... elif ... elif ... 시퀀스는 다른 언어에서 볼 수 있는 switch 또는 case 문을 대체합니다.

4. If you're comparing the same value to several constants, or checking for specific types or attributes, you may also find the match statement useful. For more details see match Statements.

동일한 값을 여러 상수와 비교하거나 특정 유형 또는 속성을 확인하는 경우, match 구문이 유용할 수 있습니다. 자세한 내용은 match 구문을 참조하세요.

## 4.2. for Statements

5. The for statement in Python differs a bit from what you may be used to in C or Pascal. Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C), Python's for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence. For example (no pun intended):

파이썬의 for 구문은 C나 Pascal에서 사용하던 것과 약간 다릅니다. 항상 숫자의 산술 진행(Pascal과 같이)을 반복하거나, 사용자에게 반복 단계와 중단 조건을 모두 정의할 수 있는 능력을 제공하는(C와 같이) 대신, 파이썬의 for 구문은 시퀀스(리스트나 문자열)의 항목을 시퀀스에 나타나는 순서대로 반복합니다. 예를 들어(말장난은 의도하지 않았습니다):

```python
>>> # Measure some strings:
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12
```

6. Code that modifies a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:

같은 컬렉션을 반복하는 동안 해당 컬렉션을 수정하는 코드는 올바르게 작성하기 까다로울 수 있습니다. 대신, 일반적으로 컬렉션의 복사본을 반복하거나 새 컬렉션을 만드는 것이 더 간단합니다:

```python
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```

## 4.3. The range() Function

7. If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:

숫자 시퀀스를 반복해야 하는 경우, 내장 함수 range()가 유용합니다. 이 함수는 산술 진행을 생성합니다:

```python
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
```

8. The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices for items of a sequence of length 10. It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the 'step'):

지정된 종료 지점은 생성된 시퀀스의 일부가 아닙니다. range(10)은 10개의 값을 생성하며, 이는 길이가 10인 시퀀스 항목의 합법적인 인덱스입니다. 범위가 다른 숫자에서 시작하도록 하거나, 다른 증가량을 지정할 수 있습니다(음수도 가능하며, 이를 '단계'라고 부르기도 합니다):

```python
>>> list(range(5, 10))
[5, 6, 7, 8, 9]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(-10, -100, -30))
[-10, -40, -70]
```

9. To iterate over the indices of a sequence, you can combine range() and len() as follows:

시퀀스의 인덱스를 반복하려면 다음과 같이 range()와 len()을 결합할 수 있습니다:

```python
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
```

10. In most such cases, however, it is convenient to use the enumerate() function, see Looping Techniques.

그러나 대부분의 이러한 경우에는 enumerate() 함수를 사용하는 것이 편리합니다. 루핑 기법을 참조하세요.

11. A strange thing happens if you just print a range:

range를 그냥 출력하면 이상한 일이 발생합니다:

```python
>>> range(10)
range(0, 10)
```

12. In many ways the object returned by range() behaves as if it is a list, but in fact it isn't. It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn't really make the list, thus saving space.

range()가 반환하는 객체는 여러 면에서 마치 리스트인 것처럼 작동하지만 실제로는 그렇지 않습니다. 이 객체는 반복할 때 원하는 시퀀스의 연속 항목을 반환하지만, 실제로 리스트를 만들지 않기 때문에 공간을 절약합니다.

13. We say such an object is iterable, that is, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted. We have seen that the for statement is such a construct, while an example of a function that takes an iterable is sum():

우리는 이러한 객체를 반복 가능(iterable)하다고 말합니다. 즉, 공급이 소진될 때까지 연속적인 항목을 얻을 수 있는 대상을 기대하는 함수와 구성에 적합합니다. for 문이 이러한 구성이라는 것을 보았으며, 반복 가능한 객체를 받는 함수의 예는 sum() 입니다:

```python
>>> sum(range(4))  # 0 + 1 + 2 + 3
6
```

14. Later we will see more functions that return iterables and take iterables as arguments. In chapter Data Structures, we will discuss in more detail about list().

나중에 우리는 반복 가능한 객체를 반환하고 인수로 받는 더 많은 함수를 볼 것입니다. 데이터 구조 장에서는 list()에 대해 더 자세히 논의할 것입니다.

## 4.4. break and continue Statements

15. The break statement breaks out of the innermost enclosing for or while loop:

break 문은 가장 안쪽의 for 또는 while 루프를 빠져나갑니다:

```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(f"{n} equals {x} * {n//x}")
...             break
...
4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3
```

16. The continue statement continues with the next iteration of the loop:

continue 문은 루프의 다음 반복을 계속합니다:

```python
>>> for num in range(2, 10):
...     if num % 2 == 0:
...         print(f"Found an even number {num}")
...         continue
...     print(f"Found an odd number {num}")
...
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
```

## 4.5. else Clauses on Loops

17. In a for or while loop the break statement may be paired with an else clause. If the loop finishes without executing the break, the else clause executes.

for 또는 while 루프에서 break 문은 else 절과 쌍을 이룰 수 있습니다. 루프가 break를 실행하지 않고 완료되면 else 절이 실행됩니다.

18. In a for loop, the else clause is executed after the loop finishes its final iteration, that is, if no break occurred.

for 루프에서 else 절은 루프가 마지막 반복을 완료한 후, 즉 break가 발생하지 않은 경우에 실행됩니다.

19. In a while loop, it's executed after the loop's condition becomes false.

while 루프에서는 루프의 조건이 거짓이 된 후에 실행됩니다.

20. In either kind of loop, the else clause is not executed if the loop was terminated by a break. Of course, other ways of ending the loop early, such as a return or a raised exception, will also skip execution of the else clause.

어떤 종류의 루프에서든, 루프가 break에 의해 종료된 경우 else 절은 실행되지 않습니다. 물론 return이나 예외 발생과 같은 다른 방법으로 루프를 일찍 종료하면 else 절의 실행도 건너뜁니다.

21. This is exemplified in the following for loop, which searches for prime numbers:

다음 for 루프에서는 소수를 검색하는 예시를 보여줍니다:

```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

22. (Yes, this is the correct code. Look closely: the else clause belongs to the for loop, not the if statement.)

(네, 이것은 올바른 코드입니다. 자세히 보세요: else 절은 if 문이 아니라 for 루프에 속합니다.)

23. One way to think of the else clause is to imagine it paired with the if inside the loop. As the loop executes, it will run a sequence like if/if/if/else. The if is inside the loop, encountered a number of times. If the condition is ever true, a break will happen. If the condition is never true, the else clause outside the loop will execute.

else 절을 생각하는 한 가지 방법은 루프 내부의 if와 짝을 이룬다고 상상하는 것입니다. 루프가 실행되면 if/if/if/else와 같은 시퀀스를 실행합니다. if는 루프 내부에 있으며, 여러 번 만납니다. 조건이 한 번이라도 참이면 break가 발생합니다. 조건이 한 번도 참이 아니면 루프 외부의 else 절이 실행됩니다.

24. When used with a loop, the else clause has more in common with the else clause of a try statement than it does with that of if statements: a try statement's else clause runs when no exception occurs, and a loop's else clause runs when no break occurs. For more on the try statement and exceptions, see Handling Exceptions.

루프와 함께 사용할 때, else 절은 if 문의 else 절보다는 try 문의 else 절과 더 많은 공통점이 있습니다: try 문의 else 절은 예외가 발생하지 않을 때 실행되며, 루프의 else 절은 break가 발생하지 않을 때 실행됩니다. try 문과 예외에 대한 자세한 내용은 예외 처리를 참조하세요.

## 4.6. pass Statements

25. The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. For example:

pass 문은 아무것도 하지 않습니다. 구문적으로 명령문이 필요하지만 프로그램이 어떤 동작도 필요로 하지 않을 때 사용될 수 있습니다. 예를 들어:

```python
>>> while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
```

26. This is commonly used for creating minimal classes:

이것은 일반적으로 최소한의 클래스를 만드는 데 사용됩니다:

```python
>>> class MyEmptyClass:
...     pass
```

27. Another place pass can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level. The pass is silently ignored:

pass가 사용될 수 있는 또 다른 장소는 새로운 코드를 작업할 때 함수나 조건문 본문의 자리 표시자로서입니다. 이를 통해 더 추상적인 수준에서 생각을 계속할 수 있습니다. pass는 조용히 무시됩니다:

```python
>>> def initlog(*args):
...     pass   # Remember to implement this!
```

## 4.7. match Statements

28. A match statement takes an expression and compares its value to successive patterns given as one or more case blocks. This is superficially similar to a switch statement in C, Java or JavaScript (and many other languages), but it's more similar to pattern matching in languages like Rust or Haskell. Only the first pattern that matches gets executed and it can also extract components (sequence elements or object attributes) from the value into variables.

match 문은 표현식을 가져와서 그 값을 하나 이상의 case 블록으로 제공되는 연속적인 패턴과 비교합니다. 이것은 겉보기에는 C, Java 또는 JavaScript(및 많은 다른 언어)의 switch 문과 비슷하지만, Rust나 Haskell과 같은 언어의 패턴 매칭과 더 유사합니다. 일치하는 첫 번째 패턴만 실행되며, 값에서 구성 요소(시퀀스 요소 또는 객체 속성)를 변수로 추출할 수도 있습니다.

29. The simplest form compares a subject value against one or more literals:

가장 간단한 형태는 주체 값을 하나 이상의 리터럴과 비교합니다:

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

30. Note the last block: the "variable name" _ acts as a wildcard and never fails to match. If no case matches, none of the branches is executed.

마지막 블록에 주목하세요: "변수 이름" _는 와일드카드 역할을 하며 항상 일치합니다. 일치하는 case가 없으면 어떤 분기도 실행되지 않습니다.

31. You can combine several literals in a single pattern using | ("or"):

| ("or")를 사용하여 단일 패턴에서 여러 리터럴을 결합할 수 있습니다:

```python
case 401 | 403 | 404:
    return "Not allowed"
```

32. Patterns can look like unpacking assignments, and can be used to bind variables:

패턴은 언패킹 할당처럼 보일 수 있으며, 변수를 바인딩하는 데 사용될 수 있습니다:

```python
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```

33. Study that one carefully! The first pattern has two literals, and can be thought of as an extension of the literal pattern shown above. But the next two patterns combine a literal and a variable, and the variable binds a value from the subject (point). The fourth pattern captures two values, which makes it conceptually similar to the unpacking assignment (x, y) = point.

그것을 주의 깊게 살펴보세요! 첫 번째 패턴에는 두 개의 리터럴이 있으며, 위에서 보여준 리터럴 패턴의 확장으로 생각할 수 있습니다. 그러나 다음 두 패턴은 리터럴과 변수를 결합하고, 변수는 주체(point)에서 값을 바인딩합니다. 네 번째 패턴은 두 개의 값을 캡처하는데, 이는 개념적으로 언패킹 할당 (x, y) = point와 유사합니다.

34. If you are using classes to structure your data you can use the class name followed by an argument list resembling a constructor, but with the ability to capture attributes into variables:

데이터를 구조화하기 위해 클래스를 사용하는 경우, 생성자와 유사한 인수 목록 뒤에 클래스 이름을 사용할 수 있지만, 속성을 변수로 캡처하는 기능도 있습니다:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
```

35. You can use positional parameters with some builtin classes that provide an ordering for their attributes (e.g. dataclasses). You can also define a specific position for attributes in patterns by setting the __match_args__ special attribute in your classes. If it's set to ("x", "y"), the following patterns are all equivalent (and all bind the y attribute to the var variable):

속성에 대한 순서를 제공하는 일부 내장 클래스(예: dataclasses)와 함께 위치 매개변수를 사용할 수 있습니다. 클래스에서 __match_args__ 특수 속성을 설정하여 패턴에서 속성의 특정 위치를 정의할 수도 있습니다. 이것이 ("x", "y")로 설정되면 다음 패턴은 모두 동등합니다(그리고 모두 y 속성을 var 변수에 바인딩합니다):

```python
Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)
```

36. A recommended way to read patterns is to look at them as an extended form of what you would put on the left of an assignment, to understand which variables would be set to what. Only the standalone names (like var above) are assigned to by a match statement. Dotted names (like foo.bar), attribute names (the x= and y= above) or class names (recognized by the "(…)" next to them like Point above) are never assigned to.

패턴을 읽는 권장 방법은 할당의 왼쪽에 넣을 것의 확장된 형태로 보는 것입니다. 이렇게 하면 어떤 변수가 무엇으로 설정될지 이해할 수 있습니다. match 문에 의해 할당되는 것은 독립 이름(위의 var와 같은)뿐입니다. 점이 있는 이름(foo.bar와 같은), 속성 이름(위의 x= 및 y=) 또는 클래스 이름(위의 Point와 같이 옆에 있는 "(…)"로 인식)에는 할당되지 않습니다.

37. Patterns can be arbitrarily nested. For example, if we have a short list of Points, with __match_args__ added, we could match it like this:

패턴은 임의로 중첩될 수 있습니다. 예를 들어, __match_args__가 추가된 Point들의 짧은 리스트가 있다면, 다음과 같이 일치시킬 수 있습니다:

```python
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
```

38. We can add an if clause to a pattern, known as a "guard". If the guard is false, match goes on to try the next case block. Note that value capture happens before the guard is evaluated:

"가드"라고 알려진 if 절을 패턴에 추가할 수 있습니다. 가드가 거짓이면, match는 다음 case 블록을 시도합니다. 가드가 평가되기 전에 값 캡처가 발생한다는 점에 유의하세요:

```python
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")
```

39. Several other key features of this statement:

이 문장의 몇 가지 다른 주요 기능:

40. Like unpacking assignments, tuple and list patterns have exactly the same meaning and actually match arbitrary sequences. An important exception is that they don't match iterators or strings.

언패킹 할당과 마찬가지로, 튜플과 리스트 패턴은 정확히 같은 의미를 가지며 실제로 임의의 시퀀스와 일치합니다. 중요한 예외는 이터레이터나 문자열과는 일치하지 않는다는 것입니다.

41. Sequence patterns support extended unpacking: [x, y, *rest] and (x, y, *rest) work similar to unpacking assignments. The name after * may also be _, so (x, y, *_) matches a sequence of at least two items without binding the remaining items.

시퀀스 패턴은 확장 언패킹을 지원합니다: [x, y, *rest]와 (x, y, *rest)는 언패킹 할당과 유사하게 작동합니다. * 다음의 이름은 _일 수도 있으므로, (x, y, *_)는 나머지 항목을 바인딩하지 않고 적어도 두 개의 항목이 있는 시퀀스와 일치합니다.

42. Mapping patterns: {"bandwidth": b, "latency": l} captures the "bandwidth" and "latency" values from a dictionary. Unlike sequence patterns, extra keys are ignored. An unpacking like **rest is also supported. (But **_ would be redundant, so it is not allowed.)

매핑 패턴: {"bandwidth": b, "latency": l}는 사전에서 "bandwidth"와 "latency" 값을 캡처합니다. 시퀀스 패턴과 달리 추가 키는 무시됩니다. **rest와 같은 언패킹도 지원됩니다. (그러나 **_는 중복되므로 허용되지 않습니다.)

43. Subpatterns may be captured using the as keyword:

하위 패턴은 as 키워드를 사용하여 캡처할 수 있습니다:

```python
case (Point(x1, y1), Point(x2, y2) as p2): ...
```

44. will capture the second element of the input as p2 (as long as the input is a sequence of two points)

입력의 두 번째 요소를 p2로 캡처합니다(입력이 두 개의 포인트 시퀀스인 경우에 한함)

45. Most literals are compared by equality, however the singletons True, False and None are compared by identity.

대부분의 리터럴은 등호로 비교되지만, 싱글톤 True, False 및 None은 ID로 비교됩니다.

46. Patterns may use named constants. These must be dotted names to prevent them from being interpreted as capture variable:

패턴은 명명된 상수를 사용할 수 있습니다. 이들은 캡처 변수로 해석되는 것을 방지하기 위해 점이 있는 이름이어야 합니다:

```python
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
```

47. For a more detailed explanation and additional examples, you can look into PEP 636 which is written in a tutorial format.

더 자세한 설명과 추가 예제는 튜토리얼 형식으로 작성된 PEP 636을 참조할 수 있습니다.

## 4.8. Defining Functions

48. We can create a function that writes the Fibonacci series to an arbitrary boundary:

임의의 경계까지 피보나치 수열을 작성하는 함수를 만들 수 있습니다:

```python
>>> def fib(n):    # write Fibonacci series less than n
...     """Print a Fibonacci series less than n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Now call the function we just defined:
>>> fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```

49. The keyword def introduces a function definition. It must be followed by the function name and the parenthesized list of formal parameters. The statements that form the body of the function start at the next line, and must be indented.

키워드 def는 함수 정의를 소개합니다. 함수 이름과 괄호 안의 형식 매개변수 목록이 뒤따라야 합니다. 함수의 본문을 형성하는 명령문은 다음 줄에서 시작하며, 들여쓰기 되어야 합니다.

50. The first statement of the function body can optionally be a string literal; this string literal is the function's documentation string, or docstring. (More about docstrings can be found in the section Documentation Strings.) There are tools which use docstrings to automatically produce online or printed documentation, or to let the user interactively browse through code; it's good practice to include docstrings in code that you write, so make a habit of it.

함수 본문의 첫 번째 문장은 선택적으로 문자열 리터럴일 수 있습니다. 이 문자열 리터럴은 함수의 문서화 문자열, 즉 docstring입니다. (docstring에 대한 자세한 내용은 문서화 문자열 섹션에서 찾을 수 있습니다.) docstring을 사용하여 자동으로 온라인이나 인쇄된 문서를 생성하거나, 사용자가 대화식으로 코드를 탐색할 수 있게 하는 도구들이 있습니다. 작성하는 코드에 docstring을 포함하는 것은 좋은 관행이므로, 습관을 들이세요.

51. The execution of a function introduces a new symbol table used for the local variables of the function. More precisely, all variable assignments in a function store the value in the local symbol table; whereas variable references first look in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names. Thus, global variables and variables of enclosing functions cannot be directly assigned a value within a function (unless, for global variables, named in a global statement, or, for variables of enclosing functions, named in a nonlocal statement), although they may be referenced.

함수의 실행은 함수의 지역 변수에 사용되는 새로운 기호 테이블을 도입합니다. 더 정확히 말하면, 함수 내의 모든 변수 할당은 지역 기호 테이블에 값을 저장합니다. 반면에 변수 참조는 먼저 지역 기호 테이블에서 찾고, 그다음 둘러싸는 함수의 지역 기호 테이블에서 찾고, 그다음 전역 기호 테이블에서 찾고, 마지막으로 내장 이름 테이블에서 찾습니다. 따라서 전역 변수와 둘러싸는 함수의 변수는 함수 내에서 직접 값을 할당할 수 없습니다(전역 변수의 경우 global 문에 명명되거나, 둘러싸는 함수의 변수의 경우 nonlocal 문에 명명되지 않는 한). 그러나 참조는 가능합니다.

52. The actual parameters (arguments) to a function call are introduced in the local symbol table of the called function when it is called; thus, arguments are passed using call by value (where the value is always an object reference, not the value of the object). [1] When a function calls another function, or calls itself recursively, a new local symbol table is created for that call.

함수 호출에 대한 실제 매개변수(인수)는 호출될 때 호출된 함수의 지역 기호 테이블에 도입됩니다. 따라서 인수는 값에 의한 호출을 사용하여 전달됩니다(여기서 값은 항상 객체 참조이며, 객체의 값이 아닙니다). [1] 함수가 다른 함수를 호출하거나 자신을 재귀적으로 호출할 때, 그 호출을 위한 새로운 지역 기호 테이블이 생성됩니다.

53. A function definition associates the function name with the function object in the current symbol table. The interpreter recognizes the object pointed to by that name as a user-defined function. Other names can also point to that same function object and can also be used to access the function:

함수 정의는 현재 기호 테이블에서 함수 이름을 함수 객체와 연관시킵니다. 인터프리터는 그 이름이 가리키는 객체를 사용자 정의 함수로 인식합니다. 다른 이름들도 동일한 함수 객체를 가리킬 수 있으며, 함수에 접근하는 데 사용될 수 있습니다:

```python
>>> fib
<function fib at 10042ed0>
>>> f = fib
>>> f(100)
0 1 1 2 3 5 8 13 21 34 55 89
```

54. Coming from other languages, you might object that fib is not a function but a procedure since it doesn't return a value. In fact, even functions without a return statement do return a value, albeit a rather boring one. This value is called None (it's a built-in name). Writing the value None is normally suppressed by the interpreter if it would be the only value written. You can see it if you really want to using print():

다른 언어에서 온 사람들은 fib가 값을 반환하지 않기 때문에 함수가 아니라 프로시저라고 반박할 수 있습니다. 사실, return 문이 없는 함수도 값을 반환하지만, 다소 지루한 값입니다. 이 값은 None(내장 이름)이라고 합니다. None 값을 쓰는 것은 일반적으로 그것이 쓰여질 유일한 값이라면 인터프리터에 의해 억제됩니다. 정말로 보고 싶다면 print()를 사용하여 볼 수 있습니다:

```python
>>> fib(0)
>>> print(fib(0))
None
```

55. It is simple to write a function that returns a list of the numbers of the Fibonacci series, instead of printing it:

피보나치 수열의 숫자 목록을 출력하는 대신 반환하는 함수를 작성하는 것은 간단합니다:

```python
>>> def fib2(n):  # return Fibonacci series up to n
...     """Return a list containing the Fibonacci series up to n."""
...     result = []
...     a, b = 0, 1
...     while a < n:
...         result.append(a)    # see below
...         a, b = b, a+b
...     return result
...
>>> f100 = fib2(100)    # call it
>>> f100                # write the result
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

56. This example, as usual, demonstrates some new Python features:

이 예제는 평소와 같이 몇 가지 새로운 파이썬 기능을 보여줍니다:

57. The return statement returns with a value from a function. return without an expression argument returns None. Falling off the end of a function also returns None.

return 문은 함수에서 값을 반환합니다. 표현식 인수 없는 return은 None을 반환합니다. 함수의 끝에 도달하는 것도 None을 반환합니다.

58. The statement result.append(a) calls a method of the list object result. A method is a function that 'belongs' to an object and is named obj.methodname, where obj is some object (this may be an expression), and methodname is the name of a method that is defined by the object's type. Different types define different methods. Methods of different types may have the same name without causing ambiguity. (It is possible to define your own object types and methods, using classes, see Classes) The method append() shown in the example is defined for list objects; it adds a new element at the end of the list. In this example it is equivalent to result = result + [a], but more efficient.

명령문 result.append(a)는 리스트 객체 result의 메서드를 호출합니다. 메서드는 객체에 '속하는' 함수이며 obj.methodname으로 명명됩니다. 여기서 obj는 어떤 객체(이것은 표현식일 수 있음)이고, methodname은 객체의 유형에 의해 정의된 메서드의 이름입니다. 서로 다른 유형은 서로 다른 메서드를 정의합니다. 서로 다른 유형의 메서드는 모호함을 일으키지 않고 같은 이름을 가질 수 있습니다. (클래스를 사용하여 자신만의 객체 유형과 메서드를 정의하는 것이 가능합니다. 클래스를 참조하세요) 예제에 보이는 append() 메서드는 리스트 객체에 대해 정의됩니다. 리스트의 끝에 새 요소를 추가합니다. 이 예제에서는 result = result + [a]와 동등하지만 더 효율적입니다.
