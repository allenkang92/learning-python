# 6. Expressions  
6. 표현식  
This chapter explains the meaning of the elements of expressions in Python.  
이 장은 파이썬 표현식의 요소들이 가지는 의미를 설명합니다.

## 6.1. Arithmetic conversions  
6.1. 산술 변환  
When a description of an arithmetic operator below uses the phrase “the numeric arguments are converted to a common type”, this means that the operator implementation for built-in types works as follows:  
아래 산술 연산자 설명에서 “숫자 인수가 공통 타입으로 변환된다”라는 표현은 내장 타입에 대한 연산자 구현이 다음과 같이 작동함을 의미합니다:  

If either argument is a complex number, the other is converted to complex;  
만약 두 인수 중 하나가 복소수이면, 다른 인수는 복소수로 변환됩니다;  

otherwise, if either argument is a floating-point number, the other is converted to floating point;  
그렇지 않고, 둘 중 하나가 부동 소수점이면 다른 인수는 부동 소수점으로 변환됩니다;  

otherwise, both must be integers and no conversion is necessary.  
그 외의 경우 두 인수 모두 정수여야 하며 변환이 필요하지 않습니다.

Some additional rules apply for certain operators (e.g., a string as a left argument to the ‘%’ operator).  
일부 연산자(예: '%' 연산자의 왼쪽 인수로 문자열이 올 때)에는 추가 규칙이 적용됩니다.  
Extensions must define their own conversion behavior.  
확장은 자체적인 변환 동작을 정의해야 합니다.

## 6.2. Atoms  
6.2. 원자들  
Atoms are the most basic elements of expressions.  
원자(atom)는 표현식의 가장 기본적인 요소입니다.  

The simplest atoms are identifiers or literals.  
가장 단순한 원자는 식별자 또는 리터럴입니다.  

Forms enclosed in parentheses, brackets or braces are also categorized syntactically as atoms.  
괄호, 대괄호 또는 중괄호로 감싸진 형식도 구문상 원자로 분류됩니다.  

The syntax for atoms is:  
원자에 대한 구문은 다음과 같습니다:  

  atom      ::= identifier | literal | enclosure  
  atom      ::= 식별자 | 리터럴 | enclosure  
  enclosure ::= parenth_form | list_display | dict_display | set_display  
         ::= parenth_form | list_display | dict_display | set_display  
         | generator_expression | yield_atom  
         | generator_expression | yield_atom

## 6.2.1. Identifiers (Names)  
6.2.1. 식별자(이름)  
An identifier occurring as an atom is a name.  
원자로 나타나는 식별자는 이름입니다.  
See section Identifiers and keywords for lexical definition and section Naming and binding for documentation of naming and binding.  
어휘적 정의는 ‘식별자와 키워드’ 섹션을, 이름 지정 및 바인딩 문서는 ‘이름 지정 및 바인딩’ 섹션을 참조하십시오.

When the name is bound to an object, evaluation of the atom yields that object.  
이름이 객체에 바인딩되면, 원자의 평가 결과는 그 객체를 반환합니다.  
When a name is not bound, an attempt to evaluate it raises a NameError exception.  
이름이 바인딩되어 있지 않으면, 이를 평가하려 할 때 NameError 예외가 발생합니다.

## 6.2.1.1. Private name mangling  
6.2.1.1. 비공개 이름 맹글링  
When an identifier that textually occurs in a class definition begins with two or more underscore characters and does not end in two or more underscores, it is considered a private name of that class.  
클래스 정의 내에 텍스트로 나타나는 식별자가 두 개 이상의 밑줄로 시작하고 두 개 이상의 밑줄로 끝나지 않으면, 이는 해당 클래스의 비공개 이름으로 간주됩니다.

See also The class specifications.  
클래스 명세도 참조하십시오.

More precisely, private names are transformed to a longer form before code is generated for them.  
더 정확히는, 비공개 이름은 코드 생성 전에 더 긴 형태로 변환됩니다.  
If the transformed name is longer than 255 characters, implementation‐defined truncation may happen.  
변환된 이름이 255자보다 길면, 구현에 따라 잘릴 수 있습니다.

The transformation is independent of the syntactical context in which the identifier is used but only the following private identifiers are mangled:  
이 변환은 식별자가 사용되는 구문적 맥락과 무관하며, 다음의 비공개 식별자에 대해서만 적용됩니다:

Any name used as the name of a variable that is assigned or read or any name of an attribute being accessed.  
할당되거나 읽히는 변수 이름이나 접근되는 속성의 이름.

The __name__ attribute of nested functions, classes, and type aliases is however not mangled.  
내부 함수, 클래스 및 타입 별칭의 __name__ 속성은 맹글링되지 않습니다.

The name of imported modules, e.g., __spam in import __spam. If the module is part of a package (i.e., its name contains a dot), the name is not mangled, e.g., the __foo in import __foo.bar is not mangled.  
가져온 모듈의 이름(예: import __spam에서의 __spam)도 해당되나, 모듈이 패키지의 일부(즉, 이름에 점이 포함된 경우)라면 맹글링되지 않습니다(예: import __foo.bar에서의 __foo는 맹글링되지 않음).

The name of an imported member, e.g., __f in from spam import __f.  
가져온 멤버의 이름(예: from spam import __f에서의 __f)도 마찬가지입니다.

The transformation rule is defined as follows:  
변환 규칙은 다음과 같이 정의됩니다:  

The class name, with leading underscores removed and a single leading underscore inserted, is inserted in front of the identifier, e.g., the identifier __spam occurring in a class named Foo, _Foo or __Foo is transformed to _Foo__spam.  
클래스 이름에서 선행 밑줄을 제거한 후 단 하나의 밑줄을 삽입한 것이 식별자 앞에 붙여집니다. 예를 들어, Foo, _Foo, 또는 __Foo라는 클래스 내의 __spam은 _Foo__spam으로 변환됩니다.

If the class name consists only of underscores, the transformation is the identity, e.g., the identifier __spam occurring in a class named _ or __ is left as is.  
클래스 이름이 오직 밑줄로만 구성된 경우 변환은 항등 함수가 되어, 예를 들어 _ 또는 __라는 클래스 내의 __spam은 그대로 둡니다.

## 6.2.2. Literals  
6.2.2. 리터럴  
Python supports string and bytes literals and various numeric literals:  
파이썬은 문자열 및 바이트 리터럴과 여러 숫자 리터럴을 지원합니다:

  literal ::= stringliteral | bytesliteral  
        | integer | floatnumber | imagnumber  
  literal ::= stringliteral | bytesliteral
        | 정수 | 부동소수점수 | 허수

Evaluation of a literal yields an object of the given type (string, bytes, integer, floating-point number, complex number) with the given value.  
리터럴의 평가는 해당 값과 함께 주어진 타입(문자열, 바이트, 정수, 부동 소수점 수, 복소수)의 객체를 반환합니다.  
The value may be approximated in the case of floating-point and imaginary (complex) literals.  
부동 소수점 및 허수 리터럴의 경우 값이 근사될 수 있습니다.  
See section Literals for details.  
자세한 내용은 리터럴 섹션을 참조하십시오.

All literals correspond to immutable data types, and hence the object’s identity is less important than its value.  
모든 리터럴은 불변 데이터 타입에 해당하므로, 객체의 정체성보다 그 값이 더 중요합니다.  
Multiple evaluations of literals with the same value (either the same occurrence in the program text or a different occurrence) may obtain the same object or a different object with the same value.  
프로그램 텍스트 내의 동일한 값의 리터럴(동일한 위치거나 다른 위치)이 같은 객체를 반환하거나 값은 같지만 다른 객체를 반환할 수 있습니다.

## 6.2.3. Parenthesized forms  
6.2.3. 괄호로 묶인 형태  
A parenthesized form is an optional expression list enclosed in parentheses:  
괄호로 묶인 형태는 괄호로 감싸진 선택적 표현식 목록입니다:

  parenth_form ::= "(" [starred_expression] ")"  
  parenth_form ::= "(" [starred_expression] ")"

A parenthesized expression list yields whatever that expression list yields: if the list contains at least one comma, it yields a tuple; otherwise, it yields the single expression that makes up the expression list.  
괄호로 묶인 표현식 목록은 그 표현식 목록이 반환하는 것을 그대로 반환합니다: 만약 목록에 하나 이상의 콤마가 포함되어 있으면 튜플을 반환하고, 그렇지 않으면 단일 표현식을 반환합니다.

An empty pair of parentheses yields an empty tuple object.  
빈 괄호 쌍은 빈 튜플 객체를 반환합니다.  
Since tuples are immutable, the same rules as for literals apply (i.e., two occurrences of the empty tuple may or may not yield the same object).  
튜플은 불변이므로 리터럴과 동일한 규칙이 적용됩니다(즉, 빈 튜플의 두 번의 발생이 동일한 객체를 반환할 수도, 다를 수도 있습니다).

Note that tuples are not formed by the parentheses, but rather by use of the comma.  
튜플은 괄호에 의해 만들어지는 것이 아니라 콤마에 의해 만들어집니다.  
The exception is the empty tuple, for which parentheses are required — allowing unparenthesized “nothing” in expressions would cause ambiguities and allow common typos to pass uncaught.  
예외는 빈 튜플이며, 이 경우 괄호가 필요합니다 — 괄호 없이 “아무것도 없음”을 허용하면 모호성을 야기하고 흔한 오타를 감지하지 못하게 됩니다.

## 6.2.4. Displays for lists, sets and dictionaries  
6.2.4. 리스트, 집합, 딕셔너리 디스플레이  
For constructing a list, a set or a dictionary Python provides special syntax called “displays”, each of them in two flavors:  
파이썬은 리스트, 집합, 딕셔너리를 구성하기 위해 각각 두 가지 방식으로 “디스플레이(display)”라는 특별한 문법을 제공합니다:  

