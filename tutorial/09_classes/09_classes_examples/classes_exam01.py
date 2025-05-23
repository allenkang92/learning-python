

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After gloval assignment:", spam)

scope_test()
print("In global scope:", spam)
# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After gloval assignment: nonlocal spam
# In global scope: global spam