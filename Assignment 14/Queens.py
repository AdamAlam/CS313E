#  File: Queens.py

#  Description:

#  Student Name: Adam Alam

#  Student UT EID: aba2288

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: October 19 2019

#  Date Last Modified: October 21 2019
sols = 0

class Queens (object):
  # initialize the board
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()

  # check if no queen captures another
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True

  # do a recursive backtracking solution
  def recursive_solve (self, col):
    global sols
    if (col == self.n):
      sols += 1
      self.print_board()
      print("")
    else:
      for i in range (self.n):
        if (self.is_valid(i, col)):
          self.board[i][col] = 'Q'
          self.recursive_solve(col+1)
          self.board[i][col] = '*'

  # if the problem has a solution print the board
  def solve (self, dim):
    global sols
    self.recursive_solve(0)
    print(f"There are {sols} solutions for a {dim} x {dim} board.")
    
def main():
  # create a regular chess board
  try:
    dim = int(input("Enter the size of board: "))
  except:
    pass
  while dim < 1 or dim > 8 or type(dim) != int:
    try:
      dim = int(input("Enter the size of board: "))
    except:
      pass
  print("")
  game = Queens(dim)
    
  # place the queens on the board
  game.solve(dim)

main()
