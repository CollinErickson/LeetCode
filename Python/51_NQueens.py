# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 22:04:53 2018

@author: cbe117
"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        s = []
        return
    def isValid(n, queens, checklastrow):
        for i in range(n):
            if abs(queens[i] - checklastrow) == i or queens[i]==checklastrow:
                return False
        return True
sol = Solution()
print(sol.solveNQueens(4))