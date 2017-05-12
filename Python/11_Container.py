# -*- coding: utf-8 -*-
"""
Created on Mon May 08 18:13:23 2017

@author: cbe117
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxar = 0
        lh = len(height)
        i = 0
        j = lh - 1
        hi = height[i]
        hj = height[j]
        minhihj = min(hi, hj)
        while i < j:
            ar = (j-i) * min(hi, hj)
            maxar = max(ar, maxar)
            if hi < hj:
                i+=1
                hi = height[i]
            else:
                j-=1
                hj = height[j]
        return maxar
    def maxAreabad(self, height):
        lh = len(height)
        maxar = 0
        maxafter = [0 for i in range(lh)]
        maxafter[lh-1] = height[lh-1]
        for j in range(lh-2, -1, -1):
            maxafter[j] = max(height[j], maxafter[j+1])
        maxbefore = [0 for i in range(lh)]
        maxbefore[0] = height[0]
        for i in range(1, lh):
            maxbefore[i] = max(height[i], maxbefore[i-1])
        i = 0
        j = lh - 1
        hi = height[i]
        hj = height[j]
        hia = maxafter[i]
        hjb = maxbefore[j]
        maxar = (j - i) * min(hi, hj)
        print 'maxafter', maxafter
        print "maxbefore", maxbefore
        print "height", height
        while i < j:
            print i, j, [hi,hj], [hia, hjb]
            ar = (j - i) * min(hi, hj)
            if ar > maxar:
                maxar = ar
                print "new", i, j, hi, hj, hia, hjb
            if (hi < hia and hj >= hjb) or (hi<hia and hj < hjb and hia<hjb):
                i += 1
                hi = height[i]
                hia = maxafter[i]
            elif hj < hjb:
                j -= 1
                hj = height[j]
                hjb = maxbefore[j]
            else:
                break
        return maxar
    def maxAreaslow(self, height):
        lh = len(height)
        maxar = 0
        for i in range(lh-1):
            hi = height[i]
            for j in range(i, lh):
                ar = (j-i) * min(hi, height[j])
                if ar > maxar:
                    maxar = ar
                    #print height, i, j, ar
        return maxar
sol = Solution()
print sol.maxArea([1, 1])
print sol.maxArea([1, 1, 2, 4, 1])
print sol.maxArea([28,342,418,485,719,670,878,752,662,994,654,504,929,660,424,855,922,744,600,229,728,33,371,863,561,772,271,178,455])

print sol.maxArea([1, 2, 4, 1, 7, 2, 1, 9, 4, 3, 2, 3, 22, 1, 1, 6, 4, 9, 1])