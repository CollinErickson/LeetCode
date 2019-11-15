# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:04:48 2019

@author: cbe117
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        x = [1 for i in range(n + 1)]
        #x[1] = 1
        for i in range(2, n + 1):
            x[i] = x[i-2] + x[i-1]
        return x[-1]
    
sol = Solution()
print(sol.climbStairs(2), 2)
print(sol.climbStairs(3), 3)
print(sol.climbStairs(12), 233)

