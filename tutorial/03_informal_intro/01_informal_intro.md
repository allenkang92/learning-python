# 3. An Informal Introduction to Python

1. In the following examples, input and output are distinguished by the presence or absence of prompts (>>> and …): to repeat the example, you must type everything after the prompt, when the prompt appears; lines that do not begin with a prompt are output from the interpreter. Note that a secondary prompt on a line by itself in an example means you must type a blank line; this is used to end a multi-line command.

다음 예제들에서는 프롬프트(>>> 및 …)의 유무에 따라 입력과 출력을 구분합니다. 예제를 따라하려면 프롬프트가 나타날 때 프롬프트 다음에 모든 것을 입력해야 합니다. 프롬프트로 시작하지 않는 줄은 인터프리터의 출력입니다. 예제에서 보조 프롬프트만 있는 줄은 빈 줄을 입력해야 함을 의미합니다. 이는 여러 줄 명령을 종료하는 데 사용됩니다.

2. You can toggle the display of prompts and output by clicking on >>> in the upper-right corner of an example box. If you hide the prompts and output for an example, then you can easily copy and paste the input lines into your interpreter.

예제 상자의 오른쪽 상단에 있는 >>>를 클릭하여 프롬프트와 출력 표시를 전환할 수 있습니다. 예제의 프롬프트와 출력을 숨기면 입력 줄을 인터프리터에 쉽게 복사하여 붙여넣을 수 있습니다.

3. Many of the examples in this manual, even those entered at the interactive prompt, include comments. Comments in Python start with the hash character, #, and extend to the end of the physical line. A comment may appear at the start of a line or following whitespace or code, but not within a string literal. A hash character within a string literal is just a hash character. Since comments are to clarify code and are not interpreted by Python, they may be omitted when typing in examples.

