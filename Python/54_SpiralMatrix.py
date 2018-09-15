# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:10:01 2018

@author: cbe117
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        out = [0 for i in range(n*m)]
        lr = 1
        ud = 0
        r=0
        c=0
        toprowdone = -1
        bottomrowdone = m
        rightcoldone = n
        leftcoldone = -1
        i = 0
        while toprowdone +1 < bottomrowdone and leftcoldone+1 < rightcoldone:
            #print(r,c,out, toprowdone, bottomrowdone, leftcoldone, rightcoldone)
            out[i] = matrix[r][c]
            if lr == 1:
                if c+1 >= rightcoldone:
                    lr=0
                    ud=1
                    toprowdone += 1
                    r += 1
                else:
                    c += 1
            elif lr == -1:
                if c-1 <= leftcoldone:
                    lr=0
                    ud=-1
                    bottomrowdone -= 1
                    r -= 1
                else:
                    c -= 1
            elif ud == 1:
                if r+1 >= bottomrowdone:
                    lr=-1
                    ud=0
                    rightcoldone -= 1
                    c -= 1
                else:
                    r += 1
            elif ud == -1:
                if r-1 <= toprowdone:
                    lr=1
                    ud=0
                    leftcoldone += 1
                    c += 1
                else:
                    r -= 1
            i += 1
        return out
sol = Solution()
print(sol.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]), '\n', [1,2,3,6,9,8,7,4,5])
    
print(sol.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]), '\n', [1,2,3,4,8,12,11,10,9,5,6,7])
    
print(sol.spiralOrder([
  [1]
]), '\n', [1])
print(sol.spiralOrder([
  [1, 2, 3, 4]
]), '\n', [1,2,3,4])
print(sol.spiralOrder([
  []
]), '\n', [])