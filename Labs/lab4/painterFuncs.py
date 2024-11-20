# Author: Ryan Connolly
# Date: September 28, 2024
# Description: This program defines all of the functions used in the painterMain module.

def intro():
    '''
    Returns an integer representing the user's choice of art and a string representing the desired border.
    '''
    print("Welcome to the painting printer!\n\tThere are many options:\n\t1. The Sailing Ship\n\t2. The Sleeping Cat\n\t3. Fish\n\t4. Owl")
    paintingChoice = int(input("Please select a painting to print: "))
    borderChoice = input("What border would you like around your painting: ")
    return paintingChoice, borderChoice

def printHeaderFooter(borderChoice, size):
    '''
    Takes in a border and size and outputs the border size number of times on the same line. 
    '''
    print(borderChoice * size)

def sleepingCat(borderChoice):
    '''
    Takes in a border as a parameter 
    o Stores the image of the cat in one or more variables
    o Calls the printHeaderFooter() function and provides it the border and an appropriate size to completely cover the top of the painting
    o Outputs each line of the ASCII art with the border symbol before and after the line.
    o Calls the printHeaderFooter() function and provides it the border and an appropriate size to completely cover the bottom of the painting
    '''
    a = "      |\\      _,,,---,,_      "
    b = " ZZZzz /,`.-'`'    -.  ;-;;,_ "
    c = "     |,4-  ) )-,_. ,\\ (  `'-' "
    d = "    '---''(_/--'  `-'\\_)      "
    printHeaderFooter(borderChoice, len(a) + 2)
    print(borderChoice + a + borderChoice + '\n' + borderChoice + b + borderChoice + '\n' + borderChoice + c + borderChoice + '\n' + borderChoice + d + borderChoice)
    printHeaderFooter(borderChoice, len(a) + 2)

def sailingShip(borderChoice):
    '''
    Takes in a border as a parameter 
    o Stores the image of the ship in one or more variables
    o Calls the printHeaderFooter() function and provides it the border and an appropriate size to completely cover the top of the painting
    o Outputs each line of the ASCII art with the border symbol before and after the line.
    o Calls the printHeaderFooter() function and provides it the border and an appropriate size to completely cover the bottom of the painting
    '''
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
    '''
    Takes in a border as a parameter 
    o Stores the image of the fish in one or more variables
    o Calls the printHeaderFooter() function and provides it the border and an appropriate size to completely cover the top of the painting
    o Outputs each line of the ASCII art with the border symbol before and after the line.
    o Calls the printHeaderFooter() function and provides it the border and an appropriate size to completely cover the bottom of the painting
    '''
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
    '''
    Takes in a border as a parameter 
    o Stores the image of the owl in one or more variables
    o Calls the printHeaderFooter() function and provides it the border and an appropriate size to completely cover the top of the painting
    o Outputs each line of the ASCII art with the border symbol before and after the line.
    o Calls the printHeaderFooter() function and provides it the border and an appropriate size to completely cover the bottom of the painting
    '''
    a = "  /\\ /\\  "
    b = " ((ovo)) "
    c = " ():::() "
    d = "   VVV   "

    printHeaderFooter(borderChoice, len(a) + 2)
    print(borderChoice + a + borderChoice + '\n' + borderChoice + b + borderChoice + '\n' + borderChoice + c + borderChoice + '\n' + borderChoice + d + borderChoice)
    printHeaderFooter(borderChoice, len(a) + 2)

def blank(borderChoice):
    ''' 
    Takes in a border as a parameter, returns nothing, and
    o Calls the printHeaderFooter() function and provides it the border and an appropriate size to completely cover the top of the painting
    o Outputs five lines of five spaces with the border in front of and after each line. This represents a blank canvas
    o Calls the printHeaderFooter() function and provides it the border and an appropriate size to completely cover the bottom of the painting
    '''
    printHeaderFooter(borderChoice, 10)
    print(borderChoice + "        " + borderChoice)
    print(borderChoice + "        " + borderChoice)
    print(borderChoice + "        " + borderChoice)
    print(borderChoice + "        " + borderChoice)
    printHeaderFooter(borderChoice, 10)