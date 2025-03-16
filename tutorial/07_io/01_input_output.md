# 7. Input and Output

1. There are several ways to present the output of a program; data can be printed in a human-readable form, or written to a file for future use. This chapter will discuss some of the possibilities.

프로그램의 출력을 표현하는 방법은 여러 가지가 있습니다; 데이터는 사람이 읽을 수 있는 형태로 출력되거나, 나중에 사용하기 위해 파일에 기록될 수 있습니다. 이 장에서는 가능한 몇 가지 방법을 논의할 것입니다.

## 7.1. Fancier Output Formatting

2. So far we've encountered two ways of writing values: expression statements and the `print()` function. (A third way is using the `write()` method of file objects; the standard output file can be referenced as `sys.stdout`. See the Library Reference for more information on this.)

지금까지 우리는 값을 작성하는 두 가지 방법을 접했습니다: 표현식 문과 `print()` 함수입니다. (세 번째 방법은 파일 객체의 `write()` 메서드를 사용하는 것입니다; 표준 출력 파일은 `sys.stdout`으로 참조될 수 있습니다. 이에 대한 자세한 정보는 라이브러리 참조를 확인하세요.)

3. Often you'll want more control over the formatting of your output than simply printing space-separated values. There are several ways to format output.

종종 공백으로 구분된 값을 단순히 출력하는 것보다 출력 형식을 더 많이 제어하고 싶을 것입니다. 출력을 형식화하는 여러 가지 방법이 있습니다.

4. To use formatted string literals, begin a string with f or F before the opening quotation mark or triple quotation mark. Inside this string, you can write a Python expression between { and } characters that can refer to variables or literal values.

형식화된 문자열 리터럴을 사용하려면, 열린 따옴표나 삼중 따옴표 앞에 f 또는 F를 붙여서 문자열을 시작하세요. 이 문자열 안에서, 변수나 리터럴 값을 참조할 수 있는 파이썬 표현식을 { 와 } 문자 사이에 작성할 수 있습니다.

```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```

5. The `str.format()` method of strings requires more manual effort. You'll still use { and } to mark where a variable will be substituted and can provide detailed formatting directives, but you'll also need to provide the information to be formatted. In the following code block there are two examples of how to format variables:

문자열의 `str.format()` 메서드는 더 많은 수동 작업을 필요로 합니다. 변수가 대체될 위치를 표시하기 위해 { 와 } 를 여전히 사용하고 상세한 형식 지시자를 제공할 수 있지만, 형식을 지정할 정보도 제공해야 합니다. 다음 코드 블록에서는 변수 형식을 지정하는 두 가지 예제가 있습니다:

```python
>>> yes_votes = 42_572_654
>>> total_votes = 85_705_149
>>> percentage = yes_votes / total_votes
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
```

6. Notice how the yes_votes are padded with spaces and a negative sign only for negative numbers. The example also prints percentage multiplied by 100, with 2 decimal places and followed by a percent sign (see Format Specification Mini-Language for details).

yes_votes가 공백으로 패딩되고 음수인 경우에만 음수 부호가 표시되는 방식을 확인하세요. 이 예제는 또한 백분율을 100으로 곱하고, 소수점 이하 2자리와 퍼센트 기호를 사용하여 출력합니다(자세한 내용은 형식 지정 미니 언어를 참조하세요).

7. Finally, you can do all the string handling yourself by using string slicing and concatenation operations to create any layout you can imagine. The string type has some methods that perform useful operations for padding strings to a given column width.

마지막으로, 문자열 슬라이싱과 연결 연산을 사용하여 상상할 수 있는 모든 레이아웃을 직접 만들 수 있습니다. 문자열 타입은 주어진 열 너비에 맞게 문자열을 패딩하는 유용한 작업을 수행하는 몇 가지 메서드를 가지고 있습니다.

8. When you don't need fancy output but just want a quick display of some variables for debugging purposes, you can convert any value to a string with the `repr()` or `str()` functions.

멋진 출력이 필요하지 않고 디버깅 목적으로 일부 변수를 빠르게 표시하고 싶을 때, `repr()` 또는 `str()` 함수를 사용하여 모든 값을 문자열로 변환할 수 있습니다.

