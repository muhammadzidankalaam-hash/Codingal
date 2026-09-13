def calculate(paid,price):
    change = paid - price
    return change 
snack_price = 25 
print("===== SNACK VENDING MACHINE =====")
print(f"This snack costs {snack_price} units. ")
print("Accepted coins: 1, 5, 10, 25")
total_inserted = 0
coins_inserted = 0
while True:
    coin = int(input("insert a coin (1, 5, 10, or 25): "))
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("invalid code, try again!\n")
        continue 
    total_inserted+= coin
    coins_inserted += 1
    print(f"Insered {coin}. Total so far: {total_inserted}\n")
    if total_inserted >= snack_price:
        print("Enough money inserted!|n")
        break
    change_due = calculate(total_inserted, snack_price)
    print("Dispensing your snack...")
    if change_due == 0:
        pass 
    else:
        print(f"Here is your change: {change_due} units")







    