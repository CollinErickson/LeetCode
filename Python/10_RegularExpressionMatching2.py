# -*- coding: utf-8 -*-
"""
Created on Fri May 12 15:11:38 2017

@author: cbe117
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:16:17 2017

@author: cbe117
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #print "starting with", s, "_", p
        lens = len(s)
        lenp = len(p)
        
        if lens==0 and lenp==0:
            return True
        
        if lens == 0:
            if lenp%2 != 0:
                return False
            for jj in range(1, lenp, 2):
                if p[jj] != "*":
                    return False
        if lenp == 0:
            return False
        
        starcheck = False
        if lenp > 1:
            if p[1] == "*":
                starcheck = True
        if starcheck:
            if p[0] == ".":
                for k in range(lens+1):
                    if self.isMatch(s[k:], p[2:]):
                        return True
                else:
                    return False
            else: 
                for k in range(lens):
                    if self.isMatch(s[k:], p[2:]):
                        return True
                    if s[k] != p[0]:
                        return False
                else:
                    if self.isMatch("", p[2:]):
                        return True
        elif p[0] == ".":
            return self.isMatch(s[1:], p[1:])
        elif s[0] == p[0]:
            return self.isMatch(s[1:], p[1:])
        #print "Shouldn't be here?", s, "_", p
        return False

sol = Solution()
print sol.isMatch("aa","a"), False
print sol.isMatch("aa","aa"), True
print sol.isMatch("aaa","aa"), False
print sol.isMatch("aa","a*"), True
print sol.isMatch("aa", ".*"), True
print sol.isMatch("ab", ".*"), True
print sol.isMatch("aab", "c*a*b"), True
print sol.isMatch("abcde", ".*de"), True
print sol.isMatch("ab", ".*c"), False
print sol.isMatch("aaa", "a*a"), True
print sol.isMatch("a", "ab*"), True
print sol.isMatch("a", "ab*c*d*"), True
print sol.isMatch("aef", "ab*c*d*ef"), True
print sol.isMatch("bbbba", ".*a*a"), True
print sol.isMatch("a", ".*..a*"), False
print sol.isMatch("acaabbaccbbacaabbbb", "a*.*b*.*a*aa*a*"), False