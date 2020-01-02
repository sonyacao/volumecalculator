from math import pi

def volume_calc(shape):

    if shape == "c":
        a = int(input("Please enter side length of the cube"))
        volume = round(a**3,3)
        print("The volume of a cube with side length", a, "is: ", volume)
    elif shape == "p":
        b = int(input("Please enter the base of the pyramid"))
        h = int(input("Please enter the height of the pyramid"))
        volume = round(1/3 * b**2 * h, 3)
        print("The volume of a pyramid with base length", b, "and height ", h, "is: ", volume)
    elif shape == "e":
        r1 = int(input("Please enter the first radius"))
        r2 = int(input("Please enter the second radius"))
        r3 = int(input("Please enter the third radius"))
        volume = round(4/3 * pi * r1 * r2 * r3,3)
        print("The volume of a ellipsoid with radius", r1, "radius ", r2, "and radius ", r3, "is: ", volume)

    return volume


