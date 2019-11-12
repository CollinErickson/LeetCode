# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 22:26:27 2019

@author: cbe117
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        r = len(grid)
        c = len(grid[0])
        #if r==1 and c==1:
        #    return 1 - obstacleGrid[0][0]
        p = [[0 for i in range(c)] for j in range(r)]
        p[r-1][c-1] = 1 - grid[r-1][c-1]
        #print(p)
        for ri in range(r-1, -1, -1):
            for ci in range(c-1, -1, -1):
                #if grid[ri][ci] < 1:
                if ri < r - 1 and ci < c - 1:
                    p[ri][ci] = min(p[ri+1][ci], p[ri][ci+1]) + grid[ri][ci]
                elif ri < r - 1:
                    p[ri][ci] = p[ri+1][ci] + grid[ri][ci]
                elif ci < c - 1:
                    p[ri][ci] = p[ri][ci+1] + grid[ri][ci]
                else:
                    p[ri][ci] = grid[ri][ci]
        #print(p)
        return p[0][0]
sol = Solution()
print(sol.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]), 7)