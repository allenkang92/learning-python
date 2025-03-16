


from dataclasses import dataclass

@dataclass
class Employee:
    name : str
    dept : str
    salary : int

john = Employee('john', 'computer lab', 1000)

print(john.dept)
# computer lab

print(john.salary)
# 1000
