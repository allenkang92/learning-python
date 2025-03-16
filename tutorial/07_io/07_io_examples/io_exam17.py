

# f = open('./io_exam16.py', 'w', encoding = "utf-8")

with open('./io_exam16.py', 'w', encoding="utf-8") as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
print(f.closed)