either the container contents are listed explicitly, or  
컨테이너 내용이 명시적으로 나열되거나,  

they are computed via a set of looping and filtering instructions, called a comprehension.  
comprehension이라 불리는 일련의 반복 및 필터링 지시문을 통해 계산됩니다.

Common syntax elements for comprehensions are:  
컴프리헨션의 공통 구문 요소는 다음과 같습니다:

  comprehension ::= assignment_expression comp_for  
  comprehension ::= assignment_expression comp_for  
  comp_for      ::= ["async"] "for" target_list "in" or_test [comp_iter]  
  comp_for      ::= ["async"] "for" target_list "in" or_test [comp_iter]  
  comp_iter     ::= comp_for | comp_if  
  comp_iter     ::= comp_for | comp_if  
  comp_if       ::= "if" or_test [comp_iter]  
  comp_if       ::= "if" or_test [comp_iter]

The comprehension consists of a single expression followed by at least one for clause and zero or more for or if clauses.  
컴프리헨션은 하나의 표현식과 그 뒤에 최소 한 개의 for 절 및 0개 이상의 for 혹은 if 절로 구성됩니다.  
In this case, the elements of the new container are those that would be produced by considering each of the for or if clauses a block, nesting from left to right, and evaluating the expression to produce an element each time the innermost block is reached.  
이 경우, 새 컨테이너의 요소는 각각의 for 혹은 if 절을 블록으로 간주하고, 왼쪽에서 오른쪽으로 중첩하여, 가장 안쪽 블록에 도달할 때마다 표현식을 평가하여 생성된 요소가 됩니다.

However, aside from the iterable expression in the leftmost for clause, the comprehension is executed in a separate implicitly nested scope.  
그러나 가장 왼쪽 for 절의 반복 가능한 표현식을 제외하고, 컴프리헨션은 별도의 암시적 중첩 스코프에서 실행됩니다.  
This ensures that names assigned to in the target list don’t “leak” into the enclosing scope.  
이로써 대상 리스트에서 할당된 이름이 둘러싸는 스코프로 “새어나가는” 일이 방지됩니다.

The iterable expression in the leftmost for clause is evaluated directly in the enclosing scope and then passed as an argument to the implicitly nested scope.  
가장 왼쪽 for 절의 반복 가능한 표현식은 둘러싸는 스코프에서 직접 평가된 후, 암시적으로 중첩된 스코프로 인자로 전달됩니다.  
Subsequent for clauses and any filter condition in the leftmost for clause cannot be evaluated in the enclosing scope as they may depend on the values obtained from the leftmost iterable.  
가장 왼쪽의 반복 가능한 표현식에서 얻은 값에 의존할 수 있으므로 이후의 for 절과 필터 조건은 둘러싸는 스코프에서 평가될 수 없습니다.  
For example: [x*y for x in range(10) for y in range(x, x+10)].  
예를 들어: [x*y for x in range(10) for y in range(x, x+10)].

To ensure the comprehension always results in a container of the appropriate type, yield and yield from expressions are prohibited in the implicitly nested scope.  
컴프리헨션이 항상 적절한 타입의 컨테이너를 반환하도록 하기 위해, 암시적 중첩 스코프에서는 yield 및 yield from 표현식이 금지됩니다.

Since Python 3.6, in an async def function, an async for clause may be used to iterate over a asynchronous iterator.  
파이썬 3.6부터 async def 함수 내에서는 비동기 반복자를 순회하기 위해 async for 절을 사용할 수 있습니다.  
A comprehension in an async def function may consist of either a for or async for clause following the leading expression, may contain additional for or async for clauses, and may also use await expressions.  
async def 함수 안의 컴프리헨션은 선행 표현식 뒤에 for 또는 async for 절을 포함할 수 있으며, 추가 for 또는 async for 절, 그리고 await 표현식도 사용할 수 있습니다.

If a comprehension contains async for clauses, or if it contains await expressions or other asynchronous comprehensions anywhere except the iterable expression in the leftmost for clause, it is called an asynchronous comprehension.  
컴프리헨션이 async for 절을 포함하거나, 가장 왼쪽 for 절의 반복 표현식을 제외한 어디에서든 await 표현식이나 다른 비동기 컴프리헨션을 포함하면 이를 비동기 컴프리헨션이라고 합니다.  
An asynchronous comprehension may suspend the execution of the coroutine function in which it appears.  
비동기 컴프리헨션은 자신이 포함된 코루틴 함수의 실행을 일시 중단할 수 있습니다.  
See also PEP 530.  
PEP 530도 참조하십시오.

Added in version 3.6: Asynchronous comprehensions were introduced.  
버전 3.6에서 추가됨: 비동기 컴프리헨션이 도입되었습니다.

Changed in version 3.8: yield and yield from prohibited in the implicitly nested scope.  
버전 3.8에서 변경됨: 암시적 중첩 스코프에서 yield 및 yield from이 금지되었습니다.

Changed in version 3.11: Asynchronous comprehensions are now allowed inside comprehensions in asynchronous functions. Outer comprehensions implicitly become asynchronous.  
버전 3.11에서 변경됨: 비동기 함수 내의 컴프리헨션 안에서 비동기 컴프리헨션이 허용되며, 외부 컴프리헨션은 암시적으로 비동기가 됩니다.

## 6.2.5. List displays  
6.2.5. 리스트 디스플레이  
A list display is a possibly empty series of expressions enclosed in square brackets:  
리스트 디스플레이는 대괄호로 감싸진, 비어 있을 수도 있는 표현식들의 나열입니다:  
  list_display ::= "[" [flexible_expression_list | comprehension] "]"  
    list_display ::= "[" [flexible_expression_list | comprehension] "]"  
A list display yields a new list object, the contents being specified by either a list of expressions or a comprehension.  
리스트 디스플레이는 표현식들의 목록 또는 컴프리헨션으로 지정되는 내용을 갖는 새로운 리스트 객체를 생성합니다.  
When a comma‑separated list of expressions is supplied, its elements are evaluated from left to right and placed into the list object in that order.  
콤마로 구분된 표현식 목록이 제공되면, 그 요소들은 왼쪽에서 오른쪽 순서대로 평가되어 리스트 객체에 차례대로 삽입됩니다.  
When a comprehension is supplied, the list is constructed from the elements resulting from the comprehension.  
컴프리헨션이 제공되면, 리스트는 컴프리헨션으로부터 생성된 요소들로 구성됩니다.

## 6.2.6. Set displays  
6.2.6. 집합 디스플레이  
A set display is denoted by curly braces and distinguishable from dictionary displays by the lack of colons separating keys and values:  
집합 디스플레이는 중괄호로 표기되며, 키와 값 사이에 콜론이 없다는 점에서 딕셔너리 디스플레이와 구별됩니다:  
  set_display ::= "{" (flexible_expression_list | comprehension) "}"  
    set_display ::= "{" (flexible_expression_list | comprehension) "}"  
A set display yields a new mutable set object, the contents being specified by either a sequence of expressions or a comprehension.  
집합 디스플레이는 표현식들의 시퀀스 또는 컴프리헨션으로 지정되는 내용을 갖는 새로운 변경 가능한 집합 객체를 생성합니다.  
When a comma‑separated list of expressions is supplied, its elements are evaluated from left to right and added to the set object.  
콤마로 구분된 표현식 목록이 제공되면, 그 요소들은 왼쪽에서 오른쪽 순서대로 평가되어 집합 객체에 추가됩니다.  
When a comprehension is supplied, the set is constructed from the elements resulting from the comprehension.  
컴프리헨션이 제공되면, 집합은 컴프리헨션으로부터 생성된 요소들로 구성됩니다.  
An empty set cannot be constructed with {}; this literal constructs an empty dictionary.  
빈 집합은 {}로 생성할 수 없으며, {}는 빈 딕셔너리를 생성합니다.

## 6.2.7. Dictionary displays  
6.2.7. 딕셔너리 디스플레이  
A dictionary display is a possibly empty series of dict items (key/value pairs) enclosed in curly braces:  
딕셔너리 디스플레이는 중괄호로 감싸진, 비어 있을 수도 있는 딕셔너리 항목(키/값 쌍)들의 나열입니다:  
  dict_display       ::= "{" [dict_item_list | dict_comprehension] "}"  
    dict_display       ::= "{" [dict_item_list | dict_comprehension] "}"  
  dict_item_list     ::= dict_item ("," dict_item)* [","]  
    dict_item_list     ::= dict_item ("," dict_item)* [","]  
  dict_item          ::= expression ":" expression | "**" or_expr  
    dict_item          ::= expression ":" expression | "**" or_expr  
  dict_comprehension ::= expression ":" expression comp_for  
    dict_comprehension ::= expression ":" expression comp_for  
A dictionary display yields a new dictionary object.  
딕셔너리 디스플레이는 새로운 딕셔너리 객체를 생성합니다.  
If a comma‑separated sequence of dict items is given, they are evaluated from left to right to define the entries of the dictionary: each key object is used as a key into the dictionary to store the corresponding value.  
콤마로 구분된 딕셔너리 항목의 시퀀스가 주어지면, 항목들은 왼쪽에서 오른쪽 순서대로 평가되어 딕셔너리의 항목을 정의합니다: 각 키 객체는 해당 값이 저장될 딕셔너리의 키로 사용됩니다.  
This means that you can specify the same key multiple times in the dict item list, and the final dictionary’s value for that key will be the last one given.  
즉, 딕셔너리 항목 목록에서 동일한 키를 여러 번 지정할 수 있으며, 해당 키에 대한 최종 딕셔너리 값은 마지막에 주어진 값이 됩니다.  
A double asterisk ** denotes dictionary unpacking. Its operand must be a mapping. Each mapping item is added to the new dictionary. Later values replace values already set by earlier dict items and earlier dictionary unpackings.  
이중 별표(**)는 딕셔너리 언패킹을 나타냅니다. 그 피연산자는 매핑이어야 하며, 매핑의 각 항목은 새로운 딕셔너리에 추가됩니다. 이후의 값들은 이전 딕셔너리 항목이나 언패킹으로 설정된 값을 대체합니다.  
Added in version 3.5: Unpacking into dictionary displays, originally proposed by PEP 448.  
버전 3.5에서 추가됨: PEP 448에서 제안된 대로 딕셔너리 디스플레이로의 언패킹이 도입되었습니다.  
A dict comprehension, in contrast to list and set comprehensions, needs two expressions separated with a colon followed by the usual “for” and “if” clauses.  
딕셔너리 컴프리헨션은 리스트와 집합 컴프리헨션과 달리, 두 개의 표현식을 콜론으로 구분한 후 일반적인 “for” 및 “if” 절이 이어져야 합니다.  
When the comprehension is run, the resulting key and value elements are inserted in the new dictionary in the order they are produced.  
컴프리헨션이 실행될 때, 생성된 키와 값 요소들은 그 순서대로 새로운 딕셔너리에 삽입됩니다.

