# 8. Errors and Exceptions

1. Until now error messages haven't been more than mentioned, but if you have tried out the examples you have probably seen some. There are (at least) two distinguishable kinds of errors: syntax errors and exceptions.

지금까지 오류 메시지에 대해서는 간단히 언급만 했지만, 예제를 직접 실행해 봤다면 아마 몇 가지 오류를 보았을 것입니다. (최소한) 두 가지 구별할 수 있는 종류의 오류가 있습니다: 구문 오류와 예외입니다.

## 8.1. Syntax Errors

2. Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python:

구문 오류(파싱 오류라고도 함)는 아마도 파이썬을 배우는 동안 가장 흔하게 접하는 불만일 것입니다:

```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax
```

3. The parser repeats the offending line and displays little arrows pointing at the token in the line where the error was detected. The error may be caused by the absence of a token before the indicated token. In the example, the error is detected at the function print(), since a colon (':') is missing before it. File name and line number are printed so you know where to look in case the input came from a script.

파서는 문제가 있는 줄을 반복하고 오류가 감지된 줄에서 토큰을 가리키는 작은 화살표를 표시합니다. 오류는 표시된 토큰 앞에 토큰이 없어서 발생할 수 있습니다. 예를 들어, 오류는 함수 print()에서 감지되는데, 이는 그 앞에 콜론(':')이 누락되었기 때문입니다. 입력이 스크립트에서 왔을 경우 어디를 살펴봐야 하는지 알 수 있도록 파일 이름과 줄 번호가 출력됩니다.

## 8.2. Exceptions

4. Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal: you will soon learn how to handle them in Python programs. Most exceptions are not handled by programs, however, and result in error messages as shown here:

문장이나 표현식이 구문적으로 올바르더라도, 실행을 시도할 때 오류가 발생할 수 있습니다. 실행 중에 감지된 오류를 예외라고 하며, 이는 무조건적으로 치명적이지는 않습니다: 곧 파이썬 프로그램에서 이를 처리하는 방법을 배우게 될 것입니다. 그러나 대부분의 예외는 프로그램에서 처리되지 않고 여기에 표시된 것과 같은 오류 메시지를 발생시킵니다:

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

5. The last line of the error message indicates what happened. Exceptions come in different types, and the type is printed as part of the message: the types in the example are ZeroDivisionError, NameError and TypeError. The string printed as the exception type is the name of the built-in exception that occurred. This is true for all built-in exceptions, but need not be true for user-defined exceptions (although it is a useful convention). Standard exception names are built-in identifiers (not reserved keywords).

오류 메시지의 마지막 줄은 무슨 일이 일어났는지를 나타냅니다. 예외는 다양한 유형으로 제공되며, 유형은 메시지의 일부로 출력됩니다: 예제의 유형은 ZeroDivisionError, NameError 및 TypeError입니다. 예외 유형으로 출력된 문자열은 발생한 내장 예외의 이름입니다. 이것은 모든 내장 예외에 해당하지만, 사용자 정의 예외에는 해당될 필요가 없습니다(유용한 규칙이지만). 표준 예외 이름은 내장 식별자입니다(예약어가 아님).

6. The rest of the line provides detail based on the type of exception and what caused it.

줄의 나머지 부분은 예외 유형과 그 원인에 기반한 세부 정보를 제공합니다.

7. The preceding part of the error message shows the context where the exception occurred, in the form of a stack traceback. In general it contains a stack traceback listing source lines; however, it will not display lines read from standard input.

오류 메시지의 앞부분은 예외가 발생한 컨텍스트를 스택 트레이스백 형태로 보여줍니다. 일반적으로 소스 라인을 나열하는 스택 트레이스백이 포함됩니다. 그러나 표준 입력에서 읽은 라인은 표시되지 않습니다.

8. Built-in Exceptions lists the built-in exceptions and their meanings.

내장 예외는 내장 예외와 그 의미를 나열합니다.

## 8.3. Handling Exceptions

9. It is possible to write programs that handle selected exceptions. Look at the following example, which asks the user for input until a valid integer has been entered, but allows the user to interrupt the program (using Control-C or whatever the operating system supports); note that a user-generated interruption is signalled by raising the KeyboardInterrupt exception.

