# Author: Ryan Connolly
# Date: October 12, 2024
# Description: This program reads from the numbers file, compute the average of the integers in the file and then print the average. 

num = open("C:\\Users\\ryanv\\OneDrive - stevens.edu\\AAI 551\\AAI 551 Coding\\Labs\\lab6\\numbers.txt","r")
def main():

    sum = 0
    counter = 0
    
    for line in num:
        print(line.strip())
        sum+= int(line.strip())
        counter+=1
        
    avg = sum/counter
    print(f"The average of the numbers in the file is {avg}")
    
    num.close()
    
main()