
# 코드의 tricks 리스트는 
# 모든 Dog 인스턴스에 의해 단일 리스트만 공유되므로 
# 클래스 변수로 사용되어서는 안 된다.

class Dog:
    
    tricks = [] # mistaken use of a class variable

    def __init__(self, name):
        self.name = name 

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')

d.add_trick('roll over')
e.add_trick('play dead')

print(d.tricks) # unexpectedly shared by all dogs
# ['roll over', 'play dead']