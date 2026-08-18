data = [10, 20, 30, 40, 50]

with open("numbers.bin", "wb") as file:
    file.write(bytes(data))

with open("numbers.bin", "rb") as file:
    content = file.read()

print("Binary Data:", content)