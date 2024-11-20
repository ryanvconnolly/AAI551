# Author: Ryan Connolly
# Date: September 21, 2024
# Description: This program will play a position guessing game with the user.

guesses = 3
x = 4
y = 8

while guesses > 0:
    print(f"You have {guesses} remaining.")
    xGuess = int(input("Where do you think the x-coordinate is (positions 1-10)?"))
    yGuess = int(input("Where do you think the y-coordinate is (position 1-10)?"))
    
    if xGuess not in range(11) or y not in range(11):
        print(f"Guess invalid.")
        guesses -= 1
    else:
        if xGuess == x and yGuess == y:
            print("You got it! Nice job.")
            break
        
        if xGuess != x or yGuess != y:
            if xGuess < x:
                print("The particle's x position is greater than your guess.")
            elif xGuess > x:
                print("The particle's x position is less than your guess.")
            if yGuess < y:
                print("The particle's y position is greater than your guess.")
            elif yGuess > y:
                print("The particle's y position is less than your guess.")
            guesses -= 1
            continue
        
if guesses == 0:
    print(f"You ran out of guesses :(. ({x}, {y}) was the particle's position.")
2