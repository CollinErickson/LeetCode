# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 21:28:50 2018

@author: cbe117
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        maxpos = 0
        for i in range(l):
            if i > maxpos:
                return False
            maxpos = max(maxpos, i + nums[i])
        
        return True
    
sol = Solution()
print(sol.canJump([2,3,1,1,4]), True)
print(sol.canJump([3,2,1,0,4]), False)
print(sol.canJump([2]), True)