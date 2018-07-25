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
        for i in range(1, lh):
            maxtoleft[i] = max(height[i-1], maxtoleft[i-1])
        for i in range(lh-2, -1, -1):
            #print i
            maxtoright[i] = max(height[i+1], maxtoright[i+1])
        for i in range(1, lh - 1):
            #print i, max(0, min(maxtoright[i], maxtoleft[i]) - height[i])
            total += max(0, min(maxtoright[i], maxtoleft[i]) - height[i])
        #print maxtoright, '\n', maxtoleft, '\n', height
        return total
sol = Solution()
print sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6
print sol.trap([2,3]), 0
print sol.trap([4,2,3]), 1
print sol.trap([4,2, 8, 2, 3]), 3