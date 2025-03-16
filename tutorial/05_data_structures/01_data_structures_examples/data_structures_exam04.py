

# 제곱수 리스트 만들기

## 방법 1
squares = list()

for x in range(10):
    squares.append(x ** 2)

print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



## 방법 2
squares = list(map(lambda x: x ** 2, range(10)))

print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


## 방법 3
squares = [x ** 2 for x in range(10)]

print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]