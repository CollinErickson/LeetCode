# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 16:34:14 2018

@author: cbe117
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
        return '[' + str(self.start) + ',' + str(self.end) + ']'  

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        
        return intervals

sol = Solution()
print(sol.insert([Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)],
                  Interval(6,7)), 
                  [[1,6],[8,10],[15,18]])