## 6.2.8. Generator expressions  
6.2.8. 제너레이터 표현식  
A generator expression is a compact generator notation in parentheses:  
제너레이터 표현식은 괄호로 감싼 간결한 제너레이터 표기법입니다:  
  generator_expression ::= "(" expression comp_for ")"  
    generator_expression ::= "(" expression comp_for ")"  
A generator expression yields a new generator object. Its syntax is the same as for comprehensions, except that it is enclosed in parentheses instead of brackets or curly braces.  
제너레이터 표현식은 새로운 제너레이터 객체를 생성하며, 그 구문은 컴프리헨션과 동일하되 대괄호나 중괄호 대신 괄호로 둘러싸입니다.  
Variables used in the generator expression are evaluated lazily when the __next__() method is called for the generator object (in the same fashion as normal generators).  
제너레이터 표현식에 사용되는 변수들은 일반 제너레이터와 같은 방식으로, 제너레이터 객체에서 __next__() 메서드가 호출될 때 지연 평가됩니다.  
However, the iterable expression in the leftmost for clause is immediately evaluated, so that an error produced by it will be emitted at the point where the generator expression is defined, rather than at the point where the first value is retrieved.  
하지만 가장 왼쪽 for 절의 반복 가능한 표현식은 즉시 평가되어, 해당 표현식에서 발생한 오류가 첫 번째 값이 반환되는 시점이 아니라 제너레이터 표현식이 정의된 시점에서 발생하게 됩니다.  
Subsequent for clauses and any filter condition in the leftmost for clause cannot be evaluated in the enclosing scope as they may depend on the values obtained from the leftmost iterable.  
이후의 for 절과 가장 왼쪽 for 절의 필터 조건은 가장 왼쪽 반복 가능 표현식으로부터 얻은 값에 의존할 수 있으므로 둘러싸는 스코프에서 평가될 수 없습니다.  
For example: (x*y for x in range(10) for y in range(x, x+10)).  
예를 들어: (x*y for x in range(10) for y in range(x, x+10)).  
The parentheses can be omitted on calls with only one argument. See section Calls for details.  
인수가 하나만 있는 호출에서는 괄호를 생략할 수 있습니다. 자세한 내용은 Calls 섹션을 참조하세요.  
To avoid interfering with the expected operation of the generator expression itself, yield and yield from expressions are prohibited in the implicitly defined generator.  
제너레이터 표현식의 정상 작동에 방해가 되지 않도록 하기 위해, 암시적으로 정의된 제너레이터 내에서는 yield 및 yield from 표현식이 금지됩니다.  
If a generator expression contains either async for clauses or await expressions it is called an asynchronous generator expression.  
만약 제너레이터 표현식이 async for 절이나 await 표현식을 포함하면, 이는 비동기 제너레이터 표현식이라고 합니다.  
An asynchronous generator expression returns a new asynchronous generator object, which is an asynchronous iterator (see Asynchronous Iterators).  
비동기 제너레이터 표현식은 새로운 비동기 제너레이터 객체를 반환하며, 이는 비동기 반복자입니다(Asynchronous Iterators 참조).  
Added in version 3.6: Asynchronous generator expressions were introduced.  
버전 3.6에서 추가됨: 비동기 제너레이터 표현식이 도입되었습니다.  
Changed in version 3.7: Prior to Python 3.7, asynchronous generator expressions could only appear in async def coroutines. Starting with 3.7, any function can use asynchronous generator expressions.  
버전 3.7에서 변경됨: 파이썬 3.7 이전에는 async def 코루틴에서만 비동기 제너레이터 표현식이 나타날 수 있었지만, 3.7부터는 모든 함수에서 비동기 제너레이터 표현식을 사용할 수 있게 되었습니다.  
Changed in version 3.8: yield and yield from prohibited in the implicitly nested scope.  
버전 3.8에서 변경됨: 암시적으로 중첩된 스코프 내에서 yield 및 yield from이 금지되었습니다.

## 6.2.9. Yield expressions  
6.2.9. yield 표현식  
  yield_atom       ::= "(" yield_expression ")"  
  yield_from       ::= "yield" "from" expression  
  yield_expression ::= "yield" yield_list | yield_from  
yield 표현식은 제너레이터 함수 또는 비동기 제너레이터 함수를 정의할 때 사용되며, 함수 본문 내에서만 사용할 수 있습니다.  
yield 표현식은 제너레이터 함수나 비동기 제너레이터 함수를 정의할 때 사용되므로, 오직 함수 정의의 본문에서만 사용할 수 있습니다.  
Using a yield expression in a function’s body causes that function to be a generator function, and using it in an async def function’s body causes that coroutine function to be an asynchronous generator function.  
함수 본문에서 yield 표현식을 사용하면 그 함수는 제너레이터 함수가 되고, async def 함수 본문에서 사용하면 그 코루틴 함수는 비동기 제너레이터 함수가 됩니다.  
For example:  
예를 들어:  

  def gen():  # defines a generator function  
    yield 123  
    
  async def agen(): # defines an asynchronous generator function  
    yield 123  
Due to their side effects on the containing scope, yield expressions are not permitted as part of the implicitly defined scopes used to implement comprehensions and generator expressions.  
포함된 스코프에 미치는 부작용 때문에, yield 표현식은 컴프리헨션과 제너레이터 표현식을 구현하는 데 사용되는 암시적 스코프의 일부로 허용되지 않습니다.  
Changed in version 3.8: Yield expressions prohibited in the implicitly nested scopes used to implement comprehensions and generator expressions.  
버전 3.8에서 변경됨: 컴프리헨션과 제너레이터 표현식을 구현하는 암시적으로 중첩된 스코프에서 yield 표현식이 금지되었습니다.  
Generator functions are described below, while asynchronous generator functions are described separately in section Asynchronous generator functions.  
제너레이터 함수는 아래에서 설명되며, 비동기 제너레이터 함수는 Asynchronous generator functions 섹션에서 별도로 설명됩니다.  
When a generator function is called, it returns an iterator known as a generator. That generator then controls the execution of the generator function.  
제너레이터 함수를 호출하면, 제너레이터라고 하는 반복자가 반환되고, 이 제너레이터가 제너레이터 함수의 실행을 제어합니다.  
The execution starts when one of the generator’s methods is called. At that time, the execution proceeds to the first yield expression, where it is suspended again, returning the value of yield_list to the generator’s caller, or None if yield_list is omitted.  
실행은 제너레이터의 메서드 중 하나가 호출될 때 시작되며, 그 시점에서 실행은 첫 번째 yield 표현식까지 진행되고, 다시 일시 중단되어 yield_list의 값(또는 yield_list가 생략되었으면 None)을 제너레이터 호출자에게 반환합니다.  
By “suspended” we mean that all local state is retained, including the current bindings of local variables, the instruction pointer, the internal evaluation stack, and the state of any exception handling.  
“일시 중단된다”는 것은 지역 변수의 현재 바인딩, 명령 포인터, 내부 평가 스택, 그리고 모든 예외 처리 상태가 유지됨을 의미합니다.  
When execution is resumed by calling one of the generator’s methods, the function proceeds as if the yield expression were just another external call.  
제너레이터의 메서드를 호출하여 실행이 재개되면, 함수는 마치 yield 표현식이 또 다른 외부 호출인 것처럼 계속 진행됩니다.  
The value of the yield expression after resuming depends on the method used: if __next__() is invoked (typically via a for loop or next() builtin) then the result is None; otherwise, if send() is used, then the result is the value passed to that method.  
재개 후 yield 표현식의 값은 사용된 메서드에 따라 달라지며, __next__()가 호출되면(주로 for 루프나 next() 내장 함수를 통해) 결과는 None이 되고, send()가 사용되면 그 메서드에 전달된 값이 결과가 됩니다.  
All of this makes generator functions quite similar to coroutines; they yield multiple times, have more than one entry point, and their execution can be suspended.  
이 모든 것은 제너레이터 함수를 코루틴과 매우 유사하게 만드는데, 이들은 여러 번 yield하고, 하나 이상의 진입점을 가지며, 실행이 일시 중단될 수 있습니다.  
The only difference is that a generator function cannot control where execution should continue after yielding; control is always transferred to the generator’s caller.  
유일한 차이는 제너레이터 함수가 yield 이후 실행이 어디서 계속되어야 하는지를 제어할 수 없고, 항상 제너레이터의 호출자에게 제어가 넘어간다는 점입니다.  
Yield expressions are allowed anywhere in a try construct.  
yield 표현식은 try 구문 내의 어디서든 허용됩니다.  
If the generator is not resumed before it is finalized (by reaching a zero reference count or being garbage collected), the generator's close() method is called, allowing any pending finally clauses to execute.  
제너레이터가 종결되기 전에(참조 카운트가 0이 되거나 가비지 컬렉션에 의해) 재개되지 않으면, 제너레이터의 close() 메서드가 호출되어 대기 중인 finally 절들이 실행될 수 있습니다.  
When yield from <expr> is used, the supplied expression must be an iterable.  
yield from <expr>이 사용될 때, 제공된 표현식은 반복 가능한 객체여야 합니다.  
The values produced by iterating that iterable are passed directly to the caller of the current generator’s methods.  
해당 반복 가능한 객체를 순회하면서 생성되는 값들은 현재 제너레이터의 메서드 호출자에게 직접 전달됩니다.  
Any values passed with send() and exceptions passed with throw() are forwarded to the underlying iterator if it supports them; otherwise, send() raises AttributeError or TypeError, and throw() raises the supplied exception immediately.  
send()로 전달된 값과 throw()로 전달된 예외는, 해당 반복자가 이를 지원하면 하위 반복자로 전달되고, 그렇지 않으면 send()는 AttributeError 또는 TypeError를 발생시키며, throw()는 즉시 전달된 예외를 발생시킵니다.  
When the underlying iterator is exhausted, the value attribute of the raised StopIteration becomes the value of the yield expression.  
하위 반복자가 소진되면, 발생한 StopIteration의 value 속성이 yield 표현식의 값이 됩니다.  
This value may be set explicitly when raising StopIteration or automatically when the subiterator is a generator (by returning a value from it).  
이 값은 StopIteration을 발생시킬 때 명시적으로 설정되거나, 하위 반복자가 제너레이터일 경우(제너레이터에서 값을 반환함으로써) 자동으로 설정될 수 있습니다.  
Changed in version 3.3: Added yield from <expr> to delegate control flow to a subiterator.  
버전 3.3에서 변경됨: yield from <expr>를 추가하여 제어 흐름을 하위 반복자로 위임하도록 하였습니다.  
The parentheses may be omitted when the yield expression is the sole expression on the right-hand side of an assignment statement.  
yield 표현식이 할당문의 오른쪽에 유일한 표현식으로 있을 때는 괄호를 생략할 수 있습니다.

