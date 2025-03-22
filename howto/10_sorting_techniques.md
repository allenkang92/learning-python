# Sorting Techniques in Python

# Python에서의 정렬 기법

## Introduction

Sorting is a fundamental operation in computer science that arranges elements in a specific order. Python provides several built-in methods for sorting data, as well as the flexibility to implement custom sorting algorithms. This guide covers various sorting techniques in Python, from basic to advanced.

## 소개

정렬은 요소를 특정 순서로 배열하는 컴퓨터 과학의 기본 작업입니다. Python은 데이터 정렬을 위한 여러 내장 메서드와 함께 사용자 지정 정렬 알고리즘을 구현할 수 있는 유연성을 제공합니다. 이 가이드는 기본부터 고급까지 Python의 다양한 정렬 기법을 다룹니다.

## Python's Built-in Sorting Methods

Python provides two primary ways to sort data:

1. The `sorted()` function - creates a new sorted list from an iterable
2. The `list.sort()` method - sorts a list in-place

### The `sorted()` Function

The `sorted()` function can be used with any iterable and returns a new sorted list:

```python
# Sorting a list
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Sorting a tuple (returns a list)
tuple_values = (3, 1, 4, 1, 5, 9)
sorted_tuple = sorted(tuple_values)
print(sorted_tuple)  # [1, 1, 3, 4, 5, 9]

# Sorting a string (sorts individual characters)
text = "python"
sorted_text = sorted(text)
print(sorted_text)  # ['h', 'n', 'o', 'p', 't', 'y']
print(''.join(sorted_text))  # "hnopty"

# Sorting a dictionary (sorts by keys)
my_dict = {'c': 3, 'a': 1, 'b': 2}
sorted_dict_keys = sorted(my_dict)
print(sorted_dict_keys)  # ['a', 'b', 'c']
```

### The `list.sort()` Method

The `list.sort()` method modifies the list in-place and returns `None`:

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = numbers.sort()
print(result)   # None
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]
```

## Python의 내장 정렬 메서드

Python은 데이터를 정렬하는 두 가지 주요 방법을 제공합니다:

1. `sorted()` 함수 - 반복 가능한 객체에서 새로운 정렬된 리스트 생성
2. `list.sort()` 메서드 - 리스트를 제자리에서 정렬

### `sorted()` 함수

`sorted()` 함수는 모든 반복 가능한 객체와 함께 사용할 수 있으며 새로운 정렬된 리스트를 반환합니다:

```python
# 리스트 정렬
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# 튜플 정렬(리스트 반환)
tuple_values = (3, 1, 4, 1, 5, 9)
sorted_tuple = sorted(tuple_values)
print(sorted_tuple)  # [1, 1, 3, 4, 5, 9]

# 문자열 정렬(개별 문자 정렬)
text = "python"
sorted_text = sorted(text)
print(sorted_text)  # ['h', 'n', 'o', 'p', 't', 'y']
print(''.join(sorted_text))  # "hnopty"

# 딕셔너리 정렬(키 기준 정렬)
my_dict = {'c': 3, 'a': 1, 'b': 2}
sorted_dict_keys = sorted(my_dict)
print(sorted_dict_keys)  # ['a', 'b', 'c']
```

### `list.sort()` 메서드

`list.sort()` 메서드는 리스트를 제자리에서 수정하고 `None`을 반환합니다:

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = numbers.sort()
print(result)   # None
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]
```

## Sorting Order

Both `sorted()` and `list.sort()` accept a `reverse` parameter to sort in descending order:

```python
# Ascending order (default)
ascending = sorted([3, 1, 4, 1, 5, 9])
print(ascending)  # [1, 1, 3, 4, 5, 9]

# Descending order
descending = sorted([3, 1, 4, 1, 5, 9], reverse=True)
print(descending)  # [9, 5, 4, 3, 1, 1]

# In-place sorting in descending order
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 1, 1]
```

## 정렬 순서

`sorted()`와 `list.sort()` 모두 내림차순으로 정렬하기 위한 `reverse` 매개변수를 받습니다:

