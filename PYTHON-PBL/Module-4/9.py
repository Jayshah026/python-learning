students = [
    {"id": 1, "name": "Jay", "age": 20, "marks": 85},
    {"id": 2, "name": "Rahul", "age": 21, "marks": 90}
]

print("Original Records:")
for student in students:
    print(student)

# UPDATE
students[0]["marks"] = 95

print("\nAfter UPDATE:")
for student in students:
    print(student)

# DELETE
students.pop(1)

print("\nAfter DELETE:")
for student in students:
    print(student)