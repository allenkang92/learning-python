# 6. Modules

1. If you quit from the Python interpreter and enter it again, the definitions you have made (functions and variables) are lost. Therefore, if you want to write a somewhat longer program, you are better off using a text editor to prepare the input for the interpreter and running it with that file as input instead. This is known as creating a script. As your program gets longer, you may want to split it into several files for easier maintenance. You may also want to use a handy function that you’ve written in several programs without copying its definition into each program.

파이썬 인터프리터를 종료하고 다시 들어가면, 정의한 것들(함수와 변수)이 사라집니다. 따라서, 조금 더 긴 프로그램을 작성하려면, 텍스트 편집기를 사용하여 인터프리터의 입력을 준비하고 그 파일을 입력으로 실행하는 것이 좋습니다. 이것을 스크립트를 작성한다고 합니다. 프로그램이 길어지면, 유지보수를 쉽게 하기 위해 여러 파일로 나누고 싶을 수 있습니다. 또한, 여러 프로그램에서 정의를 복사하지 않고 작성한 유용한 함수를 사용하고 싶을 수도 있습니다.

2. To support this, Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module; definitions from a module can be imported into other modules or into the main module (the collection of variables that you have access to in a script executed at the top level and in calculator mode).

이를 지원하기 위해, 파이썬은 정의를 파일에 넣고 스크립트나 인터프리터의 대화형 인스턴스에서 사용할 수 있는 방법을 제공합니다. 이러한 파일을 모듈이라고 하며, 모듈의 정의는 다른 모듈이나 메인 모듈(최상위에서 실행된 스크립트와 계산기 모드에서 접근할 수 있는 변수의 모음)로 가져올 수 있습니다.

3. A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py added. Within a module, the module’s name (as a string) is available as the value of the global variable __name__. For instance, use your favorite text editor to create a file called fibo.py in the current directory with the following contents:

모듈은 파이썬 정의와 문을 포함하는 파일입니다. 파일 이름은 .py 접미사가 추가된 모듈 이름입니다. 모듈 내에서, 모듈의 이름(문자열로)은 전역 변수 __name__의 값으로 사용할 수 있습니다. 예를 들어, 현재 디렉터리에 fibo.py라는 파일을 다음 내용으로 작성하세요:

```python
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

4. Now enter the Python interpreter and import this module with the following command:

이제 파이썬 인터프리터에 들어가서 다음 명령어로 이 모듈을 가져오세요:

```python
>>> import fibo
```

5. This does not enter the names of the functions defined in fibo directly in the current symbol table; it only enters the module name fibo there. Using the module name you can access the functions:

이것은 현재 심볼 테이블에 fibo에 정의된 함수 이름을 직접 입력하지 않습니다. 단지 모듈 이름 fibo를 입력합니다. 모듈 이름을 사용하여 함수를 접근할 수 있습니다:

```python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```

6. If you intend to use a function often you can assign it to a local name:

함수를 자주 사용할 의도가 있다면, 로컬 이름에 할당할 수 있습니다:

```python
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

## 6.1. More on Modules

7. A module can contain executable statements as well as function definitions. These statements are intended to initialize the module. They are executed only the first time the module name is encountered in an import statement. [1] (They are also run if the file is executed as a script.)

모듈은 함수 정의뿐만 아니라 실행 가능한 문을 포함할 수 있습니다. 이러한 문은 모듈을 초기화하는 데 사용됩니다. 이들은 import 문에서 모듈 이름이 처음으로 발견될 때만 실행됩니다. [1] (파일이 스크립트로 실행되는 경우에도 실행됩니다.)

8. Each module has its own private symbol table, which is used as the global symbol table by all functions defined in the module. Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user’s global variables. On the other hand, if you know what you are doing you can touch a module’s global variables with the same notation used to refer to its functions, modname.itemname.

