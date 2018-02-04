# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:54:02 2018

@author: cbe117
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        if candidates[0] > target:
            return []
        candict = {}
        for ci in candidates:
            if ci not in candict:
                candict[ci] = 1
            else:
                candict[ci] += 1
        #solns = []
        #for maxci in range(len(candidates)):
        #    for ti in range(0, target + 1):
        combs = {}
        for ti in range(1, target+1):
            #print "ti is", ti
            for ci in candict:
                di = ti - ci
                #print "ci is", ci, "di is", di
                if di == 0:
                    if ti not in combs:
                        combs[ti] = [[ci]]
                    else:
                        combs[ti] += [[ci]]
                if di > 0:
                    if di in combs:
                        for comb in combs[di]:
                            if comb[-1] <= ci:
                                #print di, comb, ci, ti
                                #print [comb + [ci]]
                                if len(comb) < candict[ci] or comb[-candict[ci]] < ci:
                                    if ti in combs:
                                        combs[ti] += [comb + [ci]]
                                    else:
                                        combs[ti] = [comb + [ci]]
        if target in combs:
            return combs[target]
        else:
            return []
sol = Solution()
print sol.combinationSum2([1,2,3], 6)
print sol.combinationSum2([2,3,6,7], 7)
print sol.combinationSum2([1,1,1,2,3], 3)
print sol.combinationSum2([1], 1)