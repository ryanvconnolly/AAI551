# Author: Ryan Connolly
# Date: September 28, 2024
# Description: This program implements the paintFuncs module and defines the main function. 

import painterFuncs

def main():
    paintingChoice, borderChoice = painterFuncs.intro()
    if paintingChoice == 1:
        painterFuncs.sailingShip(borderChoice)
    elif paintingChoice == 2:
        painterFuncs.sleepingCat(borderChoice)
    elif paintingChoice == 3:
        painterFuncs.fish(borderChoice)
    elif paintingChoice == 4:
        painterFuncs.owl(borderChoice)
    else:
        painterFuncs.blank(borderChoice)
        print("That painting is not in the library. Please try again.")
        exit(-1)

    print("Enjoy the art!")
main()