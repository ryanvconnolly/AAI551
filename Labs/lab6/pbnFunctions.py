# Author: Ryan Connolly
# Date: October 12, 2024
# Description: contains the functions for paintByNumbers.py

import os

def getFileName():
    """
    gets the file name from the user and checks if it exists
    """

    userChoice = input("Please input file you wish to have painted: ")
    while True:
        if os.path.exists(userChoice):
            break
        else:
            userChoice = input(f"{userChoice} does not exist! Please input file you wish to have painted:")

    return userChoice

def convertLine(line):
    """
    reads number from csv and converts it to sybmols for ascii art
    """

    line = line.strip()
    newLine = ""
    numbers = line.split(",")

    for number in numbers:
        if number == "1":
            newLine += " "
        elif number == "2":
            newLine += ","
        elif number == "3":
            newLine += "_"
        elif number == "4":
            newLine += "("
        elif number == "5":
            newLine += "O"
        elif number == "6":
            newLine += ")"
        elif number == "7":
            newLine += "-"
        elif number == "8":
            newLine += "\""

    return newLine

def processFile(filename):
    """
    reads input and writes are to output file
    """

    inputFile = open(filename, "r")
    outputFile = open("painting.txt", "w")
    for line in inputFile:
        newLine = convertLine(line)
        outputFile.write(newLine + "\n")
    inputFile.close()
    outputFile.close()