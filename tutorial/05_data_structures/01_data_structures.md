# 5. Data Structures

1. This chapter describes some things you've learned about already in more detail, and adds some new things as well.

이 장에서는 이미 배운 것들을 더 자세히 설명하고, 새로운 것들도 추가합니다.

## 5.1. More on Lists

2. The list data type has some more methods. Here are all of the methods of list objects:

리스트 데이터 타입에는 더 많은 메서드가 있습니다. 다음은 리스트 객체의 모든 메서드입니다:

3. `list.append(x)`: Add an item to the end of the list. Similar to `a[len(a):] = [x]`.

`list.append(x)`: 항목을 리스트 끝에 추가합니다. `a[len(a):] = [x]`와 유사합니다.

4. `list.extend(iterable)`: Extend the list by appending all the items from the iterable. Similar to `a[len(a):] = iterable`.

`list.extend(iterable)`: 반복 가능한 객체의 모든 항목을 추가하여 리스트를 확장합니다. `a[len(a):] = iterable`과 유사합니다.

5. `list.insert(i, x)`: Insert an item at a given position. The first argument is the index of the element before which to insert, so `a.insert(0, x)` inserts at the front of the list, and `a.insert(len(a), x)` is equivalent to `a.append(x)`.

`list.insert(i, x)`: 주어진 위치에 항목을 삽입합니다. 첫 번째 인수는 삽입할 요소 앞의 인덱스이므로, `a.insert(0, x)`는 리스트 앞에 삽입하고, `a.insert(len(a), x)`는 `a.append(x)`와 동일합니다.

6. `list.remove(x)`: Remove the first item from the list whose value is equal to x. It raises a `ValueError` if there is no such item.

`list.remove(x)`: 값이 x와 같은 첫 번째 항목을 리스트에서 제거합니다. 해당 항목이 없으면 `ValueError`를 발생시킵니다.

7. `list.pop([i])`: Remove the item at the given position in the list, and return it. If no index is specified, `a.pop()` removes and returns the last item in the list. It raises an `IndexError` if the list is empty or the index is outside the list range.

`list.pop([i])`: 리스트에서 주어진 위치의 항목을 제거하고 반환합니다. 인덱스가 지정되지 않으면, `a.pop()`은 리스트의 마지막 항목을 제거하고 반환합니다. 리스트가 비어 있거나, 인덱스가 리스트 범위를 벗어나면 `IndexError`를 발생시킵니다.

8. `list.clear()`: Remove all items from the list. Similar to `del a[:]`.

`list.clear()`: 리스트에서 모든 항목을 제거합니다. `del a[:]`와 유사합니다.

9. `list.index(x[, start[, end]])`: Return zero-based index in the list of the first item whose value is equal to x. Raises a `ValueError` if there is no such item.

`list.index(x[, start[, end]])`: 값이 x와 같은 첫 번째 항목의 리스트에서 0부터 시작하는 인덱스를 반환합니다. 해당 항목이 없으면 `ValueError`를 발생시킵니다.

10. The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

선택적 인수 start와 end는 슬라이스 표기법에서와 같이 해석되며, 검색을 리스트의 특정 부분 시퀀스로 제한하는 데 사용됩니다. 반환된 인덱스는 start 인수가 아닌 전체 시퀀스의 시작을 기준으로 계산됩니다.

11. `list.count(x)`: Return the number of times x appears in the list.

`list.count(x)`: 리스트에서 x가 나타나는 횟수를 반환합니다.

12. `list.sort(*, key=None, reverse=False)`: Sort the items of the list in place (the arguments can be used for sort customization, see `sorted()` for their explanation).

`list.sort(*, key=None, reverse=False)`: 리스트의 항목들을 제자리에서 정렬합니다(인수는 정렬 사용자 정의에 사용할 수 있으며, 설명은 `sorted()`를 참조하세요).

13. `list.reverse()`: Reverse the elements of the list in place.

`list.reverse()`: 리스트의 요소를 제자리에서 뒤집습니다.

14. `list.copy()`: Return a shallow copy of the list. Similar to `a[:]`.

`list.copy()`: 리스트의 얕은 복사본을 반환합니다. `a[:]`와 유사합니다.