```python
# 오름차순(기본값)
ascending = sorted([3, 1, 4, 1, 5, 9])
print(ascending)  # [1, 1, 3, 4, 5, 9]

# 내림차순
descending = sorted([3, 1, 4, 1, 5, 9], reverse=True)
print(descending)  # [9, 5, 4, 3, 1, 1]

# 내림차순으로 제자리 정렬
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 1, 1]
```

## Custom Sorting with Key Functions

Both `sorted()` and `list.sort()` accept a `key` parameter to specify a function that is called on each list element prior to making comparisons.

### Basic Key Function

```python
# Sort by absolute value
numbers = [-4, -2, 1, 3, -5]
sorted_by_absolute = sorted(numbers, key=abs)
print(sorted_by_absolute)  # [1, -2, 3, -4, -5]

# Sort strings by length
words = ["python", "is", "awesome", "programming", "language"]
sorted_by_length = sorted(words, key=len)
print(sorted_by_length)  # ['is', 'python', 'awesome', 'language', 'programming']
```

### Lambda Functions as Keys

You can use lambda functions for more compact key definitions:

```python
# Sort by the second element in tuples
pairs = [(1, 'b'), (5, 'a'), (3, 'c'), (2, 'd')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)  # [(5, 'a'), (1, 'b'), (3, 'c'), (2, 'd')]

# Sort strings by the last character
words = ["apple", "banana", "cherry", "date"]
sorted_by_last_char = sorted(words, key=lambda s: s[-1])
print(sorted_by_last_char)  # ['banana', 'apple', 'date', 'cherry']
```

## 키 함수를 이용한 사용자 정의 정렬

`sorted()`와 `list.sort()` 모두 비교 전 각 리스트 요소에 대해 호출되는 함수를 지정하는 `key` 매개변수를 받습니다.

### 기본 키 함수

```python
# 절대값으로 정렬
numbers = [-4, -2, 1, 3, -5]
sorted_by_absolute = sorted(numbers, key=abs)
print(sorted_by_absolute)  # [1, -2, 3, -4, -5]

# 문자열을 길이로 정렬
words = ["python", "is", "awesome", "programming", "language"]
sorted_by_length = sorted(words, key=len)
print(sorted_by_length)  # ['is', 'python', 'awesome', 'language', 'programming']
```

### 키로서의 람다 함수

더 간결한 키 정의를 위해 람다 함수를 사용할 수 있습니다:

```python
# 튜플의 두 번째 요소로 정렬
pairs = [(1, 'b'), (5, 'a'), (3, 'c'), (2, 'd')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)  # [(5, 'a'), (1, 'b'), (3, 'c'), (2, 'd')]

# 문자열을 마지막 문자로 정렬
words = ["apple", "banana", "cherry", "date"]
sorted_by_last_char = sorted(words, key=lambda s: s[-1])
print(sorted_by_last_char)  # ['banana', 'apple', 'date', 'cherry']
```

### Advanced Key Functions

The `operator` module provides useful functions for common key operations:

```python
import operator

# Sort list of dictionaries by a specific key
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 30}
]
sorted_by_age = sorted(data, key=operator.itemgetter('age'))
print(sorted_by_age)  # [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]

# Sort list of tuples by multiple elements
students = [
    ('Alice', 'A', 90),
    ('Bob', 'B', 80),
    ('Charlie', 'A', 85),
    ('David', 'C', 90)
]
# Sort by grade then by score
sorted_students = sorted(students, key=operator.itemgetter(1, 2))
print(sorted_students)  # [('Alice', 'A', 90), ('Charlie', 'A', 85), ('Bob', 'B', 80), ('David', 'C', 90)]
```

### 고급 키 함수

`operator` 모듈은 일반적인 키 작업에 유용한 함수를 제공합니다:

```python
import operator

# 특정 키로 딕셔너리 리스트 정렬
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 30}
]
sorted_by_age = sorted(data, key=operator.itemgetter('age'))
print(sorted_by_age)  # [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]

# 여러 요소로 튜플 리스트 정렬
students = [
    ('Alice', 'A', 90),
    ('Bob', 'B', 80),
    ('Charlie', 'A', 85),
    ('David', 'C', 90)
]
# 성적, 그 다음 점수 순으로 정렬
sorted_students = sorted(students, key=operator.itemgetter(1, 2))
print(sorted_students)  # [('Alice', 'A', 90), ('Charlie', 'A', 85), ('Bob', 'B', 80), ('David', 'C', 90)]
```

