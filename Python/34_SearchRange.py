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
        # dumb cases
        if lennums == 0:
            return [-1,-1]
        if lennums == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        # Get left first
        if nums[0] > target or nums[lennums-1] < target:
            return [-1,-1]
        if nums[0] == target:
            left = 0
        else:
            leftlower = 0
            leftupper = lennums - 1
            while leftlower < leftupper:
                if leftupper - leftlower == 1:
                    break
                tempind = leftlower + (leftupper - leftlower) // 2
                if nums[tempind] < target:
                    leftlower = tempind
                else:
                    leftupper = tempind
            if nums[leftupper] == target:
                left = leftupper
            else:
                left = -1
        if nums[lennums-1] == target:
            right = lennums - 1
        else:
            rightlower = left
            rightupper = lennums - 1
            while rightlower < rightupper:
                #print "right", rightlower, rightupper
                if rightupper - rightlower == 1:
                    break
                tempind = rightlower + (rightupper - rightlower) // 2
                if nums[tempind] > target:
                    rightupper = tempind
                else:
                    rightlower = tempind
            if nums[rightlower] == target:
                right = rightlower
            else:
                right = -1
        return [left, right]
sol = Solution()
print sol.searchRange(nums = [5,7,7,8,8,10], target = 8), [3,4]
print sol.searchRange(nums = [5,7,7,8,8,10], target = 6), [-1,-1]
print sol.searchRange(nums = [5,7,7,8,8,10], target = 7), [1,2]
print sol.searchRange(nums = [5,7,7,8,8,10], target = 10), [5,5]
print sol.searchRange(nums = [5,7,7,8,8,10], target = 4), [-1,-1]
print sol.searchRange(nums = [5,7,7,8,8,10], target = 11), [-1,-1]
print sol.searchRange(nums = [5,7,7,8,8,10], target = 3), [-1,-1]
print sol.searchRange(nums = [], target = 0), [-1,-1]
print sol.searchRange(nums = [0], target = 0), [0,0]
print sol.searchRange(nums = [1], target = 0), [-1,-1]
print sol.searchRange(nums = [0,0], target = 0), [0,1]
print sol.searchRange(nums = [0,1], target = 0), [0,0]
print sol.searchRange(nums = [-1,0], target = 0), [1,1]
print sol.searchRange(nums = [1,2], target = 0), [-1,-1]