See also  
  PEP 255 - Simple Generators  
  PEP 342 - Coroutines via Enhanced Generators  
  PEP 380 - Syntax for Delegating to a Subgenerator  
  PEP 525 - Asynchronous Generators  
  참고: PEP 255 - Simple Generators, PEP 342 - Coroutines via Enhanced Generators, PEP 380 - Syntax for Delegating to a Subgenerator, PEP 525 - Asynchronous Generators

## 6.2.9.1. Generator-iterator methods  
6.2.9.1. 제너레이터-반복자 메서드  
This subsection describes the methods of a generator iterator. They can be used to control the execution of a generator function.  
이 하위 섹션은 제너레이터 반복자의 메서드들을 설명하며, 이들은 제너레이터 함수의 실행을 제어하는 데 사용될 수 있습니다.

Note that calling any of the generator methods below when the generator is already executing raises a ValueError exception.  
이미 실행 중인 제너레이터에서 아래의 메서드를 호출하면 ValueError 예외가 발생함을 주의하십시오.

generator.__next__()  
Starts the execution of a generator function or resumes it at the last executed yield expression. When a generator function is resumed with a __next__() method, the current yield expression always evaluates to None. The execution then continues to the next yield expression, where the generator is suspended again, and the value of the yield_list is returned to __next__()’s caller. If the generator exits without yielding another value, a StopIteration exception is raised.  
generator.__next__()  
제너레이터 함수의 실행을 시작하거나 마지막에 실행된 yield 표현식에서 재개합니다. __next__() 메서드로 제너레이터 함수가 재개되면, 현재 yield 표현식의 값은 항상 None으로 평가됩니다. 이후 실행은 다음 yield 표현식까지 진행되고, 그 지점에서 제너레이터가 일시 중단되며, yield_list의 값이 __next__()를 호출한 측에 반환됩니다. 제너레이터가 다른 값을 yield하지 않고 종료되면 StopIteration 예외가 발생합니다.

This method is normally called implicitly, e.g. by a for loop, or by the built-in next() function.  
이 메서드는 보통 for 루프나 내장 함수 next()에 의해 암시적으로 호출됩니다.

generator.send(value)  
Resumes the execution and “sends” a value into the generator function. The value argument becomes the result of the current yield expression. The send() method returns the next value yielded by the generator, or raises StopIteration if the generator exits without yielding another value. When send() is called to start the generator, it must be called with None as the argument, because there is no yield expression that could receive the value.  
generator.send(value)  
실행을 재개하며, 제너레이터 함수로 값을 “전달”합니다. value 인수는 현재 yield 표현식의 결과가 됩니다. send() 메서드는 제너레이터가 다음에 yield한 값을 반환하거나, 제너레이터가 다른 값을 yield하지 않고 종료되면 StopIteration 예외를 발생시킵니다. 제너레이터를 시작하기 위해 send()를 호출할 때는, 수신할 yield 표현식이 없으므로 반드시 None을 인수로 전달해야 합니다.

generator.throw(value)  
generator.throw(type[, value[, traceback]])  
Raises an exception at the point where the generator was paused, and returns the next value yielded by the generator function. If the generator exits without yielding another value, a StopIteration exception is raised. If the generator function does not catch the passed-in exception, or raises a different exception, then that exception propagates to the caller.  
generator.throw(value)  
generator.throw(type[, value[, traceback]])  
제너레이터가 일시 중단된 지점에서 예외를 발생시키고 제너레이터 함수가 yield하는 다음 값을 반환합니다. 제너레이터가 다른 값을 yield하지 않고 종료되면 StopIteration 예외가 발생합니다. 만약 제너레이터 함수가 전달된 예외를 처리하지 않거나 다른 예외를 발생시키면, 그 예외는 호출자에게 전파됩니다.

For backwards compatibility, however, the second signature is supported, following a convention from older versions of Python. The type argument should be an exception class, and value should be an exception instance. If the value is not provided, the type constructor is called to get an instance. If traceback is provided, it is set on the exception, otherwise any existing __traceback__ attribute stored in value may be cleared.  
단, 이전 버전과의 호환성을 위해 두 번째 시그니처가 지원되며, 이는 파이썬 옛 버전의 관례를 따릅니다. type 인수는 예외 클래스여야 하며, value는 예외 인스턴스여야 합니다. value가 제공되지 않으면, type 생성자가 호출되어 인스턴스를 얻습니다. traceback이 제공되면 예외에 설정되며, 그렇지 않으면 value에 저장된 기존 __traceback__ 속성이 지워질 수 있습니다.

Changed in version 3.12: The second signature (type[, value[, traceback]]) is deprecated and may be removed in a future version of Python.  
버전 3.12에서 변경됨: 두 번째 시그니처 (type[, value[, traceback]])는 더 이상 권장되지 않으며, 향후 버전에서 제거될 수 있습니다.

generator.close()  
Raises a GeneratorExit at the point where the generator function was paused. If the generator function catches the exception and returns a value, this value is returned from close(). If the generator function is already closed, or raises GeneratorExit (by not catching the exception), close() returns None. If the generator yields a value, a RuntimeError is raised. If the generator raises any other exception, it is propagated to the caller. If the generator has already exited due to an exception or normal exit, close() returns None and has no other effect.  
generator.close()  
제너레이터 함수가 일시 중단된 지점에서 GeneratorExit 예외를 발생시킵니다. 만약 제너레이터 함수가 예외를 처리하고 값을 반환하면, 그 값이 close()의 반환값이 됩니다. 제너레이터 함수가 이미 종료되었거나, GeneratorExit 예외를 발생시키면(close()에서 예외를 처리하지 않으면) close()는 None을 반환합니다. 제너레이터가 값을 yield하면 RuntimeError가 발생하며, 다른 예외가 발생하면 호출자에게 전파됩니다. 제너레이터가 예외 또는 정상 종료로 인해 이미 종료된 경우, 이후의 close() 호출은 아무 효과 없이 None을 반환합니다.

Changed in version 3.13: If a generator returns a value upon being closed, the value is returned by close().  
버전 3.13에서 변경됨: 제너레이터가 종료 시 값을 반환하면, 그 값이 close()의 반환값으로 반환됩니다.

## 6.2.9.2. Examples  
6.2.9.2. 예제  
Here is a simple example that demonstrates the behavior of generators and generator functions:  
다음은 제너레이터와 제너레이터 함수의 동작을 보여주는 간단한 예제입니다:

  >>>
  def echo(value=None):
      print("Execution starts when 'next()' is called for the first time.")
      try:
          while True:
              try:
                  value = (yield value)
              except Exception as e:
                  value = e
      finally:
          print("Don't forget to clean up when 'close()' is called.")
  
  generator = echo(1)
  print(next(generator))
  # Execution starts when 'next()' is called for the first time.
  # 1
  print(next(generator))
  # None
  print(generator.send(2))
  # 2
  generator.throw(TypeError, "spam")
  # TypeError('spam',)
  generator.close()
  # Don't forget to clean up when 'close()' is called.
For examples using yield from, see PEP 380: Syntax for Delegating to a Subgenerator in “What’s New in Python.”  
yield from을 사용하는 예제는 “What’s New in Python”의 PEP 380: Syntax for Delegating to a Subgenerator를 참조하십시오.

## 6.2.9.3. Asynchronous generator functions  
6.2.9.3. 비동기 제너레이터 함수  
The presence of a yield expression in a function or method defined using async def further defines the function as an asynchronous generator function.  
async def로 정의된 함수나 메서드에 yield 표현식이 존재하면, 해당 함수는 비동기 제너레이터 함수로 정의됩니다.

