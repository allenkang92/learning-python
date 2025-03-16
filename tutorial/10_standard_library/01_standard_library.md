# 10. Brief Tour of the Standard Library

1. Python's standard library is very extensive, offering a wide range of facilities as indicated by the long table of contents listed below. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.

파이썬의 표준 라이브러리는 매우 광범위하며, 아래에 나열된 긴 목차가 보여주는 것처럼 다양한 기능을 제공합니다. 이 라이브러리에는 파일 I/O와 같이 파이썬 프로그래머가 접근할 수 없는 시스템 기능에 접근할 수 있게 해주는 내장 모듈(C로 작성됨)과 일상적인 프로그래밍에서 발생하는 많은 문제에 대한 표준화된 솔루션을 제공하는 파이썬으로 작성된 모듈이 포함되어 있습니다. 이러한 모듈 중 일부는 플랫폼 특정 요소를 플랫폼 중립적인 API로 추상화하여 파이썬 프로그램의 이식성을 장려하고 향상시키도록 명시적으로 설계되었습니다.

## 10.1. Operating System Interface

2. The os module provides dozens of functions for interacting with the operating system:

os 모듈은 운영 체제와 상호 작용하기 위한 수십 가지 함수를 제공합니다:

```python
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python313'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0
```

3. Be sure to use the import os style instead of from os import *. This will keep os.open() from shadowing the built-in open() function which operates much differently.

import os 스타일을 사용하고 from os import *를 사용하지 마세요. 이렇게 하면 os.open()이 매우 다르게 작동하는 내장 open() 함수를 가리지 않게 됩니다.

4. The built-in dir() and help() functions are useful as interactive aids for working with large modules like os:

내장된 dir()와 help() 함수는 os와 같은 큰 모듈로 작업할 때 대화형 도구로 유용합니다:

```python
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>
```

5. For daily file and directory management tasks, the shutil module provides a higher level interface that is easier to use:

일상적인 파일 및 디렉터리 관리 작업을 위해 shutil 모듈은 사용하기 더 쉬운 상위 수준 인터페이스를 제공합니다:

```python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```

## 10.2. File Wildcards

6. The glob module provides a function for making file lists from directory wildcard searches:

glob 모듈은 디렉터리 와일드카드 검색에서 파일 목록을 만들기 위한 함수를 제공합니다:

```python
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```

## 10.3. Command Line Arguments

7. Common utility scripts often need to process command line arguments. These arguments are stored in the sys module's argv attribute as a list. For instance, let's take the following demo.py file:

일반적인 유틸리티 스크립트는 종종 명령줄 인수를 처리해야 합니다. 이러한 인수는 리스트로 sys 모듈의 argv 속성에 저장됩니다. 예를 들어, 다음 demo.py 파일을 살펴보겠습니다:

```python
# File demo.py
import sys
print(sys.argv)
```

8. Here is the output from running python demo.py one two three at the command line:

명령줄에서 python demo.py one two three를 실행한 출력은 다음과 같습니다:

```
['demo.py', 'one', 'two', 'three']
```

9. The argparse module provides a more sophisticated mechanism to process command line arguments. The following script extracts one or more filenames and an optional number of lines to be displayed:

argparse 모듈은 명령줄 인수를 처리하기 위한 더 정교한 메커니즘을 제공합니다. 다음 스크립트는 하나 이상의 파일 이름과 표시할 선택적 라인 수를 추출합니다:

```python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```

10. When run at the command line with python top.py --lines=5 alpha.txt beta.txt, the script sets args.lines to 5 and args.filenames to ['alpha.txt', 'beta.txt'].

명령줄에서 python top.py --lines=5 alpha.txt beta.txt로 실행하면, 스크립트는 args.lines를 5로, args.filenames를 ['alpha.txt', 'beta.txt']로 설정합니다.

## 10.4. Error Output Redirection and Program Termination

11. The sys module also has attributes for stdin, stdout, and stderr. The latter is useful for emitting warnings and error messages to make them visible even when stdout has been redirected:

sys 모듈에는 stdin, stdout, stderr에 대한 속성도 있습니다. 후자는 stdout이 리디렉션되더라도 경고 및 오류 메시지를 표시하기 위해 유용합니다:

```python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```

12. The most direct way to terminate a script is to use sys.exit().

스크립트를 종료하는 가장 직접적인 방법은 sys.exit()를 사용하는 것입니다.

## 10.5. String Pattern Matching

