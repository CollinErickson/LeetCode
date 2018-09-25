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
        l = len(intervals)
        if l==0: return [newInterval]
        for i in range(l):
            if newInterval.start < intervals[i].start:
                intervals = intervals[0:i] + [newInterval] + intervals[i:]
                break
        else:
            intervals = intervals + [newInterval]
        #print("sorted ints are", intervals)
        l = len(intervals)
        keep = [True for i in range(l)]
        for i in range(l-1):
            if intervals[i].end >= intervals[i+1].start:
                intervals[i].end = max(intervals[i].end, intervals[i+1].end)
                intervals[i+1] = intervals[i]
                keep[i+1] = False
        return [i for i,k in zip(intervals,keep) if k]
        #return intervals

sol = Solution()
print(sol.insert([Interval(1,3),Interval(6,9)],
                  Interval(2,5)), 
                  [[1,5],[6,9]])
print(sol.insert([Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)],
                  Interval(4,8)), 
                  [[1,2],[3,10],[12,16]])
print(sol.insert([Interval(1,3)],
                  Interval(2,5)), 
                  [[1,5]])
print(sol.insert([],
                  Interval(2,5)), 
                  [[2,5]])
#print(sol.insert([Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)],
#                  Interval(6,7)), 
#                  [[1,6],[8,10],[15,18]])