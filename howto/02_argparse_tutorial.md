# Python Argparse Tutorial (Python 인자구문분석 튜토리얼)

**Author: Tshepang Mbambo**

**작성자: Tshepang Mbambo**

## Introduction

1. This tutorial is a gentle introduction to `argparse`, the recommended command-line parsing module in the Python standard library. It enables you to write user-friendly command-line interfaces easily.

이 튜토리얼은 Python 표준 라이브러리에서 권장되는 명령줄 구문 분석 모듈인 `argparse`에 대한 친절한 소개입니다. `argparse`를 사용하면 사용자 친화적인 명령줄 인터페이스를 쉽게 작성할 수 있습니다.

2. The standard library includes two other libraries for command-line parameter processing: the lower level `optparse` module (which may require more code to configure for a given application, but also allows an application to request behaviors that argparse doesn't support) and the very low level `getopt` (which specifically serves as an equivalent to the getopt() family of functions available to C programmers). However, `argparse` is recommended for most use cases.

표준 라이브러리에는 명령줄 매개변수 처리를 위한 다른 두 가지 라이브러리가 포함되어 있습니다: 더 낮은 수준의 `optparse` 모듈(주어진 애플리케이션을 구성하기 위해 더 많은 코드가 필요할 수 있지만, argparse가 지원하지 않는 동작을 요청할 수 있음)과 매우 낮은 수준의 `getopt`(특히 C 프로그래머가 사용할 수 있는 getopt() 함수군과 동등한 역할을 함)입니다. 그러나 대부분의 사용 사례에서는 `argparse`가 권장됩니다.

## Basic Concepts

3. Let's understand some basic concepts by looking at the `ls` command:

몇 가지 기본 개념을 `ls` 명령을 통해 이해해 봅시다:

```
ls
cpython  devguide  prog.py  pypy  rm-unused-function.patch

ls pypy
ctypes_configure  demo  dotviewer  include  lib_pypy  lib-python ...

ls -l
total 20
drwxr-xr-x 19 wena wena 4096 Feb 18 18:51 cpython
drwxr-xr-x  4 wena wena 4096 Feb  8 12:04 devguide
-rwxr-xr-x  1 wena wena  535 Feb 19 00:05 prog.py
drwxr-xr-x 14 wena wena 4096 Feb  7 00:59 pypy
-rw-r--r--  1 wena wena  741 Feb 18 01:01 rm-unused-function.patch
```

4. From these examples, we can understand that:

이러한 예시로부터 다음과 같은 개념을 이해할 수 있습니다:

5. Commands like `ls` can run without any options, displaying default behavior (in this case, listing the current directory).

`ls`와 같은 명령어는 옵션 없이 실행될 수 있으며, 기본 동작을 표시합니다(이 경우 현재 디렉토리 목록).

6. **Positional arguments** (like `pypy` in `ls pypy`) specify what a program should operate on, based solely on where they appear on the command line.

**위치 인자**(positional arguments, `ls pypy`의 `pypy`와 같은)는 명령줄에 나타나는 위치에만 기반하여 프로그램이 무엇을 작동해야 하는지 지정합니다.

7. **Optional arguments** (like `-l` in `ls -l`) modify the behavior of the program.

**선택적 인자**(optional arguments, `ls -l`의 `-l`과 같은)는 프로그램의 동작을 수정합니다.

## Getting Started with Argparse

8. Let's start with a very simple example that does almost nothing:

거의 아무것도 하지 않는 매우 간단한 예제로 시작하겠습니다:

```python
import argparse
parser = argparse.ArgumentParser()
parser.parse_args()
```

9. When we run this script, different things happen depending on the arguments we provide:

이 스크립트를 실행할 때, 제공하는 인자에 따라 다른 결과가 나타납니다:

```
# No arguments - nothing happens
python prog.py

# Help flag automatically provided
python prog.py --help
usage: prog.py [-h]

options:
  -h, --help  show this help message and exit

# Unknown arguments cause errors
python prog.py --verbose
usage: prog.py [-h]
prog.py: error: unrecognized arguments: --verbose
```

10. Even with this minimal code, `argparse` provides a useful help message for free with the `-h` or `--help` flag, and provides error messages for invalid arguments.

이 최소한의 코드로도 `argparse`는 `-h` 또는 `--help` 플래그로 유용한 도움말 메시지를 무료로 제공하며, 잘못된 인자에 대한 오류 메시지를 제공합니다.

## Adding Positional Arguments

11. Let's add a positional argument to our script:

우리 스크립트에 위치 인자를 추가해 봅시다:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
```

12. Now when we run it:

이제 실행하면:

```
# Requires an argument
python prog.py
usage: prog.py [-h] echo
prog.py: error: the following arguments are required: echo

# Shows help with echo as positional argument
python prog.py --help
usage: prog.py [-h] echo

positional arguments:
  echo

options:
  -h, --help  show this help message and exit

# Echo works
python prog.py foo
foo
```

13. The `add_argument()` method specifies which command-line options the program accepts. When we call `parse_args()`, it returns the arguments, which are accessible as attributes of the returned object.

`add_argument()` 메서드는 프로그램이 수용하는 명령줄 옵션을 지정합니다. `parse_args()`를 호출하면 인자를 반환하며, 이는 반환된 객체의 속성으로 접근할 수 있습니다.

14. Let's make our help message more descriptive:

도움말 메시지를 더 설명적으로 만들어 봅시다:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print(args.echo)
```

15. Now the help shows what our argument does:

이제 도움말은 인자가 무엇을 하는지 보여줍니다:

```
python prog.py --help
usage: prog.py [-h] echo

positional arguments:
  echo        echo the string you use here

options:
  -h, --help  show this help message and exit
```

## Type Conversion

16. By default, `argparse` treats all input values as strings. We can specify a type to automatically convert the argument:

기본적으로 `argparse`는 모든 입력 값을 문자열로 처리합니다. 인자를 자동으로 변환하기 위해 타입을 지정할 수 있습니다:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print(args.square**2)
```

17. This script squares an integer argument:

이 스크립트는 정수 인자를 제곱합니다:

```
python prog.py 4
16

# Fails with non-integer input
python prog.py four
usage: prog.py [-h] square
prog.py: error: argument square: invalid int value: 'four'
```

18. The `type=int` parameter tells `argparse` to convert the argument to an integer, and it automatically validates the input.

`type=int` 매개변수는 `argparse`에게 인자를 정수로 변환하도록 지시하며, 자동으로 입력을 검증합니다.

## Optional Arguments

19. Now let's add optional arguments to our script:

이제 스크립트에 선택적 인자를 추가해 봅시다:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
```

20. When we run it:

실행하면:

```
# Using verbosity
python prog.py --verbosity 1
verbosity turned on

# Without verbosity - no output
python prog.py

# Help now includes the optional argument
python prog.py --help
usage: prog.py [-h] [--verbosity VERBOSITY]

options:
  -h, --help            show this help message and exit
  --verbosity VERBOSITY
                        increase output verbosity
```

21. Optional arguments are preceded by `--` and can take a value. If not specified, they default to `None`.

선택적 인자는 `--`로 시작하며 값을 가질 수 있습니다. 지정하지 않으면 기본값은 `None`입니다.

22. If we just want a true/false flag, we can use `action="store_true"`:

단순히 참/거짓 플래그를 원한다면 `action="store_true"`를 사용할 수 있습니다:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
```

23. Now the argument works as a flag with no value needed:

이제 인자는 값이 필요 없는 플래그로 작동합니다:

```
python prog.py --verbose
verbosity turned on

# Error if value provided
python prog.py --verbose 1
usage: prog.py [-h] [--verbose]
prog.py: error: unrecognized arguments: 1
```

## Short Options

24. We can add short versions of options using single dashes:

단일 대시를 사용하여 옵션의 짧은 버전을 추가할 수 있습니다:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
```

25. Both short and long versions work:

짧은 버전과 긴 버전 모두 작동합니다:

```
python prog.py -v
verbosity turned on

python prog.py --verbose
verbosity turned on
```

## Combining Positional and Optional Arguments

26. Let's combine both types of arguments in a single script:

두 유형의 인자를 하나의 스크립트에서 결합해 봅시다:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print(f"the square of {args.square} equals {answer}")
else:
    print(answer)
```

27. This script calculates squares but the output format depends on the verbosity flag:

이 스크립트는 제곱을 계산하지만 출력 형식은 상세도 플래그에 따라 달라집니다:

```
python prog.py 4
16

python prog.py 4 --verbose
the square of 4 equals 16

# Order of arguments doesn't matter for named arguments
python prog.py --verbose 4
the square of 4 equals 16
```

## Multiple Levels of Verbosity

28. We can use integer values to specify different levels of verbosity:

다양한 수준의 상세도를 지정하기 위해 정수 값을 사용할 수 있습니다:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity == 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)
```

29. The `choices` parameter restricts the values to a specific list and automatically updates both error messages and help text:

`choices` 매개변수는 값을 특정 목록으로 제한하고 오류 메시지와 도움말 텍스트를 자동으로 업데이트합니다:

```
python prog.py 4
16

python prog.py 4 -v 1
4^2 == 16

python prog.py 4 -v 2
the square of 4 equals 16

# Error for invalid choice
python prog.py 4 -v 3
usage: prog.py [-h] [-v {0,1,2}] square
prog.py: error: argument -v/--verbosity: invalid choice: 3 (choose from 0, 1, 2)

# Help shows the valid choices
python prog.py 4 -h
usage: prog.py [-h] [-v {0,1,2}] square

positional arguments:
  square                display a square of a given number

options:
  -h, --help            show this help message and exit
  -v, --verbosity {0,1,2}
                        increase output verbosity
```

## Count Flag Occurrences

30. A common pattern is to count the occurrences of a flag to determine verbosity level, similar to how the Python interpreter itself handles verbosity:

상세도 수준을 결정하기 위해 플래그의 발생 횟수를 세는 것은 Python 인터프리터 자체가 상세도를 처리하는 방식과 유사한 일반적인 패턴입니다:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity >= 2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity >= 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)
```

31. The `action="count"` parameter counts how many times the option appears, and `default=0` ensures it has a valid value when not specified. Without the default value, the verbosity would be `None` when not specified, causing errors when compared with integers:

`action="count"` 매개변수는 옵션이 나타나는 횟수를 세고, `default=0`은 지정되지 않았을 때 유효한 값을 가지도록 합니다. 기본값이 없으면 상세도가 지정되지 않았을 때 `None`이 되어 정수와 비교할 때 오류가 발생합니다:

```
python prog.py 4
16

