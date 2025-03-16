# 9. Classes

1. Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

클래스는 데이터와 기능을 함께 묶는 수단을 제공합니다. 새 클래스를 생성하면 새로운 유형의 객체가 만들어지고, 해당 유형의 새로운 인스턴스를 만들 수 있습니다. 각 클래스 인스턴스는 상태를 유지하기 위해 속성을 가질 수 있습니다. 클래스 인스턴스는 또한 상태를 수정하기 위한 메서드(해당 클래스에 의해 정의됨)를 가질 수 있습니다.

2. Compared with other programming languages, Python's class mechanism adds classes with a minimum of new syntax and semantics. It is a mixture of the class mechanisms found in C++ and Modula-3. Python classes provide all the standard features of Object Oriented Programming: the class inheritance mechanism allows multiple base classes, a derived class can override any methods of its base class or classes, and a method can call the method of a base class with the same name. Objects can contain arbitrary amounts and kinds of data. As is true for modules, classes partake of the dynamic nature of Python: they are created at runtime, and can be modified further after creation.

다른 프로그래밍 언어와 비교할 때, 파이썬의 클래스 메커니즘은 최소한의 새로운 구문과 의미론으로 클래스를 추가합니다. C++와 Modula-3에서 찾을 수 있는 클래스 메커니즘의 혼합입니다. 파이썬 클래스는 객체 지향 프로그래밍의 모든 표준 기능을 제공합니다: 클래스 상속 메커니즘은 여러 기본 클래스를 허용하고, 파생 클래스는 그 기본 클래스나 클래스들의 어떤 메서드도 오버라이드할 수 있으며, 메서드는 같은 이름의 기본 클래스 메서드를 호출할 수 있습니다. 객체는 임의의 양과 종류의 데이터를 포함할 수 있습니다. 모듈과 마찬가지로, 클래스는 파이썬의 동적 특성을 갖습니다: 실행 시간에 생성되며, 생성 후에도 수정될 수 있습니다.

3. In C++ terminology, normally class members (including the data members) are public (except see below Private Variables), and all member functions are virtual. As in Modula-3, there are no shorthands for referencing the object's members from its methods: the method function is declared with an explicit first argument representing the object, which is provided implicitly by the call. As in Smalltalk, classes themselves are objects. This provides semantics for importing and renaming. Unlike C++ and Modula-3, built-in types can be used as base classes for extension by the user. Also, like in C++, most built-in operators with special syntax (arithmetic operators, subscripting etc.) can be redefined for class instances.

C++ 용어로, 일반적으로 클래스 멤버(데이터 멤버 포함)는 공개(아래의 비공개 변수 참조)이며, 모든 멤버 함수는 가상입니다. Modula-3와 마찬가지로, 객체의 메서드에서 객체의 멤버를 참조하기 위한 약어가 없습니다: 메서드 함수는 객체를 나타내는 명시적인 첫 번째 인수로 선언되며, 이는 호출에 의해 암시적으로 제공됩니다. Smalltalk와 마찬가지로, 클래스 자체가 객체입니다. 이는 가져오기와 이름 바꾸기를 위한 의미론을 제공합니다. C++와 Modula-3과 달리, 내장 타입은 사용자에 의한 확장을 위한 기본 클래스로 사용될 수 있습니다. 또한 C++와 같이, 특별한 구문을 가진 대부분의 내장 연산자(산술 연산자, 첨자 등)는 클래스 인스턴스를 위해 재정의될 수 있습니다.

4. (Lacking universally accepted terminology to talk about classes, I will make occasional use of Smalltalk and C++ terms. I would use Modula-3 terms, since its object-oriented semantics are closer to those of Python than C++, but I expect that few readers have heard of it.)

(클래스에 대해 이야기하기 위한 보편적으로 받아들여지는 용어가 부족하므로, 가끔 Smalltalk와 C++ 용어를 사용할 것입니다. Modula-3의 객체 지향 의미론이 C++보다 Python에 더 가깝기 때문에 Modula-3 용어를 사용하고 싶지만, 적은 독자만이 그것에 대해 들어봤을 것이라고 예상합니다.)

## 9.1. A Word About Names and Objects

5. Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object. This is known as aliasing in other languages. This is usually not appreciated on a first glance at Python, and can be safely ignored when dealing with immutable basic types (numbers, strings, tuples). However, aliasing has a possibly surprising effect on the semantics of Python code involving mutable objects such as lists, dictionaries, and most other types. This is usually used to the benefit of the program, since aliases behave like pointers in some respects. For example, passing an object is cheap since only a pointer is passed by the implementation; and if a function modifies an object passed as an argument, the caller will see the change — this eliminates the need for two different argument passing mechanisms as in Pascal.

객체는 개별성을 가지며, 여러 이름(여러 범위에서)이 동일한 객체에 바인딩될 수 있습니다. 이는 다른 언어에서는 별칭이라고 알려져 있습니다. 이는 보통 파이썬을 처음 볼 때 이해되지 않으며, 변경할 수 없는 기본 타입(숫자, 문자열, 튜플)을 다룰 때는 안전하게 무시될 수 있습니다. 그러나, 별칭은 리스트, 딕셔너리 및 대부분의 다른 타입과 같은 변경 가능한 객체를 포함하는 파이썬 코드의 의미론에 놀라운 영향을 미칠 수 있습니다. 이는 일반적으로 프로그램에 이익이 되도록 사용됩니다. 별칭은 일부 측면에서 포인터처럼 작동하기 때문입니다. 예를 들어, 구현에 의해 포인터만 전달되므로 객체 전달은 저렴합니다. 그리고, 함수가 인수로 전달된 객체를 수정하면 호출자는 그 변경을 볼 수 있습니다 — 이는 Pascal과 같이 두 가지 다른 인수 전달 메커니즘의 필요성을 제거합니다.

## 9.2. Python Scopes and Namespaces

6. Before introducing classes, I first have to tell you something about Python's scope rules. Class definitions play some neat tricks with namespaces, and you need to know how scopes and namespaces work to fully understand what's going on. Incidentally, knowledge about this subject is useful for any advanced Python programmer.

클래스를 소개하기 전에, 먼저 파이썬의 범위 규칙에 대해 알려드려야 합니다. 클래스 정의는 네임스페이스로 몇 가지 멋진 트릭을 수행하며, 무슨 일이 일어나는지 완전히 이해하려면 범위와 네임스페이스가 어떻게 작동하는지 알아야 합니다. 부수적으로, 이 주제에 대한 지식은 모든 고급 파이썬 프로그래머에게 유용합니다.

7. Let's begin with some definitions.

몇 가지 정의부터 시작합시다.

