# 4. Execution model

# 4. 실행 모델

## 4.1. Structure of a program

A Python program is constructed from code blocks. A block is a piece of Python program text that is executed as a unit. The following are blocks: a module, a function body, and a class definition. Each command typed interactively is a block. A script file (a file given as standard input to the interpreter or specified as a command line argument to the interpreter) is a code block. A script command (a command specified on the interpreter command line with the -c option) is a code block. A module run as a top level script (as module __main__) from the command line using a -m argument is also a code block. The string argument passed to the built-in functions eval() and exec() is a code block.

A code block is executed in an execution frame. A frame contains some administrative information (used for debugging) and determines where and how execution continues after the code block's execution has completed.

## 4.1. 프로그램의 구조

파이썬 프로그램은 코드 블록으로 구성됩니다. 블록은 하나의 단위로 실행되는 파이썬 프로그램 텍스트의 일부입니다. 다음은 블록의 예입니다: 모듈, 함수 본문, 클래스 정의. 대화형으로 입력된 각 명령은 블록입니다. 스크립트 파일(인터프리터에 표준 입력으로 제공되거나 인터프리터 명령줄 인수로 지정된 파일)은 코드 블록입니다. 스크립트 명령(인터프리터 명령줄에서 -c 옵션으로 지정된 명령)은 코드 블록입니다. 명령줄에서 -m 인수를 사용하여 최상위 스크립트로 실행되는 모듈(모듈 __main__로)도 코드 블록입니다. 내장 함수 eval()과 exec()에 전달된 문자열 인수는 코드 블록입니다.

코드 블록은 실행 프레임에서 실행됩니다. 프레임은 관리 정보(디버깅에 사용됨)를 포함하고 코드 블록의 실행이 완료된 후 실행이 어디서 어떻게 계속되는지 결정합니다.

## 4.2. Naming and binding

## 4.2. 이름 지정 및 바인딩

### 4.2.1. Binding of names

Names refer to objects. Names are introduced by name binding operations.

The following constructs bind names:

- formal parameters to functions,
- class definitions,
- function definitions,
- assignment expressions,
- targets that are identifiers if occurring in an assignment:
  - for loop header,
  - after as in a with statement, except clause, except* clause, or in the as-pattern in structural pattern matching,
  - in a capture pattern in structural pattern matching
- import statements.
- type statements.
- type parameter lists.

The import statement of the form from ... import * binds all names defined in the imported module, except those beginning with an underscore. This form may only be used at the module level.

A target occurring in a del statement is also considered bound for this purpose (though the actual semantics are to unbind the name).

Each assignment or import statement occurs within a block defined by a class or function definition or at the module level (the top-level code block).

If a name is bound in a block, it is a local variable of that block, unless declared as nonlocal or global. If a name is bound at the module level, it is a global variable. (The variables of the module code block are local and global.) If a variable is used in a code block but not defined there, it is a free variable.

Each occurrence of a name in the program text refers to the binding of that name established by the following name resolution rules.

### 4.2.1. 이름 바인딩

이름은 객체를 참조합니다. 이름은 이름 바인딩 작업을 통해 도입됩니다.

다음 구문은 이름을 바인딩합니다:

- 함수에 대한 형식 매개변수,
- 클래스 정의,
- 함수 정의,
- 할당 표현식,
- 할당에서 발생하는 식별자인 대상:
  - for 루프 헤더,
  - with 문, except 절, except* 절의 as 뒤에 오는 것, 또는 구조적 패턴 매칭의 as-패턴에서,
  - 구조적 패턴 매칭의 캡처 패턴에서
- import 문.
- type 문.
- 타입 매개변수 목록.

from ... import * 형식의 import 문은 밑줄로 시작하는 것을 제외하고 가져온 모듈에 정의된 모든 이름을 바인딩합니다. 이 형식은 모듈 수준에서만 사용할 수 있습니다.

del 문에서 발생하는 대상도 이 목적으로 바인딩된 것으로 간주됩니다(실제 의미는 이름을 바인딩 해제하는 것이지만).

각 할당 또는 import 문은 클래스나 함수 정의에 의해 정의된 블록 내에서 또는 모듈 수준(최상위 코드 블록)에서 발생합니다.

