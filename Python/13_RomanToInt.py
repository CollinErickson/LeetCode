# -*- coding: utf-8 -*-
"""
Created on Tue May 02 17:51:16 2017

@author: cbe117
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mp = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        nums = [mp[s[i]] for i in range(len(s))]
        a1 = [nums[i] * ((nums[i] >= nums[i+1])*2-1) for i in range(len(s)-1)]
        return sum(a1) + nums[-1]
sol = Solution()
print sol.romanToInt("DCXXI")
print sol.romanToInt("MCMXCVI")