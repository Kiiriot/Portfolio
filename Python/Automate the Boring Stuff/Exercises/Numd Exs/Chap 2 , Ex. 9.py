import os

os.system("cls")

# Write code that prints Hello if 1 is stored in spam;prints Howdy if 2 is stored in spam, and prints Greetings!
print("\n Type 1, 2 or anything else")
spam = str(input())
if spam == "1":
    print("Hello")
elif spam == "2":
    print("Howdy")
else:
    print("Greetings")

# Works