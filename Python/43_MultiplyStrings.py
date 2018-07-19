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
        len1 = len(num1)
        len2 = len(num2)
        ta = ["0" for i in range(len1 + len2)]
        for a, i in enumerate(reversed(num1)): 
            for b, j in enumerate(reversed(num2)):
                #print a,i,b,j, ta
                ij = int(i) * int(j)
                total = str(ij) + total
                sij = str(ij)
                #ta[len1+len2-a-b-1] = str(ij)
                #print len(sij), len1+len2-a-b-1
                if len(sij) == 1:
                    sij = " " + sij
                #print 'hee', ta[len1+len2-a-b-1]
                if ta[len1+len2-a-b-1] == "":
                    #if ij >= 10:
                    ta[len1+len2-a-b-1] = sij[1]
                    ta[len1+len2-a-b-1-1] = sij[0]
                    #else:
                    #    print 'here'
                    #    ta[len1+len2-a-b-1] = sij
                else: # Already a digit there
                    tb = int(ta[len1+len2-a-b-1])
                    tc = tb + ij
                    #if tc >= 10:
                    ta[len1+len2-a-b-1] = str(tc % 10)
                    # ta[len1+len2-a-b-1-1] = str(tc // 10)
                    if ta[len1+len2-a-b-1-1] == "0":
                        ta[len1+len2-a-b-1-1] = str(tc // 10)
                    else:
                        #print 'fix here'
                        kk = 0
                        td = tc // 10
                        while td != "0": #ta[len1+len2-a-b-1-1 - kk] != "0":
                            te = int(ta[len1+len2-a-b-1-1 - kk]) + int(td)
                            ta[len1+len2-a-b-1-1 - kk] = str(te % 10)
                            td = str(te // 10)
                            kk += 1
                    #else:
                    #    ta[len1+len2-a-b-1] = str(tc)
                #else:
                #    # has length two
                #    if 
        #print ta
        for i in range(len(ta) - 1):
            if ta[i] != "0":
                return "".join(ta[i:])
        return "".join(ta[-1])
        #return total
sol = Solution()
print sol.multiply(num1 = "2", num2 = "3"), "6"
print sol.multiply(num1 = "123", num2 = "456"), "56088"
print sol.multiply(num1 = "0", num2 = "0"), "0"
print sol.multiply(num1 = "0", num2 = "7"), "0"