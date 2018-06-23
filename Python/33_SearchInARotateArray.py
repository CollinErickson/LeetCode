# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 20:22:23 2018

@author: cbe117
"""

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
        if nums[lennums] < nums[0]:
            pass
        
        return
sol = Solution()
print (sol.search([4,5,6,7,0,1,2], 0))