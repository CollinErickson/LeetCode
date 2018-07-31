# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 09:13:42 2018

@author: cbe117
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = len(nums)
        if ln <= 1: return 0
        jumps = 0
        pos = 0
        maxjump = 0
        for i in range(ln-1):
            maxjump = max(maxjump, i + nums[i])
            if i == pos:
                pos = maxjump
                jumps += 1
        return jumps
    def jump2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = len(nums)
        if ln<=1:return 0
        x = [ln+10 for i in nums]
        x[ln-1] = 0
        mtr = [ln+10 for i in nums]
        mtr[ln-1] = 0
        for i in reversed(range(ln-1)):
            #print i
            for j in reversed(range(i+1, min(i+nums[i]+1, ln))):
                #print i,j
                x[i] = min(x[i], 1 + x[j])
                if x[i] <= 1 + mtr[i+1]:
                    #print 'breaking'
                    break
            mtr[i] = min(x[i], mtr[i+1])
        return x[0]
    
sol = Solution()
print sol.jump([2,3,1,1,4]), 2
print sol.jump([2,1]), 1
print sol.jump(list(reversed(range(2501)))), 1