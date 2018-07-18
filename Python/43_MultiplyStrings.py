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
        ta = ["" for i in range(len1 + len2)]
        for a, i in enumerate(reversed(num1)): 
            for b, j in enumerate(reversed(num2)):
                print a,i,b,j, ta
                ij = int(i) * int(j)
                total = str(ij) + total
                sij = str(ij)
                #ta[len1+len2-a-b-1] = str(ij)
                print len(sij), len1+len2-a-b-1
                if len(sij) == 1:
                    sij = " " + sij
                print 'hee', ta[len1+len2-a-b-1]
                if ta[len1+len2-a-b-1] == "":
                    if ij >= 10:
                        ta[len1+len2-a-b-1] = sij[1]
                        ta[len1+len2-a-b-1-1] = sij[0]
                    else:
                        print 'here'
                        ta[len1+len2-a-b-1] = sij
                else: # Already a digit there
                    tb = int(ta[len1+len2-a-b-1])
                    tc = tb + ij
                    if tc >= 10:
                        ta[len1+len2-a-b-1] = str(tc - 10)
                        ta[len1+len2-a-b-1-1] = str(tc // 10)
                    else:
                        ta[len1+len2-a-b-1] = str(tc)
                #else:
                #    # has length two
                #    if 
        print ta
        return "".join(ta)
        #return total
sol = Solution()
#print sol.multiply(num1 = "2", num2 = "3"), "6"
print sol.multiply(num1 = "123", num2 = "456"), "56088"