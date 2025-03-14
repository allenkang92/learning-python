
word = 'Python'

# 양수 인덱스 계산 => 양수 인덱싱

word[0] # character in position 0 
# 'P'

word[5] # charcter in postition 5
# 'n'


# 음수 인덱스 계산 => 음수 인덱싱
# -0은 0과 같기 때문에 음수 인덱스는 -1부터 시작.

word[-1] # last character
# 'n'

word[-2] # second-last character
# 'o'

word[-6]
# 'P'

# 슬라이싱 -> 사용하면 부분 문자열을 얻을 수 있음.

word[0:2] # characters from position 0 (included) to 2 (excluded)
# 'Py'

word[2:5] # characters form posiotion 2 (included) to 5 (excluded)
# 'tho'


# 슬라이스 인덱스에는 기본값이 있다. 
# 생략된 첫 번째 인덱스는 0, 
# 두 번째 인덱스는 슬라이스 되는 문자열의 크기로 
# 기본 설정 되어 있다.

word[:2] # character from the beginning to position 2 (excluded)
# 'Py'

word[4:] # character from position 4 (included) to the end
# 'on'

word[-2:] # character from the second-last (included) to the end
# 'on'

# 시작은 항상 포함되고,
# 끝은 항상 제외된다는 점을 유의하자.
# s[:i] + s[i:]는 항상 s와 같다.
word[:2] + word[2:]
# Python

word[:4] + word[4:]
# Python

word[42]
# line 57, in <module>
#    print(word[42])

word[4:42]
# 'on'

word[42:]
# '' (공백)

# 파이썬의 문자열은 이뮤터블, 불변이다.
# 문자열의 인덱스 위치에 할당을 하면 오류가 발생한다.

word[0] = 'J'
# line 69, in <module>
#     word[0] = 'J'
# TypeError: 'str' object does not support item assignment

word[2:] = 'py'
# line 75, in <module>
#     word[2:] = 'py'
# TypeError: 'str' object does not support item assignment

# 다른 문자열이 필요하면 새 문자열을 만들어야 한다.

'J' + word[1:]
# 'Jython'

word[:2] + 'py'
# 'Pypy'