15. An example that uses most of the list methods:

대부분의 리스트 메서드를 사용하는 예:

```python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting at position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```

16. You might have noticed that methods like `insert`, `remove` or `sort` that only modify the list have no return value printed – they return the default `None`. [1] This is a design principle for all mutable data structures in Python.

`insert`, `remove`, `sort`와 같이 리스트만 수정하는 메서드는 반환 값이 출력되지 않는다는 것을 알 수 있습니다 - 이들은 기본 `None`을 반환합니다. [1] 이것은 파이썬의 모든 변경 가능한 데이터 구조에 대한 설계 원칙입니다.

17. Another thing you might notice is that not all data can be sorted or compared. For instance, `[None, 'hello', 10]` doesn't sort because integers can't be compared to strings and `None` can't be compared to other types. Also, there are some types that don't have a defined ordering relation. For example, `3+4j < 5+7j` isn't a valid comparison.

또 다른 점은 모든 데이터가 정렬되거나 비교될 수 있는 것은 아니라는 것입니다. 예를 들어, `[None, 'hello', 10]`은 정렬되지 않는데, 이는 정수를 문자열과 비교할 수 없고 `None`을 다른 유형과 비교할 수 없기 때문입니다. 또한, 정의된 순서 관계가 없는 일부 유형도 있습니다. 예를 들어, `3+4j < 5+7j`는 유효한 비교가 아닙니다.

### 5.1.1. Using Lists as Stacks

18. The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved ("last-in, first-out"). To add an item to the top of the stack, use `append()`. To retrieve an item from the top of the stack, use `pop()` without an explicit index. For example:

리스트 메서드는 리스트를 스택으로 사용하는 것을 매우 쉽게 만듭니다. 여기서 마지막에 추가된 요소가 가장 먼저 검색되는 요소입니다("후입선출"). 스택의 꼭대기에 항목을 추가하려면 `append()`를 사용하세요. 스택의 꼭대기에서 항목을 검색하려면 명시적 인덱스 없이 `pop()`을 사용하세요. 예를 들어:

```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

### 5.1.2. Using Lists as Queues

19. It is also possible to use a list as a queue, where the first element added is the first element retrieved ("first-in, first-out"); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

리스트를 큐로 사용하는 것도 가능합니다. 여기서 처음 추가된 요소가 처음 검색되는 요소입니다("선입선출"). 그러나 리스트는 이 목적에 효율적이지 않습니다. 리스트 끝에서의 추가와 팝은 빠르지만, 리스트 시작 부분에서 삽입하거나 팝하는 것은 느립니다(모든 다른 요소들이 한 칸씩 이동해야 하기 때문입니다).

20. To implement a queue, use `collections.deque` which was designed to have fast appends and pops from both ends. For example:

큐를 구현하려면 양쪽 끝에서 빠른 추가와 팝을 하도록 설계된 `collections.deque`를 사용하세요. 예를 들어:

```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

### 5.1.3. List Comprehensions

21. List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

리스트 컴프리헨션은 리스트를 만드는 간결한 방법을 제공합니다. 일반적인 응용은 각 요소가 다른 시퀀스나 반복 가능한 객체의 각 멤버에 적용된 일부 연산의 결과인 새 리스트를 만들거나, 특정 조건을 만족하는 요소들의 부분 시퀀스를 만드는 것입니다.

22. For example, assume we want to create a list of squares, like:

예를 들어, 다음과 같은 제곱수 리스트를 만들고 싶다고 가정해 봅시다:

```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

23. Note that this creates (or overwrites) a variable named `x` that still exists after the loop completes. We can calculate the list of squares without any side effects using:

이것은 루프가 완료된 후에도 여전히 존재하는 `x`라는 변수를 생성(또는 덮어씁니다). 다음을 사용하여 부작용 없이 제곱수 리스트를 계산할 수 있습니다:

```python
squares = list(map(lambda x: x**2, range(10)))
```

24. or, equivalently:

또는 이와 동등하게:

```python
squares = [x**2 for x in range(10)]
```

25. which is more concise and readable.

이것이 더 간결하고 읽기 쉽습니다.

26. A list comprehension consists of brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses. The result will be a new list resulting from evaluating the expression in the context of the `for` and `if` clauses which follow it. For example, this listcomp combines the elements of two lists if they are not equal:

리스트 컴프리헨션은 표현식을 포함하는 대괄호로 구성되며, 그 뒤에 `for` 절이 오고, 0개 이상의 `for` 또는 `if` 절이 옵니다. 결과는 뒤에 오는 `for`와 `if` 절의 컨텍스트에서 표현식을 평가하여 얻은 새로운 리스트가 됩니다. 예를 들어, 이 리스트 컴프리헨션은 두 리스트의 요소가 같지 않은 경우 결합합니다:

```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

