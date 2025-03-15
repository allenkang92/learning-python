



def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations", f.__annotations__)
    print("Argurments", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
# Annotations {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
# Argurments spam eggs
# spam and eggs