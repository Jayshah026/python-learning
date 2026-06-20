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