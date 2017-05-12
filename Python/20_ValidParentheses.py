# -*- coding: utf-8 -*-
"""
Created on Tue May 09 14:17:38 2017

@author: cbe117
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lens = len(s)
        q = []
        front = ["(", "[", "{"]
        back = [")", "]", "}"]
        for i in range(lens):
            qi = s[i]
            if qi in front:
                q.append(qi)
            if qi in back:
                if len(q) == 0:
                    return False
            if qi == ")":
                pi = q.pop()
                if pi != "(":
                    return False
            if qi == "]":
                pi = q.pop()
                if pi != "[":
                    return False
            if qi == "}":
                pi = q.pop()
                if pi != "{":
                    return False
        if len(q) > 0:
            return False
        return True
sol = Solution()
print sol.isValid("[")
print sol.isValid("()")
print sol.isValid("()[]{}")
print sol.isValid("(]")
print sol.isValid("]")