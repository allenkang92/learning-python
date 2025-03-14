

# Fibonacci series:
# the sum of two elements defines the next.

# 언패킹 # 다중 할당.
a, b = 0, 1 # a라는 식별자에 0을 할당, b라는 식별자에 1을 할당한다.

while a < 10:
    print(a)
    a, b = b, (a + b) # 식별자 a에 b를 할당하고, 식별자 b에 a의 값과 b의 값을 언패킹하여 할당
# 0
# 1
# 1
# 2
# 3
# 5
# 8