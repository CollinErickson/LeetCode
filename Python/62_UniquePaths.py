# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 22:41:28 2018

@author: cbe117
"""

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <n:
            return self.uniquePaths(n, m)
        y = 1
        b = n + m - 2
        while b > m-1:
            y *= b
            b -= 1
        while n-1 > 0:
            y /= n-1
            n -= 1
        
        return int(y+.5)
    def factorial(self, x):
        y = 1
        if x <= 1:
            return 1
        while x > 1:
            y *= x
            x -= 1
        return y
sol = Solution()
print(sol.uniquePaths(3,2), 3)
print(sol.uniquePaths(7,3), 28)