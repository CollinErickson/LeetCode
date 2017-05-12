# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 21:41:52 2017

@author: cbe117
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_s = sorted((e,i) for i,e in enumerate(nums))
        i = 0
        while nums_s[i+1][0] < target/2:
            i = i+1
        j = i+1
        
        if j + 1 < len(nums):
            if nums_s[j][0] + nums_s[j+1][0] == target:
                return [nums_s[j][1], nums_s[j+1][1]]
        
        while True:
            ijsum = nums_s[i][0] + nums_s[j][0]
            if ijsum == target:
                return [nums_s[i][1], nums_s[j][1]]
            elif ijsum > target:
                i -= 1
            else:
                j += 1

sol = Solution()
print sol.twoSum([2,6,45,7,9], 52)
print sol.twoSum([3,2, 3], 6)