이 설명서의 많은 예제는 대화형 프롬프트에서 입력한 예제라도 주석을 포함합니다. 파이썬에서 주석은 해시 문자(#)로 시작하여 물리적 줄의 끝까지 이어집니다. 주석은 줄의 시작 부분이나 공백 또는 코드 다음에 올 수 있지만 문자열 리터럴 내에는 올 수 없습니다. 문자열 리터럴 내의 해시 문자는 단지 해시 문자일 뿐입니다. 주석은 코드를 명확히 하기 위한 것이며 파이썬이 해석하지 않으므로, 예제를 입력할 때 생략할 수 있습니다.

4. Some examples:

몇 가지 예:

```python
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
```

## 3.1. Using Python as a Calculator

## 3.1.1. Numbers

5. The interpreter acts as a simple calculator: you can type an expression at it and it will write the value. Expression syntax is straightforward: the operators +, -, * and / can be used to perform arithmetic; parentheses (()) can be used for grouping. For example:

인터프리터는 간단한 계산기 역할을 합니다: 표현식을 입력하면 값을 출력합니다. 표현식 구문은 간단합니다: 연산자 +, -, *, /를 사용하여 산술 연산을 수행할 수 있으며, 괄호(())를 사용하여 그룹화할 수 있습니다. 예를 들어:

```python
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating-point number
1.6
```

6. The integer numbers (e.g. 2, 4, 20) have type int, the ones with a fractional part (e.g. 5.0, 1.6) have type float. We will see more about numeric types later in the tutorial.

정수(예: 2, 4, 20)는 int 타입이고, 소수부가 있는 수(예: 5.0, 1.6)는 float 타입입니다. 숫자 타입에 대해서는 이 튜토리얼의 후반부에서 더 자세히 알아볼 것입니다.

7. Division (/) always returns a float. To do floor division and get an integer result you can use the // operator; to calculate the remainder you can use %:

나눗셈(/)은 항상 float을 반환합니다. 정수 결과를 얻기 위한 몫 나눗셈은 // 연산자를 사용할 수 있으며, 나머지를 계산하려면 %를 사용할 수 있습니다:

```python
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # floored quotient * divisor + remainder
17
```

8. With Python, it is possible to use the ** operator to calculate powers [1]:

파이썬에서는 ** 연산자를 사용하여 거듭제곱을 계산할 수 있습니다 [1]:

```python
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128
```

9. The equal sign (=) is used to assign a value to a variable. Afterwards, no result is displayed before the next interactive prompt:

등호(=)는 변수에 값을 할당하는 데 사용됩니다. 그 후에는 다음 대화형 프롬프트 전에 결과가 표시되지 않습니다:

```python
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```

10. If a variable is not "defined" (assigned a value), trying to use it will give you an error:

변수가 "정의되지 않은"(값이 할당되지 않은) 경우, 사용하려고 하면 오류가 발생합니다:

```python
>>> n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
```

11. There is full support for floating point; operators with mixed type operands convert the integer operand to floating point:

부동 소수점에 대한 전체 지원이 있습니다. 혼합 유형 피연산자가 있는 연산자는 정수 피연산자를 부동 소수점으로 변환합니다:

```python
>>> 4 * 3.75 - 1
14.0
```

12. In interactive mode, the last printed expression is assigned to the variable _. This means that when you are using Python as a desk calculator, it is somewhat easier to continue calculations, for example:

대화형 모드에서는 마지막으로 출력된 표현식이 변수 _에 할당됩니다. 이는 파이썬을 책상 계산기로 사용할 때 계산을 계속하기가 다소 쉽다는 것을 의미합니다. 예를 들어:

```python
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

13. This variable should be treated as read-only by the user. Don't explicitly assign a value to it — you would create an independent local variable with the same name masking the built-in variable with its magic behavior.

이 변수는 사용자가 읽기 전용으로 취급해야 합니다. 명시적으로 값을 할당하지 마세요 - 마법 같은 동작을 하는 내장 변수를 가리는 동일한 이름의 독립적인 지역 변수를 생성하게 됩니다.

14. In addition to int and float, Python supports other types of numbers, such as Decimal and Fraction. Python also has built-in support for complex numbers, and uses the j or J suffix to indicate the imaginary part (e.g. 3+5j).

int와 float 외에도 파이썬은 Decimal 및 Fraction과 같은 다른 유형의 숫자를 지원합니다. 파이썬은 또한 복소수에 대한 내장 지원이 있으며, j 또는 J 접미사를 사용하여 허수부를 나타냅니다(예: 3+5j).

## 3.1.2. Text

15. Python can manipulate text (represented by type str, so-called "strings") as well as numbers. This includes characters "!", words "rabbit", names "Paris", sentences "Got your back.", etc. "Yay! :)". They can be enclosed in single quotes ('...') or double quotes ("...") with the same result [2].

파이썬은 숫자뿐만 아니라 텍스트(타입 str, 소위 "문자열"로 표현됨)도 조작할 수 있습니다. 여기에는 문자 "!", 단어 "rabbit", 이름 "Paris", 문장 "Got your back.", 등 "Yay! :)"가 포함됩니다. 이들은 동일한 결과로 작은 따옴표('...')나 큰 따옴표("...")로 둘러싸일 수 있습니다 [2].

```python
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> "Paris rabbit got your back :)! Yay!"  # double quotes
'Paris rabbit got your back :)! Yay!'
>>> '1975'  # digits and numerals enclosed in quotes are also strings
'1975'
```

16. To quote a quote, we need to "escape" it, by preceding it with \. Alternatively, we can use the other type of quotation marks:

따옴표를 인용하려면 \를 앞에 붙여 "이스케이프"해야 합니다. 또는 다른 유형의 따옴표를 사용할 수 있습니다:

```python
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
```

17. In the Python shell, the string definition and output string can look different. The print() function produces a more readable output, by omitting the enclosing quotes and by printing escaped and special characters:

파이썬 셸에서는 문자열 정의와 출력 문자열이 다르게 보일 수 있습니다. print() 함수는 둘러싸는 따옴표를 생략하고 이스케이프된 특수 문자를 출력하여 더 읽기 쉬운 출력을 생성합니다:

```python
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), special characters are included in the string
'First line.\nSecond line.'
>>> print(s)  # with print(), special characters are interpreted, so \n produces new line
First line.
Second line.
```

18. If you don't want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:

\로 시작하는 문자를 특수 문자로 해석하지 않으려면 첫 따옴표 앞에 r을 추가하여 원시 문자열을 사용할 수 있습니다:

```python
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

