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
        
        if lens == 0:
            if lenp%2 != 0:
                return False
            for jj in range(1, lenp, 2):
                if p[jj] != "*":
                    return False
        
        i = 0
        j = 0
        while True:
            if i >= lens:
                break
            if j >= lenp:
                break
            print i, j, s[i:], p[j:]
            if j < lenp - 1:
                if p[j+1] == "*":
                    if p[j] == ".":
                        kcount = 0
                        for k in range(lens - i):
                            if lenp == j+2:
                                return True
                            if s[i+k] == p[j+2]:
                                break
                            kcount += 1
                        i += kcount
                        j += 2
                        continue
                    else:
                        kcount = 0
                        for k in range(lens - i):
                            if s[i+k] != p[j]:
                                break
                            checkmatch = self.isMatch(s[(i+k):], p[(j+2):])
                            if checkmatch:
                                return True
                            kcount += 1
                        i += kcount
                        j += 2
                        continue
            if p[j] == ".":
                i += 1
                j += 1
                continue
            if s[i] == p[j]:
                i += 1
                j += 1
                continue
            return False
        if i < lens:
            #print "i under"
            return False
        if j < lenp:
            #print "j under"
            if (lenp-j) %2 == 0:
                for jj in range(j+1, lenp, 2):
                    if p[jj] == "*":
                        return True
            return False
        return True
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