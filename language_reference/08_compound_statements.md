8. Compound statements
========================

Compound statements contain (groups of) other statements; they affect or control the execution of those other statements in some way. In general, compound statements span multiple lines, although in simple incarnations a whole compound statement may be contained in one line.

8. 복합 문장
========================

복합 문장은 다른 문장(들)을 포함하며, 이러한 다른 문장의 실행을 어떤 방식으로 영향을 주거나 제어합니다. 일반적으로 복합 문장은 여러 줄에 걸쳐 있지만, 단순한 형태에서는 전체 복합 문장이 한 줄에 포함될 수도 있습니다.

The if, while and for statements implement traditional control flow constructs. try specifies exception handlers and/or cleanup code for a group of statements, while the with statement allows the execution of initialization and finalization code around a block of code. Function and class definitions are also syntactically compound statements.

if, while, for 문은 전통적인 제어 흐름 구조를 구현합니다. try는 문장 그룹에 대한 예외 처리기 및/또는 정리 코드를 지정하며, with 문은 코드 블록 주변에 초기화 및 종료 코드의 실행을 허용합니다. 함수 및 클래스 정의도 구문적으로 복합 문장입니다.

A compound statement consists of one or more 'clauses.' A clause consists of a header and a 'suite.' The clause headers of a particular compound statement are all at the same indentation level. Each clause header begins with a uniquely identifying keyword and ends with a colon. A suite is a group of statements controlled by a clause. A suite can be one or more semicolon-separated simple statements on the same line as the header, following the header's colon, or it can be one or more indented statements on subsequent lines. Only the latter form of a suite can contain nested compound statements; the following is illegal, mostly because it wouldn't be clear to which if clause a following else clause would belong:

복합 문장은 하나 이상의 '절'로 구성됩니다. 한 절은 헤더와 '스위트'로 구성됩니다. 특정 복합 문장의 절 헤더는 모두 동일한 들여쓰기 수준에 있습니다. 각 절 헤더는 고유하게 식별하는 키워드로 시작하고 콜론으로 끝납니다. 스위트는 절에 의해 제어되는 문장 그룹입니다. 스위트는 헤더와 같은 줄에서 헤더의 콜론 다음에 세미콜론으로 구분된 하나 이상의 단순 문장일 수 있으며, 또는 후속 줄에 들여쓰기된 하나 이상의 문장일 수 있습니다. 오직 후자의 스위트 형태만 중첩된 복합 문장을 포함할 수 있습니다. 다음 예시는 불법입니다. 주로 후속 else 절이 어떤 if 절에 속하는지 명확하지 않기 때문입니다:

    if test1: if test2: print(x)

Also note that the semicolon binds tighter than the colon in this context, so that in the following example, either all or none of the print() calls are executed:

또한 이 맥락에서 세미콜론이 콜론보다 더 강하게 결합한다는 점에 유의하세요. 따라서 다음 예시에서는 모든 print() 호출이 실행되거나 하나도 실행되지 않습니다:

    if x < y < z: print(x); print(y); print(z)

Summarizing:

    compound_stmt ::= if_stmt
                      | while_stmt
                      | for_stmt
                      | try_stmt
                      | with_stmt
                      | match_stmt
                      | funcdef
                      | classdef
                      | async_with_stmt
                      | async_for_stmt
                      | async_funcdef
    suite         ::= stmt_list NEWLINE | NEWLINE INDENT statement+ DEDENT
    statement     ::= stmt_list NEWLINE | compound_stmt
    stmt_list     ::= simple_stmt (";" simple_stmt)* [";"]

Note that statements always end in a NEWLINE possibly followed by a DEDENT. Also note that optional continuation clauses always begin with a keyword that cannot start a statement, thus there are no ambiguities (the ‘dangling else’ problem is solved in Python by requiring nested if statements to be indented).

8.1. The if statement
----------------------

The if statement is used for conditional execution:

8.1. if 문
----------------------

if 문은 조건부 실행에 사용됩니다:

    if_stmt ::= "if" assignment_expression ":" suite
                ("elif" assignment_expression ":" suite)*
                ["else" ":" suite]

It selects exactly one of the suites by evaluating the expressions one by one until one is found to be true (see section Boolean operations for the definition of true and false); then that suite is executed (and no other part of the if statement is executed or evaluated). If all expressions are false, the suite of the else clause, if present, is executed.

이는 표현식을 하나씩 평가하여 참으로 판명될 때까지 진행하여 정확히 하나의 스위트를 선택합니다(참과 거짓의 정의는 불리언 연산 섹션 참조). 그 후 해당 스위트가 실행됩니다(if 문의 다른 부분은 실행되거나 평가되지 않음). 모든 표현식이 거짓이면, else 절의 스위트가 있는 경우 실행됩니다.

8.2. The while statement
-------------------------

The while statement is used for repeated execution as long as an expression is true:

8.2. while 문
-------------------------

while 문은 표현식이 참인 동안 반복 실행을 위해 사용됩니다:

    while_stmt ::= "while" assignment_expression ":" suite
                   ["else" ":" suite]

This repeatedly tests the expression and, if it is true, executes the first suite; if the expression is false (which may be the first time it is tested) the suite of the else clause, if present, is executed and the loop terminates.

이는 표현식을 반복적으로 테스트하고, 참이면 첫 번째 스위트를 실행합니다. 표현식이 거짓이면(처음 테스트될 때 거짓일 수도 있음) else 절의 스위트가 있는 경우 실행되고 루프가 종료됩니다.

A break statement executed in the first suite terminates the loop without executing the else clause's suite. A continue statement executed in the first suite skips the rest of the suite and goes back to testing the expression.

첫 번째 스위트에서 실행된 break 문은 else 절의 스위트를 실행하지 않고 루프를 종료합니다. 첫 번째 스위트에서 실행된 continue 문은 스위트의 나머지 부분을 건너뛰고 표현식 테스트로 돌아갑니다.

8.3. The for statement
-----------------------

The for statement is used to iterate over the elements of a sequence (such as a string, tuple or list) or other iterable object:

8.3. for 문
-----------------------

for 문은 시퀀스(문자열, 튜플 또는 리스트 등)나 다른 반복 가능한 객체의 요소를 반복하는 데 사용됩니다:

    for_stmt ::= "for" target_list "in" starred_list ":" suite
                 ["else" ":" suite]

The starred_list expression is evaluated once; it should yield an iterable object. An iterator is created for that iterable. The first item provided by the iterator is then assigned to the target list using the standard rules for assignments (see Assignment statements), and the suite is executed. This repeats for each item provided by the iterator. When the iterator is exhausted, the suite in the else clause, if present, is executed, and the loop terminates.

