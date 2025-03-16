# 11. Brief Tour of the Standard Library — Part II

1. This second tour covers more advanced modules that support professional programming needs. These modules rarely occur in small scripts.

이 두 번째 둘러보기에서는 전문적인 프로그래밍 요구를 지원하는 더 고급 모듈을 다룹니다. 이러한 모듈은 작은 스크립트에서는 거의 사용되지 않습니다.

## 11.1. Output Formatting

2. The reprlib module provides a version of repr() customized for abbreviated displays of large or deeply nested containers:

reprlib 모듈은 크거나 깊게 중첩된 컨테이너의 축약된 표시를 위해 사용자 지정된 repr() 버전을 제공합니다:

```python
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```

3. The pprint module offers more sophisticated control over printing both built-in and user defined objects in a way that is readable by the interpreter. When the result is longer than one line, the "pretty printer" adds line breaks and indentation to more clearly reveal data structure:

pprint 모듈은 내장 객체와 사용자 정의 객체 모두를 인터프리터가 읽을 수 있는 방식으로 출력하는 더 정교한 제어를 제공합니다. 결과가 한 줄보다 길면, "예쁜 프린터"는 데이터 구조를 더 명확하게 보여주기 위해 줄 바꿈과 들여쓰기를 추가합니다:

```python
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
...     'yellow'], 'blue']]]
>>> 
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
```

4. The textwrap module formats paragraphs of text to fit a given screen width:

textwrap 모듈은 주어진 화면 너비에 맞게 텍스트 단락의 형식을 지정합니다:

```python
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""
>>> 
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
```

5. The locale module accesses a database of culture specific data formats. The grouping attribute of locale's format function provides a direct way of formatting numbers with group separators:

locale 모듈은 문화별 데이터 형식의 데이터베이스에 접근합니다. locale의 format 함수의 grouping 속성은 그룹 구분 기호로 숫자 형식을 지정하는 직접적인 방법을 제공합니다:

```python
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv()          # get a mapping of conventions
>>> x = 1234567.8
>>> locale.format_string("%d", x, grouping=True)
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
...                      conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
```

## 11.2. Templating

6. The string module includes a versatile Template class with a simplified syntax suitable for editing by end-users. This allows users to customize their applications without having to alter the application.

string 모듈에는 최종 사용자가 편집하기에 적합한 단순화된 구문을 가진 다재다능한 Template 클래스가 포함되어 있습니다. 이를 통해 사용자는 애플리케이션을 변경하지 않고도 애플리케이션을 사용자 정의할 수 있습니다.

7. The format uses placeholder names formed by $ with valid Python identifiers (alphanumeric characters and underscores). Surrounding the placeholder with braces allows it to be followed by more alphanumeric letters with no intervening spaces. Writing $$ creates a single escaped $:

형식은 유효한 파이썬 식별자(영숫자 및 밑줄)와 함께 $로 형성된 자리 표시자 이름을 사용합니다. 자리 표시자를 중괄호로 둘러싸면 중간에 공백 없이 더 많은 영숫자를 뒤에 붙일 수 있습니다. $$를 작성하면 단일 이스케이프된 $가 생성됩니다:

```python
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
```

8. The substitute() method raises a KeyError when a placeholder is not supplied in a dictionary or a keyword argument. For mail-merge style applications, user supplied data may be incomplete and the safe_substitute() method may be more appropriate — it will leave placeholders unchanged if data is missing:

substitute() 메서드는 사전이나 키워드 인수에 자리 표시자가 제공되지 않으면 KeyError를 발생시킵니다. 메일 병합 스타일의 애플리케이션의 경우, 사용자가 제공한 데이터가 불완전할 수 있으므로 safe_substitute() 메서드가 더 적합할 수 있습니다 — 데이터가 없는 경우 자리 표시자를 변경하지 않습니다:

```python
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  ...
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'
```

9. Template subclasses can specify a custom delimiter. For example, a batch renaming utility for a photo browser may elect to use percent signs for placeholders such as the current date, image sequence number, or file format:

Template 서브클래스는 사용자 지정 구분자를 지정할 수 있습니다. 예를 들어, 사진 브라우저용 일괄 이름 바꾸기 유틸리티는 현재 날짜, 이미지 시퀀스 번호 또는 파일 형식과 같은 자리 표시자에 퍼센트 기호를 사용하도록 선택할 수 있습니다:

