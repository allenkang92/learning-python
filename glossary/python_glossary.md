# Python 용어집 (Python Glossary)

## >>>
The default Python prompt of the interactive shell. Often seen for code examples which can be executed interactively in the interpreter.

대화형 셸의 기본 Python 프롬프트. 인터프리터에서 대화식으로 실행할 수 있는 코드 예제에서 자주 볼 수 있습니다.

## ...
Can refer to:
- The default Python prompt of the interactive shell when entering the code for an indented code block, when within a pair of matching left and right delimiters (parentheses, square brackets, curly braces or triple quotes), or after specifying a decorator.
- The Ellipsis built-in constant.

다음을 지칭할 수 있습니다:
- 들여쓰기된 코드 블록 입력, 한 쌍의 일치하는 왼쪽 및 오른쪽 구분 기호(괄호, 대괄호, 중괄호 또는 삼중 따옴표) 내에 있을 때, 또는 데코레이터를 지정한 후 대화형 셸의 기본 Python 프롬프트.
- Ellipsis 내장 상수.

## abstract base class (추상 기본 클래스)
Abstract base classes complement duck-typing by providing a way to define interfaces when other techniques like hasattr() would be clumsy or subtly wrong (for example with magic methods). ABCs introduce virtual subclasses, which are classes that don't inherit from a class but are still recognized by isinstance() and issubclass(); see the abc module documentation. Python comes with many built-in ABCs for data structures (in the collections.abc module), numbers (in the numbers module), streams (in the io module), import finders and loaders (in the importlib.abc module). You can create your own ABCs with the abc module.

추상 기본 클래스는 hasattr()와 같은 다른 기술이 어색하거나 미묘하게 틀릴 수 있을 때(예: 매직 메서드 사용 시) 인터페이스를 정의하는 방법을 제공하여 덕 타이핑을 보완합니다. ABC는 클래스에서 상속받지 않지만 여전히 isinstance()와 issubclass()에 의해 인식되는 가상 서브클래스를 도입합니다; abc 모듈 설명서를 참조하세요. Python은 데이터 구조(collections.abc 모듈), 숫자(numbers 모듈), 스트림(io 모듈), 가져오기 검색기 및 로더(importlib.abc 모듈)를 위한 많은 내장 ABC를 제공합니다. abc 모듈을 사용하여 자신만의 ABC를 만들 수 있습니다.

## annotation (주석)
A label associated with a variable, a class attribute or a function parameter or return value, used by convention as a type hint.

Annotations of local variables cannot be accessed at runtime, but annotations of global variables, class attributes, and functions are stored in the __annotations__ special attribute of modules, classes, and functions, respectively.

See variable annotation, function annotation, PEP 484 and PEP 526, which describe this functionality. Also see Annotations Best Practices for best practices on working with annotations.

변수, 클래스 속성 또는 함수 매개변수나 반환 값과 연결된 레이블로, 관례상 타입 힌트로 사용됩니다.

지역 변수의 주석은 런타임에 액세스할 수 없지만, 전역 변수, 클래스 속성 및 함수의 주석은 각각 모듈, 클래스 및 함수의 __annotations__ 특수 속성에 저장됩니다.

이 기능을 설명하는 변수 주석, 함수 주석, PEP 484 및 PEP 526을 참조하세요. 또한 주석 작업에 대한 모범 사례는 주석 모범 사례를 참조하세요.

## argument (인자)
A value passed to a function (or method) when calling the function. There are two kinds of argument:

keyword argument: an argument preceded by an identifier (e.g. name=) in a function call or passed as a value in a dictionary preceded by **. For example, 3 and 5 are both keyword arguments in the following calls to complex():

```python
complex(real=3, imag=5)
complex(**{'real': 3, 'imag': 5})
```

positional argument: an argument that is not a keyword argument. Positional arguments can appear at the beginning of an argument list and/or be passed as elements of an iterable preceded by *. For example, 3 and 5 are both positional arguments in the following calls:

```python
complex(3, 5)
complex(*(3, 5))
```

Arguments are assigned to the named local variables in a function body. See the Calls section for the rules governing this assignment. Syntactically, any expression can be used to represent an argument; the evaluated value is assigned to the local variable.

See also the parameter glossary entry, the FAQ question on the difference between arguments and parameters, and PEP 362.

함수(또는 메서드)를 호출할 때 함수에 전달되는 값. 인자에는 두 가지 종류가 있습니다:

**keyword argument (키워드 인자)**: 함수 호출에서 식별자(예: name=)가 앞에 오거나 **가 앞에 오는 딕셔너리로 전달되는 인자. 예를 들어, complex() 호출에서 3과 5는 모두 키워드 인자입니다:

```python
complex(real=3, imag=5)
complex(**{'real': 3, 'imag': 5})
```

**positional argument (위치 인자)**: 키워드 인자가 아닌 인자. 위치 인자는 인자 목록의 시작 부분에 나타나거나 *가 앞에 오는 반복 가능한 객체의 요소로 전달될 수 있습니다. 예를 들어, 다음 호출에서 3과 5는 모두 위치 인자입니다:

```python
complex(3, 5)
complex(*(3, 5))
```

인자는 함수 본문에 명명된 지역 변수에 할당됩니다. 이 할당을 제어하는 규칙은 호출 섹션을 참조하세요. 구문적으로, 모든 표현식을 사용하여 인자를 표현할 수 있습니다; 평가된 값이 지역 변수에 할당됩니다.

또한 매개변수 용어집 항목, 인자와 매개변수의 차이에 대한 FAQ 질문, 그리고 PEP 362를 참조하세요.

## asynchronous context manager (비동기 컨텍스트 관리자)
An object which controls the environment seen in an async with statement by defining __aenter__() and __aexit__() methods. Introduced by PEP 492.

__aenter__()와 __aexit__() 메서드를 정의하여 async with 문에서 볼 수 있는 환경을 제어하는 객체. PEP 492에서 소개되었습니다.

## asynchronous generator (비동기 제너레이터)
A function which returns an asynchronous generator iterator. It looks like a coroutine function defined with async def except that it contains yield expressions for producing a series of values usable in an async for loop.

Usually refers to an asynchronous generator function, but may refer to an asynchronous generator iterator in some contexts. In cases where the intended meaning isn't clear, using the full terms avoids ambiguity.

An asynchronous generator function may contain await expressions as well as async for, and async with statements.

비동기 제너레이터 반복자를 반환하는 함수. async for 루프에서 사용 가능한 일련의 값을 생성하기 위해 yield 표현식을 포함한다는 점을 제외하면 async def로 정의된 코루틴 함수와 비슷합니다.

보통 비동기 제너레이터 함수를 지칭하지만, 일부 맥락에서는 비동기 제너레이터 반복자를 지칭할 수도 있습니다. 의도한 의미가 명확하지 않은 경우, 전체 용어를 사용하면 모호성을 피할 수 있습니다.

비동기 제너레이터 함수는 await 표현식은 물론 async for 및 async with 문도 포함할 수 있습니다.

## asynchronous generator iterator (비동기 제너레이터 반복자)
An object created by a asynchronous generator function.

This is an asynchronous iterator which when called using the __anext__() method returns an awaitable object which will execute the body of the asynchronous generator function until the next yield expression.

Each yield temporarily suspends processing, remembering the execution state (including local variables and pending try-statements). When the asynchronous generator iterator effectively resumes with another awaitable returned by __anext__(), it picks up where it left off. See PEP 492 and PEP 525.

비동기 제너레이터 함수에 의해 생성된 객체.

이는 __anext__() 메서드를 사용하여 호출할 때 비동기 제너레이터 함수의 본문을 다음 yield 표현식까지 실행하는 awaitable 객체를 반환하는 비동기 반복자입니다.

각 yield는 실행 상태(지역 변수 및 보류 중인 try 문 포함)를 기억하면서 처리를 일시적으로 중단합니다. 비동기 제너레이터 반복자가 __anext__()에 의해 반환된 다른 awaitable로 효과적으로 재개될 때, 중단된 지점부터 다시 시작합니다. PEP 492와 PEP 525를 참조하세요.

## asynchronous iterable (비동기 반복 가능)
An object, that can be used in an async for statement. Must return an asynchronous iterator from its __aiter__() method. Introduced by PEP 492.

async for 문에서 사용할 수 있는 객체. __aiter__() 메서드에서 비동기 반복자를 반환해야 합니다. PEP 492에서 소개되었습니다.

## asynchronous iterator (비동기 반복자)
An object that implements the __aiter__() and __anext__() methods. __anext__() must return an awaitable object. async for resolves the awaitables returned by an asynchronous iterator's __anext__() method until it raises a StopAsyncIteration exception. Introduced by PEP 492.

__aiter__() 및 __anext__() 메서드를 구현하는 객체. __anext__()는 awaitable 객체를 반환해야 합니다. async for는 비동기 반복자의 __anext__() 메서드가 StopAsyncIteration 예외를 발생시킬 때까지 반환된 awaitable을 해결합니다. PEP 492에서 소개되었습니다.

## attribute (속성)
A value associated with an object which is usually referenced by name using dotted expressions. For example, if an object o has an attribute a it would be referenced as o.a.

It is possible to give an object an attribute whose name is not an identifier as defined by Identifiers and keywords, for example using setattr(), if the object allows it. Such an attribute will not be accessible using a dotted expression, and would instead need to be retrieved with getattr().

객체와 연관된 값으로, 보통 점 표현식을 사용하여 이름으로 참조됩니다. 예를 들어, 객체 o에 속성 a가 있다면 o.a로 참조됩니다.

객체가 허용한다면, setattr()를 사용하여 Identifiers and keywords에 정의된 대로 식별자가 아닌 이름의 속성을 객체에 부여하는 것이 가능합니다. 그러한 속성은 점 표현식을 사용하여 접근할 수 없으며, 대신 getattr()로 검색해야 합니다.

## awaitable (대기 가능)
An object that can be used in an await expression. Can be a coroutine or an object with an __await__() method. See also PEP 492.

await 표현식에서 사용할 수 있는 객체. 코루틴이나 __await__() 메서드가 있는 객체일 수 있습니다. 또한 PEP 492를 참조하세요.

## BDFL
Benevolent Dictator For Life, a.k.a. Guido van Rossum, Python's creator.

Benevolent Dictator For Life(자비로운 종신 독재자), 즉 Python의 창시자인 Guido van Rossum을 지칭합니다.

## binary file (이진 파일)
A file object able to read and write bytes-like objects. Examples of binary files are files opened in binary mode ('rb', 'wb' or 'rb+'), sys.stdin.buffer, sys.stdout.buffer, instances of io.BytesIO and gzip.GzipFile.

For file objects able to read and write str objects, see text file.

바이트 유사 객체를 읽고 쓸 수 있는 파일 객체. 이진 파일의 예로는 이진 모드('rb', 'wb' 또는 'rb+')로 열린 파일, sys.stdin.buffer, sys.stdout.buffer, 그리고 io.BytesIO와 gzip.GzipFile의 인스턴스가 있습니다.

str 객체를 읽고 쓸 수 있는 파일 객체는 text file을 참조하세요.

## borrowed reference (대여된 참조)
In the C API, a borrowed reference is a reference to an object that is not owned by the code that uses it. The object will be destroyed if the reference count drops to zero. For example, garbage collection may destroy an object when the last strong reference to it is removed.

It is recommended to use Py_INCREF() to convert a borrowed reference to a strong reference in place, unless it is guaranteed that the object will not be destroyed before the last use of the borrowed reference. The Py_NewRef() function can be used to create a new strong reference.

Python의 C API에서, 대여된 참조는 코드가 참조를 소유하지 않는 객체에 대한 참조입니다. 객체가 파괴되면 dangling pointer(허상 포인터)가 됩니다. 예를 들어, 가비지 컬렉션은 객체에 대한 마지막 강한 참조를 제거하여 객체를 파괴할 수 있습니다.

대여된 참조에 Py_INCREF()를 호출하여 제자리에서 강한 참조로 변환하는 것이 권장되지만, 대여된 참조의 마지막 사용 전에 객체가 파괴될 수 없는 경우는 예외입니다. Py_NewRef() 함수를 사용하여 새로운 강한 참조를 만들 수 있습니다.

## bytes-like object (바이트 유사 객체)
An object that supports the Buffer Protocol and can export a C-contiguous buffer. This includes all bytes, bytearray, and array.array objects, as well as many common memoryview objects. Bytes-like objects can be used for various operations that work with binary data; these include compression, saving to a binary file, and sending over a socket.

Some operations need the binary data to be mutable. The documentation often refers to these as "read-write bytes-like objects". Examples of mutable buffer objects include bytearray and a memoryview of a bytearray. Other operations require the binary data to be stored in immutable objects ("read-only bytes-like objects"). Examples of these include bytes and a memoryview of a bytes object.

