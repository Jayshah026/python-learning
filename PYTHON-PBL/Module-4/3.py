import csv

data = [
    ["Name", "Age", "Marks"],
    ["Jay", 20, 85],
    ["Rahul", 21, 90],
    ["Amit", 20, 78]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)