```python
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
...     delimiter = '%'
... 
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f
>>> 
>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
...     base, ext = os.path.splitext(filename)
...     newname = t.substitute(d=date, n=i, f=ext)
...     print('{0} --> {1}'.format(filename, newname))
... 
img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
```

10. Another application for templating is separating program logic from the details of multiple output formats. This makes it possible to substitute custom templates for XML files, plain text reports, and HTML web reports.

템플릿의 또 다른 응용은 프로그램 로직을 여러 출력 형식의 세부 사항과 분리하는 것입니다. 이를 통해 XML 파일, 일반 텍스트 보고서 및 HTML 웹 보고서에 대한 사용자 정의 템플릿을 대체할 수 있습니다.

## 11.3. Working with Binary Data Record Layouts

11. The struct module provides pack() and unpack() functions for working with variable length binary record formats. The following example shows how to loop through header information in a ZIP file without using the zipfile module. Pack codes "H" and "I" represent two and four byte unsigned numbers respectively. The "<" indicates that they are standard size and in little-endian byte order:

struct 모듈은 가변 길이 이진 레코드 형식을 다루기 위한 pack() 및 unpack() 함수를 제공합니다. 다음 예제는 zipfile 모듈을 사용하지 않고 ZIP 파일의 헤더 정보를 반복하는 방법을 보여줍니다. 팩 코드 "H" 및 "I"는 각각 2바이트 및 4바이트 부호 없는 숫자를 나타냅니다. "<"는 표준 크기이고 리틀 엔디안 바이트 순서임을 나타냅니다:

```python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
```

## 11.4. Multi-threading

12. Threading is a technique for decoupling tasks which are not sequentially dependent. Threads can be used to improve the responsiveness of applications that accept user input while other tasks run in the background. A related use case is running I/O in parallel with computations in another thread.

스레딩은 순차적으로 의존하지 않는 작업을 분리하는 기술입니다. 스레드는 다른 작업이 백그라운드에서 실행되는 동안 사용자 입력을 수락하는 애플리케이션의 응답성을 향상시키는 데 사용될 수 있습니다. 관련 사용 사례는 다른 스레드의 계산과 병렬로 I/O를 실행하는 것입니다.

13. The following code shows how the high level threading module can run tasks in background while the main program continues to run:

다음 코드는 메인 프로그램이 계속 실행되는 동안 고수준 스레딩 모듈이 백그라운드에서 작업을 실행하는 방법을 보여줍니다:

```python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```

14. The principal challenge of multi-threaded applications is coordinating threads that share data or other resources. To that end, the threading module provides a number of synchronization primitives including locks, events, condition variables, and semaphores.

다중 스레드 애플리케이션의 주요 과제는 데이터나 기타 리소스를 공유하는 스레드를 조정하는 것입니다. 이를 위해 threading 모듈은 잠금, 이벤트, 조건 변수 및 세마포어를 포함한 여러 동기화 기본 요소를 제공합니다.

15. While those tools are powerful, minor design errors can result in problems that are difficult to reproduce. So, the preferred approach to task coordination is to concentrate all access to a resource in a single thread and then use the queue module to feed that thread with requests from other threads. Applications using Queue objects for inter-thread communication and coordination are easier to design, more readable, and more reliable.

이러한 도구들이 강력하지만, 작은 설계 오류로 인해 재현하기 어려운 문제가 발생할 수 있습니다. 따라서, 작업 조정에 선호되는 접근 방식은 단일 스레드에서 자원에 대한 모든 접근을 집중시키고 queue 모듈을 사용하여 다른 스레드의 요청으로 해당 스레드를 공급하는 것입니다. Queue 객체를 사용하여 스레드 간 통신 및 조정을 하는 애플리케이션은 설계가 더 쉽고, 더 읽기 쉬우며, 더 안정적입니다.

## 11.5. Logging

16. The logging module offers a full featured and flexible logging system. At its simplest, log messages are sent to a file or to sys.stderr:

logging 모듈은 완전한 기능을 갖춘 유연한 로깅 시스템을 제공합니다. 가장 간단하게, 로그 메시지는 파일이나 sys.stderr로 전송됩니다:

