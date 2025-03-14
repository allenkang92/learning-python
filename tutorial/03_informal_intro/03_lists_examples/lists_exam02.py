

# 불변인 문자열(문자열은 이뮤터블)
# 리스트는 가변적(뮤터블하다)
# 즉, 내용을 변경할 수 있다는 것.


cubes = [1, 8, 27, 65, 125] # something's wrong here -> 65

4 ** 3
# 64

cubes[3] = 64 # replace the wrong value

cubes
# [1, 8, 27, 64, 125]

# 리스트.append() 메서드를 사용해서 리스트 끝 부분에
# 새로운 항목을 추가할 수 있다.

cubes.append(216) # add the cube of 6 of 7
cubes.append(7 ** 3) # and the cube of 7

cubes
# [1, 8, 27, 64, 125, 216, 343]