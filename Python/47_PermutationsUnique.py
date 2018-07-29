# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 11:13:11 2018

@author: cbe117
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1: return [nums]
        #print nums
        #p = [[[n] + m for m in self.permute([p for p in nums if p is not n])] for n in nums]
        #p = [[n] + m for n, in nums]
        p = []
        #numsunique = list(set(nums))
        numsfirst = {}
        for i,n in enumerate(nums):
            numsfirst[n] = i
        #print numsfirst
        for n in numsfirst:# range(len(numsunique)):
            #print n
            i = numsfirst[n]#n = numsunique[i]
            #print n, self.permuteUnique([q for j,q in enumerate(nums) if j!=i])
            for m in self.permuteUnique([q for j,q in enumerate(nums) if j!=i]):
                #print n, m, [n]+m
                p.append([n]+m)
        return p
sol = Solution()
print sol.permuteUnique([1])
print sol.permuteUnique([1,1])
print sol.permuteUnique([1,2,1])
print sol.permuteUnique([1,1,2])
print sol.permuteUnique([1,1,1,2])
print sol.permuteUnique([1,1,2,2])