9. The `str()` function is meant to return representations of values which are fairly human-readable, while `repr()` is meant to generate representations which can be read by the interpreter (or will force a SyntaxError if there is no equivalent syntax). For objects which don't have a particular representation for human consumption, `str()` will return the same value as `repr()`. Many values, such as numbers or structures like lists and dictionaries, have the same representation using either function. Strings, in particular, have two distinct representations.

`str()` 함수는 사람이 읽기 쉬운 값의 표현을 반환하기 위한 것이고, `repr()` 은 인터프리터가 읽을 수 있는 표현(또는 동등한 구문이 없는 경우 SyntaxError를 강제하는)을 생성하기 위한 것입니다. 인간이 소비하기 위한 특정 표현이 없는 객체의 경우, `str()`은 `repr()`과 동일한 값을 반환합니다. 숫자나 리스트, 딕셔너리와 같은 구조와 같은 많은 값은 어느 함수를 사용하든 동일한 표현을 가집니다. 특히 문자열은 두 가지 다른 표현을 가집니다.

10. Some examples:

몇 가지 예제:

```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
>>> hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
>>> repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```

11. The string module contains a `Template` class that offers yet another way to substitute values into strings, using placeholders like $x and replacing them with values from a dictionary, but offers much less control of the formatting.

문자열 모듈에는 $x와 같은 자리 표시자를 사용하여 문자열에 값을 대체하고 사전에서 값으로 대체하는 또 다른 방법을 제공하는 `Template` 클래스가 포함되어 있지만, 형식의 제어가 훨씬 적습니다.

### 7.1.1. Formatted String Literals

12. Formatted string literals (also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}.

형식화된 문자열 리터럴(f-문자열이라고도 함)은 문자열 앞에 f 또는 F를 붙이고 표현식을 {표현식}으로 작성하여 파이썬 표현식의 값을 문자열 내에 포함할 수 있게 합니다.

13. An optional format specifier can follow the expression. This allows greater control over how the value is formatted. The following example rounds pi to three places after the decimal:

표현식 뒤에 선택적 형식 지정자가 올 수 있습니다. 이를 통해 값의 형식을 어떻게 지정할지에 대해 더 많은 제어가 가능합니다. 다음 예제는 파이를 소수점 이하 세 자리로 반올림합니다:

```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```

14. Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making columns line up.

':'후에 정수를 전달하면 해당 필드가 최소한의 문자 너비를 가지게 됩니다. 이는 열을 맞추는 데 유용합니다.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```

15. Other modifiers can be used to convert the value before it is formatted. '!a' applies `ascii()`, '!s' applies `str()`, and '!r' applies `repr()`:

다른 수정자들을 사용하여 값이 형식화되기 전에 변환할 수 있습니다. '!a'는 `ascii()`를, '!s'는 `str()`을, '!r'은 `repr()`을 적용합니다:

```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```

16. The = specifier can be used to expand an expression to the text of the expression, an equal sign, then the representation of the evaluated expression:

= 지정자는 표현식을 표현식의 텍스트, 등호, 그리고 평가된 표현식의 표현으로 확장하는 데 사용될 수 있습니다:

```python
>>> bugs = 'roaches'
>>> count = 13
>>> area = 'living room'
>>> print(f'Debugging {bugs=} {count=} {area=}')
Debugging bugs='roaches' count=13 area='living room'
```

17. See self-documenting expressions for more information on the = specifier. For a reference on these format specifications, see the reference guide for the Format Specification Mini-Language.

= 지정자에 대한 자세한 정보는 자체 문서화 표현을 참조하세요. 이러한 형식 지정에 대한 참조는 형식 지정 미니 언어에 대한 참조 가이드를 확인하세요.

### 7.1.2. The String format() Method

18. Basic usage of the `str.format()` method looks like this:

`str.format()` 메서드의 기본 사용법은 다음과 같습니다:

```python
>>> print('We are the {} who say "{}"'.format('knights', 'Ni'))
We are the knights who say "Ni"
```

19. The brackets and characters within them (called format fields) are replaced with the objects passed into the `str.format()` method. A number in the brackets can be used to refer to the position of the object passed into the `str.format()` method.

대괄호와 그 안의 문자(형식 필드라고 함)는 `str.format()` 메서드에 전달된 객체로 대체됩니다. 대괄호 안의 숫자는 `str.format()` 메서드에 전달된 객체의 위치를 참조하는 데 사용될 수 있습니다.

```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