8. A namespace is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries, but that's normally not noticeable in any way (except for performance), and it may change in the future. Examples of namespaces are: the set of built-in names (containing functions such as abs(), and built-in exception names); the global names in a module; and the local names in a function invocation. In a sense the set of attributes of an object also form a namespace. The important thing to know about namespaces is that there is absolutely no relation between names in different namespaces; for instance, two different modules may both define a function maximize without confusion — users of the modules must prefix it with the module name.

네임스페이스는 이름에서 객체로의 매핑입니다. 대부분의 네임스페이스는 현재 파이썬 딕셔너리로 구현되어 있지만, 그것은 일반적으로 어떤 식으로든 눈에 띄지 않습니다(성능 외에는), 그리고 그것은 미래에 변경될 수 있습니다. 네임스페이스의 예로는: 내장 이름의 집합(abs()와 같은 함수와 내장 예외 이름을 포함); 모듈의 전역 이름; 그리고 함수 호출의 로컬 이름이 있습니다. 어떤 의미에서 객체의 속성 집합도 네임스페이스를 형성합니다. 네임스페이스에 대해 알아야 할 중요한 것은 다른 네임스페이스의 이름 사이에 절대적으로 관계가 없다는 것입니다. 예를 들어, 두 개의 다른 모듈이 혼란 없이 maximize 함수를 모두 정의할 수 있습니다 — 모듈의 사용자는 모듈 이름으로 그것을 접두어로 붙여야 합니다.

9. By the way, I use the word attribute for any name following a dot — for example, in the expression z.real, real is an attribute of the object z. Strictly speaking, references to names in modules are attribute references: in the expression modname.funcname, modname is a module object and funcname is an attribute of it. In this case there happens to be a straightforward mapping between the module's attributes and the global names defined in the module: they share the same namespace! [1]

그런데, 저는 점 뒤에 오는 모든 이름에 대해 속성이라는 단어를 사용합니다 — 예를 들어, 표현식 z.real에서, real은 객체 z의 속성입니다. 엄밀히 말하면, 모듈의 이름에 대한 참조는 속성 참조입니다: 표현식 modname.funcname에서, modname은 모듈 객체이고 funcname은 그것의 속성입니다. 이 경우 모듈의 속성과 모듈에서 정의된 전역 이름 사이에 직관적인 매핑이 있게 됩니다: 그들은 같은 네임스페이스를 공유합니다! [1]

10. Attributes may be read-only or writable. In the latter case, assignment to attributes is possible. Module attributes are writable: you can write modname.the_answer = 42. Writable attributes may also be deleted with the del statement. For example, del modname.the_answer will remove the attribute the_answer from the object named by modname.

속성은 읽기 전용이거나 쓰기 가능할 수 있습니다. 후자의 경우, 속성에 대한 할당이 가능합니다. 모듈 속성은 쓰기 가능합니다: modname.the_answer = 42와 같이 쓸 수 있습니다. 쓰기 가능한 속성은 또한 del 문으로 삭제될 수 있습니다. 예를 들어, del modname.the_answer는 modname이라는 이름의 객체에서 the_answer 속성을 제거합니다.

11. Namespaces are created at different moments and have different lifetimes. The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted. The global namespace for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits. The statements executed by the top-level invocation of the interpreter, either read from a script file or interactively, are considered part of a module called __main__, so they have their own global namespace. (The built-in names actually also live in a module; this is called builtins.)

네임스페이스는 다른 순간에 생성되며 다른 수명을 가집니다. 내장 이름을 포함하는 네임스페이스는 파이썬 인터프리터가 시작될 때 생성되며, 절대 삭제되지 않습니다. 모듈에 대한 전역 네임스페이스는 모듈 정의가 읽힐 때 생성됩니다; 일반적으로, 모듈 네임스페이스도 인터프리터가 종료될 때까지 지속됩니다. 인터프리터의 최상위 호출에 의해 실행되는 문장들은, 스크립트 파일에서 읽히든 대화식으로 읽히든, __main__이라는 모듈의 일부로 간주되므로, 그들은 자신의 전역 네임스페이스를 가집니다. (내장 이름들도 실제로 모듈에 있습니다; 이것은 builtins라고 불립니다.)

12. The local namespace for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled within the function. (Actually, forgetting would be a better way to describe what actually happens.) Of course, recursive invocations each have their own local namespace.

함수에 대한 로컬 네임스페이스는 함수가 호출될 때 생성되고, 함수가 반환하거나 함수 내에서 처리되지 않는 예외를 발생시킬 때 삭제됩니다. (사실, 잊어버리는 것이 실제로 일어나는 일을 설명하는 더 나은 방법일 것입니다.) 물론, 재귀 호출은 각각 자신의 로컬 네임스페이스를 가집니다.

13. A scope is a textual region of a Python program where a namespace is directly accessible. "Directly accessible" here means that an unqualified reference to a name attempts to find the name in the namespace.

범위는 네임스페이스가 직접 접근 가능한 파이썬 프로그램의 텍스트 영역입니다. 여기서 "직접 접근 가능"은 이름에 대한 비한정 참조가 네임스페이스에서 이름을 찾으려고 시도한다는 의미입니다.

14. Although scopes are determined statically, they are used dynamically. At any time during execution, there are 3 or 4 nested scopes whose namespaces are directly accessible:

범위는 정적으로 결정되지만, 동적으로 사용됩니다. 실행 중 어느 시점에서든, 네임스페이스가 직접 접근 가능한 3개 또는 4개의 중첩된 범위가 있습니다:

15. the innermost scope, which is searched first, contains the local names

가장 안쪽 범위, 먼저 검색되며, 로컬 이름을 포함합니다

16. the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contain non-local, but also non-global names

모든 둘러싸는 함수의 범위, 가장 가까운 둘러싸는 범위부터 검색하며, 비-로컬하지만 또한 비-전역 이름을 포함합니다

17. the next-to-last scope contains the current module's global names

마지막에서 두 번째 범위는 현재 모듈의 전역 이름을 포함합니다

18. the outermost scope (searched last) is the namespace containing built-in names

가장 바깥쪽 범위(마지막으로 검색됨)는 내장 이름을 포함하는 네임스페이스입니다

19. If a name is declared global, then all references and assignments go directly to the next-to-last scope containing the module's global names. To rebind variables found outside of the innermost scope, the nonlocal statement can be used; if not declared nonlocal, those variables are read-only (an attempt to write to such a variable will simply create a new local variable in the innermost scope, leaving the identically named outer variable unchanged).

이름이 전역으로 선언되면, 모든 참조와 할당은 모듈의 전역 이름을 포함하는 마지막에서 두 번째 범위로 직접 갑니다. 가장 안쪽 범위 바깥에서 발견된 변수를 다시 바인딩하기 위해, nonlocal 문을 사용할 수 있습니다; nonlocal로 선언되지 않으면, 그 변수들은 읽기 전용입니다(그러한 변수에 쓰려는 시도는 단순히 가장 안쪽 범위에 새로운 로컬 변수를 생성하며, 동일한 이름의 외부 변수는 변경되지 않습니다).