이름이 블록에 바인딩된 경우, nonlocal 또는 global로 선언되지 않는 한 해당 블록의 지역 변수입니다. 이름이 모듈 수준에서 바인딩된 경우 전역 변수입니다. (모듈 코드 블록의 변수는 지역 및 전역입니다.) 변수가 코드 블록에서 사용되지만 거기에 정의되지 않은 경우, 자유 변수입니다.

프로그램 텍스트에서 이름의 각 출현은 다음 이름 확인 규칙에 의해 설정된 해당 이름의 바인딩을 참조합니다.

### 4.2.2. Resolution of names

A scope defines the visibility of a name within a block. If a local variable is defined in a block, its scope includes that block. If the definition occurs in a function block, the scope extends to any blocks contained within the defining one, unless a contained block introduces a different binding for the name.

When a name is used in a code block, it is resolved using the nearest enclosing scope. The set of all such scopes visible to a code block is called the block's environment.

When a name is not found at all, a NameError exception is raised. If the current scope is a function scope, and the name refers to a local variable that has not yet been bound to a value at the point where the name is used, an UnboundLocalError exception is raised. UnboundLocalError is a subclass of NameError.

If a name binding operation occurs anywhere within a code block, all uses of the name within the block are treated as references to the current block. This can lead to errors when a name is used within a block before it is bound. This rule is subtle. Python lacks declarations and allows name binding operations to occur anywhere within a code block. The local variables of a code block can be determined by scanning the entire text of the block for name binding operations. See the FAQ entry on UnboundLocalError for examples.

If the global statement occurs within a block, all uses of the names specified in the statement refer to the bindings of those names in the top-level namespace. Names are resolved in the top-level namespace by searching the global namespace, i.e. the namespace of the module containing the code block, and the builtins namespace, the namespace of the module builtins. The global namespace is searched first. If the names are not found there, the builtins namespace is searched next. If the names are also not found in the builtins namespace, new variables are created in the global namespace. The global statement must precede all uses of the listed names.

The global statement has the same scope as a name binding operation in the same block. If the nearest enclosing scope for a free variable contains a global statement, the free variable is treated as a global.

The nonlocal statement causes corresponding names to refer to previously bound variables in the nearest enclosing function scope. SyntaxError is raised at compile time if the given name does not exist in any enclosing function scope. Type parameters cannot be rebound with the nonlocal statement.

The namespace for a module is automatically created the first time a module is imported. The main module for a script is always called __main__.

Class definition blocks and arguments to exec() and eval() are special in the context of name resolution. A class definition is an executable statement that may use and define names. These references follow the normal rules for name resolution with an exception that unbound local variables are looked up in the global namespace. The namespace of the class definition becomes the attribute dictionary of the class. The scope of names defined in a class block is limited to the class block; it does not extend to the code blocks of methods. This includes comprehensions and generator expressions, but it does not include annotation scopes, which have access to their enclosing class scopes. This means that the following will fail:

```python
class A:
    a = 42
    b = list(a + i for i in range(10))
```

However, the following will succeed:

```python
class A:
    type Alias = Nested
    class Nested: pass

print(A.Alias.__value__)  # <type 'A.Nested'>
```

### 4.2.2. 이름 해결

스코프는 블록 내에서 이름의 가시성을 정의합니다. 지역 변수가 블록에 정의된 경우, 해당 스코프는 그 블록을 포함합니다. 정의가 함수 블록에서 발생하는 경우, 스코프는 포함된 블록이 해당 이름에 대해 다른 바인딩을 도입하지 않는 한 정의하는 블록 내에 포함된 모든 블록으로 확장됩니다.

이름이 코드 블록에서 사용될 때, 가장 가까운 둘러싸는 스코프를 사용하여 해결됩니다. 코드 블록에 표시되는 모든 이러한 스코프의 집합을 블록의 환경이라고 합니다.

이름이 전혀 발견되지 않으면 NameError 예외가 발생합니다. 현재 스코프가 함수 스코프이고 이름이 사용되는 시점에 아직 값에 바인딩되지 않은 지역 변수를 참조하는 경우 UnboundLocalError 예외가 발생합니다. UnboundLocalError는 NameError의 하위 클래스입니다.

