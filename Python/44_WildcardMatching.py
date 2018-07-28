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
        if ls ==0 and lp==0:
            return True
        if ls>0 and lp==0:
            return False
        if ls==0 and lp>0:
            for j in range(lp):
                if p[j] != "*":
                    return False
                return True
        m = [[False for j in range(lp)] for i in range(ls)]
        m[0][0] = (s[0] == p[0] or p[0]=='*' or p[0]=='?')
        for i in range(ls):
            for j in range(lp):
                #print i,j
                #for mr in m:print mr
                if i > 0 and (m[i-1][j] and p[j]=="*"):
                    m[i][j] = True
                if i>0 and j>0 and m[i-1][j-1] and (p[j] == "?" or p[j] == "*" or s[i] == p[j]):
                    m[i][j] = True
                #if j>0 and m[i][j-1] and (p[j-1]=="*" and (p[j]=="*" or p[j]==s[i])):
                #    m[i][j] = True
                if j>0 and (m[i][j-1] and p[j]=="*"):
                    m[i][j] = True
        return m[ls-1][lp-1]
    
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



