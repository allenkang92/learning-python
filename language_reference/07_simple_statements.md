# 7. Simple statements  
# 7. 단순 문장

A simple statement is comprised within a single logical line. Several simple statements may occur on a single line separated by semicolons.  
단순 문장은 단일 논리적 라인 내에 구성되며, 여러 단순 문장이 세미콜론으로 구분되어 한 줄에 나타날 수 있습니다.

The syntax for simple statements is:  
단순 문장의 구문은 다음과 같습니다:
```
simple_stmt ::= expression_stmt
                | assert_stmt
                | assignment_stmt
                | augmented_assignment_stmt
                | annotated_assignment_stmt
                | pass_stmt
                | del_stmt
                | return_stmt
                | yield_stmt
                | raise_stmt
                | break_stmt
                | continue_stmt
                | import_stmt
                | future_stmt
                | global_stmt
                | nonlocal_stmt
                | type_stmt
```

## 7.2. Assignment statements  
(See section Primaries for the syntax definitions for attributeref, subscription, and slicing.)  
(속성 참조, 서브스크립션, 슬라이싱의 구문 정의는 Primaries 섹션을 참조하십시오.)

An assignment statement evaluates the expression list (remember that this can be a single expression or a comma-separated list, the latter yielding a tuple) and assigns the single resulting object to each of the target lists, from left to right.  
할당 문장은 표현식 목록(단일 표현식이거나 쉼표로 구분된 목록; 후자는 튜플을 생성함)을 평가한 후, 왼쪽에서 오른쪽 순서로 각 대상 리스트에 단일 결과 객체를 할당합니다.

Assignment is defined recursively depending on the form of the target (list). When a target is part of a mutable object (an attribute reference, subscription or slicing), the mutable object must ultimately perform the assignment and decide about its validity, and may raise an exception if the assignment is unacceptable. The rules observed by various types and the exceptions raised are given with the definition of the object types (see section The standard type hierarchy).  
할당은 대상(리스트)의 형태에 따라 재귀적으로 정의됩니다. 만약 대상이 가변 객체(속성 참조, 서브스크립션 또는 슬라이싱)의 일부라면, 해당 가변 객체가 할당을 수행하고 유효성을 결정하며, 할당이 부적절할 경우 예외를 발생시킬 수 있습니다. 여러 타입에 의해 적용되는 규칙과 발생 가능한 예외들은 객체 타입의 정의(표준 타입 계층 섹션 참조)와 함께 설명됩니다.

Assignment of an object to a target list, optionally enclosed in parentheses or square brackets, is recursively defined as follows.  
괄호나 대괄호로 선택적으로 둘러싸인 대상 리스트에 객체를 할당하는 것은 다음과 같이 재귀적으로 정의됩니다.

- If the target list is a single target with no trailing comma, optionally in parentheses, the object is assigned to that target.  
  - 만약 대상 리스트가 후행 쉼표가 없는 단일 대상(괄호 안에 있을 수도 있음)이라면, 객체는 해당 대상에 할당됩니다.

- Else:  
  - 그 외, 만약 대상 리스트에 별표(*)가 접두어로 붙은 단일 대상(‘starred’ 대상)이 포함되어 있다면:  
    The object must be an iterable with at least as many items as there are targets in the target list, minus one. The first items of the iterable are assigned, from left to right, to the targets before the starred target. The final items of the iterable are assigned to the targets after the starred target. A list of the remaining items in the iterable is then assigned to the starred target (the list can be empty).  
    객체는 대상 리스트에 있는 대상의 개수에서 하나를 뺀 만큼의 항목을 가진 반복 가능한(iterable) 객체여야 합니다. 반복 가능한 객체의 첫 항목부터 순서대로 별표 대상 앞의 대상들에 할당되며, 마지막 항목들은 별표 대상 뒤의 대상들에 할당됩니다. 남은 항목들의 리스트가 별표 대상에 할당됩니다(리스트는 비어 있을 수도 있습니다).
  
  - Else: The object must be an iterable with the same number of items as there are targets in the target list, and the items are assigned, from left to right, to the corresponding targets.  
    그렇지 않으면, 객체는 대상 리스트의 대상 개수와 동일한 항목 수를 가진 반복 가능한 객체여야 하며, 항목들은 왼쪽에서 오른쪽 순서대로 각각의 대상에 할당됩니다.

Assignment of an object to a single target is recursively defined as follows.  
단일 대상에 객체를 할당하는 것은 다음과 같이 재귀적으로 정의됩니다.

- If the target is an identifier (name):  
  - 만약 대상이 식별자(이름)라면:
    - If the name does not occur in a global or nonlocal statement in the current code block: the name is bound to the object in the current local namespace.  
      만약 현재 코드 블록에서 해당 이름이 global 또는 nonlocal 문에 나타나지 않으면, 이름은 현재 지역 네임스페이스에 객체로 바인딩됩니다.
    - Otherwise: the name is bound to the object in the global namespace or the outer namespace determined by nonlocal, respectively.  
      그렇지 않으면, 이름은 전역 네임스페이스 또는 nonlocal로 결정된 외부 네임스페이스에 바인딩됩니다.
    - The name is rebound if it was already bound. This may cause the reference count for the object previously bound to the name to reach zero, causing the object to be deallocated and its destructor (if it has one) to be called.  
      이미 바인딩된 경우 이름은 재바인딩되며, 이로 인해 이전에 해당 이름에 바인딩된 객체의 참조 카운트가 0이 되어 객체가 할당 해제되고(있다면) 소멸자 호출이 발생할 수 있습니다.

