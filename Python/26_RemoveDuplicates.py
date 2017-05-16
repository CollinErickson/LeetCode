# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:56:07 2017

@author: cbe117
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lnums = len(nums)
        if lnums <= 1:
            return lnums
        if lnums == 2:
            if nums[0] == nums[1]:
                return 1
            return 2
        lastunique = nums[0]
        nextindex = 1
        for i in range(1, lnums):
            numsi = nums[i]
            if numsi != lastunique:
                if i > nextindex:
                    nums[nextindex] = nums[i]
                
                nextindex += 1
                lastunique = numsi
        return nextindex
sol = Solution()
print sol.removeDuplicates([])
print sol.removeDuplicates([1])
print sol.removeDuplicates([1,2,3,4,5,6])
print sol.removeDuplicates([1,2,3,4,4, 5])
print sol.removeDuplicates([1,2,2, 2, 2, 2, 3, 3, 3, 3,3,4,4,5, 5, 5, 5,5,6])
print sol.removeDuplicates([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4])