starred_list 표현식은 한 번 평가됩니다. 이는 반복 가능한 객체를 산출해야 합니다. 해당 반복 가능한 객체에 대한 반복자가 생성됩니다. 그런 다음 반복자가 제공하는 첫 번째 항목이 할당 규칙을 사용하여 대상 리스트에 할당되고(할당 문 참조), 스위트가 실행됩니다. 이는 반복자가 제공하는 각 항목에 대해 반복됩니다. 반복자가 소진되면, else 절의 스위트가 있는 경우 실행되고 루프가 종료됩니다.

A break statement executed in the first suite terminates the loop without executing the else clause's suite. A continue statement executed in the first suite skips the rest of the suite and continues with the next item, or with the else clause if there is no next item.

첫 번째 스위트에서 실행된 break 문은 else 절의 스위트를 실행하지 않고 루프를 종료합니다. 첫 번째 스위트에서 실행된 continue 문은 스위트의 나머지 부분을 건너뛰고 다음 항목으로 계속하거나, 다음 항목이 없는 경우 else 절로 계속합니다.

The for-loop makes assignments to the variables in the target list. This overwrites all previous assignments to those variables including those made in the suite of the for-loop:

for 루프는 대상 리스트의 변수에 할당합니다. 이는 for 루프의 스위트에서 수행된 할당을 포함하여 해당 변수에 대한 모든 이전 할당을 덮어씁니다:

    for i in range(10):
        print(i)
        i = 5             # this will not affect the for-loop
                          # because i will be overwritten with the next
                          # index in the range

Names in the target list are not deleted when the loop is finished, but if the sequence is empty, they will not have been assigned to at all by the loop. Hint: the built-in type range() represents immutable arithmetic sequences of integers. For instance, iterating range(3) successively yields 0, 1, and then 2.

대상 리스트의 이름은 루프가 끝날 때 삭제되지 않지만, 시퀀스가 비어 있으면 루프에 의해 전혀 할당되지 않습니다. 힌트: 내장 타입 range()는 불변의 산술 정수 시퀀스를 나타냅니다. 예를 들어, range(3)을 반복하면 차례로 0, 1, 그리고 2가 산출됩니다.

Changed in version 3.11: Starred elements are now allowed in the expression list.

버전 3.11에서 변경됨: 이제 표현식 리스트에 별표 요소가 허용됩니다.

8.4. The try statement
-----------------------

The try statement specifies exception handlers and/or cleanup code for a group of statements:

8.4. try 문
-----------------------

try 문은 문장 그룹에 대한 예외 처리기 및/또는 정리 코드를 지정합니다:

    try_stmt  ::= try1_stmt | try2_stmt | try3_stmt
    try1_stmt ::= "try" ":" suite
                  ("except" [expression ["as" identifier]] ":" suite)+
                  ["else" ":" suite]
                  ["finally" ":" suite]
    try2_stmt ::= "try" ":" suite
                  ("except" "*" expression ["as" identifier] ":" suite)+
                  ["else" ":" suite]
                  ["finally" ":" suite]
    try3_stmt ::= "try" ":" suite
                  "finally" ":" suite

Additional information on exceptions can be found in section Exceptions, and information on using the raise statement to generate exceptions may be found in section The raise statement.

예외에 대한 추가 정보는 Exceptions 섹션에서 찾을 수 있으며, 예외를 생성하기 위한 raise 문 사용에 관한 정보는 The raise statement 섹션에서 찾을 수 있습니다.

8.4.1. except clause
~~~~~~~~~~~~~~~~~~~~~~

The except clause(s) specify one or more exception handlers. When no exception occurs in the try clause, no exception handler is executed. When an exception occurs in the try suite, a search for an exception handler is started. This search inspects the except clauses in turn until one is found that matches the exception. An expression-less except clause, if present, must be last; it matches any exception.

8.4.1. except 절
~~~~~~~~~~~~~~~~~~~~~~

except 절은 하나 이상의 예외 처리기를 지정합니다. try 절에서 예외가 발생하지 않으면 예외 처리기가 실행되지 않습니다. try 스위트에서 예외가 발생하면 예외 처리기 검색이 시작됩니다. 이 검색은 except 절을 차례로 검사하여 예외와 일치하는 절이 발견될 때까지 진행합니다. 표현식이 없는 except 절은 있는 경우 마지막에 위치해야 합니다. 이는 모든 예외와 일치합니다.

For an except clause with an expression, the expression must evaluate to an exception type or a tuple of exception types. The raised exception matches an except clause whose expression evaluates to the class or a non-virtual base class of the exception object, or to a tuple that contains such a class.

표현식이 있는 except 절의 경우, 표현식은 예외 타입 또는 예외 타입의 튜플로 평가되어야 합니다. 발생한 예외는 표현식이 예외 객체의 클래스 또는 비가상 기본 클래스로 평가되거나, 그런 클래스를 포함하는 튜플로 평가되는 except 절과 일치합니다.

If no except clause matches the exception, the search for an exception handler continues in the surrounding code and on the invocation stack. [1]

예외와 일치하는 except 절이 없으면, 예외 처리기 검색은 주변 코드와 호출 스택에서 계속됩니다. [1]

If the evaluation of an expression in the header of an except clause raises an exception, the original search for a handler is canceled and a search starts for the new exception in the surrounding code and on the call stack (it is treated as if the entire try statement raised the exception).

except 절의 헤더에서 표현식 평가가 예외를 발생시키면, 핸들러의 원래 검색은 취소되고 주변 코드와 호출 스택에서 새 예외에 대한 검색이 시작됩니다(이는 전체 try 문이 예외를 발생시킨 것처럼 처리됩니다).

When a matching except clause is found, the exception is assigned to the target specified after the as keyword in that except clause, if present, and the except clause's suite is executed. All except clauses must have an executable block. When the end of this block is reached, execution continues normally after the entire try statement. (This means that if two nested handlers exist for the same exception, and the exception occurs in the try clause of the inner handler, the outer handler will not handle the exception.)

일치하는 except 절이 발견되면, 예외는 해당 except 절에서 as 키워드 뒤에 지정된 대상에 할당(있는 경우)되고 except 절의 스위트가 실행됩니다. 모든 except 절은 실행 가능한 블록을 가져야 합니다. 이 블록의 끝에 도달하면, 실행은 전체 try 문 이후에 정상적으로 계속됩니다. (이는 동일한 예외에 대해 두 개의 중첩된 핸들러가 존재하고, 예외가 내부 핸들러의 try 절에서 발생하면, 외부 핸들러는 예외를 처리하지 않는다는 것을 의미합니다.)

When an exception has been assigned using as target, it is cleared at the end of the except clause. This is as if

    except E as N:
        foo

was translated to

    except E as N:
        try:
            foo
        finally:
            del N

This means the exception must be assigned to a different name to be able to refer to it after the except clause. Exceptions are cleared because with the traceback attached to them, they form a reference cycle with the stack frame, keeping all locals in that frame alive until the next garbage collection occurs.

예외가 as 대상 사용하여 할당된 경우, except 절의 끝에서 지워집니다. 이는 다음과 같이 번역된 것과 같습니다:

    except E as N:
        foo

