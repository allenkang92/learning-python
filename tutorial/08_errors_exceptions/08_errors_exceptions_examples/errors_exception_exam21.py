# ```python
# >>> try:
# ...     raise TypeError('bad type')
# ... except Exception as e:
# ...     e.add_note('Add some information')
# ...     e.add_note('Add some more information')
# ...     raise
# ...
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
#     raise TypeError('bad type')
# TypeError: bad type
# Add some information
# Add some more information
# ```