20. If keyword arguments are used in the `str.format()` method, their values are referred to by using the name of the argument.

`str.format()` 메서드에 키워드 인수가 사용되면, 해당 값은 인수의 이름을 사용하여 참조됩니다.

```python
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

21. Positional and keyword arguments can be arbitrarily combined:

위치 인수와 키워드 인수는 임의로 조합될 수 있습니다:

```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
...                                                    other='Georg'))
The story of Bill, Manfred, and Georg.
```

22. If you have a really long format string that you don't want to split up, it would be nice if you could reference the variables to be formatted by name instead of by position. This can be done by simply passing the dict and using square brackets '[]' to access the keys.

정말 긴 형식 문자열을 분할하고 싶지 않다면, 위치 대신 이름으로 형식을 지정할 변수를 참조할 수 있으면 좋을 것입니다. 이는 단순히 사전을 전달하고 대괄호 '[]'를 사용하여 키에 액세스하면 됩니다.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

23. This could also be done by passing the table dictionary as keyword arguments with the ** notation.

이것은 ** 표기법으로 테이블 사전을 키워드 인수로 전달하여 수행할 수도 있습니다.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

24. This is particularly useful in combination with the built-in function `vars()`, which returns a dictionary containing all local variables:

이것은 모든 로컬 변수를 포함하는 사전을 반환하는 내장 함수 `vars()`와 함께 사용하면 특히 유용합니다:

```python
>>> table = {k: str(v) for k, v in vars().items()}
>>> message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
>>> print(message.format(**table))
__name__: __main__; __doc__: None; __package__: None; __loader__: ...
```

25. As an example, the following lines produce a tidily aligned set of columns giving integers and their squares and cubes:

예를 들어, 다음 줄은 정수와 그것의 제곱 및 세제곱을 나타내는 깔끔하게 정렬된 열 집합을 생성합니다:

```python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

26. For a complete overview of string formatting with `str.format()`, see Format String Syntax.

`str.format()`을 사용한 문자열 형식 지정에 대한 완전한 개요는 형식 문자열 구문을 참조하세요.

### 7.1.3. Manual String Formatting

27. Here's the same table of squares and cubes, formatted manually:

다음은 수동으로 형식을 지정한 제곱과 세제곱의 동일한 표입니다:

```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

28. (Note that the one space between each column was added by the way `print()` works: it always adds spaces between its arguments.)

(각 열 사이의 한 공백은 `print()`의 작동 방식에 의해 추가되었습니다: 항상 인수 사이에 공백을 추가합니다.)

29. The `str.rjust()` method of string objects right-justifies a string in a field of a given width by padding it with spaces on the left. There are similar methods `str.ljust()` and `str.center()`. These methods do not write anything, they just return a new string. If the input string is too long, they don't truncate it, but return it unchanged; this will mess up your column lay-out but that's usually better than the alternative, which would be lying about a value. (If you really want truncation you can always add a slice operation, as in `x.ljust(n)[:n]`.)

문자열 객체의 `str.rjust()` 메서드는 왼쪽에 공백을 채워 주어진 너비의 필드에서 문자열을 오른쪽 정렬합니다. 유사한 메서드로 `str.ljust()`와 `str.center()`가 있습니다. 이 메서드들은 아무것도 쓰지 않고, 단지 새로운 문자열을 반환합니다. 입력 문자열이 너무 길면, 잘라내지 않고 변경 없이 반환합니다; 이렇게 하면 열 레이아웃이 엉망이 되겠지만, 대안(값에 대해 거짓말하는 것)보다 일반적으로 나은 방법입니다. (정말로 잘라내고 싶다면 `x.ljust(n)[:n]`과 같이 슬라이스 연산을 추가할 수 있습니다.)

30. There is another method, `str.zfill()`, which pads a numeric string on the left with zeros. It understands about plus and minus signs:

또 다른 메서드인 `str.zfill()`은 숫자 문자열의 왼쪽에 0을 채웁니다. 이는 더하기와 빼기 부호를 이해합니다:

```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```

### 7.1.4. Old string formatting

31. The % operator (modulo) can also be used for string formatting. Given `format % values` (where format is a string), % conversion specifications in format are replaced with zero or more elements of values. This operation is commonly known as string interpolation. For example:

% 연산자(모듈로)도 문자열 형식 지정에 사용될 수 있습니다. `format % values`(format은 문자열)가 주어지면, format의 % 변환 사양은 values의 0개 이상의 요소로 대체됩니다. 이 연산은 일반적으로 문자열 보간법이라고 합니다. 예를 들어:

```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

