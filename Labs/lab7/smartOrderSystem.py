# Author: Ryan Connolly
# Date: November 2, 2024
# Description: This module implements the SmartProduct class and creates instances of the Product class to calculate the total price and outputs product information.

import SmartProduct as sp 

def calcTotal(products):
    total = 0.0
    for p in products:
        total += p.getTotal()
    return total

def main():
    products = []
    
    types = int(input("\nHow many different products do you want? : "))
    
    for i in range(types):
        print(f"\nEnter the name and quantity of product {i+1}.")
        name = input("Product Name: ")
        quant = int(input("Quantity: "))
        
        id = i+1
        price = 9.99
        
        prod = sp.SmartProduct(id, name, quant, price)
        prod.setTotal(quant*price)
        
        products.append(prod)
        
    final = calcTotal(products)

    print(f"\nOrder Summary: ")
    
    for prod in products:
        print(f"\nProduct ID: {prod.getID()}")
        print(f"Name: {prod.getProduct()}")
        print(f"Quantity: {prod.getQuantity()}")
        print(f"Price: ${prod.getPx():.2f}")
        print(f"Total Price: ${prod.getTotal():.2f}")
    
    print(f"Total for All Products: ${final:.2f}")
    
if __name__  == "__main__":
    main()
    
