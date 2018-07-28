# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 08:41:34 2018

@author: cbe117
"""
# TRY RECURSIVE

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)
        return
    
    def solve(self, board):
        i,j = self.findMissing(board)
        if i==-1 and j==-1:
            return True
        #Have indices
        for k in range(1,10):
            #print i,j,k
            if self.isValid(i, j, k, board):
                board[i][j] = str(k)
                if self.solve(board):
                    return True
                # Didn't work
                board[i][j] = "."
        return False
    def findMissing(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    return i,j
        return -1,-1
    def isValid(self, i,j,k,board):
        for a in range(9):
            if a != j and board[i][a] == str(k):
                return False
            if a != i and board[a][j] == str(k):
                return False
        for a in range((i//3)*3, (i//3)*3+3):
            for b in range((j//3)*3, (j//3)*3+3):
                if not (a==i and b==j) and board[a][b] == str(k):
                    return False
        return True
    

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # Check across rows
    for i in range(9):
        s = set()
        for j in range(9):
            bij = board[i][j]
            if bij!= "." and bij in s:
                print i, j, "row"
                return False
            s.add(bij)
    # Check down columns
    for j in range(9):
        s = set()
        for i in range(9):
            bij = board[i][j]
            if bij!= "." and bij in s:
                print i, j, "col"
                return False
            s.add(bij)
    # Check 3x3 squares
    for i in range(3):
        for j in range(3):
            s = set()
            for k in range(3):
                for l in range(3):
                    bijkl = board[i*3+k][j*3+l]
                    if bijkl!= "." and bijkl in s:
                        print i, j, "square"
                        return False
                    s.add(bijkl)
                    
    return True
def pprint(board):
    print
    for i in range(9):
        for j in range(9):
            print board[i][j],
        print
    return

if False:   
    sol = Solution()
    brd = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
                    [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
                    ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
                    [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
                    [".",".",".",".","8",".",".","7","9"]]
    po = sol.solveSudoku(brd)
    print brd

sol = Solution()
brd2 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],
        [".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],
        [".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],
        [".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],
        [".",".",".","2","7","5","9",".","."]]
po2 = sol.solveSudoku(brd2)
for b in brd2: print b #print brd2
