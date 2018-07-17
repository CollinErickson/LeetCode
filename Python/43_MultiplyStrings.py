# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 23:02:24 2018

@author: cbe117
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        total = ""
        for i in reversed(num1):
            
            for j in reversed(num2):
                ij = int(i) * int(j)
                total = str(ij) + total
        return total
sol = Solution()
print sol.multiply(num1 = "2", num2 = "3"), "6"
print sol.multiply(num1 = "123", num2 = "456"), "56088"