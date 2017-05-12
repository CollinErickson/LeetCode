# -*- coding: utf-8 -*-
"""
Created on Tue May 02 11:19:02 2017

@author: cbe117
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        d = {}
        for i in range(len(nums)):
            numsi = nums[i]
            if numsi in d:
                d[numsi] = d[numsi] + [i]
            else:
                d[numsi] = [i]
        #print d
        solns = []
        for i in range(len(nums) - 1):
            a = nums[i]
            if i != d[a][0]:
                continue
            for j in range(i+1, len(nums)):
                b = nums[j]
                if a != b and j != d[b][0]:
                    continue
                c = -a - b
                if c == a and c == b:
                    if len(d[c]) >= 3:
                        if i == d[c][0] and j == d[c][1]:
                            solns += [[a, b, c]]
                elif c == a:
                    if len(d[c]) >= 2:
                        if i == d[c][0]:
                            solns += [[a, b, c]]
                elif c == b:
                    if len(d[c]) >= 2:
                        if j == d[c][0]:
                            solns += [[a, b, c]]
                elif a == b:
                    pass
                else:
                    if c in d:
                        #print d[a], d[b], d[c], j, d[c] > j
                        #for dc in d[c]:
                        if d[c][0] > j:
                            solns += [[a, b, c]]

        return solns

sol = Solution()
print sol.threeSum([2,6,45,7,9])
print sol.threeSum([3,2, 3, 3])
print sol.threeSum([3,2, 4])
print sol.threeSum([3,2, 4, -1, -3, -3])
print sol.threeSum([3,2, 4, -1, -3, -3, -1, 2, -4])
print sol.threeSum([-1, 0, 1, 2, -1, -4])
print sol.threeSum([-1, 0, 1, 2, -1, 0, 0, -4])
print sol.threeSum([1, 1, -2])
print sol.threeSum([1, -1, -1, 0])
print sol.threeSum([1, 1, -1, -1, 0, 1, 1, -1, -1, 0, 0, -2])
print sol.threeSum([82597,-9243,62390,83030,-97960,-26521,-61011,83390,-38677,12333,75987,46091,83794,19355,-71037,-6242,-28801,324])
