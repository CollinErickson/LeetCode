class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not any(board): return
        
        r, c = len(board), len(board[0])
        Os = Queue()
        for i in range(r):
          if board[i][0] == "O":
            Os.put((i,0))
          if board[i][c-1] == "O":
            Os.put((i,c-1))
        for j in range(c):
          if board[0][j] == "O":
            Os.put((0,j))
          if board[r-1][j] == "O":
            Os.put((r-1,j))
        while not Os.empty():
          (i,j) = Os.get()
          #print('got', i, j)
          if i>=0 and i < r and j >= 0 and j < c and board[i][j] == "O":
              board[i][j] = "B"
              Os.put((i-1,j))
              Os.put((i+1,j))
              Os.put((i,j-1))
              Os.put((i,j+1))
        for i in range(r):
            for j in range(c):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "B":
                    board[i][j] = "O"
        #print('done')
        return None
from queue import Queue

sol = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
(sol.solve(board))
print(board)
#board = [["X","O","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#print(sol.solve(board))
#print(board)


#any([[4]])
