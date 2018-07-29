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
        if lm % 2 == 1:
            j = lm // 2
            for i in range(lm // 2):
                matrix[i][j], matrix[j][lm-1-i], matrix[lm-1-i][lm-1-j], matrix[lm-1-j][i] = \
                matrix[lm-1-j][i], matrix[i][j], matrix[j][lm-1-i], matrix[lm-1-i][lm-1-j]
        return

def pprint(x):
    for i in x:
        print i
sol = Solution()
m1 = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
sol.rotate(m1)
print m1, '\n', [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
m2 = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
sol.rotate(m2)
#pprint(m2)
#pprint([
#  [15,13, 2, 5],
#  [14, 3, 4, 1],
#  [12, 6, 8, 9],
#  [16, 7,10,11]
#])
print m2, '\n', [
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

m1 = [
  [1,2],
  [4,5]
]
sol.rotate(m1)
print m1, '\n', [
  [4,1],
  [5,2]
]