19. There is one subtle aspect to raw strings: a raw string may not end in an odd number of \ characters; see the FAQ entry for more information and workarounds.

원시 문자열에는 한 가지 미묘한 측면이 있습니다: 원시 문자열은 홀수 개의 \ 문자로 끝날 수 없습니다. 자세한 정보와 해결 방법은 FAQ 항목을 참조하세요.

20. String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End-of-line characters are automatically included in the string, but it's possible to prevent this by adding a \ at the end of the line. In the following example, the initial newline is not included:

문자열 리터럴은 여러 줄에 걸쳐 있을 수 있습니다. 한 가지 방법은 삼중 따옴표를 사용하는 것입니다: """...""" 또는 '''...'''. 줄 끝 문자는 자동으로 문자열에 포함되지만, 줄 끝에 \를 추가하여 이를 방지할 수 있습니다. 다음 예제에서는 초기 줄바꿈이 포함되지 않습니다:

```python
>>> print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
```

21. Strings can be concatenated (glued together) with the + operator, and repeated with *:

문자열은 + 연산자로 연결(붙여서)하고, *로 반복할 수 있습니다:

```python
>>> # 3 times 'un', followed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
```

22. Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.

두 개 이상의 문자열 리터럴(즉, 따옴표로 둘러싸인 것들)이 서로 옆에 있으면 자동으로 연결됩니다.

```python
>>> 'Py' 'thon'
'Python'
```

23. This feature is particularly useful when you want to break long strings:

이 기능은 긴 문자열을 나누고 싶을 때 특히 유용합니다:

```python
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
```

24. This only works with two literals though, not with variables or expressions:

그러나 이것은 두 리터럴에만 작동하며, 변수나 표현식에는 작동하지 않습니다:

```python
>>> prefix = 'Py'
>>> prefix 'thon'  # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon'
           ^^^^^^
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
               ^^^^^
SyntaxError: invalid syntax
```

25. If you want to concatenate variables or a variable and a literal, use +:

변수나 변수와 리터럴을 연결하려면 +를 사용하세요:

```python
>>> prefix + 'thon'
'Python'
```

26. Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:

문자열은 첫 번째 문자가 인덱스 0을 갖는 인덱싱(첨자)될 수 있습니다. 별도의 문자 타입은 없습니다. 문자는 단순히 크기가 1인 문자열입니다:

```python
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'
```

27. Indices may also be negative numbers, to start counting from the right:

인덱스는 오른쪽에서부터 계산하기 위해 음수일 수도 있습니다:

```python
>>> word[-1]  # last character
'n'
>>> word[-2]  # second-last character
'o'
>>> word[-6]
'P'
```

28. Note that since -0 is the same as 0, negative indices start from -1.

-0은 0과 같기 때문에 음수 인덱스는 -1부터 시작합니다.

29. In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain a substring:

인덱싱 외에도 슬라이싱도 지원됩니다. 인덱싱은 개별 문자를 가져오는 데 사용되지만, 슬라이싱을 사용하면 부분 문자열을 얻을 수 있습니다:

```python
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
```

30. Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.

슬라이스 인덱스에는 유용한 기본값이 있습니다. 생략된 첫 번째 인덱스는 0으로, 생략된 두 번째 인덱스는 슬라이스되는 문자열의 크기로 기본 설정됩니다.

```python
>>> word[:2]   # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:]   # characters from position 4 (included) to the end
'on'
>>> word[-2:]  # characters from the second-last (included) to the end
'on'
```

31. Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:

시작은 항상 포함되고 끝은 항상 제외된다는 점에 유의하세요. 이렇게 하면 s[:i] + s[i:]가 항상 s와 같게 됩니다:

```python
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
```

32. One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n, for example:

슬라이스 작동 방식을 기억하는 한 가지 방법은 인덱스가 문자 사이를 가리키며, 첫 번째 문자의 왼쪽 가장자리가 0으로 번호가 매겨진다고 생각하는 것입니다. 그런 다음 n개의 문자로 이루어진 문자열의 마지막 문자의 오른쪽 가장자리는 인덱스 n을 가집니다. 예를 들어:

```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

33. The first row of numbers gives the position of the indices 0…6 in the string; the second row gives the corresponding negative indices. The slice from i to j consists of all characters between the edges labeled i and j, respectively.

첫 번째 행의 숫자는 문자열에서 인덱스 0…6의 위치를 나타냅니다. 두 번째 행은 해당 음수 인덱스를 나타냅니다. i에서 j까지의 슬라이스는 각각 i와 j로 레이블이 지정된 가장자리 사이의 모든 문자로 구성됩니다.

34. For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For example, the length of word[1:3] is 2.

음이 아닌 인덱스의 경우, 두 인덱스가 모두 범위 내에 있다면 슬라이스의 길이는 인덱스의 차이입니다. 예를 들어, word[1:3]의 길이는 2입니다.

35. Attempting to use an index that is too large will result in an error:

너무 큰 인덱스를 사용하려고 하면 오류가 발생합니다:

```python
>>> word[42]  # the word only has 6 characters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

36. However, out of range slice indexes are handled gracefully when used for slicing:

그러나 슬라이싱에 사용될 때 범위를 벗어난 슬라이스 인덱스는 우아하게 처리됩니다:

```python
>>> word[4:42]
'on'
>>> word[42:]
''
```

37. Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error:

파이썬 문자열은 변경할 수 없습니다 — 불변입니다. 따라서 문자열의 인덱스 위치에 할당하면 오류가 발생합니다:

```python
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

38. If you need a different string, you should create a new one:

다른 문자열이 필요하면 새 문자열을 만들어야 합니다:

```python
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
```

39. The built-in function len() returns the length of a string:

내장 함수 len()은 문자열의 길이를 반환합니다:

```python
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
```

40. **See also**
- Text Sequence Type — str
  Strings are examples of sequence types, and support the common operations supported by such types.
- String Methods
  Strings support a large number of methods for basic transformations and searching.
- f-strings
  String literals that have embedded expressions.
- Format String Syntax
  Information about string formatting with str.format().
- printf-style String Formatting
  The old formatting operations invoked when strings are the left operand of the % operator are described in more detail here.

**참고**
- 텍스트 시퀀스 타입 — str
  문자열은 시퀀스 타입의 예이며, 그러한 타입이 지원하는 공통 연산을 지원합니다.
- 문자열 메서드
  문자열은 기본 변환 및 검색을 위한 많은 메서드를 지원합니다.
- f-문자열
  표현식이 내장된 문자열 리터럴.
- 형식 문자열 구문
  str.format()을 사용한 문자열 형식 지정에 대한 정보.
- printf 스타일 문자열 형식
  문자열이 % 연산자의 왼쪽 피연산자일 때 호출되는 이전 형식 지정 연산은 여기에서 자세히 설명합니다.

## 3.1.3. Lists

41. Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.

파이썬은 다른 값을 함께 그룹화하는 데 사용되는 여러 복합 데이터 타입을 알고 있습니다. 가장 다용도로 사용되는 것은 리스트로, 대괄호 사이에 쉼표로 구분된 값(항목)의 목록으로 작성할 수 있습니다. 리스트는 다른 유형의 항목을 포함할 수 있지만, 일반적으로 모든 항목은 동일한 유형을 가집니다.

```python
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```

42. Like strings (and all other built-in sequence types), lists can be indexed and sliced:

문자열(및 다른 모든 내장 시퀀스 타입)과 마찬가지로 리스트는 인덱싱 및 슬라이싱할 수 있습니다:

```python
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
```

43. Lists also support operations like concatenation:

리스트는 연결과 같은 연산도 지원합니다:

```python
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

44. Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:

불변인 문자열과 달리 리스트는 가변 타입입니다. 즉, 내용을 변경할 수 있습니다:

```python
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
```

45. You can also add new items at the end of the list, by using the list.append() method (we will see more about methods later):

리스트.append() 메서드를 사용하여 리스트 끝에 새 항목을 추가할 수도 있습니다(메서드에 대해서는 나중에 더 자세히 알아보겠습니다):

```python
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```

46. Simple assignment in Python never copies data. When you assign a list to a variable, the variable refers to the existing list. Any changes you make to the list through one variable will be seen through all other variables that refer to it:

파이썬에서 단순 할당은 데이터를 복사하지 않습니다. 변수에 리스트를 할당하면 변수는 기존 리스트를 참조합니다. 하나의 변수를 통해 리스트를 변경하면 해당 리스트를 참조하는 다른 모든 변수를 통해서도 변경 사항이 보입니다:

```python
>>> rgb = ["Red", "Green", "Blue"]
>>> rgba = rgb
>>> id(rgb) == id(rgba)  # they reference the same object
True
>>> rgba.append("Alph")
>>> rgb
["Red", "Green", "Blue", "Alph"]
```

47. All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list:

모든 슬라이스 연산은 요청된 요소를 포함하는 새 리스트를 반환합니다. 이는 다음 슬라이스가 리스트의 얕은 복사본을 반환한다는 것을 의미합니다:

```python
>>> correct_rgba = rgba[:]
>>> correct_rgba[-1] = "Alpha"
>>> correct_rgba
["Red", "Green", "Blue", "Alpha"]
>>> rgba
["Red", "Green", "Blue", "Alph"]
```

48. Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:

슬라이스에 할당하는 것도 가능하며, 이를 통해 리스트의 크기를 변경하거나 완전히 비울 수도 있습니다:

```python
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
```

49. The built-in function len() also applies to lists:

내장 함수 len()도 리스트에 적용됩니다:

```python
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
```

50. It is possible to nest lists (create lists containing other lists), for example:

리스트를 중첩(다른 리스트를 포함하는 리스트 생성)하는 것도 가능합니다. 예를 들어:

```python
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```

## 3.2. First Steps Towards Programming

51. Of course, we can use Python for more complicated tasks than adding two and two together. For instance, we can write an initial sub-sequence of the Fibonacci series as follows:

물론, 우리는 단순히 두 개의 숫자를 더하는 것보다 더 복잡한 작업에 파이썬을 사용할 수 있습니다. 예를 들어, 피보나치 수열의 초기 부분 시퀀스를 다음과 같이 작성할 수 있습니다:

```python
>>> # Fibonacci series:
>>> # the sum of two elements defines the next
>>> a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8
```

52. This example introduces several new features.

이 예제는 몇 가지 새로운 기능을 소개합니다.

53. The first line contains a multiple assignment: the variables a and b simultaneously get the new values 0 and 1. On the last line this is used again, demonstrating that the expressions on the right-hand side are all evaluated first before any of the assignments take place. The right-hand side expressions are evaluated from the left to the right.

첫 번째 줄에는 다중 할당이 포함되어 있습니다: 변수 a와 b는 동시에 새 값 0과 1을 얻습니다. 마지막 줄에서 이것이 다시 사용되는데, 이는 할당이 이루어지기 전에 오른쪽 표현식이 모두 먼저 평가된다는 것을 보여줍니다. 오른쪽 표현식은 왼쪽에서 오른쪽으로 평가됩니다.