When an asynchronous generator function is called, it returns an asynchronous iterator known as an asynchronous generator object. That object then controls the execution of the generator function. An asynchronous generator object is typically used in an async for statement in a coroutine function analogously to how a generator object would be used in a for statement.  
비동기 제너레이터 함수를 호출하면, 비동기 제너레이터 객체라고 하는 비동기 반복자가 반환되고, 이 객체가 제너레이터 함수의 실행을 제어합니다. 비동기 제너레이터 객체는 일반 제너레이터 객체가 for 문에서 사용되는 것과 유사하게, 코루틴 함수 내의 async for 문에서 사용됩니다.

Calling one of the asynchronous generator’s methods returns an awaitable object, and the execution starts when this object is awaited on. At that time, the execution proceeds to the first yield expression, where it is suspended again, returning the value of yield_list to the awaiting coroutine.  
비동기 제너레이터의 메서드를 호출하면 awaitable 객체가 반환되며, 이 객체가 await될 때 실행이 시작됩니다. 그 시점에서 실행은 첫 번째 yield 표현식까지 진행되고, yield_list의 값이 await하는 코루틴에 반환되며 다시 일시 중단됩니다.

As with a generator, suspension means that all local state is retained, including the current bindings of local variables, the instruction pointer, the internal evaluation stack, and the state of any exception handling. When the execution is resumed by awaiting on the next object returned by the asynchronous generator’s methods, the function can proceed exactly as if the yield expression were just another external call. The value of the yield expression after resuming depends on the method which resumed the execution. If __anext__() is used then the result is None. Otherwise, if asend() is used, then the result will be the value passed in to that method.  
제너레이터와 마찬가지로, 일시 중단은 지역 변수의 현재 바인딩, 명령 포인터, 내부 평가 스택, 예외 처리 상태 등 모든 지역 상태가 유지됨을 의미합니다. 이후 비동기 제너레이터의 메서드가 반환한 다음 객체를 await하여 실행이 재개되면, yield 표현식이 또 다른 외부 호출처럼 작동하며, 재개 된 후 yield 표현식의 값은 재개에 사용된 메서드에 따라 결정됩니다. __anext__()가 사용되면 결과는 None, asend()가 사용되면 전달된 값이 결과가 됩니다.

If an asynchronous generator happens to exit early by break, the caller task being cancelled, or other exceptions, the generator’s async cleanup code will run and possibly raise exceptions or access context variables in an unexpected context–perhaps after the lifetime of tasks it depends, or during the event loop shutdown when the async-generator garbage collection hook is called. To prevent this, the caller must explicitly close the async generator by calling aclose() method to finalize the generator and ultimately detach it from the event loop.  
만약 비동기 제너레이터가 break, 호출된 태스크의 취소 또는 기타 예외로 인해 조기에 종료된다면, 제너레이터의 비동기 정리 코드가 실행되어 예외가 발생하거나 예기치 않은 컨텍스트에서 컨텍스트 변수를 접근할 수 있습니다. (예를 들어, 제너레이터가 의존하는 태스크의 수명 이후 또는 이벤트 루프 종료 시에) 이를 방지하기 위해 호출자는 반드시 aclose() 메서드를 호출하여 비동기 제너레이터를 명시적으로 종료하고, 최종적으로 이를 이벤트 루프로부터 분리해야 합니다.

In an asynchronous generator function, yield expressions are allowed anywhere in a try construct. However, if an asynchronous generator is not resumed before it is finalized (by reaching a zero reference count or by being garbage collected), then a yield expression within a try construct could result in a failure to execute pending finally clauses. In this case, it is the responsibility of the event loop or scheduler running the asynchronous generator to call the asynchronous generator-iterator’s aclose() method and run the resulting coroutine object, thus allowing any pending finally clauses to execute.  
비동기 제너레이터 함수 내에서는 try 구문 어디서든 yield 표현식이 허용됩니다. 다만, 비동기 제너레이터가 종료(참조 카운트 0 또는 가비지 컬렉션) 전에 재개되지 않으면, try 구문 내의 yield 표현식 때문에 대기 중인 finally 절이 실행되지 않을 수 있습니다. 이 경우 이벤트 루프나 스케줄러가 비동기 제너레이터 반복자의 aclose() 메서드를 호출하고, 반환된 코루틴 객체를 실행하여 대기 중인 finally 절들을 실행해야 합니다.

To take care of finalization upon event loop termination, an event loop should define a finalizer function which takes an asynchronous generator-iterator and presumably calls aclose() and executes the coroutine. This finalizer may be registered by calling sys.set_asyncgen_hooks(). When first iterated over, an asynchronous generator-iterator will store the registered finalizer to be called upon finalization. For a reference example of a finalizer method see the implementation of asyncio.Loop.shutdown_asyncgens in Lib/asyncio/base_events.py.  
이벤트 루프 종료 시 정리를 위해, 이벤트 루프는 비동기 제너레이터 반복자를 인수로 받아 aclose()를 호출하고 코루틴을 실행하는 정리자 함수를 정의해야 합니다. 이 정리자는 sys.set_asyncgen_hooks()를 호출하여 등록될 수 있습니다. 처음 반복될 때, 비동기 제너레이터 반복자는 정리 시 호출될 등록된 정리자를 저장합니다. 정리자 함수의 참고 예제는 Lib/asyncio/base_events.py의 asyncio.Loop.shutdown_asyncgens 구현을 참조하십시오.

The expression yield from <expr> is a syntax error when used in an asynchronous generator function.  
비동기 제너레이터 함수 내에서 yield from <expr>은 구문 오류입니다.

## 6.2.9.4. Asynchronous generator-iterator methods  
6.2.9.4. 비동기 제너레이터 반복자 메서드  
This subsection describes the methods of an asynchronous generator iterator, which are used to control the execution of a generator function.  
이 하위 섹션은 제너레이터 함수의 실행을 제어하는 데 사용되는 비동기 제너레이터 반복자의 메서드들을 설명합니다.

async agen.__anext__()  
Returns an awaitable which when run starts to execute the asynchronous generator or resumes it at the last executed yield expression. When an asynchronous generator function is resumed with an __anext__() method, the current yield expression always evaluates to None in the returned awaitable, which when run will continue to the next yield expression. The value of the yield_list of the yield expression is the value of the StopIteration exception raised by the completing coroutine. If the asynchronous generator exits without yielding another value, the awaitable instead raises a StopAsyncIteration exception, signalling that the asynchronous iteration has completed.  
async agen.__anext__()  
비동기 제너레이터 반복자를 실행하면, awaitable 객체가 반환되며, 이 객체가 실행될 때 비동기 제너레이터의 실행을 시작하거나 마지막 yield 표현식에서 재개됩니다. __anext__() 메서드로 재개될 때, 현재 yield 표현식의 값은 반환된 awaitable 내에서 항상 None으로 평가되며, 실행되면 다음 yield 표현식으로 계속 진행됩니다. yield 표현식의 yield_list 값은 완료된 코루틴이 발생시킨 StopIteration 예외의 값입니다. 비동기 제너레이터가 다른 값을 yield하지 않고 종료되면, awaitable은 대신 StopAsyncIteration 예외를 발생시켜 비동기 반복이 완료되었음을 알립니다.

This method is normally called implicitly by an async for loop.  
이 메서드는 보통 async for 루프에 의해 암시적으로 호출됩니다.

async agen.asend(value)  
Returns an awaitable which when run resumes the execution of the asynchronous generator. As with the send() method for a generator, this “sends” a value into the asynchronous generator function, and the value argument becomes the result of the current yield expression. The awaitable returned by the asend() method will return the next value yielded by the generator as the value of the raised StopIteration, or raises StopAsyncIteration if the asynchronous generator exits without yielding another value. When asend() is called to start the asynchronous generator, it must be called with None as the argument, because there is no yield expression that could receive the value.  
async agen.asend(value)  
비동기 제너레이터의 실행을 재개하고, 제너레이터 함수로 값을 "전달"하는 awaitable 객체를 반환합니다. 제너레이터의 send() 메서드와 마찬가지로, 이 메서드는 value 인수를 통해 현재 yield 표현식의 결과를 결정하며, asend()가 반환하는 awaitable은 제너레이터가 다음에 yield한 값을 StopIteration 예외의 값처럼 반환하거나, 값 없이 종료되면 StopAsyncIteration을 발생시킵니다. 비동기 제너레이터를 시작하기 위해 asend()를 호출할 때는 반드시 None을 인수로 전달해야 합니다.

async agen.athrow(value)  
async agen.athrow(type[, value[, traceback]])  
Returns an awaitable that raises an exception of type type at the point where the asynchronous generator was paused, and returns the next value yielded by the generator function as the value of the raised StopIteration exception. If the asynchronous generator exits without yielding another value, a StopAsyncIteration exception is raised by the awaitable. If the generator function does not catch the passed-in exception, or raises a different exception, then when the awaitable is run that exception propagates to the caller of the awaitable.  
async agen.athrow(value)  
async agen.athrow(type[, value[, traceback]])  
비동기 제너레이터가 일시 중단된 지점에서 type 타입의 예외를 발생시키고, 제너레이터 함수가 yield하는 다음 값을 StopIteration 예외의 값으로 반환하는 awaitable 객체를 반환합니다. 비동기 제너레이터가 다른 값을 yield하지 않고 종료되면, awaitable은 StopAsyncIteration 예외를 발생시킵니다. 제너레이터 함수가 전달된 예외를 처리하지 않거나 다른 예외를 발생시키면, awaitable이 실행될 때 해당 예외가 호출자에게 전파됩니다.

Changed in version 3.12: The second signature (type[, value[, traceback]]) is deprecated and may be removed in a future version of Python.  
버전 3.12에서 변경됨: 두 번째 시그니처 (type[, value[, traceback]])는 더 이상 권장되지 않으며 향후 버전에서 제거될 수 있습니다.

