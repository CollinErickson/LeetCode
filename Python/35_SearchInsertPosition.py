# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 22:10:44 2018

@author: cbe117
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lennums = len(nums)
        for i in range(lennums):
            if nums[i] >= target:
                return i
        return lennums
c1 = Solution()
print (c1.searchInsert([1,3,5,6], 5), 2)
print (c1.searchInsert([1,3,5,6], 2), 1)
print (c1.searchInsert([1,3,5,6], 7), 4)
print (c1.searchInsert([1,3,5,6], 0), 0)