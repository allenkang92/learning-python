


s = 'abc'
it = iter(s)

print(it)
# <str_iterator object at 0x1037f6f40>

print(next(it))
# a

print(next(it))
# b

print(next(it))
# c

print(next(it))
# line 19, in <module>
#     print(next(it))
# StopIteration