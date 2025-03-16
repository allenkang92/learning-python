

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
# Traceback (most recent call last):
# line 4, in <module>
#     raise NameError('HiThere')
# NameError: HiThere