


import math
from fractions import Fraction

arr = [-0.10430216751806065, -266310978.67179024, 143401161448607.16,
       -143401161400469.7, 266262841.31058735, -0.003244936839808227]

print(float(sum(map(Fraction, arr)))) # Exact summation with single rounding
# 8.042173697819788e-13

print(math.fsum(arr)) # Single rounding
# 8.042173697819788e-13

print(sum(arr)) # Multiple rounding in extended precision
# -0.0051575902860057365
# ??? -> 왜 8.042178034628478e-13 이게 아니지?

total = 0.0

for x in arr:
    total += x # Multiple roundings in standard precision

print(total) # Straight addition has no correct digits!
# -0.0051575902860057365
