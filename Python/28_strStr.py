# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:29:58 2017

@author: cbe117
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lhay = len(haystack)
        lnee = len(needle)
        if lnee == 0:
            return 0
        if lhay == 0:
            return -1
        i = 0
        j = 0
        while i < lhay:
            print i, j, haystack[i] , needle[j]
            if haystack[i] == needle[j]:
                j += 1
                i += 1
                if j == lnee:
                    return i - lnee
            else:
                i += 1 - j
                j = 0
            if i == lhay:
                return -1
            
sol = Solution()
print sol.strStr("bcdefg", "g")
print sol.strStr("", "")
print sol.strStr("mississippi", "issip")
print sol.strStr("ililp", "ilp")