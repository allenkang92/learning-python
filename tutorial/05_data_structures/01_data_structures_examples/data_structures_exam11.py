

# 튜플

t = 12345, 54321, 'hello!'

print(t[0])
# 12345

print(t)
# (12345, 54321, 'hello!')

u = t, (1, 2, 3, 4, 5)

print(u)
# ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Tuples are immutable:
t[0] = 88888
# line 19, in <module>
#     t[0] = 88888
# TypeError: 'tuple' object does not support item assignment