다음과 같이 번역된 것과 같습니다:

    except E as N:
        try:
            foo
        finally:
            del N

이는 예외가 except 절 이후에 참조될 수 있도록 다른 이름에 할당되어야 함을 의미합니다. 예외는 추적이 첨부된 상태로 스택 프레임과 참조 사이클을 형성하여, 다음 가비지 컬렉션이 발생할 때까지 해당 프레임의 모든 로컬 변수를 유지하기 때문에 지워집니다.

Before an except clause's suite is executed, the exception is stored in the sys module, where it can be accessed from within the body of the except clause by calling sys.exception(). When leaving an exception handler, the exception stored in the sys module is reset to its previous value:

except 절의 스위트가 실행되기 전에, 예외는 sys 모듈에 저장되며, except 절 본문 내에서 sys.exception()을 호출하여 접근할 수 있습니다. 예외 처리기를 떠날 때, sys 모듈에 저장된 예외는 이전 값으로 재설정됩니다:

    >>>
    print(sys.exception())
    None
    try:
        raise TypeError
    except:
        print(repr(sys.exception()))
        try:
             raise ValueError
        except:
            print(repr(sys.exception()))
        print(repr(sys.exception()))

    TypeError()
    ValueError()
    TypeError()
    print(sys.exception())
    None

8.4.2. except* clause
~~~~~~~~~~~~~~~~~~~~~~~

The except* clause(s) are used for handling ExceptionGroups. The exception type for matching is interpreted as in the case of except, but in the case of exception groups we can have partial matches when the type matches some of the exceptions in the group. This means that multiple except* clauses can execute, each handling part of the exception group. Each clause executes at most once and handles an exception group of all matching exceptions. Each exception in the group is handled by at most one except* clause, the first that matches it.

8.4.2. except* 절
~~~~~~~~~~~~~~~~~~~~~~~

except* 절은 ExceptionGroups를 처리하는 데 사용됩니다. 일치를 위한 예외 타입은 except의 경우와 같이 해석되지만, 예외 그룹의 경우 타입이 그룹의 일부 예외와 일치할 때 부분 일치가 가능합니다. 이는 여러 except* 절이 실행될 수 있으며, 각각이 예외 그룹의 일부를 처리함을 의미합니다. 각 절은 최대 한 번만 실행되며 모든 일치하는 예외의 예외 그룹을 처리합니다. 그룹의 각 예외는 최대 한 개의 except* 절, 즉 처음으로 일치하는 절에 의해 처리됩니다.

    >>>
    try:
        raise ExceptionGroup("eg",
            [ValueError(1), TypeError(2), OSError(3), OSError(4)])
    except* TypeError as e:
        print(f'caught {type(e)} with nested {e.exceptions}')
    except* OSError as e:
        print(f'caught {type(e)} with nested {e.exceptions}')

    caught <class 'ExceptionGroup'> with nested (TypeError(2),)
    caught <class 'ExceptionGroup'> with nested (OSError(3), OSError(4))
      + Exception Group Traceback (most recent call last):
      |   File "<stdin>", line 2, in <module>
      | ExceptionGroup: eg
      +-+---------------- 1 ----------------
        | ValueError: 1
        +------------------------------------

Any remaining exceptions that were not handled by any except* clause are re-raised at the end, along with all exceptions that were raised from within the except* clauses. If this list contains more than one exception to reraise, they are combined into an exception group.

어떤 except* 절에서도 처리되지 않은 나머지 예외들은 except* 절 내에서 발생한 모든 예외와 함께 마지막에 다시 발생합니다. 이 목록에 다시 발생시킬 예외가 둘 이상 포함되어 있으면, 그 예외들은 예외 그룹으로 결합됩니다.

If the raised exception is not an exception group and its type matches one of the except* clauses, it is caught and wrapped by an exception group with an empty message string.

발생한 예외가 예외 그룹이 아니고 그 타입이 except* 절 중 하나와 일치하면, 빈 메시지 문자열이 있는 예외 그룹으로 포착되고 감싸집니다.

    >>>
    try:
        raise BlockingIOError
    except* BlockingIOError as e:
        print(repr(e))

    ExceptionGroup('', (BlockingIOError()))

An except* clause must have a matching expression; it cannot be except*:. Furthermore, this expression cannot contain exception group types, because that would have ambiguous semantics.

except* 절은 일치하는 표현식을 가져야 합니다; except*:일 수는 없습니다. 또한, 이 표현식은 모호한 의미를 가질 수 있기 때문에 예외 그룹 타입을 포함할 수 없습니다.

It is not possible to mix except and except* in the same try. break, continue and return cannot appear in an except* clause.

같은 try에서 except와 except*를 섞는 것은 불가능합니다. break, continue, return은 except* 절에 나타날 수 없습니다.

8.4.3. else clause
~~~~~~~~~~~~~~~~~~~~

The optional else clause is executed if the control flow leaves the try suite, no exception was raised, and no return, continue, or break statement was executed. Exceptions in the else clause are not handled by the preceding except clauses.

8.4.3. else 절
~~~~~~~~~~~~~~~~~~~~

선택적 else 절은 제어 흐름이 try 스위트를 떠나고, 예외가 발생하지 않았으며, return, continue 또는 break 문이 실행되지 않은 경우 실행됩니다. else 절의 예외는 앞의 except 절에 의해 처리되지 않습니다.

8.4.4. finally clause
~~~~~~~~~~~~~~~~~~~~~~~

If finally is present, it specifies a 'cleanup' handler. The try clause is executed, including any except and else clauses. If an exception occurs in any of the clauses and is not handled, the exception is temporarily saved. The finally clause is executed. If there is a saved exception it is re-raised at the end of the finally clause. If the finally clause raises another exception, the saved exception is set as the context of the new exception. If the finally clause executes a return, break or continue statement, the saved exception is discarded:

8.4.4. finally 절
~~~~~~~~~~~~~~~~~~~~~~~

finally가 있으면, '정리' 핸들러를 지정합니다. try 절은 except 및 else 절을 포함하여 실행됩니다. 절 중 하나에서 예외가 발생하고 처리되지 않으면, 예외는 임시로 저장됩니다. finally 절이 실행됩니다. 저장된 예외가 있으면 finally 절의 끝에서 다시 발생합니다. finally 절이 다른 예외를 발생시키면, 저장된 예외는 새 예외의 컨텍스트로 설정됩니다. finally 절이 return, break 또는 continue 문을 실행하면, 저장된 예외는 버려집니다:

    >>>
    def f():
        try:
            1/0
        finally:
            return 42

    f()
    42

The exception information is not available to the program during execution of the finally clause.

finally 절 실행 중에는 예외 정보를 프로그램에서 사용할 수 없습니다.

When a return, break or continue statement is executed in the try suite of a try…finally statement, the finally clause is also executed 'on the way out.'