- If the target is an attribute reference:  
  - 만약 대상이 속성 참조라면:
    The primary expression in the reference is evaluated. It should yield an object with assignable attributes; if this is not the case, TypeError is raised. That object is then asked to assign the assigned object to the given attribute; if it cannot perform the assignment, it raises an exception (usually but not necessarily AttributeError).  
    참조 내의 기본 표현식이 평가되어 할당 가능한 속성을 가진 객체를 반환해야 하며, 그렇지 않으면 TypeError가 발생합니다. 이후 그 객체가 주어진 속성에 할당된 객체를 할당하도록 요청하며, 할당이 불가능하면 (보통 AttributeError지만 반드시 그렇지는 않음) 예외가 발생합니다.
    
    Note: If the object is a class instance and the attribute reference occurs on both sides of the assignment operator, the right-hand side expression, a.x, can access either an instance attribute or (if no instance attribute exists) a class attribute. The left-hand side target a.x is always set as an instance attribute, creating it if necessary. Thus, the two occurrences of a.x do not necessarily refer to the same attribute: if the right-hand side expression refers to a class attribute, the left-hand side creates a new instance attribute as the target of the assignment.  
    참고: 만약 객체가 클래스 인스턴스이고 할당 연산자의 양쪽에 a.x 형태의 속성 참조가 있으면, 오른쪽 표현식은 인스턴스 속성 또는 (인스턴스 속성이 없을 경우) 클래스 속성에 접근할 수 있습니다. 반면, 왼쪽의 a.x 대상은 항상 인스턴스 속성으로 설정되어 필요 시 생성됩니다. 그러므로 a.x의 두 출현이 반드시 같은 속성을 참조하지는 않습니다 (오른쪽이 클래스 속성을 참조하면 왼쪽은 새로운 인스턴스 속성을 생성합니다).
    
    ```python
    class Cls:
        x = 3             # class variable
    inst = Cls()
    inst.x = inst.x + 1   # inst.x becomes 4 while Cls.x remains 3
    ```
    (이 설명은 property()로 생성된 descriptor 속성 등에는 반드시 적용되지 않습니다.)

- If the target is a subscription:  
  - 만약 대상이 인덱싱(서브스크립션)이라면:
    The primary expression in the reference is evaluated. It should yield either a mutable sequence object (such as a list) or a mapping object (such as a dictionary). Next, the subscript expression is evaluated.  
    참조 내의 기본 표현식이 평가되어 가변 시퀀스(예: 리스트)나 매핑(예: 딕셔너리) 객체를 반환해야 하며, 그 후 서브스크립트 표현식이 평가됩니다.
    
    - If the primary is a mutable sequence object (such as a list), the subscript must yield an integer. If it is negative, the sequence’s length is added to it. The resulting value must be a nonnegative integer less than the sequence’s length, and the sequence is asked to assign the assigned object to its item with that index. If the index is out of range, IndexError is raised (assignment to a subscripted sequence cannot add new items to a list).  
      만약 기본 객체가 가변 시퀀스(예: 리스트)라면, 서브스크립트는 정수를 반환해야 하며 음수이면 시퀀스 길이를 더합니다. 결과 값은 시퀀스 길이보다 작은 0 이상의 정수여야 하며, 해당 인덱스의 항목에 객체가 할당됩니다. 인덱스가 범위를 벗어나면 IndexError가 발생합니다.
    
    - If the primary is a mapping object (such as a dictionary), the subscript must have a type compatible with the mapping’s key type, and the mapping is then asked to create a key/value pair which maps the subscript to the assigned object. This can either replace an existing key/value pair with the same key value, or insert a new key/value pair (if no key with the same value existed).  
      만약 기본 객체가 매핑(예: 딕셔너리)이라면, 서브스크립트는 매핑의 키 타입과 호환되어야 하며, 해당 서브스크립트를 키로 하여 객체를 값으로 갖는 새 키/값 쌍을 생성합니다. 이 과정은 기존 키/값 쌍을 대체하거나(동일한 키가 있을 경우) 새로 추가합니다.
    
    For user-defined objects, the __setitem__() method is called with appropriate arguments.  
    사용자 정의 객체의 경우, __setitem__() 메서드가 적절한 인수와 함께 호출됩니다.

- If the target is a slicing:  
  - 만약 대상이 슬라이싱이라면:
    The primary expression in the reference is evaluated. It should yield a mutable sequence object (such as a list). The assigned object should be a sequence object of the same type. Next, the lower and upper bound expressions are evaluated, insofar they are present; defaults are zero and the sequence’s length. The bounds should evaluate to integers. If either bound is negative, the sequence’s length is added to it. The resulting bounds are clipped to lie between zero and the sequence’s length, inclusive. Finally, the sequence object is asked to replace the slice with the items of the assigned sequence. The length of the slice may be different from the length of the assigned sequence, thus changing the length of the target sequence, if the target sequence allows it.  
    참조 내의 기본 표현식이 평가되어 가변 시퀀스(예: 리스트) 객체를 반환해야 하며, 할당되는 객체도 동일 타입의 시퀀스여야 합니다. 그 후, 하한과 상한 표현식이 평가되며, 만약 생략되면 기본값은 각각 0과 시퀀스 길이입니다. 하한과 상한은 정수로 평가되어야 하며, 음수인 경우 시퀀스 길이를 더합니다. 결과 범위는 0 이상 시퀀스 길이 이하로 잘라내어지고, 마지막으로 시퀀스 객체는 해당 슬라이스를 할당된 시퀀스의 항목들로 대체합니다. 만약 할당된 시퀀스의 길이가 기존 슬라이스와 다르면 대상 시퀀스의 길이가 변경될 수 있습니다.