20. Usually, the local scope references the local names of the (textually) current function. Outside functions, the local scope references the same namespace as the global scope: the module's namespace. Class definitions place yet another namespace in the local scope.

일반적으로, 로컬 범위는 (텍스트적으로) 현재 함수의 로컬 이름을 참조합니다. 함수 밖에서, 로컬 범위는 전역 범위와 같은 네임스페이스를 참조합니다: 모듈의 네임스페이스. 클래스 정의는 로컬 범위에 또 다른 네임스페이스를 배치합니다.

21. It is important to realize that scopes are determined textually: the global scope of a function defined in a module is that module's namespace, no matter from where or by what alias the function is called. On the other hand, the actual search for names is done dynamically, at run time — however, the language definition is evolving towards static name resolution, at "compile" time, so don't rely on dynamic name resolution! (In fact, local variables are already determined statically.)

범위가 텍스트적으로 결정된다는 것을 인식하는 것이 중요합니다: 모듈에서 정의된 함수의 전역 범위는 그 모듈의 네임스페이스입니다. 함수가 어디서 또는 어떤 별칭으로 호출되든 상관없습니다. 반면에, 실제 이름 검색은 동적으로, 런타임에 수행됩니다 — 그러나, 언어 정의는 "컴파일" 시간에, 정적 이름 해결을 향해 진화하고 있으므로, 동적 이름 해결에 의존하지 마세요! (사실, 로컬 변수는 이미 정적으로 결정됩니다.)

22. A special quirk of Python is that – if no global or nonlocal statement is in effect – assignments to names always go into the innermost scope. Assignments do not copy data — they just bind names to objects. The same is true for deletions: the statement del x removes the binding of x from the namespace referenced by the local scope. In fact, all operations that introduce new names use the local scope: in particular, import statements and function definitions bind the module or function name in the local scope.

파이썬의 특별한 특성 중 하나는 – 전역이나 비지역 문이 영향을 미치지 않는 경우 – 이름에 대한 할당은 항상 가장 안쪽 범위로 들어간다는 것입니다. 할당은 데이터를 복사하지 않습니다 — 그들은 단지 이름을 객체에 바인딩합니다. 삭제에도 같은 것이 적용됩니다: del x 문은 로컬 범위에 의해 참조되는 네임스페이스에서 x의 바인딩을 제거합니다. 사실, 새로운 이름을 도입하는 모든 작업은 로컬 범위를 사용합니다: 특히, import 문과 함수 정의는 모듈이나 함수 이름을 로컬 범위에 바인딩합니다.

23. The global statement can be used to indicate that particular variables live in the global scope and should be rebound there; the nonlocal statement indicates that particular variables live in an enclosing scope and should be rebound there.

global 문은 특정 변수가 전역 범위에 있고 거기서 다시 바인딩되어야 함을 나타내는 데 사용될 수 있습니다; nonlocal 문은 특정 변수가 둘러싸는 범위에 있고 거기서 다시 바인딩되어야 함을 나타냅니다.

### 9.2.1. Scopes and Namespaces Example

24. This is an example demonstrating how to reference the different scopes and namespaces, and how global and nonlocal affect variable binding:

다음은 다른 범위와 네임스페이스를 참조하는 방법과 global 및 nonlocal이 변수 바인딩에 어떤 영향을 미치는지 보여주는 예입니다:

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

25. The output of the example code is:

예제 코드의 출력은 다음과 같습니다:

```
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

26. Note how the local assignment (which is default) didn't change scope_test's binding of spam. The nonlocal assignment changed scope_test's binding of spam, and the global assignment changed the module-level binding.

로컬 할당(기본값)이 scope_test의 spam 바인딩을 변경하지 않았음을 주목하세요. nonlocal 할당은 scope_test의 spam 바인딩을 변경했고, global 할당은 모듈 수준의 바인딩을 변경했습니다.

27. You can also see that there was no previous binding for spam before the global assignment.

또한 global 할당 전에는 spam에 대한 이전 바인딩이 없었음을 알 수 있습니다.

## 9.3. A First Look at Classes

28. Classes introduce a little bit of new syntax, three new object types, and some new semantics.

클래스는 약간의 새로운 구문, 세 가지 새로운 객체 타입, 그리고 몇 가지 새로운 의미론을 소개합니다.

### 9.3.1. Class Definition Syntax

29. The simplest form of class definition looks like this:

클래스 정의의 가장 간단한 형태는 다음과 같습니다:

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

30. Class definitions, like function definitions (def statements) must be executed before they have any effect. (You could conceivably place a class definition in a branch of an if statement, or inside a function.)

클래스 정의는, 함수 정의(def 문)처럼 효과가 있기 전에 실행되어야 합니다. (개념적으로 if 문의 분기나 함수 안에 클래스 정의를 배치할 수 있습니다.)

31. In practice, the statements inside a class definition will usually be function definitions, but other statements are allowed, and sometimes useful — we'll come back to this later. The function definitions inside a class normally have a peculiar form of argument list, dictated by the calling conventions for methods — again, this is explained later.

실제로, 클래스 정의 내의 문장들은 보통 함수 정의일 것이지만, 다른 문장들도 허용되며, 때로는 유용합니다 — 이에 대해서는 나중에 다시 살펴보겠습니다. 클래스 내의 함수 정의는 일반적으로 메서드에 대한 호출 규칙에 의해 지정된 특이한 형태의 인수 목록을 가집니다 — 이것도 나중에 설명됩니다.

32. When a class definition is entered, a new namespace is created, and used as the local scope — thus, all assignments to local variables go into this new namespace. In particular, function definitions bind the name of the new function here.

클래스 정의가 입력되면, 새로운 네임스페이스가 생성되고, 로컬 범위로 사용됩니다 — 따라서, 로컬 변수에 대한 모든 할당은 이 새로운 네임스페이스로 들어갑니다. 특히, 함수 정의는 여기서 새 함수의 이름을 바인딩합니다.

33. When a class definition is left normally (via the end), a class object is created. This is basically a wrapper around the contents of the namespace created by the class definition; we'll learn more about class objects in the next section. The original local scope (the one in effect just before the class definition was entered) is reinstated, and the class object is bound here to the class name given in the class definition header (ClassName in the example).

클래스 정의가 정상적으로 종료되면(끝을 통해), 클래스 객체가 생성됩니다. 이것은 기본적으로 클래스 정의에 의해 생성된 네임스페이스의 내용을 감싸는 래퍼입니다. 다음 섹션에서 클래스 객체에 대해 더 알아볼 것입니다. 원래 로컬 범위(클래스 정의가 입력되기 직전에 효과가 있던 범위)가 복원되고, 클래스 객체는 클래스 정의 헤더에 주어진 클래스 이름(예제의 ClassName)에 바인딩됩니다.

### 9.3.2. Class Objects

34. Class objects support two kinds of operations: attribute references and instantiation.

클래스 객체는 두 가지 종류의 연산을 지원합니다: 속성 참조와 인스턴스화.

35. Attribute references use the standard syntax used for all attribute references in Python: obj.name. Valid attribute names are all the names that were in the class's namespace when the class object was created. So, if the class definition looked like this:

속성 참조는 파이썬의 모든 속성 참조에 사용되는 표준 구문을 사용합니다: obj.name. 유효한 속성 이름은 클래스 객체가 생성될 때 클래스의 네임스페이스에 있었던 모든 이름입니다. 따라서, 클래스 정의가 다음과 같다면:

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

36. then MyClass.i and MyClass.f are valid attribute references, returning an integer and a function object, respectively. Class attributes can also be assigned to, so you can change the value of MyClass.i by assignment. __doc__ is also a valid attribute, returning the docstring belonging to the class: "A simple example class".

그러면 MyClass.i와 MyClass.f는 유효한 속성 참조이며, 각각 정수와 함수 객체를 반환합니다. 클래스 속성에는 할당할 수도 있으므로, 할당을 통해 MyClass.i의 값을 변경할 수 있습니다. __doc__도 유효한 속성으로, 클래스에 속한 문서 문자열: "A simple example class"을 반환합니다.

37. Class instantiation uses function notation. Just pretend that the class object is a parameterless function that returns a new instance of the class. For example (assuming the above class):

클래스 인스턴스화는 함수 표기법을 사용합니다. 클래스 객체가 클래스의 새 인스턴스를 반환하는 매개변수 없는 함수라고 가정하면 됩니다. 예를 들어 (위의 클래스를 가정):

```python
x = MyClass()
```

38. creates a new instance of the class and assigns this object to the local variable x.

클래스의 새 인스턴스를 생성하고 이 객체를 로컬 변수 x에 할당합니다.

39. The instantiation operation ("calling" a class object) creates an empty object. Many classes like to create objects with instances customized to a specific initial state. Therefore a class may define a special method named __init__(), like this:

인스턴스화 연산(클래스 객체 "호출")은 빈 객체를 생성합니다. 많은 클래스는 특정 초기 상태로 사용자 정의된 인스턴스로 객체를 생성하고 싶어합니다. 따라서 클래스는 다음과 같이 __init__()이라는 특별한 메서드를 정의할 수 있습니다:

```python
def __init__(self):
    self.data = []
