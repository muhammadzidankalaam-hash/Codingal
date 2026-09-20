import random 
playing = True 
number = str(random.randint(0,9))
print("I will generate a number 0 to 9 and you have to guess the number one digit at time.")
print("The game ends when you get 1 hero!")
while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("You win the game!")
        print("The number was",number)
        break
    else:
        print("Your guess isn't right try again")