Buffer Protocol을 지원하고 C-contiguous 버퍼를 내보낼 수 있는 객체입니다. 여기에는 모든 bytes, bytearray 및 array.array 객체와 많은 일반적인 memoryview 객체가 포함됩니다. 바이트 유사 객체는 이진 데이터로 작업하는 다양한 작업에 사용될 수 있습니다. 여기에는 압축, 이진 파일에 저장, 소켓을 통한 전송이 포함됩니다.

일부 작업에서는 이진 데이터가 변경 가능해야 합니다. 문서에서는 이를 종종 "읽기-쓰기 바이트 유사 객체"라고 합니다. 변경 가능한 버퍼 객체의 예로는 bytearray와 bytearray의 memoryview가 있습니다. 다른 작업에서는 이진 데이터가 불변 객체("읽기 전용 바이트 유사 객체")에 저장되어야 합니다. 이러한 예로는 bytes와 bytes 객체의 memoryview가 있습니다.

## bytecode (바이트코드)
Python source code is compiled into bytecode, the internal representation of a Python program in the CPython interpreter. The bytecode is cached in .pyc files so that executing the same file is faster the second time (bypassing the compilation from source to bytecode). This "intermediate language" is said to run on a virtual machine that executes the corresponding machine code for each bytecode. Bytecode is not expected to work between different Python virtual machines, nor to be stable between Python releases.

A list of bytecode instructions can be found in the dis module documentation.

Python 소스 코드는 CPython 인터프리터에서 Python 프로그램의 내부 표현인 바이트코드로 컴파일됩니다. 바이트코드는 동일한 파일을 실행하는 것이 두 번째에는 더 빠르도록 .pyc 파일에 캐시됩니다(소스에서 바이트코드로의 재컴파일을 피할 수 있음). 이 "중간 언어"는 각 바이트코드에 해당하는 기계어 코드를 실행하는 가상 머신에서 실행된다고 합니다. 바이트코드는 다른 Python 가상 머신 간에 작동하거나 Python 릴리스 간에 안정적으로 유지될 것으로 예상되지 않습니다.

바이트코드 명령어 목록은 dis 모듈 문서에서 찾을 수 있습니다.

## callable (호출 가능한 객체)
An object is callable if it can be called, possibly with a set of arguments, in the following syntax:

```python
callable(argument1, argument2, argumentN)
```

Functions, and methods are callable. Instances of classes that implement __call__() are also callable.

호출 가능한 객체는 다음 구문으로 (가능하게는 인수 집합과 함께) 호출될 수 있는 객체입니다:

```python
callable(argument1, argument2, argumentN)
```

함수, 그리고 확장하면 메서드는 호출 가능합니다. __call__() 메서드를 구현하는 클래스의 인스턴스도 호출 가능합니다.

## callback (콜백)
A subroutine function which is passed as an argument to be executed later.

나중에 어떤 시점에 실행되도록 인수로 전달되는 서브루틴 함수입니다.

## class (클래스)
A template for creating user-defined objects. Class definitions normally contain method definitions which operate on instances of the class.

사용자 정의 객체를 생성하기 위한 템플릿입니다. 클래스 정의는 일반적으로 클래스의 인스턴스에서 작동하는 메서드 정의를 포함합니다.

## class variable (클래스 변수)
A variable defined in a class and intended to be modified only at the class level, not in an instance of the class.

클래스에 정의되고 클래스 수준에서만 수정되도록 의도된 변수(즉, 클래스의 인스턴스에서는 수정되지 않음).

## closure variable (클로저 변수)
A free variable that has been bound in a function closure. See closure for an example.

중첩된 스코프에서 참조되는 자유 변수로, globals나 builtin 네임스페이스에서 런타임에 해결되기보다 외부 스코프에서 정의됩니다. 쓰기 액세스를 허용하기 위해 nonlocal 키워드로 명시적으로 정의하거나, 변수가 읽기만 하는 경우 암시적으로 정의될 수 있습니다.

예를 들어, 다음 코드의 내부 함수에서 x와 print는 모두 자유 변수이지만, x만이 클로저 변수입니다:

```python
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
        print(x)
    return inner
```

codeobject.co_freevars 속성(이름에도 불구하고 모든 참조된 자유 변수를 나열하는 대신 클로저 변수의 이름만 포함) 때문에, 더 일반적인 자유 변수 용어는 때로는 특히 클로저 변수를 지칭하기 위한 의도된 의미일 때도 사용됩니다.

## complex number (복소수)
An extension of the familiar real number system in which all numbers are expressed as a sum of a real part and an imaginary part. Imaginary numbers are real multiples of the imaginary unit (the square root of -1), often written i in mathematics or j in engineering. Python has built-in support for complex numbers, which are written with this latter notation; the imaginary part is written with a j suffix, e.g., 3+1j. To access the complex equivalents of the math module, use cmath. Complex numbers are a fairly advanced mathematical concept; if you don't know you need them, you can safely ignore them.

모든 숫자가 실수부와 허수부의 합으로 표현되는, 친숙한 실수 시스템의 확장입니다. 허수는 종종 수학에서 i로, 공학에서 j로 쓰는 허수 단위(제곱근 -1)의 실수 배수입니다. Python은 복소수를 내장 지원하며, 후자의 표기법으로 작성됩니다. 허수부는 j 접미사로 작성됩니다(예: 3+1j). math 모듈의 복소수 등가물에 접근하려면 cmath를 사용하세요. 복소수 사용은 꽤 고급 수학적 기능입니다. 그것들이 필요하다는 인식이 없다면, 안전하게 무시할 수 있습니다.

## context (컨텍스트)
The term context may refer to any of several related meanings:

- The temporary environment that is controlled by a context manager and seen in a with statement.
- A collection of key-value bindings associated with a specific contextvars.Context object and accessed via ContextVar objects. See context variable.
- A contextvars.Context object. See current context.

이 용어는 어디서 어떻게 사용되느냐에 따라 다른 의미를 가집니다. 일반적인 의미:

- with 문을 통해 컨텍스트 관리자가 설정한 임시 상태나 환경입니다.
- 특정 contextvars.Context 객체와 연관되고 ContextVar 객체를 통해 접근되는 키-값 바인딩의 컬렉션입니다. 컨텍스트 변수도 참조하세요.
- contextvars.Context 객체입니다. 현재 컨텍스트도 참조하세요.

## context management protocol (컨텍스트 관리 프로토콜)
The __enter__() and __exit__() methods that are called by the with statement. See PEP 343.

with 문에 의해 호출되는 __enter__()와 __exit__() 메서드입니다. PEP 343을 참조하세요.

## context manager (컨텍스트 관리자)
An object which controls the environment seen in a with statement by implementing the context management protocol (the __enter__() and __exit__() methods). See PEP 343.

컨텍스트 관리 프로토콜을 구현하고 with 문에서 보이는 환경을 제어하는 객체입니다. PEP 343을 참조하세요.

## context variable (컨텍스트 변수)
A variable whose value depends on the context in which it is accessed. The value is retrieved using a contextvars.ContextVar object. Context variables are primarily used to manage state in concurrent asynchronous tasks.

값이 어떤 컨텍스트가 현재 컨텍스트인지에 따라 달라지는 변수입니다. 값은 contextvars.ContextVar 객체를 통해 접근됩니다. 컨텍스트 변수는 주로 동시 비동기 작업 간에 상태를 격리하는 데 사용됩니다.

## contiguous (연속적인)
A buffer is considered contiguous exactly if it is either C-contiguous or Fortran-contiguous. Zero-dimensional buffers are C and Fortran contiguous. In one-dimensional arrays, the items must be laid out in memory next to each other, starting from the beginning of the memory block. In multidimensional C-contiguous arrays, the last index varies the fastest when visiting items in memory address order. However, in Fortran-contiguous arrays, the first index varies the fastest.

버퍼는 C-연속적이거나 Fortran-연속적인 경우에만 정확히 연속적이라고 간주됩니다. 0차원 버퍼는 C 및 Fortran 연속적입니다. 1차원 배열에서, 항목들은 0부터 시작하여 인덱스가 증가하는 순서로 메모리에 서로 옆에 배치되어야 합니다. 다차원 C-연속 배열에서는 메모리 주소순으로 항목을 방문할 때 마지막 인덱스가 가장 빠르게 변합니다. 그러나 Fortran-연속 배열에서는 첫 번째 인덱스가 가장 빠르게 변합니다.

## coroutine (코루틴)
A coroutine is a generalization of subroutines. Subroutines are entered at one point and exited at another point. Coroutines can be entered, exited, and resumed at many different points. They can be implemented with async def statements. See also PEP 492.

코루틴은 서브루틴의 더 일반화된 형태입니다. 서브루틴은 한 지점에서 들어가 다른 지점에서 나옵니다. 코루틴은 여러 다른 지점에서 들어가고, 나가고, 재개될 수 있습니다. 이는 async def 문으로 구현할 수 있습니다. PEP 492도 참조하세요.

## coroutine function (코루틴 함수)
A function that returns a coroutine object. A coroutine function may be defined with async def statements, and may contain await, async for, and async with keywords. Introduced by PEP 492.

코루틴 객체를 반환하는 함수입니다. 코루틴 함수는 async def 문으로 정의될 수 있으며, await, async for, async with 키워드를 포함할 수 있습니다. 이는 PEP 492에서 도입되었습니다.

## CPython
The canonical implementation of the Python programming language, as distributed on python.org. The term "CPython" is used when necessary to distinguish this implementation from others such as Jython or IronPython.

python.org에서 배포되는 Python 프로그래밍 언어의 표준 구현입니다. "CPython"이라는 용어는 이 구현을 Jython이나 IronPython과 같은 다른 구현과 구별해야 할 때 사용됩니다.

## current context (현재 컨텍스트)
The context (contextvars.Context object) that is used when a ContextVar object is accessed (get or set). Each thread has its own current context. Frameworks that run asynchronous tasks (such as asyncio) will associate each task with a context, and that context will be the current context when the task is running or resumes.

ContextVar 객체가 현재 컨텍스트 변수의 값에 접근(가져오거나 설정)하기 위해 사용하는 컨텍스트(contextvars.Context 객체)입니다. 각 스레드는 자체 현재 컨텍스트를 가집니다. 비동기 작업을 실행하기 위한 프레임워크(asyncio 참조)는 각 작업을 컨텍스트와 연결하며, 이 컨텍스트는 작업이 시작되거나 실행을 재개할 때마다 현재 컨텍스트가 됩니다.

## decorator (데코레이터)
A function returning another function, usually applied as a function transformation using the @wrapper syntax. Common examples for decorators are classmethod() and staticmethod().

The decorator syntax is merely syntactic sugar, the following two function definitions are semantically equivalent:

```python
def f(arg):
    ...
f = staticmethod(f)

@staticmethod
def f(arg):
    ...
```

The same concept exists for classes, but is less commonly used there. See the function definitions and class definitions sections for more about decorators.

보통 @wrapper 구문을 사용하여 함수 변환으로 적용되는, 다른 함수를 반환하는 함수입니다. 데코레이터의 일반적인 예로는 classmethod()와 staticmethod()가 있습니다.

데코레이터 구문은 단순한 문법적 설탕입니다. 다음 두 함수 정의는 의미적으로 동일합니다:

```python
def f(arg):
    ...
f = staticmethod(f)

@staticmethod
def f(arg):
    ...
```

같은 개념이 클래스에도 존재하지만, 그곳에서는 덜 일반적으로 사용됩니다. 데코레이터에 대한 자세한 내용은 함수 정의와 클래스 정의 문서를 참조하세요.

## descriptor (설명자)
Any object which defines the methods __get__(), __set__(), or __delete__(). When a class attribute is a descriptor, its special binding behavior is triggered upon attribute lookup. Normally, using a.b to get, set, or delete an attribute looks up the object b in the class dictionary for a, but if b is a descriptor, the respective descriptor method gets called. Understanding descriptors is a key to a deep understanding of Python because they are the basis for many features including functions, methods, properties, class methods, static methods, and references to super classes.

For more information about descriptor methods, see Implementing Descriptors or the Descriptor How To Guide.

__get__(), __set__() 또는 __delete__() 메서드를 정의하는 모든 객체입니다. 클래스 속성이 설명자일 때, 그 특별한 바인딩 동작은 속성 조회 시 트리거됩니다. 일반적으로, a.b를 사용하여 속성을 가져오거나, 설정하거나, 삭제하는 것은 a의 클래스 사전에서 b라는 객체를 찾지만, b가 설명자인 경우 해당 설명자 메서드가 호출됩니다. 설명자를 이해하는 것은 Python을 깊이 이해하는 데 중요합니다. 왜냐하면 그것들은 함수, 메서드, 프로퍼티, 클래스 메서드, 정적 메서드, 수퍼 클래스에 대한 참조와 같은 많은 기능의 기반이기 때문입니다.

