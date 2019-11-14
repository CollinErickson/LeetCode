# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:00:41 2019

@author: cbe117
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        while i ** 2 <= x:
            i += 1
        return i - 1 #((i-1) ** 2 < x)
    
    def mySqrt2(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        return int(math.sqrt(x))
    
sol = Solution()
print(sol.mySqrt(4), 2)
print(sol.mySqrt(8), 2)
print(sol.mySqrt(9), 3)
print(sol.mySqrt(10), 3)
print(sol.mySqrt(1), 1)
