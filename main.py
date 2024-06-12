currentBoard = [
[ 0, 0, 0, 0, 0, 0, 0, 0],
[ 0, 0, 2, 2, 1, 1, 1, 0],
[ 0, 0, 1, 2, 1, 1, 0, 0],
[ 0, 0, 0, 2, 1, 1, 0, 0],
[ 0, 0, 0, 2, 1, 0, 0, 0],
[ 0, 0, 0, 0, 0, 0, 0, 0],
[ 0, 0, 0, 0, 0, 0, 0, 0],
[ 0, 0, 0, 0, 0, 0, 0, 0]
];

def checkAndMarkRow(board):
  for j in range(len(board)):
      if board[j] == 2:
        currentIndex = j
        while currentIndex != len(board)-1 and board[currentIndex+1] == 1:
            currentIndex += 1
        if currentIndex != len(board)-1 and currentIndex != j:
          board[currentIndex+1] = 3

  for h in range(len(board)):
    if board[h] == 2:
      currentIndexReverse = h
      while currentIndexReverse != 0 and board[currentIndexReverse-1] == 1:
        currentIndexReverse -= 1
      if currentIndexReverse != 0 and currentIndexReverse != h:
        board[currentIndexReverse-1] = 3
  return board

def markRows(board):
  result = []
  for currentRow in board:
    result.append(checkAndMarkRow(currentRow))
  return board

def markColumns(board):
  newBoard = []
  for h in range(8):
    for i in range(8):
      newBoard.append(board[i][h])
      if len(newBoard) == 8:
        markedBoard = checkAndMarkRow(newBoard)
        newBoard = []
        if 3 in markedBoard:
          indexOfThree = markedBoard.index(3)
          board[indexOfThree][h] = 3
          markedBoard = []
  return board

def markDiagonals(board):
  numBoard = len(board)
  # 右下→左上
  for i in range(1-numBoard, numBoard):
    diagonal = []
    for h in range(numBoard-abs(i)):
      diagonal.append(board[max(0, -i)+h][max(0, i)+h])
    markedDiagonal = checkAndMarkRow(diagonal)
    for j in range(len(markedDiagonal)):
      if markedDiagonal[j] == 3:
        board[max(0, -i)+j][max(0, i)+j] = 3

  # 左下→右上
  for i in range(1-numBoard, numBoard):
    diagonal = []
    for h in range(numBoard-abs(i)):
      diagonal.append(board[max(0, i)+h][min(numBoard+i, numBoard)-h-1])
    markedDiagonal = checkAndMarkRow(diagonal)
    for j in range(len(markedDiagonal)):
      if markedDiagonal[j] == 3:
        board[max(0, i)+j][min(numBoard+i, numBoard)-j-1] = 3
  return board


def canPutTwoBoard(board):
  markRows(board)
  markColumns(board)
  markDiagonals(board)
  return board

print(canPutTwoBoard(currentBoard))
