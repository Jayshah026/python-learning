import random

computer = random.choice([-1, 0, 1]) # Here numbers are easy to understand instead of string so computer will choose random 
                                     # number from these numbers

print("Welcome to the Snake, Water & Gun game")
print("")

print("Here\n s = snake \n w = water \n g = gun ") # To inform the user what are these s, w, g really means
print("")

you_input = input("Enter your choices form \"s, w, g\" :  ") # To take input from the user

you_dict = {"s" : -1, "w" : 0, "g" : 1} # Here key will be string by that it will be easier to choose numbers to compare

you_reverse_dict = {-1 : "Snake", 0 : "Water", 1 : "Gun"} # To show what value both chooses

you = you_dict[you_input]

print(f"The computer choice is {you_reverse_dict[computer]} \nAnd your choice is {you_reverse_dict[you]}")

if(computer == you):
    print("It's a draw, Try again")

else:
    if(computer == -1 and you == 0):
        print("you have Lost the game 😫")

    elif(computer == -1 and you == 1):
        print("you have Won the game 😝")

    elif(computer == 0 and you == -1):
        print("you have Won the game 😝")

    elif(computer == 0 and you == 1):
        print("you have Lost the game 😫")

    elif(computer == 1 and you == -1):
        print("you have Lost the game 😫")

    elif(computer == 1 and you == 0):
        print("you have Won the game 😝")

print("")
print("Well played")



"""
OUTPUT : 

Welcome to the Snake, Water & Gun game

Here
 s = snake 
 w = water 
 g = gun 

Enter your choises form "s, w, g" :  s
The computer choice is Snake 
And your choice is Snake
It's a draw, Try again

Well played


Welcome to the Snake, Water & Gun game

Here
 s = snake 
 w = water 
 g = gun 

Enter your choices form "s, w, g" :  g
The computer choice is Water 
And your choice is Gun
you have Lost the game 😫

Well played


Welcome to the Snake, Water & Gun game

Here
 s = snake 
 w = water 
 g = gun 

Enter your choices form "s, w, g" :  g
The computer choice is Snake 
And your choice is Gun
you have Won the game 😝

Well played

"""