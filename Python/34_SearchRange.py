# -*- coding: utf-8 -*-
"""
Created on Sat Jul 07 21:13:23 2018

@author: cbe117
"""
import math
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lennums = len(nums)
        right = -1
        left = lennums
        diff = lennums/2
        # Get left first
        if nums[0] == target:
            left = 0
        else:
            diff = int(math.pow(math.ceil(math.log(lennums/2)), 2))
            ii = diff # lennums / 2 - 1
            while diff >=1:
                diff //= 2
                print diff, ii
                if ii >= lennums:
                    left = -1
                elif nums[ii] <= target:
                    ii += diff
                else:
                    ii -= diff
        return [left, right]
    def binarySearch(self, nums, target):
        pass
sol = Solution()
print sol.searchRange(nums = [5,7,7,8,8,10], target = 8), [3,4]