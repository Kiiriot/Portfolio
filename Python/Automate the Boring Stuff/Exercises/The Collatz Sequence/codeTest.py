import collatzSqc,sys,time,os

os.system("cls")

try: # Code Testing
 collatzSqc.collatz()
except ValueError: # Code Breaking
 time.sleep(1); print("\nYou must enter a number"); time.sleep(1)
 sys.exit