# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 22:04:53 2018

@author: cbe117
"""

class Solution(object):
    s = []
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n==1: return [["Q"]]
        self.run([-1 for i in range(n)], index=0)
        return self.s
    def run(self, board, index):
        #print(index, board)
        # board is vector with rows of queens
        # index is the current index to check, go left to right
        # Check if board is filled out. If yes, it is solution, would have been
        #  rejected earlier if not valid
        if index == len(board):
            tmp = ["."*i + "Q" + "."*(len(board)-i-1) for i in board]
            #print(tmp, board)
            self.s.append(tmp)
            return
        for i in range(len(board)):
            board[index] = i
            if self.isValid(n=index,board=board[:index], checklastrow=i):
                self.run(board[:], index + 1)
    def isValid(self, n, board, checklastrow):
        for i in range(n):
            if abs(board[i] - checklastrow) == n-i or board[i]==checklastrow:
                return False
        return True
sol = Solution()
#print(sol.solveNQueens(4))
#print(sol.solveNQueens(5))
print(sol.solveNQueens(7))