선택한 예외를 처리하는 프로그램을 작성할 수 있습니다. 다음 예를 보세요. 이 예는 사용자에게 유효한 정수가 입력될 때까지 입력을 요청하지만, 사용자가 프로그램을 중단할 수 있게 합니다(Control-C 또는 운영 체제가 지원하는 무엇이든 사용). 사용자가 생성한 인터럽트는 KeyboardInterrupt 예외를 발생시켜 신호를 보낸다는 점에 유의하세요.

```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
```

10. The try statement works as follows.

try 문은 다음과 같이 작동합니다.

11. First, the try clause (the statement(s) between the try and except keywords) is executed.

먼저, try 절(try와 except 키워드 사이의 문장(들))이 실행됩니다.

12. If no exception occurs, the except clause is skipped and execution of the try statement is finished.

예외가 발생하지 않으면 except 절은 건너뛰고 try 문의 실행이 완료됩니다.

13. If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then, if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try/except block.

try 절의 실행 중에 예외가 발생하면 절의 나머지 부분은 건너뜁니다. 그런 다음, 그 유형이 except 키워드 뒤에 명명된 예외와 일치하면 except 절이 실행되고, 그 후 try/except 블록 이후의 실행이 계속됩니다.

14. If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with an error message.

except 절에 명명된 예외와 일치하지 않는 예외가 발생하면, 이는 외부 try 문으로 전달됩니다. 처리기를 찾지 못하면 처리되지 않은 예외이며 실행은 오류 메시지와 함께 중지됩니다.

15. A try statement may have more than one except clause, to specify handlers for different exceptions. At most one handler will be executed. Handlers only handle exceptions that occur in the corresponding try clause, not in other handlers of the same try statement. An except clause may name multiple exceptions as a parenthesized tuple, for example:

try 문은 다른 예외에 대한 처리기를 지정하기 위해 하나 이상의 except 절을 가질 수 있습니다. 최대 하나의 처리기만 실행됩니다. 처리기는 해당 try 절에서 발생하는 예외만 처리하며, 동일한 try 문의 다른 처리기에서 발생하는 예외는 처리하지 않습니다. except 절은 괄호로 묶인 튜플로 여러 예외를 명명할 수 있습니다. 예를 들어:

```python
... except (RuntimeError, TypeError, NameError):
...     pass
```

16. A class in an except clause matches exceptions which are instances of the class itself or one of its derived classes (but not the other way around — an except clause listing a derived class does not match instances of its base classes). For example, the following code will print B, C, D in that order:

except 절의 클래스는 그 클래스 자체의 인스턴스이거나 그 파생 클래스 중 하나의 인스턴스인 예외와 일치합니다(그러나 그 반대는 아닙니다 - 파생 클래스를 나열하는 except 절은 기본 클래스의 인스턴스와 일치하지 않습니다). 예를 들어, 다음 코드는 B, C, D 순서로 출력합니다:

```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

17. Note that if the except clauses were reversed (with except B first), it would have printed B, B, B — the first matching except clause is triggered.

except 절이 역순이었다면(except B가 먼저), B, B, B가 출력되었을 것입니다 - 첫 번째 일치하는 except 절이 트리거됩니다.

18. When an exception occurs, it may have associated values, also known as the exception's arguments. The presence and types of the arguments depend on the exception type.

예외가 발생하면 예외 인자라고도 알려진 관련 값이 있을 수 있습니다. 인자의 존재와 유형은 예외 유형에 따라 달라집니다.

19. The except clause may specify a variable after the exception name. The variable is bound to the exception instance which typically has an args attribute that stores the arguments. For convenience, builtin exception types define \_\_str\_\_() to print all the arguments without explicitly accessing .args.

except 절은 예외 이름 뒤에 변수를 지정할 수 있습니다. 변수는 일반적으로 인자를 저장하는 args 속성을 가진 예외 인스턴스에 바인딩됩니다. 편의를 위해 내장 예외 유형은 명시적으로 .args에 접근하지 않고도 모든 인자를 출력하기 위해 \_\_str\_\_()을 정의합니다.

```python
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception type
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

20. The exception's \_\_str\_\_() output is printed as the last part ('detail') of the message for unhandled exceptions.

예외의 \_\_str\_\_() 출력은 처리되지 않은 예외에 대한 메시지의 마지막 부분('detail')으로 출력됩니다.

21. BaseException is the common base class of all exceptions. One of its subclasses, Exception, is the base class of all the non-fatal exceptions. Exceptions which are not subclasses of Exception are not typically handled, because they are used to indicate that the program should terminate. They include SystemExit which is raised by sys.exit() and KeyboardInterrupt which is raised when a user wishes to interrupt the program.