27. and it's equivalent to:

이것은 다음과 동등합니다:

```python
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

28. Note how the order of the `for` and `if` statements is the same in both these snippets.

이 두 코드 조각에서 `for`와 `if` 문의 순서가 동일함에 주목하세요.

29. If the expression is a tuple (e.g. the `(x, y)` in the previous example), it must be parenthesized.

표현식이 튜플인 경우(예: 이전 예제의 `(x, y)`), 괄호로 묶어야 합니다.

```python
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1
    [x, x**2 for x in range(6)]
     ^^^^^^^
SyntaxError: did you forget parentheses around the comprehension target?
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

30. List comprehensions can contain complex expressions and nested functions:

리스트 컴프리헨션은 복잡한 표현식과 중첩 함수를 포함할 수 있습니다:

```python
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

### 5.1.4. Nested List Comprehensions

31. The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension.

리스트 컴프리헨션의 초기 표현식은 다른 리스트 컴프리헨션을 포함한 임의의 표현식일 수 있습니다.

32. Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:

길이가 4인 리스트 3개로 구현된 3x4 행렬의 다음 예를 고려하세요:

```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```

33. The following list comprehension will transpose rows and columns:

다음 리스트 컴프리헨션은 행과 열을 전치합니다:

```python
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

34. As we saw in the previous section, the inner list comprehension is evaluated in the context of the `for` that follows it, so this example is equivalent to:

이전 섹션에서 보았듯이, 내부 리스트 컴프리헨션은 그 뒤에 오는 `for`의 컨텍스트에서 평가되므로, 이 예는 다음과 동등합니다:

```python
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

35. which, in turn, is the same as:

이것은 다시, 다음과 같습니다:

```python
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

36. In the real world, you should prefer built-in functions to complex flow statements. The `zip()` function would do a great job for this use case:

실제로는 복잡한 흐름 문보다 내장 함수를 선호해야 합니다. `zip()` 함수는 이 사용 사례에 매우 적합합니다:

