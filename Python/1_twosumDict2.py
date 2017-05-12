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
        target2 = target / 2
        for i in range(len(nums)):
            numsi = nums[i]
            if numsi == target2:
                if numsi in d:
                    d[numsi] = [d[numsi], i]
                else:
                    d[numsi] = i
            else:
                d[numsi] = i
        #print d
        for i in nums:
            if i == target2:
                if not isinstance(d[i], int):
                    return d[i][0:2]
            elif (target - i) in d:
                return [d[i], d[target - i]]
        return "error"

sol = Solution()
print sol.twoSum([2,6,45,7,9], 52)
print sol.twoSum([3,2, 3], 6)
print sol.twoSum([3,2, 4], 6)