이름 바인딩 작업이 코드 블록 내의 어디에서든 발생하면 블록 내의 이름의 모든 사용은 현재 블록에 대한 참조로 취급됩니다. 이는 이름이 바인딩되기 전에 블록 내에서 사용될 때 오류를 일으킬 수 있습니다. 이 규칙은 미묘합니다. 파이썬은 선언이 없고 코드 블록 내 어디서나 이름 바인딩 작업이 발생할 수 있습니다. 코드 블록의 지역 변수는 이름 바인딩 작업에 대한 블록의 전체 텍스트를 스캔하여 결정할 수 있습니다. 예제는 UnboundLocalError에 관한 FAQ 항목을 참조하십시오.

global 문이 블록 내에서 발생하면 문에 지정된 이름의 모든 사용은 최상위 네임스페이스에 있는 해당 이름의 바인딩을 참조합니다. 이름은 코드 블록을 포함하는 모듈의 네임스페이스인 전역 네임스페이스와 builtins 모듈의 네임스페이스인 builtins 네임스페이스를 검색하여 최상위 네임스페이스에서 해결됩니다. 먼저 전역 네임스페이스를 검색합니다. 이름이 거기에서 발견되지 않으면 다음으로 builtins 네임스페이스를 검색합니다. 이름이 builtins 네임스페이스에서도 발견되지 않으면 전역 네임스페이스에 새 변수가 생성됩니다. global 문은 나열된 이름의 모든 사용보다 앞에 와야 합니다.

global 문은 동일한 블록의 이름 바인딩 작업과 동일한 스코프를 갖습니다. 자유 변수에 대한 가장 가까운 둘러싸는 스코프에 global 문이 포함되어 있으면 자유 변수는 전역으로 취급됩니다.

nonlocal 문은 해당 이름이 가장 가까운 둘러싸는 함수 스코프에서 이전에 바인딩된 변수를 참조하도록 합니다. 주어진 이름이 둘러싸는 함수 스코프에 존재하지 않으면 컴파일 시 SyntaxError가 발생합니다. 타입 매개변수는 nonlocal 문으로 다시 바인딩할 수 없습니다.

모듈의 네임스페이스는 모듈이 처음 가져올 때 자동으로 생성됩니다. 스크립트의 메인 모듈은 항상 __main__이라고 합니다.

클래스 정의 블록과 exec() 및 eval()에 대한 인수는 이름 해결 맥락에서 특별합니다. 클래스 정의는 이름을 사용하고 정의할 수 있는 실행 가능한 문입니다. 이러한 참조는 바인딩되지 않은 지역 변수가 전역 네임스페이스에서 조회된다는 예외와 함께 이름 해결에 대한 일반 규칙을 따릅니다. 클래스 정의의 네임스페이스는 클래스의 속성 사전이 됩니다. 클래스 블록에 정의된 이름의 스코프는 클래스 블록으로 제한됩니다. 메서드의 코드 블록으로 확장되지 않습니다. 여기에는 컴프리헨션과 제너레이터 표현식이 포함되지만, 둘러싸는 클래스 스코프에 접근할 수 있는 어노테이션 스코프는 포함되지 않습니다. 이는 다음이 실패한다는 것을 의미합니다:

```python
class A:
    a = 42
    b = list(a + i for i in range(10))
```

그러나 다음은 성공합니다:

```python
class A:
    type Alias = Nested
    class Nested: pass

print(A.Alias.__value__)  # <type 'A.Nested'>
```

### 4.2.3. Annotation scopes

Type parameter lists and type statements introduce annotation scopes, which behave mostly like function scopes, but with some exceptions discussed below. Annotations currently do not use annotation scopes, but they are expected to use annotation scopes in Python 3.13 when PEP 649 is implemented.

Annotation scopes are used in the following contexts:

- Type parameter lists for generic type aliases.
- Type parameter lists for generic functions. A generic function's annotations are executed within the annotation scope, but its defaults and decorators are not.
- Type parameter lists for generic classes. A generic class's base classes and keyword arguments are executed within the annotation scope, but its decorators are not.
- The bounds, constraints, and default values for type parameters (lazily evaluated).
- The value of type aliases (lazily evaluated).

Annotation scopes differ from function scopes in the following ways:

- Annotation scopes have access to their enclosing class namespace. If an annotation scope is immediately within a class scope, or within another annotation scope that is immediately within a class scope, the code in the annotation scope can use names defined in the class scope as if it were executed directly within the class body. This contrasts with regular functions defined within classes, which cannot access names defined in the class scope.
- Expressions in annotation scopes cannot contain yield, yield from, await, or := expressions. (These expressions are allowed in other scopes contained within the annotation scope.)
- Names defined in annotation scopes cannot be rebound with nonlocal statements in inner scopes. This includes only type parameters, as no other syntactic elements that can appear within annotation scopes can introduce new names.
- While annotation scopes have an internal name, that name is not reflected in the qualified name of objects defined within the scope. Instead, the __qualname__ of such objects is as if the object were defined in the enclosing scope.

Added in version 3.12: Annotation scopes were introduced in Python 3.12 as part of PEP 695.

Changed in version 3.13: Annotation scopes are also used for type parameter defaults, as introduced by PEP 696.

### 4.2.3. 어노테이션 스코프

타입 매개변수 목록과 타입 문은 주로 함수 스코프처럼 작동하지만 아래에서 논의된 일부 예외가 있는 어노테이션 스코프를 도입합니다. 현재 어노테이션은 어노테이션 스코프를 사용하지 않지만 PEP 649가 구현되는 Python 3.13에서는 어노테이션 스코프를 사용할 것으로 예상됩니다.

어노테이션 스코프는 다음 컨텍스트에서 사용됩니다:

- 제네릭 타입 별칭을 위한 타입 매개변수 목록.
- 제네릭 함수를 위한 타입 매개변수 목록. 제네릭 함수의 어노테이션은 어노테이션 스코프 내에서 실행되지만 기본값과 데코레이터는 그렇지 않습니다.
- 제네릭 클래스를 위한 타입 매개변수 목록. 제네릭 클래스의 기본 클래스와 키워드 인수는 어노테이션 스코프 내에서 실행되지만 데코레이터는 그렇지 않습니다.
- 타입 매개변수의 경계, 제약 조건 및 기본값(지연 평가됨).
- 타입 별칭의 값(지연 평가됨).

어노테이션 스코프는 다음과 같은 방식으로 함수 스코프와 다릅니다:

- 어노테이션 스코프는 둘러싸는 클래스 네임스페이스에 접근할 수 있습니다. 어노테이션 스코프가 클래스 스코프 내에 바로 있거나, 클래스 스코프 내에 바로 있는 다른 어노테이션 스코프 내에 있는 경우, 어노테이션 스코프의 코드는 마치 클래스 본문 내에서 직접 실행된 것처럼 클래스 스코프에 정의된 이름을 사용할 수 있습니다. 이는 클래스 스코프에 정의된 이름에 접근할 수 없는 클래스 내에 정의된 일반 함수와 대조됩니다.
- 어노테이션 스코프의 표현식에는 yield, yield from, await 또는 := 표현식이 포함될 수 없습니다. (이러한 표현식은 어노테이션 스코프 내에 포함된 다른 스코프에서는 허용됩니다.)
- 어노테이션 스코프에 정의된 이름은 내부 스코프의 nonlocal 문으로 다시 바인딩할 수 없습니다. 여기에는 타입 매개변수만 포함되며, 어노테이션 스코프 내에 나타날 수 있는 다른 구문 요소는 새 이름을 도입할 수 없습니다.
- 어노테이션 스코프에는 내부 이름이 있지만 해당 이름은 스코프 내에 정의된 객체의 정규화된 이름에 반영되지 않습니다. 대신, 그러한 객체의 __qualname__은 마치 객체가 둘러싸는 스코프에 정의된 것처럼 됩니다.

3.12 버전에서 추가됨: 어노테이션 스코프는 PEP 695의 일부로 Python 3.12에 도입되었습니다.

3.13 버전에서 변경됨: PEP 696에서 도입된 대로 어노테이션 스코프는 타입 매개변수 기본값에도 사용됩니다.

### 4.2.4. Lazy evaluation

The values of type aliases created through the type statement are lazily evaluated. The same applies to the bounds, constraints, and default values of type variables created through the type parameter syntax. This means that they are not evaluated when the type alias or type variable is created. Instead, they are only evaluated when doing so is necessary to resolve an attribute access.

Example:

```python
>>>
type Alias = 1/0
Alias.__value__
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
def func[T: 1/0](): pass
T = func.__type_params__[0]
T.__bound__
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
```

Here the exception is raised only when the __value__ attribute of the type alias or the __bound__ attribute of the type variable is accessed.

