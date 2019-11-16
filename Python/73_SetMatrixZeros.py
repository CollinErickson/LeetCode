# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:18:04 2019

@author: cbe117
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ncol = len(matrix[0])
        nrow = len(matrix)
        zcol = [0 for i in range(len(matrix[0]))]
        zrow = [0 for i in range(len(matrix))]
        for icol in range(ncol):
            for irow in range(nrow):
                if matrix[irow][icol] == 0:
                    zcol[icol] = 1
                    zrow[irow] = 1
        for icol in range(ncol):
            for irow in range(nrow):
                if zcol[icol] == 1 or zrow[irow] == 1:
                    matrix[irow][icol] = 0
        
        #return matrix

sol = Solution()
print(sol.setZeroes([
  [1,1,1],
  [1,0,1],
  [1,1,1]
]), '\n', [
  [1,0,1],
  [0,0,0],
  [1,0,1]
])