각 모듈은 자체의 개인 심볼 테이블을 가지고 있으며, 이는 모듈에 정의된 모든 함수에 의해 전역 심볼 테이블로 사용됩니다. 따라서, 모듈의 작성자는 사용자의 전역 변수와의 우연한 충돌을 걱정하지 않고 모듈에서 전역 변수를 사용할 수 있습니다. 반면에, 무엇을 하고 있는지 알고 있다면, 함수에 접근하는 것과 동일한 표기법을 사용하여 모듈의 전역 변수에 접근할 수 있습니다, modname.itemname.

9. Modules can import other modules. It is customary but not required to place all import statements at the beginning of a module (or script, for that matter). The imported module names are placed in the importing module’s global symbol table.

모듈은 다른 모듈을 가져올 수 있습니다. 모든 import 문을 모듈(또는 스크립트)의 시작 부분에 배치하는 것이 관례이지만 필수는 아닙니다. 가져온 모듈 이름은 가져오는 모듈의 전역 심볼 테이블에 배치됩니다.

10. There is a variant of the import statement that imports names from a module directly into the importing module’s symbol table. For example:

모듈의 이름을 가져오는 모듈의 심볼 테이블에 직접 가져오는 import 문 변형이 있습니다. 예를 들어:

```python
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

11. This does not introduce the module name from which the imports are taken in the local symbol table (so in the example, fibo is not defined).

이것은 가져온 모듈 이름을 로컬 심볼 테이블에 도입하지 않습니다(따라서 예제에서 fibo는 정의되지 않습니다).

12. There is even a variant to import all names that a module defines:

모듈이 정의하는 모든 이름을 가져오는 변형도 있습니다:

```python
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

13. This imports all names except those beginning with an underscore (_).

이는 밑줄(_)로 시작하는 이름을 제외한 모든 이름을 가져옵니다.

14. Note that in general the practice of importing * from a module or package is frowned upon, since it often causes poorly readable code. However, it is okay to use it to save typing in interactive sessions.

일반적으로 모듈이나 패키지에서 *를 가져오는 관행은 권장되지 않습니다. 이는 종종 읽기 어려운 코드를 유발하기 때문입니다. 그러나 대화형 세션에서 타이핑을 줄이기 위해 사용하는 것은 괜찮습니다.

15. If the module name is followed by as, then the name following as is bound directly to the imported module.

모듈 이름 뒤에 as가 오면, as 뒤의 이름이 가져온 모듈에 직접 바인딩됩니다.

```python
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

16. This is effectively importing the module in the same way that import fibo will do, with the only difference of it being available as fib.

이는 import fibo가 하는 것과 동일한 방식으로 모듈을 가져오는 것이며, 단지 fib로 사용할 수 있다는 점만 다릅니다.

17. It can also be used when utilising from with similar effects:

유사한 효과를 위해 from을 사용할 때도 사용할 수 있습니다:

```python
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

## 6.2. Standard Modules

18. Python comes with a library of standard modules, described in a separate document, the Python Library Reference (``library``). Some modules are built into the interpreter; these provide access to operations that are not part of the core of the language but are nevertheless built in, either for efficiency or to provide access to operating system primitives such as system calls. The set of such modules is a configuration option which also depends on the underlying platform. For example, the `winreg` module is only provided on Windows systems. One particular module deserves some attention: `sys`, which is built into every Python interpreter. The variables `sys.ps1` and `sys.ps2` define the strings used as primary and secondary prompts:

파이썬은 표준 모듈 라이브러리를 제공하며, 이는 별도의 문서인 파이썬 라이브러리 참조(``library``)에 설명되어 있습니다. 일부 모듈은 인터프리터에 내장되어 있으며, 이는 언어의 핵심 부분이 아니지만 효율성을 위해 또는 시스템 호출과 같은 운영 체제 기본 요소에 접근하기 위해 내장되어 있습니다. 이러한 모듈의 집합은 구성 옵션이며, 기본 플랫폼에 따라 다릅니다. 예를 들어, `winreg` 모듈은 Windows 시스템에서만 제공됩니다. 특정 모듈 하나가 주목할 만한데, 그것은 모든 파이썬 인터프리터에 내장된 `sys`입니다. 변수 `sys.ps1`과 `sys.ps2`는 기본 및 보조 프롬프트로 사용되는 문자열을 정의합니다:

```python
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```

