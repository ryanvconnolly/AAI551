# Author: Ryan Connolly
# Date: November 2, 2024
# Description: This module is an updated version of the Product class that stores a product's id number.

class SmartProduct:
    def __init__(self, id, name, quantity, px):
        self.__product = name
        self.__quantity = quantity
        self.__px = px
        self.__total = px*quantity
        self.__id = id
    
    def getProduct(self):
        return self.__product
    
    def setProduct(self, name):
        self.__product = name
    
    def getQuantity(self):
        return self.__quantity
    
    def setQuantity(self, quant):
        self.__quantity = quant
    
    def getPx(self):
        return self.__px
    
    def setPx(self, px):
        self.__px = px
    
    def getTotal(self):
        return self.__total
    
    def setTotal(self, total):
        self.__total = total
    
    def getID(self):
        return self.__id 
    
    def setID(self, id):
        self.__id = id