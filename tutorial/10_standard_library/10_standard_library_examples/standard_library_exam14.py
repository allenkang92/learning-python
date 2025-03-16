


from timeit import Timer

print(Timer('t = a; a = b; b = t', 'a = 1; b = 2').timeit())
# 0.03783678400000001

print(Timer('a, b = b, a', 'a = 1; b = 2').timeit())
# 0.043898502000000034