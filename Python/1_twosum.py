# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 12:55:39 2017

@author: cbe117
"""
import numpy as np
class Solution(object):
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #nums2 = list(nums)
        #nums2.sort()
        #nums2.sort()
        nums = np.asarray(nums)
        nums_order = np.argsort(nums)
        nums2 = nums[nums_order]
        #lnums = len(nums)
        # i = lnums/2
        i = 0
        while nums2[i+1] < target/2:
            i = i+1
        j = i+1
        #print "starting with ", i, j
        #print nums, target
        
        while True:
            ijsum = nums2[i] + nums2[j]
            print i, j, ijsum, target
            if ijsum == target:
                #i_ind = int(np.where(nums_order == i)[0])
                #j_ind = int(np.where(nums_order == j)[0])
                i_ind = nums_order[i]
                j_ind = nums_order[j]
                return [i_ind, j_ind]
                return [i, j]
            elif ijsum > target:
                i -= 1
            else:
                j += 1
            #if i < 0 or j > len(nums):
            #    return 'broke', i, j

sol = Solution()
print sol.twoSum([2,6,45,7,9], 52)
#print sol.twoSum2([2,6,45,7,9], 52)