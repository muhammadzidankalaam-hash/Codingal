secret = 49
attempts = 0 

while attempts < 5:
    n = int(input("What is your guess? "))
    attempts +=1

    if n == secret:
        print("Hot")
        break
    elif n < secret:
        print("cold")
    else:
        print("warm")

if attempts == 5 and n != secret:
    print("You lost! The number was 49.")
        

        
