# Author: Ryan Connolly
# Date: November 2, 2024
# Description: This module imports the Product module and creates instances of the Product class to calculate the total price and outputs product information.

import Product

def calcTotal(product):
    total = product.getQuantity()*product.getPx()
    product.setTotal(total)


def main():
    p1 = Product.Product()
    
    name = input("Please enter the name of the product you wish to order: ")
    quant = int(input("Please enter the number of items you wish to order: "))
    
    p1.setProduct(name)
    p1.setQuantity(quant)
    
    p1.setPx(9.99)
    
    calcTotal(p1)
    
    print(f"Order Summary: ")
    print(f"Name: {p1.getProduct()}")
    print(f"Quantity: {p1.getQuantity()}")
    print(f"Price: ${p1.getPx():.2f}")
    print(f"Total Price: ${p1.getTotal():.2f}")
    
if __name__  == "__main__":
    main()
    