설명자 메서드에 대한 자세한 정보는 설명자 구현하기 또는 설명자 방법 가이드를 참조하세요.

## dictionary (딕셔너리)
An associative array, where arbitrary keys are mapped to values. Keys can be any object with __hash__() and __eq__() methods. Called a hash in Perl.

임의의 키가 값에 매핑되는 연관 배열입니다. 키는 __hash__()와 __eq__() 메서드를 가진 어떤 객체도 될 수 있습니다. Perl에서는 해시라고 불립니다.

## dictionary comprehension (딕셔너리 컴프리헨션)
A compact way to process all or part of the elements in an iterable and return a dictionary with the results. results = {n: n ** 2 for n in range(10)} generates a dictionary that maps the keys n to the values n ** 2. See displays for lists, sets and dictionaries.

반복 가능한 객체의 요소 전체 또는 일부를 처리하고 결과를 딕셔너리로 반환하는 간결한 방법입니다. results = {n: n ** 2 for n in range(10)}은 키 n이 값 n ** 2에 매핑된 딕셔너리를 생성합니다. 리스트, 세트, 딕셔너리에 대한 디스플레이를 참조하세요.

## dictionary view (딕셔너리 뷰)
The objects returned from dict.keys(), dict.values(), and dict.items() are called dictionary views. They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes. To force the dictionary view to become a full list use list(dictview). See dictionary view objects.

dict.keys(), dict.values(), dict.items()에서 반환되는 객체를 딕셔너리 뷰라고 합니다. 이들은 딕셔너리 항목의 동적 뷰를 제공하므로, 딕셔너리가 변경되면 뷰가 이러한 변경을 반영합니다. 딕셔너리 뷰를 전체 리스트로 강제하려면 list(dictview)를 사용하세요. 딕셔너리 뷰 객체를 참조하세요.

## docstring (문서 문자열)
A string literal which appears as the first expression in a class, function or module. While ignored when the suite is executed, it is recognized by the compiler and put into the __doc__ attribute of the enclosing class, function or module. Since it is available via introspection, it is the canonical place for documentation of the object.

클래스, 함수 또는 모듈의 첫 번째 표현식으로 나타나는, 문자열 리터럴입니다. 스위트가 실행될 때 무시되지만, 컴파일러에 의해 인식되어 둘러싸는 클래스, 함수 또는 모듈의 __doc__ 속성에 저장됩니다. 내성(introspection)을 통해 사용할 수 있기 때문에, 객체의 문서화를 위한 표준적인 위치입니다.

## duck-typing (덕 타이핑)
A programming style which does not look at an object's type to determine if it has the right interface; instead, the method or attribute is simply called or used ("If it looks like a duck and quacks like a duck, it must be a duck."). By emphasizing interfaces rather than specific types, well-designed code improves its flexibility by allowing polymorphic substitutions. Duck-typing avoids tests using type() or isinstance(). (However, duck-typing can be complemented with abstract base classes.) Instead, it typically uses hasattr() tests or EAFP programming.

올바른 인터페이스를 가졌는지 확인하기 위해 객체의 타입을 살펴보지 않는 프로그래밍 스타일입니다. 대신, 메서드나 속성이 단순히 호출되거나 사용됩니다("오리처럼 생기고 꽥꽥 거리면 오리임에 틀림없다"). 특정 타입보다는 인터페이스를 강조함으로써, 잘 설계된 코드는 다형성 대체를 허용하여 유연성을 향상시킵니다. 덕 타이핑은 type()이나 isinstance()를 사용한 테스트를 피합니다(그러나 덕 타이핑은 추상 기본 클래스로 보완될 수 있습니다). 대신, 일반적으로 hasattr() 테스트나 EAFP 프로그래밍을 사용합니다.

## EAFP
Easier to ask for forgiveness than permission. This common Python coding style assumes the existence of valid keys or attributes and catches exceptions if the assumption proves false. This clean and fast style is characterized by many try and except statements. The technique contrasts with the LBYL style common to many other languages such as C.

용서를 구하는 것이 허락을 구하는 것보다 쉽다(Easier to ask for forgiveness than permission). 이 일반적인 Python 코딩 스타일은 유효한 키나 속성의 존재를 가정하고, 가정이 거짓으로 판명되면 예외를 잡습니다. 이 깨끗하고 빠른 스타일은 많은 try와 except 문의 존재로 특징지어집니다. 이 기법은 C와 같은 많은 다른 언어에서 일반적인 LBYL 스타일과 대조됩니다.

## expression (표현식)
A piece of syntax which can be evaluated to some value. In other words, an expression is an accumulation of expression elements like literals, names, attribute access, operators or function calls which all return a value. In contrast to many other languages, not all language constructs are expressions. There are also statement which cannot be used as expressions (such as while). Assignments are also statements, not expressions.

어떤 값으로 평가될 수 있는 구문의 일부입니다. 다시 말해, 표현식은 리터럴, 이름, 속성 접근, 연산자 또는 함수 호출과 같이 모두 값을 반환하는 표현 요소의 축적입니다. 많은 다른 언어와 달리, 모든 언어 구조가 표현식인 것은 아닙니다. 표현식으로 사용할 수 없는 문장도 있습니다(예: while). 할당도 표현식이 아닌 문장입니다.

## extension module (확장 모듈)
A module written in C or C++, using Python's C API to interact with the core and with user code.

코어 및 사용자 코드와 상호 작용하기 위해 Python의 C API를 사용하여 C나 C++로 작성된 모듈입니다.

## f-string (f-문자열)
String literals prefixed with 'f' or 'F' are commonly called "f-strings" which is short for formatted string literals. See also PEP 498.

'f'나 'F'로 접두사가 붙은 문자열 리터럴은 일반적으로 "f-문자열"이라고 불리며, 이는 형식화된 문자열 리터럴의 약자입니다. PEP 498도 참조하세요.

## file object (파일 객체)
An object exposing a file-oriented API (with methods such as read() or write()) to an underlying resource. Depending on the way it was created, a file object can mediate access to a real on-disk file or to another type of storage or communication device (for example standard input/output, in-memory buffers, sockets, pipes, etc.). File objects are also called file-like objects or streams.

Actually, three kinds of file objects are supported: raw binary files, buffered binary files, and text files. Their interfaces are defined in the io module. The standard way to open a file is with the open() function.

기본 리소스에 대한 파일 지향적 API(read()나 write()와 같은 메서드)를 노출하는 객체입니다. 생성 방식에 따라, 파일 객체는 실제 디스크 상의 파일에 대한 액세스를 중재하거나 다른 종류의 저장소나 통신 장치(예: 표준 입력/출력, 메모리 내 버퍼, 소켓, 파이프 등)에 대한 액세스를 중재할 수 있습니다. 파일 객체는 파일 유사 객체나 스트림이라고도 불립니다.

실제로 세 가지 범주의 파일 객체가 있습니다: 원시 바이너리 파일, 버퍼링된 바이너리 파일, 텍스트 파일. 이들의 인터페이스는 io 모듈에 정의되어 있습니다. 파일 객체를 생성하는 표준적인 방법은 open() 함수를 사용하는 것입니다.

## file-like object (파일 유사 객체)
A synonym for file object.

파일 객체의 동의어입니다.

## filesystem encoding and error handler (파일시스템 인코딩 및 오류 처리기)
The encoding and error handler used by Python to decode bytes from the operating system and encode Unicode to the operating system.

The filesystem encoding must guarantee to successfully decode all bytes below 128. If the filesystem encoding fails to provide this guarantee, API functions may raise UnicodeError.

The sys.getfilesystemencoding() and sys.getfilesystemencodeerrors() functions can be used to get the filesystem encoding and error handler.

The filesystem encoding and error handler are configured at Python startup by the PyConfig_Read() function: see the filesystem_encoding and filesystem_errors members of PyConfig.

See also locale encoding.

Python이 운영 체제에서 바이트를 디코딩하고 Unicode를 운영 체제로 인코딩하는 데 사용하는 인코딩과 오류 처리기입니다.

파일시스템 인코딩은 128 미만의 모든 바이트를 성공적으로 디코딩할 수 있도록 보장해야 합니다. 파일 시스템 인코딩이 이 보장을 제공하지 못하면, API 함수는 UnicodeError를 발생시킬 수 있습니다.

sys.getfilesystemencoding()과 sys.getfilesystemencodeerrors() 함수는 파일시스템 인코딩과 오류 처리기를 얻는 데 사용될 수 있습니다.

파일시스템 인코딩과 오류 처리기는 PyConfig_Read() 함수에 의해 Python 시작 시 구성됩니다: PyConfig의 filesystem_encoding과 filesystem_errors 멤버를 참조하세요.

로케일 인코딩도 참조하세요.

## finder (파인더)
An object that tries to find the loader for a module that is being imported.

There are two types of finders: meta path finders that are on sys.meta_path and path entry finders that are on sys.path_hooks.

See also the finder and loader and importlib.

가져오고 있는 모듈의 로더를 찾으려고 시도하는 객체입니다.

두 가지 유형의 파인더가 있습니다: sys.meta_path와 함께 사용하는 메타 경로 파인더와 sys.path_hooks와 함께 사용하는 경로 항목 파인더입니다.

자세한 내용은 파인더와 로더 및 importlib을 참조하세요.

## floor division (내림 나눗셈)
Mathematical division that rounds down to the nearest integer. The floor division operator is //. For example, the expression 11 // 4 evaluates to 2 in contrast to the 2.75 returned by true division. (-11) // 4 is -3 because that is -2.75 rounded down. See PEP 238.

가장 가까운 정수로 내림하는 수학적 나눗셈입니다. 내림 나눗셈 연산자는 //입니다. 예를 들어, 표현식 11 // 4는 부동 소수점 진짜 나눗셈으로 반환되는 2.75와 대조적으로 2로 평가됩니다. (-11) // 4는 -2.75를 내림하여 -3이 됩니다. PEP 238을 참조하세요.

## function (함수)
A series of statements which returns some value to a caller. It can also be passed zero or more arguments which may be used in the execution of the body. See also parameter, method, and the Function definitions section.

일련의 명령문을 수행하는 코드 블록으로, 이름이 지정되고 매개변수를 받을 수 있으며 값을 반환할 수도 있습니다. 함수 정의는 def 키워드로 시작합니다.

호출자에게 어떤 값을 반환하는 일련의 명령문입니다. 본문 실행에 사용될 수 있는 0개 이상의 인수를 전달받을 수도 있습니다. 매개변수, 메서드 및 함수 정의 섹션도 참조하세요.

## function annotation (함수 주석)
An annotation of a function parameter or return value.

Function annotations are usually used for type hints: for example, this function is expected to take two int arguments and is also expected to have an int return value:

```python
def sum_two_numbers(a: int, b: int) -> int:
   return a + b
```

The function annotation syntax is explained in section Function definitions.

See variable annotation and PEP 484 which describe this functionality. Also see Annotations Best Practices for best practices on working with annotations.

함수 매개변수 또는 반환 값에 대한 주석입니다.

함수 주석은 일반적으로 타입 힌트에 사용됩니다: 예를 들어, 이 함수는 두 개의 int 인수를 받고 int 반환 값을 가질 것으로 예상됩니다:

```python
def sum_two_numbers(a: int, b: int) -> int:
   return a + b
```

함수 주석 구문은 함수 정의 섹션에 설명되어 있습니다.

이 기능을 설명하는 변수 주석과 PEP 484를 참조하세요. 또한 주석 작업에 대한 모범 사례는 주석 모범 사례를 참조하세요.

## free threading (자유 스레딩)
A threading model where multiple threads can run Python bytecode simultaneously within the same interpreter. This is in contrast to the global interpreter lock which allows only one thread to execute Python bytecode at a time. See PEP 703.

여러 스레드가 동일한 인터프리터 내에서 Python 바이트코드를 동시에 실행할 수 있는 스레딩 모델입니다. 이는 한 번에 하나의 스레드만 Python 바이트코드를 실행할 수 있는 전역 인터프리터 락(GIL)과 대조됩니다. PEP 703을 참조하세요.

## free variable (자유 변수)
Formally, as defined in the language execution model, a free variable is any variable used in a namespace which is not a local variable in that namespace. See closure variable for an example. Pragmatically, due to the name of the codeobject.co_freevars attribute, the term is also sometimes used as a synonym for closure variable.

공식적으로, 언어 실행 모델에서 정의된 대로, 자유 변수는 해당 네임스페이스의 로컬 변수가 아닌 네임스페이스에서 사용되는 모든 변수입니다. 예시는 클로저 변수를 참조하세요. 실용적으로, codeobject.co_freevars 속성의 이름 때문에, 이 용어는 때로는 클로저 변수의 동의어로도 사용됩니다.

