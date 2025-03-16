

while True:
    try:
        x = int(input("plz enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")

