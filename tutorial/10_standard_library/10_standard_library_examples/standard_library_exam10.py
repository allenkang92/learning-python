

import random

print(random.choice(['apple', 'pear', 'banana']))

print(random.sample(range(100), 10)) # sampling without replacement

print(random.random()) # random float from the interval (0.0, 1.0)

print(random.randrange(6)) # random integer chosen from range(6)


# 1회차
# apple
# [17, 98, 67, 56, 31, 99, 60, 10, 80, 61]
# 0.259
# 0

# 2회차
# pear
# [81, 89, 21, 79, 54, 5, 37, 32, 93, 52]
# 0.8647539995354865
# 2

# 3회차
# banana
# [23, 30, 11, 96, 74, 0, 1, 98, 8, 82]
# 0.853371477241472
# 5

# -> 고정값 아님.