```

40. When a class defines an __init__() method, class instantiation automatically invokes __init__() for the newly created class instance. So in this example, a new, initialized instance can be obtained by:

클래스가 __init__() 메서드를 정의하면, 클래스 인스턴스화는 새로 생성된 클래스 인스턴스에 대해 자동으로 __init__()을 호출합니다. 따라서 이 예에서, 초기화된 새 인스턴스는 다음과 같이 얻을 수 있습니다:

```python
x = MyClass()
```

41. Of course, the __init__() method may have arguments for greater flexibility. In that case, arguments given to the class instantiation operator are passed on to __init__(). For example,

물론, __init__() 메서드는 더 큰 유연성을 위해 인수를 가질 수 있습니다. 이 경우, 클래스 인스턴스화 연산자에 주어진 인수가 __init__()에 전달됩니다. 예를 들어,

```python
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

### 9.3.3. Instance Objects

42. Now what can we do with instance objects? The only operations understood by instance objects are attribute references. There are two kinds of valid attribute names: data attributes and methods.

이제 인스턴스 객체로 무엇을 할 수 있을까요? 인스턴스 객체가 이해하는 유일한 연산은 속성 참조입니다. 유효한 속성 이름에는 두 가지 종류가 있습니다: 데이터 속성과 메서드.

43. data attributes correspond to "instance variables" in Smalltalk, and to "data members" in C++. Data attributes need not be declared; like local variables, they spring into existence when they are first assigned to. For example, if x is the instance of MyClass created above, the following piece of code will print the value 16, without leaving a trace:

데이터 속성은 Smalltalk의 "인스턴스 변수"와 C++의 "데이터 멤버"에 해당합니다. 데이터 속성은 선언할 필요가 없습니다. 로컬 변수처럼, 처음 할당될 때 존재하게 됩니다. 예를 들어, x가 위에서 생성한 MyClass의 인스턴스라면, 다음 코드는 흔적을 남기지 않고 값 16을 출력합니다:

```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

44. The other kind of instance attribute reference is a method. A method is a function that "belongs to" an object.

다른 종류의 인스턴스 속성 참조는 메서드입니다. 메서드는 객체에 "속하는" 함수입니다.

45. Valid method names of an instance object depend on its class. By definition, all attributes of a class that are function objects define corresponding methods of its instances. So in our example, x.f is a valid method reference, since MyClass.f is a function, but x.i is not, since MyClass.i is not. But x.f is not the same thing as MyClass.f — it is a method object, not a function object.

인스턴스 객체의 유효한 메서드 이름은 해당 클래스에 따라 다릅니다. 정의에 따르면, 함수 객체인 클래스의 모든 속성은 해당 인스턴스의 해당 메서드를 정의합니다. 따라서 우리 예제에서, MyClass.f가 함수이기 때문에 x.f는 유효한 메서드 참조이지만, MyClass.i는 함수가 아니기 때문에 x.i는 아닙니다. 그러나 x.f는 MyClass.f와 같은 것이 아닙니다 — 그것은 함수 객체가 아닌 메서드 객체입니다.

### 9.3.4. Method Objects

46. Usually, a method is called right after it is bound:

일반적으로, 메서드는 바인딩된 직후에 호출됩니다:

```python
x.f()
```

47. In the MyClass example, this will return the string 'hello world'. However, it is not necessary to call a method right away: x.f is a method object, and can be stored away and called at a later time. For example:

MyClass 예제에서, 이것은 문자열 'hello world'를 반환합니다. 그러나, 메서드를 바로 호출할 필요는 없습니다: x.f는 메서드 객체이며, 저장해 두었다가 나중에 호출할 수 있습니다. 예를 들어:

```python
xf = x.f
while True:
    print(xf())
