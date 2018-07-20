# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 22:41:46 2018

@author: cbe117
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = len(nums)
        firstnotchecked = 0
        lastplace = ln - 1
        itocheck = 0
        while itocheck < ln:
            x = nums[itocheck]
            if x > lastplace:
                tx = nums[lastplace]
                nums[lastplace] = x
                nums[itocheck] = tx
                continue
            else: # within range still
        return
sol = Solution()
print sol.firstMissingPositive([1,2,0]), 3
print sol.firstMissingPositive([3,4,-1,1]), 1
print sol.firstMissingPositive([7,8,9,11,12]), 1