# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 21:17:25 2019

@author: cbe117
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if (len(heights) == 0):
            return 0
        maxarea = 0
        st = []
        for i in range(len(heights)):
            h = heights[i]
            if len(st) == 0:
                st.append(heights[i])
            else:
                width = 0
                print(st)
                while (len(st) > 0) and st[-1] >= heights[i]:
                    width += 1
                    p = st.pop()
                    area = width * p
                    maxarea = max(maxarea, area)
        return maxarea
    def largestRectangleAreaSlow(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxarea = 0
        for l in range(len(heights)):
            lowest = heights[l]
            for r in range(l+1, len(heights) + 1):
                lowest = min(lowest, heights[r-1])
                area = lowest * (r - l)
                maxarea = max(maxarea, area)
        return maxarea
                
        

sol = Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3]), 10)
print(sol.largestRectangleArea([i for i in range(20000)]), 20000)