CPython implementation detail: In the current implementation, the syntax for targets is taken to be the same as for expressions, and invalid syntax is rejected during the code generation phase, causing less detailed error messages.  
CPython 구현 세부 사항: 현재 구현에서는 대상에 대한 구문을 표현식과 동일하게 간주하며, 잘못된 구문은 코드 생성 단계에서 거부되어 상세하지 않은 오류 메시지를 발생시킵니다.

Although the definition of assignment implies that overlaps between the left-hand side and the right-hand side are ‘simultaneous’ (for example, a, b = b, a swaps two variables), overlaps within the collection of assigned-to variables occur left-to-right, sometimes resulting in confusion. For instance, the following program prints [0, 2]:  
비록 할당의 정의가 좌변과 우변이 ‘동시에’ 발생하는 것으로 암시하더라도 (예: a, b = b, a가 두 변수를 교환함), 할당 대상 변수 집합 내의 겹침은 왼쪽에서 오른쪽 순으로 발생하여 때로 혼란을 초래합니다. 예를 들어, 다음 프로그램은 [0, 2]를 출력합니다:

```python
x = [0, 1]
i = 0
i, x[i] = 1, 2         # i가 먼저 업데이트 된 후 x[i]가 업데이트됨
print(x)
```

See also: PEP 3132 – Extended Iterable Unpacking, which specifies the *target feature.  
또한, *target 기능에 대한 명세는 PEP 3132 - Extended Iterable Unpacking을 참조하십시오.

## 7.2.1. Augmented assignment statements
Augmented assignment is the combination, in a single statement, of a binary operation and an assignment statement.
증강 할당은 단일 문장에서 이항 연산과 할당 문을 결합한 것입니다.

```
augmented_assignment_stmt ::= augtarget augop (expression_list | yield_expression)
augtarget                 ::= identifier | attributeref | subscription | slicing
augop                     ::= "+=" | "-=" | "*=" | "@=" | "/=" | "//=" | "%=" | "**="
                              | ">>=" | "<<=" | "&=" | "^=" | "|="
```
(See section Primaries for the syntax definitions of the last three symbols.)
(마지막 세 기호의 구문 정의는 Primaries 섹션을 참조하십시오.)

An augmented assignment evaluates the target (which, unlike normal assignment statements, cannot be an unpacking) and the expression list, performs the binary operation specific to the type of assignment on the two operands, and assigns the result to the original target. The target is only evaluated once.
증강 할당은 (일반 할당 문과 달리 언패킹이 불가능한) 대상을 단 한 번 평가한 후, 해당 대상과 표현식 목록에 대해 타입에 맞는 이항 연산을 수행하고 그 결과를 원래 대상에 할당합니다.

An augmented assignment statement like x += 1 can be rewritten as x = x + 1 to achieve a similar, but not exactly equal effect. In the augmented version, x is only evaluated once. Also, when possible, the actual operation is performed in-place, meaning that rather than creating a new object and assigning that to the target, the old object is modified instead.
x += 1과 같은 증강 할당 문은 x = x + 1으로 바꿀 수 있지만 완전히 동일한 효과는 아닙니다. 증강 할당에서는 x가 단 한 번만 평가되고, 가능한 경우 실제 연산이 제자리에서 수행되어 새 객체를 생성하지 않고 기존 객체가 수정됩니다.

Unlike normal assignments, augmented assignments evaluate the left-hand side before evaluating the right-hand side. For example, a[i] += f(x) first looks-up a[i], then it evaluates f(x) and performs the addition, and lastly, it writes the result back to a[i].
일반 할당과 달리, 증강 할당은 오른쪽 표현식을 평가하기 전에 왼쪽 표현식을 먼저 평가합니다. 예를 들어, a[i] += f(x)는 먼저 a[i]를 조회한 후 f(x)를 평가하고 덧셈을 수행한 다음, 그 결과를 a[i]에 다시 기록합니다.

With the exception of assigning to tuples and multiple targets in a single statement, the assignment done by augmented assignment statements is handled the same way as normal assignments. Similarly, with the exception of the possible in-place behavior, the binary operation performed by augmented assignment is the same as the normal binary operations.
단일 문장에서 튜플과 여러 대상에 할당하는 경우를 제외하고, 증강 할당 문에 의한 할당은 일반 할당과 동일한 방식으로 처리됩니다. 마찬가지로, 제자리 연산이 가능한 경우를 제외하고, 증강 할당에 의해 수행되는 이항 연산은 일반 이항 연산과 동일합니다.

For targets which are attribute references, the same caveat about class and instance attributes applies as for regular assignments.
속성 참조인 대상의 경우, 클래스 및 인스턴스 속성에 대한 주의 사항은 일반 할당과 동일하게 적용됩니다.

## 7.2.2. Annotated assignment statements
Annotation assignment is the combination, in a single statement, of a variable or attribute annotation and an optional assignment statement.
주석 할당은 단일 문장에서 변수 또는 속성 주석과 선택적인 할당 문을 결합한 것입니다.

