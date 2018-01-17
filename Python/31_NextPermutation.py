# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 22:08:12 2018

@author: cbe117
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lennums = len(nums)
        if lennums <= 1:
            return
        if lennums == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return
        for i in range(lennums-2, -1, -1):
            R = nums[i+1]
            L = nums[i]
            if L < R:
                #print L, R
                minrightofL = R
                indexofmroL = i+1
                for j in range(i+1, lennums):
                    if nums[j] > L and nums[j] < minrightofL:
                        minrightofL = nums[j]
                        indexofmroL = j
                nums[i], nums[indexofmroL] = nums[indexofmroL], nums[i]
                #print 'before', nums
                if indexofmroL+1 <= lennums - 1:
                    for j in range(indexofmroL, lennums-1):
                        if nums[j] < nums[j+1]:
                            nums[j], nums[j+1] = nums[j+1], nums[j]
                #print 'after ', nums
                for j in range(i+1, lennums):
                    k = lennums + i - j
                    #print j,k
                    if k <= j:
                        break
                    if nums[j] < nums[k]:
                        break
                    nums[j], nums[k] = nums[k], nums[j]
                    
                return
        else:
            nums.reverse()
        return

ll = [2,3,1,3,3] #[1,3,2]
print ll
sol = Solution()
sol.nextPermutation(ll)
print ll
print [2,3,3,1,3]

ll = [2,1,2,2,2,2,2,1] #[1,3,2]
print ll
sol = Solution()
sol.nextPermutation(ll)
print ll
print [2,2,1,1,2,2,2,2]

ll = [3,4,1,4,3,3] #[1,3,2]
print ll
sol = Solution()
sol.nextPermutation(ll)
print ll
print [3,4,3,1,3,4]