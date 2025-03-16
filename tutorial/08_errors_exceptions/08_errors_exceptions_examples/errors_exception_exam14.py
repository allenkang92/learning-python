


try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

# Traceback (most recent call last):
#   File "/../../learning-python/practice-python/tutorial/08_errors_exceptions/08_errors_exceptions_examples/errors_exception_exam14.py", line 7, in <module>
#     raise RuntimeError from None
# RuntimeError