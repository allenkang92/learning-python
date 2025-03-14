# 4.9. More on Defining Functions

1. It is also possible to define functions with a variable number of arguments. There are three forms, which can be combined.

함수를 가변 개수의 인수로 정의하는 것도 가능합니다. 세 가지 형태가 있으며, 이들은 조합될 수 있습니다.

## 4.9.1. Default Argument Values

2. The most useful form is to specify a default value for one or more arguments. This creates a function that can be called with fewer arguments than it is defined to allow. For example:

가장 유용한 형태는 하나 이상의 인수에 기본값을 지정하는 것입니다. 이렇게 하면 정의된 것보다 더 적은 인수로 호출될 수 있는 함수가 생성됩니다. 예를 들어:

```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```

3. This function can be called in several ways:

이 함수는 여러 가지 방법으로 호출될 수 있습니다:

- giving only the mandatory argument: `ask_ok('Do you really want to quit?')`
- giving one of the optional arguments: `ask_ok('OK to overwrite the file?', 2)`
- or even giving all arguments: `ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')`

- 필수 인수만 제공: `ask_ok('Do you really want to quit?')`
- 선택적 인수 중 하나 제공: `ask_ok('OK to overwrite the file?', 2)`
- 또는 모든 인수 제공: `ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')`

4. This example also introduces the in keyword. This tests whether or not a sequence contains a certain value.

이 예제는 또한 in 키워드를 소개합니다. 이것은 시퀀스가 특정 값을 포함하는지 여부를 테스트합니다.

5. The default values are evaluated at the point of function definition in the defining scope, so that

기본값은 함수 정의 지점의 정의 범위에서 평가되므로

```python
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
```

6. will print 5.

5를 출력할 것입니다.

7. Important warning: The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls:

중요 경고: 기본값은 한 번만 평가됩니다. 이는 기본값이 리스트, 딕셔너리 또는 대부분의 클래스의 인스턴스와 같은 가변 객체일 때 차이가 납니다. 예를 들어, 다음 함수는 후속 호출에서 전달된 인수를 누적합니다:

```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
```

8. This will print

이것은 다음과 같이 출력합니다:

```
[1]
[1, 2]
[1, 2, 3]
```

9. If you don't want the default to be shared between subsequent calls, you can write the function like this instead:

후속 호출 간에 기본값이 공유되는 것을 원하지 않는다면, 대신 다음과 같이 함수를 작성할 수 있습니다:

