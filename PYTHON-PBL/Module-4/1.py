file = open("sample.txt", "w")
file.write("Python File Handling")
file.close()

file = open("sample.txt", "r")
content = file.read()
file.close()

print("File Content:", content)