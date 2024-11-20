# Author: Ryan Connolly
# October 5, 2024
# Description: This program designates space and funding to 5 pieces of lab equipment at a time and allows the user to add equipment up to that max, remove equipment owned by the lab, and display what is currently owned. 

labEquip = []

menu = "Manager Menu: \n 1. Add equipment \n 2. Remove Equipment \n 3. Display Current Equipment \n 4. Leave the Laboratory Manager\n"
print(menu)
choice = input("Please enter the digit of the task you would like to complete: ")


while choice != "4":
    if choice == "1":
        if len(labEquip) < 5:
            add = input("What would you like to add to the lab: ")
            labEquip.append(add)
            print(f"{add} has been added to the lab.\n")
            
        else:
            print("The lab does not have enough room. Please remove an item or exit Lab Manager.\n")
            
    elif choice == "2":
        remove = input("What would you like to remove: ")
        
        if remove in labEquip:
            labEquip.remove(remove)
            print(f"{remove} has been removed from the lab.\n")
        else:
            print(f"{remove} is not in the lab. Please try again.\n")
    
    elif choice == "3":
        if labEquip:
            print("The current inventory of the lab is: ")
            for i in range(len(labEquip)):
                print(labEquip[i], end=", ")
            print("\n")
        else:
            print("The lab is currently empty.\n")
        
    else: 
        print(f"{choice} is an invalid option. Please try again.\n")
    
    print(menu)
    choice = input("Please enter the digit of the task you would like to complete: ")

print("Thanks for your contribution to the lab. Have a nice day!")