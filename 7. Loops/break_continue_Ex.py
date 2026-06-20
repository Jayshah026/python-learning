print("Using break statement")
for i in range(1,11):
    if(i == 6):
        break       # Here if i = 6 then the loop will stop at 6 and will print the values before it 
    print(i)

print("Using continue statement ")
for i in range(1, 11):
    if(i == 6):
        continue    # Here if i = 6 then the loop will skip that iteration and then again start printing values
    print(i)



"""
OUTPUT :

Using break statement
1
2
3
4
5
Using continue statement 
1
2
3
4
5
7
8
9
10
"""