This behavior is primarily useful for references to types that have not yet been defined when the type alias or type variable is created. For example, lazy evaluation enables creation of mutually recursive type aliases:

```python
from typing import Literal

type SimpleExpr = int | Parenthesized
type Parenthesized = tuple[Literal["("], Expr, Literal[")"]]
type Expr = SimpleExpr | tuple[SimpleExpr, Literal["+", "-"], Expr]
```

Lazily evaluated values are evaluated in annotation scope, which means that names that appear inside the lazily evaluated value are looked up as if they were used in the immediately enclosing scope.

Added in version 3.12.

### 4.2.4. 지연 평가

type 문을 통해 생성된 타입 별칭의 값은 지연 평가됩니다. 동일하게 타입 매개변수 구문을 통해 생성된 타입 변수의 경계, 제약 조건 및 기본값에도 적용됩니다. 이는 타입 별칭이나 타입 변수가 생성될 때 평가되지 않음을 의미합니다. 대신, 속성 접근을 해결하는 데 필요한 경우에만 평가됩니다.

예:

```python
>>>
type Alias = 1/0
Alias.__value__
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
def func[T: 1/0](): pass
T = func.__type_params__[0]
T.__bound__
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
```

여기서 예외는 타입 별칭의 __value__ 속성이나 타입 변수의 __bound__ 속성에 접근할 때만 발생합니다.

이 동작은 주로 타입 별칭이나 타입 변수가 생성될 때 아직 정의되지 않은 타입에 대한 참조에 유용합니다. 예를 들어, 지연 평가를 통해 상호 재귀적인 타입 별칭을 생성할 수 있습니다:

```python
from typing import Literal

type SimpleExpr = int | Parenthesized
type Parenthesized = tuple[Literal["("], Expr, Literal[")"]]
type Expr = SimpleExpr | tuple[SimpleExpr, Literal["+", "-"], Expr]
```

지연 평가된 값은 어노테이션 스코프에서 평가되며, 이는 지연 평가된 값 내부에 나타나는 이름이 마치 바로 둘러싸는 스코프에서 사용된 것처럼 조회됨을 의미합니다.

3.12 버전에서 추가됨.

### 4.2.5. Builtins and restricted execution

CPython implementation detail: Users should not touch __builtins__; it is strictly an implementation detail. Users wanting to override values in the builtins namespace should import the builtins module and modify its attributes appropriately.

