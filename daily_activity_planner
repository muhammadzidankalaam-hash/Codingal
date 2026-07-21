# PART 1: Ask for today's temperature
temperature = int(input("Enter today's temperature in Celsius: "))
 
# PART 2: Decide between outdoor and indoor activity
if temperature < 20:
    activity = "indoor reading"
    print("It is cool today.")
    print("Do", activity)
else:
    activity = "outdoor play"
    print("It is warm today.")
    print("Do", activity)
 
# PART 3: Ask whether it is raining
is_raining = input("Is it raining today? (yes/no): ")
 
# PART 4: Add a rain reminder only if it is raining
if is_raining == "yes":
    print("Choose an indoor activity or carry an umbrella!")
 
# PART 5: Ask for the homework time
homework_time = int(input("Enter homework time in minutes: "))
 
# PART 6: Decide whether study break is needed
if homework_time > 60:
    needs_break = "yes"
    print("You have a long homework session today.")
    print("Take a short break before your", activity)
else:
    needs_break = "no"
    print("Homework time is short today.")
    print("No long break needed before your", activity)
 
# PART 7: Ask whether there is free time
has_free_time = input("Do you have free time today? (yes/no): ")
 
# PART 8: Decide between hobby time and planning time
if has_free_time == "yes":
    final_task = "hobby time"
    print("You have free time today.")
    print("Enjoy your", final_task)
else:
    final_task = "planning time"
    print("You do not have much free time today.")
    print("Use some time for", final_task)
 
# PART 9: This message always prints, no matter what was chosen above
print("")
print("Daily activity check complete!")
 
# PART 10: Print the final activity summary
print("===== DAILY ACTIVITY PLANNER =====")
print("Temperature:", temperature)
print("Activity Chosen:", activity)
print("Raining:", is_raining)
print("Study Break Needed:", needs_break)
print("Final Task:", final_task)
print("==================================")
