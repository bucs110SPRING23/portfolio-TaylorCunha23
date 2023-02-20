import random

correctguess = random.randrange(1,10)

for i in range(3):
        guess = int(input("Guess a random number between 1 and 10:"))

        if (guess == correctguess):
            print("Correct!")
            break
        elif (guess > correctguess):
            print("Too high, try again!")
        else:
            print("Too low, try again!")
print("You used up all your guesses!")