try…finally 문의 try 스위트에서 return, break 또는 continue 문이 실행되면, finally 절도 '나가는 길에' 실행됩니다.

The return value of a function is determined by the last return statement executed. Since the finally clause always executes, a return statement executed in the finally clause will always be the last one executed:

함수의 반환 값은 마지막으로 실행된 return 문에 의해 결정됩니다. finally 절은 항상 실행되므로, finally 절에서 실행된 return 문은 항상 마지막으로 실행됩니다:

    >>>
    def foo():
        try:
            return 'try'
        finally:
            return 'finally'

    foo()
    'finally'

Changed in version 3.8: Prior to Python 3.8, a continue statement was illegal in the finally clause due to a problem with the implementation.

버전 3.8에서 변경됨: Python 3.8 이전에는 구현 문제로 인해 finally 절에서 continue 문이 불법이었습니다.

8.5. The with statement
------------------------

The with statement is used to wrap the execution of a block with methods defined by a context manager (see section With Statement Context Managers). This allows common try…except…finally usage patterns to be encapsulated for convenient reuse.

8.5. with 문
------------------------

with 문은 컨텍스트 관리자에 의해 정의된 메서드로 블록의 실행을 감싸는 데 사용됩니다(With Statement Context Managers 섹션 참조). 이를 통해 일반적인 try…except…finally 사용 패턴을 편리한 재사용을 위해 캡슐화할 수 있습니다.

    with_stmt          ::= "with" ( "(" with_stmt_contents ","? ")" | with_stmt_contents ) ":" suite
    with_stmt_contents ::= with_item ("," with_item)*
    with_item          ::= expression ["as" target]

The execution of the with statement with one "item" proceeds as follows:

1. The context expression (the expression given in the with_item) is evaluated to obtain a context manager.
2. The context manager's __enter__() is loaded for later use.
3. The context manager's __exit__() is loaded for later use.
4. The context manager's __enter__() method is invoked.
5. If a target was included in the with statement, the return value from __enter__() is assigned to it.
   
   > **Note:** The with statement guarantees that if the __enter__() method returns without an error, then __exit__() will always be called. Thus, if an error occurs during the assignment to the target list, it will be treated the same as an error occurring within the suite would be. See step 7 below.

6. The suite is executed.
7. The context manager's __exit__() method is invoked. If an exception caused the suite to be exited, its type, value, and traceback are passed as arguments to __exit__(). Otherwise, three None arguments are supplied.

If the suite was exited due to an exception, and the return value from the __exit__() method was false, the exception is reraised. If the return value was true, the exception is suppressed, and execution continues with the statement following the with statement.

If the suite was exited for any reason other than an exception, the return value from __exit__() is ignored, and execution proceeds at the normal location for the kind of exit that was taken.

with 문이 하나의 "항목"으로 실행되는 과정은 다음과 같습니다:

1. 컨텍스트 표현식(with_item에 주어진 표현식)이 평가되어 컨텍스트 관리자를 얻습니다.
2. 컨텍스트 관리자의 __enter__()가 나중에 사용하기 위해 로드됩니다.
3. 컨텍스트 관리자의 __exit__()가 나중에 사용하기 위해 로드됩니다.
4. 컨텍스트 관리자의 __enter__() 메서드가 호출됩니다.
5. with 문에 target이 포함된 경우, __enter__()의 반환 값이 그 target에 할당됩니다.
   
   > **참고:** with 문은 __enter__() 메서드가 오류 없이 반환되면 __exit__()가 항상 호출됨을 보장합니다. 따라서 target 리스트에 할당하는 동안 오류가 발생하면, 이는 suite 내에서 발생하는 오류와 동일하게 처리됩니다. 아래 7단계를 참조하세요.

6. suite가 실행됩니다.
7. 컨텍스트 관리자의 __exit__() 메서드가 호출됩니다. 예외로 인해 suite가 종료된 경우, 그 예외의 type, value, traceback이 __exit__()에 인수로 전달됩니다. 그렇지 않으면 세 개의 None 인수가 제공됩니다.

suite가 예외로 인해 종료되고 __exit__() 메서드의 반환 값이 false인 경우, 예외가 다시 발생합니다. 반환 값이 true인 경우, 예외는 억제되고 실행은 with 문 다음 문장으로 계속됩니다.

suite가 예외 이외의 이유로 종료된 경우, __exit__()의 반환 값은 무시되고 실행은 취해진 종료 유형에 대한 정상 위치에서 계속됩니다.

The following code:

```python
with EXPRESSION as TARGET:
    SUITE
```

is semantically equivalent to:

```python
manager = (EXPRESSION)
enter = type(manager).__enter__
exit = type(manager).__exit__
value = enter(manager)
hit_except = False

try:
    TARGET = value
    SUITE
except:
    hit_except = True
    if not exit(manager, *sys.exc_info()):
        raise
finally:
    if not hit_except:
        exit(manager, None, None, None)
```

다음 코드:

```python
with EXPRESSION as TARGET:
    SUITE
```

는 의미론적으로 다음과 동일합니다:

```python
manager = (EXPRESSION)
enter = type(manager).__enter__
exit = type(manager).__exit__
value = enter(manager)
hit_except = False

try:
    TARGET = value
    SUITE
except:
    hit_except = True
    if not exit(manager, *sys.exc_info()):
        raise
finally:
    if not hit_except:
        exit(manager, None, None, None)
```

With more than one item, the context managers are processed as if multiple with statements were nested:

```python
with A() as a, B() as b:
    SUITE
```

is semantically equivalent to:

```python
with A() as a:
    with B() as b:
        SUITE
```

여러 항목이 있을 경우, 컨텍스트 관리자는 여러 with 문이 중첩된 것처럼 처리됩니다:

```python
with A() as a, B() as b:
    SUITE
```

는 의미론적으로 다음과 동일합니다:

```python
with A() as a:
    with B() as b:
        SUITE
```

You can also write multi-item context managers in multiple lines if the items are surrounded by parentheses. For example:

```python
with (
    A() as a,
    B() as b,
):
    SUITE
```

항목이 괄호로 둘러싸인 경우 여러 항목 컨텍스트 관리자를 여러 줄에 작성할 수도 있습니다. 예:

```python
with (
    A() as a,
    B() as b,
):
    SUITE
```

Changed in version 3.1: Support for multiple context expressions.

Changed in version 3.10: Support for using grouping parentheses to break the statement in multiple lines.

버전 3.1에서 변경됨: 다중 컨텍스트 표현식 지원.

버전 3.10에서 변경됨: 그룹화 괄호를 사용하여 문장을 여러 줄로 나누는 기능 지원.

See also  
PEP 343 - The "with" statement  
The specification, background, and examples for the Python with statement.

참조  
PEP 343 - "with" 문  
Python with 문의 명세, 배경 및 예제.

8.6. The match statement
------------------------

Added in version 3.10.

The match statement is used for pattern matching. Syntax:

```
match_stmt   ::= 'match' subject_expr ":" NEWLINE INDENT case_block+ DEDENT
subject_expr ::= star_named_expression "," star_named_expressions?
                 | named_expression
case_block   ::= 'case' patterns [guard] ":" block
```

Note: This section uses single quotes to denote soft keywords.

8.6. match 문
------------------------

버전 3.10에서 추가됨.

match 문은 패턴 매칭에 사용됩니다. 구문:

```
match_stmt   ::= 'match' subject_expr ":" NEWLINE INDENT case_block+ DEDENT
subject_expr ::= star_named_expression "," star_named_expressions?
                 | named_expression
case_block   ::= 'case' patterns [guard] ":" block
```

참고: 이 섹션에서는 소프트 키워드를 나타내기 위해 작은따옴표를 사용합니다.

Pattern matching takes a pattern as input (following case) and a subject value (following match). The pattern (which may contain subpatterns) is matched against the subject value. The outcomes are:

1. A match success or failure (also termed a pattern success or failure).
2. Possible binding of matched values to a name. The prerequisites for this are further discussed below.

The match and case keywords are soft keywords.

패턴 매칭은 패턴(case 다음)을 입력으로 받고 주체 값(match 다음)을 사용합니다. 패턴(하위 패턴을 포함할 수 있음)은 주체 값과 대조됩니다. 결과는 다음과 같습니다:

1. 매치 성공 또는 실패(패턴 성공 또는 실패라고도 함).
2. 일치된 값을 이름에 바인딩할 가능성. 이에 대한 전제 조건은 아래에서 자세히 논의됩니다.

match와 case 키워드는 소프트 키워드입니다.

See also  
PEP 634 – Structural Pattern Matching: Specification  
PEP 636 – Structural Pattern Matching: Tutorial

참조  
PEP 634 – 구조적 패턴 매칭: 명세  
PEP 636 – 구조적 패턴 매칭: 튜토리얼

8.6.1. Overview
~~~~~~~~~~~~~~~~

Here's an overview of the logical flow of a match statement:

1. The subject expression subject_expr is evaluated and a resulting subject value obtained. If the subject expression contains a comma, a tuple is constructed using the standard rules.
2. Each pattern in a case_block is attempted to match with the subject value. The specific rules for success or failure are described below. The match attempt can also bind some or all of the standalone names within the pattern. The precise pattern binding rules vary per pattern type and are specified below. Name bindings made during a successful pattern match outlive the executed block and can be used after the match statement.
   
   > **Note:** During failed pattern matches, some subpatterns may succeed. Do not rely on bindings being made for a failed match. Conversely, do not rely on variables remaining unchanged after a failed match. The exact behavior is dependent on implementation and may vary. This is an intentional decision made to allow different implementations to add optimizations.

3. If the pattern succeeds, the corresponding guard (if present) is evaluated. In this case all name bindings are guaranteed to have happened.
4. If the guard evaluates as true or is missing, the block inside case_block is executed.
5. Otherwise, the next case_block is attempted as described above.
6. If there are no further case blocks, the match statement is completed.

> **Note:** Users should generally never rely on a pattern being evaluated. Depending on implementation, the interpreter may cache values or use other optimizations which skip repeated evaluations.

8.6.1. 개요
~~~~~~~~~~~~~~~~

match 문의 논리적 흐름에 대한 개요는 다음과 같습니다:

1. 주체 표현식(subject_expr)이 평가되어 결과 주체 값을 얻습니다. 주체 표현식에 쉼표가 포함된 경우 표준 규칙을 사용하여 튜플이 구성됩니다.
2. case_block의 각 패턴은 주체 값과 일치하는지 시도됩니다. 성공 또는 실패에 대한 특정 규칙은 아래에 설명되어 있습니다. 일치 시도는 패턴 내의 독립 이름 중 일부 또는 전부를 바인딩할 수도 있습니다. 정확한 패턴 바인딩 규칙은 패턴 유형에 따라 다르며 아래에 명시되어 있습니다. 성공적인 패턴 일치 중에 만들어진 이름 바인딩은 실행된 블록 이후에도 유지되며 match 문 이후에 사용될 수 있습니다.
   
   > **참고:** 실패한 패턴 일치 중에 일부 하위 패턴이 성공할 수 있습니다. 실패한 일치에 대해 바인딩이 이루어질 것이라고 의존하지 마세요. 반대로, 실패한 일치 후에 변수가 변경되지 않은 상태로 유지될 것이라고 의존하지 마세요. 정확한 동작은 구현에 따라 다를 수 있습니다. 이는 서로 다른 구현이 최적화를 추가할 수 있도록 하기 위한 의도적인 결정입니다.

3. 패턴이 성공하면 해당 가드(있는 경우)가 평가됩니다. 이 경우 모든 이름 바인딩이 발생했음이 보장됩니다.
4. 가드가 참으로 평가되거나 없는 경우, case_block 내부의 블록이 실행됩니다.
5. 그렇지 않으면 위에서 설명한 대로 다음 case_block이 시도됩니다.
6. 더 이상 case 블록이 없으면 match 문이 완료됩니다.

> **참고:** 사용자는 일반적으로 패턴이 평가된다고 의존해서는 안 됩니다. 구현에 따라 인터프리터는 값을 캐시하거나 반복 평가를 건너뛰는 다른 최적화를 사용할 수 있습니다.

A sample match statement:

```python
>>>
flag = False
match (100, 200):
   case (100, 300):  # Mismatch: 200 != 300
       print('Case 1')
   case (100, 200) if flag:  # Successful match, but guard fails
       print('Case 2')
   case (100, y):  # Matches and binds y to 200
       print(f'Case 3, y: {y}')
   case _:  # Pattern not attempted
       print('Case 4, I match anything!')

Case 3, y: 200
```

In this case, if flag is a guard. Read more about that in the next section.

match 문의 예:

```python
>>>
flag = False
match (100, 200):
   case (100, 300):  # 불일치: 200 != 300
       print('Case 1')
   case (100, 200) if flag:  # 성공적인 일치이지만 가드가 실패함
       print('Case 2')
   case (100, y):  # 일치하고 y를 200에 바인딩함
       print(f'Case 3, y: {y}')
   case _:  # 패턴이 시도되지 않음
       print('Case 4, I match anything!')

Case 3, y: 200
```

이 경우, if flag는 가드입니다. 다음 섹션에서 더 자세히 알아보세요.

8.6.2. Guards
~~~~~~~~~~~~~~~~

```
guard ::= "if" named_expression
```

A guard (which is part of the case) must succeed for code inside the case block to execute. It takes the form: if followed by an expression.

The logical flow of a case block with a guard follows:

1. Check that the pattern in the case block succeeded. If the pattern failed, the guard is not evaluated and the next case block is checked.
2. If the pattern succeeded, evaluate the guard.
3. If the guard condition evaluates as true, the case block is selected.
4. If the guard condition evaluates as false, the case block is not selected.
5. If the guard raises an exception during evaluation, the exception bubbles up.