```

48. will continue to print hello world until the end of time.

이것은 시간이 끝날 때까지 hello world를 계속 출력할 것입니다.

49. What exactly happens when a method is called? You may have noticed that x.f() was called without an argument above, even though the function definition for f() specified an argument. What happened to the argument? Surely Python raises an exception when a function that requires an argument is called without any — even if the argument isn't actually used…

메서드가 호출될 때 정확히 무슨 일이 일어날까요? 위에서 f()의 함수 정의가 인수를 지정했음에도 불구하고, x.f()가 인수 없이 호출되었다는 것을 알아차렸을 수도 있습니다. 인수는 어떻게 되었을까요? 분명히 파이썬은 인수가 필요한 함수가 인수 없이 호출될 때 예외를 발생시킵니다 — 인수가 실제로 사용되지 않더라도...

50. Actually, you may have guessed the answer: the special thing about methods is that the instance object is passed as the first argument of the function. In our example, the call x.f() is exactly equivalent to MyClass.f(x). In general, calling a method with a list of n arguments is equivalent to calling the corresponding function with an argument list that is created by inserting the method's instance object before the first argument.

실제로, 답을 추측했을 수도 있습니다: 메서드에 관한 특별한 점은 인스턴스 객체가 함수의 첫 번째 인수로 전달된다는 것입니다. 우리 예제에서, x.f() 호출은 MyClass.f(x)와 정확히 동등합니다. 일반적으로, n 개의 인수 목록으로 메서드를 호출하는 것은 메서드의 인스턴스 객체를 첫 번째 인수 앞에 삽입하여 생성된 인수 목록으로 해당 함수를 호출하는 것과 동등합니다.

51. In general, methods work as follows. When a non-data attribute of an instance is referenced, the instance's class is searched. If the name denotes a valid class attribute that is a function object, references to both the instance object and the function object are packed into a method object. When the method object is called with an argument list, a new argument list is constructed from the instance object and the argument list, and the function object is called with this new argument list.

일반적으로, 메서드는 다음과 같이 작동합니다. 인스턴스의 비-데이터 속성이 참조될 때, 인스턴스의 클래스가 검색됩니다. 이름이 함수 객체인 유효한 클래스 속성을 나타내는 경우, 인스턴스 객체와 함수 객체에 대한 참조가 모두 메서드 객체로 패킹됩니다. 메서드 객체가 인수 목록으로 호출되면, 인스턴스 객체와 인수 목록에서 새 인수 목록이 구성되고, 함수 객체는 이 새 인수 목록으로 호출됩니다.

### 9.3.5. Class and Instance Variables

52. Generally speaking, instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class:

일반적으로 말해서, 인스턴스 변수는 각 인스턴스에 고유한 데이터를 위한 것이고 클래스 변수는 클래스의 모든 인스턴스가 공유하는 속성과 메서드를 위한 것입니다:

```python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```

53. As discussed in A Word About Names and Objects, shared data can have possibly surprising effects with involving mutable objects such as lists and dictionaries. For example, the tricks list in the following code should not be used as a class variable because just a single list would be shared by all Dog instances:

Names and Objects에 관한 단어에서 논의한 바와 같이, 공유 데이터는 리스트 및 딕셔너리와 같은 변경 가능한 객체와 관련하여 놀라운 효과를 가질 수 있습니다. 예를 들어, 다음 코드의 tricks 리스트는 모든 Dog 인스턴스에 의해 단일 리스트만 공유되므로 클래스 변수로 사용되어서는 안 됩니다:

```python
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```

54. Correct design of the class should use an instance variable instead:

클래스의 올바른 설계는 대신 인스턴스 변수를 사용해야 합니다:

```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```

## 9.4. Random Remarks

55. If the same attribute name occurs in both an instance and in a class, then attribute lookup prioritizes the instance:

같은 속성 이름이 인스턴스와 클래스 모두에 있는 경우, 속성 조회는 인스턴스를 우선시합니다:

```python
>>> class Warehouse:
...    purpose = 'storage'
...    region = 'west'
...
>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east
```

56. Data attributes may be referenced by methods as well as by ordinary users ("clients") of an object. In other words, classes are not usable to implement pure abstract data types. In fact, nothing in Python makes it possible to enforce data hiding — it is all based upon convention. (On the other hand, the Python implementation, written in C, can completely hide implementation details and control access to an object if necessary; this can be used by extensions to Python written in C.)

데이터 속성은 객체의 일반 사용자("클라이언트")뿐만 아니라 메서드에 의해서도 참조될 수 있습니다. 즉, 클래스는 순수한 추상 데이터 타입을 구현하는 데 사용할 수 없습니다. 사실, 파이썬에서는 데이터 숨김을 강제하는 것이 가능하지 않습니다 — 모든 것은 규칙에 근거합니다. (반면에, C로 작성된 파이썬 구현은 필요한 경우 구현 세부 사항을 완전히 숨기고 객체에 대한 접근을 제어할 수 있습니다; 이것은 C로 작성된 파이썬 확장에서 사용될 수 있습니다.)

57. Clients should use data attributes with care — clients may mess up invariants maintained by the methods by stamping on their data attributes. Note that clients may add data attributes of their own to an instance object without affecting the validity of the methods, as long as name conflicts are avoided — again, a naming convention can save a lot of headaches here.

클라이언트는 데이터 속성을 주의해서 사용해야 합니다 — 클라이언트는 데이터 속성을 밟아서 메서드에 의해 유지되는 불변량을 엉망으로 만들 수 있습니다. 클라이언트는 이름 충돌을 피하는 한, 메서드의 유효성에 영향을 주지 않고 인스턴스 객체에 자신의 데이터 속성을 추가할 수 있다는 점에 유의하세요 — 다시 말해, 명명 규칙은 여기에서 많은 두통을 줄일 수 있습니다.

58. There is no shorthand for referencing data attributes (or other methods!) from within methods. I find that this actually increases the readability of methods: there is no chance of confusing local variables and instance variables when glancing through a method.

메서드 내에서 데이터 속성(또는 다른 메서드!)을 참조하기 위한 약어는 없습니다. 나는 이것이 실제로 메서드의 가독성을 높인다고 생각합니다: 메서드를 훑어볼 때 로컬 변수와 인스턴스 변수를 혼동할 가능성이 없습니다.

59. Often, the first argument of a method is called self. This is nothing more than a convention: the name self has absolutely no special meaning to Python. Note, however, that by not following the convention your code may be less readable to other Python programmers, and it is also conceivable that a class browser program might be written that relies upon such a convention.

종종, 메서드의 첫 번째 인수는 self라고 불립니다. 이것은 규칙에 불과합니다: self라는 이름은 파이썬에게 절대적으로 특별한 의미가 없습니다. 그러나, 규칙을 따르지 않으면 코드가 다른 파이썬 프로그래머에게 읽기 어려울 수 있으며, 또한 그러한 규칙에 의존하는 클래스 브라우저 프로그램이 작성될 수도 있습니다.

60. Any function object that is a class attribute defines a method for instances of that class. It is not necessary that the function definition is textually enclosed in the class definition: assigning a function object to a local variable in the class is also ok. For example:

클래스 속성인 모든 함수 객체는 해당 클래스의 인스턴스에 대한 메서드를 정의합니다. 함수 정의가 클래스 정의 내에 텍스트적으로 포함될 필요는 없습니다: 함수 객체를 클래스의 로컬 변수에 할당하는 것도 괜찮습니다. 예를 들어:

```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```

61. Now f, g and h are all attributes of class C that refer to function objects, and consequently they are all methods of instances of C — h being exactly equivalent to g. Note that this practice usually only serves to confuse the reader of a program.

이제 f, g 및 h는 모두 함수 객체를 참조하는 클래스 C의 속성이며, 결과적으로 모두 C의 인스턴스의 메서드입니다 — h는 g와 정확히 동등합니다. 이 관행은 일반적으로 프로그램의 독자를 혼란스럽게 할 뿐입니다.

62. Methods may call other methods by using method attributes of the self argument:

메서드는 self 인수의 메서드 속성을 사용하여 다른 메서드를 호출할 수 있습니다:

```python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

