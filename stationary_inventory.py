items = ["pencil","eraser","notebook","sharpener","glue"]
stock_counts = [15,65,0,54,23]
inventory ={item: count for item, count in zip(items, stock_counts)}
print("Full inventory:",inventory)
in_stock_items = [item for item in items if inventory[item] > 0]
print("Items In Stock:",in_stock_items)
chosen_item = input("Which item do you want to buy?")
if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(chosen_item, "is out of stock! Stopping the checker.")
    exit()
prices = [10,5,40,15,20]
markup = int(input("Enter the markup amount to add to every price:"))
marked_up_prices = list(map(lambda p: p + markup,prices))
print("Marked Up Prices:",marked_up_prices) 