Guards are allowed to have side effects as they are expressions. Guard evaluation must proceed from the first to the last case block, one at a time, skipping case blocks whose pattern(s) don't all succeed. (I.e., guard evaluation must happen in order.) Guard evaluation must stop once a case block is selected.

8.6.2. 가드
~~~~~~~~~~~~~~~~

```
guard ::= "if" named_expression
```

가드(case의 일부)는 case 블록 내의 코드가 실행되기 위해 성공해야 합니다. 형식은 if 다음에 표현식이 옵니다.

가드가 있는 case 블록의 논리적 흐름은 다음과 같습니다:

1. case 블록의 패턴이 성공했는지 확인합니다. 패턴이 실패하면 가드는 평가되지 않고 다음 case 블록이 확인됩니다.
2. 패턴이 성공하면 가드를 평가합니다.
3. 가드 조건이 참으로 평가되면 case 블록이 선택됩니다.
4. 가드 조건이 거짓으로 평가되면 case 블록이 선택되지 않습니다.
5. 평가 중에 가드가 예외를 발생시키면 예외가 상위로 전파됩니다.

가드는 표현식이므로 부작용을 가질 수 있습니다. 가드 평가는 첫 번째부터 마지막 case 블록까지 한 번에 하나씩 진행되어야 하며, 패턴이 모두 성공하지 않는 case 블록은 건너뜁니다(즉, 가드 평가는 순서대로 이루어져야 함). case 블록이 선택되면 가드 평가는 중지되어야 합니다.

8.6.3. Irrefutable Case Blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An irrefutable case block is a match-all case block. A match statement may have at most one irrefutable case block, and it must be last.

A case block is considered irrefutable if it has no guard and its pattern is irrefutable. A pattern is considered irrefutable if we can prove from its syntax alone that it will always succeed. Only the following patterns are irrefutable:

- AS Patterns whose left-hand side is irrefutable
- OR Patterns containing at least one irrefutable pattern
- Capture Patterns
- Wildcard Patterns
- parenthesized irrefutable patterns

8.6.3. 반박 불가능한 Case 블록
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

반박 불가능한 case 블록은 모든 것과 일치하는 case 블록입니다. match 문은 최대 하나의 반박 불가능한 case 블록을 가질 수 있으며, 이는 마지막에 위치해야 합니다.

case 블록은 가드가 없고 패턴이 반박 불가능한 경우 반박 불가능한 것으로 간주됩니다. 패턴은 그 구문만으로도 항상 성공할 것임을 증명할 수 있다면 반박 불가능한 것으로 간주됩니다. 다음 패턴만 반박 불가능합니다:

- 왼쪽 측이 반박 불가능한 AS 패턴
- 적어도 하나의 반박 불가능한 패턴을 포함하는 OR 패턴
- 캡처 패턴
- 와일드카드 패턴
- 괄호로 묶인 반박 불가능한 패턴

8.6.4. Patterns
~~~~~~~~~~~~~~~~

Note: This section uses grammar notations beyond standard EBNF:
- the notation SEP.RULE+ is shorthand for RULE (SEP RULE)*
- the notation !RULE is shorthand for a negative lookahead assertion

The top-level syntax for patterns is:

```
patterns       ::= open_sequence_pattern | pattern
pattern        ::= as_pattern | or_pattern
closed_pattern ::= | literal_pattern
                   | capture_pattern
                   | wildcard_pattern
                   | value_pattern
                   | group_pattern
                   | sequence_pattern
                   | mapping_pattern
                   | class_pattern
```

The descriptions below will include a description "in simple terms" of what a pattern does for illustration purposes (credits to Raymond Hettinger for a document that inspired most of the descriptions). Note that these descriptions are purely for illustration purposes and may not reflect the underlying implementation. Furthermore, they do not cover all valid forms.

8.6.4. 패턴
~~~~~~~~~~~~~~~~

참고: 이 섹션은 표준 EBNF를 넘어선 문법 표기법을 사용합니다:
- SEP.RULE+ 표기법은 RULE (SEP RULE)*의 축약형입니다
- !RULE 표기법은 부정 전방 탐색 단언의 축약형입니다

패턴의 최상위 구문은 다음과 같습니다:

```
patterns       ::= open_sequence_pattern | pattern
pattern        ::= as_pattern | or_pattern
closed_pattern ::= | literal_pattern
                   | capture_pattern
                   | wildcard_pattern
                   | value_pattern
                   | group_pattern
                   | sequence_pattern
                   | mapping_pattern
                   | class_pattern
```

아래 설명에는 설명을 위해 패턴이 수행하는 작업에 대한 "간단한 용어"로 설명이 포함됩니다(대부분의 설명에 영감을 준 문서에 대한 Raymond Hettinger의 공로를 인정합니다). 이러한 설명은 순전히 설명 목적이며 기본 구현을 반영하지 않을 수 있습니다. 또한 모든 유효한 형식을 다루지는 않습니다.

#### 8.6.4.1. OR Patterns

An OR pattern is two or more patterns separated by vertical bars |. Syntax:

```
or_pattern ::= "|".closed_pattern+
```

Only the final subpattern may be irrefutable, and each subpattern must bind the same set of names to avoid ambiguity.

An OR pattern matches each of its subpatterns in turn to the subject value, until one succeeds. The OR pattern is then considered successful. Otherwise, if none of the subpatterns succeed, the OR pattern fails.

In simple terms, P1 | P2 | ... will try to match P1, if it fails it will try to match P2, succeeding immediately if any succeeds, failing otherwise.

#### 8.6.4.1. OR 패턴

OR 패턴은 수직 막대 |로 구분된 두 개 이상의 패턴입니다. 구문:

```
or_pattern ::= "|".closed_pattern+
```

마지막 하위 패턴만 반박 불가능할 수 있으며, 각 하위 패턴은 모호함을 피하기 위해 동일한 이름 집합을 바인딩해야 합니다.

OR 패턴은 하나가 성공할 때까지 주체 값에 대해 각 하위 패턴을 차례로 일치시킵니다. 그러면 OR 패턴은 성공적인 것으로 간주됩니다. 그렇지 않고 하위 패턴이 모두 성공하지 못하면 OR 패턴은 실패합니다.

간단히 말해서, P1 | P2 | ...은 P1을 일치시키려고 시도하고, 실패하면 P2를 일치시키려고 시도하며, 어느 하나라도 성공하면 즉시 성공하고, 그렇지 않으면 실패합니다.

#### 8.6.4.2. AS Patterns

An AS pattern matches an OR pattern on the left of the as keyword against a subject. Syntax:

```
as_pattern ::= or_pattern "as" capture_pattern
```

If the OR pattern fails, the AS pattern fails. Otherwise, the AS pattern binds the subject to the name on the right of the as keyword and succeeds. capture_pattern cannot be a _.

