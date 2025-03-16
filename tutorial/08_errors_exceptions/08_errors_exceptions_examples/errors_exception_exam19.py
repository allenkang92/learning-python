

# ```python
# >>> def f():
# ...     raise ExceptionGroup(
# ...         "group1",
# ...         [
# ...             OSError(1),
# ...             SystemError(2),
# ...             ExceptionGroup(
# ...                 "group2",
# ...                 [
# ...                     OSError(3),
# ...                     RecursionError(4)
# ...                 ]
# ...             )
# ...         ]
# ...     )
# ...
# >>> try:
# ...     f()
# ... except* OSError as e:
# ...     print("There were OSErrors")
# ... except* SystemError as e:
# ...     print("There were SystemErrors")
# ...
# There were OSErrors
# There were SystemErrors
#   + Exception Group Traceback (most recent call last):
#   |   File "<stdin>", line 2, in <module>
#   |     f()
#   |     ~^^
#   |   File "<stdin>", line 2, in f
#   |     raise ExceptionGroup(
#   |     ...<12 lines>...
#   |     )
#   | ExceptionGroup: group1 (1 sub-exception)
#   +-+---------------- 1 ----------------
#     | ExceptionGroup: group2 (1 sub-exception)
#     +-+---------------- 1 ----------------
#       | RecursionError: 4
#       +------------------------------------
# ```