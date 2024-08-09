import random, sys, os

os.system("cls")

# Rock, Paper, Scissors
print("\nROCK, PAPER, SCISSORS")

# Scoreboard variables
wins = 0
losses = 0
ties = 0

# Game Loop
while True:
    print("\n%s Wins, %s Losses, %s Ties" % (wins, losses, ties)) # Only thing I couldn't do!
    # Player Input
    while True:
        print("\nEnter your move: (r)ock, (p)aper, (s)isscors or (q)uit")
        usrMove = input()
        if usrMove == "q":
            sys.exit()
        elif usrMove == 'r' or usrMove == 'p' or usrMove == 's':
            break
        print('Type one of r, p, s, or q.')

    # User choice
    if usrMove == "r":
        print("ROCK versus...")
    elif usrMove == "p":
        print("PAPER versus...")
    else:
        print("SCISSORS versus...")

    # PC choice
    pcMove = random.randint(1, 3)
    if pcMove == 1:
        pcMove = "r"
        print("ROCK")
    elif pcMove == 2:
        pcMove = "p"
        print("PAPER")
    elif pcMove == 3:
        pcMove = "s"
        print("SCISSORS")

    # Update Scoreboard
    if usrMove == pcMove:
        print('It is a tie!')
        ties = ties + 1
    elif usrMove == 'r' and pcMove == 's':
        print('You win!')
        wins = wins + 1
    elif usrMove == 'p' and pcMove == 'r':
        print('You win!')
        wins = wins + 1
    elif usrMove == 's' and pcMove == 'p':
        print('You win!')
        wins = wins + 1
    elif usrMove == 'r' and pcMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif usrMove == 'p' and pcMove == 's':
        print('You lose!')
        losses = losses + 1
    elif usrMove == 's' and pcMove == 'r':
        print('You lose!')
        losses = losses + 1