## Implementing Common Sorting Algorithms

While Python's built-in sorting functions are optimized and sufficient for most cases, understanding common sorting algorithms can be valuable for educational purposes or special requirements.

### Bubble Sort

```python
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example
nums = [64, 34, 25, 12, 22, 11, 90]
sorted_nums = bubble_sort(nums.copy())
print(sorted_nums)  # [11, 12, 22, 25, 34, 64, 90]
```

### Selection Sort

```python
def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the unsorted part
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example
nums = [64, 25, 12, 22, 11]
sorted_nums = selection_sort(nums.copy())
print(sorted_nums)  # [11, 12, 22, 25, 64]
```

## 일반적인 정렬 알고리즘 구현

Python의 내장 정렬 함수가 최적화되어 있고 대부분의 경우 충분하지만, 일반적인 정렬 알고리즘을 이해하는 것은 교육 목적이나 특별한 요구 사항에 유용할 수 있습니다.

### 버블 정렬

```python
def bubble_sort(arr):
    n = len(arr)
    # 모든 배열 요소를 순회
    for i in range(n):
        # 마지막 i개 요소는 이미 정렬됨
        for j in range(0, n-i-1):
            # 다음 요소보다 현재 요소가 더 크면 교환
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 예시
nums = [64, 34, 25, 12, 22, 11, 90]
sorted_nums = bubble_sort(nums.copy())
print(sorted_nums)  # [11, 12, 22, 25, 34, 64, 90]
```

### 선택 정렬

```python
def selection_sort(arr):
    n = len(arr)
    # 모든 배열 요소를 순회
    for i in range(n):
        # 정렬되지 않은 부분에서 최소 요소 찾기
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 찾은 최소 요소를 첫 번째 요소와 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 예시
nums = [64, 25, 12, 22, 11]
sorted_nums = selection_sort(nums.copy())
print(sorted_nums)  # [11, 12, 22, 25, 64]
```

### Insertion Sort

```python
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Example
nums = [12, 11, 13, 5, 6]
sorted_nums = insertion_sort(nums.copy())
print(sorted_nums)  # [5, 6, 11, 12, 13]
```

### Quick Sort

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Example
nums = [10, 7, 8, 9, 1, 5]
sorted_nums = quick_sort(nums)
print(sorted_nums)  # [1, 5, 7, 8, 9, 10]
```

### Merge Sort

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # Sort the two halves
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Check if any elements were left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Example
nums = [38, 27, 43, 3, 9, 82, 10]
sorted_nums = merge_sort(nums.copy())
print(sorted_nums)  # [3, 9, 10, 27, 38, 43, 82]
```

### 삽입 정렬

```python
def insertion_sort(arr):
    # 1부터 len(arr)까지 순회
    for i in range(1, len(arr)):
        key = arr[i]
        # key보다 큰 arr[0..i-1]의 요소를
        # 현재 위치에서 한 위치 앞으로 이동
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# 예시
nums = [12, 11, 13, 5, 6]
sorted_nums = insertion_sort(nums.copy())
print(sorted_nums)  # [5, 6, 11, 12, 13]
```

### 퀵 정렬

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# 예시
nums = [10, 7, 8, 9, 1, 5]
sorted_nums = quick_sort(nums)
print(sorted_nums)  # [1, 5, 7, 8, 9, 10]
```

### 병합 정렬

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # 두 반쪽 정렬
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # 임시 배열 L[]과 R[]에 데이터 복사
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # 남은 요소가 있는지 확인
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# 예시
nums = [38, 27, 43, 3, 9, 82, 10]
sorted_nums = merge_sort(nums.copy())
print(sorted_nums)  # [3, 9, 10, 27, 38, 43, 82]
```

## Special Sorting Techniques

### Stable Sorting

A stable sort preserves the relative order of equal elements. Python's `sorted()` and `list.sort()` are stable:

```python
# Example with tuples (name, score)
students = [('Alice', 85), ('Bob', 70), ('Charlie', 85), ('David', 90)]

# Sorting by score (Alice and Charlie have the same score)
sorted_by_score = sorted(students, key=lambda x: x[1])
print(sorted_by_score)  # [('Bob', 70), ('Alice', 85), ('Charlie', 85), ('David', 90)]
# Alice appears before Charlie in the original list and in the sorted list
```

### Partial Sorting with Heapq

The `heapq` module provides functions for partial sorting, which can be more efficient when you only need a subset of sorted elements:

```python
import heapq

numbers = [10, 4, 5, 8, 2, 9, 1]

# Get the 3 smallest elements
smallest = heapq.nsmallest(3, numbers)
print(smallest)  # [1, 2, 4]

# Get the 2 largest elements
largest = heapq.nlargest(2, numbers)
print(largest)  # [10, 9]

# With key functions
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 40}
]

youngest = heapq.nsmallest(2, people, key=lambda x: x["age"])
print(youngest)  # [{"name": "Bob", "age": 25}, {"name": "Alice", "age": 30}]
```

## 특별한 정렬 기법

### 안정적 정렬

안정적 정렬은 동일한 요소의 상대적 순서를 유지합니다. Python의 `sorted()`와 `list.sort()`는 안정적입니다:

```python
# 튜플 예시 (이름, 점수)
students = [('Alice', 85), ('Bob', 70), ('Charlie', 85), ('David', 90)]

# 점수로 정렬 (Alice와 Charlie는 같은 점수)
sorted_by_score = sorted(students, key=lambda x: x[1])
print(sorted_by_score)  # [('Bob', 70), ('Alice', 85), ('Charlie', 85), ('David', 90)]
# Alice는 원래 리스트와 정렬된 리스트에서 Charlie보다 먼저 나타남
```

### Heapq를 이용한 부분 정렬

`heapq` 모듈은 부분 정렬을 위한 함수를 제공하며, 정렬된 요소의 일부만 필요할 때 더 효율적일 수 있습니다:

```python
import heapq

numbers = [10, 4, 5, 8, 2, 9, 1]

# 가장 작은 3개 요소 가져오기
smallest = heapq.nsmallest(3, numbers)
print(smallest)  # [1, 2, 4]

# 가장 큰 2개 요소 가져오기
largest = heapq.nlargest(2, numbers)
print(largest)  # [10, 9]

# 키 함수를 사용한 예시
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 40}
]

youngest = heapq.nsmallest(2, people, key=lambda x: x["age"])
print(youngest)  # [{"name": "Bob", "age": 25}, {"name": "Alice", "age": 30}]
```

### Sorting with the `sorted` Function from Natural Sort Order

For sorting strings with numbers in a "natural" way (e.g., "file1.txt" comes before "file10.txt"):

```python
import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]

file_names = ["file1.txt", "file10.txt", "file2.txt", "file20.txt"]
sorted_naturally = sorted(file_names, key=natural_sort_key)
print(sorted_naturally)  # ['file1.txt', 'file2.txt', 'file10.txt', 'file20.txt']
```

## Multi-level Sorting

### Sorting by Multiple Keys

You can sort by multiple criteria using tuples in the key function:

```python
# Sort by grade (ascending) and then by age (descending)
students = [
    ("Alice", "A", 22),
    ("Bob", "B", 20),
    ("Charlie", "A", 25),
    ("David", "C", 23)
]

sorted_students = sorted(students, key=lambda x: (x[1], -x[2]))
print(sorted_students)
# [('Charlie', 'A', 25), ('Alice', 'A', 22), ('Bob', 'B', 20), ('David', 'C', 23)]
```

### Using itemgetter for Multiple Criteria

