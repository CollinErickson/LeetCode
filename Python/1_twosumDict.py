# -*- coding: utf-8 -*-
"""
Created on Tue May 02 10:57:59 2017

@author: cbe117
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            if nums[i] == target / 2:
                if nums[i] in d:
                    d[nums[i]] = [d[nums[i]], i]
                else:
                    d[nums[i]] = i
            else:
                d[nums[i]] = i
        #print d
        for i in nums:
            if i == target / 2:
                if not isinstance(d[i], int):
                    return d[i][0:2]
            elif (target - i) in d:
                return [d[i], d[target - i]]
        return "error"

sol = Solution()
print sol.twoSum([2,6,45,7,9], 52)
print sol.twoSum([3,2, 3], 6)
print sol.twoSum([3,2, 4], 6)