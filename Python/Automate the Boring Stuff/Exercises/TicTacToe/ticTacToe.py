import os,time,board

os.system("cls")

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

print("    \nTIC-TAC-TOE    "), time.sleep(1)
print("\n\nWho will start, (X) or (O)?"), time.sleep(1)
turn = input()
turn = turn.upper()

while True: # Checks for right symbol
 if turn != "X":
  if turn != "O":
   print("\nWrong Symbol, try again (X) or (O):")
   turn = input()
   turn = turn.upper()
  else:
   break
 else:
  break

os.system("cls")
for i in range(9):
 time.sleep(0.5), board.printBoard(theBoard)
 print("\n Turn for " + turn + ". Move on which space?")
 move = input()
 theBoard[move] = turn
 if turn == "X":
  turn = "O"
 else:
  turn = "X"

time.sleep(0.5), print(theBoard)