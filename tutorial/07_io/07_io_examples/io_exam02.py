

# 숫자 리터럴에 사용된 언더스코어(_)는 Python 3.6부터 도입된 기능
# 큰 숫자를 읽기 쉽게 만들기 위한 시각적 구분자
# 언더스코어는 Python 인터프리터에 의해 무시되며, 숫자의 값이나 타입에는 전혀 영향을 미치지 않습니다. 단지 코드를 읽는 사람이 큰 숫자를 더 쉽게 읽을 수 있도록 도와주는 역할만

yes_votes = 42_572_654
total_votes =  85_705_149
percentage = yes_votes / total_votes

print('{:-9} YES votes {:2.2%}'.format(yes_votes, percentage))
# 42572654 YES votes 49.67%