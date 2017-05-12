# -*- coding: utf-8 -*-
"""
Created on Tue May 09 10:47:07 2017

@author: cbe117
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lstrs = len(strs)
        if lstrs == 0:
            return ""
        if lstrs == 1:
            return strs[0]
        lenstrs = [len(s) for s in strs]
        minlenstrs = min(lenstrs)
        for i in range(minlenstrs):
            #print i, p
            m = strs[0][i]
            for j in range(1, lstrs):
                if strs[j][i] != m:
                    return strs[0][0:i]
            
        return strs[0][0:minlenstrs]
    def longestCommonPrefixWorksButSlow(self, strs):
        p = ""
        lstrs = len(strs)
        if lstrs == 0:
            return ""
        if lstrs == 1:
            return strs[0]
        lenstrs = [len(s) for s in strs]
        for i in range(min(lenstrs)):
            #print i, p
            m = strs[0][i]
            for j in range(1, lstrs):
                if strs[j][i] != m:
                    return p
            p += m
        return p
                
sol = Solution()
print sol.longestCommonPrefix([])
print sol.longestCommonPrefix(["abc"])
print sol.longestCommonPrefix(["abc", "abcd"])
print sol.longestCommonPrefix(["abc", "bcd"])
print sol.longestCommonPrefix(["a", "b"])