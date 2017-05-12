# -*- coding: utf-8 -*-
"""
Created on Tue May 02 18:09:28 2017

@author: cbe117
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        #mp = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        #subs = {"M":[2], "D":[2], "C":[4], "L":[4], "X":[6], "V":[6], "I":[]}
        subs = {0:[2], 1:[2], 2:[4], 3:[4], 4:[6], 5:[6], 6:[]}
        nums = [1000, 500, 100, 50, 10, 5, 1]
        chars = ["M", "D", "C", "L", "X", "V", "I"]
        s = ""
        for i in range(len(nums)):
            tnum = num / nums[i]
            for j in range(tnum):
                s += chars[i]
            num = num - tnum * nums[i]
            if i < 6:
                for j in subs[i]:
                    if num + nums[j] >= nums[i] and num > nums[j] and nums[i] > 2*nums[j]:
                        s += chars[j] + chars[i]
                        num = num - nums[i] + nums[j]
        return s
sol = Solution()
print sol.intToRoman(621)
print sol.intToRoman(4)
print sol.intToRoman(5)
print sol.intToRoman(9)
print sol.intToRoman(999)
print sol.intToRoman(45)