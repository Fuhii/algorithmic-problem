from enum import Enum

class State(Enum):
  BLANK = 0
  WHITE = 1
  BlACK = 2
  PUTBLACK = 3
  BOARDROW = 8

def checkAndMarkRow(board):
  # ある配列の要素が２である時それよりあとの要素に１が続いておりその後０が現れた場所を３に置き換える処理
  n = len(board)
  for j in range(n):
      if board[j] == State.BlACK.value:
        currentIndex = j
        while currentIndex != n-1 and board[currentIndex+1] == State.WHITE.value:
            currentIndex += 1
        if currentIndex != n-1 and currentIndex != j:
          board[currentIndex+1] = State.PUTBLACK.value
  # 配列を逆順にして同様にして３に置き換える処理
  for h in range(n):
    if board[h] == State.BlACK.value:
      currentIndexReverse = h
      while currentIndexReverse != 0 and board[currentIndexReverse-1] == State.WHITE.value:
        currentIndexReverse -= 1
      if currentIndexReverse != 0 and currentIndexReverse != h:
        board[currentIndexReverse-1] = State.PUTBLACK.value
  return board

def markRows(board):
  result = []
  for currentRow in board:
    result.append(checkAndMarkRow(currentRow))
  return board

def markColumns(board):
  # 二重配列のたての要素を取得し３に置き換える処理
  n = len(board)
  newBoard = []
  for h in range(State.BOARDROW.value):
    for i in range(State.BOARDROW.value):
      newBoard.append(board[i][h])
      if n == State.BOARDROW.value:
        markedBoard = checkAndMarkRow(newBoard)
        newBoard = []
        if State.PUTBLACK.value in markedBoard:
          indexOfThree = markedBoard.index(State.PUTBLACK.value)
          board[indexOfThree][h] = State.PUTBLACK.value
          markedBoard = []
  return board

def markDiagonals(board):
  # 二重配列の右下→左上の斜めの要素を取得し３に置き換える処理
  # iは対角線の数を表しhはその対角線に含まれる要素の数を表す。
  n = len(board)
  for i in range(1-n, n):
    diagonal = []
    for h in range(n-abs(i)):
      diagonal.append(board[max(0, -i)+h][max(0, i)+h])
    markedDiagonal = checkAndMarkRow(diagonal)
    # ３をおける場所のindexを特定して置き換える処理
    for j in range(len(markedDiagonal)):
      if markedDiagonal[j] == State.PUTBLACK.value:
        board[max(0, -i)+j][max(0, i)+j] = State.PUTBLACK.value

  # 二重配列の左下→右上の斜めの要素を取得し３に置き換える処理
  for i in range(1-n, n):
    diagonal = []
    for h in range(n-abs(i)):
      diagonal.append(board[max(0, i)+h][min(n+i, n)-h-1])
    markedDiagonal = checkAndMarkRow(diagonal)
    for j in range(len(markedDiagonal)):
      if markedDiagonal[j] == State.PUTBLACK.value:
        board[max(0, i)+j][min(n+i, n)-j-1] = State.PUTBLACK.value
  return board


def markBoard(board):
  # 横方向を探索し３に置き換える処理
  markRows(board)
  # 縦方向を探索し３に置き換える処理
  markColumns(board)
  # 斜め方向を探索し３に置き換える処理
  markDiagonals(board)
  return board

if __name__ == "__main__":
  result = markBoard([
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 2, 2, 1, 1, 1, 0],
    [ 0, 0, 1, 2, 1, 1, 0, 0],
    [ 0, 0, 0, 2, 1, 1, 0, 0],
    [ 0, 0, 0, 2, 1, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0]
  ])
  print(result)

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
