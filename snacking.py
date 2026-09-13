# Snack Vending Machine

# PART 1: A function that works out change and sends it back with return
def calculate_change(paid, price):
    change = paid - price
    return change

# PART 2: Set the snack price and greet the customer
snack_price = 25
print("===== SNACK VENDING MACHINE =====")
print(f"This snack costs {snack_price} units.")
print("Accepted coins: 1, 5, 10, 25\n")

total_inserted = 0
coins_inserted = 0

# PART 3: Keep accepting coins until enough money is inserted
while True:
    coin = int(input("Insert a coin (1, 5, 10, or 25): "))

    # PART 4: Reject any coin that isn't a valid value
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin, try again!\n")
        continue

    # PART 5: Add the valid coin to the running total
    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far: {total_inserted}\n")

    # PART 6: Stop asking for coins once enough has been inserted
    if total_inserted >= snack_price:
        print("Enough money inserted!\n")
        break

# PART 7: Work out the change using the value returned by calculate_change
change_due = calculate_change(total_inserted, snack_price)

print("Dispensing your snack...")

# PART 8: Nothing extra to do when the change is exactly zero
if change_due == 0:
    pass
else:
    print(f"Here is your change: {change_due} units")

# PART 9: Print a short summary of the purchase
print("\n===== PURCHASE SUMMARY =====")
print("Snack Price:", snack_price)
print("Coins Inserted:", coins_inserted)
print("Total Paid:", total_inserted)
print("Change Given:", change_due)
print("=============================")
print("Thanks for your purchase!")
# End of program