63. Methods may reference global names in the same way as ordinary functions. The global scope associated with a method is the module containing its definition. (A class is never used as a global scope.) While one rarely encounters a good reason for using global data in a method, there are many legitimate uses of the global scope: for one thing, functions and modules imported into the global scope can be used by methods, as well as functions and classes defined in it. Usually, the class containing the method is itself defined in this global scope, and in the next section we'll find some good reasons why a method would want to reference its own class.

메서드는 일반 함수와 같은 방식으로 전역 이름을 참조할 수 있습니다. 메서드와 관련된 전역 범위는 그 정의를 포함하는 모듈입니다. (클래스는 결코 전역 범위로 사용되지 않습니다.) 메서드에서 전역 데이터를 사용하는 좋은 이유를 거의 만나지 않지만, 전역 범위의 많은 합법적인 사용이 있습니다: 하나는, 전역 범위로 가져온 함수와 모듈이 메서드에서 사용될 수 있으며, 그 안에 정의된 함수와 클래스도 마찬가지입니다. 일반적으로, 메서드를 포함하는 클래스는 이 전역 범위에 정의되며, 다음 섹션에서 메서드가 자신의 클래스를 참조하기를 원하는 몇 가지 좋은 이유를 찾을 수 있습니다.

64. Each value is an object, and therefore has a class (also called its type). It is stored as object.__class__.

각 값은 객체이므로 클래스(타입이라고도 함)를 가집니다. 이것은 object.__class__로 저장됩니다.

## 9.5. Inheritance

65. Of course, a language feature would not be worthy of the name "class" without supporting inheritance. The syntax for a derived class definition looks like this:

물론, "클래스"라는 이름을 가진 언어 기능은 상속을 지원하지 않으면 그 가치가 없을 것입니다. 파생 클래스 정의의 구문은 다음과 같습니다:

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

66. The name BaseClassName must be defined in a namespace accessible from the scope containing the derived class definition. In place of a base class name, other arbitrary expressions are also allowed. This can be useful, for example, when the base class is defined in another module:

BaseClassName 이름은 파생 클래스 정의를 포함하는 범위에서 접근 가능한 네임스페이스에 정의되어야 합니다. 기본 클래스 이름 대신, 다른 임의의 표현식도 허용됩니다. 예를 들어, 기본 클래스가 다른 모듈에 정의되어 있을 때 유용할 수 있습니다:

```python
class DerivedClassName(modname.BaseClassName):
```

67. Execution of a derived class definition proceeds the same as for a base class. When the class object is constructed, the base class is remembered. This is used for resolving attribute references: if a requested attribute is not found in the class, the search proceeds to look in the base class. This rule is applied recursively if the base class itself is derived from some other class.

파생 클래스 정의의 실행은 기본 클래스와 동일하게 진행됩니다. 클래스 객체가 구성되면, 기본 클래스가 기억됩니다. 이는 속성 참조를 해결하는 데 사용됩니다: 요청된 속성이 클래스에서 발견되지 않으면, 검색은 기본 클래스에서 찾기 위해 진행됩니다. 기본 클래스 자체가 다른 클래스에서 파생된 경우 이 규칙이 재귀적으로 적용됩니다.

68. There's nothing special about instantiation of derived classes: DerivedClassName() creates a new instance of the class. Method references are resolved as follows: the corresponding class attribute is searched, descending down the chain of base classes if necessary, and the method reference is valid if this yields a function object.

파생 클래스의 인스턴스화에 대해 특별한 것은 없습니다: DerivedClassName()은 클래스의 새 인스턴스를 생성합니다. 메서드 참조는 다음과 같이 해결됩니다: 해당 클래스 속성이 검색되고, 필요한 경우 기본 클래스 체인을 내려가며, 이것이 함수 객체를 산출하면 메서드 참조가 유효합니다.

69. Derived classes may override methods of their base classes. Because methods have no special privileges when calling other methods of the same object, a method of a base class that calls another method defined in the same base class may end up calling a method of a derived class that overrides it. (For C++ programmers: all methods in Python are effectively virtual.)

파생 클래스는 기본 클래스의 메서드를 오버라이드할 수 있습니다. 메서드는 같은 객체의 다른 메서드를 호출할 때 특별한 특권이 없기 때문에, 같은 기본 클래스에 정의된 다른 메서드를 호출하는 기본 클래스의 메서드는 결국 그것을 오버라이드하는 파생 클래스의 메서드를 호출할 수 있습니다. (C++ 프로그래머를 위해: Python의 모든 메서드는 사실상 가상입니다.)

70. An overriding method in a derived class may in fact want to extend rather than simply replace the base class method of the same name. There is a simple way to call the base class method directly: just call BaseClassName.methodname(self, arguments). This is occasionally useful to clients as well. (Note that this only works if the base class is accessible as BaseClassName in the global scope.)

파생 클래스의 오버라이딩 메서드는 실제로 동일한 이름의 기본 클래스 메서드를 단순히 대체하기보다는 확장하고 싶어할 수 있습니다. 기본 클래스 메서드를 직접 호출하는 간단한 방법이 있습니다: BaseClassName.methodname(self, arguments)를 호출하면 됩니다. 이는 때때로 클라이언트에게도 유용합니다. (이는 기본 클래스가 전역 범위에서 BaseClassName으로 접근 가능한 경우에만 작동한다는 점에 유의하세요.)

71. Python has two built-in functions that work with inheritance:

Python에는 상속과 함께 작동하는 두 가지 내장 함수가 있습니다:

72. Use isinstance() to check an instance's type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.

isinstance()를 사용하여 인스턴스의 타입을 확인하세요: isinstance(obj, int)는 obj.__class__가 int이거나 int에서 파생된 클래스인 경우에만 True가 됩니다.

73. Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.

issubclass()를 사용하여 클래스 상속을 확인하세요: bool이 int의 서브클래스이므로 issubclass(bool, int)는 True입니다. 그러나 float은 int의 서브클래스가 아니므로 issubclass(float, int)는 False입니다.

### 9.5.1. Multiple Inheritance

