# 비트 연산자(Bitwise Operator)

비트 연산자는 2진수 형태로 데이터를 다룰 때 사용해요.
비트 연산자를 이해하기 위한 베이스는 "전등 스위치"를 들 수 있어요.
전등 스위치는 켜짐(1)과 꺼짐(0), 두 가지 상태만 있어요.
*여기서 켜짐은 True, 꺼짐은 False를 의미해요.

## 기본 비트 연산자

### AND 연산(&)
두 개의 스위치가 모두 켜져 있을 때만 전등이 켜지는 거예요.

```python
# AND 연산
result = 5 & 3  # 101 & 011 = 001
print(result)   # 출력: 1
```

### OR 연산(|)
두 개의 스위치 중 하나라도 켜져 있으면 전등이 켜지는 거예요.

```python
# OR 연산
result = 5 | 3  # 101 | 011 = 111
print(result)   # 출력: 7
```

### XOR 연산(^)
두 개의 스위치 중 하나만 켜져 있을 때 전등이 켜지는 거예요.
(서로의 결과가 달라야 전등이 켜진다는 의미예요)

```python
# XOR 연산
result = 5 ^ 3  # 101 ^ 011 = 110
print(result)   # 출력: 6
```

### NOT 연산(~)
스위치의 상태를 반대로 바꾸는 연산이에요. 켜진 스위치는 끄고, 꺼진 스위치는 켜요.

```python
# NOT 연산
result = ~5     # ~101 = -(101 + 1) = -110 = -6
print(result)   # 출력: -6
```

## 비트 시프트 연산자

### 왼쪽 시프트(<<)
왼쪽으로 한칸 이동은 맨 오른쪽에 0하나를 추가한다는 의미예요.
즉, 2를 곱하는 효과가 있어요.

```python
# 왼쪽 시프트 연산
result = 5 << 1  # 101 << 1 = 1010
print(result)    # 출력: 10
```

### 오른쪽 시프트(>>)
오른쪽으로 한칸 이동은 맨 오른쪽 값을 지운다는 의미예요.
여기서 2진수 0101과 10은 같은 2를 뜻해요.

```python
# 오른쪽 시프트 연산
result = 5 >> 1  # 101 >> 1 = 010
print(result)    # 출력: 2
```

## 비트 연산자 활용 예제

### 홀수/짝수 확인

```python
# 마지막 비트가 0이면 짝수, 1이면 홀수
def is_even(num):
    return num & 1 == 0

print(is_even(4))  # 출력: True
print(is_even(7))  # 출력: False
```

### 특정 비트 설정/해제

```python
# n번째 비트 설정 (0부터 시작)
def set_bit(num, n):
    return num | (1 << n)

# n번째 비트 해제
def clear_bit(num, n):
    return num & ~(1 << n)

# n번째 비트 토글(반전)
def toggle_bit(num, n):
    return num ^ (1 << n)

# n번째 비트 확인
def check_bit(num, n):
    return (num & (1 << n)) != 0

# 예제
number = 10  # 1010
print(set_bit(number, 0))    # 1011 = 11
print(clear_bit(number, 1))  # 1000 = 8
print(toggle_bit(number, 3)) # 0010 = 2
print(check_bit(number, 1))  # True
```

### 두 변수 값 교환

```python
# XOR 연산을 사용한 두 변수 값 교환
a = 5
b = 9
print(f"교환 전: a = {a}, b = {b}")

a = a ^ b
b = a ^ b
a = a ^ b

print(f"교환 후: a = {a}, b = {b}")  # 출력: 교환 후: a = 9, b = 5
```

### 2의 거듭제곱 확인

```python
# 2의 거듭제곱인지 확인 (딱 하나의 비트만 1인 경우)
def is_power_of_two(num):
    return num > 0 and (num & (num - 1)) == 0

print(is_power_of_two(8))   # 출력: True (1000)
print(is_power_of_two(10))  # 출력: False (1010)
```

## 비트 연산자 성능 이점

비트 연산은 매우 빠른 연산으로, 특히 다음과 같은 경우에 유용합니다:

1. 플래그 관리 (여러 상태를 하나의 정수로 관리)
2. 메모리 효율성이 중요한 경우
3. 하드웨어 제어나 저수준 프로그래밍
4. 암호화 알고리즘
5. 그래픽 처리

## 주의사항

1. 비트 연산은 정수형에만 적용됩니다.
2. 부호 있는 정수(signed integer)의 경우, 비트 시프트 연산이 예상과 다르게 동작할 수 있습니다.
3. 파이썬에서 정수는 크기 제한이 없기 때문에, 매우 큰 수에 대한 비트 연산 결과에 유의해야 합니다.