async agen.aclose()  
Returns an awaitable that when run will throw a GeneratorExit into the asynchronous generator function at the point where it was paused. If the asynchronous generator function then exits gracefully, is already closed, or raises GeneratorExit (by not catching the exception), then the returned awaitable will raise a StopIteration exception. Any further awaitables returned by subsequent calls to the asynchronous generator will raise a StopAsyncIteration exception. If the asynchronous generator yields a value, a RuntimeError is raised by the awaitable. If the asynchronous generator raises any other exception, it is propagated to the caller of the awaitable. If the asynchronous generator has already exited due to an exception or normal exit, then further calls to aclose() will return an awaitable that does nothing.  
async agen.aclose()  
비동기 제너레이터 함수가 일시 중단된 지점에서 GeneratorExit 예외를 발생시키는 awaitable 객체를 반환합니다. 이후 제너레이터 함수가 정상적으로 종료되거나 이미 닫혔거나, GeneratorExit을 발생시키면(예외를 처리하지 않음) 반환된 awaitable은 StopIteration 예외를 발생시킵니다. 이후의 호출에서 반환되는 awaitable들은 모두 StopAsyncIteration 예외를 발생시킵니다. 만약 비동기 제너레이터가 값을 yield하면, awaitable은 RuntimeError를 발생시키고, 다른 예외가 발생하면 호출자에게 전파합니다. 제너레이터가 이미 예외 또는 정상 종료로 인해 종료된 경우, 이후 aclose() 호출은 아무런 효과 없이 awaitable을 반환합니다.

## 6.3. Primaries  
6.3. 기본 연산자  
Primaries represent the most tightly bound operations of the language. Their syntax is:  
Primary는 언어에서 가장 높은 우선순위의 연산을 나타냅니다. 구문은 다음과 같습니다:  

  primary ::= atom | attributeref | subscription | slicing | call

## 6.3.1. Attribute references  
6.3.1. 속성 참조  
An attribute reference is a primary followed by a period and a name:  
속성 참조는 primary 뒤에 점(.)과 이름이 오는 형태입니다:  

  attributeref ::= primary "." identifier

The primary must evaluate to an object that supports attribute references (most objects do). The object is asked to produce the attribute whose name is the identifier. Multiple evaluations of the same attribute reference may yield different objects.  
primary는 속성 참조를 지원하는 객체여야 하며, 해당 객체에 identifier에 해당하는 속성을 요청합니다. 동일한 속성 참조의 여러 평가가 서로 다른 객체를 반환할 수 있습니다.

This production can be customized by overriding the __getattribute__() method or the __getattr__() method. If an AttributeError is raised and __getattr__() is defined, it is called as a fallback.  
이 구문은 __getattribute__() 또는 __getattr__() 메서드를 재정의하여 사용자 정의할 수 있습니다. 만약 AttributeError가 발생하고 __getattr__()가 정의되어 있으면 후속 호출로 사용됩니다.

## 6.3.2. Subscriptions  
6.3.2. 서브스크립션  
The subscription of a container instance generally selects an element from it; for a generic class, it usually returns a GenericAlias object.  
컨테이너 인스턴스에 대한 서브스크립션은 일반적으로 그 요소를 선택하며, 제네릭 클래스의 경우 GenericAlias 객체를 반환합니다.

  subscription ::= primary "[" flexible_expression_list "]"

When subscripted, the interpreter evaluates the primary and the expression list. If the expression list contains a comma or any starred expression, it evaluates to a tuple; otherwise, it is the sole member’s value.  
서브스크립션 시, primary와 expression list가 평가됩니다. 만약 expression list에 콤마나 별표 표현식이 있으면 튜플로 평가되고, 그렇지 않으면 유일한 값으로 평가됩니다.

For built-in types, if the primary is a mapping then the expression list must match a key; if it is a sequence then an int or slice is expected.  
내장 타입의 경우, primary가 매핑이면 expression list의 값이 키로 사용되고, 시퀀스이면 정수나 슬라이스여야 합니다.

Changed in version 3.11: Expressions in an expression list may be starred.  
버전 3.11에서 변경됨: expression list 내의 표현식은 별표(*)를 포함할 수 있습니다.

## 6.3.3. Slicings  
6.3.3. 슬라이싱  
A slicing selects a range of items in a sequence (e.g. string, tuple, list) and can be used as an expression or target in assignments/deletions.  
슬라이싱은 문자열, 튜플, 리스트와 같은 시퀀스에서 항목 범위를 선택하며, 표현식 또는 할당/삭제의 대상이 될 수 있습니다.

The syntax for a slicing is:  
슬라이싱의 구문은 다음과 같습니다:

  slicing      ::= primary "[" slice_list "]"  
  slice_list   ::= slice_item ("," slice_item)* [","]  
  slice_item   ::= expression | proper_slice  
  proper_slice ::= [lower_bound] ":" [upper_bound] [ ":" [stride] ]  
  lower_bound  ::= expression  
  upper_bound  ::= expression  
  stride       ::= expression

If the slice list contains at least one comma, the key used for indexing is a tuple; otherwise, it is the conversion of the single slice item, where a proper slice becomes a slice object.  
슬라이스 목록에 콤마가 한 개 이상 있으면 인덱싱 키는 튜플이 되고, 그렇지 않으면 단일 항목의 값(정상적인 슬라이스는 slice 객체로 변환됨)입니다.

## 6.3.4. Calls  
6.3.4. 함수 호출  
A call invokes a callable with a possibly empty series of arguments:  
함수 호출은 인수가 비어 있을 수도 있는 callable 객체를 호출하는 것입니다.

  call ::= primary "(" [argument_list [","] | comprehension] ")"

The full argument syntax (including positional, starred, and keyword arguments) is defined in detail elsewhere. A call always returns a value (possibly None) unless an exception occurs.  
위치 인수, 별표 인수, 키워드 인수를 포함한 인수 문법은 다른 곳에 자세히 정의되어 있으며, 예외가 없는 한 항상 어떤 값을 반환합니다.

## 6.4. Await expression  
6.4. await 표현식  
An await expression suspends the execution of a coroutine on an awaitable object. It can only be used inside a coroutine function.  
await 표현식은 awaitable 객체에서 코루틴의 실행을 일시 중단합니다. 이는 코루틴 함수 내부에서만 사용할 수 있습니다.

  await_expr ::= "await" primary

Added in version 3.5.  
버전 3.5에서 추가됨.

## 6.5. The power operator  
6.5. 거듭제곱 연산자  
The power operator binds more tightly than unary operators on its left; it binds less tightly than unary operators on its right. The syntax is:  
거듭제곱 연산자는 왼쪽의 단항 연산자보다 더 강하게 결합하며, 오른쪽의 단항 연산자보다는 약하게 결합합니다. 구문은 다음과 같습니다:  

  power ::= (await_expr | primary) ["**" u_expr]  

Thus, in an unparenthesized sequence of power and unary operators, the operators are evaluated from right to left (this does not constrain the evaluation order for the operands): -1**2 results in -1.  
따라서 괄호 없이 나열된 거듭제곱 및 단항 연산자들의 경우, 연산자는 오른쪽에서 왼쪽 순으로 평가됩니다(피연산자의 평가 순서를 제한하지는 않습니다): -1**2는 -1이 됩니다.

The power operator has the same semantics as the built-in pow() function when called with two arguments: it yields its left argument raised to the power of its right argument. The numeric arguments are first converted to a common type, and the result is of that type.  
거듭제곱 연산자는 내장 pow() 함수(인수가 2개인 경우)와 동일한 의미론을 가지며, 왼쪽 인수를 오른쪽 인수의 거듭제곱으로 계산합니다. 숫자 인수는 먼저 공통 타입으로 변환되고 결과도 해당 타입이 됩니다.

For int operands, the result has the same type as the operands unless the second argument is negative; in that case, all arguments are converted to float and a float result is delivered. For example, 10**2 returns 100, but 10**-2 returns 0.01.  
정수 인수의 경우 두 번째 인수가 음수가 아니면 결과는 인수와 같은 타입이고, 음수인 경우 모든 인수를 부동소수점으로 변환하여 부동소수점 결과를 반환합니다. 예를 들어, 10**2는 100을, 10**-2는 0.01을 반환합니다.

Raising 0.0 to a negative power results in a ZeroDivisionError. Raising a negative number to a fractional power results in a complex number. (In earlier versions it raised a ValueError.)  
0.0을 음수 거듭제곱하면 ZeroDivisionError가 발생하고, 음수를 분수 거듭제곱하면 복소수가 반환됩니다. (이전 버전에서는 ValueError가 발생하였습니다.)

This operation can be customized using the special __pow__() and __rpow__() methods.  
이 연산은 __pow__()와 __rpow__() 특별 메서드를 재정의하여 사용자 정의할 수 있습니다.

## 6.6. Unary arithmetic and bitwise operations  
6.6. 단항 산술 및 비트 연산자  
All unary arithmetic and bitwise operations have the same priority:  
모든 단항 산술 및 비트 연산자는 동일한 우선순위를 가집니다:

  u_expr ::= power | "-" u_expr | "+" u_expr | "~" u_expr  

The unary - (minus) operator yields the negation of its numeric argument; the operation can be overridden with the __neg__() special method.  
단항 - 연산자는 숫자 인수의 부호를 반전하며, __neg__() 메서드를 재정의하여 사용자 지정할 수 있습니다.

The unary + (plus) operator yields its numeric argument unchanged; the operation can be overridden with the __pos__() special method.  
단항 + 연산자는 인수를 그대로 반환하며, __pos__() 메서드로 재정의할 수 있습니다.

The unary ~ (invert) operator yields the bitwise inversion of its integer argument. The bitwise inversion of x is defined as -(x+1). It only applies to integral numbers or to custom objects that override the __invert__() special method.  
단항 ~ 연산자는 정수 인수의 비트 반전을 수행하며, x의 비트 반전은 -(x+1)로 정의됩니다. 이는 정수 또는 __invert__()를 재정의한 사용자 객체에만 적용됩니다.

