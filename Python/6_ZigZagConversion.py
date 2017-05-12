# -*- coding: utf-8 -*-
"""
Created on Tue May 09 17:46:58 2017

@author: cbe117
"""
import math
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lens = len(s)
        if lens == 0:
            return ""
        if numRows == 1:
            return s
        groupsize = 2*numRows - 2
        numgroups = int(math.ceil(1. *lens / groupsize)) #group[-1]
        #print numgroups
        a = ["" for i in range(lens)]
        
        b = 0
        i = 0
        for b in range(numRows):
            for g in range(numgroups):
                #print b, g, numgroups
                if b==0:
                    a[i] = s[g*groupsize]
                elif b == numRows - 1:
                    ind = g*groupsize + numRows - 1
                    if ind >= lens:
                        break
                    a[i] = s[ind]
                else:
                    ind1 = g*groupsize + b
                    if ind1 >= lens:
                        break
                    a[i] = s[ind1]
                    i += 1
                    ind2 = g*groupsize + groupsize - b
                    if ind2 >= lens:
                        break
                    a[i] = s[ind2]
                    
                    pass
                i+=1
        return "".join(a)
sol = Solution()
print sol.convert("0123456789", 3)
print sol.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"
print sol.convert("abc", 10)
print sol.convert("", 1)