```
annotated_assignment_stmt ::= augtarget ":" expression
                              ["=" (starred_expression | yield_expression)]
```
The difference from normal assignment statements is that only a single target is allowed.
일반 할당 문과의 차이점은 단 하나의 대상만 허용된다는 것입니다.

The assignment target is considered “simple” if it consists of a single name that is not enclosed in parentheses. For simple assignment targets, if in class or module scope, the annotations are evaluated and stored in a special class or module attribute __annotations__ that is a dictionary mapping from variable names (mangled if private) to evaluated annotations. This attribute is writable and is automatically created at the start of class or module body execution, if annotations are found statically.
할당 대상이 괄호로 둘러싸이지 않은 단일 이름으로 구성되면 “단순”하다고 간주됩니다. 단순 할당 대상의 경우, 클래스 또는 모듈 범위 내에서는, 주석이 평가되어 변수 이름(비공개의 경우 맹글링된)에서 평가된 주석으로 매핑되는 특수 클래스 또는 모듈 속성 __annotations__에 저장됩니다. 이 속성은 쓰기 가능하며, 정적 주석이 발견되면 클래스 또는 모듈 본문 실행 시작 시 자동으로 생성됩니다.

If the assignment target is not simple (an attribute, subscript node, or parenthesized name), the annotation is evaluated if in class or module scope, but not stored.
할당 대상이 단순하지 않은 경우(예: 속성, 서브스크립션 노드, 괄호로 둘러싸인 이름), 주석은 클래스 또는 모듈 범위 내에서는 평가되지만 저장되지는 않습니다.

If a name is annotated in a function scope, then this name is local for that scope. Annotations are never evaluated and stored in function scopes.
함수 범위 내에서 이름이 주석 처리되면, 해당 이름은 그 범위의 지역 변수로 간주됩니다. 함수 범위에서는 주석이 평가되어 저장되지 않습니다.

If the right hand side is present, an annotated assignment performs the actual assignment before evaluating annotations (where applicable). If the right hand side is not present for an expression target, then the interpreter evaluates the target except for the last __setitem__() or __setattr__() call.
우변이 존재하면, 주석 할당은 (적용 가능한 경우) 주석 평가 전에 실제 할당을 수행합니다. 우변이 없는 경우, 인터프리터는 마지막 __setitem__() 또는 __setattr__() 호출을 제외하고 대상을 평가합니다.

See also  
PEP 526 - Syntax for Variable Annotations  
PEP 484 - Type hints
(참조:  
PEP 526 - 변수 주석 문법  
PEP 484 - 타입 힌트)
Changed in version 3.8: Now annotated assignments allow the same expressions in the right hand side as regular assignments. Previously, some expressions (like un-parenthesized tuple expressions) caused a syntax error.
버전 3.8에서 변경됨: 이제 주석 할당은 우측에 일반 할당과 동일한 표현식을 허용합니다. 이전에는 괄호 없는 튜플 표현식과 같이 일부 표현식에서 구문 오류가 발생했습니다.

## 7.3. The assert statement
Assert statements are a convenient way to insert debugging assertions into a program:
```
assert_stmt ::= "assert" expression ["," expression]
```
The simple form, `assert expression`, is equivalent to
```
if __debug__:
    if not expression: raise AssertionError
```
The extended form, `assert expression1, expression2`, is equivalent to
```
if __debug__:
    if not expression1: raise AssertionError(expression2)
```
These equivalences assume that `__debug__` and `AssertionError` refer to the built-in variables with those names. In the current implementation, the built-in variable `__debug__` is True under normal circumstances, False when optimization is requested (command line option -O). The current code generator emits no code for an assert statement when optimization is requested at compile time. Note that it is unnecessary to include the source code for the expression that failed in the error message; it will be displayed as part of the stack trace.

**Korean Translation:**
어설트(assert) 문은 프로그램에 디버깅용 어설션을 삽입하는 편리한 방법입니다:
```
assert_stmt ::= "assert" expression ["," expression]
```
단순한 형태인 `assert expression`은 다음과 동일합니다:
```
if __debug__:
    if not expression: raise AssertionError
```
확장된 형태인 `assert expression1, expression2`는 다음과 동일합니다:
```
if __debug__:
    if not expression1: raise AssertionError(expression2)
```
이 등가성은 `__debug__`와 `AssertionError`가 해당 이름의 내장 변수임을 전제로 합니다. 현재 구현에서 내장 변수 `__debug__`는 일반 상황에서는 True이며, 최적화가 요청될 경우(False)로 설정됩니다(-O 옵션). 컴파일 시 최적화가 요청되면 어설트 문에 대해 코드를 생성하지 않습니다. 실패한 표현식의 소스 코드를 오류 메시지에 포함할 필요는 없으며, 이는 스택 트레이스의 일부로 표시됩니다.

## 7.4. The pass statement
```
pass_stmt ::= "pass"
```
Pass is a null operation — when it is executed, nothing happens. It is useful as a placeholder when a statement is required syntactically, but no code needs to be executed, for example:
```
def f(arg): pass    # a function that does nothing (yet)
class C: pass       # a class with no methods (yet)
```

**Korean Translation:**
`pass`는 아무 작업도 수행하지 않는 널 연산입니다 — 실행되면 아무 일도 일어나지 않습니다. 이는 구문상 문장이 반드시 필요하지만 실행할 코드가 없을 때 자리 표시자로 유용합니다. 예를 들어:
```
def f(arg): pass    # 아직 아무것도 하지 않는 함수
class C: pass       # 아직 메서드가 없는 클래스
```

