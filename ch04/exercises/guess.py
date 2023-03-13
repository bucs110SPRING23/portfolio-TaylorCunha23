import random

correctguess = random.randrange(1,1000)
guesses = []

while(True):
    guess = int(input("Guess a random number between 1 and 1000:"))
    guesses.append(guess)
    number_of_guesses = len(guesses)
    if (guess == correctguess):
        print("Correct!")
        break
    elif (guess > correctguess):
        print("Too high, try again!")
    else:
        print("Too low, try again!")

print("The correct guess was:", correctguess)
print("Your guesses:", guesses)
print("It took you", number_of_guesses, "tries to get the correct guess.")
print("The maximum number of guesses it should take using a binary search algorithm is 10 guesses.")
    
    