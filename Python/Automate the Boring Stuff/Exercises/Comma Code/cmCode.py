import os

os.system("cls")

spam = ['apples', 'bananas', 'tofu', 'cats']
repNum = len(spam)

for x in range(repNum - 1):
 print(spam[x] + ", ", end="")
print("and " + spam[x + 1])

