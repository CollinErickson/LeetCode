# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 21:33:11 2018

@author: cbe117
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lh = len(height)
        if lh <= 2: return 0
        maxtoright = [0 for i in range(lh)]
        maxtoleft  = [0 for i in range(lh)]
        total = 0
        for i in range(lh):
            pass
        for i in range(lh):
            pass
        for i in range(1, lh - 2)
        
        return
sol = Solution()
print sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6