

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)

f(0)
# 42

f(1)
# 43