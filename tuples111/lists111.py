# Create an empty list
empty_list = []
print(empty_list)
 
# PART 1: Create a list of student marks
marks = [85, 72, 90, 66, 78]
print("Student Marks:", marks)
 
# PART 2: Use * operator to repeat a sample marks list
sample_marks = [10, 20, 30] * 2
print("Repeated Sample Marks:", sample_marks)
 
# PART 3: Find the length of the marks list
print("Number of marks:", len(marks))
 
# PART 4: Access items using indexing
print("First mark:", marks[0])
print("Last mark:", marks[-1])
 
# PART 5: Access a range using slicing
first_three_marks = marks[0:3]
print("First three marks:", first_three_marks)
 
# PART 6: Reverse the marks list using slicing
reversed_marks = marks[::-1]
print("Reversed Marks:", reversed_marks)
 
# PART 7: Function to find marks that start and end with same digit
def match_marks(mark_list):
    count = 0
    matched_marks = []
 
    for mark in mark_list:
        mark_text = str(mark)
 
        if len(mark_text) > 1 and mark_text[0] == mark_text[-1]:
            count += 1
            matched_marks.append(mark)
 
    print("Marks with first and last digit same:", matched_marks)
    return count
 
same_digit_count = match_marks([88, 72, 99, 65, 77])
print("Number of matching marks:", same_digit_count)
 
# PART 8: Iterate through the list to find sum and average
total = 0
 
for mark in marks:
    total += mark
 
average = total / len(marks)
 
print("Sum of marks:", total)
print("Average marks:", average)
 
# PART 9: Sort the list to find smallest and largest marks
marks.sort()
 
print("Smallest mark is:", marks[0])
print("Largest mark is:", marks[-1])
 
# PART 10: Print the final student marks summary
print("")
print("===== STUDENT MARKS LIST ANALYZER =====")
print("Sorted Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Lowest Mark:", marks[0])
print("Highest Mark:", marks[-1])
print("=======================================")
