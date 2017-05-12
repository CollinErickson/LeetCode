# -*- coding: utf-8 -*-
"""
Created on Tue May 02 16:48:20 2017

@author: cbe117
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ns = nums
        ns.sort()
        lns = len(ns)
        best_diff = abs(ns[0] + ns[1] + ns[2] - target)
        best_val = ns[0] + ns[1] + ns[2]
        for i in range(lns - 2):
            j = i + 1
            k = lns-1
            while j < k:
                if i==j:
                    j += 1
                elif i == k:
                    k -= 1
                else:
                    tar = ns[i] + ns[j] + ns[k]
                    #print i, j, k, tar
                    tardiff = abs(tar - target)
                    if tardiff < best_diff:
                        best_diff = tardiff
                        best_val = tar
                    if tar < target:
                        j += 1
                    elif tar > target:
                        k -= 1
                    else:
                        return tar
                #print i, j, k
        return best_val
sol = Solution()
print sol.threeSumClosest([1,3,5,7], 6)