BaseException은 모든 예외의 공통 기본 클래스입니다. 그 서브클래스 중 하나인 Exception은 모든 비치명적 예외의 기본 클래스입니다. Exception의 서브클래스가 아닌 예외는 일반적으로 처리되지 않습니다. 이는 프로그램이 종료되어야 함을 나타내는 데 사용되기 때문입니다. 여기에는 sys.exit()에 의해 발생하는 SystemExit와 사용자가 프로그램을 중단하고자 할 때 발생하는 KeyboardInterrupt가 포함됩니다.

22. Exception can be used as a wildcard that catches (almost) everything. However, it is good practice to be as specific as possible with the types of exceptions that we intend to handle, and to allow any unexpected exceptions to propagate on.

Exception은 (거의) 모든 것을 잡아내는 와일드카드로 사용될 수 있습니다. 그러나 우리가 처리하려는 예외 유형을 가능한 한 구체적으로 하고 예상치 못한 예외가 계속 전파되도록 하는 것이 좋은 관행입니다.

23. The most common pattern for handling Exception is to print or log the exception and then re-raise it (allowing a caller to handle the exception as well):

Exception을 처리하는 가장 일반적인 패턴은 예외를 출력하거나 로그로 기록한 다음 다시 발생시키는 것입니다(호출자가 예외도 처리할 수 있도록):

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

24. The try … except statement has an optional else clause, which, when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception. For example:

try … except 문에는 선택적 else 절이 있으며, 이 절이 있는 경우 모든 except 절 다음에 와야 합니다. 이는 try 절이 예외를 발생시키지 않을 경우 실행되어야 하는 코드에 유용합니다. 예를 들어:

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

25. The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn't raised by the code being protected by the try … except statement.

else 절의 사용은 try 절에 추가 코드를 추가하는 것보다 낫습니다. 이는 try … except 문으로 보호되는 코드에 의해 발생하지 않은 예외를 우연히 잡는 것을 방지하기 때문입니다.

26. Exception handlers do not handle only exceptions that occur immediately in the try clause, but also those that occur inside functions that are called (even indirectly) in the try clause. For example:

예외 처리기는 try 절에서 즉시 발생하는 예외만 처리하는 것이 아니라 try 절에서 호출된(간접적으로도) 함수 내에서 발생하는 예외도 처리합니다. 예를 들어:

```python
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
```

## 8.4. Raising Exceptions

27. The raise statement allows the programmer to force a specified exception to occur. For example:

raise 문은 프로그래머가 지정된 예외를 강제로 발생시킬 수 있게 합니다. 예를 들어:

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise NameError('HiThere')
NameError: HiThere
```

28. The sole argument to raise indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from BaseException, such as Exception or one of its subclasses). If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments:

raise의 인자는 발생시킬 예외를 나타냅니다. 이는 예외 인스턴스 또는 예외 클래스(BaseException에서 파생된 클래스, 예를 들어 Exception 또는 그 서브클래스 중 하나)여야 합니다. 예외 클래스가 전달되면, 인자 없이 생성자를 호출하여 암시적으로 인스턴스화됩니다:

```python
raise ValueError  # shorthand for 'raise ValueError()'
```

29. If you need to determine whether an exception was raised but don't intend to handle it, a simpler form of the raise statement allows you to re-raise the exception:

예외가 발생했는지 확인해야 하지만 처리할 의도가 없는 경우, 더 간단한 형태의 raise 문을 사용하여 예외를 다시 발생시킬 수 있습니다:

```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise NameError('HiThere')
NameError: HiThere
```

## 8.5. Exception Chaining

30. If an unhandled exception occurs inside an except section, it will have the exception being handled attached to it and included in the error message:

except 섹션 내에서 처리되지 않은 예외가 발생하면, 처리 중인 예외가 연결되어 오류 메시지에 포함됩니다:

```python
>>> try:
...     open("database.sqlite")
... except OSError:
...     raise RuntimeError("unable to handle error")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    open("database.sqlite")
    ~~~~^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError("unable to handle error")