```python
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

37. See Unpacking Argument Lists for details on the asterisk in this line.

이 줄의 별표에 관한 자세한 내용은 인수 리스트 언패킹을 참조하세요.

## 5.2. The del statement

38. There is a way to remove an item from a list given its index instead of its value: the `del` statement. This differs from the `pop()` method which returns a value. The `del` statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice). For example:

인덱스를 사용하여 값 대신 리스트에서 항목을 제거하는 방법이 있습니다: `del` 문입니다. 이는 값을 반환하는 `pop()` 메서드와 다릅니다. `del` 문은 또한 리스트에서 슬라이스를 제거하거나 전체 리스트를 지우는 데 사용될 수 있습니다(앞서 슬라이스에 빈 리스트를 할당하여 수행했습니다). 예를 들어:

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

39. `del` can also be used to delete entire variables:

`del`은 전체 변수를 삭제하는 데도 사용할 수 있습니다:

```python
>>> del a
```

40. Referencing the name `a` hereafter is an error (at least until another value is assigned to it). We'll find other uses for `del` later.

이후 이름 `a`를 참조하면 오류가 발생합니다(적어도 다른 값이 할당될 때까지). 나중에 `del`의 다른 용도를 알아볼 것입니다.

## 5.3. Tuples and Sequences

41. We saw that lists and strings have many common properties, such as indexing and slicing operations. They are two examples of sequence data types (see Sequence Types — list, tuple, range). Since Python is an evolving language, other sequence data types may be added. There is also another standard sequence data type: the tuple.

리스트와 문자열은 인덱싱, 슬라이싱 연산과 같은 많은 공통 속성을 가지고 있습니다. 이들은 시퀀스 데이터 타입의 두 가지 예입니다(시퀀스 타입 — 리스트, 튜플, 범위 참조). 파이썬은 진화하는 언어이므로 다른 시퀀스 데이터 타입이 추가될 수 있습니다. 또 다른 표준 시퀀스 데이터 타입으로는 튜플이 있습니다.

42. A tuple consists of a number of values separated by commas, for instance:

튜플은 쉼표로 구분된 여러 값으로 구성됩니다. 예를 들어:

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
>>> u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
>>> t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
>>> v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

43. As you see, on output tuples are always enclosed in parentheses, so that nested tuples are interpreted correctly; they may be input with or without surrounding parentheses, although often parentheses are necessary anyway (if the tuple is part of a larger expression). It is not possible to assign to the individual items of a tuple, however it is possible to create tuples which contain mutable objects, such as lists.

보시다시피, 출력 시 튜플은 항상 괄호로 둘러싸여 있어 중첩 튜플이 정확하게 해석됩니다. 튜플은 주변 괄호가 있거나 없이 입력될 수 있지만, 종종 괄호가 필요합니다(튜플이 더 큰 표현식의 일부인 경우). 튜플의 개별 항목에 할당하는 것은 불가능하지만, 리스트와 같은 변경 가능한 객체를 포함하는 튜플을 생성하는 것은 가능합니다.

44. Though tuples may seem similar to lists, they are often used in different situations and for different purposes. Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

튜플이 리스트와 비슷해 보일 수 있지만, 튜플은 종종 다른 상황과 다른 목적으로 사용됩니다. 튜플은 불변이며, 일반적으로 언패킹(이 섹션의 뒷부분 참조)이나 인덱싱(또는 네임드튜플의 경우 속성으로도)을 통해 접근하는 이질적인 요소 시퀀스를 포함합니다. 리스트는 변경 가능하며, 요소들은 일반적으로 동질적이고 리스트를 반복하여 접근합니다.

45. A special problem is the construction of tuples containing 0 or 1 items: the syntax has some extra quirks to accommodate these. Empty tuples are constructed by an empty pair of parentheses; a tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses). Ugly, but effective. For example:

0개 또는 1개의 항목을 포함하는 튜플을 구성하는 데는 특별한 문제가 있습니다: 구문에는 이를 수용하기 위한 몇 가지 추가 특성이 있습니다. 빈 튜플은 빈 괄호 쌍으로 구성됩니다. 한 항목으로 구성된 튜플은 값 뒤에 쉼표를 붙여 구성됩니다(단일 값을 괄호로 묶는 것만으로는 충분하지 않습니다). 보기에는 좋지 않지만 효과적입니다. 예를 들어:

```python
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```

46. The statement `t = 12345, 54321, 'hello!'` is an example of tuple packing: the values 12345, 54321 and 'hello!' are packed together in a tuple. The reverse operation is also possible:

`t = 12345, 54321, 'hello!'` 문은 튜플 패킹의 예입니다: 값 12345, 54321 및 'hello!'가 함께 튜플로 패킹됩니다. 역 연산도 가능합니다:

```python
>>> x, y, z = t
```

47. This is called, appropriately enough, sequence unpacking and works for any sequence on the right-hand side. Sequence unpacking requires that there are as many variables on the left side of the equals sign as there are elements in the sequence. Note that multiple assignment is really just a combination of tuple packing and sequence unpacking.

이것은 적절하게도 시퀀스 언패킹이라고 불리며 오른쪽의 모든 시퀀스에 대해 작동합니다. 시퀀스 언패킹에는 등호 왼쪽에 시퀀스의 요소 수만큼 많은 변수가 필요합니다. 다중 할당은 실제로 튜플 패킹과 시퀀스 언패킹의 조합일 뿐임을 유의하세요.

## 5.4. Sets

48. Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

파이썬은 집합을 위한 데이터 타입도 포함하고 있습니다. 집합은 중복 요소가 없는 순서 없는 컬렉션입니다. 기본 용도로는 멤버십 테스트와 중복 항목 제거가 있습니다. 집합 객체는 합집합, 교집합, 차집합, 대칭 차집합과 같은 수학적 연산도 지원합니다.

49. Curly braces or the `set()` function can be used to create sets. Note: to create an empty set you have to use `set()`, not `{}`; the latter creates an empty dictionary, a data structure that we discuss in the next section.

중괄호 또는 `set()` 함수를 사용하여 집합을 생성할 수 있습니다. 참고: 빈 집합을 만들려면 `{}`가 아닌 `set()`을 사용해야 합니다. 후자는 다음 섹션에서 논의할 데이터 구조인 빈 사전을 생성합니다.

50. Here is a brief demonstration:

간단한 시연입니다:

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

51. Similarly to list comprehensions, set comprehensions are also supported:

리스트 컴프리헨션과 유사하게 집합 컴프리헨션도 지원됩니다:

```python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```

## 5.5. Dictionaries

52. Another useful data type built into Python is the dictionary (see Mapping Types — dict). Dictionaries are sometimes found in other languages as "associative memories" or "associative arrays". Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can't use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like `append()` and `extend()`.

파이썬에 내장된 또 다른 유용한 데이터 타입은 사전입니다(매핑 타입 — dict 참조). 사전은 다른 언어에서 "연관 메모리" 또는 "연관 배열"로 불리기도 합니다. 숫자 범위로 색인되는 시퀀스와 달리, 사전은 키로 색인되는데, 이 키는 어떤 불변 타입이든 될 수 있습니다. 문자열과 숫자는 항상 키로 사용될 수 있습니다. 튜플은 문자열, 숫자 또는 튜플만 포함하는 경우 키로 사용될 수 있습니다. 튜플이 직접 또는 간접적으로 변경 가능한 객체를 포함하는 경우 키로 사용될 수 없습니다. 리스트는 키로 사용할 수 없습니다. 리스트는 인덱스 할당, 슬라이스 할당 또는 `append()`와 `extend()`와 같은 메서드를 사용하여 제자리에서 수정될 수 있기 때문입니다.

53. It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: `{}`. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.

사전은 키: 값 쌍의 집합으로 생각하는 것이 가장 좋습니다. 이때 키는 (하나의 사전 내에서) 고유해야 합니다. 중괄호 쌍은 빈 사전을 생성합니다: `{}`. 중괄호 안에 쉼표로 구분된 키:값 쌍 목록을 배치하면 사전에 초기 키:값 쌍이 추가됩니다. 이것은 출력에 사전이 작성되는 방식이기도 합니다.

54. The main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pair with `del`. If you store using a key that is already in use, the old value associated with that key is forgotten. It is an error to extract a value using a non-existent key.

사전의 주요 연산은 일부 키로 값을 저장하고 키를 지정하여 값을 추출하는 것입니다. `del`을 사용하여 키:값 쌍을 삭제하는 것도 가능합니다. 이미 사용 중인 키를 사용하여 저장하면 해당 키와 연관된 이전 값은 잊혀집니다. 존재하지 않는 키를 사용하여 값을 추출하는 것은 오류입니다.

55. Performing `list(d)` on a dictionary returns a list of all the keys used in the dictionary, in insertion order (if you want it sorted, just use `sorted(d)` instead). To check whether a single key is in the dictionary, use the `in` keyword.

사전에 `list(d)`를 수행하면 삽입 순서대로 사전에 사용된 모든 키의 리스트가 반환됩니다(정렬된 순서를 원한다면 대신 `sorted(d)`를 사용하세요). 하나의 키가 사전에 있는지 확인하려면 `in` 키워드를 사용하세요.

56. Here is a small example using a dictionary:

다음은 사전을 사용하는 작은 예제입니다:

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

57. The `dict()` constructor builds dictionaries directly from sequences of key-value pairs:

`dict()` 생성자는 키-값 쌍의 시퀀스에서 직접 사전을 구축합니다:

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

58. In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

또한, dict 컴프리헨션을 사용하여 임의의 키와 값 표현식에서 사전을 만들 수 있습니다:

```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

