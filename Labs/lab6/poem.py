# Author: Ryan Connolly
# Date: October 12, 2024
# Description: This program reads the poem in Snowball,txt, stores the info, and then writes a short summary in a new file.

import os
def main():
    title = ""
    author = ""
    lines = []
    fileName = ""

    fileName = input("Please input the name of the poem you wish summarized:")

    while True:
        if os.path.exists(fileName):       #enter full filepath
            break
        else:
            fileName = input(f"{fileName} does not exist! Please input the name of a different poem you want to be summarized:")

    file = open(fileName, "r")
    title = file.readline().strip()
    author = file.readline().strip()

    for line in file:
        lines.append(line.strip())

    file.close()

    while True:
        if os.path.exists("output.txt"):
            break
        else:
            outputFile = open("C:\\Users\\ryanv\\OneDrive - stevens.edu\\AAI 551\\AAI 551 Coding\\Labs\\lab6\\output.txt", "w")
            lineSum = len(lines)

            outputFile.write(f"The name of the poem is {title}\n")
            outputFile.write(f"The author of the poem is {author}\n")
            outputFile.write(f"The number of lines in the poem is {lineSum}\n")
            outputFile.write(f"A preview of the poem is:\n")

            for line in lines[:3]:
                outputFile.write(line + "\n")

            outputFile.close()

main()