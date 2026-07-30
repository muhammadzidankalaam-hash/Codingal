print("Welcome to Car Service")
print("- 1 BMW")
print("- 2 Porsche")
print()
choice = int (input("enter a number 1 or 2"))
print() 
if choice ==1:
    print(" step 2 pick your BMW model")
    print(" 1 = BMW3SERIES")
    print(" 2 = BMWM4COMPETITION")
    print()
    BMW = int(input("1 or 2"))
    print()
    if BMW==1 :
        print("you have picked BMW3SERIES")
    else:
        print("you have picked a BMWM4COMPETITION")
elif choice == 2:
    print("pick your porsche model")
    print("1 = Panamera ")
    print("2 = Taycan")
    print()
    porsche =int(input("1 or 2"))
    print()
    if porsche==1:
        print("you have picked Panamera")
else:
    print("you have picked Taycan")
print()
print()
print()
print("your vehicle is ready")
print()
