# Author: Ryan Connolly
# Date: September 28, 2024
# Description: This program calculates and prints the total surface area of a square pyramid. 

import math

# function definitions
def calcBaseArea(side):
    return side ** 2

# add your function definition for calcSideArea here
def calcSideArea (base, height):
    return 2*base * math.sqrt(((base**2)/4) + height**2)

# add your function definition for prntSurfArea here
def prntSurfArea (base_a, side_a):
    surfA =  base_a + side_a
    print(f"Total surface area of the square pyramid is {surfA} square feet.")

def main():
    side = float(input("Enter the side length of the base of the square pyramid in feet: "))

    height = float(input("Enter the height of the square pyramid in feet: "))

    base_area = calcBaseArea(side)
    print(f"Base surface area of the square pyramid is {base_area} square feet.")

    # add your function to calculate the side area and assign
    side_area = calcSideArea(side, height)
    print(f"The total side surface area of the square pyramid is {side_area} square feet.")

    # add your function call to print the total surface area
    total = prntSurfArea(base_area, side_area)
    print(f"The total surface area of the square pyramid is {total} square feet.")


if __name__ == "__main__":
    main()