```python
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```

17. This produces the following output:

이는 다음과 같은 출력을 생성합니다:

```
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down
```

18. By default, informational and debugging messages are suppressed and the output is sent to standard error. Other output options include routing messages through email, datagrams, sockets, or to an HTTP Server. New filters can select different routing based on message priority: DEBUG, INFO, WARNING, ERROR, and CRITICAL.

기본적으로, 정보 및 디버깅 메시지는 억제되고 출력은 표준 오류로 전송됩니다. 다른 출력 옵션으로는 이메일, 데이터그램, 소켓 또는 HTTP 서버를 통한 메시지 라우팅이 포함됩니다. 새 필터는 메시지 우선 순위(DEBUG, INFO, WARNING, ERROR 및 CRITICAL)에 따라 다른 라우팅을 선택할 수 있습니다.

19. The logging system can be configured directly from Python or can be loaded from a user editable configuration file for customized logging without altering the application.

로깅 시스템은 파이썬에서 직접 구성되거나 애플리케이션을 변경하지 않고 사용자 편집 가능한 구성 파일에서 로드하여 사용자 정의 로깅을 할 수 있습니다.

## 11.6. Weak References

20. Python does automatic memory management (reference counting for most objects and garbage collection to eliminate cycles). The memory is freed shortly after the last reference to it has been eliminated.

파이썬은 자동 메모리 관리를 수행합니다(대부분의 객체에 대한 참조 카운팅 및 순환을 제거하기 위한 가비지 컬렉션). 메모리는 그것에 대한 마지막 참조가 제거된 직후에 해제됩니다.

21. This approach works fine for most applications but occasionally there is a need to track objects only as long as they are being used by something else. Unfortunately, just tracking them creates a reference that makes them permanent. The weakref module provides tools for tracking objects without creating a reference. When the object is no longer needed, it is automatically removed from a weakref table and a callback is triggered for weakref objects. Typical applications include caching objects that are expensive to create:

이 접근 방식은 대부분의 애플리케이션에서 잘 작동하지만, 간혹 다른 무언가에 의해 사용되는 동안에만 객체를 추적해야 할 필요가 있습니다. 불행하게도, 단순히 그들을 추적하는 것은 그들을 영구적으로 만드는 참조를 생성합니다. weakref 모듈은 참조를 생성하지 않고 객체를 추적하기 위한 도구를 제공합니다. 객체가 더 이상 필요하지 않으면, 자동으로 weakref 테이블에서 제거되고 weakref 객체에 대한 콜백이 트리거됩니다. 일반적인 응용에는 생성하는 데 비용이 많이 드는 객체를 캐싱하는 것이 포함됩니다:

```python
>>> import weakref, gc
>>> class A:
...     def __init__(self, value):
...         self.value = value
...     def __repr__(self):
...         return str(self.value)
... 
>>> a = A(10)                   # create a reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a            # does not create a reference
>>> d['primary']                # fetch the object if it is still alive
10
>>> del a                       # remove the one reference
>>> gc.collect()                # run garbage collection right away
0
>>> d['primary']                # entry was automatically removed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entry was automatically removed
  File "C:/python313/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
```

## 11.7. Tools for Working with Lists

22. Many data structure needs can be met with the built-in list type. However, sometimes there is a need for alternative implementations with different performance trade-offs.

많은 데이터 구조 요구는 내장 리스트 유형으로 충족될 수 있습니다. 그러나, 때로는 다른 성능 트레이드오프를 가진 대안 구현이 필요할 때가 있습니다.

23. The array module provides an array object that is like a list that stores only homogeneous data and stores it more compactly. The following example shows an array of numbers stored as two byte unsigned binary numbers (typecode "H") rather than the usual 16 bytes per entry for regular lists of Python int objects:

array 모듈은 동종 데이터만 저장하고 더 컴팩트하게 저장하는 리스트와 같은 배열 객체를 제공합니다. 다음 예제는 일반 Python int 객체 리스트의 항목당 일반적인 16바이트 대신 두 바이트 부호 없는 이진 숫자(유형 코드 "H")로 저장된 숫자 배열을 보여줍니다:

```python
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
```

