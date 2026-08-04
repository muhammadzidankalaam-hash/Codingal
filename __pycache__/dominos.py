print("Welcome to Dominos Service Chat")
print("- 1 Cheese Pizza")
print("- 2 Veg Pizza")
print()
choice = int (input("enter a number 1 or 2"))
print() 
if choice ==1:
    print(" step 2 pick your bread")
    print(" 1 = Garlic Bread ")
    print(" 2 = Cheese Bites ")
    print()
    Cheese = int(input("1 or 2"))
    print()
    if Cheese ==1 :
        print("you have picked Garlic Bread")
    else:
        print("you have picked a Cheese Bites")
elif choice == 2:
    print("pick your Veg Toppings")
    print("1 = Olives ")
    print("2 = Tomatoes")
    print()
    Veg =int(input("1 or 2"))
    print()
    if Veg==1:
        print("you have picked Olives")
else:
    print("you have picked Tomatoes")
print()
print()
print()
print("your Pizza is ready")
print()
name = input("What is your name? ")

print("I hope you liked the Program!", name)
print("the total cost with taxes is $15")
pick = input("Debit or Credit")
pick = input("visa, american express == paypal")
pick = input("would you like your order to be delivered or would you like to pick it up")
print()
input("thank you for ordering from dominos bye!")
    
