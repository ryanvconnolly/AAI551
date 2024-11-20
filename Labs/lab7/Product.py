# Author: Ryan Connolly
# Date: November 2, 2024
# Description: This module creates the class Product, with a constructor that defines the product, quantity, price, and total price, with getter and setter methods for each. 


class Product:
    def __init__(self):
        self.__product = ""
        self.__quantity = 0
        self.__px = 0.0
        self.__total = 0.0
    
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
        

