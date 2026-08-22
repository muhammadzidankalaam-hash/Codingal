# Grocery Billing Queue
 
print("=== Grocery Billing Queue ===\n")
 
low_price_items = 0
medium_price_items = 0
high_price_items = 0
 
customers_served = 0
total_sales = 0
 
billing = True
 
while billing:                              # outer while -- one customer per loop
    name = input("Enter customer name: ")
    item_count = int(input(f"Hello {name}! How many items are you buying? "))
 
    if item_count <= 0:
        print("Invalid item count. Please enter a positive number.\n")
        continue
 
    print(f"\nBilling items for {name}:")
    customer_total = 0
    item_number = 1
 
    while item_number <= item_count:        # inner while -- one item per loop
        item_name = input("Enter item name: ")
        price = int(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))
 
        if price <= 0 or quantity <= 0:
            print("Invalid price or quantity. Please enter again.\n")
            continue
 
        item_total = price * quantity
        print(f"  {item_name}: {quantity} x {price} = {item_total}")
 
        customer_total += item_total
 
        if price < 50:
            low_price_items += quantity
        elif price <= 100:
            medium_price_items += quantity
        else:
            high_price_items += quantity
 
        item_number += 1
 
    customers_served += 1
    total_sales += customer_total
 
    print(f"\nTotal bill for {name}: {customer_total}")
    print("Billing complete!\n")
 
    again = input("Next customer? (yes/no): ").strip().lower()
 
    if again != "yes":
        billing = False
 
 
print("\n=== Grocery Category Report ===")
 
for slot in range(1, 4):                    # outer for -- one price category per loop
    if slot == 1:
        label, total = "Low price items", low_price_items
    elif slot == 2:
        label, total = "Medium price items", medium_price_items
    else:
        label, total = "High price items", high_price_items
 
    if total > 0:
        print(f"  {label}: {total} ", end="")
 
        for item in range(total):           # inner for -- one symbol per item
            print("*", end="")
 
        print()
 
print(f"\nCustomers served : {customers_served}")
print(f"Total sales      : {total_sales}")
print("Grocery billing closed. Goodbye!")