The builtins namespace associated with the execution of a code block is actually found by looking up the name __builtins__ in its global namespace; this should be a dictionary or a module (in the latter case the module's dictionary is used). By default, when in the __main__ module, __builtins__ is the built-in module builtins; when in any other module, __builtins__ is an alias for the dictionary of the builtins module itself.

### 4.2.5. 내장 및 제한된 실행

CPython 구현 세부 사항: 사용자는 __builtins__를 건드리지 말아야 합니다. 이는 엄격한 구현 세부 사항입니다. builtins 네임스페이스의 값을 재정의하려는 사용자는 builtins 모듈을 가져와 해당 속성을 적절히 수정해야 합니다.

코드 블록 실행과 관련된 builtins 네임스페이스는 실제로 글로벌 네임스페이스에서 __builtins__ 이름을 조회하여 찾습니다. 이는 사전이나 모듈이어야 합니다(후자의 경우 모듈의 사전이 사용됨). 기본적으로 __main__ 모듈에 있을 때 __builtins__는 내장 모듈 builtins입니다. 다른 모듈에 있을 때 __builtins__는 builtins 모듈 자체의 사전에 대한 별칭입니다.

### 4.2.6. Interaction with dynamic features

Name resolution of free variables occurs at runtime, not at compile time. This means that the following code will print 42:

```python
i = 10
def f():
    print(i)
i = 42
f()
```

The eval() and exec() functions do not have access to the full environment for resolving names. Names may be resolved in the local and global namespaces of the caller. Free variables are not resolved in the nearest enclosing namespace, but in the global namespace. [1] The exec() and eval() functions have optional arguments to override the global and local namespace. If only one namespace is specified, it is used for both.

### 4.2.6. 동적 기능과의 상호 작용

자유 변수의 이름 해결은 컴파일 시간이 아닌 런타임에 발생합니다. 이는 다음 코드가 42를 출력한다는 것을 의미합니다:

```python
i = 10
def f():
    print(i)
i = 42
f()
```

eval() 및 exec() 함수는 이름을 해결하기 위한 전체 환경에 접근할 수 없습니다. 이름은 호출자의 지역 및 전역 네임스페이스에서 해결될 수 있습니다. 자유 변수는 가장 가까운 둘러싸는 네임스페이스가 아닌 전역 네임스페이스에서 해결됩니다. [1] exec() 및 eval() 함수는 전역 및 지역 네임스페이스를 재정의하기 위한 선택적 인수를 가집니다. 하나의 네임스페이스만 지정된 경우, 두 가지 모두에 사용됩니다.

## 4.3. Exceptions

Exceptions are a means of breaking out of the normal flow of control of a code block in order to handle errors or other exceptional conditions. An exception is raised at the point where the error is detected; it may be handled by the surrounding code block or by any code block that directly or indirectly invoked the code block where the error occurred.

The Python interpreter raises an exception when it detects a run-time error (such as division by zero). A Python program can also explicitly raise an exception with the raise statement. Exception handlers are specified with the try … except statement. The finally clause of such a statement can be used to specify cleanup code which does not handle the exception, but is executed whether an exception occurred or not in the preceding code.

Python uses the "termination" model of error handling: an exception handler can find out what happened and continue execution at an outer level, but it cannot repair the cause of the error and retry the failing operation (except by re-entering the offending piece of code from the top).

When an exception is not handled at all, the interpreter terminates execution of the program, or returns to its interactive main loop. In either case, it prints a stack traceback, except when the exception is SystemExit.

Exceptions are identified by class instances. The except clause is selected depending on the class of the instance: it must reference the class of the instance or a non-virtual base class thereof. The instance can be received by the handler and can carry additional information about the exceptional condition.

> **Note:** Exception messages are not part of the Python API. Their contents may change from one version of Python to the next without warning and should not be relied on by code which will run under multiple versions of the interpreter.

See also the description of the try statement in section The try statement and raise statement in section The raise statement.

## 4.3. 예외

예외는 오류나 다른 예외적인 조건을 처리하기 위해 코드 블록의 정상적인 제어 흐름에서 벗어나는 수단입니다. 예외는 오류가 감지된 지점에서 발생합니다. 이는 주변 코드 블록이나 오류가 발생한 코드 블록을 직접 또는 간접적으로 호출한 코드 블록에 의해 처리될 수 있습니다.

파이썬 인터프리터는 런타임 오류(예: 0으로 나누기)를 감지할 때 예외를 발생시킵니다. 파이썬 프로그램은 raise 문으로 명시적으로 예외를 발생시킬 수도 있습니다. 예외 핸들러는 try … except 문으로 지정됩니다. 이러한 문의 finally 절은 예외를 처리하지 않지만 예외가 발생했는지 여부와 관계없이 실행되는 정리 코드를 지정하는 데 사용할 수 있습니다.

파이썬은 "종료" 모델의 오류 처리를 사용합니다: 예외 핸들러는 무슨 일이 일어났는지 알아내고 외부 수준에서 실행을 계속할 수 있지만, 오류의 원인을 수정하고 실패한 작업을 다시 시도할 수는 없습니다(문제가 있는 코드 조각을 위에서부터 다시 시작하는 경우는 제외).

예외가 전혀 처리되지 않으면 인터프리터는 프로그램 실행을 종료하거나 대화형 주 루프로 돌아갑니다. 두 경우 모두 예외가 SystemExit가 아닌 한 스택 추적을 출력합니다.

예외는 클래스 인스턴스로 식별됩니다. except 절은 인스턴스의 클래스에 따라 선택됩니다: 인스턴스의 클래스나 그 비가상 기본 클래스를 참조해야 합니다. 인스턴스는 핸들러가 받을 수 있으며 예외 상황에 대한 추가 정보를 전달할 수 있습니다.

> **참고:** 예외 메시지는 Python API의 일부가 아닙니다. 그 내용은 경고 없이 한 버전의 파이썬에서 다음 버전으로 변경될 수 있으며, 여러 버전의 인터프리터에서 실행될 코드에서 이에 의존해서는 안 됩니다.

try 문에 대한 설명은 try 문 섹션을 참조하고, raise 문에 대한 설명은 raise 문 섹션을 참조하십시오.
