import os

os.system("cls")

phrase = "I love jogging in winter"
count = {}

for characters in phrase:
 count.setdefault(characters, 0)
 count[characters] += 1
print(count)