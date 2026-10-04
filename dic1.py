student = {
    "id1": {"name": "zidan", "class": "v" ,"subject": "science"},
    "id2": {"name": "Zara", "class": "v"  ,"subject": "science"},
    "id3": {"name": "zidan","class": "v" ,"subject": "science"},
    
}
result = {}
seen_keys = []
for student_id, details in student.items():
    unique_key = (details["name"], details["class"], details["subject"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details
for k,v in result.items(): 
    print(k, ":", v)

