


x = 3.141592

print(x.as_integer_ratio())
# (3537118140137533, 1125899906842624)

print(x == 3537118140137533 / 1125899906842624)
# True

print(x.hex())
# 0x1.921fafc8b007ap+1

print(x == float.fromhex('0x1.921fafc8b007ap+1'))
# True
