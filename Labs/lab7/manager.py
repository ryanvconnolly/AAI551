# Author: Ryan Connolly
# Date: November 2, 2024
# Description: This module implements the Warehouse class so the user can update the inventory of the warehouse.

import Warehouse as w
def main():
    num = w.Warehouse(0)
    
    while True:
        print("\nWarehouse Inventory Manager Menu: ")
        print("1. Add items.")
        print("2. Remove items.")
        print("3. Output total.")
        print("4. Quit.")
    
        choice = int(input("\nWhat would you like to do today? (1-4):"))
    
        match choice:
            case 1:
                num.add()
            case 2:
                num.remove()
            case 3:
                print(f"\nTotal goods in Warehouse: {num.getTotal()}")
            case 4:
                print("\nHave a nice day.")
                break
            case default:
                print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()