import time,os

chessBoard = {"h1": "bking", "h2": "wking", "h3": "wking"}


def isValidChessBoard(chessBoard): # function that takes an argument
 os.system("cls")
 print("---CHESS BOARD VALIDATOR---"), time.sleep(2)
 print("\nRemember, duplicate coordinates won't be counted!"), time.sleep(2)
 print("\nAnalyzing your Chess Board..."), print(), time.sleep(3)
 coordForm = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", # Acceptable coords format
              "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8",
              "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8",
              "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8",
              "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8",
              "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8",
              "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8",
              "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"]
 pieceForm = ["wking", "wbishop", "wknight", "wrook", "wpawn", "wqueen", # Acceptable piece format
              "bking", "bbishop", "bknight", "brook", "bpawn", "bqueen"]
 coordCount = {"a1": 0, "a2": 0, "a3": 0, "a4": 0, "a5": 0, "a6": 0, "a7": 0, "a8": 0, # Coordinate Counter for // Error //
              "b1": 0, "b2": 0, "b3": 0, "b4": 0, "b5": 0, "b6": 0, "b7": 0, "b8": 0,
              "c1": 0, "c2": 0, "c3": 0, "c4": 0, "c5": 0, "c6": 0, "c7": 0, "c8": 0,
              "d1": 0, "d2": 0, "d3": 0, "d4": 0, "d5": 0, "d6": 0, "d7": 0, "d8": 0,
              "e1": 0, "e2": 0, "e3": 0, "e4": 0, "e5": 0, "e6": 0, "e7": 0, "e8": 0,
              "f1": 0, "f2": 0, "f3": 0, "f4": 0, "f5": 0, "f6": 0, "f7": 0, "f8": 0,
              "g1": 0, "g2": 0, "g3": 0, "g4": 0, "g5": 0, "g6": 0, "g7": 0, "g8": 0,
              "h1": 0, "h2": 0, "h3": 0, "h4": 0, "h5": 0, "h6": 0, "h7": 0, "h8": 0}
 wPieceCount = {"wking": 0, "wbishop": 0, "wknight": 0, "wrook": 0, "wpawn": 0, "wqueen": 0} # White Piece Counter for // Error //
 bPieceCount = {"bking": 0, "bbishop": 0, "bknight": 0, "brook": 0, "bpawn": 0, "bqueen": 0} # Black Piece Counter for // Error //
 for coord, piece in chessBoard.items(): # For Loop Start
  if coord not in coordForm: # // ERROR // Coordinate in wrong format
   print("Error: Coordinate in wrong format\n")
   break
  elif piece not in pieceForm: # // ERROR // Piece in wrong format
   print("Error: Piece in wrong format\n")
   break
  else: # Sum Counter
   coordCount[coord] += 1
   if piece in wPieceCount:
    wPieceCount[piece] += 1
   else:
    bPieceCount[piece] += 1
   if sum(wPieceCount.values()) > 16: # // ERROR // Too many White Pieces
    print("Error: Too many White Pieces\n")
    break
   elif sum(bPieceCount.values()) > 16: # // ERROR // Too many Black Pieces
    print("Error: Too many Black Pieces\n")
    break
   elif coordCount[coord] > 1: # // ERROR // Piece on the same square | Won't work because Dictionaries can't have duplicate keys!
    print("Error: Piece on the same square\n")
    break
   else: # Piece Counter
    if wPieceCount["wking"] > 1: # // ERROR // Too many White Kings
     print("Error: Too many White Kings\n")
     break
    elif bPieceCount["bking"] > 1: # // ERROR // Too many Black Kings
     print("Error: Too many Black Kings\n")
     break
    elif wPieceCount["wpawn"] > 8: # // ERROR // Too many White Pawns
     print("Error: Too many White Pawns\n")
     break
    elif bPieceCount["bpawn"] > 8: # // ERROR // Too many Black Pawns
     print("Error: Too many Black Pawns\n")
     break
 else:
  print("Chess Board has been Validated, no errors found!\n")

isValidChessBoard(chessBoard)
