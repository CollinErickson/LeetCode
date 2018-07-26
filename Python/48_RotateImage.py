# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 21:17:36 2018

@author: cbe117
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        lm = len(matrix)
        if lm < 2: return
        # Rotate not on center row/col
        for i in range(lm // 2):
            for j in range(lm // 2):
                matrix[i][j], matrix[j][lm-1-i], matrix[lm-1-i][lm-1-j], matrix[lm-1-j][i] = \
                matrix[lm-1-j][i], matrix[i][j], matrix[j][lm-1-i], matrix[lm-1-i][lm-1-j]
        return
sol = Solution()
m1 = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
sol.rotate(m1)
print m1, [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]