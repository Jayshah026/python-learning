import random 

n = random.randint(1, 100)

guesses = 0

user = -1

while(user != n):
    user = int(input("Guess the number : "))
    guesses += 1

    if(user > n):
        print("Enter lower number")
    elif(user < n):
        print("Enter higher number")
    else:
        print("You have guessed the number 🤩🙌")


print(f"Here user have guessed the number {n} in {guesses} Guesses")