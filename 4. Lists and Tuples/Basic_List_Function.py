Code : 

MyList = [423, 23, 54, 65 , 1, 32, 2, 100, 58]


MyList.append(897)
print(MyList)

print(MyList.count(23))

MyList.pop(1)
print(MyList)

MyList.sort()
print(MyList)

MyList.clear()
print(MyList)


OUTPUT : 

[423, 23, 54, 65, 1, 32, 2, 100, 58, 897]
1
[423, 54, 65, 1, 32, 2, 100, 58, 897]
[1, 2, 32, 54, 58, 65, 100, 423, 897]
[]
