

def foo(name, **kwds):
    return 'name' in kwds

foo(1, **{'name' : 2})
# line 6, in <module>
#     foo(1, **{'name' : 2})
# TypeError: foo() got multiple values for argument 'name'

