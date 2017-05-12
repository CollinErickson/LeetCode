# -*- coding: utf-8 -*-
"""
Created on Sat May 06 23:16:18 2017

@author: cbe117
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sum2_inds = {}
        lennums = len(nums)
        for i in range(lennums-1):
            a = nums[i]
            for j in range(i+1, lennums):
                b = nums[j]
                c = a + b
                if c in sum2_inds:
                    sum2_inds[c] = sum2_inds[c] + [[i, j]]
                else:
                    sum2_inds[c] = [[i, j]]
        pairs = []
        sol_dic = {}
        for i in range(lennums-1):
            a = nums[i]
            for j in range(i+1, lennums):
                b = nums[j]
                tar = target - a - b
                if tar in sum2_inds:
                    for p in sum2_inds[tar]:
                        #if i != p[0] and i != p[1] and j != p[0] and j != p[1]:
                        if j < p[0]:
                            sol = [a, b, nums[p[0]], nums[p[1]]]
                            sol.sort()
                            sol_tuple = tuple(sol)
                            #inds.sort()
                            #inds = tuple(inds)
                            if sol_tuple not in sol_dic:
                                pairs.append(sol)
                                sol_dic[tuple(sol)] = True
                                
        #print sum2_inds
        return pairs
sol = Solution()
print sol.fourSum([1,1,2,-1,-1,-2, 0], 0)
print sol.fourSum([1,1,2,-1,-1,-2], 11)