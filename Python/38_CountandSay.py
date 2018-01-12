# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:45:42 2018

@author: cbe117
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return None
        if n == 1:
            return "1"
        i = 1
        istr = str(i)
        while i < n:
            #print(i, n)
            #istr = str(i)
            inext = ""
            while len(istr) > 0:
                #print(istr)
                i0 = istr[0]
                tc = 1
                while tc < len(istr):
                    if istr[tc] == i0:
                        tc += 1
                    else:
                        break
               # print(i, tc, i0, istr)
                istr = istr[tc:len(istr)]
                inext += str(tc) + i0
            i += 1
            istr = inext
        return inext
        
print Solution().countAndSay(0), None
print Solution().countAndSay(1), 1
print Solution().countAndSay(2), 11
print Solution().countAndSay(3), 21
print Solution().countAndSay(4), 1211
print Solution().countAndSay(5), 111221
