"""

To print this pattern : 

  *
 ***
*****

"""

n = int(input("Enter a number : "))

for i in range(1, n + 1):
    print(" " * (n - i), end = "")
    print("*" * (2 * i - 1), end = "")
    print("")



# OR METHOD

# n = int(input("Enter a number : "))

# for i in range(0, n):
#     print(" " * (n - i + 1), end = "")
#     print("*" * (2 * (i + 1) - 1), end = "")
#     print("")