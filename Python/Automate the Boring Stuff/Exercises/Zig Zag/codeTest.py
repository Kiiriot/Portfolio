import zigZag,sys,os

os.system("cls")

# Executes Loop-Animation
try:
 while True:
  zigZag.ZZRight()
  zigZag.ZZLeft()
except KeyboardInterrupt:
 sys.exit