32. More information can be found in the printf-style String Formatting section.

더 많은 정보는 printf 스타일 문자열 형식 지정 섹션에서 찾을 수 있습니다.

## 7.2. Reading and Writing Files

33. `open()` returns a file object, and is most commonly used with two positional arguments and one keyword argument: `open(filename, mode, encoding=None)`

`open()`은 파일 객체를 반환하며, 보통 두 개의 위치 인수와 하나의 키워드 인수와 함께 사용됩니다: `open(filename, mode, encoding=None)`

```python
>>> f = open('workfile', 'w', encoding="utf-8")
```

34. The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. `mode` can be `'r'` when the file will only be read, `'w'` for only writing (an existing file with the same name will be erased), and `'a'` opens the file for appending; any data written to the file is automatically added to the end. `'r+'` opens the file for both reading and writing. The `mode` argument is optional; `'r'` will be assumed if it's omitted.

첫 번째 인수는 파일 이름을 포함하는 문자열입니다. 두 번째 인수는 파일을 사용하는 방식을 설명하는 몇 개의 문자를 포함한 또 다른 문자열입니다. `mode`는 파일을 읽기만 할 때 `'r'`, 쓰기만 할 때 `'w'`(같은 이름의 기존 파일은 지워짐), 파일을 추가하기 위해 열 때 `'a'`일 수 있습니다. 파일에 기록된 데이터는 자동으로 끝에 추가됩니다. `'r+'`는 읽기와 쓰기 모두를 위해 파일을 엽니다. `mode` 인수는 선택 사항이며, 생략하면 `'r'`이 가정됩니다.

35. Normally, files are opened in text mode, that means, you read and write strings from and to the file, which are encoded in a specific encoding. If encoding is not specified, the default is platform dependent (see `open()`). Because UTF-8 is the modern de-facto standard, `encoding="utf-8"` is recommended unless you know that you need to use a different encoding. Appending a `'b'` to the mode opens the file in binary mode. Binary mode data is read and written as bytes objects. You can not specify encoding when opening file in binary mode.

일반적으로 파일은 텍스트 모드로 열립니다. 즉, 특정 인코딩으로 인코딩된 파일에서 문자열을 읽고 쓰게 됩니다. 인코딩이 지정되지 않으면, 기본값은 플랫폼에 따라 다릅니다(`open()` 참조). UTF-8은 현대의 사실상 표준이기 때문에, 다른 인코딩을 사용해야 한다는 것을 알고 있지 않는 한 `encoding="utf-8"`이 권장됩니다. 모드에 `'b'`를 추가하면 파일이 바이너리 모드로 열립니다. 바이너리 모드 데이터는 바이트 객체로 읽고 씁니다. 바이너리 모드로 파일을 열 때는 인코딩을 지정할 수 없습니다.

36. In text mode, the default when reading is to convert platform-specific line endings (`\n` on Unix, `\r\n` on Windows) to just `\n`. When writing in text mode, the default is to convert occurrences of `\n` back to platform-specific line endings. This behind-the-scenes modification to file data is fine for text files, but will corrupt binary data like that in JPEG or EXE files. Be very careful to use binary mode when reading and writing such files.

텍스트 모드에서 읽을 때 기본값은 플랫폼별 줄 끝(Unix에서는 `\n`, Windows에서는 `\r\n`)을 `\n`으로만 변환하는 것입니다. 텍스트 모드로 쓸 때 기본값은 `\n`의 발생을 다시 플랫폼별 줄 끝으로 변환하는 것입니다. 파일 데이터에 대한 이러한 배후 수정은 텍스트 파일에는 괜찮지만, JPEG나 EXE 파일과 같은 바이너리 데이터를 손상시킬 것입니다. 그런 파일을 읽고 쓸 때는 바이너리 모드를 사용하도록 매우 주의하세요.