In simple terms P as NAME will match with P, and on success it will set NAME = <subject>.

#### 8.6.4.2. AS 패턴

AS 패턴은 as 키워드의 왼쪽에 있는 OR 패턴을 주체와 대조합니다. 구문:

```
as_pattern ::= or_pattern "as" capture_pattern
```

OR 패턴이 실패하면 AS 패턴도 실패합니다. 그렇지 않으면 AS 패턴은 주체를 as 키워드 오른쪽의 이름에 바인딩하고 성공합니다. capture_pattern은 _일 수 없습니다.

간단히 말해서 P as NAME은 P와 일치하고, 성공하면 NAME = <주체>로 설정합니다.

#### 8.6.4.3. Literal Patterns

A literal pattern corresponds to most literals in Python. Syntax:

```
literal_pattern ::= signed_number
                    | signed_number "+" NUMBER
                    | signed_number "-" NUMBER
                    | strings
                    | "None"
                    | "True"
                    | "False"
signed_number   ::= ["-"] NUMBER
```

The rule strings and the token NUMBER are defined in the standard Python grammar. Triple-quoted strings are supported. Raw strings and byte strings are supported. f-strings are not supported.

The forms signed_number '+' NUMBER and signed_number '-' NUMBER are for expressing complex numbers; they require a real number on the left and an imaginary number on the right. E.g. 3 + 4j.

In simple terms, LITERAL will succeed only if <subject> == LITERAL. For the singletons None, True and False, the is operator is used.

#### 8.6.4.3. 리터럴 패턴

리터럴 패턴은 파이썬의 대부분의 리터럴에 해당합니다. 구문:

```
literal_pattern ::= signed_number
                    | signed_number "+" NUMBER
                    | signed_number "-" NUMBER
                    | strings
                    | "None"
                    | "True"
                    | "False"
signed_number   ::= ["-"] NUMBER
```

strings 규칙과 NUMBER 토큰은 표준 파이썬 문법에 정의되어 있습니다. 삼중 따옴표 문자열이 지원됩니다. 원시 문자열과 바이트 문자열이 지원됩니다. f-문자열은 지원되지 않습니다.

signed_number '+' NUMBER와 signed_number '-' NUMBER 형식은 복소수를 표현하기 위한 것입니다. 왼쪽에 실수, 오른쪽에 허수가 필요합니다. 예: 3 + 4j.

간단히 말해서, LITERAL은 <주체> == LITERAL일 경우에만 성공합니다. None, True, False와 같은 싱글톤의 경우 is 연산자가 사용됩니다.

#### 8.6.4.4. Capture Patterns

A capture pattern binds the subject value to a name. Syntax:

```
capture_pattern ::= !'_' NAME
```

A single underscore _ is not a capture pattern (this is what !'_' expresses). It is instead treated as a wildcard_pattern.

In a given pattern, a given name can only be bound once. E.g. case x, x: ... is invalid while case [x] | x: ... is allowed.

Capture patterns always succeed. The binding follows scoping rules established by the assignment expression operator in PEP 572; the name becomes a local variable in the closest containing function scope unless there's an applicable global or nonlocal statement.

In simple terms NAME will always succeed and it will set NAME = <subject>.

#### 8.6.4.4. 캡처 패턴

캡처 패턴은 주체 값을 이름에 바인딩합니다. 구문:

```
capture_pattern ::= !'_' NAME
```

단일 밑줄 _는 캡처 패턴이 아닙니다(이것이 !'_'가 표현하는 것입니다). 대신 와일드카드 패턴으로 취급됩니다.

주어진 패턴에서 주어진 이름은 한 번만 바인딩될 수 있습니다. 예를 들어, case x, x: ...는 유효하지 않지만 case [x] | x: ...는 허용됩니다.

캡처 패턴은 항상 성공합니다. 바인딩은 PEP 572의 할당 표현식 연산자에 의해 설정된 스코핑 규칙을 따릅니다. 적용 가능한 global 또는 nonlocal 문이 없는 한, 이름은 가장 가까운 함수 스코프에서 지역 변수가 됩니다.

간단히 말해서, NAME은 항상 성공하며 NAME = <주체>로 설정합니다.

#### 8.6.4.5. Wildcard Patterns

A wildcard pattern always succeeds (matches anything) and binds no name. Syntax:

```
wildcard_pattern ::= '_'
```

_ is a soft keyword within any pattern, but only within patterns. It is an identifier, as usual, even within match subject expressions, guards, and case blocks.

In simple terms, _ will always succeed.

#### 8.6.4.5. 와일드카드 패턴

와일드카드 패턴은 항상 성공하며(모든 것과 일치함) 어떤 이름도 바인딩하지 않습니다. 구문:

```
wildcard_pattern ::= '_'
```

_는 패턴 내에서는 소프트 키워드이지만, 패턴 내에서만 그렇습니다. match 주체 표현식, 가드, case 블록 내에서도 평소와 같이 식별자입니다.

간단히 말해서, _는 항상 성공합니다.

#### 8.6.4.6. Value Patterns

A value pattern represents a named value in Python. Syntax:

```
value_pattern ::= attr
attr          ::= name_or_attr "." NAME
name_or_attr  ::= attr | NAME
```

The dotted name in the pattern is looked up using standard Python name resolution rules. The pattern succeeds if the value found compares equal to the subject value (using the == equality operator).

In simple terms NAME1.NAME2 will succeed only if <subject> == NAME1.NAME2

> **Note:** If the same value occurs multiple times in the same match statement, the interpreter may cache the first value found and reuse it rather than repeat the same lookup. This cache is strictly tied to a given execution of a given match statement.

#### 8.6.4.6. 값 패턴

값 패턴은 파이썬에서 명명된 값을 나타냅니다. 구문:

```
value_pattern ::= attr
attr          ::= name_or_attr "." NAME
name_or_attr  ::= attr | NAME
```

패턴의 도트 이름은 표준 파이썬 이름 해결 규칙을 사용하여 조회됩니다. 발견된 값이 주체 값과 동일하게 비교되면(== 동등 연산자 사용) 패턴이 성공합니다.

간단히 말해서, NAME1.NAME2는 <주체> == NAME1.NAME2인 경우에만 성공합니다.

> **참고:** 동일한 값이 동일한 match 문에서 여러 번 발생하는 경우, 인터프리터는 첫 번째로 발견된 값을 캐시하고 동일한 조회를 반복하는 대신 재사용할 수 있습니다. 이 캐시는 특정 match 문의 특정 실행에 엄격하게 연결됩니다.

#### 8.6.4.7. Group Patterns

A group pattern allows users to add parentheses around patterns to emphasize the intended grouping. Otherwise, it has no additional syntax. Syntax:

```
group_pattern ::= "(" pattern ")"
```

In simple terms (P) has the same effect as P.

#### 8.6.4.7. 그룹 패턴