19. These two variables are only defined if the interpreter is in interactive mode.

이 두 변수는 인터프리터가 대화형 모드에 있을 때만 정의됩니다.

20. The `sys` module also has attributes for stdin, stdout, and stderr. The latter are useful for emitting warnings and error messages to make them visible even when stdout has been redirected:

`sys` 모듈에는 stdin, stdout, stderr에 대한 속성도 있습니다. 후자는 경고 및 오류 메시지를 출력하여 stdout이 리디렉션된 경우에도 이를 볼 수 있도록 하는 데 유용합니다:

```python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```

21. The `sys` module has many other functions and variables. For more information, see the Python Library Reference.

`sys` 모듈에는 많은 다른 함수와 변수가 있습니다. 자세한 내용은 파이썬 라이브러리 참조를 참조하세요.

## 6.3. The dir() Function

22. The built-in function `dir()` is used to find out which names a module defines. It returns a sorted list of strings:

내장 함수 `dir()`은 모듈이 정의하는 이름을 찾는 데 사용됩니다. 정렬된 문자열 리스트를 반환합니다:

```python
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']
```

23. Without arguments, `dir()` lists the names you have defined currently:

인수 없이 사용하면, `dir()`은 현재 정의된 이름들을 나열합니다:

```python
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```

24. Note that it lists all types of names: variables, modules, functions, etc.

모든 유형의 이름(변수, 모듈, 함수 등)을 나열한다는 점에 유의하세요.

25. `dir()` does not list the names of built-in functions and variables. If you want a list of those, they are defined in the standard module `builtins`:

`dir()`은 내장 함수와 변수의 이름을 나열하지 않습니다. 그것들의 목록이 필요하면, 표준 모듈 `builtins`에 정의되어 있습니다:

```python
>>> import builtins
>>> dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
```

## 6.4. Packages

26. Packages are a way of structuring Python’s module namespace by using “dotted module names”. For example, the module name A.B designates a submodule named B in a package named A. Just like the use of modules saves the authors of different modules from having to worry about each other’s global variable names, the use of dotted module names saves the authors of multi-module packages from having to worry about each other’s module names.

패키지는 "점으로 구분된 모듈 이름"을 사용하여 파이썬의 모듈 네임스페이스를 구조화하는 방법입니다. 예를 들어, 모듈 이름 A.B는 A라는 패키지에 있는 B라는 하위 모듈을 지정합니다. 모듈을 사용하면 서로의 전역 변수 이름을 걱정할 필요가 없는 것처럼, 점으로 구분된 모듈 이름을 사용하면 여러 모듈 패키지의 작성자가 서로의 모듈 이름을 걱정할 필요가 없습니다.

27. Suppose you want to design a collection of modules (a “package”) for the uniform handling of sound files and sound data. There are many different sound file formats (usually recognized by their extension, for example: .wav, .aiff, .au), so you may need to create and maintain a growing collection of modules for the conversion between the various file formats. There are also many different operations you might want to perform on sound data (such as mixing, adding echo, applying an equalizer function, creating an artificial stereo effect), so in addition you will be writing a never-ending stream of modules to perform these operations. Here is a possible structure for your package (expressed in terms of a hierarchical filesystem):

사운드 파일과 사운드 데이터를 일관되게 처리하기 위한 모듈 모음(“패키지”)을 설계하고 싶다고 가정해 봅시다. 많은 다른 사운드 파일 형식이 있습니다(일반적으로 확장자로 인식됩니다. 예: .wav, .aiff, .au). 따라서 다양한 파일 형식 간의 변환을 위해 점점 더 많은 모듈 모음을 생성하고 유지 관리해야 할 수 있습니다. 또한 사운드 데이터에 대해 수행하고자 하는 많은 다른 작업이 있습니다(예: 믹싱, 에코 추가, 이퀄라이저 함수 적용, 인공 스테레오 효과 생성). 따라서 이러한 작업을 수행하기 위해 끝없는 모듈 스트림을 작성하게 될 것입니다. 다음은 패키지의 가능한 구조입니다(계층적 파일 시스템의 용어로 표현됨):

