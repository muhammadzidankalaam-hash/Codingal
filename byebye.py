valid = False
while not valid:
    try:
        n = int(input("Enter a number"))
        while n %2==0:

             print("bye")
        valid = True
    except ValueError:
        print("invalid")
        
