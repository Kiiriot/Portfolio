import random, os # Imports the "random" library

os.system("cls")

# Guess the number
pcGuess = random.randint(1, 20) # Random number from 1 to 20
print("\nI'm thinking of a number from 1 to 20")
print("Take your guess:")
usrGuess = int(input()) # User's guess
numGuess = 1

while pcGuess != usrGuess: # Start of the loop
    if pcGuess < usrGuess:
        print("\nYour guess is too high, try again.")
    elif pcGuess > usrGuess:
        print("\nYour guess is too low, try again.")
    print("Take your guess:")
    usrGuess = int(input()) # Asks for another user's guess
    numGuess += 1 # Count of guesses until final result

print("\nGood job! You guessed my number in " + str(numGuess) + " guesses!") # Final result