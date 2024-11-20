# Author: Ryan Connolly
# Date: November 2, 2024
# Description: This module stores information related to the goods in the warehouse.

class Warehouse:
    def __init__(self, initial = 0):
        self.__total = initial
    
    def add(self):
        add = int(input("\nHow many goods would you like to add to the warehouse? : "))
        self.__total += add
    
    def remove(self):
        sub = int(input("\nHow many goods would you like to remove to the warehouse? : "))
        if sub > self.__total:
            print("\nThere are not enough items in the warehouse to remove that many items. Please try again.")
        else:
            self.__total -= sub

    def getTotal(self):
        return self.__total