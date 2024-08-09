import random, os # Imports the "random" library

os.system("cls")

# Guess the number in 5 tries
pcGuess = random.randint(1, 20) # Random number from 1 to 20
print("\nI'm thinking of a number from 1 to 20, guess it in 5 attempts.")

for numGuess in range(1, 6): # Player guesses 5 times
    print("Take your guess:")
    usrGuess = int(input()) # User's guess
    if pcGuess < usrGuess:
        print("\nYour guess is too high, try again.")
    elif pcGuess > usrGuess:
            print("\nYour guess is too low, try again.")
    else:
         break

if usrGuess == pcGuess:
    print("\nGood job! You guessed my number in " + str(numGuess) + " guesses!") # Good Result
else:
    print('\nNope. The number I was thinking of was ' + str(pcGuess) + ".") # Failed