13. The re module provides regular expression tools for advanced string processing. For complex matching and manipulation, regular expressions offer succinct, optimized solutions:

re 모듈은 고급 문자열 처리를 위한 정규 표현식 도구를 제공합니다. 복잡한 매칭 및 조작을 위해, 정규 표현식은 간결하고 최적화된 솔루션을 제공합니다:

```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```

14. When only simple capabilities are needed, string methods are preferred because they are easier to read and debug:

단순한 기능만 필요할 때는 읽고 디버그하기 더 쉬우므로 문자열 메서드가 선호됩니다:

```python
>>> 'tea for too'.replace('too', 'two')
'tea for two'
```

## 10.6. Mathematics

15. The math module gives access to the underlying C library functions for floating-point math:

math 모듈은 부동소수점 수학을 위한 기반 C 라이브러리 함수에 접근할 수 있게 해줍니다:

```python
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
```

16. The random module provides tools for making random selections:

random 모듈은 무작위 선택을 위한 도구를 제공합니다:

```python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float from the interval [0.0, 1.0)
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4
```

17. The statistics module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data:

statistics 모듈은 수치 데이터의 기본 통계적 속성(평균, 중앙값, 분산 등)을 계산합니다:

```python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```

18. The SciPy project <https://scipy.org> has many other modules for numerical computations.

SciPy 프로젝트 <https://scipy.org>에는 수치 계산을 위한 다른 많은 모듈이 있습니다.

## 10.7. Internet Access

19. There are a number of modules for accessing the internet and processing internet protocols. Two of the simplest are urllib.request for retrieving data from URLs and smtplib for sending mail:

인터넷에 접근하고 인터넷 프로토콜을 처리하기 위한 여러 모듈이 있습니다. 가장 간단한 두 가지는 URL에서 데이터를 검색하기 위한 urllib.request와 메일을 보내기 위한 smtplib입니다:

```python
>>> from urllib.request import urlopen
>>> with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
...     for line in response:
...         line = line.decode()             # Convert bytes to a str
...         if line.startswith('datetime'):
...             print(line.rstrip())         # Remove trailing newline
...
datetime: 2022-01-01T01:36:47.689215+00:00

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()
```

20. (Note that the second example needs a mailserver running on localhost.)

(두 번째 예제는 localhost에서 실행 중인 메일서버가 필요합니다.)

## 10.8. Dates and Times

21. The datetime module supplies classes for manipulating dates and times in both simple and complex ways. While date and time arithmetic is supported, the focus of the implementation is on efficient member extraction for output formatting and manipulation. The module also supports objects that are timezone aware.

datetime 모듈은 간단하거나 복잡한 방식으로 날짜와 시간을 조작하기 위한 클래스를 제공합니다. 날짜와 시간 계산이 지원되지만, 구현의 초점은 출력 형식 지정과 조작을 위한 효율적인 멤버 추출에 있습니다. 이 모듈은 시간대를 인식하는 객체도 지원합니다.

```python
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```

## 10.9. Data Compression

22. Common data archiving and compression formats are directly supported by modules including: zlib, gzip, bz2, lzma, zipfile and tarfile.

일반적인 데이터 보관 및 압축 형식은 zlib, gzip, bz2, lzma, zipfile, tarfile을 포함한 모듈에 의해 직접 지원됩니다.

```python
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```

## 10.10. Performance Measurement

23. Some Python users develop a deep interest in knowing the relative performance of different approaches to the same problem. Python provides a measurement tool that answers those questions immediately.

일부 Python 사용자는 동일한 문제에 대한 다른 접근 방식의 상대적 성능을 알고자 하는 깊은 관심을 가지고 있습니다. Python은 이러한 질문에 즉시 답변하는 측정 도구를 제공합니다.

24. For example, it may be tempting to use the tuple packing and unpacking feature instead of the traditional approach to swapping arguments. The timeit module quickly demonstrates a modest performance advantage:

예를 들어, 인수를 교환하는 전통적인 접근 방식 대신 튜플 패킹 및 언패킹 기능을 사용하는 것이 유혹적일 수 있습니다. timeit 모듈은 완만한 성능 이점을 빠르게 보여줍니다:

```python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```

25. In contrast to timeit's fine level of granularity, the profile and pstats modules provide tools for identifying time critical sections in larger blocks of code.

timeit의 정밀한 수준의 세분성과 대조적으로, profile 및 pstats 모듈은 더 큰 코드 블록에서 시간이 중요한 섹션을 식별하기 위한 도구를 제공합니다.