59. When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:

키가 단순한 문자열인 경우, 키워드 인수를 사용하여 쌍을 지정하는 것이 더 쉬울 때가 있습니다:

```python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

## 5.6. Looping Techniques

60. When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the `items()` method.

사전을 반복할 때, `items()` 메서드를 사용하여 키와 해당 값을 동시에 검색할 수 있습니다.

```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```

61. When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the `enumerate()` function.

시퀀스를 반복할 때, `enumerate()` 함수를 사용하여 위치 인덱스와 해당 값을 동시에 검색할 수 있습니다.

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```

62. To loop over two or more sequences at the same time, the entries can be paired with the `zip()` function.

동시에 두 개 이상의 시퀀스를 반복하려면, `zip()` 함수로 항목을 짝지을 수 있습니다.

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

63. To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the `reversed()` function.

시퀀스를 역순으로 반복하려면, 먼저 시퀀스를 정방향으로 지정한 다음 `reversed()` 함수를 호출하세요.

```python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```

64. To loop over a sequence in sorted order, use the `sorted()` function which returns a new sorted list while leaving the source unaltered.

정렬된 순서로 시퀀스를 반복하려면, 소스를 변경하지 않고 새로 정렬된 리스트를 반환하는 `sorted()` 함수를 사용하세요.

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
```

65. Using `set()` on a sequence eliminates duplicate elements. The use of `sorted()` in combination with `set()` over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.

시퀀스에 `set()`을 사용하면 중복 요소가 제거됩니다. 시퀀스에 대해 `set()`과 함께 `sorted()`를 사용하는 것은 시퀀스의 고유한 요소를 정렬된 순서로 반복하는 관용적인 방법입니다.

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```