## 7.5. The del statement
```
del_stmt ::= "del" target_list
```
Deletion is recursively defined very similar to the way assignment is defined. Rather than spelling it out in full detail, here are some hints:
- Deletion of a target list recursively deletes each target, from left to right.
- Deletion of a name removes the binding of that name from the local or global namespace, depending on whether the name occurs in a global statement in the same code block. If the name is unbound, a NameError exception will be raised.
- Deletion of attribute references, subscriptions, and slicings is passed to the primary object involved; deletion of a slicing is in general equivalent to assignment of an empty slice of the right type (but even this is determined by the sliced object).

Changed in version 3.2: Previously it was illegal to delete a name from the local namespace if it occurs as a free variable in a nested block.

**Korean Translation:**
`del` 문은 할당이 정의되는 방식과 매우 유사하게 재귀적으로 정의됩니다. 모든 세부 사항을 기술하는 대신 몇 가지 포인터를 제공합니다:
- 대상 리스트의 삭제는 왼쪽에서 오른쪽 순으로 각 대상을 재귀적으로 삭제합니다.
- 이름의 삭제는 동일한 코드 블록에서 해당 이름이 global 문에 나타나는지에 따라, 그 이름의 바인딩을 지역 또는 전역 네임스페이스에서 제거합니다. 만약 이름이 바인딩되어 있지 않다면 NameError 예외가 발생합니다.
- 속성 참조, 서브스크립션 및 슬라이싱의 삭제는 관련 기본 객체에 위임되며, 슬라이싱의 삭제는 일반적으로 해당 타입의 빈 슬라이스를 할당하는 것과 동일합니다(그러나 이 또한 슬라이스된 객체에 의해 결정됩니다).

버전 3.2에서 변경됨: 이전에는 중첩 블록에서 자유 변수로 등장하는 이름을 지역 네임스페이스에서 삭제하는 것이 불법이었습니다.

## 7.6. The return statement
```
return_stmt ::= "return" [expression_list]
```
Return may only occur syntactically nested in a function definition, not within a nested class definition.
If an expression list is present, it is evaluated, else None is substituted.
Return leaves the current function call with the expression list (or None) as return value.
When return passes control out of a try statement with a finally clause, that finally clause is executed before really leaving the function.
In a generator function, the return statement indicates that the generator is done and will cause StopIteration to be raised. The returned value (if any) is used as an argument to construct StopIteration and becomes the StopIteration.value attribute.
In an asynchronous generator function, an empty return statement indicates that the asynchronous generator is done and will cause StopAsyncIteration to be raised. A non-empty return statement is a syntax error in an asynchronous generator function.

**Korean Translation:**
```
return_stmt ::= "return" [expression_list]
```
`return`은 함수 정의 내에서만 구문적으로 나타나야 하며, 중첩된 클래스 정의 내에서는 사용할 수 없습니다.
표현식 목록이 있으면 이를 평가하며, 없으면 None이 대체됩니다.
`return`은 현재 함수 호출을 종료하고, 반환 값으로 표현식 목록(또는 None)을 전달합니다.
`return`이 finally 절이 있는 try 문을 벗어날 때, 실제로 함수를 종료하기 전에 해당 finally 절이 실행됩니다.
제너레이터 함수에서 `return` 문은 제너레이터의 종료를 나타내며 StopIteration 예외를 발생시킵니다. 반환된 값(있는 경우)은 StopIteration 인스턴스를 구성하는 인수로 사용되어 StopIteration.value 속성이 됩니다.
비동기 제너레이터 함수에서는 빈 `return` 문이 제너레이터의 종료를 나타내며 StopAsyncIteration 예외를 발생시킵니다. 비어 있지 않은 `return` 문은 비동기 제너레이터 함수에서 구문 오류입니다.

## 7.7. The yield statement
```
yield_stmt ::= yield_expression
```
A yield statement is semantically equivalent to a yield expression. The yield statement can be used to omit the parentheses that would otherwise be required in the equivalent yield expression statement. For example, the yield statements
```
yield <expr>
yield from <expr>
```
are equivalent to the yield expression statements
```
(yield <expr>)
(yield from <expr>)
```
Yield expressions and statements are only used when defining a generator function, and are only used in the body of the generator function. Using yield in a function definition is sufficient to cause that definition to create a generator function instead of a normal function.
For full details of yield semantics, refer to the Yield expressions section.

**Korean Translation:**
`yield` 문은 의미상으로 `yield` 표현식과 동일합니다. `yield` 문을 사용하면, 해당 yield 표현식 문에 필요한 괄호를 생략할 수 있습니다. 예를 들어, 다음과 같은 `yield` 문
```
yield <expr>
yield from <expr>
```
은 다음과 같은 yield 표현식 문과 동일합니다:
```
(yield <expr>)
(yield from <expr>)
```
`yield` 표현식과 문은 제너레이터 함수를 정의할 때만 사용되며, 제너레이터 함수의 본문에서만 사용됩니다. 함수 정의 내에서 `yield`를 사용하면 해당 함수가 일반 함수 대신 제너레이터 함수로 생성됩니다.
자세한 yield의 의미 체계는 Yield expressions 섹션을 참조하십시오.