그룹 패턴을 사용하면 사용자가 의도한 그룹화를 강조하기 위해 패턴 주위에 괄호를 추가할 수 있습니다. 그렇지 않으면 추가 구문이 없습니다. 구문:

```
group_pattern ::= "(" pattern ")"
```

간단히 말해서, (P)는 P와 동일한 효과를 가집니다.

#### 8.6.4.8. Sequence Patterns

A sequence pattern contains several subpatterns to be matched against sequence elements. The syntax is similar to the unpacking of a list or tuple.

```
sequence_pattern       ::= "[" [maybe_sequence_pattern] "]"
                           | "(" [open_sequence_pattern] ")"
open_sequence_pattern  ::= maybe_star_pattern "," [maybe_sequence_pattern]
maybe_sequence_pattern ::= ",".maybe_star_pattern+ ","?
maybe_star_pattern     ::= star_pattern | pattern
star_pattern           ::= "*" (capture_pattern | wildcard_pattern)
```

There is no difference if parentheses or square brackets are used for sequence patterns (i.e. (...) vs [...] ).

> **Note:** A single pattern enclosed in parentheses without a trailing comma (e.g. (3 | 4)) is a group pattern. While a single pattern enclosed in square brackets (e.g. [3 | 4]) is still a sequence pattern.

At most one star subpattern may be in a sequence pattern. The star subpattern may occur in any position. If no star subpattern is present, the sequence pattern is a fixed-length sequence pattern; otherwise it is a variable-length sequence pattern.

The following is the logical flow for matching a sequence pattern against a subject value:

1. If the subject value is not a sequence [2], the sequence pattern fails.
2. If the subject value is an instance of str, bytes or bytearray the sequence pattern fails.
3. The subsequent steps depend on whether the sequence pattern is fixed or variable-length.

If the sequence pattern is fixed-length:
- If the length of the subject sequence is not equal to the number of subpatterns, the sequence pattern fails
- Subpatterns in the sequence pattern are matched to their corresponding items in the subject sequence from left to right. Matching stops as soon as a subpattern fails. If all subpatterns succeed in matching their corresponding item, the sequence pattern succeeds.

Otherwise, if the sequence pattern is variable-length:
- If the length of the subject sequence is less than the number of non-star subpatterns, the sequence pattern fails.
- The leading non-star subpatterns are matched to their corresponding items as for fixed-length sequences.
- If the previous step succeeds, the star subpattern matches a list formed of the remaining subject items, excluding the remaining items corresponding to non-star subpatterns following the star subpattern.
- Remaining non-star subpatterns are matched to their corresponding subject items, as for a fixed-length sequence.

> **Note:** The length of the subject sequence is obtained via len() (i.e. via the __len__() protocol). This length may be cached by the interpreter in a similar manner as value patterns.

In simple terms [P1, P2, P3, … , P<N>] matches only if all the following happens:
- check <subject> is a sequence
- len(subject) == <N>
- P1 matches <subject>[0] (note that this match can also bind names)
- P2 matches <subject>[1] (note that this match can also bind names)
- … and so on for the corresponding pattern/element.

#### 8.6.4.8. 시퀀스 패턴

시퀀스 패턴은 시퀀스 요소에 대해 일치시킬 여러 하위 패턴을 포함합니다. 구문은 리스트나 튜플의 언패킹과 유사합니다.

```
sequence_pattern       ::= "[" [maybe_sequence_pattern] "]"
                           | "(" [open_sequence_pattern] ")"
open_sequence_pattern  ::= maybe_star_pattern "," [maybe_sequence_pattern]
maybe_sequence_pattern ::= ",".maybe_star_pattern+ ","?
maybe_star_pattern     ::= star_pattern | pattern
star_pattern           ::= "*" (capture_pattern | wildcard_pattern)
```

시퀀스 패턴에 괄호나 대괄호를 사용하는 데 차이가 없습니다(즉, (...) vs [...])

> **참고:** 후행 쉼표 없이 괄호로 묶인 단일 패턴(예: (3 | 4))은 그룹 패턴입니다. 반면 대괄호로 묶인 단일 패턴(예: [3 | 4])은 여전히 시퀀스 패턴입니다.

시퀀스 패턴에는 최대 하나의 별표 하위 패턴이 있을 수 있습니다. 별표 하위 패턴은 어느 위치에서든 발생할 수 있습니다. 별표 하위 패턴이 없으면 시퀀스 패턴은 고정 길이 시퀀스 패턴입니다. 그렇지 않으면 가변 길이 시퀀스 패턴입니다.

주체 값에 대한 시퀀스 패턴 일치의 논리적 흐름은 다음과 같습니다:

1. 주체 값이 시퀀스가 아니면[2], 시퀀스 패턴은 실패합니다.
2. 주체 값이 str, bytes 또는 bytearray의 인스턴스인 경우 시퀀스 패턴은 실패합니다.
3. 후속 단계는 시퀀스 패턴이 고정 길이인지 가변 길이인지에 따라 달라집니다.

시퀀스 패턴이 고정 길이인 경우:
- 주체 시퀀스의 길이가 하위 패턴의 수와 같지 않으면 시퀀스 패턴은 실패합니다.
- 시퀀스 패턴의 하위 패턴은 왼쪽에서 오른쪽으로 주체 시퀀스의 해당 항목과 일치됩니다. 하위 패턴이 실패하는 즉시 일치가 중지됩니다. 모든 하위 패턴이 해당 항목과 일치하는 데 성공하면 시퀀스 패턴은 성공합니다.

그렇지 않고 시퀀스 패턴이 가변 길이인 경우:
- 주체 시퀀스의 길이가 별표가 아닌 하위 패턴의 수보다 작으면 시퀀스 패턴은 실패합니다.
- 선행하는 별표가 아닌 하위 패턴은 고정 길이 시퀀스와 마찬가지로 해당 항목과 일치됩니다.
- 이전 단계가 성공하면, 별표 하위 패턴은 별표 하위 패턴 다음에 오는 별표가 아닌 하위 패턴에 해당하는 나머지 항목을 제외한 나머지 주체 항목으로 형성된 리스트와 일치합니다.
- 나머지 별표가 아닌 하위 패턴은 고정 길이 시퀀스와 마찬가지로 해당 주체 항목과 일치됩니다.

> **참고:** 주체 시퀀스의 길이는 len()을 통해 얻습니다(즉, __len__() 프로토콜을 통해). 이 길이는 값 패턴과 유사한 방식으로 인터프리터에 의해 캐시될 수 있습니다.

간단히 말해서, [P1, P2, P3, … , P<N>]은 다음 모든 조건이 충족될 때만 일치합니다:
- <주체>가 시퀀스인지 확인
- len(subject) == <N>
- P1이 <subject>[0]와 일치함(이 일치가 이름도 바인딩할 수 있음에 유의)
- P2가 <subject>[1]과 일치함(이 일치가 이름도 바인딩할 수 있음에 유의)
- ... 등 해당 패턴/요소에 대해 계속됨.