74. Python supports a form of multiple inheritance as well. A class definition with multiple base classes looks like this:

Python은 다중 상속의 형태도 지원합니다. 여러 기본 클래스가 있는 클래스 정의는 다음과 같습니다:

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

75. For most purposes, in the simplest cases, you can think of the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy. Thus, if an attribute is not found in DerivedClassName, it is searched for in Base1, then (recursively) in the base classes of Base1, and if it was not found there, it was searched for in Base2, and so on.

대부분의 목적에서, 가장 간단한 경우에는, 부모 클래스에서 상속된 속성에 대한 검색을 깊이 우선, 왼쪽에서 오른쪽으로 생각할 수 있으며, 계층에서 중복이 있는 경우 같은 클래스를 두 번 검색하지 않습니다. 따라서, 속성이 DerivedClassName에서 발견되지 않으면, Base1에서 검색하고, 그 다음 (재귀적으로) Base1의 기본 클래스에서 검색하며, 거기서 찾지 못하면 Base2에서 검색하는 식입니다.

76. In fact, it is slightly more complex than that; the method resolution order changes dynamically to support cooperative calls to super(). This approach is known in some other multiple-inheritance languages as call-next-method and is more powerful than the super call found in single-inheritance languages.

사실, 그것보다 약간 더 복잡합니다. 메서드 해결 순서는 super()에 대한 협력적 호출을 지원하기 위해 동적으로 변경됩니다. 이 접근법은 일부 다른 다중 상속 언어에서 call-next-method로 알려져 있으며, 단일 상속 언어에서 발견되는 super 호출보다 더 강력합니다.

77. Dynamic ordering is necessary because all cases of multiple inheritance exhibit one or more diamond relationships (where at least one of the parent classes can be accessed through multiple paths from the bottommost class). For example, all classes inherit from object, so any case of multiple inheritance provides more than one path to reach object. To keep the base classes from being accessed more than once, the dynamic algorithm linearizes the search order in a way that preserves the left-to-right ordering specified in each class, that calls each parent only once, and that is monotonic (meaning that a class can be subclassed without affecting the precedence order of its parents). Taken together, these properties make it possible to design reliable and extensible classes with multiple inheritance. For more detail, see The Python 2.3 Method Resolution Order.

동적 정렬이 필요한 이유는 모든 다중 상속 사례가 하나 이상의 다이아몬드 관계를 나타내기 때문입니다(여기서 적어도 하나의 부모 클래스가 최하위 클래스에서 여러 경로를 통해 접근될 수 있음). 예를 들어, 모든 클래스는 object에서 상속되므로, 다중 상속의 모든 경우는 object에 도달하기 위한 둘 이상의 경로를 제공합니다. 기본 클래스가 두 번 이상 접근되는 것을 방지하기 위해, 동적 알고리즘은 각 클래스에 지정된 왼쪽에서 오른쪽 순서를 유지하고, 각 부모를 한 번만 호출하며, 단조롭게(즉, 클래스가 부모의 우선 순위에 영향을 주지 않고 서브클래스화될 수 있음) 검색 순서를 선형화합니다. 이러한 속성들을 함께 고려하면, 다중 상속으로 신뢰할 수 있고 확장 가능한 클래스를 설계할 수 있습니다. 자세한 내용은 Python 2.3 Method Resolution Order를 참조하세요.

## 9.6. Private Variables

78. "Private" instance variables that cannot be accessed except from inside an object don't exist in Python. However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.

객체 내부에서만 접근할 수 있는 "비공개" 인스턴스 변수는 Python에 존재하지 않습니다. 그러나 대부분의 Python 코드가 따르는 관례가 있습니다: 밑줄로 시작하는 이름(예: _spam)은 API의 비공개 부분으로 취급되어야 합니다(함수, 메서드 또는 데이터 멤버인지에 관계없이). 이는 구현 세부 사항으로 간주되어야 하며 통지 없이 변경될 수 있습니다.

79. Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by subclasses), there is limited support for such a mechanism, called name mangling. Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam, where classname is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, as long as it occurs within the definition of a class.

클래스 비공개 멤버에 대한 유효한 사용 사례가 있기 때문에(즉, 서브클래스에 의해 정의된 이름과의 이름 충돌을 피하기 위해), 이름 맹글링이라고 하는 이러한 메커니즘에 대한 제한된 지원이 있습니다. __spam 형식의 식별자(적어도 두 개의 선행 밑줄, 많아야 하나의 후행 밑줄)는 텍스트적으로 _classname__spam으로 대체됩니다. 여기서 classname은 선행 밑줄이 제거된 현재 클래스 이름입니다. 이 맹글링은 클래스의 정의 내에서 발생하는 한, 식별자의 구문적 위치와 관계없이 수행됩니다.

80. See also The private name mangling specifications for details and special cases. Name mangling is helpful for letting subclasses override methods without breaking intraclass method calls. For example:

자세한 내용 및 특수 사례는 비공개 이름 맹글링 사양을 참조하세요. 이름 맹글링은 클래스 내 메서드 호출을 깨지 않고 서브클래스가 메서드를 오버라이드할 수 있게 하는 데 도움이 됩니다. 예를 들어:

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

81. The above example would work even if MappingSubclass were to introduce a __update identifier since it is replaced with _Mapping__update in the Mapping class and _MappingSubclass__update in the MappingSubclass class respectively.

위 예제는 MappingSubclass가 __update 식별자를 도입하더라도 작동할 것입니다. 이는 Mapping 클래스에서는 _Mapping__update로, MappingSubclass 클래스에서는 _MappingSubclass__update로 각각 대체되기 때문입니다.

82. Note that the mangling rules are designed mostly to avoid accidents; it still is possible to access or modify a variable that is considered private. This can even be useful in special circumstances, such as in the debugger.

맹글링 규칙은 주로 사고를 피하기 위해 설계되었다는 점에 유의하세요. 비공개로 간주되는 변수에 접근하거나 수정하는 것은 여전히 가능합니다. 이는 디버거와 같은 특별한 상황에서도 유용할 수 있습니다.

83. Notice that code passed to exec() or eval() does not consider the classname of the invoking class to be the current class; this is similar to the effect of the global statement, the effect of which is likewise restricted to code that is byte-compiled together. The same restriction applies to getattr(), setattr() and delattr(), as well as when referencing __dict__ directly.

exec() 또는 eval()에 전달된 코드는 호출 클래스의 클래스 이름을 현재 클래스로 간주하지 않습니다. 이는 global 문의 효과와 유사하며, 그 효과는 마찬가지로 함께 바이트 컴파일된 코드에 제한됩니다. 동일한 제한은 getattr(), setattr() 및 delattr()에도 적용되며, __dict__를 직접 참조할 때도 마찬가지입니다.

## 9.7. Odds and Ends