```python
from operator import itemgetter

employees = [
    {'name': 'Alice', 'department': 'HR', 'salary': 65000},
    {'name': 'Bob', 'department': 'Dev', 'salary': 75000},
    {'name': 'Charlie', 'department': 'HR', 'salary': 70000},
    {'name': 'David', 'department': 'Dev', 'salary': 80000}
]

# Sort by department, then by salary (highest first)
sorted_employees = sorted(
    employees, 
    key=lambda e: (e['department'], -e['salary'])
)
print(sorted_employees)
# [{'name': 'David', 'department': 'Dev', 'salary': 80000}, 
#  {'name': 'Bob', 'department': 'Dev', 'salary': 75000}, 
#  {'name': 'Charlie', 'department': 'HR', 'salary': 70000}, 
#  {'name': 'Alice', 'department': 'HR', 'salary': 65000}]
```

### 자연 정렬 순서를 사용한 정렬

숫자가 포함된 문자열을 "자연스러운" 방식으로 정렬하기 위한 방법 (예: "file1.txt"가 "file10.txt"보다 먼저 옴):

```python
import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]

file_names = ["file1.txt", "file10.txt", "file2.txt", "file20.txt"]
sorted_naturally = sorted(file_names, key=natural_sort_key)
print(sorted_naturally)  # ['file1.txt', 'file2.txt', 'file10.txt', 'file20.txt']
```

## 다중 수준 정렬

### 여러 키로 정렬하기

키 함수에서 튜플을 사용하여 여러 기준으로 정렬할 수 있습니다:

```python
# 학점(오름차순)으로 정렬한 다음 나이(내림차순)로 정렬
students = [
    ("Alice", "A", 22),
    ("Bob", "B", 20),
    ("Charlie", "A", 25),
    ("David", "C", 23)
]

sorted_students = sorted(students, key=lambda x: (x[1], -x[2]))
print(sorted_students)
# [('Charlie', 'A', 25), ('Alice', 'A', 22), ('Bob', 'B', 20), ('David', 'C', 23)]
```

### 여러 기준에 itemgetter 사용하기

```python
from operator import itemgetter

employees = [
    {'name': 'Alice', 'department': 'HR', 'salary': 65000},
    {'name': 'Bob', 'department': 'Dev', 'salary': 75000},
    {'name': 'Charlie', 'department': 'HR', 'salary': 70000},
    {'name': 'David', 'department': 'Dev', 'salary': 80000}
]

# 부서별, 그 다음 급여(가장 높은 것 먼저) 순으로 정렬
sorted_employees = sorted(
    employees, 
    key=lambda e: (e['department'], -e['salary'])
)
print(sorted_employees)
# [{'name': 'David', 'department': 'Dev', 'salary': 80000}, 
#  {'name': 'Bob', 'department': 'Dev', 'salary': 75000}, 
#  {'name': 'Charlie', 'department': 'HR', 'salary': 70000}, 
#  {'name': 'Alice', 'department': 'HR', 'salary': 65000}]
```

## Performance Considerations

### Time Complexity of Sorting Algorithms

| Algorithm      | Best Case  | Average Case | Worst Case | Space Complexity | Stable? |
|----------------|------------|--------------|------------|------------------|---------|
| Bubble Sort    | O(n)       | O(n²)        | O(n²)      | O(1)             | Yes     |
| Selection Sort | O(n²)      | O(n²)        | O(n²)      | O(1)             | No      |
| Insertion Sort | O(n)       | O(n²)        | O(n²)      | O(1)             | Yes     |
| Merge Sort     | O(n log n) | O(n log n)   | O(n log n) | O(n)             | Yes     |
| Quick Sort     | O(n log n) | O(n log n)   | O(n²)      | O(log n)         | No      |
| Heap Sort      | O(n log n) | O(n log n)   | O(n log n) | O(1)             | No      |
| Python's built-in sort (Timsort) | O(n) | O(n log n) | O(n log n) | O(n) | Yes |

### Performance Tips

1. **Use built-in functions**: Python's built-in sorting is highly optimized.
2. **Choose the right algorithm**: Consider the nature of your data and the specific requirements of your task.
3. **Pre-compute values**: If the key function is expensive, pre-compute the values.
4. **For small subsets**: Use `heapq.nsmallest()` or `heapq.nlargest()` instead of sorting the entire list.
5. **For large datasets**: Consider using specialized libraries like NumPy or Pandas.

## 성능 고려 사항

### 정렬 알고리즘의 시간 복잡도

