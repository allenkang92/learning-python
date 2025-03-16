


def func():
    raise ConnectionError

try: 
    func()

except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
# Traceback (most recent call last):
#   File "/../../learning-python/practice-python/tutorial/08_errors_exceptions/08_errors_exceptions_examples/errors_exception_exam13.py", line 8, in <module>
#     func()
#   File "/../../learning-python/practice-python/tutorial/08_errors_exceptions/08_errors_exceptions_examples/errors_exception_exam13.py", line 5, in func
#     raise ConnectionError
# ConnectionError

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "/../../learning-python/practice-python/tutorial/08_errors_exceptions/08_errors_exceptions_examples/errors_exception_exam13.py", line 11, in <module>
#     raise RuntimeError('Failed to open database') from exc
# RuntimeError: Failed to open database