python prog.py 4 -v
4^2 == 16

python prog.py 4 -vv
the square of 4 equals 16

# Multiple v flags stack
python prog.py 4 -vvv
the square of 4 equals 16

# Long form can be repeated too
python prog.py 4 --verbosity --verbosity
the square of 4 equals 16

# Cannot provide a value with count action
python prog.py 4 -v 1
usage: prog.py [-h] [-v] square
prog.py: error: unrecognized arguments: 1
```

32. Note that we use `>=` instead of `==` in the comparison to properly handle any number of verbosity flags, so `-vvv` or more will still give the most verbose output:

비교에서 `==` 대신 `>=`를 사용하여 임의 개수의 상세도 플래그를 적절히 처리하므로, `-vvv` 이상은 여전히 가장 상세한 출력을 제공합니다:

```
python prog.py 4 -vvvv
the square of 4 equals 16
```

## Advanced Usage

32. `argparse` supports many more features including:
   - Subcommands (like `git add`, `git commit`)
   - Mutually exclusive groups
   - Required named arguments
   - Custom types and actions
   - Argument groups for organizing help output
   - File handling arguments

`argparse`는 다음을 포함한 더 많은 기능을 지원합니다:
   - 하위 명령어(`git add`, `git commit`과 같은)
   - 상호 배타적 그룹
   - 필수 명명 인자
   - 사용자 정의 유형 및 액션
   - 도움말 출력을 구성하기 위한 인자 그룹
   - 파일 처리 인자

33. As you build more complex command-line interfaces, refer to the official Python documentation for `argparse` to learn about these advanced features.

더 복잡한 명령줄 인터페이스를 구축할 때는 이러한 고급 기능에 대해 알아보기 위해 `argparse`에 대한 공식 Python 문서를 참조하세요.

## Multiple Positional Arguments

36. Let's expand our program to perform general exponentiation instead of just squares:

일반적인 거듭제곱을 수행하도록 프로그램을 확장해 봅시다:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()
answer = args.x**args.y
if args.verbosity >= 2:
    print(f"{args.x} to the power {args.y} equals {answer}")
elif args.verbosity >= 1:
    print(f"{args.x}^{args.y} == {answer}")
else:
    print(answer)
```

