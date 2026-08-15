total_chores = 4

original_count = total_chores

print(f"You have {original_count} chores to finish today!\n")

# PART 2: Keep a counter for completed chores and the current chore number

completed_count = 0

chore_num = 1

# PART 3: Repeat while there are still chores left to check off

while chore_num <= total_chores:

# PART 4: Work out the current chore's name from its number

if chore_num == 1: next_chore = "Make your bed"

elif chore_num == 2: next_chore = "Feed the pet"

elif chore_num == 3: next_chore = "Take out the trash"

else: next_chore = "Wash the dishes"

answer = input(f"Have you finished: {next_chore}? (yes/no): ")

# PART 5: Only move on to the next chore once it is marked done

if answer == "yes":

completed_count += 1

chore_num += 1

print("Great job! Chore completed.")

else:

print("Okay, finish it and check again!")

# PART 6: Print how many chores remain after each check

print("Chores remaining:", total_chores - completed_count)

print()

# PART 7: This only prints once every chore is marked done

print("===== ALL CHORES COMPLETE! =====")

print("Great work finishing your entire checklist today!\n")
