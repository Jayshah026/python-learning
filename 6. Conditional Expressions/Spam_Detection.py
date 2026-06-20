Code : 

message = input("Enter the message : ")

m1 = "Click now"
m2 = "Subscribe Now"
m3 = "Buy this"
m4 = "Free for you"
m5 = "Redeem now"

if((m1 in message) or (m2 in message) or (m3 in message) or (m4 in message) or (m5 in message)):
    print("This is a spam message")

else:
    print("This is not a spam message")


OUTPUT : 

Enter the message : Hello sir, the Claude subscription is Free for you, Redeem now!!
This is a spam message
