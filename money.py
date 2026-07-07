amount=int(input("enter the amount of money:"))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("number of 100 rupees note:",note1)
print("number of 50 rupees note:",note2)
print("number of 10 rupees note:",note3)