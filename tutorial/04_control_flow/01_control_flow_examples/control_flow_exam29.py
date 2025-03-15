

pairs = [(1, 'one'),
         (2, 'two'),
         (3, 'three'),
         (4, 'four')]

# sort() 메서드에서 key 매개변수는 "무엇을 기준으로 정렬할지"를 알려주는 역할
pairs.sort(key = lambda pair: pair[1])
print(pairs)
# 알파벳 순서 정렬..
# [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]