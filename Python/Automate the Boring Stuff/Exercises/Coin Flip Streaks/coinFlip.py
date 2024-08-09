import random, os

os.system("cls")

totFlip = 10000
finList = []

# Coin Flip Program
for x in range(totFlip):
 if random.randint(0, 1) == 0:
  finList.append('H')
 else:
  finList.append('T')

"""
# Print List of visibility
print(finList)
print(finList[500])
"""

# Streak of 6 checker Program
flipH = 0
flipT = 0
streakH = 0
streakT = 0

for x in range(len(finList)):
 if finList[x] == "H":
  flipT = 0
  flipH += 1
  if flipH == 6:
   streakH += 1
   flipH == 0
 if finList[x] == "T":
  flipH = 0
  flipT += 1
  if flipT == 6:
   streakT += 1
   flipT == 0

totStreak = streakH + streakT
print("The total number of streaks is: " + str(totStreak))