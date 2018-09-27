# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 21:20:46 2018

@author: cbe117
"""
import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        return "".join([str(i) for i in self.getPermutation2(n,k)])
    def getPermutation2(self, n,k):
        if n == 1: return [1]
        #print(n,k)
        m = math.factorial(n-1)
        p = (k-1) // m + 1
        return [p] + [i + (i>=p) for i in self.getPermutation2(n-1, k - (p-1)*m)]
        return [p, (n-1, k - (p-1)*m)]

sol = Solution()
print(sol.getPermutation(3,3), '213')
print(sol.getPermutation(4,9), '2314')
print(sol.getPermutation(3,2), '132')