## 7.8. The raise statement
```
raise_stmt ::= "raise" [expression ["from" expression]]
```
If no expressions are present, raise re-raises the exception that is currently being handled (the active exception). If there isn’t an active exception, a RuntimeError is raised indicating that this is an error.
Otherwise, raise evaluates the first expression as the exception object. It must be either a subclass or an instance of BaseException. If it is a class, the exception instance will be obtained when needed by instantiating the class with no arguments.
The type of the exception is the exception instance’s class, the value is the instance itself.
A traceback object is normally created automatically when an exception is raised and attached to it as the __traceback__ attribute. You can create an exception and set your own traceback in one step using the with_traceback() exception method (which returns the same exception instance, with its traceback set to its argument), like so:
```
raise Exception("foo occurred").with_traceback(tracebackobj)
```
The from clause is used for exception chaining: if given, the second expression must be another exception class or instance. If the second expression is an exception instance, it will be attached to the raised exception as the __cause__ attribute (which is writable). If the expression is an exception class, the class will be instantiated and the resulting exception instance will be attached to the raised exception as the __cause__ attribute. If the raised exception is not handled, both exceptions will be printed.
A similar mechanism works implicitly if a new exception is raised when an exception is already being handled. The previous exception is then attached as the new exception’s __context__ attribute.
Exception chaining can be explicitly suppressed by specifying None in the from clause:
```
try:
    print(1 / 0)
except:
    raise RuntimeError("Something bad happened") from None
```
Additional information on exceptions can be found in section Exceptions, and information about handling exceptions is in section The try statement.
Changed in version 3.3: None is now permitted as Y in raise X from Y.
Added the __suppress_context__ attribute to suppress automatic display of the exception context.
Changed in version 3.11: If the traceback of the active exception is modified in an except clause, a subsequent raise statement re-raises the exception with the modified traceback. Previously, the exception was re-raised with the traceback it had when it was caught.

**Korean Translation:**
```
raise_stmt ::= "raise" [expression ["from" expression]]
```
표현식이 없으면, `raise`는 현재 처리 중인 예외(활성 예외)를 재발생시킵니다. 활성 예외가 없으면, 이것이 오류임을 나타내는 RuntimeError가 발생합니다.
그렇지 않으면, `raise`는 첫 번째 표현식을 예외 객체로 평가합니다. 이 객체는 BaseException의 서브클래스이거나 인스턴스여야 합니다. 만약 클래스라면, 인수가 없이 인스턴스화되어 필요 시 예외 인스턴스를 얻습니다.
예외의 타입은 해당 예외 인스턴스의 클래스이며, 값은 인스턴스 자체입니다.
예외 발생 시 일반적으로 traceback 객체가 자동으로 생성되어 예외의 `__traceback__` 속성에 첨부됩니다. with_traceback() 메서드를 사용하면 예외를 생성하면서 자신만의 traceback을 설정할 수 있습니다(동일한 예외 인스턴스를 반환하며, 그 traceback을 인수로 설정함). 예:
```
raise Exception("foo occurred").with_traceback(tracebackobj)
```
`from` 절은 예외 체이닝에 사용됩니다: 지정된 경우, 두 번째 표현식은 다른 예외 클래스 또는 인스턴스여야 합니다. 두 번째 표현식이 예외 인스턴스이면, 이는 발생된 예외의 `__cause__` 속성(쓰기 가능)에 첨부됩니다. 표현식이 예외 클래스이면, 그 클래스가 인스턴스화되어 결과 예외 인스턴스가 발생된 예외의 `__cause__` 속성에 첨부됩니다. 발생한 예외가 처리되지 않으면 두 예외 모두 출력됩니다.
유사한 메커니즘은 이미 처리 중인 예외가 있을 때 새 예외가 발생하면 암시적으로 작동하며, 이전 예외가 새 예외의 `__context__` 속성에 첨부됩니다.
예외 체이닝은 `from` 절에 None을 지정하여 명시적으로 억제할 수 있습니다:
```
try:
    print(1 / 0)
except:
    raise RuntimeError("Something bad happened") from None
```
예외에 대한 추가 정보는 Exceptions 섹션을, 예외 처리에 관한 정보는 try 문 섹션을 참조하십시오.
버전 3.3에서 변경됨: 이제 `raise X from Y`에서 Y로 None이 허용됩니다.
자동 예외 컨텍스트 표시를 억제하기 위해 __suppress_context__ 속성이 추가되었습니다.
버전 3.11에서 변경됨: except 절에서 활성 예외의 traceback이 수정되면, 이후의 raise 문은 수정된 traceback과 함께 예외를 재발생시킵니다. 이전에는 예외가 잡혔을 때의 traceback으로 재발생되었습니다.

## 7.9. The break statement  
break_stmt ::= "break"  
break may only occur syntactically nested in a for or while loop, but not nested in a function or class definition within that loop.  
It terminates the nearest enclosing loop, skipping the optional else clause if the loop has one.  
If a for loop is terminated by break, the loop control target keeps its current value.  
When break passes control out of a try statement with a finally clause, that finally clause is executed before really leaving the loop.

7.9. 중단(break) 문  
break_stmt ::= "break"  
break 문은 for 또는 while 루프 내에서만 구문적으로 사용할 수 있으며, 해당 루프 내에 함수나 클래스 정의가 중첩되어서는 안 됩니다.  
이 문장은 가장 가까운 루프를 종료하며, 루프에 else 절이 있을 경우 이를 건너뜁니다.  
for 루프가 break로 종료되면, 루프 제어 대상은 현재 값을 유지합니다.  
try 문에 finally 절이 있는 경우, break가 제어를 벗어나기 전에 해당 finally 절이 실행됩니다.

