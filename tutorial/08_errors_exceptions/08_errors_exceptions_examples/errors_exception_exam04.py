

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst)) # the exception type
    print(inst.args) # argument stored in .args
    print(inst) # __str__ allows args to be printed directly,
                # but may be overridden in exception subclasses
    x, y = inst.args # unpack args
    print('x = ', x)
    print('y = ', y)
# <class 'Exception'>
# ('spam', 'eggs')
# ('spam', 'eggs')
# x =  spam
# y =  eggs    