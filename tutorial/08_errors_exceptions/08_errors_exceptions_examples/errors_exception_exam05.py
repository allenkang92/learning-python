


import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())

except OSError as err:
    print("OS error:", err)

except ValueError:
    print("Could not conver data to an integer.")

except Exception as err:
    print(f"Unexpected {err = }, {type(err) = }")
    raise
# OS error: [Errno 2] No such file or directory: 'myfile.txt'