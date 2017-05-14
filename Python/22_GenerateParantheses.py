# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:46:47 2017

@author: cbe117
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        n = 2*n
        if n == 0:
            return []
        a = [[1]]
        for i in range(1, n):
            #print a
            b = a
            a = []
            for c in b:
                #print "c is", c, c[-1], a
                if c[-1] > 0:
                    a.append(c + [c[-1]-1])
                    #print "added one", a
                if c[-1] - (n-i) < 0:
                    a.append(c + [c[-1] + 1])
        return [self.mapNumsToPars(i, n) for i in a]
    def mapNumsToPars(self, p, n):
        return "".join(["("] + ["(" if p[i+1] > p[i] else ")" for i in range(n-1)])
sol = Solution()
print sol.generateParenthesis(3)