Code : 

a = int(input("Enter the subject marks : "))

if(a < 0 or a > 100):
    print("Enter valid marks")

elif(a > 80 and a <= 100):
    print("Grade A")

elif(a > 60 and a <=80):
    print("Grade B")

elif(a > 40 and a <= 60):
    print("Grade C")

else:
    print("Grade F")


OUTPUT :

Enter the subject marks : 48 
Grade C
