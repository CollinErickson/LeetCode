# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 20:44:03 2019

@author: cbe117
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # Track where last 0, 1, and 2 are
        l0 = -1
        l1 = -1
        l2 = -1
        
        if len(nums) <= 1:
            return nums
        if nums[0] == 0:
            l0 = 0
        elif nums[0] == 1:
            l1 = 0
        elif nums[0] == 2:
            l2 = 0
        for i in range(1, len(nums)):
            #print('it is', nums, l0, l1, l2)
            if nums[i] == 0: # Need to put before 1 and 2
                if l1 < i and l1 >= 0 and l2 < i and l2 >= 0:
                    nums[l0 + 1] = 0
                    nums[l1 + 1] = 1
                    nums[i]  = 2
                    l0 += 1
                    l1 += 1
                    l2 = i
                elif l1 < i and l1 >= 0:
                    nums[l0 + 1] = 0
                    nums[i]  = 1
                    l0 += 1
                    l1 = i
                elif l2 < i and l2 >= 0:
                    nums[l0 + 1] = 0
                    nums[i]  = 2
                    l0 += 1
                    l2 = i
                else: # Only 0's before
                    l0 = i
            elif nums[i] == 1: # Need to put before 2
                if l2 < i and l2 >= 0:
                    if l1 < 0:
                        l1 = l0
                    nums[l1 + 1] = 1
                    nums[i]  = 2
                    l1 += 1
                    l2 = i
                else: # Only 0's before
                    l1 = i
            elif nums[i] == 2: # Just fine
                # Do nothing
                l2 = i
        return nums
sol = Solution()
print(sol.sortColors([0,2,2,0,0,2,0,2,0]))
print(sol.sortColors([1,1,0,1,1,1,0,0,0,1,0,0,1,0,1,1,1,0]))
print(sol.sortColors([1,1,2,2]))
print(sol.sortColors([1,1,2,2,1,1,2,1,1,2,2,1,2]))
print(sol.sortColors([1,1,2,0,0,2,1,1,2,0,2,0,1]))
print(sol.sortColors([2,0,2,1,1,0]))
print(sol.sortColors([1,0]))
print(sol.sortColors([1,2]))
print(sol.sortColors([2,1]))
print(sol.sortColors([2,0]))
print(sol.sortColors([0,1,0]))
print(sol.sortColors([0,2,0]))