37. It is good practice to use the `with` keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using `with` is also much shorter than writing equivalent `try-finally` blocks:

파일 객체를 다룰 때 `with` 키워드를 사용하는 것이 좋은 관행입니다. 장점은 어떤 시점에서 예외가 발생하더라도 스위트가 끝난 후 파일이 제대로 닫힌다는 것입니다. `with`를 사용하는 것은 동등한 `try-finally` 블록을 작성하는 것보다 훨씬 짧습니다:

```python
>>> with open('workfile', encoding="utf-8") as f:
...     read_data = f.read()
...
>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```

38. If you're not using the `with` keyword, then you should call `f.close()` to close the file and immediately free up any system resources used by it.

`with` 키워드를 사용하지 않는다면, `f.close()`를 호출하여 파일을 닫고 그것이 사용한 모든 시스템 자원을 즉시 해제해야 합니다.

39. **Warning:** Calling `f.write()` without using the `with` keyword or calling `f.close()` might result in the arguments of `f.write()` not being completely written to the disk, even if the program exits successfully.

**경고:** `with` 키워드를 사용하거나 `f.close()`를 호출하지 않고 `f.write()`를 호출하면, 프로그램이 성공적으로 종료되더라도 `f.write()`의 인수가 디스크에 완전히 쓰이지 않을 수 있습니다.

40. After a file object is closed, either by a `with` statement or by calling `f.close()`, attempts to use the file object will automatically fail.

`with` 문이나 `f.close()` 호출에 의해 파일 객체가 닫힌 후, 파일 객체를 사용하려는 시도는 자동으로 실패합니다.

