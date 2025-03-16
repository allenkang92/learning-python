

# 리스트 메서드를 사용하는 예시
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))
# 2

print(fruits.count('tangerine'))
# 0

print(fruits.index('banana'))
# 3

print(fruits.index('banana', 4)) # Find next banana starting at position 4
# 6

fruits.reverse()

print(fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

fruits.append('grape')
print(fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

fruits.sort()
print(fruits)
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

print(fruits.pop())
# pear
