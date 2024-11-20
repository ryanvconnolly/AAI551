# Author: Ryan Connolly
# Date: September 21, 2024
# Description: This program finds the sum of all odd numbers between two randomly generated numbers.

import random

int1 = random.randint(0,10)
int2 = random.randint(11,20)
sum = 0
oddNum = 0

if (int1 % 2) == 0:
    int1 += 1
if (int2 % 2) == 0:
    int2 -= 1
    
for oddNum in range (int1, int2+1, 2):
    sum += oddNum
    
print(f" The first number was {int1}, the second was {int2}, and the sum is {sum}.")

