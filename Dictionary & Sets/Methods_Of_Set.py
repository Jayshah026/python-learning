"""
Some of the basic operations or methods we have used in here for SET. 
"""

Code : 

s1 = {1, 3, 4, 64, 43}
s2 = {4, 42, 3, 54}

print("Union of sets")
print(s1.union(s2))
print("Intersection of sets")
print(s1.intersection(s2))

print("Adding an element into s1")
s1.add(100)
print(s1)

print("Removing an element from the s2")
s2.remove(54)
print(s2)


OUTPUT :

Union of sets
{64, 1, 3, 4, 42, 43, 54}
Intersection of sets
{3, 4}
Adding an element into s1
{64, 1, 3, 4, 100, 43}
Removing an element from the s2
{42, 3, 4}