## __future__ (미래)
A future statement, from __future__ import <feature>, directs the compiler to compile the current module using syntax or semantics that will become standard in a future release of Python. The __future__ module documents the possible values of feature. By importing this module and evaluating its variables, you can see when a new feature was first added to the language and when it will (or did) become the default:

```python
>>> import __future__
>>> __future__.division
_Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)
```

미래 문, from __future__ import <feature>는 컴파일러가 Python의 향후 릴리스에서 표준이 될 구문이나 의미론을 사용하여 현재 모듈을 컴파일하도록 지시합니다. __future__ 모듈은 feature의 가능한 값을 문서화합니다. 이 모듈을 가져와 변수를 평가함으로써, 새 기능이 언어에 처음 추가된 시기와 기본값이 될(또는 된) 시기를 볼 수 있습니다:

```python
>>> import __future__
>>> __future__.division
_Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)
```

## garbage collection (가비지 컬렉션)
The process of freeing memory when it is not used anymore. Python performs garbage collection via reference counting and a cyclic garbage collector that is able to detect and break reference cycles. The garbage collector can be controlled using the gc module.

더 이상 사용되지 않는 메모리를 해제하는 과정입니다. Python은 참조 카운팅과 참조 순환을 감지하고 깨뜨릴 수 있는 순환 가비지 컬렉터를 통해 가비지 컬렉션을 수행합니다. 가비지 컬렉터는 gc 모듈을 사용하여 제어할 수 있습니다.

## generator (제너레이터)
A function which returns a generator iterator. It looks like a normal function except that it contains yield expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function.

Usually refers to a generator function, but may refer to a generator iterator in some contexts. In cases where the intended meaning isn't clear, using the full terms avoids ambiguity.

제너레이터 반복자를 반환하는 함수입니다. for 루프에서 사용 가능한 일련의 값을 생성하거나 next() 함수로 한 번에 하나씩 검색할 수 있는 yield 표현식을 포함한다는 점을 제외하면 일반 함수와 비슷합니다.

일반적으로 제너레이터 함수를 지칭하지만, 일부 맥락에서는 제너레이터 반복자를 지칭할 수도 있습니다. 의도한 의미가 명확하지 않은 경우, 전체 용어를 사용하면 모호성을 피할 수 있습니다.

## generator iterator (제너레이터 반복자)
An object created by a generator function.

Each yield temporarily suspends processing, remembering the execution state (including local variables and pending try-statements). When the generator iterator resumes, it picks up where it left off (in contrast to functions which start fresh on every invocation).

제너레이터 함수에 의해 생성된 객체입니다.

각 yield는 실행 상태(지역 변수 및 보류 중인 try 문 포함)를 기억하면서 처리를 일시적으로 중단합니다. 제너레이터 반복자가 재개되면, 중단된 지점부터 다시 시작합니다(매 호출마다 새로 시작하는 함수와 대조적).

## generator expression (제너레이터 표현식)
An expression that returns an iterator. It looks like a normal expression followed by a for clause defining a loop variable, range, and an optional if clause. The combined expression generates values for an enclosing function:

```python
>>> sum(i*i for i in range(10))         # sum of squares 0, 1, 4, ... 81
285
```

반복자를 반환하는 표현식입니다. 루프 변수, 범위 및 선택적 if 절을 정의하는 for 절이 뒤따르는 일반 표현식처럼 보입니다. 결합된 표현식은 둘러싸는 함수에 대한 값을 생성합니다:

```python
>>> sum(i*i for i in range(10))         # 제곱의 합 0, 1, 4, ... 81
285
```

## generic function (제네릭 함수)
A function composed of multiple functions implementing the same operation for different types. Which implementation should be used during a call is determined by the dispatch algorithm.

See also the single dispatch glossary entry, the functools.singledispatch() decorator, and PEP 443.

다양한 타입에 대해 동일한 연산을 구현하는 여러 함수로 구성된 함수입니다. 호출 중에 어떤 구현이 사용되어야 하는지는 디스패치 알고리즘에 의해 결정됩니다.

단일 디스패치 용어집 항목, functools.singledispatch() 데코레이터 및 PEP 443도 참조하세요.

## generic type (제네릭 타입)
A type that can be parameterized; typically a container class such as list or dict. Used for type hints and annotations.

For more details, see generic alias types, PEP 483, PEP 484, PEP 585, and the typing module.

매개변수화될 수 있는 타입; 일반적으로 list나 dict와 같은 컨테이너 클래스입니다. 타입 힌트 및 주석에 사용됩니다.

자세한 내용은 제네릭 별칭 타입, PEP 483, PEP 484, PEP 585 및 typing 모듈을 참조하세요.

## GIL (글로벌 인터프리터 락)
See global interpreter lock.

global interpreter lock을 참조하세요.

## global interpreter lock (글로벌 인터프리터 락)
The mechanism used by the CPython interpreter to assure that only one thread executes Python bytecode at a time. This simplifies the CPython implementation by making the object model (including critical built-in types such as dict) implicitly safe against concurrent access. Locking the entire interpreter makes it easier for the interpreter to be multi-threaded, at the expense of much of the parallelism afforded by multi-processor machines.

However, some extension modules, either standard or third-party, are designed so as to release the GIL when doing computationally intensive tasks such as compression or hashing. Also, the GIL is always released when doing I/O.

As of Python 3.13, the GIL can be disabled using the --disable-gil build configuration. After building Python with this option, code must be run with -X gil=0 or after setting the PYTHON_GIL=0 environment variable. This feature enables improved performance for multi-threaded applications and makes it easier to use multi-core CPUs efficiently. For more details, see PEP 703.

CPython 인터프리터가 한 번에 하나의 스레드만 Python 바이트코드를 실행하도록 보장하는 데 사용하는 메커니즘입니다. 이는 객체 모델(dict와 같은 중요한 내장 타입 포함)을 동시 접근으로부터 암시적으로 안전하게 함으로써 CPython 구현을 단순화합니다. 전체 인터프리터를 잠그면 인터프리터가 다중 스레드화되기 쉽지만, 다중 프로세서 기계가 제공하는 병렬 처리의 많은 부분이 희생됩니다.

그러나 일부 확장 모듈(표준 또는 타사)은 압축이나 해싱과 같은 계산 집약적인 작업을 수행할 때 GIL을 해제하도록 설계되었습니다. 또한, I/O를 수행할 때는 항상 GIL이 해제됩니다.

Python 3.13부터, GIL은 --disable-gil 빌드 구성을 사용하여 비활성화할 수 있습니다. 이 옵션으로 Python을 빌드한 후, 코드는 -X gil=0으로 실행하거나 PYTHON_GIL=0 환경 변수를 설정한 후 실행해야 합니다. 이 기능은 다중 스레드 응용 프로그램의 성능을 향상시키고 다중 코어 CPU를 효율적으로 사용하기 쉽게 합니다. 자세한 내용은 PEP 703을 참조하세요.

## hash-based pyc (해시 기반 pyc)
A bytecode cache file that uses the hash rather than the last-modified time of the corresponding source file to determine its validity. See Cached bytecode invalidation.

해당 소스 파일의 마지막 수정 시간 대신 해시를 사용하여 유효성을 결정하는 바이트코드 캐시 파일입니다. 캐시된 바이트코드 무효화를 참조하세요.

## hashable (해시 가능)
An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__() method), and can be compared to other objects (it needs an __eq__() method). Hashable objects which compare equal must have the same hash value.

Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally.

Most of Python's immutable built-in objects are hashable; mutable containers (such as lists or dictionaries) are not; immutable containers (such as tuples and frozensets) are only hashable if their elements are hashable. Objects which are instances of user-defined classes are hashable by default. They all compare unequal (except with themselves), and their hash value is derived from their id().

객체가 수명 동안 절대 변하지 않는 해시 값을 가지고 있고(__hash__() 메서드가 필요), 다른 객체와 비교할 수 있다면(__eq__() 메서드가 필요) 해시 가능합니다. 동등하게 비교되는 해시 가능 객체는 동일한 해시 값을 가져야 합니다.

해시 가능성은 객체를 딕셔너리 키와 집합 멤버로 사용할 수 있게 합니다. 이러한 데이터 구조는 내부적으로 해시 값을 사용하기 때문입니다.

Python의 대부분의 불변 내장 객체는 해시 가능합니다; 가변 컨테이너(리스트나 딕셔너리 같은)는 그렇지 않습니다; 불변 컨테이너(튜플과 frozenset 같은)는 요소가 해시 가능한 경우에만 해시 가능합니다. 사용자 정의 클래스의 인스턴스인 객체는 기본적으로 해시 가능합니다. 이들은 모두 (자기 자신을 제외하고) 불평등하게 비교되며, 해시 값은 id()에서 파생됩니다.

## IDLE (IDLE)
An Integrated Development and Learning Environment for Python. IDLE — Python editor and shell is a basic editor and interpreter environment which ships with the standard distribution of Python.

Python을 위한 통합 개발 및 학습 환경입니다. IDLE — Python 편집기 및 셸은 Python의 표준 배포판과 함께 제공되는 기본 편집기 및 인터프리터 환경입니다.

## immortal (불멸)
Immortal objects are a CPython implementation detail introduced in PEP 683.

If an object is immortal, its reference count is never modified, and therefore it is never deallocated while the interpreter is running. For example, True and None are immortal in CPython.

불멸 객체는 PEP 683에서 소개된 CPython 구현 세부 사항입니다.

객체가 불멸이면 참조 개수가 절대 수정되지 않으므로 인터프리터가 실행되는 동안 절대 할당 해제되지 않습니다. 예를 들어, CPython에서 True와 None은 불멸입니다.

## immutable (불변)
An object with a fixed value. Immutable objects include numbers, strings and tuples. Such an object cannot be altered. A new object has to be created if a different value has to be stored. They play an important role in places where a constant hash value is needed, for example as a key in a dictionary.

고정된 값을 가진 객체입니다. 불변 객체에는 숫자, 문자열 및 튜플이 포함됩니다. 이러한 객체는 변경할 수 없습니다. 다른 값을 저장해야 한다면 새 객체를 만들어야 합니다. 불변 객체는 상수 해시 값이 필요한 곳, 예를 들어 딕셔너리의 키로 중요한 역할을 합니다.

## import path (가져오기 경로)
A list of locations (or path entries) that are searched by the path based finder for modules to import. During import, this list of locations usually comes from sys.path, but for subpackages it may also come from the parent package's __path__ attribute.

모듈을 가져오기 위해 경로 기반 파인더가 검색하는 위치(또는 경로 항목)의 목록입니다. 가져오기 중에 이 위치 목록은 일반적으로 sys.path에서 나오지만, 서브패키지의 경우 부모 패키지의 __path__ 속성에서 나올 수도 있습니다.

## importing (가져오기)
The process by which Python code in one module is made available to Python code in another module.

다른 모듈의 Python 코드에서 한 모듈의 Python 코드를 사용할 수 있게 하는 과정입니다.

## importer (가져오기 도구)
An object that both finds and loads a module; both a finder and loader object.

모듈을 찾고 로드하는 객체; 파인더와 로더 객체의 기능을 모두 가집니다.