## 7.10. The continue statement  
continue_stmt ::= "continue"  
continue may only occur syntactically nested in a for or while loop, but not nested in a function or class definition within that loop.  
It continues with the next cycle of the nearest enclosing loop.  
When continue passes control out of a try statement with a finally clause, that finally clause is executed before really starting the next loop cycle.

7.10. 계속(continue) 문  
continue_stmt ::= "continue"  
continue 문은 for 또는 while 루프 내에서만 구문적으로 사용할 수 있으며, 해당 루프 내에 함수나 클래스 정의가 중첩되어서는 안 됩니다.  
이 문장은 가장 가까운 루프의 다음 반복으로 계속 진행합니다.  
try 문에 finally 절이 있는 경우, continue가 제어를 넘기기 전에 해당 finally 절이 실행된 후 다음 루프 반복이 시작됩니다.

## 7.11. The import statement  
import_stmt     ::= "import" module ["as" identifier] ("," module ["as" identifier])*  
                    | "from" relative_module "import" identifier ["as" identifier]  
                      ("," identifier ["as" identifier])*  
                    | "from" relative_module "import" "(" identifier ["as" identifier]  
                      ("," identifier ["as" identifier])* [","] ")"  
                    | "from" relative_module "import" "*"  
module          ::= (identifier ".")* identifier  
relative_module ::= "."* module | "."+  

The basic import statement (no from clause) is executed in two steps:  
1. Find a module, loading and initializing it if necessary.  
2. Define a name or names in the local namespace for the scope where the import statement occurs.  

When multiple clauses are present (separated by commas), the two steps are carried out separately for each clause as if they were individual import statements.

If the requested module is retrieved successfully, it is made available in the local namespace in one of three ways:  
- If the module name is followed by as, then the name following as is bound directly to the imported module.  
- If no other name is specified and the module is top level, the module’s name is bound locally as a reference to the imported module.  
- If the module is not top level, then the name of its top level package is bound locally; the imported module must then be accessed using its fully qualified name.

The from form proceeds as follows:  
1. Find the module specified in the from clause, loading and initializing it if necessary.  
2. For each identifier in the import list:  
   - Check if the imported module has an attribute by that name.  
   - If not, attempt to import a submodule with that name and check again.  
   - If still not found, raise ImportError.  
   - Otherwise, store a reference to that attribute (using the as name if specified) in the local namespace.

For example:  
- `import foo` – foo is imported and bound locally.  
- `import foo.bar.baz` – foo, foo.bar, and foo.bar.baz are imported; foo is bound locally.  
- `import foo.bar.baz as fbb` – foo.bar.baz is bound locally as fbb.  
- `from foo.bar import baz` – foo, foo.bar, and foo.bar.baz are imported; foo.bar.baz is bound as baz.  
- `from foo import attr` – foo is imported and foo.attr is bound as attr.  
- When using `from module import *`, all public names defined in the module are bound in the local namespace. Public names are determined by the module's __all__ or, if absent, by names not beginning with an underscore.

The wildcard import is allowed only at the module level and will raise a SyntaxError if used inside a function or class definition.

Relative imports use leading dots to specify the current package context:  
- One dot means the current package.  
- Two dots mean up one package level; three dots mean up two levels, etc.

importlib.import_module() is provided for dynamic module loading.  
Additionally, an auditing event named import is raised with arguments including module, filename, sys.path, sys.meta_path, and sys.path_hooks.

7.11. 임포트(import) 문  
import_stmt     ::= "import" module ["as" identifier] ("," module ["as" identifier])*  
                    | "from" relative_module "import" identifier ["as" identifier]  
                      ("," identifier ["as" identifier])*  
                    | "from" relative_module "import" "(" identifier ["as" identifier]  
                      ("," identifier ["as" identifier])* [","] ")"  
                    | "from" relative_module "import" "*"  
module          ::= (identifier ".")* identifier  
relative_module ::= "."* module | "."+  

기본 import 문(즉, from 절 없이)은 두 단계로 실행됩니다:  
1. 모듈을 찾아 필요하면 로드 및 초기화합니다.  
2. 해당 import 문이 있는 스코프의 지역 네임스페이스에 이름을 정의합니다.  

여러 구문(쉼표로 구분된)이 포함된 경우 각 구문에 대해 별도의 import 문처럼 위의 두 단계가 수행됩니다.

요청된 모듈을 성공적으로 가져오면, 다음 세 가지 방식 중 하나로 지역 네임스페이스에 제공됩니다:  
- 모듈 이름 뒤에 as가 있으면, as 뒤의 이름이 가져온 모듈에 직접 바인딩됩니다.  
- 다른 이름이 지정되지 않고 모듈이 최상위 모듈이면, 모듈의 이름이 가져온 모듈에 대한 참조로 지역 네임스페이스에 바인딩됩니다.  
- 모듈이 최상위 모듈이 아니라면, 해당 모듈을 포함하는 최상위 패키지의 이름이 지역 네임스페이스에 바인딩되며, 가져온 모듈은 전체 한정 이름을 통해 접근해야 합니다.

