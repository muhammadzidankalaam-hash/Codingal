# PART 1: Create a dictionary of student records
student_data = {
    "id1": {"name": "Sara", "class": "V", "subject": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject": "english, math, science"},
    "id3": {"name": "Sara", "class": "V", "subject": "english, math, science"},
    "id4": {"name": "Surya", "class": "V", "subject": "english, coding, math"}
}
 
print("Original Student Records:")
print(student_data)
 
# PART 2: Access values from the dictionary
print("")
print("Details of id1:")
print(student_data.get("id1", "Not Found"))
 
print("")
print("Details of id5:")
print(student_data.get("id5", "Not Found"))
 
# PART 3: Add a new student record
student_data["id5"] = {
    "name": "Anaya",
    "class": "V",
    "subject": "english, art, science"
}
 
print("")
print("After adding id5:")
print(student_data)
 
# PART 4: Update an existing student record
student_data["id2"]["subject"] = "english, math, coding"
 
print("")
print("After updating id2 subject:")
print(student_data["id2"])
 
# PART 5: Remove duplicate student records
cleaned_data = {}
seen_records = []
 
for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject"])
 
    if unique_key not in seen_records:
        seen_records.append(unique_key)
        cleaned_data[student_id] = details
 
student_data = cleaned_data
 
print("")
print("After removing duplicate records:")
print(student_data)
 
# PART 6: Remove one student record using pop()
removed_student = student_data.pop("id4", "Student not found")
 
print("")
print("Removed student:")
print(removed_student)
 
# PART 7: Check the dictionary's length
print("")
print("Total student records left:", len(student_data))
 
# PART 8: Iterate through the dictionary
print("")
print("===== FINAL STUDENT SUBJECT RECORDS =====")
 
for student_id, details in student_data.items():
    print(student_id, ":", details)
 
print("==========================================")