tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
 colWidth = [0] * len(data)
 numItems = [len(data[0])]
 for sublist, x in enumerate(data):
  maxLen = 0
  for string in sublist:
   if len(string) > maxLen:
    maxLen = string
  colWidth[sublist] = maxLen
 print(colWidth)

printTable(tableData)

