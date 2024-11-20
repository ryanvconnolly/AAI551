# Author: Ryan Connolly
# Date: October 12, 2024
# Description: calls the file name function and the process function. informs the user that the image is located in the painting.txt file

import pbnFunctions

def main():
    current = pbnFunctions.getFileName()
    pbnFunctions.processFile(current)
    
    print("The image can be opened with the painting.txt file :)")
    
main()