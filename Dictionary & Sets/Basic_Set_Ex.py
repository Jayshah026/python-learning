Code : 

s = {1, 1, 4.3, 423,42.3,True, None, 3223, "jay", 2, 2}

print(type(s))
print(s)

e = set()         # This is an empty set
print(type(e), e)


OUTPUT : 

<class 'set'>
{None, 1, 2, 4.3, 423, 'jay', 42.3, 3223}
<class 'set'> set()


"""

Explanation : 

Here the output will not be in ordered way. 
Set just make sure that every element inside it, at output time all the repeated values will be vanished. Means every element will be Unique in Output. 

"""
