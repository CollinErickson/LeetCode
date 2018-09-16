# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 20:51:36 2018

@author: cbe117
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
        return str(self.start) + ',' + str(self.end)         
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        l = len(intervals)
        if l <= 1: return intervals
        keep = [True for i in range(l)]
        intervals.sort()
        for i in range(l-1):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals[i+1] = intervals[i]
                keep[i+1] = False
        return [i for i,k in zip(intervals,keep) if k]
sol = Solution()
#print(sol.merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
print(sol.merge([Interval(1,4),Interval(4,5)]), [[1,5]])

print(sol.merge([Interval(1,5)]), [[1,5]])




