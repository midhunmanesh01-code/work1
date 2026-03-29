def isright(a, b, c):
    # Sort the sides so the largest side becomes the hypotenuse
    sides = sorted([a, b, c])
    x, y, z = sides  # x and y are smaller, z is largest

    # Check Pythagorean theorem
    return x**2 + y**2 == z**2


# Main program
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if isright(a, b, c):
    print("It is a Right Triangle.")
else:
    print("It is NOT a Right Triangle.")
