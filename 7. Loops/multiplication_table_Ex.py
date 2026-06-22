n = int(input("Enter a number for multiplication table : "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")



n = int(input("Enter a number for multiplication table for reverse order : "))

for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")




"""
OUTPUT : 

Enter a number for multiplication table : 10
10 x 1 = 10
10 x 2 = 20
10 x 3 = 30
10 x 4 = 40
10 x 5 = 50
10 x 6 = 60
10 x 7 = 70
10 x 8 = 80
10 x 9 = 90
10 x 10 = 100
Enter a number for multiplication table for reverse order : 10
10 x 10 = 100
10 x 9 = 90
10 x 8 = 80
10 x 7 = 70
10 x 6 = 60
10 x 5 = 50
10 x 4 = 40
10 x 3 = 30
10 x 2 = 20
10 x 1 = 10

"""