24. The collections module provides a deque object that is like a list with faster appends and pops from the left side but slower lookups in the middle. These objects are well suited for implementing queues and breadth first tree searches:

collections 모듈은 리스트와 비슷하지만 왼쪽에서의 추가와 제거가 더 빠르고 중간에서의 조회는 더 느린 deque 객체를 제공합니다. 이러한 객체는 큐와 너비 우선 트리 검색을 구현하는 데 적합합니다:

```python
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1
>>> unsearched = deque([starting_node])
>>> def breadth_first_search(unsearched):
...     node = unsearched.popleft()
...     for m in gen_moves(node):
...         if is_goal(m):
...             return m
...         unsearched.append(m)
```

25. In addition to alternative list implementations, the library also offers other tools such as the bisect module with functions for manipulating sorted lists:

대체 리스트 구현 외에도, 라이브러리는 정렬된 리스트를 조작하기 위한 함수가 있는 bisect 모듈과 같은 다른 도구도 제공합니다:

```python
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
```

26. The heapq module provides functions for implementing heaps based on regular lists. The lowest valued entry is always kept at position zero. This is useful for applications which repeatedly access the smallest element but do not want to run a full list sort:

heapq 모듈은 일반 리스트를 기반으로 힙을 구현하기 위한 함수를 제공합니다. 가장 낮은 값의 항목은 항상 위치 0에 유지됩니다. 이는 가장 작은 요소에 반복적으로 접근하지만 전체 리스트 정렬을 실행하고 싶지 않은 응용 프로그램에 유용합니다:

```python
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data)                      # rearrange the list into heap order
>>> heappush(data, -5)                 # add a new entry
>>> [heappop(data) for i in range(3)]  # fetch the three smallest entries
[-5, 0, 1]
```

## 11.8. Decimal Floating-Point Arithmetic

27. The decimal module offers a Decimal datatype for decimal floating-point arithmetic. Compared to the built-in float implementation of binary floating point, the class is especially helpful for:

decimal 모듈은 십진 부동 소수점 산술을 위한 Decimal 데이터 유형을 제공합니다. 내장된 이진 부동 소수점의 float 구현과 비교하여, 이 클래스는 특히 다음과 같은 경우에 도움이 됩니다:

28. financial applications and other uses which require exact decimal representation,

금융 애플리케이션 및 정확한 십진 표현이 필요한 기타 용도,

29. control over precision,

정밀도 제어,

30. control over rounding to meet legal or regulatory requirements,

법적 또는 규제 요구 사항을 충족하기 위한 반올림 제어,

31. tracking of significant decimal places, or

중요한 소수 자릿수 추적, 또는

32. applications where the user expects the results to match calculations done by hand.

사용자가 결과가 손으로 계산한 것과 일치하기를 기대하는 애플리케이션.

33. For example, calculating a 5% tax on a 70 cent phone charge gives different results in decimal floating point and binary floating point. The difference becomes significant if the results are rounded to the nearest cent:

예를 들어, 70센트의 전화 요금에 5% 세금을 계산하면 십진 부동 소수점과 이진 부동 소수점에서 다른 결과가 나옵니다. 결과가 가장 가까운 센트로 반올림되면 차이가 중요해집니다:

```python
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
```

34. The Decimal result keeps a trailing zero, automatically inferring four place significance from multiplicands with two place significance. Decimal reproduces mathematics as done by hand and avoids issues that can arise when binary floating point cannot exactly represent decimal quantities.

Decimal 결과는 끝에 0을 유지하며, 두 자리 중요도를 가진 승수에서 자동으로 네 자리 중요도를 추론합니다. Decimal은 손으로 계산한 것처럼 수학을 재현하고 이진 부동 소수점이 십진 수량을 정확히 나타낼 수 없을 때 발생할 수 있는 문제를 피합니다.

35. Exact representation enables the Decimal class to perform modulo calculations and equality tests that are unsuitable for binary floating point:

정확한 표현을 통해 Decimal 클래스는 이진 부동 소수점에 적합하지 않은 모듈로 계산과 동등성 테스트를 수행할 수 있습니다:

```python
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995

>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0
False
```

36. The decimal module provides arithmetic with as much precision as needed:

decimal 모듈은 필요한 만큼의 정밀도로 산술을 제공합니다:

```python
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
```
