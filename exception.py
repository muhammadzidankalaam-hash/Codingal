try:
    number = int(input("Enter a Number"))
    print("The number entered is",number)
except ValueError as ex:
    print("except",ex)
