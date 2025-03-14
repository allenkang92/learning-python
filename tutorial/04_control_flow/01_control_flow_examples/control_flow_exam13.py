

# 피보나치 수열 함수 만들기

def fib(n): # write Fibonacci series less than n
    """
    Print a Fibonacci series less than n.
    """
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, (a + b)
    print()

# Now call the function we just defined:
fib(2000)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

fib
# <function fib at 0x107fc84c0>

# f라는 식별자에 fib 함수를 할당.
f = fib 
f(100)
# 0 1 1 2 3 5 8 13 21 34 55 89

fib(0)
print(fib(0))
# None