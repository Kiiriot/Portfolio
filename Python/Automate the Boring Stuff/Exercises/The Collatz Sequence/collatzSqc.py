import time, os

os.system("cls")

def collatz():
 num = int(input("\nEnter a number: "))
 while True: # Main loop
  if num % 2 == 0: # "%" Gives the rest of the divison, there is no rest if it's even
   print("\nNumber is Even"); time.sleep(1)
   print(str(num) + " divided by 2 is:"); time.sleep(1)
   num //= 2; print(num); time.sleep(1)
  elif num == 1: # Goal
   print("\nWe made it to 1!"); time.sleep(1)
   break
  elif num % 2 == 1: # "%" Gives the rest of the divison, there IS rest if it's odd
   print("\nNumber is Odd"); time.sleep(1)
   print("To make it even we multiply it by 3, and sum it 1:"); time.sleep(1)
   num *= 3; num += 1
   print(num); time.sleep(1)