84. Sometimes it is useful to have a data type similar to the Pascal "record" or C "struct", bundling together a few named data items. The idiomatic approach is to use dataclasses for this purpose:

때로는 Pascal의 "record"나 C의 "struct"와 유사한 데이터 타입을 가지는 것이 유용할 수 있습니다. 이름이 지정된 몇 개의 데이터 항목을 함께 묶는 것입니다. 이를 위한 관용적 접근법은 dataclasses를 사용하는 것입니다:

```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int
    
john = Employee('john', 'computer lab', 1000)
john.dept
'computer lab'
john.salary
1000
```

85. A piece of Python code that expects a particular abstract data type can often be passed a class that emulates the methods of that data type instead. For instance, if you have a function that formats some data from a file object, you can define a class with methods read() and readline() that get the data from a string buffer instead, and pass it as an argument.

특정 추상 데이터 타입을 기대하는 Python 코드 조각은 종종 해당 데이터 타입의 메서드를 에뮬레이트하는 클래스를 대신 전달받을 수 있습니다. 예를 들어, 파일 객체에서 일부 데이터를 포맷하는 함수가 있다면, read()와 readline() 메서드를 가진 클래스를 정의하여 대신 문자열 버퍼에서 데이터를 가져오고, 이를 인수로 전달할 수 있습니다.

86. Instance method objects have attributes, too: m.__self__ is the instance object with the method m(), and m.__func__ is the function object corresponding to the method.

인스턴스 메서드 객체도 속성을 가집니다: m.__self__는 메서드 m()을 가진 인스턴스 객체이고, m.__func__는 메서드에 해당하는 함수 객체입니다.

## 9.8. Iterators

87. By now you have probably noticed that most container objects can be looped over using a for statement:

지금쯤이면 대부분의 컨테이너 객체가 for 문을 사용하여 반복될 수 있다는 것을 알아차렸을 것입니다:

```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```

88. This style of access is clear, concise, and convenient. The use of iterators pervades and unifies Python. Behind the scenes, the for statement calls iter() on the container object. The function returns an iterator object that defines the method __next__() which accesses elements in the container one at a time. When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to terminate. You can call the __next__() method using the next() built-in function; this example shows how it all works:

이 접근 방식은 명확하고, 간결하며, 편리합니다. 반복자의 사용은 파이썬 전체에 퍼져 있으며 통합합니다. 내부적으로 for 문은 컨테이너 객체에 대해 iter()를 호출합니다. 이 함수는 컨테이너의 요소를 한 번에 하나씩 접근하는 __next__() 메서드를 정의하는 반복자 객체를 반환합니다. 더 이상 요소가 없으면, __next__()는 StopIteration 예외를 발생시켜 for 루프가 종료되도록 알립니다. next() 내장 함수를 사용하여 __next__() 메서드를 호출할 수 있습니다; 이 예제는 모든 것이 어떻게 작동하는지 보여줍니다:

```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x10c90e650>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
```

89. Having seen the mechanics behind the iterator protocol, it is easy to add iterator behavior to your classes. Define an __iter__() method which returns an object with a __next__() method. If the class defines __next__(), then __iter__() can just return self:

반복자 프로토콜의 메커니즘을 확인했으므로, 클래스에 반복자 동작을 추가하는 것은 쉽습니다. __next__() 메서드가 있는 객체를 반환하는 __iter__() 메서드를 정의하세요. 클래스가 __next__()를 정의하는 경우, __iter__()는 단순히 self를 반환할 수 있습니다:

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```

```python
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
```

## 9.9. Generators

90. Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). An example shows that generators can be trivially easy to create:

제너레이터는 반복자를 생성하기 위한 간단하고 강력한 도구입니다. 일반 함수처럼 작성되지만 데이터를 반환하려 할 때마다 yield 문을 사용합니다. next()가 호출될 때마다, 제너레이터는 중단된 위치에서 다시 시작합니다(모든 데이터 값과 마지막으로 실행된 문장을 기억합니다). 다음 예제는 제너레이터가 아주 쉽게 생성될 수 있음을 보여줍니다:

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
```

```python
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g
```

91. Anything that can be done with generators can also be done with class-based iterators as described in the previous section. What makes generators so compact is that the __iter__() and __next__() methods are created automatically.

제너레이터로 할 수 있는 모든 것은 이전 섹션에서 설명한 클래스 기반 반복자로도 수행할 수 있습니다. 제너레이터가 매우 간결한 이유는 __iter__()와 __next__() 메서드가 자동으로 생성되기 때문입니다.

92. Another key feature is that the local variables and execution state are automatically saved between calls. This made the function easier to write and much more clear than an approach using instance variables like self.index and self.data.

또 다른 주요 기능은 로컬 변수와 실행 상태가 호출 사이에 자동으로 저장된다는 것입니다. 이로 인해 함수는 self.index와 self.data와 같은 인스턴스 변수를 사용하는 접근 방식보다 작성하기 쉽고 훨씬 더 명확해집니다.

93. In addition to automatic method creation and saving program state, when generators terminate, they automatically raise StopIteration. In combination, these features make it easy to create iterators with no more effort than writing a regular function.

자동 메서드 생성과 프로그램 상태 저장 외에도, 제너레이터가 종료되면 자동으로 StopIteration을 발생시킵니다. 이러한 기능을 조합하면 일반 함수를 작성하는 것 이상의 노력 없이 반복자를 쉽게 만들 수 있습니다.

## 9.10. Generator Expressions

94. Some simple generators can be coded succinctly as expressions using a syntax similar to list comprehensions but with parentheses instead of square brackets. These expressions are designed for situations where the generator is used right away by an enclosing function. Generator expressions are more compact but less versatile than full generator definitions and tend to be more memory friendly than equivalent list comprehensions.

일부 간단한 제너레이터는 리스트 컴프리헨션과 유사한 구문을 사용하되 대괄호 대신 괄호를 사용하여 간결하게 코딩될 수 있습니다. 이러한 표현식은 제너레이터가 둘러싸는 함수에 의해 즉시 사용되는 상황을 위해 설계되었습니다. 제너레이터 표현식은 완전한 제너레이터 정의보다 더 간결하지만 덜 다재다능하며, 동등한 리스트 컴프리헨션보다 메모리를 더 효율적으로 사용하는 경향이 있습니다.

95. Examples:

예시:

```python
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```

**Footnotes**

[1] 한 가지를 제외하고. 모듈 객체에는 __dict__라는 비밀 읽기 전용 속성이 있으며, 이는 모듈의 네임스페이스를 구현하는 데 사용되는 사전을 반환합니다. __dict__ 이름은 속성이지만 전역 이름이 아닙니다. 분명히, 이를 사용하는 것은 네임스페이스 구현의 추상화를 위반하며, 사후 디버거와 같은 것으로 제한되어야 합니다.
