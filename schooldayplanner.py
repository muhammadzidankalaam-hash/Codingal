print("Smart School Day Planner")
print("Answer 3 quick questions and we will plan a day for you")
day = input("what day is it monday to to sunday").strip().lower()
weather = input("what is the weather sunny rainy or cloudy").strip().lower
homework = input("is your homework done yes or no").strip().lower
print()
print("your plan for the {day}")
print("-"*35)
if day in("saturday","sunday"):
    print("weekend enjoy your day time")
elif day==("monday"):
    print(" first day of the week")
elif day==("friday"):
    print("last day of school return library books")
elif day in ("tuesday","wednesday","thursday"):
    print(" regular school day stay focused ")
else :
    print("day not recognised ")


if weather=="sunny"and homework== "yes":
    print("after school you can head to the park")
if weather=="rainy"or weather=="cloudy":
    print("pack your umbrella because it might rain")
if not (homework=="yes"):
    print("not done yet first finish it and then go out")


if weather=="rainy "and not(homework=="yes"):
    print("stay in and finish your homework")
elif weather=="sunny "and homework=="yes"and not(day in("saturday","sunday")):
    print("all set for a great day at school")
else:
    print("take one step at a time")


print("plan completed have a wonderful day")


  
