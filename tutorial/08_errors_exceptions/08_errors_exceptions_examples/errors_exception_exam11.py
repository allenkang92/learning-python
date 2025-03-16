

try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")
# line 4, in <module>
#     open("database.sqlite")
# FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "/../../learning-python/practice-python/tutorial/08_errors_exceptions/08_errors_exceptions_examples/errors_exception_exam11.py", line 6, in <module>
#     raise RuntimeError("unable to handle error")
# RuntimeError: unable to handle error