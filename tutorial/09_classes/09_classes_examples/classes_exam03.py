




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
print(dir(x))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'data', 'f', 'i']