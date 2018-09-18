# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 22:24:52 2018

@author: cbe117
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cursum = 0
        maxcursum = nums[0]
        for i in nums:
            cursum += i
            maxcursum = max(maxcursum, cursum)
            if cursum < 0:
                cursum = 0
        return maxcursum
    
sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
print(sol.maxSubArray([-1]), -1)
print(sol.maxSubArray([-1, -1]), -1)
print(sol.maxSubArray([-1,0]), 0)