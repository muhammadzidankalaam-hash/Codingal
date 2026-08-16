print("=== ATM Cash Dispenser ===/n")
total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0 
customer_served = 0
total_dispensed = 0
serving= True 
while serving:
    name = input("enter your name")
    amount = int(input(f"Hello {name}! enter a withdrawal amount:"))
    if amount <= 0:
        print("invalid amount please enter a valid amount")
        continue
    print(f"\nDispensing {amount} units for {name}:")
    remaining = amount
    idx = 1
    while idx <= 6:
        if idx == 1: value = 100
        elif idx == 2: value = 50
        elif idx == 3: value = 20
        elif idx == 4: value = 10
        elif idx == 5: value = 5
        else: value = 1
        count = remaining // value 
        if count > 0
        



