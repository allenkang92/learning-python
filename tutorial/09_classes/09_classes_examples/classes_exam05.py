




class MyClass:
    """
    A simple example class
    """
    i = 12345

    def f(self):
        return 'hello world'
    
    def __init__(self):
        self.data = []


x = MyClass()
x.counter = 1

while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
# 16
del x.counter
