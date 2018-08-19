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
        m = [[False for j in range(lp+1)] for i in range(ls+1)]
        m[0][0] = True # (s[0] == p[0] or p[0]=='*' or p[0]=='?')
        for i in range(ls+1):
            for j in range(1, lp+1):
                if p[j-1] == "*":
                    m[i][j] = m[i][j-1] or (i>0 and m[i-1][j])
                elif i>0 and (s[i-1]==p[j-1] or p[j-1]=="?"):
                    m[i][j] = m[i-1][j-1]
        return m[ls][lp]
    
sol = Solution()
print sol.isMatch(s = "aa", p = "a"), False
print sol.isMatch(s = "aa", p = "*"), True
print sol.isMatch(s = "cb", p = "?a"), False
print sol.isMatch(s = "abceb", p = "a*b"), True
print sol.isMatch(s = "acdcb", p = "a*c?b"), False
print sol.isMatch(s = "aa", p = "??"), True
print sol.isMatch(s = "g", p = "?"), True
print sol.isMatch(s = "aaffd", p = "*"), True
print sol.isMatch(s = "sdfadfl", p = "***"), True
print sol.isMatch(s = "g", p = ""), not True
print sol.isMatch(s = "", p = "****"), True
print sol.isMatch(s = "adceb", p = "*a*b"), True
print sol.isMatch(s = "a", p = "*a"), True
print sol.isMatch(s = "aab", p = "c*a*b"), False
print sol.isMatch(s = "a", p = "a*"), True
print sol.isMatch(s = "mississippi", p = "m??*ss*?i*pi"), False