```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

28. When importing the package, Python searches through the directories on sys.path looking for the package subdirectory.

패키지를 가져올 때, 파이썬은 sys.path의 디렉터리를 검색하여 패키지 하위 디렉터리를 찾습니다.

29. The __init__.py files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name, such as string, from unintentionally hiding valid modules that occur later on the module search path. In the simplest case, __init__.py can just be an empty file, but it can also execute initialization code for the package or set the __all__ variable, described later.

__init__.py 파일은 파이썬이 디렉터리를 패키지를 포함하는 것으로 처리하도록 하기 위해 필요합니다. 이는 string과 같은 공통 이름을 가진 디렉터리가 모듈 검색 경로에서 나중에 발생하는 유효한 모듈을 의도치 않게 숨기는 것을 방지하기 위해 수행됩니다. 가장 간단한 경우, __init__.py는 빈 파일일 수 있지만, 패키지에 대한 초기화 코드를 실행하거나 나중에 설명할 __all__ 변수를 설정할 수도 있습니다.

30. Users of the package can import individual modules from the package, for example:

패키지 사용자는 패키지에서 개별 모듈을 가져올 수 있습니다. 예를 들어:

```python
import sound.effects.echo
```

31. This loads the submodule sound.effects.echo. It must be referenced with its full name.

이는 하위 모듈 sound.effects.echo를 로드합니다. 전체 이름으로 참조해야 합니다.

```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

32. An alternative way of importing the submodule is:

하위 모듈을 가져오는 또 다른 방법은 다음과 같습니다:

```python
from sound.effects import echo
```

33. This also loads the submodule echo, and makes it available without its package prefix, so it can be used as follows:

이는 하위 모듈 echo를 로드하고, 패키지 접두사 없이 사용할 수 있도록 하여 다음과 같이 사용할 수 있습니다:

```python
echo.echofilter(input, output, delay=0.7, atten=4)
```

34. Yet another variation is to import the desired function or variable directly:

또 다른 변형은 원하는 함수나 변수를 직접 가져오는 것입니다:

```python
from sound.effects.echo import echofilter
```

35. Again, this loads the submodule echo, but this makes its function echofilter() directly available:

다시 말해, 이는 하위 모듈 echo를 로드하지만, 함수 echofilter()를 직접 사용할 수 있게 합니다:

```python
echofilter(input, output, delay=0.7, atten=4)
```

36. Note that when using from package import item, the item can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable. The import statement first tests whether the item is defined in the package; if not, it assumes it is a module and attempts to load it. If it fails to find it, an ImportError exception is raised.

from package import item을 사용할 때, item은 패키지의 하위 모듈(또는 하위 패키지)일 수도 있고, 함수, 클래스 또는 변수와 같은 패키지에 정의된 다른 이름일 수도 있습니다. import 문은 먼저 item이 패키지에 정의되어 있는지 테스트합니다. 그렇지 않으면, 모듈로 간주하고 로드하려고 시도합니다. 찾지 못하면 ImportError 예외가 발생합니다.

37. Conversely, when using import item.subitem.subsubitem, each item except for the last must be a package; the last item can be a module or a package but can’t be a class or function or variable defined in the previous item.

반대로, import item.subitem.subsubitem을 사용할 때, 마지막을 제외한 각 item은 패키지여야 합니다. 마지막 item은 모듈 또는 패키지일 수 있지만, 이전 item에 정의된 클래스, 함수 또는 변수일 수는 없습니다.

38. Importing * from a package is not recommended, as it often causes poorly readable code. However, if the package’s __init__.py code defines a list named __all__, it is taken to be the list of module names that should be imported when from package import * is encountered. It is up to the package author to keep this list up-to-date and to decide which modules the package exports as part of its public API. If __all__ is not defined, the statement from package import * does not import all submodules from the package into the current namespace; it only ensures that the package has been imported (possibly running any initialization code in __init__.py) and then imports whatever names are defined in the package. This includes any names defined (and submodules explicitly loaded) by __init__.py.