| 알고리즘       | 최선의 경우 | 평균적인 경우 | 최악의 경우 | 공간 복잡도 | 안정성? |
|----------------|------------|--------------|------------|------------------|---------|
| 버블 정렬      | O(n)       | O(n²)        | O(n²)      | O(1)             | 예      |
| 선택 정렬      | O(n²)      | O(n²)        | O(n²)      | O(1)             | 아니오  |
| 삽입 정렬      | O(n)       | O(n²)        | O(n²)      | O(1)             | 예      |
| 병합 정렬      | O(n log n) | O(n log n)   | O(n log n) | O(n)             | 예      |
| 퀵 정렬        | O(n log n) | O(n log n)   | O(n²)      | O(log n)         | 아니오  |
| 힙 정렬        | O(n log n) | O(n log n)   | O(n log n) | O(1)             | 아니오  |
| Python 내장 정렬(Timsort) | O(n) | O(n log n) | O(n log n) | O(n) | 예 |

### 성능 팁

1. **내장 함수 사용하기**: Python의 내장 정렬은 매우 최적화되어 있습니다.
2. **적절한 알고리즘 선택하기**: 데이터의 특성과 작업의 특정 요구 사항을 고려하세요.
3. **값 미리 계산하기**: 키 함수가 비싸다면, 값을 미리 계산하세요.
4. **작은 부분집합의 경우**: 전체 리스트를 정렬하는 대신 `heapq.nsmallest()` 또는 `heapq.nlargest()`를 사용하세요.
5. **대규모 데이터셋의 경우**: NumPy나 Pandas 같은 특화된 라이브러리 사용을 고려하세요.

## Best Practices

1. **Use built-in sorting**: In most cases, Python's built-in `sorted()` or `list.sort()` is the best choice.

2. **Understand key functions**: Key functions can greatly simplify sorting complex data structures.

3. **Choose in-place vs. new list**: Use `list.sort()` for in-place sorting to save memory, or `sorted()` when you need to preserve the original list.

4. **Consider stability**: If maintaining the relative order of equal elements is important, ensure you're using a stable sort.

5. **Optimize for large datasets**: For very large datasets, consider if you actually need a full sort or just the smallest/largest elements.

6. **Profile your code**: If sorting is a performance bottleneck, measure the impact of different sorting approaches.

## Conclusion

Python provides powerful and flexible tools for sorting data. The built-in sorting functions are sufficient for most use cases, but understanding various sorting algorithms and techniques can be valuable for optimizing performance or handling special requirements.

By mastering Python's sorting capabilities, you can write more efficient code and solve complex data manipulation problems with ease.

## 모범 사례

1. **내장 정렬 사용하기**: 대부분의 경우 Python의 내장 `sorted()` 또는 `list.sort()`가 최선의 선택입니다.

2. **키 함수 이해하기**: 키 함수는 복잡한 데이터 구조 정렬을 크게 단순화할 수 있습니다.

3. **제자리 vs. 새 리스트 선택하기**: 메모리를 절약하기 위해 제자리 정렬에는 `list.sort()`를 사용하고, 원래 리스트를 보존해야 할 때는 `sorted()`를 사용하세요.

4. **안정성 고려하기**: 동일한 요소의 상대적 순서 유지가 중요하다면, 안정적인 정렬을 사용하고 있는지 확인하세요.

5. **대규모 데이터셋 최적화하기**: 매우 큰 데이터셋의 경우, 전체 정렬이 필요한지 아니면 가장 작은/큰 요소만 필요한지 고려하세요.

6. **코드 프로파일링하기**: 정렬이 성능 병목 현상이라면, 다양한 정렬 접근법의 영향을 측정하세요.

## 결론

Python은 데이터 정렬을 위한 강력하고 유연한 도구를 제공합니다. 내장 정렬 함수는 대부분의 사용 사례에 충분하지만, 다양한 정렬 알고리즘과 기법을 이해하는 것은 성능을 최적화하거나 특별한 요구 사항을 처리하는 데 유용할 수 있습니다.

Python의 정렬 기능을 마스터함으로써, 더 효율적인 코드를 작성하고 복잡한 데이터 조작 문제를 쉽게 해결할 수 있습니다.