In all three cases, if the argument does not have the proper type, a TypeError exception is raised.  
세 경우 모두, 인수가 올바른 타입이 아니면 TypeError 예외가 발생합니다.

## 6.7. Binary arithmetic operations  
6.7. 이항 산술 연산자  
The binary arithmetic operations have the conventional priority levels. Note that some of these operations also apply to certain non-numeric types. Apart from the power operator, there are only two levels, one for multiplicative operators and one for additive operators:  
이항 산술 연산자는 전통적인 우선순위를 가지며, 일부 연산은 숫자가 아닌 타입에도 적용됩니다. 거듭제곱 연산자를 제외하면 곱셈·나눗셈 계열과 덧셈·뺄셈 계열의 두 단계로 구분됩니다:

  m_expr ::= u_expr | m_expr "*" u_expr | m_expr "@" m_expr |  
           m_expr "//" u_expr | m_expr "/" u_expr |  
           m_expr "%" u_expr  
  a_expr ::= m_expr | a_expr "+" m_expr | a_expr "-" m_expr  

The * (multiplication) operator yields the product of its arguments. The arguments must either both be numbers, or one argument must be an integer and the other must be a sequence. In the former case, the numbers are converted to a common type and then multiplied together. In the latter case, sequence repetition is performed; a negative repetition factor yields an empty sequence.  
곱셈(*) 연산자는 인수의 곱을 반환합니다. 두 인수가 모두 숫자이거나, 하나가 정수이고 다른 하나가 시퀀스여야 합니다. 전자의 경우 숫자를 공통 타입으로 변환 후 곱하고, 후자의 경우 시퀀스 반복을 수행하며, 반복 횟수가 음수이면 빈 시퀀스를 반환합니다.

This operation can be customized using the special __mul__() and __rmul__() methods.  
이 연산은 __mul__()와 __rmul__() 메서드로 사용자 정의할 수 있습니다.

The @ (at) operator is intended to be used for matrix multiplication. No built-in Python types implement this operator.  
@ 연산자는 행렬 곱셈용으로 의도되었으며, 내장 타입에서는 구현되어 있지 않습니다.

This operation can be customized using the special __matmul__() and __rmatmul__() methods.  
이 연산은 __matmul__()와 __rmatmul__() 메서드로 사용자 정의할 수 있습니다.

