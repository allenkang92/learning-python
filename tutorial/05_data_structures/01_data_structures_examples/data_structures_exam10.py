



# 인덱스 사용해서 리스트에서 항목을 제거 하는 방법
# del. 

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
# [1, 66.25, 333, 333, 1234.5]


del a[2:4]
print(a)
# [1, 66.25, 1234.5]


del a[:]
print(a)
# []

del a
print(a)
# line 24, in <module>
#     print(a)
# NameError: name 'a' is not defined