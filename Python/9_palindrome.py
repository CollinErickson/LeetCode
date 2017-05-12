# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 23:45:29 2017

@author: cbe117
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = list(str(abs(x)))
        s.reverse()
        return abs(x) == int(''.join(s))
sol = Solution()
print sol.isPalindrome(1234)
print sol.isPalindrome(1234321)
print sol.isPalindrome(-2147483648)