RuntimeError: unable to handle error
```

31. To indicate that an exception is a direct consequence of another, the raise statement allows an optional from clause:

예외가 다른 예외의 직접적인 결과임을 나타내기 위해, raise 문은 선택적 from 절을 허용합니다:

```python
# exc must be exception instance or None.
raise RuntimeError from exc
```

32. This can be useful when you are transforming exceptions. For example:

이는 예외를 변환할 때 유용할 수 있습니다. 예를 들어:

```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    func()
    ~~~~^^
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError('Failed to open database') from exc
RuntimeError: Failed to open database
```

33. It also allows disabling automatic exception chaining using the from None idiom:

또한 from None 관용구를 사용하여 자동 예외 체이닝을 비활성화할 수 있습니다:

```python
>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError from None
RuntimeError
```

34. For more information about chaining mechanics, see Built-in Exceptions.

체이닝 메커니즘에 대한 자세한 내용은 내장 예외를 참조하세요.

## 8.6. User-defined Exceptions

35. Programs may name their own exceptions by creating a new exception class (see Classes for more about Python classes). Exceptions should typically be derived from the Exception class, either directly or indirectly.

프로그램은 새로운 예외 클래스를 생성하여 자체 예외의 이름을 지정할 수 있습니다(파이썬 클래스에 대한 자세한 내용은 클래스를 참조하세요). 예외는 일반적으로 Exception 클래스에서 직접 또는 간접적으로 파생되어야 합니다.

36. Exception classes can be defined which do anything any other class can do, but are usually kept simple, often only offering a number of attributes that allow information about the error to be extracted by handlers for the exception.

예외 클래스는 다른 클래스가 할 수 있는 모든 것을 할 수 있도록 정의될 수 있지만, 일반적으로 간단하게 유지되며, 종종 예외 처리기가 오류에 대한 정보를 추출할 수 있는 여러 속성만 제공합니다.

37. Most exceptions are defined with names that end in "Error", similar to the naming of the standard exceptions.

대부분의 예외는 표준 예외의 명명과 유사하게 "Error"로 끝나는 이름으로 정의됩니다.

38. Many standard modules define their own exceptions to report errors that may occur in functions they define.

많은 표준 모듈은 그들이 정의한 함수에서 발생할 수 있는 오류를 보고하기 위해 자신만의 예외를 정의합니다.

## 8.7. Defining Clean-up Actions

39. The try statement has another optional clause which is intended to define clean-up actions that must be executed under all circumstances. For example:

try 문에는 모든 상황에서 실행되어야 하는 정리 작업을 정의하기 위한 또 다른 선택적 절이 있습니다. 예를 들어:

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise KeyboardInterrupt
KeyboardInterrupt
```

40. If a finally clause is present, the finally clause will execute as the last task before the try statement completes. The finally clause runs whether or not the try statement produces an exception. The following points discuss more complex cases when an exception occurs:

finally 절이 있는 경우, finally 절은 try 문이 완료되기 전의 마지막 작업으로 실행됩니다. finally 절은 try 문이 예외를 생성하든 말든 실행됩니다. 다음 요점은 예외가 발생할 때 더 복잡한 경우를 논의합니다:

41. If an exception occurs during execution of the try clause, the exception may be handled by an except clause. If the exception is not handled by an except clause, the exception is re-raised after the finally clause has been executed.

try 절의 실행 중에 예외가 발생하면, 예외는 except 절에 의해 처리될 수 있습니다. 예외가 except 절에 의해 처리되지 않으면, finally 절이 실행된 후 예외가 다시 발생합니다.

42. An exception could occur during execution of an except or else clause. Again, the exception is re-raised after the finally clause has been executed.

except 또는 else 절의 실행 중에 예외가 발생할 수 있습니다. 다시 말해, finally 절이 실행된 후 예외가 다시 발생합니다.

43. If the finally clause executes a break, continue or return statement, exceptions are not re-raised.

finally 절이 break, continue 또는 return 문을 실행하면 예외가 다시 발생하지 않습니다.

44. If the try statement reaches a break, continue or return statement, the finally clause will execute just prior to the break, continue or return statement's execution.

try 문이 break, continue 또는 return 문에 도달하면, finally 절은 break, continue 또는 return 문의 실행 직전에 실행됩니다.

45. If a finally clause includes a return statement, the returned value will be the one from the finally clause's return statement, not the value from the try clause's return statement.

finally 절이 return 문을 포함하는 경우, 반환된 값은 try 절의 return 문의 값이 아닌 finally 절의 return 문의 값이 됩니다.

46. For example:

예를 들어:

```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False
```

47. A more complicated example:

더 복잡한 예:

