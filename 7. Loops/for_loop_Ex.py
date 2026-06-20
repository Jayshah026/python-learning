print("Printing values from 1 to 5") 

for i in range(1, 6):                     # Here value will print normally from 1 to 5
    print(i)


print("Printing values from 0 to 5") 

for i in range(6):                        # Here we only gave end value and will print value accordingly with including 0
    print(i)


print("Printing Values with the help of step size") 

for i in range(0, 50, 5):                 # Here we have starting value = 0, ending value = 50 and step size = 5
    print(i)




"""
OUTPUT : 

Printing values from 1 to 5
1
2
3
4
5
Printing values from 0 to 5
0
1
2
3
4
5
Printing Values with the help of step size
0
5
10
15
20
25
30
35
40
45
"""