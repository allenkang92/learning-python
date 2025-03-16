


# def f():
#     excs = [OSError('error 1', SystemError('error 2'))]
#     raise ExceptionGroup('there were problems', excs)

# f()

# ```python
# >>> def f():
# ...     excs = [OSError('error 1'), SystemError('error 2')]
# ...     raise ExceptionGroup('there were problems', excs)
# ...
# >>> f()
#   + Exception Group Traceback (most recent call last):
#   |   File "<stdin>", line 1, in <module>
#   |     f()
#   |     ~^^
#   |   File "<stdin>", line 3, in f
#   |     raise ExceptionGroup('there were problems', excs)
#   | ExceptionGroup: there were problems (2 sub-exceptions)
#   +-+---------------- 1 ----------------
#     | OSError: error 1
#     +---------------- 2 ----------------
#     | SystemError: error 2
#     +------------------------------------
# >>> try:
# ...     f()
# ... except Exception as e:
# ...     print(f'caught {type(e)}: e')
# ...
# caught <class 'ExceptionGroup'>: e
# ```