The / (division) and // (floor division) operators yield the quotient of their arguments. The numeric arguments are first converted to a common type. Division of integers yields a float, while floor division of integers results in an integer; the result is that of mathematical division with the ‘floor’ function applied to the result. Division by zero raises the ZeroDivisionError exception.  
나눗셈(/)과 바닥 나눗셈(//) 연산자는 인수의 몫을 반환합니다. 숫자 인수는 공통 타입으로 변환되며, 정수 나눗셈은 부동소수점을, 바닥 나눗셈은 정수를 반환합니다. 0으로 나누면 ZeroDivisionError가 발생합니다.

The division operation can be customized using the special __truediv__() and __rtruediv__() methods. The floor division operation can be customized using the special __floordiv__() and __rfloordiv__() methods.  
이 연산들은 __truediv__(), __rtruediv__(), __floordiv__(), __rfloordiv__() 메서드로 재정의할 수 있습니다.

The % (modulo) operator yields the remainder from the division of the first argument by the second. The numeric arguments are first converted to a common type. A zero right argument raises the ZeroDivisionError exception. The arguments may be floating-point numbers, e.g., 3.14 % 0.7 equals 0.34 (since 3.14 equals 4 * 0.7 + 0.34.) The modulo operator always yields a result with the same sign as its second operand (or zero); the absolute value of the result is strictly smaller than the absolute value of the second operand.  
나머지(%) 연산자는 첫 번째 인수를 두 번째 인수로 나눈 나머지를 반환합니다. 숫자 인수는 공통 타입으로 변환되며, 0으로 나누면 ZeroDivisionError가 발생합니다. 실수의 경우도 적용되며, 예를 들어 3.14 % 0.7은 0.34입니다(3.14 = 4 * 0.7 + 0.34). 결과의 부호는 두 번째 피연산자와 같고 절댓값은 두 번째 피연산자의 절댓값보다 작습니다.

The floor division and modulo operators are connected by the following identity:  
  x == (x // y) * y + (x % y)  
They are also connected with the built-in function divmod():  
  divmod(x, y) == (x // y, x % y).  
The modulo operation can be customized using the special __mod__() and __rmod__() methods.  
바닥 나눗셈과 나머지 연산자는 x == (x//y)*y + (x%y)로 연결되며, divmod() 함수와도 연관됩니다.

The floor division operator, the modulo operator, and the divmod() function are not defined for complex numbers. Instead, convert to a floating-point number using the abs() function if appropriate.  
복소수에는 바닥 나눗셈, 나머지 연산, divmod()가 정의되지 않으므로, 필요시 abs()를 사용하여 부동소수점으로 변환합니다.

The + (addition) operator yields the sum of its arguments. The arguments must either both be numbers or both be sequences of the same type. In the former case, the numbers are converted to a common type and then added together. In the latter case, the sequences are concatenated.  
덧셈(+) 연산자는 인수의 합을 반환합니다. 두 인수가 모두 숫자이거나 동일 타입 시퀀스여야 하며, 숫자의 경우 공통 타입으로 변환 후 더하고, 시퀀스의 경우 연결합니다.

This operation can be customized using the special __add__() and __radd__() methods.  
이 연산은 __add__()와 __radd__() 메서드로 재정의할 수 있습니다.

The - (subtraction) operator yields the difference of its arguments. The numeric arguments are first converted to a common type.  
뺄셈(-) 연산자는 인수의 차를 반환하며, 숫자 인수는 공통 타입으로 변환됩니다.

This operation can be customized using the special __sub__() and __rsub__() methods.  
이 연산은 __sub__()와 __rsub__() 메서드로 재정의할 수 있습니다.

## 6.8. Shifting operations  
6.8. 시프트 연산자  
The shifting operations have lower priority than the arithmetic operations:  
시프트 연산자는 산술 연산자보다 낮은 우선순위를 가집니다.

  shift_expr ::= a_expr | shift_expr ("<<" | ">>") a_expr  

These operators accept integers as arguments. They shift the first argument to the left or right by the number of bits given by the second argument.  
이 연산자들은 정수를 인수로 받아, 첫 번째 인수를 두 번째 인수만큼 비트 단위로 왼쪽 또는 오른쪽으로 이동합니다.

The left shift operation can be customized using the special __lshift__() and __rlshift__() methods. The right shift operation can be customized using the special __rshift__() and __rrshift__() methods.  
왼쪽/오른쪽 시프트 연산은 각각 __lshift__(), __rlshift__()와 __rshift__(), __rrshift__() 메서드로 사용자 정의할 수 있습니다.

A right shift by n bits is defined as floor division by pow(2, n). A left shift by n bits is defined as multiplication with pow(2, n).  
n비트 오른쪽 시프트는 pow(2, n)으로 바닥 나눗셈한 결과와 같고, n비트 왼쪽 시프트는 pow(2, n)과 곱한 결과와 같습니다.

## 6.9. Binary bitwise operations  
각 비트 연산자는 서로 다른 우선순위를 가집니다:

  and_expr ::= shift_expr | and_expr "&" shift_expr  
  xor_expr ::= and_expr | xor_expr "^" and_expr  
  or_expr  ::= xor_expr | or_expr "|" xor_expr  

The & operator yields the bitwise AND of its arguments, which must be integers or one of them must be a custom object overriding __and__() or __rand__() special methods.  
  & 연산자는 인수들의 비트 AND를 반환합니다. 인수는 정수이거나 __and__() 또는 __rand__() 메서드를 재정의한 사용자 객체여야 합니다.

The ^ operator yields the bitwise XOR (exclusive OR) of its arguments, which must be integers or one of them must be a custom object overriding __xor__() or __rxor__() special methods.  
  ^ 연산자는 인수들의 비트 XOR(배타적 OR)를 반환하며, 인수는 정수이거나 __xor__() 또는 __rxor__() 메서드를 재정의한 사용자 객체여야 합니다.

The | operator yields the bitwise (inclusive) OR of its arguments, which must be integers or one of them must be a custom object overriding __or__() or __ror__() special methods.  
  | 연산자는 인수들의 비트 OR(포함 OR)를 반환하며, 인수는 정수이거나 __or__() 또는 __ror__() 메서드를 재정의한 사용자 객체여야 합니다.

## 6.10. Comparisons  
산술, 시프트 및 비트 연산자보다 낮은 우선순위를 가지며, 모든 비교 연산은 동일한 우선순위를 가집니다. 또한 C와 달리,  
a < b < c와 같은 표현은 수학에서 통용되는 해석을 따릅니다:

  comparison    ::= or_expr (comp_operator or_expr)*  
  comp_operator ::= "<" | ">" | "==" | ">=" | "<=" | "!="  
           | "is" ["not"] | ["not"] "in"

Comparisons yield boolean values: True or False. Custom rich comparison methods may return non-boolean values. In this case Python will call bool() on such value in boolean contexts.  
비교 연산자는 True 또는 False와 같은 불리언 값을 반환합니다. 사용자 정의 비교 메서드가 불리언이 아닌 값을 반환하면, 불리언 문맥에서 bool()을 호출합니다.

Comparisons can be chained arbitrarily, e.g., x < y <= z is equivalent to x < y and y <= z, except that y is evaluated only once (but in both cases z is not evaluated at all when x < y is found to be false).  
비교는 임의로 연결될 수 있으며, 예를 들어 x < y <= z는 x < y and y <= z와 동일합니다. 단, y는 한 번만 평가되며, x < y가 거짓이면 z는 평가되지 않습니다.

Formally, if a, b, c, …, y, z are expressions and op1, op2, …, opN are comparison operators, then  
a op1 b op2 c ... y opN z is equivalent to a op1 b and b op2 c and ... y opN z,  
except that each expression is evaluated at most once.  
형식적으로, a, b, c, …, y, z가 표현식이고 op1, op2, …, opN이 비교 연산자라면  
a op1 b op2 c ... y opN z는 a op1 b and b op2 c and ... and y opN z와 같으며, 각 표현식은 최대 한 번만 평가됩니다.

Note that a op1 b op2 c doesn’t imply any kind of comparison between a and c, so that, e.g., x < y > z is perfectly legal (though perhaps not pretty).  
a op1 b op2 c는 a와 c 사이의 비교를 암시하지 않으므로, 예를 들어 x < y > z는 전혀 문제 없이 허용됩니다.

## 6.10.1. Value comparisons  
<, >, ==, >=, <=, and != compare the values of two objects. The objects do not need to have the same type.  
  <, >, ==, >=, <=, != 연산자는 두 객체의 값을 비교하며, 두 객체는 같은 타입일 필요가 없습니다.

The default behavior for equality comparison is based on object identity.  
기본 동등 비교의 동작은 객체의 동일성에 기반합니다.

A default order comparison (<, >, <=, and >=) is not provided; an attempt raises TypeError.  
기본 순서 비교는 제공되지 않아, 시도 시 TypeError가 발생합니다.

## 6.10.2. Membership test operations  
The operators in and not in test for membership. x in s evaluates to True if x is a member of s, and False otherwise.  
  in, not in 연산자는 멤버십을 검사하며, x in s는 x가 s의 멤버일 때 True, 그렇지 않으면 False를 반환합니다.

For container types such as list, tuple, set, frozenset, dict or collections.deque, x in y is equivalent to  
any(x is e or x == e for e in y).  
리스트, 튜플, 집합, frozenset, 딕셔너리 또는 collections.deque와 같은 컨테이너에서는 x in y가  
any(x is e or x == e for e in y)와 동일합니다.

## 6.10.3. Identity comparisons  
The operators is and is not test for an object’s identity: x is y is true if and only if x and y are the same object.  
  is, is not 연산자는 객체의 동일성을 검사하며, x is y는 x와 y가 동일 객체일 때만 참입니다.

## 6.11. Boolean operations  
or_test  ::= and_test | or_test "or" and_test  
and_test ::= not_test | and_test "and" not_test  
not_test ::= comparison | "not" not_test  

In Boolean contexts, the following values are interpreted as false: False, None, numeric zero of all types, and empty strings and containers. All other values are true.  
불리언 문맥에서는 False, None, 모든 타입의 0 값, 빈 문자열 및 컨테이너가 거짓으로 해석되며, 나머지는 참입니다.

The operator not returns True if its argument is false, False otherwise.  
not 연산자는 인수가 거짓이면 True, 그렇지 않으면 False를 반환합니다.

The expression x and y evaluates x; if x is false, its value is returned; otherwise, y is evaluated and its value returned.  
x and y는 먼저 x를 평가하여 거짓이면 그 값을, 참이면 y를 평가하여 그 값을 반환합니다.

Similarly, x or y returns x if x is true, otherwise y.  
x or y는 x가 참이면 x를, 거짓이면 y를 반환합니다.

## 6.12. Assignment expressions  
할당 표현식  
assignment_expression ::= [identifier ":="] expression  
An assignment expression (sometimes also called a “named expression” or “walrus”) assigns an expression to an identifier, while also returning the value of the expression.  
할당 표현식(때때로 “named expression” 또는 “walrus”라고도 함)은 식별자에 표현식을 할당하면서 그 표현식의 값을 반환합니다.

One common use case is when handling matched regular expressions:  
  if matching := pattern.search(data):  
    do_something(matching)  

Or, when processing a file stream in chunks:  
  while chunk := file.read(9000):  
    process(chunk)  

Assignment expressions must be surrounded by parentheses when used as expression statements and when used as sub‑expressions in slicing, conditional, lambda, keyword‑argument, and comprehension‑if expressions and in assert, with, and assignment statements. In all other places they can be used without extra parentheses, including in if and while statements.  
할당 표현식은 표현식 문(statement)이나 슬라이싱, 조건부, 람다, 키워드 인수, 컴프리헨션‑if 등 서브 표현식으로 사용할 때 반드시 괄호로 감싸야 하며, 그 외의 경우에는 괄호 없이 사용 가능합니다.

Added in version 3.8: See PEP 572 for more details about assignment expressions.  
버전 3.8에서 추가됨: 할당 표현식에 대한 자세한 내용은 PEP 572를 참조하십시오.

## 6.13. Conditional expressions  
조건 표현식  
conditional_expression ::= or_test ["if" or_test "else" expression]  
expression             ::= conditional_expression | lambda_expr  
Conditional expressions (sometimes called a “ternary operator”) have the lowest priority of all Python operations.  
조건 표현식(때때로 “삼항 연산자”라고도 함)은 모든 파이썬 연산자 중 가장 낮은 우선순위를 가집니다.

The expression x if C else y first evaluates the condition, C rather than x. If C is true, x is evaluated and its value is returned; otherwise, y is evaluated and its value is returned.  
표현식 x if C else y는 먼저 조건 C를 평가하며, C가 참이면 x가 평가되어 그 값이 반환되고, 그렇지 않으면 y가 평가되어 그 값이 반환됩니다.

See PEP 308 for more details about conditional expressions.  
자세한 내용은 PEP 308을 참조하십시오.

## 6.14. Lambdas  
람다 표현식  
lambda_expr ::= "lambda" [parameter_list] ":" expression  
Lambda expressions (sometimes called lambda forms) are used to create anonymous functions. The expression lambda parameters: expression yields a function object.  
람다 표현식(때때로 lambda form이라고도 함)은 익명 함수를 만들기 위해 사용되며, "lambda 매개변수: 표현식"은 함수 객체를 생성합니다.

The unnamed object behaves like a function object defined with:  
  def <lambda>(parameters):  
    return expression  
익명 객체는 위와 같이 정의된 함수와 동일하게 동작합니다.

See section Function definitions for the syntax of parameter lists. Note that functions created with lambda expressions cannot contain statements or annotations.  
매개변수 목록의 구문은 함수 정의 섹션을 참조하십시오.

## 6.15. Expression lists  
표현식 목록  
starred_expression       ::= ["*"] or_expr  
flexible_expression      ::= assignment_expression | starred_expression  
flexible_expression_list ::= flexible_expression ("," flexible_expression)* [","]  
starred_expression_list  ::= starred_expression ("," starred_expression)* [","]  
expression_list          ::= expression ("," expression)* [","]  
yield_list               ::= expression_list | starred_expression "," [starred_expression_list]  
Except when part of a list or set display, an expression list containing at least one comma yields a tuple. The expressions are evaluated from left to right.  
콤마가 하나 이상 포함된 표현식 목록은 튜플을 반환하며, 표현식은 왼쪽에서 오른쪽으로 평가됩니다.

An asterisk * denotes iterable unpacking. Its operand must be an iterable, and the iterable is expanded into its individual items.  
별표(*)는 반복 가능 객체의 언패킹을 나타냅니다.

Added in version 3.5: Iterable unpacking in expression lists, originally proposed by PEP 448.  
버전 3.5에서 추가됨.

Added in version 3.11: Any item in an expression list may be starred. See PEP 646.  
버전 3.11에서 추가됨.

A trailing comma is required only to create a one-item tuple (e.g., 1,); otherwise it is optional. A single expression without a trailing comma yields that expression’s value, not a tuple.  
한 항목 튜플을 생성하기 위해선 후행 콤마가 필요하며, 그렇지 않으면 단일 표현식의 값이 반환됩니다.

## 6.16. Evaluation order  
평가 순서  
Python evaluates expressions from left to right. In assignment statements the right-hand side is evaluated before the left-hand side.  
파이썬은 표현식을 왼쪽에서 오른쪽으로 평가하며, 할당문에서는 오른쪽이 먼저 평가됩니다.

Examples:  
  expr1, expr2, expr3, expr4  
  (expr1, expr2, expr3, expr4)  
  {expr1: expr2, expr3: expr4}  
  expr1 + expr2 * (expr3 - expr4)  
  expr1(expr2, expr3, *expr4, **expr5)  
  expr3, expr4 = expr1, expr2

## 6.17. Operator precedence  
연산자 우선순위  
The following table summarizes the operator precedence in Python, from highest (most binding) to lowest (least binding). Operators with the same precedence group left-to-right (except exponentiation and conditional expressions group right-to-left).  
다음 표는 파이썬의 연산자 우선순위를 가장 높은 결합력부터 가장 낮은 결합력 순으로 요약합니다. 동일 우선순위의 연산자는 왼쪽에서 오른쪽으로 그룹화되며(거듭제곱과 조건 표현식은 오른쪽에서 왼쪽으로 그룹화됨):

  Operator                         Description  
  (expressions...), [expressions...], {key: value...}, {expressions...}  
    Binding or parenthesized expression, list/dict/set display  
  x[index], x[index:index], x(arguments...), x.attribute  
    Subscription, slicing, call, attribute reference  
  await x                         Await expression  
  **                             Exponentiation  
  +x, -x, ~x                      Unary plus, minus, bitwise NOT  
  *, @, /, //, %                  Multiplication, matrix multiplication, division, floor division, remainder  
  +, -                            Addition and subtraction  
  <<, >>                          Shifts  
  &                              Bitwise AND  
  ^                              Bitwise XOR  
  |                              Bitwise OR  
  in, not in, is, is not, <, <=, >, >=, !=, ==  
    Comparisons, membership tests, identity tests  
  not x                           Boolean NOT  
  and                             Boolean AND  
  or                              Boolean OR  
  if – else                       Conditional expression  
  lambda                          Lambda expression  
  :=                              Assignment expression

