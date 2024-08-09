import time,os

os.system("cls")

# Zig-Zag Code
# Going Right
def ZZRight():
 time.sleep(0.1)
 print("*" * 12)
 indent = 0
 while indent < 20:
  indent += 1
  time.sleep(0.1)
  print(" " * indent + "*" * 12)

# Going Left
def ZZLeft():
 indent = 20
 while indent <= 20 and indent > 1:
  indent -= 1
  time.sleep(0.1)
  print(" " * indent + "*" * 12)