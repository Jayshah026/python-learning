def sum(n):
    if(n == 1):
        return 1
    else:
        return n + sum(n - 1)
    

a = sum(5)

print(a)



"""
OUTPUT : 

15

"""