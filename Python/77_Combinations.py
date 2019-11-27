# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 22:54:46 2019

@author: cbe117
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[i+1] for i in range(n)]
        s = self.combine(n, k-1)
        u = []
        #print('s is', s)
        for t in s:
            if t[-1] < n:
                for a in range(t[-1] + 1, n+1):
                    tx = t[:]
                    tx.append(a)
                    u.append(tx)
        return u
        
        s = []
        x = [1 + i for i in range(k)]
        s.append(x)
        while True:
            i = n - 1
            
            break
        return s
sol = Solution()
print(sol.combine(4,2), '\n', [
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
])
print(sol.combine(5, 1))
print(sol.combine(5, 4))