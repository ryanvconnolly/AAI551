# Author: Ryan Connolly
# Date: September 21, 2024
# Description: This program converts digits into Roman numerals.

num = int(input("Please enter a digit (1-9) to convert to a Roman numeral: "))

if num == 1:
    print("Numeral: \u2160")
elif num == 2:
    print("Numeral: \u2161")
elif num == 3:
    print("Numeral: \u2162")
elif num == 4:
    print("Numeral: \u2163")
elif num == 5:
    print("Numeral: \u2164")
elif num == 6:
    print("Numeral: \u2165")
elif num == 7:
    print("Numeral: \u2166")
elif num == 8:
    print("Numeral: \u2167")
elif num == 9:
    print("Numeral: \u2168")
else:
    print("Digit invalid. Please try again.")