```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

## 4.9.2. Keyword Arguments

10. Functions can also be called using keyword arguments of the form kwarg=value. For instance, the following function:

함수는 kwarg=value 형식의 키워드 인수를 사용하여 호출될 수도 있습니다. 예를 들어, 다음 함수:

```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
```

11. accepts one required argument (voltage) and three optional arguments (state, action, and type). This function can be called in any of the following ways:

하나의 필수 인수(voltage)와 세 개의 선택적 인수(state, action, type)를 받습니다. 이 함수는 다음 중 어떤 방법으로도 호출될 수 있습니다:

```python
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
```

12. but all the following calls would be invalid:

하지만 다음 호출은 모두 유효하지 않습니다:

```python
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
```

13. In a function call, keyword arguments must follow positional arguments. All the keyword arguments passed must match one of the arguments accepted by the function (e.g. actor is not a valid argument for the parrot function), and their order is not important. This also includes non-optional arguments (e.g. parrot(voltage=1000) is valid too). No argument may receive a value more than once. Here's an example that fails due to this restriction:

함수 호출에서 키워드 인수는 위치 인수 뒤에 와야 합니다. 전달된 모든 키워드 인수는 함수가 받는 인수 중 하나와 일치해야 하며(예: actor는 parrot 함수의 유효한 인수가 아님), 순서는 중요하지 않습니다. 이는 필수 인수도 포함합니다(예: parrot(voltage=1000)도 유효함). 어떤 인수도 값을 두 번 이상 받을 수 없습니다. 다음은 이 제한 때문에 실패하는 예입니다:

```python
>>> def function(a):
...     pass
...
>>> function(0, a=0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: function() got multiple values for argument 'a'
```

14. When a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types — dict) containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter of the form *name (described in the next subsection) which receives a tuple containing the positional arguments beyond the formal parameter list. (*name must occur before **name.) For example, if we define a function like this:

**name 형식의 최종 형식 매개변수가 있으면, 형식 매개변수에 해당하는 것을 제외한 모든 키워드 인수를 포함하는 사전(Mapping Types — dict 참조)을 받습니다. 이는 형식 매개변수 목록을 넘어선 위치 인수를 포함하는 튜플을 받는 *name 형식의 형식 매개변수(다음 하위 섹션에 설명됨)와 결합될 수 있습니다. (*name은 **name 앞에 와야 합니다.) 예를 들어, 다음과 같이 함수를 정의하면:

```python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
```

15. It could be called like this:

다음과 같이 호출할 수 있습니다:

```python
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
```

16. and of course it would print:

그리고 물론 다음과 같이 출력할 것입니다:

```
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
```

17. Note that the order in which the keyword arguments are printed is guaranteed to match the order in which they were provided in the function call.

키워드 인수가 출력되는 순서는 함수 호출에서 제공된 순서와 일치하는 것이 보장됩니다.

## 4.9.3. Special parameters

18. By default, arguments may be passed to a Python function either by position or explicitly by keyword. For readability and performance, it makes sense to restrict the way arguments can be passed so that a developer need only look at the function definition to determine if items are passed by position, by position or keyword, or by keyword.

기본적으로 인수는 위치나 명시적으로 키워드로 파이썬 함수에 전달될 수 있습니다. 가독성과 성능을 위해, 개발자가 함수 정의만 보고도 항목이 위치로, 위치나 키워드로, 또는 키워드로 전달되는지 결정할 수 있도록 인수가 전달되는 방식을 제한하는 것이 합리적입니다.

19. A function definition may look like:

함수 정의는 다음과 같을 수 있습니다:

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

20. where / and * are optional. If used, these symbols indicate the kind of parameter by how the arguments may be passed to the function: positional-only, positional-or-keyword, and keyword-only. Keyword parameters are also referred to as named parameters.

여기서 /와 *는 선택 사항입니다. 사용되면, 이 기호들은 인수가 함수에 전달되는 방식에 따른 매개변수의 종류를 나타냅니다: 위치-전용, 위치-또는-키워드, 키워드-전용. 키워드 매개변수는 명명된 매개변수라고도 합니다.

### 4.9.3.1. Positional-or-Keyword Arguments

21. If / and * are not present in the function definition, arguments may be passed to a function by position or by keyword.

함수 정의에 /와 *가 없으면, 인수는 위치나 키워드로 함수에 전달될 수 있습니다.

### 4.9.3.2. Positional-Only Parameters

22. Looking at this in a bit more detail, it is possible to mark certain parameters as positional-only. If positional-only, the parameters' order matters, and the parameters cannot be passed by keyword. Positional-only parameters are placed before a / (forward-slash). The / is used to logically separate the positional-only parameters from the rest of the parameters. If there is no / in the function definition, there are no positional-only parameters.

좀 더 자세히 살펴보면, 특정 매개변수를 위치-전용으로 표시하는 것이 가능합니다. 위치-전용인 경우, 매개변수의 순서가 중요하며, 매개변수는 키워드로 전달될 수 없습니다. 위치-전용 매개변수는 / (슬래시) 앞에 배치됩니다. /는 위치-전용 매개변수를 나머지 매개변수와 논리적으로 구분하는 데 사용됩니다. 함수 정의에 /가 없으면 위치-전용 매개변수가 없습니다.

23. Parameters following the / may be positional-or-keyword or keyword-only.

/ 다음의 매개변수는 위치-또는-키워드나 키워드-전용일 수 있습니다.

### 4.9.3.3. Keyword-Only Arguments

24. To mark parameters as keyword-only, indicating the parameters must be passed by keyword argument, place an * in the arguments list just before the first keyword-only parameter.

매개변수를 키워드-전용으로 표시하여 매개변수가 키워드 인수로 전달되어야 함을 나타내려면, 첫 번째 키워드-전용 매개변수 바로 앞의 인수 목록에 *를 배치합니다.

### 4.9.3.4. Function Examples

25. Consider the following example function definitions paying close attention to the markers / and *:

다음 예제 함수 정의에서 마커 /와 *에 주의를 기울여 보세요:

```python
>>> def standard_arg(arg):
...     print(arg)
...
>>> def pos_only_arg(arg, /):
...     print(arg)
...
>>> def kwd_only_arg(*, arg):
...     print(arg)
...
>>> def combined_example(pos_only, /, standard, *, kwd_only):
...     print(pos_only, standard, kwd_only)
```

26. The first function definition, standard_arg, the most familiar form, places no restrictions on the calling convention and arguments may be passed by position or keyword:

첫 번째 함수 정의 standard_arg는 가장 익숙한 형태로, 호출 규약에 제한을 두지 않으며 인수는 위치나 키워드로 전달될 수 있습니다:

```python
>>> standard_arg(2)
2
>>> standard_arg(arg=2)
2
```

27. The second function pos_only_arg is restricted to only use positional parameters as there is a / in the function definition:

두 번째 함수 pos_only_arg는 함수 정의에 /가 있으므로 위치 매개변수만 사용하도록 제한됩니다:

```python
>>> pos_only_arg(1)
1
>>> pos_only_arg(arg=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
```

28. The third function kwd_only_arg only allows keyword arguments as indicated by a * in the function definition:

세 번째 함수 kwd_only_arg는 함수 정의에 *가 있어 키워드 인수만 허용합니다:

```python
>>> kwd_only_arg(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given
>>> kwd_only_arg(arg=3)
3
```

29. And the last uses all three calling conventions in the same function definition:

그리고 마지막은 세 가지 호출 규약을 모두 같은 함수 정의에서 사용합니다:

```python
>>> combined_example(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() takes 2 positional arguments but 3 were given
>>> combined_example(1, 2, kwd_only=3)
1 2 3
>>> combined_example(1, standard=2, kwd_only=3)
1 2 3
>>> combined_example(pos_only=1, standard=2, kwd_only=3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'
```

30. Finally, consider this function definition which has a potential collision between the positional argument name and **kwds which has name as a key:

마지막으로, 위치 인수 name과 name을 키로 갖는 **kwds 간의 잠재적 충돌이 있는 이 함수 정의를 고려해 보세요:

```python
def foo(name, **kwds):
    return 'name' in kwds
```

31. There is no possible call that will make it return True as the keyword 'name' will always bind to the first parameter. For example:

키워드 'name'이 항상 첫 번째 매개변수에 바인딩되기 때문에, True를 반환하게 할 수 있는 호출은 없습니다. 예를 들어:

```python
>>> foo(1, **{'name': 2})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() got multiple values for argument 'name'
```

32. But using / (positional only arguments), it is possible since it allows name as a positional argument and 'name' as a key in the keyword arguments:

그러나 / (위치 전용 인수)를 사용하면, name을 위치 인수로, 'name'을 키워드 인수의 키로 허용하기 때문에 가능합니다:

```python
>>> def foo(name, /, **kwds):
...     return 'name' in kwds
...
>>> foo(1, **{'name': 2})
True
```

33. In other words, the names of positional-only parameters can be used in **kwds without ambiguity.

다시 말해, 위치-전용 매개변수의 이름은 모호함 없이 **kwds에서 사용될 수 있습니다.

### 4.9.3.5. Recap

34. The use case will determine which parameters to use in the function definition:

사용 사례에 따라 함수 정의에서 사용할 매개변수가 결정됩니다:

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
```

35. As guidance:

지침으로:

- Use positional-only if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning, if you want to enforce the order of the arguments when the function is called or if you need to take some positional parameters and arbitrary keywords.

- Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or you want to prevent users relying on the position of the argument being passed.

- For an API, use positional-only to prevent breaking API changes if the parameter's name is modified in the future.

- 매개변수의 이름을 사용자가 사용할 수 없게 하려면 위치-전용을 사용하세요. 이는 매개변수 이름에 실제 의미가 없을 때, 함수 호출 시 인수 순서를 강제하고 싶을 때, 또는 일부 위치 매개변수와 임의의 키워드를 받아야 할 때 유용합니다.

- 이름에 의미가 있고 함수 정의가 이름을 명시적으로 사용함으로써 더 이해하기 쉬울 때, 또는 사용자가 전달되는 인수의 위치에 의존하지 않게 하고 싶을 때 키워드-전용을 사용하세요.

- API의 경우, 매개변수의 이름이 향후에 수정되어도 API가 깨지지 않도록 위치-전용을 사용하세요.

## 4.9.4. Arbitrary Argument Lists

36. Finally, the least frequently used option is to specify that a function can be called with an arbitrary number of arguments. These arguments will be wrapped up in a tuple (see Tuples and Sequences). Before the variable number of arguments, zero or more normal arguments may occur.

마지막으로, 가장 덜 자주 사용되는 옵션은 함수가 임의 개수의 인수로 호출될 수 있도록 지정하는 것입니다. 이러한 인수는 튜플로 묶입니다(튜플 및 시퀀스 참조). 가변 개수의 인수 전에 0개 이상의 일반 인수가 올 수 있습니다.

```python
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
```

37. Normally, these variadic arguments will be last in the list of formal parameters, because they scoop up all remaining input arguments that are passed to the function. Any formal parameters which occur after the *args parameter are 'keyword-only' arguments, meaning that they can only be used as keywords rather than positional arguments.

일반적으로 이러한 가변 인수는 형식 매개변수 목록의 마지막에 위치합니다. 함수에 전달되는 모든 나머지 입력 인수를 모두 가져가기 때문입니다. *args 매개변수 뒤에 오는 모든 형식 매개변수는 '키워드-전용' 인수로, 위치 인수가 아닌 키워드로만 사용될 수 있습니다.

```python
>>> def concat(*args, sep="/"):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
```

## 4.9.5. Unpacking Argument Lists

38. The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments. For instance, the built-in range() function expects separate start and stop arguments. If they are not available separately, write the function call with the *-operator to unpack the arguments out of a list or tuple:

인수가 이미 리스트나 튜플에 있지만 별도의 위치 인수를 요구하는 함수 호출을 위해 풀어야 하는 역상황이 발생합니다. 예를 들어, 내장 range() 함수는 별도의 start와 stop 인수를 기대합니다. 이들이 별도로 사용할 수 없는 경우, *-연산자를 사용하여 리스트나 튜플에서 인수를 푸는 함수 호출을 작성하세요:

```python
>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]
```

39. In the same fashion, dictionaries can deliver keyword arguments with the **-operator:

같은 방식으로, 사전은 **-연산자를 사용하여 키워드 인수를 전달할 수 있습니다:

```python
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```

## 4.9.6. Lambda Expressions

40. Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: lambda a, b: a+b. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables from the containing scope:

작은 익명 함수는 lambda 키워드로 생성할 수 있습니다. 이 함수는 두 인수의 합을 반환합니다: `lambda a, b: a+b`. Lambda 함수는 함수 객체가 필요한 모든 곳에서 사용할 수 있습니다. 구문적으로 단일 표현식으로 제한됩니다. 의미적으로는 일반 함수 정의를 위한 문법적 설탕일 뿐입니다. 중첩된 함수 정의와 마찬가지로, lambda 함수는 포함하는 범위의 변수를 참조할 수 있습니다:

```python
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```

41. The above example uses a lambda expression to return a function. Another use is to pass a small function as an argument:

위의 예제는 함수를 반환하기 위해 lambda 표현식을 사용합니다. 또 다른 용도는 작은 함수를 인수로 전달하는 것입니다:

```python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

## 4.9.7. Documentation Strings

42. Here are some conventions about the content and formatting of documentation strings.

다음은 문서화 문자열의 내용과 형식에 관한 몇 가지 규칙입니다.

43. The first line should always be a short, concise summary of the object's purpose. For brevity, it should not explicitly state the object's name or type, since these are available by other means (except if the name happens to be a verb describing a function's operation). This line should begin with a capital letter and end with a period.

첫 번째 줄은 항상 객체의 목적을 간결하게 요약해야 합니다. 간결함을 위해, 객체의 이름이나 유형을 명시적으로 언급하지 않아야 합니다. 이는 다른 방법으로도 확인할 수 있기 때문입니다(이름이 함수의 작동을 설명하는 동사인 경우는 예외). 이 줄은 대문자로 시작하여 마침표로 끝나야 합니다.

44. If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description. The following lines should be one or more paragraphs describing the object's calling conventions, its side effects, etc.

문서화 문자열에 더 많은 줄이 있는 경우, 두 번째 줄은 비어 있어야 합니다. 이는 요약과 설명의 나머지 부분을 시각적으로 구분합니다. 다음 줄은 객체의 호출 규약, 부작용 등을 설명하는 하나 이상의 단락이어야 합니다.

45. The Python parser does not strip indentation from multi-line string literals in Python, so tools that process documentation have to strip indentation if desired. This is done using the following convention. The first non-blank line after the first line of the string determines the amount of indentation for the entire documentation string. (We can't use the first line since it is generally adjacent to the string's opening quotes so its indentation is not apparent in the string literal.) Whitespace "equivalent" to this indentation is then stripped from the start of all lines of the string. Lines that are indented less should not occur, but if they occur all their leading whitespace should be stripped. Equivalence of whitespace should be tested after expansion of tabs (to 8 spaces, normally).

파이썬 파서는 파이썬의 여러 줄 문자열 리터럴에서 들여쓰기를 제거하지 않으므로, 문서를 처리하는 도구는 원하는 경우 들여쓰기를 제거해야 합니다. 이는 다음 규칙을 사용하여 수행됩니다. 문자열의 첫 번째 줄 다음에 오는 첫 번째 비어있지 않은 줄이 전체 문서화 문자열에 대한 들여쓰기 양을 결정합니다. (첫 번째 줄은 일반적으로 문자열의 여는 따옴표에 인접해 있어 들여쓰기가 문자열 리터럴에서 명확하지 않기 때문에 사용할 수 없습니다.) 이 들여쓰기에 "상응하는" 공백은 문자열의 모든 줄의 시작 부분에서 제거됩니다. 덜 들여쓰기된 줄은 발생하지 않아야 하지만, 발생하면 모든 선행 공백이 제거되어야 합니다. 공백의 동등성은 탭의 확장(일반적으로 8개의 공백으로) 후에 테스트해야 합니다.

46. Here is an example of a multi-line docstring:

다음은 여러 줄 문서화 문자열의 예입니다:

```python
>>> def my_function():
...     """Do nothing, but document it.
...
...     No, really, it doesn't do anything.
...     """
...     pass
...
>>> print(my_function.__doc__)
Do nothing, but document it.

    No, really, it doesn't do anything.
```

## 4.9.8. Function Annotations

47. Function annotations are completely optional metadata information about the types used by user-defined functions (see PEP 3107 and PEP 484 for more information).

함수 주석은 사용자 정의 함수에서 사용되는 유형에 대한 완전히 선택적인 메타데이터 정보입니다(자세한 정보는 PEP 3107 및 PEP 484 참조).

48. Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no effect on any other part of the function. Parameter annotations are defined by a colon after the parameter name, followed by an expression evaluating to the value of the annotation. Return annotations are defined by a literal ->, followed by an expression, between the parameter list and the colon denoting the end of the def statement. The following example has a required argument, an optional argument, and the return value annotated:

주석은 함수의 __annotations__ 속성에 사전으로 저장되며, 함수의 다른 부분에는 영향을 미치지 않습니다. 매개변수 주석은 매개변수 이름 뒤에 콜론을 붙이고 주석의 값으로 평가되는 표현식이 따라옵니다. 반환 주석은 매개변수 목록과 def 문의 끝을 나타내는 콜론 사이에 리터럴 ->와 표현식으로 정의됩니다. 다음 예제는 필수 인수, 선택적 인수 및 반환 값에 주석이 달려 있습니다:

```python
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```

## 4.10. Intermezzo: Coding Style

49. Now that you are about to write longer, more complex pieces of Python, it is a good time to talk about coding style. Most languages can be written (or more concise, formatted) in different styles; some are more readable than others. Making it easy for others to read your code is always a good idea, and adopting a nice coding style helps tremendously for that.

이제 더 길고 복잡한 파이썬 코드를 작성하려고 하므로, 코딩 스타일에 대해 이야기할 좋은 시간입니다. 대부분의 언어는 다양한 스타일로 작성(또는 더 간결하게, 형식화)될 수 있습니다. 일부는 다른 것보다 더 읽기 쉽습니다. 다른 사람이 당신의 코드를 쉽게 읽을 수 있도록 하는 것은 항상 좋은 아이디어이며, 좋은 코딩 스타일을 채택하면 이를 크게 도울 수 있습니다.

50. For Python, PEP 8 has emerged as the style guide that most projects adhere to; it promotes a very readable and eye-pleasing coding style. Every Python developer should read it at some point; here are the most important points extracted for you:

파이썬의 경우, PEP 8이 대부분의 프로젝트가 준수하는 스타일 가이드로 등장했습니다. 이는 매우 읽기 쉽고 보기 좋은 코딩 스타일을 장려합니다. 모든 파이썬 개발자는 어느 시점에서 이를 읽어야 합니다. 여기에 가장 중요한 점들을 추출해 놓았습니다:

51. Use 4-space indentation, and no tabs.

4칸 들여쓰기를 사용하고, 탭을 사용하지 마세요.

52. 4 spaces are a good compromise between small indentation (allows greater nesting depth) and large indentation (easier to read). Tabs introduce confusion, and are best left out.

4칸 들여쓰기는 작은 들여쓰기(더 큰 중첩 깊이 허용)와 큰 들여쓰기(읽기 쉬움) 사이의 좋은 타협점입니다. 탭은 혼란을 초래하므로, 사용하지 않는 것이 좋습니다.

53. Wrap lines so that they don't exceed 79 characters.

줄이 79자를 초과하지 않도록 줄 바꿈을 하세요.

54. This helps users with small displays and makes it possible to have several code files side-by-side on larger displays.

이는 작은 디스플레이를 사용하는 사용자를 돕고, 큰 디스플레이에서 여러 코드 파일을 나란히 볼 수 있게 합니다.

55. Use blank lines to separate functions and classes, and larger blocks of code inside functions.

함수와 클래스, 그리고 함수 내의 더 큰 코드 블록을 구분하기 위해 빈 줄을 사용하세요.

56. When possible, put comments on a line of their own.

가능하면 주석을 별도의 줄에 배치하세요.

57. Use docstrings.

문서화 문자열을 사용하세요.

58. Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4).

연산자 주변과 쉼표 뒤에 공백을 사용하세요. 그러나 괄호 구조 안쪽에는 직접적으로 사용하지 마세요: `a = f(1, 2) + g(3, 4)`.

59. Name your classes and functions consistently; the convention is to use UpperCamelCase for classes and lowercase_with_underscores for functions and methods. Always use self as the name for the first method argument (see A First Look at Classes for more on classes and methods).

클래스와 함수의 이름을 일관되게 지으세요. 관례는 클래스에는 UpperCamelCase를, 함수와 메서드에는 lowercase_with_underscores를 사용하는 것입니다. 첫 번째 메서드 인수의 이름으로 항상 self를 사용하세요(클래스와 메서드에 대한 자세한 내용은 클래스 첫 인상 참조).

60. Don't use fancy encodings if your code is meant to be used in international environments. Python's default, UTF-8, or even plain ASCII work best in any case.

코드가 국제적 환경에서 사용될 예정이라면 화려한 인코딩을 사용하지 마세요. 어떤 경우든 파이썬의 기본인 UTF-8 또는 일반 ASCII가 가장 잘 작동합니다.

61. Likewise, don't use non-ASCII characters in identifiers if there is only the slightest chance people speaking a different language will read or maintain the code.

마찬가지로, 다른 언어를 사용하는 사람이 코드를 읽거나 유지 관리할 가능성이 조금이라도 있다면 식별자에 비ASCII 문자를 사용하지 마세요.

**Footnotes**

[1] 사실, 객체 참조에 의한 호출이 더 나은 설명일 것입니다. 가변 객체가 전달되는 경우, 호출자는 피호출자가 그것에 가하는 모든 변경(리스트에 삽입된 항목 등)을 볼 수 있기 때문입니다.
