def greates_Num(a , b, c):
    if(a > b and a > c):
        print(f"{a} Is the greatest number")
    elif(b > a and b > c):
        print(f"{b} Is the greatest number")
    else:
        print(f"{c} Is the greatest number")
    print("")

greates_Num(4, 23 ,42)
greates_Num(5, 2332, 412)
greates_Num(89, 29, 68)


# OR you can take user input and also do the same thing.

def greates_Num():
    a = int(input("Enter 1st number : "))
    b = int(input("Enter 2nd number : "))
    c = int(input("Enter 3rd number : "))

    if(a > b and a > c):
        print(f"{a} Is the greatest number")
    elif(b > a and b > c):
        print(f"{b} Is the greatest number")
    else:
        print(f"{c} Is the greatest number")


greates_Num()



"""
OUTPUT : 

42 Is the greatest number

2332 Is the greatest number

89 Is the greatest number

Enter 1st number : 365
Enter 2nd number : 154
Enter 3rd number : 452
452 Is the greatest number

"""