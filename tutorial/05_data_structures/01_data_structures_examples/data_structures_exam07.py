
# call a method on each element

freshfruit = ['  banana', '  loganberry', 'passion fruit  ']

print([weapon.strip() for weapon in freshfruit])
# ['banana', 'loganberry', 'passion fruit']



# create a list of 2-tuples like (number, square)
print([(x, x ** 2) for x in range(6)])
# 

# [x, x ** 2 for x in range(6)]
# line 15
#     [x, x ** 2 for x in range(6)]
#                ^
# SyntaxError: invalid syntax

# flatten a list using a listcomp with two 'for'

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])
# [1, 2, 3, 4, 5, 6, 7, 8, 9]