패키지에서 *를 가져오는 것은 권장되지 않습니다. 이는 종종 읽기 어려운 코드를 유발하기 때문입니다. 그러나 패키지의 __init__.py 코드가 __all__이라는 이름의 리스트를 정의하면, 이는 from package import *가 발생할 때 가져와야 할 모듈 이름의 리스트로 간주됩니다. 이 리스트를 최신 상태로 유지하고 패키지가 공개 API의 일부로 내보내는 모듈을 결정하는 것은 패키지 작성자의 몫입니다. __all__이 정의되지 않은 경우, from package import * 문은 패키지의 모든 하위 모듈을 현재 네임스페이스로 가져오지 않습니다. 이는 단지 패키지가 가져와졌음을 보장하고(아마도 __init__.py의 초기화 코드를 실행) 패키지에 정의된 이름을 가져옵니다. 여기에는 __init__.py에 의해 정의된 모든 이름(및 명시적으로 로드된 하위 모듈)이 포함됩니다.

39. Here is an example of a potentially confusing situation. In the file sound/effects/__init__.py, the following code is included:

다음은 잠재적으로 혼란스러운 상황의 예입니다. 파일 sound/effects/__init__.py에 다음 코드가 포함되어 있습니다:

```python
__all__ = ["echo", "surround", "reverse"]
```

40. This means that when you type from sound.effects import *, you will import the three named submodules of the sound.effects package.

이는 from sound.effects import *를 입력하면 sound.effects 패키지의 세 명명된 하위 모듈을 가져오게 됨을 의미합니다.

41. If __all__ is not defined, the statement from sound.effects import * does not import all submodules from the sound.effects package into the current namespace; it only ensures that the package sound.effects has been imported (possibly running any initialization code in sound/effects/__init__.py) and then imports whatever names are defined in the package. This includes any names defined (and submodules explicitly loaded) by sound/effects/__init__.py.

__all__이 정의되지 않은 경우, from sound.effects import * 문은 sound.effects 패키지의 모든 하위 모듈을 현재 네임스페이스로 가져오지 않습니다. 이는 단지 패키지 sound.effects가 가져와졌음을 보장하고(아마도 sound/effects/__init__.py의 초기화 코드를 실행) 패키지에 정의된 이름을 가져옵니다. 여기에는 sound/effects/__init__.py에 의해 정의된 모든 이름(및 명시적으로 로드된 하위 모듈)이 포함됩니다.

42. Remember, there is nothing wrong with using from package import specific_submodule! In fact, this is the recommended notation unless the importing module needs to use submodules with the same name from different packages.

from package import specific_submodule을 사용하는 것은 전혀 문제가 없습니다! 사실, 가져오는 모듈이 다른 패키지에서 동일한 이름의 하위 모듈을 사용해야 하는 경우가 아니라면, 이것이 권장되는 표기법입니다.

43. Although certain modules are designed to export only names that follow certain patterns when you use import *, it is still considered bad practice in production code.

일부 모듈은 import *를 사용할 때 특정 패턴을 따르는 이름만 내보내도록 설계되었지만, 이는 여전히 프로덕션 코드에서 나쁜 관행으로 간주됩니다.

44. Remember, there is nothing wrong with using from package import specific_submodule! In fact, this is the recommended notation unless the importing module needs to use submodules with the same name from different packages.

from package import specific_submodule을 사용하는 것은 전혀 문제가 없습니다! 사실, 가져오는 모듈이 다른 패키지에서 동일한 이름의 하위 모듈을 사용해야 하는 경우가 아니라면, 이것이 권장되는 표기법입니다.

45. The most important thing is that the package author should provide a clear and consistent API, and the user should follow the package’s documentation and guidelines.

가장 중요한 것은 패키지 작성자가 명확하고 일관된 API를 제공해야 하며, 사용자는 패키지의 문서와 지침을 따라야 한다는 것입니다.

**Footnotes**

[1] 사실, 객체 참조에 의한 호출이 더 나은 설명일 것입니다. 가변 객체가 전달되는 경우, 호출자는 피호출자가 그것에 가하는 모든 변경(리스트에 삽입된 항목 등)을 볼 수 있기 때문입니다.