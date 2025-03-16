


from decimal import Decimal
from fractions import Fraction

print(Fraction.from_float(0.1))
# 3602879701896397/36028797018963968

print((0.1).as_integer_ratio())
# (3602879701896397, 36028797018963968)

print(Decimal.from_float(0.1))
# 0.1000000000000000055511151231257827021181583404541015625

print(format(Decimal.from_float(0.1), '.17'))
# 0.10000000000000001