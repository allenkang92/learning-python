


s = 'Hello, world'

print(str(s))
# Hello, world

print(repr(s))
# 'Hello, world'

print(str(1/7))
# 0.14285714285714285

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
# The value of x is 32.5, and y is 40000...

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# 'hello, world\n'

# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))
# (32.5, 40000, ('spam', 'eggs'))