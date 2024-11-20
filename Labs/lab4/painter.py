# Author: Ryan Connolly
# Date: September 28, 2024
# Description: This program allows the user to choose from 4 options for was ASCII art painting they want to see. 

def intro():
    print("Welcome to the painting printer!\n\tThere are many options:\n\t1. The Sailing Ship\n\t2. The Sleeping Cat\n\t3. Fish\n\t4. Owl")
    paintingChoice = int(input("Please select a painting to print: "))
    borderChoice = input("What border would you like around your painting: ")
    return paintingChoice, borderChoice

def printHeaderFooter(borderChoice, size):
    print(borderChoice * size)

def sleepingCat(borderChoice):
    a = "      |\\      _,,,---,,_      "
    b = " ZZZzz /,`.-'`'    -.  ;-;;,_ "
    c = "     |,4-  ) )-,_. ,\\ (  `'-' "
    d = "    '---''(_/--'  `-'\\_)      "
    printHeaderFooter(borderChoice, len(a) + 2)
    print(borderChoice + a + borderChoice + '\n' + borderChoice + b + borderChoice + '\n' + borderChoice + c + borderChoice + '\n' + borderChoice + d + borderChoice)
    printHeaderFooter(borderChoice, len(a) + 2)

def sailingShip(borderChoice):
    a = "       |    |    |            "
    b = "      )_)  )_)  )_)           "
    c = "     )___))___))___)\\         "
    d = "    )____)____)_____)\\\\       "
    e = "  _____|____|____|____\\\\\\__   "
    f = "  \\    Satisfaction   /       "
    g = " ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ "
    printHeaderFooter(borderChoice, len(a) + 2)
    print(borderChoice + a + borderChoice + '\n' + borderChoice + b + borderChoice + '\n' + borderChoice + c + borderChoice + '\n' + borderChoice + d + borderChoice + '\n' + borderChoice + e + borderChoice + '\n' + borderChoice + f + borderChoice + '\n' + borderChoice + g + borderChoice)
    printHeaderFooter(borderChoice, len(a) + 2)

def fish(borderChoice):
    a = "       /`·.¸         "
    b = "      /¸...¸`:·      "
    c = "  ¸.·´  ¸   `·.¸.·´) "
    d = " : © ):´;      ¸  {  "
    e = "  `·.¸ `·  ¸.·´\\`·¸) "
    f = "      `\\\\´´\\¸.·´     "
    printHeaderFooter(borderChoice, len(a) + 2)
    print(borderChoice + a + borderChoice + '\n' + borderChoice + b + borderChoice + '\n' + borderChoice + c + borderChoice + '\n' + borderChoice + d + borderChoice + '\n' + borderChoice + e + borderChoice + '\n' + borderChoice + f + borderChoice)
    printHeaderFooter(borderChoice, len(a) + 2)

def owl(borderChoice):
    a = "  /\\ /\\  "
    b = " ((ovo)) "
    c = " ():::() "
    d = "   VVV   "

    printHeaderFooter(borderChoice, len(a) + 2)
    print(borderChoice + a + borderChoice + '\n' + borderChoice + b + borderChoice + '\n' + borderChoice + c + borderChoice + '\n' + borderChoice + d + borderChoice)
    printHeaderFooter(borderChoice, len(a) + 2)

def blank(borderChoice):
    printHeaderFooter(borderChoice, 10)
    print(borderChoice + "        " + borderChoice)
    print(borderChoice + "        " + borderChoice)
    print(borderChoice + "        " + borderChoice)
    print(borderChoice + "        " + borderChoice)
    printHeaderFooter(borderChoice, 10)

def main():
    paintingChoice, borderChoice = intro()
    if paintingChoice == 1:
        sailingShip(borderChoice)
    elif paintingChoice == 2:
        sleepingCat(borderChoice)
    elif paintingChoice == 3:
        fish(borderChoice)
    elif paintingChoice == 4:
        owl(borderChoice)
    else:
        blank(borderChoice)
        print("That painting is not in the library. Please try again.")
        exit(-1)

    print("Enjoy the art!")

main()