## interactive (대화형)
Python has an interactive interpreter which means you can enter statements and expressions at the interpreter prompt, immediately execute them and see their results. Just launch python with no arguments (possibly by selecting it from your computer's main menu). It is a very powerful way to test out new ideas or inspect modules and packages (remember help(x)). For more on interactive mode, see Interactive Mode.

Python은 대화형 인터프리터를 가지고 있어서 인터프리터 프롬프트에서 문장과 표현식을 입력하고 즉시 실행하여 결과를 볼 수 있습니다. 인수 없이 python을 실행하기만 하면 됩니다(컴퓨터의 메인 메뉴에서 선택하는 방식으로). 이는 새로운 아이디어를 테스트하거나 모듈 및 패키지를 검사하는 매우 강력한 방법입니다(help(x)를 기억하세요). 대화형 모드에 대한 자세한 내용은 대화형 모드를 참조하세요.

## interpreted (인터프리트된)
Python is an interpreted language, as opposed to a compiled one, though the distinction can be blurry because of the presence of the bytecode compiler. This means that source files can be run directly without explicitly creating an executable which is then run. Interpreted languages typically have a shorter development/debug cycle than compiled ones, though their programs generally also run more slowly. See also interactive.

Python은 컴파일된 언어가 아닌 해석(인터프리트)되는 언어입니다. 다만, 바이트코드 컴파일러의 존재로 인해 이 구분이 불분명할 수 있습니다. 이는 실행 파일을 명시적으로 생성하여 실행하지 않고도 소스 파일을 직접 실행할 수 있음을 의미합니다. 해석형 언어는 일반적으로 컴파일 언어보다 개발/디버그 주기가 짧지만, 프로그램 실행은 대체로 더 느립니다. 대화형(interactive)도 참조하세요.

## interpreter shutdown (인터프리터 종료)
When asked to shut down, the Python interpreter enters a special phase where it gradually releases all allocated resources, such as modules and various critical internal structures. It also makes several calls to the garbage collector. This can trigger the execution of code in user-defined destructors or weakref callbacks. Code executed during the shutdown phase can encounter various exceptions as the resources it relies on may not function anymore (common examples are library modules or the warnings machinery).

The main reason for interpreter shutdown is that the __main__ module or the script being run has finished executing.

종료 요청을 받으면 Python 인터프리터는 모듈 및 다양한 중요 내부 구조와 같은 할당된 모든 리소스를 점진적으로 해제하는 특별한 단계에 들어갑니다. 또한 가비지 컬렉터에 여러 번 호출합니다. 이로 인해 사용자 정의 소멸자나 약한 참조 콜백에서 코드 실행이 트리거될 수 있습니다. 종료 단계에서 실행되는 코드는 의존하는 리소스가 더 이상 작동하지 않을 수 있으므로 다양한 예외를 만날 수 있습니다(일반적인 예로는 라이브러리 모듈이나 경고 메커니즘이 있습니다).

인터프리터 종료의 주된 이유는 __main__ 모듈이나 실행 중인 스크립트의 실행이 완료되었기 때문입니다.

## iterable (반복 가능)
An object capable of returning its members one at a time. Examples of iterables include all sequence types (such as list, str, and tuple) and some non-sequence types like dict, file objects, and objects of any classes you define with an __iter__() method or with a __getitem__() method that implements sequence semantics.

Iterables can be used in a for loop and in many other places where a sequence is needed (zip(), map(), …). When an iterable object is passed as an argument to the built-in function iter(), it returns an iterator for the object. This iterator is good for one pass over the set of values. When using iterables, it is usually not necessary to call iter() or deal with iterator objects yourself. The for statement does that automatically for you, creating a temporary unnamed variable to hold the iterator for the duration of the loop. See also iterator, sequence, and generator.

멤버를 한 번에 하나씩 반환할 수 있는 객체입니다. 반복 가능한 객체의 예로는 모든 시퀀스 유형(list, str, tuple 등)과 dict, 파일 객체, __iter__() 메서드나 시퀀스 의미론을 구현하는 __getitem__() 메서드로 정의한 클래스의 객체와 같은 비시퀀스 유형이 있습니다.

반복 가능한 객체는 for 루프와 시퀀스가 필요한 다른 많은 곳(zip(), map() 등)에서 사용할 수 있습니다. 반복 가능한 객체가 내장 함수 iter()에 인수로 전달되면 해당 객체에 대한 반복자를 반환합니다. 이 반복자는 값 집합을 한 번 순회하는 데 적합합니다. 반복 가능한 객체를 사용할 때는 일반적으로 iter()를 호출하거나 직접 반복자 객체를 다룰 필요가 없습니다. for 문이 자동으로 처리하여 루프 동안 반복자를 보관할 임시 이름 없는 변수를 만듭니다. 반복자(iterator), 시퀀스(sequence), 제너레이터(generator)도 참조하세요.

## iterator (반복자)
An object representing a stream of data. Repeated calls to the iterator's __next__() method (or passing it to the built-in function next()) return successive items in the stream. When no more data are available a StopIteration exception is raised instead. At this point, the iterator object is exhausted and any further calls to its __next__() method just raise StopIteration again. Iterators are required to have an __iter__() method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted. One notable exception is code which attempts multiple iteration passes. A container object (such as a list) produces a fresh new iterator each time you pass it to the iter() function or use it in a for loop. Attempting this with an iterator will just return the same exhausted iterator object used in the previous iteration pass, making it appear like an empty container.

More information can be found in Iterator Types.

CPython implementation detail: CPython does not consistently apply the requirement that an iterator define __iter__(). And also please note that the free-threading CPython does not guarantee the thread-safety of iterator operations.

데이터 스트림을 나타내는 객체입니다. 반복자의 __next__() 메서드를 반복 호출하거나(또는 내장 함수 next()에 전달) 스트림의 연속 항목을 반환합니다. 더 이상 사용할 수 있는 데이터가 없으면 대신 StopIteration 예외가 발생합니다. 이 시점에서 반복자 객체는 소진되고 __next__() 메서드에 대한 추가 호출은 다시 StopIteration을 발생시킵니다. 반복자는 반복자 객체 자체를 반환하는 __iter__() 메서드를 가져야 하므로 모든 반복자는 또한 반복 가능하며 다른 반복 가능한 객체가 허용되는 대부분의 장소에서 사용될 수 있습니다. 한 가지 주목할 만한 예외는 여러 반복 패스를 시도하는 코드입니다. 컨테이너 객체(예: 리스트)는 iter() 함수에 전달하거나 for 루프에서 사용할 때마다 새로운 반복자를 생성합니다. 반복자로 이를 시도하면 이전 반복 패스에서 사용된 동일한 소진된 반복자 객체를 반환하여 빈 컨테이너처럼 보이게 됩니다.

자세한 내용은 반복자 타입에서 확인할 수 있습니다.

CPython 구현 세부 사항: CPython은 반복자가 __iter__()를 정의해야 한다는 요구 사항을 일관되게 적용하지 않습니다. 또한 자유 스레딩 CPython은 반복자 작업의 스레드 안전성을 보장하지 않습니다.

## key function (키 함수)
A key function or collation function is a callable that returns a value used for sorting or ordering. For example, locale.strxfrm() is used to produce a sort key that is aware of locale specific sort conventions.

A number of tools in Python accept key functions to control how elements are ordered or grouped. They include min(), max(), sorted(), list.sort(), heapq.merge(), heapq.nsmallest(), heapq.nlargest(), and itertools.groupby().

There are several ways to create a key function. For example. the str.lower() method can serve as a key function for case insensitive sorts. Alternatively, a key function can be built from a lambda expression such as lambda r: (r[0], r[2]). Also, operator.attrgetter(), operator.itemgetter(), and operator.methodcaller() are three key function constructors. See the Sorting HOW TO for examples of how to create and use key functions.

키 함수 또는 대조 함수는 정렬이나 순서 지정에 사용되는 값을 반환하는 호출 가능한 객체입니다. 예를 들어, locale.strxfrm()은 로캘별 정렬 규칙을 인식하는 정렬 키를 생성하는 데 사용됩니다.

Python의 여러 도구는 요소가 정렬되거나 그룹화되는 방식을 제어하기 위해 키 함수를 허용합니다. 여기에는 min(), max(), sorted(), list.sort(), heapq.merge(), heapq.nsmallest(), heapq.nlargest(), itertools.groupby() 등이 포함됩니다.

키 함수를 만드는 방법은 여러 가지가 있습니다. 예를 들어, str.lower() 메서드는 대소문자를 구분하지 않는 정렬을 위한 키 함수로 사용될 수 있습니다. 또는 lambda r: (r[0], r[2])와 같은 람다 표현식에서 키 함수를 만들 수 있습니다. 또한 operator.attrgetter(), operator.itemgetter(), operator.methodcaller()는 세 가지 키 함수 생성자입니다. 키 함수를 만들고 사용하는 방법의 예는 정렬 방법을 참조하세요.

## keyword argument (키워드 인자)
See argument.

argument를 참조하세요.

## lambda (람다)
An anonymous inline function consisting of a single expression which is evaluated when the function is called. The syntax to create a lambda function is lambda [parameters]: expression

함수가 호출될 때 평가되는 단일 표현식으로 구성된 익명 인라인 함수입니다. 람다 함수를 만드는 구문은 lambda [parameters]: expression입니다.

## LBYL (뛰기 전에 살펴보기)
Look before you leap. This coding style explicitly tests for pre-conditions before making calls or lookups. This style contrasts with the EAFP approach and is characterized by the presence of many if statements.

In a multi-threaded environment, the LBYL approach can risk introducing a race condition between "the looking" and "the leaping". For example, the code, if key in mapping: return mapping[key] can fail if another thread removes key from mapping after the test, but before the lookup. This issue can be solved with locks or by using the EAFP approach.

뛰기 전에 살펴보기(Look before you leap). 이 코딩 스타일은 호출이나 조회를 하기 전에 사전 조건을 명시적으로 테스트합니다. 이 스타일은 EAFP 접근 방식과 대조되며 많은 if 문의 존재로 특징지어집니다.

다중 스레드 환경에서 LBYL 접근 방식은 "살펴보기"와 "뛰기" 사이에 경쟁 조건을 도입할 위험이 있습니다. 예를 들어, 코드 if key in mapping: return mapping[key]는 테스트 후 조회 전에 다른 스레드가 mapping에서 key를 제거하면 실패할 수 있습니다. 이 문제는 잠금을 사용하거나 EAFP 접근 방식을 사용하여 해결할 수 있습니다.

## list (리스트)
A built-in Python sequence. Despite its name it is more akin to an array in other languages than to a linked list since access to elements is O(1).

내장 Python 시퀀스입니다. 이름에도 불구하고 요소에 대한 접근이 O(1)이므로 연결 리스트보다는 다른 언어의 배열에 더 가깝습니다.

## list comprehension (리스트 컴프리헨션)
A compact way to process all or part of the elements in a sequence and return a list with the results. result = ['{:#04x}'.format(x) for x in range(256) if x % 2 == 0] generates a list of strings containing even hex numbers (0x..) in the range from 0 to 255. The if clause is optional. If omitted, all elements in range(256) are processed.

시퀀스의 모든 요소 또는 일부를 처리하고 결과를 포함하는 리스트를 반환하는 간결한 방법입니다. result = ['{:#04x}'.format(x) for x in range(256) if x % 2 == 0]은 0에서 255 범위의 짝수 16진수(0x..)를 포함하는 문자열 리스트를 생성합니다. if 절은 선택 사항입니다. 생략하면 range(256)의 모든 요소가 처리됩니다.

## loader (로더)
An object that loads a module. It must define the exec_module() and create_module() methods to implement the Loader interface. A loader is typically returned by a finder. See also:

- Finders and loaders
- importlib.abc.Loader
- PEP 302

모듈을 로드하는 객체입니다. Loader 인터페이스를 구현하기 위해 exec_module() 및 create_module() 메서드를 정의해야 합니다. 로더는 일반적으로 파인더에 의해 반환됩니다. 다음도 참조하세요:

- 파인더와 로더
- importlib.abc.Loader
- PEP 302

## locale encoding (로케일 인코딩)
On Unix, it is the encoding of the LC_CTYPE locale. It can be set with locale.setlocale(locale.LC_CTYPE, new_locale).

On Windows, it is the ANSI code page (ex: "cp1252").

On Android and VxWorks, Python uses "utf-8" as the locale encoding.

locale.getencoding() can be used to get the locale encoding.

See also the filesystem encoding and error handler.

Unix에서는 LC_CTYPE 로케일의 인코딩입니다. locale.setlocale(locale.LC_CTYPE, new_locale)로 설정할 수 있습니다.

Windows에서는 ANSI 코드 페이지입니다(예: "cp1252").

Android 및 VxWorks에서 Python은 로케일 인코딩으로 "utf-8"을 사용합니다.

locale.getencoding()을 사용하여 로케일 인코딩을 얻을 수 있습니다.

파일시스템 인코딩 및 오류 처리기도 참조하세요.

## magic method (매직 메서드)
An informal synonym for special method.

특수 메서드의 비공식적인 동의어입니다.

## mapping (매핑)
A container object that supports arbitrary key lookups and implements the methods specified in the collections.abc.Mapping or collections.abc.MutableMapping abstract base classes. Examples include dict, collections.defaultdict, collections.OrderedDict and collections.Counter.

임의의 키 조회를 지원하고 collections.abc.Mapping 또는 collections.abc.MutableMapping 추상 기본 클래스에 지정된 메서드를 구현하는 컨테이너 객체입니다. 예로는 dict, collections.defaultdict, collections.OrderedDict, collections.Counter가 있습니다.

## meta path finder (메타 경로 파인더)
A finder returned by a search of sys.meta_path. Meta path finders are related to, but different from path entry finders.

See importlib.abc.MetaPathFinder for the methods that meta path finders implement.

sys.meta_path 검색에 의해 반환되는 파인더입니다. 메타 경로 파인더는 경로 항목 파인더와 관련이 있지만 다릅니다.

메타 경로 파인더가 구현하는 메서드는 importlib.abc.MetaPathFinder를 참조하세요.

## metaclass (메타클래스)
The class of a class. Class definitions create a class name, a class dictionary, and a list of base classes. The metaclass is responsible for taking those three arguments and creating the class. Most object oriented programming languages provide a default implementation. What makes Python special is that it is possible to create custom metaclasses. Most users never need this tool, but when the need arises, metaclasses can provide powerful, elegant solutions. They have been used for logging attribute access, adding thread-safety, tracking object creation, implementing singletons, and many other tasks.

More information can be found in Metaclasses.

클래스의 클래스입니다. 클래스 정의는 클래스 이름, 클래스 사전 및 기본 클래스 목록을 만듭니다. 메타클래스는 이 세 가지 인수를 가져와 클래스를 만드는 역할을 합니다. 대부분의 객체 지향 프로그래밍 언어는 기본 구현을 제공합니다. Python이 특별한 점은 사용자 정의 메타클래스를 만들 수 있다는 것입니다. 대부분의 사용자는 이 도구가 필요하지 않지만, 필요할 때 메타클래스는 강력하고 우아한 솔루션을 제공할 수 있습니다. 메타클래스는 속성 접근 로깅, 스레드 안전성 추가, 객체 생성 추적, 싱글톤 구현 등 다양한 작업에 사용되었습니다.

자세한 정보는 메타클래스에서 찾을 수 있습니다.

## method (메서드)
A function which is defined inside a class body. If called as an attribute of an instance of that class, the method will get the instance object as its first argument (which is usually called self). See function and nested scope.

클래스 본문 내에서 정의된 함수입니다. 해당 클래스의 인스턴스의 속성으로 호출되면 메서드는 인스턴스 객체를 첫 번째 인수로 받습니다(일반적으로 self라고 함). function과 nested scope를 참조하세요.

## method resolution order (메서드 해석 순서)
Method Resolution Order is the order in which base classes are searched for a member during lookup. See The Python 2.3 Method Resolution Order for details of the algorithm used by the Python interpreter since the 2.3 release.

메서드 해석 순서는 조회 중 멤버에 대해 기본 클래스를 검색하는 순서입니다. 2.3 릴리스 이후 Python 인터프리터가 사용하는 알고리즘의 자세한 내용은 Python 2.3 메서드 해석 순서를 참조하세요.

## module (모듈)
An object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of importing.

See also package.

Python 코드의 조직 단위 역할을 하는 객체입니다. 모듈은 임의의 Python 객체를 포함하는 네임스페이스를 가지고 있습니다. 모듈은 가져오기 과정을 통해 Python에 로드됩니다.

패키지(package)도 참조하세요.

## module spec (모듈 스펙)
A namespace containing the import-related information used to load a module. An instance of importlib.machinery.ModuleSpec.

See also Module specs.

모듈을 로드하는 데 사용되는 가져오기 관련 정보를 포함하는 네임스페이스입니다. importlib.machinery.ModuleSpec의 인스턴스입니다.

모듈 스펙(Module specs)도 참조하세요.

## MRO (MRO)
See method resolution order.

메서드 해석 순서(method resolution order)를 참조하세요.

## mutable (변경 가능한)
Mutable objects can change their value but keep their id(). See also immutable.

변경 가능한 객체는 값을 변경할 수 있지만 id()는 유지합니다. immutable도 참조하세요.

## named tuple (명명된 튜플)
The term "named tuple" applies to any type or class that inherits from tuple and whose indexable elements are also accessible using named attributes. The type or class may have other features as well.

Several built-in types are named tuples, including the values returned by time.localtime() and os.stat(). Another example is sys.float_info:

```python
>>> sys.float_info[1]                   # indexed access
1024
>>> sys.float_info.max_exp              # named field access
1024
>>> isinstance(sys.float_info, tuple)   # kind of tuple
True
```

Some named tuples are built-in types (such as the above examples). Alternatively, a named tuple can be created from a regular class definition that inherits from tuple and that defines named fields. Such a class can be written by hand, or it can be created by inheriting typing.NamedTuple, or with the factory function collections.namedtuple(). The latter techniques also add some extra methods that may not be found in hand-written or built-in named tuples.

"명명된 튜플"이라는 용어는 튜플에서 상속하고 인덱싱 가능한 요소도 명명된 속성을 사용하여 접근할 수 있는 모든 유형이나 클래스에 적용됩니다. 유형이나 클래스에는 다른 기능도 있을 수 있습니다.

time.localtime()과 os.stat()이 반환하는 값을 포함한 여러 내장 유형이 명명된 튜플입니다. 또 다른 예는 sys.float_info입니다:

```python
>>> sys.float_info[1]                   # 인덱스 접근
1024
>>> sys.float_info.max_exp              # 명명된 필드 접근
1024
>>> isinstance(sys.float_info, tuple)   # 튜플의 일종
True
```

일부 명명된 튜플은 내장 유형입니다(위의 예와 같은). 또는 튜플에서 상속하고 명명된 필드를 정의하는 일반 클래스 정의에서 명명된 튜플을 만들 수 있습니다. 이러한 클래스는 수동으로 작성하거나 typing.NamedTuple에서 상속하거나 팩토리 함수 collections.namedtuple()로 만들 수 있습니다. 후자의 기술은 수동 작성 또는 내장 명명된 튜플에서 찾을 수 없는 일부 추가 메서드도 추가합니다.

## namespace (네임스페이스)
The place where a variable is stored. Namespaces are implemented as dictionaries. There are the local, global and built-in namespaces as well as nested namespaces in objects (in methods). Namespaces support modularity by preventing naming conflicts. For instance, the functions builtins.open and os.open() are distinguished by their namespaces. Namespaces also aid readability and maintainability by making it clear which module implements a function. For instance, writing random.seed() or itertools.islice() makes it clear that those functions are implemented by the random and itertools modules, respectively.

변수가 저장되는 곳입니다. 네임스페이스는 딕셔너리로 구현됩니다. 로컬, 전역 및 내장 네임스페이스와 객체(메서드)의 중첩된 네임스페이스가 있습니다. 네임스페이스는 이름 충돌을 방지하여 모듈성을 지원합니다. 예를 들어, builtins.open과 os.open() 함수는 네임스페이스로 구분됩니다. 또한 네임스페이스는 어떤 모듈이 함수를 구현하는지 명확히 함으로써 가독성과 유지 보수성을 돕습니다. 예를 들어, random.seed()나 itertools.islice()를 작성하면 이러한 함수가 각각 random과 itertools 모듈에 의해 구현된다는 것이 명확합니다.

## namespace package (네임스페이스 패키지)
A package which serves only as a container for subpackages. Namespace packages may have no physical representation, and specifically are not like a regular package because they have no __init__.py file.

Namespace packages allow several individually installable packages to have a common parent package. Otherwise, it is recommended to use a regular package.

For more information, see PEP 420 and Namespace packages.

See also module.

서브패키지를 위한 컨테이너 역할만 하는 패키지입니다. 네임스페이스 패키지는 물리적 표현이 없을 수 있으며, 특히 __init__.py 파일이 없기 때문에 일반 패키지와 다릅니다.

네임스페이스 패키지를 통해 개별적으로 설치 가능한 여러 패키지가 공통 부모 패키지를 가질 수 있습니다. 그렇지 않은 경우, 일반 패키지를 사용하는 것이 권장됩니다.

자세한 내용은 PEP 420과 네임스페이스 패키지를 참조하세요.

모듈(module)도 참조하세요.

## nested scope (중첩 스코프)
The ability to refer to a variable in an enclosing definition. For instance, a function defined inside another function can refer to variables in the outer function. Note that nested scopes by default work only for reference and not for assignment. Local variables both read and write in the innermost scope. Likewise, global variables read and write to the global namespace. The nonlocal allows writing to outer scopes.

둘러싸는 정의의 변수를 참조하는 능력입니다. 예를 들어, 다른 함수 내에서 정의된 함수는 외부 함수의 변수를 참조할 수 있습니다. 중첩된 스코프가 기본적으로 할당이 아닌 참조에만 작동한다는 점에 주의하세요. 지역 변수는 가장 안쪽 스코프에서 읽고 쓸 수 있습니다. 마찬가지로, 전역 변수는 전역 네임스페이스에서 읽고 씁니다. nonlocal은 외부 스코프에 쓰는 것을 허용합니다.

## new-style class (새 스타일 클래스)
Old name for the flavor of classes now used for all class objects. In earlier Python versions, only new-style classes could use Python's newer, versatile features like __slots__, descriptors, properties, __getattribute__(), class methods, and static methods.

현재 모든 클래스 객체에 사용되는 클래스 형식의 옛 이름입니다. 이전 Python 버전에서는 새 스타일 클래스만이 __slots__, 디스크립터, 속성, __getattribute__(), 클래스 메서드 및 정적 메서드와 같은 Python의 새롭고 다재다능한 기능을 사용할 수 있었습니다.

## object (객체)
Any data with state (attributes or value) and defined behavior (methods). Also the ultimate base class of any new-style class.

상태(속성 또는 값)와 정의된 동작(메서드)을 가진 모든 데이터입니다. 또한 모든 새 스타일 클래스의 최상위 기본 클래스이기도 합니다.

## optimized scope (최적화된 스코프)
A scope where target local variable names are reliably known to the compiler when the code is compiled, allowing optimization of read and write access to these names. The local namespaces for functions, generators, coroutines, comprehensions, and generator expressions are optimized in this fashion. Note: most interpreter optimizations are applied to all scopes, only those relying on a known set of local and nonlocal variable names are restricted to optimized scopes.

코드가 컴파일될 때 대상 지역 변수 이름이 컴파일러에 의해 확실히 알려져 있어서 이러한 이름에 대한 읽기 및 쓰기 액세스를 최적화할 수 있는 스코프입니다. 함수, 제너레이터, 코루틴, 컴프리헨션 및 제너레이터 표현식에 대한 지역 네임스페이스는 이런 방식으로 최적화됩니다. 참고: 대부분의 인터프리터 최적화는 모든 스코프에 적용되지만, 알려진 지역 및 비지역 변수 이름 집합에 의존하는 것들만 최적화된 스코프로 제한됩니다.

## package (패키지)
A Python module which can contain submodules or recursively, subpackages. Technically, a package is a Python module with a __path__ attribute.

See also regular package and namespace package.

서브모듈이나 재귀적으로 서브패키지를 포함할 수 있는 Python 모듈입니다. 기술적으로, 패키지는 __path__ 속성이 있는 Python 모듈입니다.

일반 패키지와 네임스페이스 패키지도 참조하세요.

## parameter (매개변수)
A named entity in a function (or method) definition that specifies an argument (or in some cases, arguments) that the function can accept. There are five kinds of parameter:

positional-or-keyword: specifies an argument that can be passed either positionally or as a keyword argument. This is the default kind of parameter, for example foo and bar in the following:

```python
def func(foo, bar=None): ...
```

positional-only: specifies an argument that can be supplied only by position. Positional-only parameters can be defined by including a / character in the parameter list of the function definition after them, for example posonly1 and posonly2 in the following:

```python
def func(posonly1, posonly2, /, positional_or_keyword): ...
```

keyword-only: specifies an argument that can be supplied only by keyword. Keyword-only parameters can be defined by including a single var-positional parameter or bare * in the parameter list of the function definition before them, for example kw_only1 and kw_only2 in the following:

```python
def func(arg, *, kw_only1, kw_only2): ...
```

var-positional: specifies that an arbitrary sequence of positional arguments can be provided (in addition to any positional arguments already accepted by other parameters). Such a parameter can be defined by prepending the parameter name with *, for example args in the following:

```python
def func(*args, **kwargs): ...
```

var-keyword: specifies that arbitrarily many keyword arguments can be provided (in addition to any keyword arguments already accepted by other parameters). Such a parameter can be defined by prepending the parameter name with **, for example kwargs in the example above.

Parameters can specify both optional and required arguments, as well as default values for some optional arguments.

See also the argument glossary entry, the FAQ question on the difference between arguments and parameters, the inspect.Parameter class, the Function definitions section, and PEP 362.

함수(또는 메서드) 정의에서 함수가 받을 수 있는 인수(또는 경우에 따라 인수들)를 지정하는 명명된 엔티티입니다. 다섯 가지 종류의 매개변수가 있습니다:

positional-or-keyword: 위치적으로 또는 키워드 인수로 전달될 수 있는 인수를 지정합니다. 이는 기본 종류의 매개변수입니다. 예를 들어 다음에서 foo와 bar가 있습니다:

```python
def func(foo, bar=None): ...
```

positional-only: 위치로만 제공될 수 있는 인수를 지정합니다. 위치 전용 매개변수는 함수 정의의 매개변수 목록에 / 문자를 포함시켜 정의할 수 있습니다. 예를 들어 다음에서 posonly1과 posonly2가 있습니다:

```python
def func(posonly1, posonly2, /, positional_or_keyword): ...
```

keyword-only: 키워드로만 제공될 수 있는 인수를 지정합니다. 키워드 전용 매개변수는 함수 정의의 매개변수 목록에 단일 var-positional 매개변수 또는 베어 *를 포함시켜 정의할 수 있습니다. 예를 들어 다음에서 kw_only1과 kw_only2가 있습니다:

```python
def func(arg, *, kw_only1, kw_only2): ...
```

var-positional: 임의의 위치 인수 시퀀스가 제공될 수 있음을 지정합니다(다른 매개변수에 의해 이미 허용된 위치 인수 외에도). 이러한 매개변수는 매개변수 이름 앞에 *를 붙여 정의할 수 있습니다. 예를 들어 다음에서 args가 있습니다:

```python
def func(*args, **kwargs): ...
```

var-keyword: 임의의 많은 키워드 인수가 제공될 수 있음을 지정합니다(다른 매개변수에 의해 이미 허용된 키워드 인수 외에도). 이러한 매개변수는 매개변수 이름 앞에 **를 붙여 정의할 수 있습니다. 예를 들어 위의 예에서 kwargs가 있습니다.

매개변수는 선택적 및 필수 인수 모두를 지정할 수 있으며, 일부 선택적 인수에 대한 기본값도 지정할 수 있습니다.

인수 용어집 항목, 인수와 매개변수의 차이에 대한 FAQ 질문, inspect.Parameter 클래스, 함수 정의 섹션 및 PEP 362도 참조하세요.

## path entry (경로 항목)
A single location on the import path which the path based finder consults to find modules for importing.

가져오기를 위한 모듈을 찾기 위해 경로 기반 파인더가 참조하는 가져오기 경로 상의 단일 위치입니다.

## path entry finder (경로 항목 파인더)
A finder returned by a callable on sys.path_hooks (i.e. a path entry hook) which knows how to locate modules given a path entry.

See importlib.abc.PathEntryFinder for the methods that path entry finders implement.

경로 항목이 주어졌을 때 모듈을 찾는 방법을 아는 sys.path_hooks의 호출 가능 객체(즉, 경로 항목 훅)에 의해 반환되는 파인더입니다.

경로 항목 파인더가 구현하는 메서드는 importlib.abc.PathEntryFinder를 참조하세요.

## path entry hook (경로 항목 훅)
A callable on the sys.path_hooks list which returns a path entry finder if it knows how to find modules on a specific path entry.

특정 경로 항목에서 모듈을 찾는 방법을 아는 경우 경로 항목 파인더를 반환하는 sys.path_hooks 목록의 호출 가능 객체입니다.

## path based finder (경로 기반 파인더)
One of the default meta path finders which searches an import path for modules.

가져오기 경로에서 모듈을 검색하는 기본 메타 경로 파인더 중 하나입니다.

## path-like object (경로형 객체)
An object representing a file system path. A path-like object is either a str or bytes object representing a path, or an object implementing the os.PathLike protocol. An object that supports the os.PathLike protocol can be converted to a str or bytes file system path by calling the os.fspath() function; os.fsdecode() and os.fsencode() can be used to guarantee a str or bytes result instead, respectively. Introduced by PEP 519.

파일 시스템 경로를 나타내는 객체입니다. 경로형 객체는 경로를 나타내는 str이나 bytes 객체, 또는 os.PathLike 프로토콜을 구현하는 객체입니다. os.PathLike 프로토콜을 지원하는 객체는 os.fspath() 함수를 호출하여 str이나 bytes 파일 시스템 경로로 변환할 수 있습니다. 대신 os.fsdecode()와 os.fsencode()를 사용하여 각각 str이나 bytes 결과를 보장할 수 있습니다. PEP 519에서 도입되었습니다.

## PEP (PEP)
Python Enhancement Proposal. A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment. PEPs should provide a concise technical specification and a rationale for proposed features.

PEPs are intended to be the primary mechanisms for proposing major new features, for collecting community input on an issue, and for documenting the design decisions that have gone into Python. The PEP author is responsible for building consensus within the community and documenting dissenting opinions.

See PEP 1.

Python 개선 제안서(Python Enhancement Proposal)입니다. PEP는 Python 커뮤니티에 정보를 제공하거나 Python 또는 그 프로세스나 환경에 대한 새로운 기능을 설명하는 설계 문서입니다. PEP는 제안된 기능에 대한 간결한 기술적 명세와 근거를 제공해야 합니다.

PEP는 주요 새 기능을 제안하고, 특정 이슈에 대한 커뮤니티 의견을 수집하고, Python에 반영된 설계 결정을 문서화하기 위한 주요 메커니즘입니다. PEP 작성자는 커뮤니티 내에서 합의를 형성하고 반대 의견을 문서화할 책임이 있습니다.

PEP 1을 참조하세요.

## portion (부분)
A set of files in a single directory (possibly stored in a zip file) that contribute to a namespace package, as defined in PEP 420.

PEP 420에 정의된 대로, 네임스페이스 패키지에 기여하는 단일 디렉토리(가능하게는 zip 파일에 저장된)의 파일 집합입니다.

## positional argument (위치 인자)
See argument.

인자(argument)를 참조하세요.

## provisional API (잠정 API)
A provisional API is one which has been deliberately excluded from the standard library's backwards compatibility guarantees. While major changes to such interfaces are not expected, as long as they are marked provisional, backwards incompatible changes (up to and including removal of the interface) may occur if deemed necessary by core developers. Such changes will not be made gratuitously – they will occur only if serious fundamental flaws are uncovered that were missed prior to the inclusion of the API.

Even for provisional APIs, backwards incompatible changes are seen as a "solution of last resort" - every attempt will still be made to find a backwards compatible resolution to any identified problems.

This process allows the standard library to continue to evolve over time, without locking in problematic design errors for extended periods of time. See PEP 411 for more details.

잠정 API는 표준 라이브러리의 이전 버전 호환성 보장에서 의도적으로 제외된 API입니다. 이러한 인터페이스에 대한 주요 변경은 예상되지 않지만, 잠정적으로 표시되는 한, 코어 개발자가 필요하다고 판단하면 이전 버전과 호환되지 않는 변경(인터페이스 제거 포함)이 발생할 수 있습니다. 이러한 변경은 무분별하게 이루어지지 않습니다 - API가 포함되기 전에 놓쳤던 심각한 근본적인 결함이 발견된 경우에만 발생합니다.

잠정 API의 경우에도, 이전 버전과 호환되지 않는 변경은 "마지막 수단의 해결책"으로 간주됩니다 - 식별된 모든 문제에 대해 이전 버전과 호환되는 해결책을 찾기 위한 모든 노력이 계속될 것입니다.

이 프로세스를 통해 표준 라이브러리는 장기간 동안 문제가 있는 설계 오류를 고정시키지 않고도 시간이 지남에 따라 계속 발전할 수 있습니다. 자세한 내용은 PEP 411을 참조하세요.

## provisional package (잠정 패키지)
See provisional API.

잠정 API(provisional API)를 참조하세요.

## Python 3000 (Python 3000)
Nickname for the Python 3.x release line (coined long ago when the release of version 3 was something in the distant future.) This is also abbreviated "Py3k".

Python 3.x 릴리스 라인의 별명(버전 3의 릴리스가 먼 미래의 일이었을 때 오래 전에 만들어졌습니다). 이는 "Py3k"로도 약칭됩니다.

## Pythonic (파이썬스러운)
An idea or piece of code which closely follows the most common idioms of the Python language, rather than implementing code using concepts common to other languages. For example, a common idiom in Python is to loop over all elements of an iterable using a for statement. Many other languages don't have this type of construct, so people unfamiliar with Python sometimes use a numerical counter instead:

```python
for i in range(len(food)):
    print(food[i])
```

As opposed to the cleaner, Pythonic method:

```python
for piece in food:
    print(piece)
```

다른 언어에 공통적인 개념을 사용하여 코드를 구현하기보다는 Python 언어의 가장 일반적인 관용구를 밀접하게 따르는 아이디어나 코드입니다. 예를 들어, Python의 일반적인 관용구는 for 문을 사용하여 반복 가능한 객체의 모든 요소를 반복하는 것입니다. 많은 다른 언어에는 이런 유형의 구문이 없으므로, Python에 익숙하지 않은 사람들은 때로는 대신 숫자 카운터를 사용합니다:

```python
for i in range(len(food)):
    print(food[i])
```

더 깔끔하고 파이썬스러운 방법과 대조적입니다:

```python
for piece in food:
    print(piece)
```

## qualified name (정규화된 이름)
A dotted name showing the "path" from a module's global scope to a class, function or method defined in that module, as defined in PEP 3155. For top-level functions and classes, the qualified name is the same as the object's name:

```python
>>> class C:
...     class D:
...         def meth(self):
...             pass
...
>>> C.__qualname__
'C'
>>> C.D.__qualname__
'C.D'
>>> C.D.meth.__qualname__
'C.D.meth'
```

When used to refer to modules, the fully qualified name means the entire dotted path to the module, including any parent packages, e.g. email.mime.text:

```python
>>> import email.mime.text
>>> email.mime.text.__name__
'email.mime.text'
```

PEP 3155에 정의된 대로, 모듈의 전역 범위에서 해당 모듈에 정의된 클래스, 함수 또는 메서드까지의 "경로"를 보여주는 점으로 구분된 이름입니다. 최상위 함수와 클래스의 경우, 정규화된 이름은 객체의 이름과 동일합니다:

```python
>>> class C:
...     class D:
...         def meth(self):
...             pass
...
>>> C.__qualname__
'C'
>>> C.D.__qualname__
'C.D'
>>> C.D.meth.__qualname__
'C.D.meth'
```

모듈을 참조하는 데 사용될 때, 완전히 정규화된 이름은 모든 상위 패키지를 포함하여 모듈에 이르는 전체 점 경로를 의미합니다. 예: email.mime.text:

```python
>>> import email.mime.text
>>> email.mime.text.__name__
'email.mime.text'
```

## reference count (참조 카운트)
The number of references to an object. When the reference count of an object drops to zero, it is deallocated. Some objects are immortal and have reference counts that are never modified, and therefore the objects are never deallocated. Reference counting is generally not visible to Python code, but it is a key element of the CPython implementation. Programmers can call the sys.getrefcount() function to return the reference count for a particular object.

객체에 대한 참조 수입니다. 객체의 참조 카운트가 0으로 떨어지면 해제됩니다. 일부 객체는 불멸이며 참조 카운트가 절대 수정되지 않으므로 객체가 결코 해제되지 않습니다. 참조 카운팅은 일반적으로 Python 코드에서 볼 수 없지만, CPython 구현의 핵심 요소입니다. 프로그래머는 sys.getrefcount() 함수를 호출하여 특정 객체에 대한 참조 카운트를 반환할 수 있습니다.

## regular package (일반 패키지)
A traditional package, such as a directory containing an __init__.py file.

See also namespace package.

디렉토리에 __init__.py 파일이 포함된 전통적인 패키지입니다.

네임스페이스 패키지(namespace package)도 참조하세요.

## REPL (REPL)
An acronym for the "read–eval–print loop", another name for the interactive interpreter shell.

"read-eval-print loop"(읽기-평가-출력 루프)의 약어로, 대화형 인터프리터 셸의 다른 이름입니다.

## __slots__ (__slots__)
A declaration inside a class that saves memory by pre-declaring space for instance attributes and eliminating instance dictionaries. Though popular, the technique is somewhat tricky to get right and is best reserved for rare cases where there are large numbers of instances in a memory-critical application.

인스턴스 속성을 위한 공간을 미리 선언하고 인스턴스 딕셔너리를 제거하여 메모리를 절약하는 클래스 내부의 선언입니다. 인기는 있지만, 이 기술은 올바르게 구현하기가 다소 까다롭고 메모리가 중요한 응용 프로그램에서 인스턴스 수가 많은 드문 경우에 가장 적합합니다.

## sequence (시퀀스)
An iterable which supports efficient element access using integer indices via the __getitem__() special method and defines a __len__() method that returns the length of the sequence. Some built-in sequence types are list, str, tuple, and bytes. Note that dict also supports __getitem__() and __len__(), but is considered a mapping rather than a sequence because the lookups use arbitrary hashable keys rather than integers.

The collections.abc.Sequence abstract base class defines a much richer interface that goes beyond just __getitem__() and __len__(), adding count(), index(), __contains__(), and __reversed__(). Types that implement this expanded interface can be registered explicitly using register(). For more documentation on sequence methods generally, see Common Sequence Operations.

__getitem__() 특수 메서드를 통해 정수 인덱스를 사용하여 효율적인 요소 접근을 지원하고 시퀀스의 길이를 반환하는 __len__() 메서드를 정의하는 반복 가능한 객체입니다. 내장 시퀀스 유형으로는 list, str, tuple, bytes 등이 있습니다. dict도 __getitem__()과 __len__()을 지원하지만, 조회에 정수 대신 임의의 해시 가능한 키를 사용하므로 시퀀스가 아닌 매핑으로 간주됩니다.

collections.abc.Sequence 추상 기본 클래스는 __getitem__()과 __len__()을 넘어 count(), index(), __contains__(), __reversed__()를 추가하는 훨씬 더 풍부한 인터페이스를 정의합니다. 이 확장된 인터페이스를 구현하는 유형은 register()를 사용하여 명시적으로 등록될 수 있습니다. 시퀀스 메서드에 관한 일반적인 문서는 일반 시퀀스 연산을 참조하세요.

## set comprehension (집합 컴프리헨션)
A compact way to process all or part of the elements in an iterable and return a set with the results. results = {c for c in 'abracadabra' if c not in 'abc'} generates the set of strings {'r', 'd'}. See Displays for lists, sets and dictionaries.

반복 가능한 객체의 모든 요소 또는 일부를 처리하고 결과로 집합을 반환하는 간결한 방법입니다. results = {c for c in 'abracadabra' if c not in 'abc'}는 {'r', 'd'} 문자열 집합을 생성합니다. 리스트, 집합 및 딕셔너리에 대한 디스플레이를 참조하세요.

## single dispatch (단일 디스패치)
A form of generic function dispatch where the implementation is chosen based on the type of a single argument.

단일 인수의 타입에 기초하여 구현이 선택되는 제네릭 함수 디스패치의 한 형태입니다.

## slice (슬라이스)
An object usually containing a portion of a sequence. A slice is created using the subscript notation, [] with colons between numbers when several are given, such as in variable_name[1:3:5]. The bracket (subscript) notation uses slice objects internally.

일반적으로 시퀀스의 일부를 포함하는 객체입니다. 슬라이스는 대괄호 표기법을 사용하여 생성되며, 여러 개가 주어질 때는 숫자 사이에 콜론을 사용합니다(예: variable_name[1:3:5]). 대괄호(첨자) 표기법은 내부적으로 슬라이스 객체를 사용합니다.

## soft deprecated (소프트 지원 중단)
A soft deprecated API should not be used in new code, but it is safe for already existing code to use it. The API remains documented and tested, but will not be enhanced further.

Soft deprecation, unlike normal deprecation, does not plan on removing the API and will not emit warnings.

See PEP 387: Soft Deprecation.

소프트 지원 중단된 API는 새 코드에서 사용하지 않아야 하지만, 이미 존재하는 코드에서 사용하는 것은 안전합니다. API는 계속 문서화되고 테스트되지만 더 이상 개선되지는 않습니다.

일반적인 지원 중단과 달리, 소프트 지원 중단은 API 제거 계획이 없으며 경고를 발생시키지 않습니다.

PEP 387: 소프트 지원 중단을 참조하세요.

## special method (특수 메서드)
A method that is called implicitly by Python to execute a certain operation on a type, such as addition. Such methods have names starting and ending with double underscores. Special methods are documented in Special method names.

덧셈과 같은 특정 연산을 타입에서 실행하기 위해 Python에 의해 암시적으로 호출되는 메서드입니다. 이러한 메서드는 이름이 이중 밑줄로 시작하고 끝납니다. 특수 메서드는 특수 메서드 이름에 문서화되어 있습니다.

## statement (문)
A statement is part of a suite (a "block" of code). A statement is either an expression or one of several constructs with a keyword, such as if, while or for.

문은 스위트("코드 블록")의 일부입니다. 문은 표현식이거나 if, while, for와 같은 키워드를 가진 여러 구성 중 하나입니다.

## static type checker (정적 타입 검사기)
An external tool that reads Python code and analyzes it, looking for issues such as incorrect types. See also type hints and the typing module.

Python 코드를 읽고 분석하여 잘못된 타입과 같은 문제를 찾는 외부 도구입니다. 타입 힌트와 typing 모듈도 참조하세요.

## strong reference (강한 참조)
In Python's C API, a strong reference is a reference to an object which is owned by the code holding the reference. The strong reference is taken by calling Py_INCREF() when the reference is created and released with Py_DECREF() when the reference is deleted.

The Py_NewRef() function can be used to create a strong reference to an object. Usually, the Py_DECREF() function must be called on the strong reference before exiting the scope of the strong reference, to avoid leaking one reference.

See also borrowed reference.

Python의 C API에서 강한 참조는 참조를 보유하는 코드가 소유한 객체에 대한 참조입니다. 강한 참조는 참조가 생성될 때 Py_INCREF()를 호출하여 가져오고 참조가 삭제될 때 Py_DECREF()로 해제됩니다.

Py_NewRef() 함수를 사용하여 객체에 대한 강한 참조를 생성할 수 있습니다. 일반적으로 참조 누수를 방지하기 위해 강한 참조의 범위를 벗어나기 전에 강한 참조에 대해 Py_DECREF() 함수를 호출해야 합니다.

대여된 참조(borrowed reference)도 참조하세요.

## text encoding (텍스트 인코딩)
A string in Python is a sequence of Unicode code points (in range U+0000–U+10FFFF). To store or transfer a string, it needs to be serialized as a sequence of bytes.

Serializing a string into a sequence of bytes is known as "encoding", and recreating the string from the sequence of bytes is known as "decoding".

There are a variety of different text serialization codecs, which are collectively referred to as "text encodings".

Python에서 문자열은 유니코드 코드 포인트(U+0000-U+10FFFF 범위)의 시퀀스입니다. 문자열을 저장하거나 전송하려면 바이트 시퀀스로 직렬화해야 합니다.

문자열을 바이트 시퀀스로 직렬화하는 것을 "인코딩"이라고 하며, 바이트 시퀀스에서 문자열을 재생성하는 것을 "디코딩"이라고 합니다.

다양한 텍스트 직렬화 코덱이 있으며, 이를 통틀어 "텍스트 인코딩"이라고 합니다.

## text file (텍스트 파일)
A file object able to read and write str objects. Often, a text file actually accesses a byte-oriented datastream and handles the text encoding automatically. Examples of text files are files opened in text mode ('r' or 'w'), sys.stdin, sys.stdout, and instances of io.StringIO.

See also binary file for a file object able to read and write bytes-like objects.

str 객체를 읽고 쓸 수 있는 파일 객체입니다. 종종 텍스트 파일은 실제로 바이트 지향 데이터 스트림에 접근하고 텍스트 인코딩을 자동으로 처리합니다. 텍스트 파일의 예로는 텍스트 모드('r' 또는 'w')로 열린 파일, sys.stdin, sys.stdout 및 io.StringIO의 인스턴스가 있습니다.

바이트 유사 객체를 읽고 쓸 수 있는 파일 객체에 대해서는 바이너리 파일(binary file)도 참조하세요.

## triple-quoted string (삼중 따옴표 문자열)
A string which is bound by three instances of either a quotation mark (") or an apostrophe ('). While they don't provide any functionality not available with single-quoted strings, they are useful for a number of reasons. They allow you to include unescaped single and double quotes within a string and they can span multiple lines without the use of the continuation character, making them especially useful when writing docstrings.

인용 부호(") 또는 아포스트로피(')의 세 인스턴스로 묶인 문자열입니다. 단일 따옴표 문자열에서 사용할 수 없는 기능을 제공하지는 않지만, 여러 가지 이유로 유용합니다. 문자열 내에 이스케이프되지 않은 작은따옴표와 큰따옴표를 포함할 수 있으며, 연속 문자의 사용 없이 여러 줄에 걸쳐 있을 수 있어, 특히 독스트링을 작성할 때 유용합니다.

## type (타입)
The type of a Python object determines what kind of object it is; every object has a type. An object's type is accessible as its __class__ attribute or can be retrieved with type(obj).

Python 객체의 타입은 그것이 어떤 종류의 객체인지 결정합니다; 모든 객체는 타입을 가집니다. 객체의 타입은 __class__ 속성으로 접근하거나 type(obj)로 검색할 수 있습니다.

## type alias (타입 별칭)
A synonym for a type, created by assigning the type to an identifier.

Type aliases are useful for simplifying type hints. For example:

```python
def remove_gray_shades(
        colors: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    pass
```

could be made more readable like this:

```python
Color = tuple[int, int, int]

def remove_gray_shades(colors: list[Color]) -> list[Color]:
    pass
```

See typing and PEP 484, which describe this functionality.

타입을 식별자에 할당하여 생성된 타입의 동의어입니다.

타입 별칭은 타입 힌트를 단순화하는 데 유용합니다. 예를 들어:

```python
def remove_gray_shades(
        colors: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    pass
```

이것을 다음과 같이 더 읽기 쉽게 만들 수 있습니다:

```python
Color = tuple[int, int, int]

def remove_gray_shades(colors: list[Color]) -> list[Color]:
    pass
```

이 기능을 설명하는 typing과 PEP 484를 참조하세요.

## type hint (타입 힌트)
An annotation that specifies the expected type for a variable, a class attribute, or a function parameter or return value.

Type hints are optional and are not enforced by Python but they are useful to static type checkers. They can also aid IDEs with code completion and refactoring.

Type hints of global variables, class attributes, and functions, but not local variables, can be accessed using typing.get_type_hints().

See typing and PEP 484, which describe this functionality.

변수, 클래스 속성, 함수 매개변수 또는 반환 값에 대한 예상 타입을 지정하는 주석입니다.

타입 힌트는 선택 사항이며 Python에 의해 강제되지 않지만 정적 타입 검사기에 유용합니다. 또한 코드 완성 및 리팩터링에 IDE를 도울 수 있습니다.

전역 변수, 클래스 속성 및 함수의 타입 힌트는 typing.get_type_hints()를 사용하여 접근할 수 있지만 지역 변수는 접근할 수 없습니다.

이 기능을 설명하는 typing과 PEP 484를 참조하세요.

## universal newlines (범용 줄바꿈)
A manner of interpreting text streams in which all of the following are recognized as ending a line: the Unix end-of-line convention '\n', the Windows convention '\r\n', and the old Macintosh convention '\r'. See PEP 278 and PEP 3116, as well as bytes.splitlines() for an additional use.

텍스트 스트림을 해석하는 방식으로, 다음 모두가 행의 끝으로 인식됩니다: Unix 줄 끝 규칙 '\n', Windows 규칙 '\r\n', 그리고 구식 Macintosh 규칙 '\r'. PEP 278과 PEP 3116을 참조하세요. 또한 추가 용도로 bytes.splitlines()를 참조하세요.

## variable annotation (변수 주석)
An annotation of a variable or a class attribute.

When annotating a variable or a class attribute, assignment is optional:

```python
class C:
    field: 'annotation'
```

Variable annotations are usually used for type hints: for example this variable is expected to take int values:

```python
count: int = 0
```

Variable annotation syntax is explained in section Annotated assignment statements.

See function annotation, PEP 484 and PEP 526, which describe this functionality. Also see Annotations Best Practices for best practices on working with annotations.

변수 또는 클래스 속성의 주석입니다.

변수 또는 클래스 속성에 주석을 달 때, 할당은 선택 사항입니다:

```python
class C:
    field: 'annotation'
```

변수 주석은 일반적으로 타입 힌트에 사용됩니다: 예를 들어 이 변수는 int 값을 가질 것으로 예상됩니다:

```python
count: int = 0
```

변수 주석 구문은 주석이 달린 할당 문 섹션에 설명되어 있습니다.

이 기능을 설명하는 함수 주석, PEP 484 및 PEP 526을 참조하세요. 또한 주석 작업에 관한 모범 사례는 주석 모범 사례를 참조하세요.

## virtual environment (가상 환경)
A cooperatively isolated runtime environment that allows Python users and applications to install and upgrade Python distribution packages without interfering with the behaviour of other Python applications running on the same system.

See also venv.

Python 사용자와 응용 프로그램이 동일한 시스템에서 실행 중인 다른 Python 응용 프로그램의 동작을 방해하지 않고 Python 배포 패키지를 설치하고 업그레이드할 수 있게 해주는 협력적으로 격리된 런타임 환경입니다.

venv도 참조하세요.

## virtual machine (가상 머신)
A computer defined entirely in software. Python's virtual machine executes the bytecode emitted by the bytecode compiler.

소프트웨어에서 완전히 정의된 컴퓨터입니다. Python의 가상 머신은 바이트코드 컴파일러에 의해 방출된 바이트코드를 실행합니다.

## Zen of Python (파이썬의 선)
Listing of Python design principles and philosophies that are helpful in understanding and using the language. The listing can be found by typing "import this" at the interactive prompt.

언어를 이해하고 사용하는 데 도움이 되는 Python 설계 원칙과 철학을 나열한 것입니다. 대화형 프롬프트에서 "import this"를 입력하여 목록을 볼 수 있습니다.
