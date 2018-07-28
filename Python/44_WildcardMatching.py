# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 21:54:04 2018

@author: cbe117
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls = len(s)
        lp = len(p)
        m = [[False for j in range(lp)] for i in range(ls)]
        m[0][0] = True
        for i in range(ls):
            for j in range(ls):
                if i > 0 and (m[i-1][j] and p[j]=="*"):
                    m[i][j] = True
                if i>0 and m[i-1][j-1] and (p[j] == "?" or p[j] == "*" or s[i] == p[j]):
                    m[i][j] = True
        return
    
sol = Solution()
print sol.isMatch(s = "aa", p = "a"), False
print sol.isMatch(s = "aa", p = "*"), True
print sol.isMatch(s = "cb", p = "?a"), False
print sol.isMatch(s = "abceb", p = "a*b"), True
print sol.isMatch(s = "acdcb", p = "a*c?b"), False