54. The while loop executes as long as the condition (here: a < 10) remains true. In Python, like in C, any non-zero integer value is true; zero is false. The condition may also be a string or list value, in fact any sequence; anything with a non-zero length is true, empty sequences are false. The test used in the example is a simple comparison. The standard comparison operators are written the same as in C: < (less than), > (greater than), == (equal to), <= (less than or equal to), >= (greater than or equal to) and != (not equal to).

while 루프는 조건(여기서는 a < 10)이 참인 한 계속 실행됩니다. C와 마찬가지로 파이썬에서는 0이 아닌 정수 값은 참이고, 0은 거짓입니다. 조건은 문자열이나 리스트 값, 사실상 모든 시퀀스가 될 수 있습니다. 길이가 0이 아닌 모든 것은 참이고, 빈 시퀀스는 거짓입니다. 예제에서 사용된 테스트는 간단한 비교입니다. 표준 비교 연산자는 C와 같이 작성됩니다: < (미만), > (초과), == (같음), <= (이하), >= (이상) 및 != (같지 않음).

55. The body of the loop is indented: indentation is Python's way of grouping statements. At the interactive prompt, you have to type a tab or space(s) for each indented line. In practice you will prepare more complicated input for Python with a text editor; all decent text editors have an auto-indent facility. When a compound statement is entered interactively, it must be followed by a blank line to indicate completion (since the parser cannot guess when you have typed the last line). Note that each line within a basic block must be indented by the same amount.

루프의 본문은 들여쓰기 되어 있습니다: 들여쓰기는 파이썬에서 명령문을 그룹화하는 방식입니다. 대화형 프롬프트에서는 들여쓰기된 각 줄에 대해 탭이나 공백을 입력해야 합니다. 실제로는 텍스트 편집기로 파이썬용 더 복잡한 입력을 준비할 것입니다. 모든 적절한 텍스트 편집기에는 자동 들여쓰기 기능이 있습니다. 복합 명령문이 대화식으로 입력될 때는 완료를 나타내기 위해 빈 줄이 뒤따라야 합니다(파서가 마지막 줄을 입력한 시점을 추측할 수 없기 때문입니다). 기본 블록 내의 각 줄은 동일한 양만큼 들여쓰기 되어야 합니다.

56. The print() function writes the value of the argument(s) it is given. It differs from just writing the expression you want to write (as we did earlier in the calculator examples) in the way it handles multiple arguments, floating-point quantities, and strings. Strings are printed without quotes, and a space is inserted between items, so you can format things nicely, like this:

print() 함수는 주어진 인수의 값을 출력합니다. 이는 단순히 표현식을 출력하는 것(이전 계산기 예제에서 했던 것처럼)과 다르게 여러 인수, 부동 소수점 수량 및 문자열을 처리하는 방식이 다릅니다. 문자열은 따옴표 없이 출력되고 항목 사이에 공백이 삽입되므로 다음과 같이 깔끔하게 서식을 지정할 수 있습니다:

```python
>>> i = 256*256
>>> print('The value of i is', i)
The value of i is 65536
```

57. The keyword argument end can be used to avoid the newline after the output, or end the output with a different string:

키워드 인수 end를 사용하여 출력 후 줄바꿈을 방지하거나 출력을 다른 문자열로 끝낼 수 있습니다:

```python
>>> a, b = 0, 1
>>> while a < 1000:
...     print(a, end=',')
...     a, b = b, a+b
...
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
```

**Footnotes**

[1] ** 연산자는 - 보다 우선 순위가 높기 때문에, -3**2는 -(3**2)로 해석되어 -9가 됩니다. 이를 피하고 9를 얻으려면 (-3)**2를 사용할 수 있습니다.

[2] 다른 언어와 달리 \n과 같은 특수 문자는 작은 따옴표('...')와 큰 따옴표("...")에서 동일한 의미를 갖습니다. 둘 사이의 유일한 차이점은 작은 따옴표 내에서는 "를 이스케이프할 필요가 없지만 \'는 이스케이프해야 한다는 것이며, 그 반대의 경우도 마찬가지입니다.
