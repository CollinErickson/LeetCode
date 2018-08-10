# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 20:47:05 2018

@author: cbe117
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #if n < 0: return 1 / self.myPow(x, -n)
        if n == 1: return x
        if n == 0: return 1
        bn = bin(abs(n))[2:]
        tot = 1
        pn = [-1 for i in range(len(bn))]
        for i, v in enumerate(reversed(bn)):
            #print v, i
            if i==0:
                #pn[i] = x
                if n > 0:
                    pn[i] = x
                else:
                    pn[i] = 1./x
            else:
                pn[i] = pn[i-1]**2
            if v=='1':
                tot *= pn[i]
                #if n > 0:
                #    tot *= pn[i]
                #else:
                #    tot /= pn[i]
        return tot

sol = Solution()
print sol.myPow(2., 10), 1024.
print sol.myPow(2.1, 3), 9.26100
print sol.myPow(2., -2), .25
print sol.myPow(2., -2147483648), 0., pow(2., -2147483648)