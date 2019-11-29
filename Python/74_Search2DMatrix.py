# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 15:37:32 2019

@author: cbe117
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        for i in range(length(matrix)):
            for j in range(length(matrix[0])):
                if matrix[i][j] == target:
                    return False
                elif matrix[i][j] < target:
                    return False
        
        return False
sol = Solution()
print(sol.searchMatrix( [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3), True)