from 형태는 다음과 같이 진행됩니다:  
1. 필요 시 모듈을 찾아 로드 및 초기화합니다.  
2. import 구문에 명시된 각 식별자에 대해:  
   - 가져온 모듈에 해당 이름의 속성이 있는지 확인합니다.  
   - 없으면 하위 모듈을 import한 후 다시 확인합니다.  
   - 그래도 없으면 ImportError가 발생합니다.  
   - 있으면, as 절이 있으면 그 이름으로, 없으면 원래 이름으로 지역 네임스페이스에 바인딩합니다.

## 7.11.1. Future statements  
A future statement is a directive to the compiler that a module should be compiled using syntax or semantics that will be standard in a future Python release.

It is intended to ease migration to future versions by allowing new features to be used on a per-module basis before becoming standard.  
```
future_stmt ::= "from" "__future__" "import" feature ["as" identifier]
                ("," feature ["as" identifier])*  
                | "from" "__future__" "import" "(" feature ["as" identifier]
                ("," feature ["as" identifier])* [","] ")"
feature     ::= identifier
```

A future statement must appear near the top of the module; only the module docstring, comments, blank lines, or other future statements may precede it.  
Currently, the only feature requiring a future statement is annotations (see PEP 563).  
Other historical features (such as absolute_import, division, print_function, etc.) are always enabled in Python 3 and kept only for backward compatibility.

A future statement is processed specially at compile time and may affect the generated code. Its runtime semantics are that of a normal import of the __future__ module.

7.11.1. 미래(future) 문  
future_stmt ::= "from" "__future__" "import" feature ["as" identifier]
                ("," feature ["as" identifier])*  
                | "from" "__future__" "import" "(" feature ["as" identifier]
                ("," feature ["as" identifier])* [","] ")"
feature     ::= identifier

미래 문은 모듈을 미래 릴리스에서 표준이 될 구문 또는 의미 체계로 컴파일하도록 컴파일러에 지시하는 명령입니다.  
이 문은 모듈 수준에서 새로운 기능을 사용해 미래 버전으로의 마이그레이션을 원활하게 하기 위해 사용됩니다.  
미래 문은 모듈 상단에 나타나야 하며, 모듈 독스트링, 주석, 빈 줄 또는 다른 미래 문 외에는 어떠한 코드도 그보다 앞에 올 수 없습니다.  
현재 유일하게 미래 문이 필요한 기능은 어노테이션(PEP 563 참조)이며, 나머지 과거 기능들은 Python 3에서 항상 활성화되어 후방 호환성을 위해 남아 있습니다.

## 7.12. The global statement  
global_stmt ::= "global" identifier ("," identifier)*  

The global statement causes the listed identifiers to be interpreted as global. Without it, assignment to a global variable would be impossible (even though free variables may refer to globals without declaration).

It applies to the entire scope of a function or class body. A SyntaxError is raised if a variable is used or assigned before its global declaration.

7.12. 전역(global) 문  
global_stmt ::= "global" identifier ("," identifier)*  

global 문은 나열된 식별자들을 전역으로 취급하도록 만듭니다. 이를 선언하지 않으면 전역 변수에 할당할 수 없습니다(자유 변수는 선언 없이 전역을 참조할 수 있음).  
이 문은 함수나 클래스 본문의 전체 스코프에 적용되며, 전역 선언 이전에 사용되거나 할당되면 SyntaxError가 발생합니다.

## 7.13. The nonlocal statement  
nonlocal_stmt ::= "nonlocal" identifier ("," identifier)*  

When a function or class definition is nested within other functions, its “nonlocal” scopes are those of the enclosing functions.  
The nonlocal statement causes the listed identifiers to refer to variables bound in an outer (non-global) scope. If the name is not found in any enclosing scope, a SyntaxError is raised.

It applies to the entire scope of the defining function or class.  
For further details see PEP 3104.

7.13. 비지역(nonlocal) 문  
nonlocal_stmt ::= "nonlocal" identifier ("," identifier)*  

함수나 클래스 정의가 다른 함수에 중첩되어 있을 경우, 그 비지역 스코프는 둘러싼 함수들의 지역 스코프입니다.  
nonlocal 문은 나열된 식별자들이 외부(전역이 아닌) 스코프에 바인딩된 변수임을 참조하게 만듭니다. 만약 해당 이름이 어떤 외부 스코프에도 존재하지 않으면 SyntaxError가 발생합니다.  
이 문은 정의된 함수 또는 클래스의 전체 스코프에 적용됩니다. (자세한 내용은 PEP 3104를 참조하십시오.)

## 7.14. The type statement
type_stmt ::= 'type' identifier [type_params] "=" expression

The type statement declares a type alias, which is an instance of typing.TypeAliasType.

For example, the following statement creates a type alias:

    type Point = tuple[float, float]

This code is roughly equivalent to:

    annotation-def VALUE_OF_Point():
        return tuple[float, float]
    Point = typing.TypeAliasType("Point", VALUE_OF_Point())

annotation-def indicates an annotation scope, which behaves mostly like a function, but with several small differences.

The value of the type alias is evaluated in the annotation scope. It is not evaluated when the type alias is created, but only when the value is accessed through the type alias’s __value__ attribute (see Lazy evaluation). This allows the type alias to refer to names that are not yet defined.

Type aliases may be made generic by adding a type parameter list after the name. See Generic type aliases for more.

type is a soft keyword.

Added in version 3.12.

See also
PEP 695 - Type Parameter Syntax  
Introduced the type statement and syntax for generic classes and functions.
