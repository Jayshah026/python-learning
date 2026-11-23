# writing sentence with fstring

name = input("Enter your name : ")
age = int(input("Enter your age : "))

print(f"My name is {name} and the age is {age}")


# writing sentence without fstring total 2 methods

# Method 1

print("My name is", name, "and my age is", age)

# Method 2 

print("My name is " + name + " and my age is " + str(age))