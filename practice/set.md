# 집합(Set)

집합은 순서가 없고 중복을 허용하지 않는 자료형입니다. 

## 집합 생성

```python
# 중괄호를 사용한 집합 생성
fruit_basket = {"apple", "banana", "grape"}

# set() 함수를 사용한 집합 생성
numbers = set([1, 2, 3, 4, 5])

# 빈 집합 생성 (주의: 빈 중괄호 {}는 딕셔너리를 생성합니다)
empty_set = set()
```

## 집합 연산

### 집합에 요소 추가

```python
fruit_basket = {"apple", "banana", "grape"}
fruit_basket.add("orange")
print(fruit_basket)  # 출력: {'apple', 'banana', 'grape', 'orange'}
```

### 집합에서 요소 제거

```python
fruit_basket = {"apple", "banana", "grape", "orange"}
fruit_basket.remove("banana")  # 요소가 없으면 KeyError 발생
print(fruit_basket)  # 출력: {'apple', 'grape', 'orange'}

# discard() 메서드는 요소가 없어도 오류가 발생하지 않음
fruit_basket.discard("kiwi")  # 오류 없음
```

### 집합 업데이트

```python
fruit_basket = {"apple", "grape", "orange"}
more_fruits = ["kiwi", "pear", "apple"]
fruit_basket.update(more_fruits)
print(fruit_basket)  # 출력: {'apple', 'grape', 'orange', 'kiwi', 'pear'}
```

## 집합 수학 연산

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 합집합(Union)
print(a | b)  # {1, 2, 3, 4, 5, 6}
print(a.union(b))  # {1, 2, 3, 4, 5, 6}

# 교집합(Intersection)
print(a & b)  # {3, 4}
print(a.intersection(b))  # {3, 4}

# 차집합(Difference)
print(a - b)  # {1, 2}
print(a.difference(b))  # {1, 2}

# 대칭 차집합(Symmetric Difference)
print(a ^ b)  # {1, 2, 5, 6}
print(a.symmetric_difference(b))  # {1, 2, 5, 6}
```

## 집합 포함 관계 확인

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

# 부분집합(Subset) 확인
print(a.issubset(b))  # True
print(a <= b)  # True

# 진부분집합(Proper Subset) 확인
print(a < b)  # True

# 상위집합(Superset) 확인
print(b.issuperset(a))  # True
print(b >= a)  # True

# 진상위집합(Proper Superset) 확인
print(b > a)  # True
```

## 집합 컴프리헨션(Set Comprehension)

리스트 컴프리헨션과 유사하게 집합 컴프리헨션을 사용할 수 있습니다.

```python
# 1부터 10까지의 짝수로 구성된 집합
even_numbers = {x for x in range(1, 11) if x % 2 == 0}
print(even_numbers)  # {2, 4, 6, 8, 10}
```

## 집합과 다른 자료형 비교

| 특성 | 집합(Set) | 리스트(List) | 튜플(Tuple) | 딕셔너리(Dict) |
|------|---------|------------|------------|--------------|
| 순서 | X | O | O | X |
| 중복 | X | O | O | 키: X, 값: O |
| 변경 가능 | O | O | X | O |
| 인덱싱 | X | O | O | 키로 접근 |
| 생성 | `{}`, `set()` | `[]`, `list()` | `()`, `tuple()` | `{key:value}`, `dict()` |

## 실용적인 집합 활용 사례

### 중복 제거

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)  # [1, 2, 3, 4, 5] (순서는 보장되지 않음)
```

### 멤버십 테스트

집합은 리스트보다 멤버십 테스트(요소 포함 여부 확인)가 빠릅니다.

```python
large_list = list(range(10000))
large_set = set(range(10000))

# 시간 비교 (set이 훨씬 빠름)
import time

# 리스트 검색
start = time.time()
9999 in large_list
end = time.time()
print(f"리스트 검색 시간: {end - start}")

# 집합 검색
start = time.time()
9999 in large_set
end = time.time()
print(f"집합 검색 시간: {end - start}")
```

### 공통 요소 찾기

```python
users_a = {"Alice", "Bob", "Charlie", "David"}
users_b = {"Charlie", "Dave", "Eve", "Frank"}

# 두 집합에 모두 있는 사용자 찾기
common_users = users_a & users_b
print(common_users)  # {'Charlie'}
```

## 집합 사용 시 주의사항

1. 집합의 요소는 해시 가능(hashable)해야 합니다. 따라서 리스트나 딕셔너리는 집합의 요소가 될 수 없습니다.
2. 집합은 순서를 보장하지 않으므로, 순서가 중요한 경우에는 적합하지 않습니다.
3. `remove()` 메서드 사용 시 요소가 없으면 KeyError가 발생합니다. 오류 방지를 위해 `discard()` 메서드를 사용하는 것이 좋습니다.
4. 집합은 해시 테이블을 기반으로 하므로 매우 빠른 검색 속도를 제공합니다(O(1)).
