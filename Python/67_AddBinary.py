# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 21:52:57 2019

@author: cbe117
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if (len(a) > len(b)):
            return self.addBinary(b, a)
        i = 0
        out = []
        carry = False
        while True:
            
            if i <= len(a):
                tmp = int(a[len(a) - i - 1]) + int(b[len(a) - i - 1]) + int(carry)
            if tmp>1:
                tmp = 0
                carry = True
            i = i + 1
            if i > len(b):
                break
            out.append(tmp)
        return out
    def addBinary2(self, a, b):
        x = bin(int(a, 2) + int(b, 2))
        return x
sol = Solution()
print(sol.addBinary('11','1'), '100')
print(sol.addBinary('1010','1011'), '10101')