66. It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.

리스트를 반복하는 동안 리스트를 변경하고 싶을 때가 있습니다. 그러나 대신 새 리스트를 만드는 것이 종종 더 간단하고 안전합니다.

```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

## 5.8. Comparing Sequences and Other Types

67. Sequence objects typically may be compared to other objects with the same sequence type. The comparison uses lexicographical ordering: first the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, until either sequence is exhausted. If two items to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively. If all items of two sequences compare equal, the sequences are considered equal. If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one. Lexicographical ordering for strings uses the Unicode code point number to order individual characters. Some examples of comparisons between sequences of the same type:

시퀀스 객체는 일반적으로 동일한 시퀀스 타입을 가진 다른 객체와 비교될 수 있습니다. 비교는 사전적 순서를 사용합니다: 먼저 처음 두 항목을 비교하고, 그들이 다르다면 이것이 비교의 결과를 결정합니다. 만약 그들이 같다면, 다음 두 항목을 비교하는 식으로 어느 한 시퀀스가 소진될 때까지 계속됩니다. 비교할 두 항목이 동일한 타입의 시퀀스인 경우, 사전적 비교가 재귀적으로 수행됩니다. 두 시퀀스의 모든 항목이 동일하게 비교되면, 시퀀스는 동일한 것으로 간주됩니다. 한 시퀀스가 다른 시퀀스의 초기 부분 시퀀스인 경우, 더 짧은 시퀀스가 더 작은(더 작은) 것입니다. 문자열의 사전적 순서는 유니코드 코드 포인트 번호를 사용하여 개별 문자를 정렬합니다. 동일한 타입의 시퀀스 간 비교의 몇 가지 예:

```python
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```

68. Note that comparing objects of different types with < or > is legal provided that the objects have appropriate comparison methods. For example, mixed numeric types are compared according to their numeric value, so 0 equals 0.0, etc. Otherwise, rather than providing an arbitrary ordering, the interpreter will raise a TypeError exception.

서로 다른 타입의 객체를 < 또는 >로 비교하는 것은 객체에 적절한 비교 메서드가 있는 경우 합법입니다. 예를 들어, 혼합 숫자 타입은 숫자 값에 따라 비교되므로 0은 0.0과 같습니다. 그렇지 않으면, 임의의 순서를 제공하기 보다는 인터프리터가 TypeError 예외를 발생시킵니다.

**Footnotes**

[1] 다른 언어는 변형된 객체를 반환할 수 있으며, 이를 통해 `d->insert("a")->remove("b")->sort();`와 같은 메서드 체이닝이 가능합니다.