```python
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

### 7.2.1. Methods of File Objects

41. The rest of the examples in this section will assume that a file object called `f` has already been created.

이 섹션의 나머지 예제들은 `f`라는 파일 객체가 이미 생성되었다고 가정합니다.

42. To read a file's contents, call `f.read(size)`, which reads some quantity of data and returns it as a string (in text mode) or bytes object (in binary mode). `size` is an optional numeric argument. When size is omitted or negative, the entire contents of the file will be read and returned; it's your problem if the file is twice as large as your machine's memory. Otherwise, at most `size` characters (in text mode) or `size` bytes (in binary mode) are read and returned. If the end of the file has been reached, `f.read()` will return an empty string (`''`).

파일의 내용을 읽으려면 `f.read(size)`를 호출하세요. 이는 일정량의 데이터를 읽고, 그것을 문자열(텍스트 모드에서) 또는 바이트 객체(바이너리 모드에서)로 반환합니다. `size`는 선택적 숫자 인수입니다. size가 생략되거나 음수일 때, 파일의 전체 내용이 읽히고 반환됩니다. 파일이 기계의 메모리보다 두 배 크다면 그것은 당신의 문제입니다. 그렇지 않으면, 최대 `size` 문자(텍스트 모드에서) 또는 `size` 바이트(바이너리 모드에서)가 읽히고 반환됩니다. 파일의 끝에 도달하면, `f.read()`는 빈 문자열(`''`)을 반환합니다.

```python
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```

43. `f.readline()` reads a single line from the file; a newline character (`\n`) is left at the end of the string, and is only omitted on the last line of the file if the file doesn't end in a newline. This makes the return value unambiguous; if `f.readline()` returns an empty string, the end of the file has been reached, while a blank line is represented by `'\n'`, a string containing only a single newline.

`f.readline()`은 파일에서 한 줄을 읽습니다. 줄 바꿈 문자(`\n`)는 문자열의 끝에 남아 있으며, 파일이 줄 바꿈으로 끝나지 않는 경우에만 파일의 마지막 줄에서 생략됩니다. 이는 반환 값을 명확하게 만듭니다. `f.readline()`이 빈 문자열을 반환하면, 파일의 끝에 도달했으며, 빈 줄은 단일 줄 바꿈만 포함하는 `'\n'` 문자열로 표현됩니다.

```python
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```

44. For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:

파일에서 줄을 읽기 위해, 파일 객체를 반복할 수 있습니다. 이는 메모리 효율적이고, 빠르며, 간단한 코드로 이어집니다:

```python
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
```

45. If you want to read all the lines of a file in a list you can also use `list(f)` or `f.readlines()`.

파일의 모든 줄을 리스트로 읽고 싶다면 `list(f)` 또는 `f.readlines()`를 사용할 수도 있습니다.

46. `f.write(string)` writes the contents of `string` to the file, returning the number of characters written.

`f.write(string)`은 `string`의 내용을 파일에 쓰고, 쓰여진 문자 수를 반환합니다.

```python
>>> f.write('This is a test\n')
15
```

47. Other types of objects need to be converted – either to a string (in text mode) or a bytes object (in binary mode) – before writing them:

다른 유형의 객체는 작성하기 전에 문자열(텍스트 모드에서) 또는 바이트 객체(바이너리 모드에서)로 변환해야 합니다:

```python
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
```

48. `f.tell()` returns an integer giving the file object's current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.

`f.tell()`은 파일 객체의 현재 위치를 정수로 반환합니다. 이는 바이너리 모드에서 파일 시작부터의 바이트 수로 표현되며, 텍스트 모드에서는 불투명한 숫자로 표현됩니다.

49. To change the file object's position, use `f.seek(offset, whence)`. The position is computed from adding `offset` to a reference point; the reference point is selected by the `whence` argument. A `whence` value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. `whence` can be omitted and defaults to 0, using the beginning of the file as the reference point.

파일 객체의 위치를 변경하려면, `f.seek(offset, whence)`를 사용하세요. 위치는 기준점에 `offset`을 추가하여 계산됩니다. 기준점은 `whence` 인수에 의해 선택됩니다. 0의 `whence` 값은 파일의 시작에서부터 측정하고, 1은 현재 파일 위치를 사용하며, 2는 파일의 끝을 기준점으로 사용합니다. `whence`는 생략될 수 있으며 기본값은 0으로, 파일의 시작을 기준점으로 사용합니다.

```python
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```

50. In text files (those opened without a `b` in the mode string), only seeks relative to the beginning of the file are allowed (the exception being seeking to the very file end with `seek(0, 2)`) and the only valid offset values are those returned from the `f.tell()`, or zero. Any other offset value produces undefined behaviour.

텍스트 파일(모드 문자열에 `b`가 없이 열린 파일)에서는 파일 시작에 상대적인 탐색만 허용됩니다(`seek(0, 2)`로 파일의 맨 끝으로 이동하는 것은 예외). 유효한 오프셋 값은 `f.tell()`에서 반환된 값이나 0뿐입니다. 다른 오프셋 값은 정의되지 않은 동작을 생성합니다.

51. File objects have some additional methods, such as `isatty()` and `truncate()` which are less frequently used; consult the Library Reference for a complete guide to file objects.

파일 객체에는 `isatty()`와 `truncate()`와 같은 덜 자주 사용되는 추가 메서드가 있습니다. 파일 객체에 대한 전체 가이드는 라이브러리 참조를 참조하세요.

### 7.2.2. Saving structured data with json

52. Strings can easily be written to and read from a file. Numbers take a bit more effort, since the `read()` method only returns strings, which will have to be passed to a function like `int()`, which takes a string like `'123'` and returns its numeric value 123. When you want to save more complex data types like nested lists and dictionaries, parsing and serializing by hand becomes complicated.

문자열은 파일에서 쉽게 쓰이고 읽힐 수 있습니다. 숫자는 좀 더 노력이 필요합니다. `read()` 메서드는 문자열만 반환하므로, 이를 `int()`와 같은 함수에 전달해야 합니다. 이 함수는 `'123'과 같은 문자열을 받아 그 숫자 값 123을 반환합니다. 중첩된 리스트와 사전과 같은 더 복잡한 데이터 타입을 저장하고 싶을 때, 수동으로 파싱하고 직렬화하는 것은 복잡해집니다.

