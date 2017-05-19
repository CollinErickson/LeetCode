# -*- coding: utf-8 -*-
"""
Created on Wed May 17 19:59:10 2017

@author: cbe117
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = False
        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = - divisor
        elif dividend < 0:
            neg = True
            dividend = - dividend
        elif divisor < 0:
            neg = True
            divisor = - divisor
        ans = 0
        while dividend >= divisor:
            tsor = divisor
            tt = 1
            while True:
                if tsor + tsor <= dividend:
                    tt = tt + tt
                    tsor = tsor + tsor
                else:
                    break
            #print dividend, tt, tsor, ans
            ans += tt
            dividend -= tsor
        if neg:
            ans = -ans
        if ans > 2147483647:
            return 2147483647
        if ans < -2147483648:
            return -2147483648
        return ans
sol = Solution()
print sol.divide(13,4)
print sol.divide(13,40)
print sol.divide(13,-4)
print sol.divide(-13,4)
print sol.divide(-13,-4)
print sol.divide(12,4)
print sol.divide(-2147483648,-1)
print sol.divide(120,4)