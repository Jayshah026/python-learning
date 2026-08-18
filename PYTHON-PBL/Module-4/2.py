file = open("student.txt", "w")
file.write("Name: Jay\n")
file.write("Course: Computer Engineering\n")
file.write("Marks: 85\n")
file.close()

file = open("student.txt", "r")
content = file.read()
file.close()

print(content)