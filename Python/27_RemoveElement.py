# -*- coding: utf-8 -*-
"""
Created on Tue May 16 18:34:37 2017

@author: cbe117
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        lnums = len(nums)
        if lnums == 0:
            return 0
        for i in range(lnums ):
            if i + count >= lnums:
                #print "breaking", i, count, nums
                return lnums - count#, nums
            #print i, nums[i]
            while nums[i] == val:
                #print i, count, nums
                #nums[count] = nums[i]
                #nums[i] = val
                nums[i:(lnums-1)] = nums[(i+1):lnums]
                nums[lnums-1] = val
                count += 1
                if i + count >= lnums:
                    #print "breaking", i, count, nums
                    return lnums - count#, nums
            #print i, nums[i], "after"
            #print nums
        #print "made it to end"
        return lnums - count#, nums
sol = Solution()
print sol.removeElement([], 3)
print sol.removeElement([3,2,2,3, 1, 2, 3, 4, 5, 6, 4, 3], 3)
print sol.removeElement([3,2,2,3, 4, 5, 3, 2, 3, 2, 1, 3, 3, 4], 3)
print sol.removeElement([3,2,2,3, 4, 5, 3, 2, 3, 2, 1, 3, 3, 4, 3, 3, 3, 3, 3, 7, 8], 3), 10
print sol.removeElement([1, 2, 4, 5], 3), 4
print sol.removeElement([3, 3, 3, 3], 3), 0
print sol.removeElement([3, 3, 3, 3, 1], 3), 1