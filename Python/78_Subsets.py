# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 21:18:41 2019

@author: cbe117
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[i+1] for i in range(n)]
        s = self.combine(n, k-1)
        u = []
        #print('s is', s)
        for t in s:
            if t[-1] < n:
                for a in range(t[-1] + 1, n+1):
                    tx = t[:]
                    tx.append(a)
                    u.append(tx)
        return u
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        s = [[]]
        
        for i in range(1, len(nums) + 1):
            t = self.combine(len(nums), i)
            for u in t:
                #s.append(t)
                s.append([nums[j-1] for j in u])
        
        return s
sol = Solution()
print(sol.subsets([3]))
print(sol.subsets([1,2,3]))
print(sol.subsets([3,5,7,112]))