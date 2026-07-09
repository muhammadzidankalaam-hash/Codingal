cost = float(input("enter the actual cost"))
sold = float(input("enter the sold cost"))
if cost < sold:
    amount = sold - cost
    print("total profit={0}".format(amount))
else:
    print("no profit")