37. Now our program requires two positional arguments, a base and an exponent:

이제 프로그램은 밑과 지수, 두 개의 위치 인자를 필요로 합니다:

```
python prog.py
usage: prog.py [-h] [-v] x y
prog.py: error: the following arguments are required: x, y

python prog.py 4 2 -v
4^2 == 16
```

## Changing the Display Based on Verbosity

38. Instead of using verbosity to change the format of the output, we can use it to display more or less information:

상세도를 사용하여 출력 형식을 변경하는 대신, 더 많거나 적은 정보를 표시하는 데 사용할 수 있습니다:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()
answer = args.x**args.y
if args.verbosity >= 2:
    print(f"Running '{__file__}'")
if args.verbosity >= 1:
    print(f"{args.x}^{args.y} == ", end="")
print(answer)
```

39. Now, with different verbosity levels, we get different amounts of output:

이제 다양한 상세도 수준에 따라 다양한 양의 출력을 얻습니다:

```
python prog.py 4 2
16

python prog.py 4 2 -v
4^2 == 16

python prog.py 4 2 -vv
Running 'prog.py'
4^2 == 16
```

## Handling Ambiguous Arguments

40. Sometimes it's unclear whether an argument is meant to be positional or optional. The `--` separator tells `argparse` that everything after it should be treated as a positional argument:

때로는 인자가 위치 인자인지 선택적 인자인지 불분명합니다. `--` 구분자는 `argparse`에게 그 뒤의 모든 것을 위치 인자로 취급하도록 지시합니다:

```python
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-n', nargs='+')
parser.add_argument('args', nargs='*')

