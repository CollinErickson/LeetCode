# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 22:11:18 2019

@author: cbe117
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        #if r==1 and c==1:
        #    return 1 - obstacleGrid[0][0]
        p = [[0 for i in range(c)] for j in range(r)]
        p[r-1][c-1] = 1 - obstacleGrid[r-1][c-1]
        #print(p)
        for ri in range(r-1, -1, -1):
            for ci in range(c-1, -1, -1):
                if obstacleGrid[ri][ci] < 1:
                    if ri < r - 1 and ci < c - 1:
                        p[ri][ci] = p[ri+1][ci] + p[ri][ci+1]
                    elif ri < r - 1:
                        p[ri][ci] = p[ri+1][ci]
                    elif ci < c - 1:
                        p[ri][ci] = p[ri][ci+1]
                    else:
                        pass
        #print(p)
        return p[0][0]
sol = Solution()
print(sol.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]), 2)
print(sol.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,1,0],
  [0,0,0]
]), 2)
print(sol.uniquePathsWithObstacles([[1]]), 0)
print(sol.uniquePathsWithObstacles([[0, 1]]), 0)