## 10.11. Quality Control

26. One approach for developing high quality software is to write tests for each function as it is developed and to run those tests frequently during the development process.

고품질 소프트웨어를 개발하는 한 가지 접근 방식은 개발되는 각 함수에 대한 테스트를 작성하고 개발 과정에서 해당 테스트를 자주 실행하는 것입니다.

27. The doctest module provides a tool for scanning a module and validating tests embedded in a program's docstrings. Test construction is as simple as cutting-and-pasting a typical call along with its results into the docstring. This improves the documentation by providing the user with an example and it allows the doctest module to make sure the code remains true to the documentation:

doctest 모듈은 모듈을 스캔하고 프로그램의 docstring에 내장된 테스트를 검증하기 위한 도구를 제공합니다. 테스트 구성은 일반적인 호출과 그 결과를 docstring에 복사하여 붙여넣는 것만큼 간단합니다. 이는 사용자에게 예제를 제공함으로써 문서를 개선하고, doctest 모듈이 코드가 문서에 충실하게 유지되도록 확인할 수 있게 합니다:

```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
```

28. The unittest module is not as effortless as the doctest module, but it allows a more comprehensive set of tests to be maintained in a separate file:

unittest 모듈은 doctest 모듈만큼 쉽지는 않지만, 별도의 파일에서 더 포괄적인 테스트 세트를 유지할 수 있습니다:

```python
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
```

## 10.12. Batteries Included

29. Python has a "batteries included" philosophy. This is best seen through the sophisticated and robust capabilities of its larger packages. For example:

Python은 "내장된 배터리" 철학을 가지고 있습니다. 이는 더 큰 패키지의 정교하고 강력한 기능을 통해 가장 잘 알 수 있습니다. 예를 들어:

30. The xmlrpc.client and xmlrpc.server modules make implementing remote procedure calls into an almost trivial task. Despite the modules' names, no direct knowledge or handling of XML is needed.

xmlrpc.client 및 xmlrpc.server 모듈은 원격 프로시저 호출을 구현하는 것을 거의 사소한 작업으로 만듭니다. 모듈 이름에도 불구하고, XML에 대한 직접적인 지식이나 처리가 필요하지 않습니다.

31. The email package is a library for managing email messages, including MIME and other RFC 2822-based message documents. Unlike smtplib and poplib which actually send and receive messages, the email package has a complete toolset for building or decoding complex message structures (including attachments) and for implementing internet encoding and header protocols.

email 패키지는 MIME 및 기타 RFC 2822 기반 메시지 문서를 포함한 이메일 메시지를 관리하기 위한 라이브러리입니다. 실제로 메시지를 보내고 받는 smtplib 및 poplib와 달리, email 패키지는 복잡한 메시지 구조(첨부 파일 포함)를 구축하거나 디코딩하고, 인터넷 인코딩 및 헤더 프로토콜을 구현하기 위한 완전한 도구 세트를 제공합니다.

32. The json package provides robust support for parsing this popular data interchange format. The csv module supports direct reading and writing of files in Comma-Separated Value format, commonly supported by databases and spreadsheets. XML processing is supported by the xml.etree.ElementTree, xml.dom and xml.sax packages. Together, these modules and packages greatly simplify data interchange between Python applications and other tools.

json 패키지는 이 인기있는 데이터 교환 형식을 파싱하기 위한 강력한 지원을 제공합니다. csv 모듈은 데이터베이스나 스프레드시트에서 일반적으로 지원되는 쉼표로 구분된 값 형식의 파일을 직접 읽고 쓰는 것을 지원합니다. XML 처리는 xml.etree.ElementTree, xml.dom 및 xml.sax 패키지에 의해 지원됩니다. 이러한 모듈과 패키지를 함께 사용하면 Python 응용 프로그램과 다른 도구 간의 데이터 교환이 크게 단순화됩니다.

33. The sqlite3 module is a wrapper for the SQLite database library, providing a persistent database that can be updated and accessed using slightly nonstandard SQL syntax.

sqlite3 모듈은 SQLite 데이터베이스 라이브러리의 래퍼로, 약간 비표준 SQL 구문을 사용하여 업데이트하고 접근할 수 있는 영구적인 데이터베이스를 제공합니다.

34. Internationalization is supported by a number of modules including gettext, locale, and the codecs package.

국제화는 gettext, locale 및 codecs 패키지를 포함한 여러 모듈에 의해 지원됩니다.
