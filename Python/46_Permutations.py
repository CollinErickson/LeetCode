# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 10:31:16 2018

@author: cbe117
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1: return [nums]
        #print nums
        #p = [[[n] + m for m in self.permute([p for p in nums if p is not n])] for n in nums]
        #p = [[n] + m for n, in nums]
        p = []
        for n in nums:
            #print n, self.permute([q for q in nums if q is not n])
            #continue
            for m in self.permute([q for q in nums if q is not n]):
                #break
                #print n, m, [n]+m
                p.append([n]+m)
        return p

sol = Solution()
if True:
    print sol.permute([1,2,3]), '\n', [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
if True: print sol.permute([1,2,3,4])
print sol.permute([1,2])
print sol.permute([1])
