print("==============================================")
print("Welcome to custom ride")
print("==============================================")
print()
print("which vehicle would you like to pick")
print("- 1 Bike")
print("- 2 Car")
print()
choice = int (input("Enter a number 1 or 2"))
print()
if choice ==1:
    print(" step 2 pick your bike type")
    print(" 1 = Scooty")
    print(" 2 = Mountain Bike")
    print()
    bike =int(input("1 or 2"))
    print()
    if bike==1 :
        print("you have picked the scooty")
    else:
        print("you have picked a mountain bike")
elif choice == 2:
    print("pick your car type")
    print("1 = Sedan ")
    print("2 = SUV")
    print()
    car =int(input("1 or 2"))
    print()
    if car==1:
        print("you have picked a sedan")
    else: 
        print("you have picked the SUV")
else:
    print("it is not a valid choice")
    print()
print("your custom ride is ready")


