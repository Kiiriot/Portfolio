import os,time

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# Inventory Display - Works /Needs to be tested with addToInv/
def displayInv(inventory):
 time.sleep(1)
 print("Inventory: "), print()
 totNum = 0
 for item, quantity in inventory.items():
  time.sleep(0.3), print(item + ": " + str(quantity))
  totNum += quantity
 time.sleep(0.5)
 print("The total number of items is: " + str(totNum), end=".")

addedItems = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Adds Items from List to Inv, needs to be completed and tested
def addToInv(inventory, addedItems):
 for loot in addedItems:
  if loot in inventory.keys():
   inventory[loot] += 1
  else:
   inventory.setdefault(loot, 1)


os.system("cls")

displayInv(inventory), print()

addToInv(inventory, addedItems), print()

displayInv(inventory), print()
