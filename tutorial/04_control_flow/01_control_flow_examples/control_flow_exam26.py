

list(range(3, 6)) # normal call with separate arguments
# [3, 4, 5]


args = [3, 6]
list(range(*args)) # call with arguments unpacked from a list
# [3, 4, 5]