# Ambiguous: -f looks like an option, but it's not defined
parser.parse_args(['-f'])  # Error

# Using -- to indicate -f is positional
parser.parse_args(['--', '-f'])  # -f is now a positional argument

# Without --, -n takes all the arguments
parser.parse_args(['-n', '1', '2', '3'])  # All go to -n

# With --, arguments after -- go to positional args
parser.parse_args(['-n', '1', '--', '2', '3'])  # 1 to -n, 2 and 3 to positional
```

41. This is particularly useful when you might have positional arguments that start with dashes.

이는 특히 대시로 시작하는 위치 인자가 있을 때 유용합니다.

## Mutually Exclusive Groups

42. In some cases, you might want to specify options that conflict with each other. `argparse` provides a way to define mutually exclusive groups:

일부 경우에는 서로 충돌하는 옵션을 지정하고 싶을 수 있습니다. `argparse`는 상호 배타적 그룹을 정의하는 방법을 제공합니다:

```python
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")
```

43. In this example, `--verbose` and `--quiet` cannot be used together:

이 예제에서는 `--verbose`와 `--quiet`를 함께 사용할 수 없습니다:

```
python prog.py 4 2
4^2 == 16

python prog.py 4 2 -q
16

python prog.py 4 2 -v
4 to the power 2 equals 16

python prog.py 4 2 -v -q
usage: prog.py [-h] [-v | -q] x y
prog.py: error: argument -q/--quiet: not allowed with argument -v/--verbose
```

## Adding a Program Description

44. You can add a description to your program to tell users what it does:

프로그램이 무엇을 하는지 사용자에게 알려주기 위해 설명을 추가할 수 있습니다:

```python
import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")
```

45. The description appears in the help output:

설명은 도움말 출력에 나타납니다:

```
python prog.py --help
usage: prog.py [-h] [-v | -q] x y

calculate X to the power of Y

positional arguments:
  x              the base
  y              the exponent

options:
  -h, --help     show this help message and exit
  -v, --verbose
  -q, --quiet
```

## Translating argparse Output

46. The output messages from `argparse` (help text, error messages) can be translated using the `gettext` module for internationalization:

`argparse`의 출력 메시지(도움말 텍스트, 오류 메시지)는 국제화를 위해 `gettext` 모듈을 사용하여 번역할 수 있습니다:

```python
import argparse
import gettext

# Setup translation
gettext.bindtextdomain('myapp', '/path/to/translations')
gettext.textdomain('myapp')
_ = gettext.gettext

# Use translated strings in your parser
parser = argparse.ArgumentParser(description=_("calculate X to the power of Y"))
parser.add_argument("x", type=int, help=_("the base"))
parser.add_argument("y", type=int, help=_("the exponent"))
```

47. To extract the translatable strings from the `argparse` module itself, you can use a tool like Babel:

`argparse` 모듈 자체에서 번역 가능한 문자열을 추출하려면 Babel과 같은 도구를 사용할 수 있습니다:

```
pybabel extract -o messages.po /usr/lib/python3.12/argparse.py
```

48. You can find the location of the `argparse` module on your system with:

시스템에서 `argparse` 모듈의 위치를 다음과 같이 찾을 수 있습니다:

```python
import argparse
print(argparse.__file__)
```

49. In the help output, standard phrases like "usage:", "positional arguments:", "options:", and "show this help message and exit" are all translatable through gettext:

도움말 출력에서 "usage:", "positional arguments:", "options:", "show this help message and exit"와 같은 표준 문구는 모두 gettext를 통해 번역 가능합니다:

```
python prog.py --help
usage: prog.py [-h] [-v | -q] x y

