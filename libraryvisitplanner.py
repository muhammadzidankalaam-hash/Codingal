# Library Visit Planner

print("=== Library Visit Planner ===")
print("Answer 3 quick questions and I will plan your library visit!\n")

day       = input("What day is it? (Monday to Sunday): ").strip().capitalize()
weather   = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
book_due  = input("Do you have a book to return? (yes / no): ").strip().lower()

print()
print(f"=== Your Library Plan for {day} ===")
print("-" * 35)

# Topic 1 -- if-elif-else: classify the day
if day in ("Saturday", "Sunday"):
    print("Day type    : Weekend - a good time for a relaxed library visit!")
elif day == "Monday":
    print("Day type    : Start of the week. Check your reading list.")
elif day == "Friday":
    print("Day type    : Last school day. Return books before the weekend.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type    : Regular school day. Plan a short library visit.")
else:
    print("Day type    : Day not recognised. Please check the spelling.")

# Topic 2 -- AND operator: sunny AND book due
if weather == "sunny" and book_due == "yes":
    print("Library tip : Great weather! Return your book and borrow a new one.")

# Topic 3 -- OR operator: rainy OR cloudy
if weather == "rainy" or weather == "cloudy":
    print("Weather tip : Carry an umbrella if you are going to the library.")

# Topic 4 -- NOT operator: book NOT due
if not (book_due == "yes"):
    print("Book status : No book return needed today. You can browse new books.")

# Topic 5 -- Combining AND + OR + NOT together
if weather == "rainy" and book_due == "yes":
    print("Best plan   : Visit the library carefully and return your book on time.")
elif weather == "sunny" and book_due == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan   : Stop by the library after school and return your book.")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan   : Perfect day for a longer reading session at the library!")
else:
    print("Best plan   : Check your schedule and plan a simple library visit.")

print()
print("Library plan complete! Happy reading!")
