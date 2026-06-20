n = int(input("Enter a number : "))

for i in range(2, n):
    if(n % i == 0):
        print("Number is not a prime number")
        break
else:
    print("Number is a prime number")





"""
If a number is divisable by 1 and the number itself then it's called prime number

Ex : 55 -> Not a prime number
     79 -> Is a prime number
"""