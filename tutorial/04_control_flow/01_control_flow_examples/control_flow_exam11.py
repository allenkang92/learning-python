


# pass문은 아무것도 하지 않는다.
# 구문적으로 명령문이 필요하지만, 
# 프로그램이 어떤 동작도 필요로 하지 않을 때,
# 사용될 수 있다.

while True:
    pass # Busy-wait for keyboard interrupt (Ctrl + C)


class MyEmptyClass:
    pass

# pass
# 새로운 코드를 작업할 때나,
# 함수나 조건문 본문의 자리 표시자로 역할을 할 수 있다.
# 이를 통해서 더 추상적인 수준에서 생각을 계속할 수 있다.
# pass는 조용히 무시된다.

def initlog(*args):
    pass # Remember to implement this!