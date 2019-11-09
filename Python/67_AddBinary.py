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
        carry = 0
        while True:
            if i < len(a):
                #print('first', len(a) - i - 1, i, int(a[len(a) - i - 1]), int(b[len(b) - i - 1]), int(carry))
                tmp = int(a[len(a) - i - 1]) + int(b[len(b) - i - 1]) + int(carry)
            else:
                #print(i, int(b[len(a) - i - 1]), int(carry))
                tmp = int(b[len(b) - i - 1]) + int(carry)
                #print('temp', tmp, tmp //2, tmp%2, out)
            if tmp>1:
                carry = tmp // 2
                tmp = tmp % 2
            else:
                carry = 0
            i = i + 1
            out.append(tmp)
            if i >= len(b):
                break
        #print('postadd', carry, tmp)
        if carry > 0:
            out.append(carry)
        out.reverse()
        out = ('').join([str(a) for a in out])
        return out
    def addBinary2(self, a, b):
        x = bin(int(a, 2) + int(b, 2))
        return x
sol = Solution()
print(sol.addBinary('11','1'), '100')
print(sol.addBinary('1010','1011'), '10101')
print(sol.addBinary('1111','1111'), '11110')
print(sol.addBinary('100','110010'), '110110')