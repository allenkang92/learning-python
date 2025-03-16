


vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled
print([x ** 2 for x in vec])
# [16, 4, 0, 4, 16]

# filter the list to exclude nagative numbers
print([x for x in vec if x >= 0])
# [0, 2, 4]

# apply a function to all the elements
print([abs(x) for x in vec])
# [4, 2, 0, 2, 4]
