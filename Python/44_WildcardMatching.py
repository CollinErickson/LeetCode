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
        return
    
sol = Solution()
print sol.isMatch(s = "aa", p = "a"), False
print sol.isMatch(s = "aa", p = "*"), True
print sol.isMatch(s = "cb", p = "?a"), False
print sol.isMatch(s = "abceb", p = "a*b"), True
print sol.isMatch(s = "acdcb", p = "a*c?b"), False