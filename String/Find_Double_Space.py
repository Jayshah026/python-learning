Code : 

String = "My name is Jay  D Shah"

print(String.find("  "))
print(String.find("J"))
print(String.find("   "))



OUTPUT : 

14    # Here it's an index showing where the element is that we are finding. Here double space detected on 11th index.
11    # Here "J" is detected on 11th Index
-1    # Here there is no "   " (Three spaces) so here the value is -1 showing that element we are finding is not exits. 
