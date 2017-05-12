# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 21:13:22 2017

@author: cbe117
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 0
        sgn = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            #print x
            xnext = x / 10
        
            z = x - xnext * 10
            y = y*10 + z
            x = xnext
        if y >= 2147483648L: 
            return 0
        return y * sgn
sol = Solution()
print sol.reverse(-1234344)
print sol.reverse(1534236469)
        