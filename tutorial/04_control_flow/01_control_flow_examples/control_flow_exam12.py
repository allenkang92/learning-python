

# match


# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"

    
# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"


# case 401 | 403 | 404:
#     return "Not allowed"


# point is an (x, y) tuple
# match point:
#     case (0, 0):
#         print("Origin")
#     case (0, y):
#         print(f"Y={y}")
#     case (x, 0):
#         print(f"X={x}")
#     case (x, y):
#         print(f"X={x}, Y={y}")
#     case _:
#         raise ValueError("Not a point")

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# def where_is(point):
#     match point:
#         case Point(x=0, y=0):
#             print("Origin")
#         case Point(x=0, y=y):
#             print(f"Y={y}")
#         case Point(x=x, y=0):
#             print(f"X={x}")
#         case Point():
#             print("Somewhere else")
#         case _:
#             print("Not a point")

# Point(1, var)
# Point(1, y=var)
# Point(x=1, y=var)
# Point(y=var, x=1)

# class Point:
#     __match_args__ = ('x', 'y')
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# match points:
#     case []:
#         print("No points")
#     case [Point(0, 0)]:
#         print("The origin")
#     case [Point(x, y)]:
#         print(f"Single point {x}, {y}")
#     case [Point(0, y1), Point(0, y2)]:
#         print(f"Two on the Y axis at {y1}, {y2}")
#     case _:
#         print("Something else")

# match point:
#     case Point(x, y) if x == y:
#         print(f"Y=X at {x}")
#     case Point(x, y):
#         print(f"Not on the diagonal")

# case (Point(x1, y1), Point(x2, y2) as p2): ...

# from enum import Enum
# class Color(Enum):
#     RED = 'red'
#     GREEN = 'green'
#     BLUE = 'blue'

# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")