```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    divide("2", "1")
    ~~~~~~^^^^^^^^^^
  File "<stdin>", line 3, in divide
    result = x / y
             ~~^~~
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

48. As you can see, the finally clause is executed in any event. The TypeError raised by dividing two strings is not handled by the except clause and therefore re-raised after the finally clause has been executed.

보시다시피, finally 절은 어떤 경우에도 실행됩니다. 두 문자열을 나누어 발생한 TypeError는 except 절에서 처리되지 않으므로 finally 절이 실행된 후 다시 발생합니다.

49. In real world applications, the finally clause is useful for releasing external resources (such as files or network connections), regardless of whether the use of the resource was successful.

실제 애플리케이션에서, finally 절은 리소스 사용이 성공적이었는지 여부에 관계없이 외부 리소스(예: 파일 또는 네트워크 연결)를 해제하는 데 유용합니다.

## 8.8. Predefined Clean-up Actions

50. Some objects define standard clean-up actions to be undertaken when the object is no longer needed, regardless of whether or not the operation using the object succeeded or failed. Look at the following example, which tries to open a file and print its contents to the screen.

일부 객체는 객체를 사용한 작업이 성공했는지 실패했는지에 관계없이 객체가 더 이상 필요하지 않을 때 수행할 표준 정리 작업을 정의합니다. 파일을 열고 그 내용을 화면에 출력하려는 다음 예를 살펴보세요.

```python
for line in open("myfile.txt"):
    print(line, end="")
```

51. The problem with this code is that it leaves the file open for an indeterminate amount of time after this part of the code has finished executing. This is not an issue in simple scripts, but can be a problem for larger applications. The with statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly.

이 코드의 문제는 코드의 이 부분이 실행을 마친 후에도 파일을 무기한 열어 둔다는 것입니다. 이는 간단한 스크립트에서는 문제가 되지 않지만, 더 큰 애플리케이션에서는 문제가 될 수 있습니다. with 문은 파일과 같은 객체가 항상 신속하고 올바르게 정리되도록 하는 방식으로 사용될 수 있게 합니다.

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

52. After the statement is executed, the file f is always closed, even if a problem was encountered while processing the lines. Objects which, like files, provide predefined clean-up actions will indicate this in their documentation.

문장이 실행된 후, 파일 f는 항상 닫힙니다. 라인 처리 중에 문제가 발생했더라도 마찬가지입니다. 파일과 같이 미리 정의된 정리 작업을 제공하는 객체는 이를 문서에 표시합니다.

## 8.9. Raising and Handling Multiple Unrelated Exceptions

53. There are situations where it is necessary to report several exceptions that have occurred. This is often the case in concurrency frameworks, when several tasks may have failed in parallel, but there are also other use cases where it is desirable to continue execution and collect multiple errors rather than raise the first exception.

여러 예외가 발생했음을 보고해야 하는 상황이 있습니다. 이는 종종 동시성 프레임워크에서, 여러 작업이 병렬로 실패했을 수 있는 경우에 해당하지만, 첫 번째 예외를 발생시키기보다는 실행을 계속하고 여러 오류를 수집하는 것이 바람직한 다른 사용 사례도 있습니다.

54. The builtin ExceptionGroup wraps a list of exception instances so that they can be raised together. It is an exception itself, so it can be caught like any other exception.

내장된 ExceptionGroup은 예외 인스턴스의 목록을 감싸서 함께 발생시킬 수 있도록 합니다. 이것은 그 자체로 예외이므로, 다른 예외처럼 잡을 수 있습니다.

```python
>>> def f():
...     excs = [OSError('error 1'), SystemError('error 2')]
...     raise ExceptionGroup('there were problems', excs)
...
>>> f()
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |     f()
  |     ~^^
  |   File "<stdin>", line 3, in f
  |     raise ExceptionGroup('there were problems', excs)
  | ExceptionGroup: there were problems (2 sub-exceptions)
  +-+---------------- 1 ----------------
    | OSError: error 1
    +---------------- 2 ----------------
    | SystemError: error 2
    +------------------------------------
