import random

number = random.randint(1,100)
guess = 0

while guess != number:
    guess = int(input("Enter Guess -"))
    if (guess < number):
        print("Guess Higher")
    elif (guess > number):
        print("Guess lower") 
    else:
        print("(Congratulations!you are the winner")       