

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
# [1]
# [1, 2]
# [1, 2, 3]