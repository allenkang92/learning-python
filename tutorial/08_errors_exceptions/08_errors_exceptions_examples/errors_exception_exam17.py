


def divide(x, y):
    try:
        result = x / y

    except ZeroDivisionError:
        print("division by zero!")
    
    else:
        print("result is", result)

    finally:
        print("executing finally clause")

divide(2, 1)
# result is 2.0
# executing finally clause

divide(2, 0)
# division by zero!
# executing finally clause

divide('2', '1')
# line 25, in <module>
#     divide('2', '1')
#   File "/../../learning-python/practice-python/tutorial/08_errors_exceptions/08_errors_exceptions_examples/errors_exception_exam17.py", line 6, in divide
#     result = x / y
# TypeError: unsupported operand type(s) for /: 'str' and 'str'