>>> try:
...     f()
... except Exception as e:
...     print(f'caught {type(e)}: e')
...
caught <class 'ExceptionGroup'>: e
```

55. By using except* instead of except, we can selectively handle only the exceptions in the group that match a certain type. In the following example, which shows a nested exception group, each except* clause extracts from the group exceptions of a certain type while letting all other exceptions propagate to other clauses and eventually to be reraised.

except 대신 except*를 사용하여, 그룹 내에서 특정 유형과 일치하는 예외만 선택적으로 처리할 수 있습니다. 중첩된 예외 그룹을 보여주는 다음 예에서, 각 except* 절은 그룹에서 특정 유형의 예외를 추출하면서 다른 모든 예외가 다른 절로 전파되도록 하고 결국 다시 발생됩니다.

```python
>>> def f():
...     raise ExceptionGroup(
...         "group1",
...         [
...             OSError(1),
...             SystemError(2),
...             ExceptionGroup(
...                 "group2",
...                 [
...                     OSError(3),
...                     RecursionError(4)
...                 ]
...             )
...         ]
...     )
...
>>> try:
...     f()
... except* OSError as e:
...     print("There were OSErrors")
... except* SystemError as e:
...     print("There were SystemErrors")
...
There were OSErrors
There were SystemErrors
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 2, in <module>
  |     f()
  |     ~^^
  |   File "<stdin>", line 2, in f
  |     raise ExceptionGroup(
  |     ...<12 lines>...
  |     )
  | ExceptionGroup: group1 (1 sub-exception)
  +-+---------------- 1 ----------------
    | ExceptionGroup: group2 (1 sub-exception)
    +-+---------------- 1 ----------------
      | RecursionError: 4
      +------------------------------------
```

56. Note that the exceptions nested in an exception group must be instances, not types. This is because in practice the exceptions would typically be ones that have already been raised and caught by the program, along the following pattern:

예외 그룹에 중첩된 예외는 유형이 아니라 인스턴스여야 합니다. 이는 실제로 예외가 일반적으로 프로그램에 의해 이미 발생하고 잡힌 것이기 때문입니다. 다음 패턴을 따릅니다:

```python
>>> excs = []
>>> for test in tests:
...     try:
...         test.run()
...     except Exception as e:
...         excs.append(e)
...
>>> if excs:
...    raise ExceptionGroup("Test Failures", excs)
...
```

## 8.10. Enriching Exceptions with Notes

57. When an exception is created in order to be raised, it is usually initialized with information that describes the error that has occurred. There are cases where it is useful to add information after the exception was caught. For this purpose, exceptions have a method add_note(note) that accepts a string and adds it to the exception's notes list. The standard traceback rendering includes all notes, in the order they were added, after the exception.

예외가 발생하기 위해 생성될 때, 일반적으로 발생한 오류를 설명하는 정보로 초기화됩니다. 예외가 잡힌 후에 정보를 추가하는 것이 유용한 경우가 있습니다. 이를 위해, 예외에는 문자열을 받아 예외의 노트 목록에 추가하는 add_note(note) 메서드가 있습니다. 표준 트레이스백 렌더링은 예외 후에 추가된 순서대로 모든 노트를 포함합니다.

```python
>>> try:
...     raise TypeError('bad type')
... except Exception as e:
...     e.add_note('Add some information')
...     e.add_note('Add some more information')
...     raise
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise TypeError('bad type')
TypeError: bad type
Add some information
Add some more information
```

58. For example, when collecting exceptions into an exception group, we may want to add context information for the individual errors. In the following each exception in the group has a note indicating when this error has occurred.

예를 들어, 예외 그룹으로 예외를 수집할 때, 개별 오류에 대한 컨텍스트 정보를 추가하고 싶을 수 있습니다. 다음에서 그룹의 각 예외에는 이 오류가 발생한 시기를 나타내는 노트가 있습니다.

```python
>>> def f():
...     raise OSError('operation failed')
...
>>> excs = []
>>> for i in range(3):
...     try:
...         f()
...     except Exception as e:
...         e.add_note(f'Happened in Iteration {i+1}')
...         excs.append(e)
...
>>> raise ExceptionGroup('We have some problems', excs)
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |     raise ExceptionGroup('We have some problems', excs)
  | ExceptionGroup: We have some problems (3 sub-exceptions)
  +-+---------------- 1 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |     f()
    |     ~^^
    |   File "<stdin>", line 2, in f
    |     raise OSError('operation failed')
    | OSError: operation failed
    | Happened in Iteration 1
    +---------------- 2 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |     f()
    |     ~^^
    |   File "<stdin>", line 2, in f
    |     raise OSError('operation failed')
    | OSError: operation failed
    | Happened in Iteration 2
    +---------------- 3 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |     f()
    |     ~^^
    |   File "<stdin>", line 2, in f
    |     raise OSError('operation failed')
    | OSError: operation failed
    | Happened in Iteration 3
    +------------------------------------
```