calculate X to the power of Y

positional arguments:
  x              the base
  y              the exponent

options:
  -h, --help     show this help message and exit
  -v, --verbose
  -q, --quiet
```

## Custom Type Converters

50. You can define custom type converters to process input before it's stored:

입력이 저장되기 전에 처리하기 위한 사용자 정의 타입 변환기를 정의할 수 있습니다:

```python
import argparse

# Custom type function
def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
    return ivalue

parser = argparse.ArgumentParser()
parser.add_argument("--count", type=positive_int, help="a positive integer")
args = parser.parse_args()
print(args.count)
```

51. This allows for more complex validation and processing:

이를 통해 더 복잡한 유효성 검사와 처리가 가능합니다:

```
python prog.py --count 5
5

python prog.py --count -5
usage: prog.py [-h] [--count COUNT]
prog.py: error: argument --count: -5 is not a positive integer
```

52. Type converters can also be used to handle complex input formats or to customize how arguments are interpreted:

타입 변환기는 복잡한 입력 형식을 처리하거나 인자의 해석 방식을 사용자 정의하는 데도 사용될 수 있습니다:

```python
import argparse

# Parse key=value pairs
def parse_key_value(string):
    key, value = string.split('=', 1)
    return key, value

parser = argparse.ArgumentParser()
parser.add_argument("--config", type=parse_key_value, action="append")
args = parser.parse_args()
config_dict = dict(args.config or [])
print(config_dict)
```

53. This allows for flexible command-line interfaces:

이를 통해 유연한 명령줄 인터페이스를 만들 수 있습니다:

```
python prog.py --config host=localhost --config port=8080
{'host': 'localhost', 'port': '8080'}
```

## Custom Prefix Characters

54. By default, `argparse` recognizes `-` as the prefix for optional arguments. You can customize this using the `prefix_chars` parameter:

기본적으로 `argparse`는 선택적 인자의 접두사로 `-`를 인식합니다. `prefix_chars` 매개변수를 사용하여 이를 사용자 정의할 수 있습니다:

```python
import argparse

parser = argparse.ArgumentParser(prefix_chars='-+')

parser.add_argument('-a', metavar='<value>', action='append',
                    type=lambda x: ('-', x))
parser.add_argument('+a', metavar='<value>', action='append',
                    type=lambda x: ('+', x))

args = parser.parse_args()
print(args)
```

55. This allows for different prefixes to be treated distinctly:

이렇게 하면 서로 다른 접두사를 구별하여 처리할 수 있습니다:

```
python prog.py -a value1 +a value2
Namespace(a=[('-', 'value1'), ('+', 'value2')])
```

56. Custom prefixes are useful when you need to differentiate between different types of options, such as positive and negative settings, or when creating interfaces for programs that traditionally use different prefixes (like DOS commands that use `/` instead of `-`).

사용자 정의 접두사는 긍정적 및 부정적 설정과 같은 다른 유형의 옵션을 구별해야 할 때, 또는 전통적으로 다른 접두사를 사용하는 프로그램(예: `-` 대신 `/`를 사용하는 DOS 명령)의 인터페이스를 만들 때 유용합니다.

## Conclusion

57. The `argparse` module provides a powerful, flexible way to create sophisticated command-line interfaces in Python with minimal code. It automatically generates help and usage messages and issues errors when users give the program invalid arguments.

`argparse` 모듈은 최소한의 코드로 Python에서 정교한 명령줄 인터페이스를 만들기 위한 강력하고 유연한 방법을 제공합니다. 자동으로 도움말과 사용법 메시지를 생성하고 사용자가 프로그램에 잘못된 인자를 제공할 때 오류를 발생시킵니다.

58. By understanding how to use positional arguments, optional arguments, type conversion, and other features of `argparse`, you can create user-friendly command-line programs that are both powerful and easy to use.

위치 인자, 선택적 인자, 타입 변환 및 `argparse`의 다른 기능을 사용하는 방법을 이해함으로써 강력하면서도 사용하기 쉬운 사용자 친화적인 명령줄 프로그램을 만들 수 있습니다.

59. The examples in this tutorial cover many common use cases, but `argparse` offers even more functionality. The official Python documentation for `argparse` provides comprehensive details about all available features.

이 튜토리얼의 예제는 많은 일반적인 사용 사례를 다루지만, `argparse`는 더 많은 기능을 제공합니다. `argparse`에 대한 공식 Python 문서는 모든 사용 가능한 기능에 대한 포괄적인 세부 정보를 제공합니다.
