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
        if ln == 1:
            return 2 if nums[0] == 1 else 1
        firstnotchecked = 0
        lastplace = ln - 1
        itocheck = 0
        while itocheck <= lastplace:
            #print itocheck, nums, firstnotchecked, lastplace
            x = nums[itocheck]
            if x > lastplace or x < 1 or (x!=itocheck+1 and nums[x-1] == x):
                #print 'c1'
                tx = nums[lastplace]
                nums[lastplace] = x
                nums[itocheck] = tx
                lastplace -= 1
                continue
            elif x == itocheck + 1:
                #print 'c2'
                itocheck += 1
            else: # within range still
                #print 'c3'
                tx = nums[x - 1]
                nums[x-1] = x
                nums[itocheck] = tx
        return itocheck + 1
sol = Solution()
print sol.firstMissingPositive([1,2,0]), 3
print sol.firstMissingPositive([3,4,-1,1]), 2
print sol.firstMissingPositive([7,8,9,11,12]), 1
print sol.firstMissingPositive([2]), 1
print sol.firstMissingPositive([1]), 2
print sol.firstMissingPositive([1,2,3]), 3
print sol.firstMissingPositive([5,6,3,1,2,32]), 3
print sol.firstMissingPositive([5,6,3,1,2,3,4]), 7