53. Rather than having users constantly writing and debugging code to save complicated data types to files, Python allows you to use the popular data interchange format called JSON (JavaScript Object Notation). The standard module called `json` can take Python data hierarchies, and convert them to string representations; this process is called serializing. Reconstructing the data from the string representation is called deserializing. Between serializing and deserializing, the string representing the object may have been stored in a file or data, or sent over a network connection to some distant machine.

사용자가 복잡한 데이터 타입을 파일에 저장하기 위해 코드를 계속해서 작성하고 디버깅하는 대신, 파이썬은 JSON(JavaScript Object Notation)이라는 인기 있는 데이터 교환 형식을 사용할 수 있게 해줍니다. `json`이라는 표준 모듈은 파이썬 데이터 계층을 가져와서 문자열 표현으로 변환할 수 있습니다. 이 과정을 직렬화라고 합니다. 문자열 표현에서 데이터를 재구성하는 것을 역직렬화라고 합니다. 직렬화와 역직렬화 사이에, 객체를 나타내는 문자열은 파일이나 데이터에 저장되거나, 네트워크 연결을 통해 먼 기계로 전송되었을 수 있습니다.

54. **Note:** The JSON format is commonly used by modern applications to allow for data exchange. Many programmers are already familiar with it, which makes it a good choice for interoperability.

**참고:** JSON 형식은 데이터 교환을 위해 현대 애플리케이션에서 일반적으로 사용됩니다. 많은 프로그래머들이 이미 익숙하기 때문에, 상호 운용성을 위한 좋은 선택입니다.

55. If you have an object `x`, you can view its JSON string representation with a simple line of code:

객체 `x`가 있다면, 간단한 코드 한 줄로 그 JSON 문자열 표현을 볼 수 있습니다:

```python
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```

56. Another variant of the `dumps()` function, called `dump()`, simply serializes the object to a text file. So if `f` is a text file object opened for writing, we can do this:

`dumps()` 함수의 또 다른 변형인 `dump()`는 단순히 객체를 텍스트 파일로 직렬화합니다. 따라서 `f`가 쓰기 위해 열린 텍스트 파일 객체라면, 이렇게 할 수 있습니다:

```python
json.dump(x, f)
```

57. To decode the object again, if `f` is a binary file or text file object which has been opened for reading:

객체를 다시 디코딩하려면, `f`가 읽기 위해 열린 바이너리 파일이나 텍스트 파일 객체인 경우:

```python
x = json.load(f)
```

58. **Note:** JSON files must be encoded in UTF-8. Use `encoding="utf-8"` when opening JSON file as a text file for both of reading and writing.

**참고:** JSON 파일은 UTF-8로 인코딩되어야 합니다. 읽기와 쓰기 모두를 위해 JSON 파일을 텍스트 파일로 열 때는 `encoding="utf-8"`을 사용하세요.

59. This simple serialization technique can handle lists and dictionaries, but serializing arbitrary class instances in JSON requires a bit of extra effort. The reference for the `json` module contains an explanation of this.

이 간단한 직렬화 기술은 리스트와 사전을 처리할 수 있지만, JSON에서 임의의 클래스 인스턴스를 직렬화하는 데는 약간의 추가 노력이 필요합니다. `json` 모듈에 대한 참조에는 이에 대한 설명이 포함되어 있습니다.

60. **See also:** `pickle` - the pickle module - Contrary to JSON, `pickle` is a protocol which allows the serialization of arbitrarily complex Python objects. As such, it is specific to Python and cannot be used to communicate with applications written in other languages. It is also insecure by default: deserializing pickle data coming from an untrusted source can execute arbitrary code, if the data was crafted by a skilled attacker.

**참고 항목:** `pickle` - pickle 모듈 - JSON과 달리, `pickle`은 임의로 복잡한 파이썬 객체의 직렬화를 허용하는 프로토콜입니다. 그러므로, 이는 파이썬에 특화되어 있으며 다른 언어로 작성된 애플리케이션과 통신하는 데 사용될 수 없습니다. 또한 기본적으로 안전하지 않습니다: 신뢰할 수 없는 소스에서 온 pickle 데이터를 역직렬화하면, 데이터가 숙련된 공격자에 의해 작성된 경우 임의의 코드가 실행될 수 있습니다.
