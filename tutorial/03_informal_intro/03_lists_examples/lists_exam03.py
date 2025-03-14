
# 파이썬에서 단순 할당은 데이터를 복사하지 않는다.
# 식별자에 리스트를 할당하면 식별자는 기존 리스트를 참조한다.
# 하나의 식별자를 통해서 리스트를 변경하면 해당 리스트를 참조하는
# 다른 모든 식별자를 통해서도 변경사항이 보인다.

rgb = ["R", "G", "B"]

rgba = rgb

id(rgb) == id(rgba) # they reference the same object
# True

rgba.append("Alph")

rgb
# ['R', 'G', 'B', 'Alph']

# 모든 슬라이스 연산은 요청된 요소를 포함하는 새 리스트를 반환한다.
correct_rgba = rgba[:]

correct_rgba[-1] = "Alpha"

correct_rgba
# ['R', 'G', 'B', 'Alpha']

print(rgba)
# ['R', 'G', 'B', 'Alph']

id(correct_rgba) == id(rgba)
# False

