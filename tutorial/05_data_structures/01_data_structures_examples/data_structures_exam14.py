


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')

print(a) # unique letters in a
# {'d', 'c', 'b', 'r', 'a'}

print(a - b) # letters in a but not in b
# {'d', 'r', 'b'}

print(a | b) # letters in a or b or both
# {'z', 'd', 'c', 'l', 'b', 'm', 'r', 'a'}

print(a & b) # letters in both a and b
# {'c', 'a'}

print(a ^ b) # letters in a or b but not both
# {'z', 'd', 'r', 'm', 'l', 'b'}
