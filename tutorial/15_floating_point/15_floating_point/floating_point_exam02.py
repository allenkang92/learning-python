


print(0.1 + 0.1 + 0.1 == 0.3)
# False

print(round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1))
# False


import math
print(math.isclose(0.1 + 0.1 + 0.1, 0.3))
# True

print(round(math.pi, ndigits = 2) == round(22 / 7, ndigits = 2))
# True