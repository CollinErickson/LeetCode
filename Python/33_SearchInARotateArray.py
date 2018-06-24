# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 20:22:23 2018

@author: cbe117
"""

import math

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lennums = len(nums)
        if lennums == 0:
            return -1
        if lennums == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        # Find switch point with binary search
        a = int(math.log(lennums, 2))
        i = lennums / 2
        while a > 0:
            a /= 2
            if nums[i] > nums[i+1]:
                stop
            
        if nums[lennums / 2] < nums[0]:
            if target >= nums[0] or target < nums[lennums / 2]:
                return self.search(nums[0:(lennums/2)], target)
            else:
                return self.binary(nums[(lennums/2):lennums], target)
        else:
            if target >= nums[0] and target < nums[lennums / 2]:
                return self.binary(nums[0:(lennums/2)], target)
            else:
                return self.search(nums[(lennums/2):lennums], target)
        return "error"
    def binary(self, nums, target):
        pass
sol = Solution()
print (sol.search([4,5,6,7,0,1,2], 0))