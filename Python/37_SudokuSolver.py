# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 20:36:41 2018

@author: cbe117
"""

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        poss = [[[] for i in range(9)] for j in range(9)]
        # Create poss, possibilities
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    poss[i][j] = set([i for i in range(9)])
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    poss[i][j] = set([i for i in range(9)])
        
        for i in range(1e3):
            pass
        
        return
    
sol = Solution()
brd = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]
sol.solveSudoku(brd)
print brd