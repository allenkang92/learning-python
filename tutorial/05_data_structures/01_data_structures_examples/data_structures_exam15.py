


tel = {'jack' : 4098, 'sape': 4239}
tel['guido'] = 4127

print(tel)
# {'jack': 4098, 'sape': 4239, 'guido': 4127}

print(tel['jack'])
# 4098

del tel['sape']
tel['irv'] = 4127

print(tel)
# {'jack': 4098, 'guido': 4127, 'irv': 4127}

print(list(tel))
# ['jack', 'guido', 'irv']

print(sorted(tel))
# ['guido', 'irv', 'jack']

print('guido' in tel)
# True

print('jack' not in tel)
# False



# dict comprehensions
print({x : x ** 2 for x in (2, 4, 6)})
# {2: 4, 4: 16, 6: 36}


print(dict(sape = 4139, guido = 4127, jack = 4098))
# {'sape': 4139, 'guido': 4127, 'jack': 4098}