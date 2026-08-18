student = {
    "name": "Jay",
    "age": 20,
    "course": "Computer Engineering",
    "marks": 85
}

print("Student:", student)
print("Name:", student["name"])
print("Age:", student["age"])

student["marks"] = 90
print("Updated Marks:", student["marks"])

student["city"] = "Ahmedabad"
print("Updated Dictionary:", student)