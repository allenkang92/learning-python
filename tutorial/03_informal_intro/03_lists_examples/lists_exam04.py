# 슬라이스에 할당하는 것도 가능하다. 
# 리스트의 크기를 변경하거나 완전히 비울 수도 있다.

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']


# replace some values
letters[2:5] = ['C', 'D', 'E']
letters
# ['a', 'b', 'C', 'D', 'E', 'f', 'g']

# now remove them
letters[2:5] = []
letters
# ['a', 'b', 'f', 'g']

# clear the list by replacing 
# all the elements with an empty list
letters[:] = []
letters
# []

# 내장 함수 len()도 리스트에 적용된다.
letters = ['a', 'b', 'c', 'd']
len(letters)
# 4