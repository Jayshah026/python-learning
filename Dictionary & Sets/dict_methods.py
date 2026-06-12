Code : 

marks = {

    "Jay" : 100,
    "Heet" : 98,
    "Hetva" : 84,
    "Dhruv" : 88,
    "Mohit" : 100
}

print(marks)                                # Prints the whole dictionary

print(marks.items())                        # Prints every items which is in the marks dictionary

print(marks.keys())                         # Prints every keys of the dictionary 

print(marks.values())                       # Prints every value of the dictionary 

marks.update({"Mohit" : 81, "Jenny" : 52})  # To update the existing value or add new value in the dictionary 
print(marks)                                

print(marks.get("Jay", "Dhruv"))            # Here if Jay exist then Dhruv will have no effect, if not then get will look for Dhruv

print(marks.get("Jay23", "Dhruv"))          # Here Jay23 is not there but it will not give error, so now get will return Dhruv

print(marks.get("Jay23", marks["Dhruv"]))   # Here now we will have 88 instead of Dhruv

print(marks["Jay"])


OUTPUT : 

{'Jay': 100, 'Heet': 98, 'Hetva': 84, 'Dhruv': 88, 'Mohit': 100}
dict_items([('Jay', 100), ('Heet', 98), ('Hetva', 84), ('Dhruv', 88), ('Mohit', 100)])
dict_keys(['Jay', 'Heet', 'Hetva', 'Dhruv', 'Mohit'])
dict_values([100, 98, 84, 88, 100])
{'Jay': 100, 'Heet': 98, 'Hetva': 84, 'Dhruv': 88, 'Mohit': 81, 'Jenny': 52}
100
Dhruv
88
100
