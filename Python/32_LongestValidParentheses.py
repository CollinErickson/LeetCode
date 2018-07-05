# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 17:28:45 2018

@author: cbe117
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        print s
        if len(s) <= 1:
            return 0
        for i in range(len(s)-1):
            if s[i] == "(" and s[i+1] == ")":
                return 1 + self.longestValidParentheses(s[0:i] + s[(i+2):len(s)])
        return 0
sol = Solution()
print sol.longestValidParentheses("(())"), 2
print sol.longestValidParentheses(")()())"), 4
