# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 21:45:37 2019

@author: cbe117
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        x = ''.join([str(i) for i in digits])
        y = [int(i) for i in str(int(x)+1)]
        return y

sol = Solution()
print(sol.plusOne([1,2,3]))
print(sol.plusOne([9,9,9]))