def checkAndMarkRow(board):
  # ある配列の要素が２である時それよりあとの要素に１が続いておりその後０が現れた場所を３に置き換える処理
  for j in range(len(board)):
      if board[j] == 2:
        currentIndex = j
        while currentIndex != len(board)-1 and board[currentIndex+1] == 1:
            currentIndex += 1
        if currentIndex != len(board)-1 and currentIndex != j:
          board[currentIndex+1] = 3
  # 配列を逆順にして同様にして３に置き換える処理
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
  # 二重配列のたての要素を取得し３に置き換える処理
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
  # 二重配列の右下→左上の斜めの要素を取得し３に置き換える処理
  # iは対角線の数を表しhはその対角線に含まれる要素の数を表す。
  for i in range(1-numBoard, numBoard):
    diagonal = []
    for h in range(numBoard-abs(i)):
      diagonal.append(board[max(0, -i)+h][max(0, i)+h])
    markedDiagonal = checkAndMarkRow(diagonal)
    # ３をおける場所のindexを特定して置き換える処理
    for j in range(len(markedDiagonal)):
      if markedDiagonal[j] == 3:
        board[max(0, -i)+j][max(0, i)+j] = 3

  # 二重配列の左下→右上の斜めの要素を取得し３に置き換える処理
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
  # 横方向を探索し３に置き換える処理
  markRows(board)
  # 縦方向を探索し３に置き換える処理
  markColumns(board)
  # 斜め方向を探索し３に置き換える処理
  markDiagonals(board)
  return board

if __name__ == "__main__":
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
  print(canPutTwoBoard(currentBoard))

  #　問題
  #　以下のような二周配列が与えられたとする。それをオセロの盤面と見た時に０は空白、１は白、２は黒と考える。
  #　その時２をおくことのできる０の場所を３に置き換える処理を実装してください。
  # currentBoard = [
  #   [ 0, 0, 0, 0, 0, 0, 0, 0],
  #   [ 0, 0, 2, 2, 1, 1, 1, 0],
  #   [ 0, 0, 1, 2, 1, 1, 0, 0],
  #   [ 0, 0, 0, 2, 1, 1, 0, 0],
  #   [ 0, 0, 0, 2, 1, 0, 0, 0],
  #   [ 0, 0, 0, 0, 0, 0, 0, 0],
  #   [ 0, 0, 0, 0, 0, 0, 0, 0],
  #   [ 0, 0, 0, 0, 0, 0, 0, 0]
  # ];
