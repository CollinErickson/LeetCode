# -*- coding: utf-8 -*-
"""
Created on Tue May 09 10:23:18 2017

@author: cbe117
"""

class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        n = 0
        sign = 1
        s = s.strip()
        if s[0] == "-":
            sign = -1
            s = s[1:len(s)]
        elif s[0] == "+":
            s = s[1:len(s)]
        for i in range(len(s)):
            try:
                si = int(s[i])
                n = 10*n + si
            except ValueError:
                break
        m = n * sign
        m = min(m, 2147483647)
        m = max(m, -2147483648)
        return m
sol = Solution()
print sol.myAtoi("3245")
print sol.myAtoi("    \t+3245")
print sol.myAtoi("    \t-3245")
print sol.myAtoi("    \t-3245:abcd")
print sol.myAtoi("")
print sol.myAtoi("2147483648")