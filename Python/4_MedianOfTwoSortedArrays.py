# -*- coding: utf-8 -*-
"""
Created on Tue May 02 19:43:22 2017

@author: cbe117
"""
import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 == 0 and l2 == 0:
            return None
        if l1 == 0:
            return self.median(nums2)
        if l2 == 0:
            return self.median(nums1)
        if l1 == 1 and l2 == 1:
            return (nums1[0] + nums2[0]) / 2.
        elif l1 == 1:
            return self.medianone(nums1, nums2)
        elif l2 == 1:
            return self.medianone(nums2, nums1)
        l1_odd = l1 % 2 != 0
        l2_odd = l2 % 2 != 0
        if l1_odd and l2_odd:
            return self.findMedianSortedArraysEven(nums1, nums2)
        elif l1_odd:
            return self.findMedianSortedArraysOddEven(nums1, nums2)
        elif l2_odd:
            return self.findMedianSortedArraysOddEven(nums2, nums1)
        return self.findMedianSortedArraysEven(nums1, nums2)
    def median(self, nums):
        l = len(nums)
        if l % 2 == 0:
            return (nums[l/2-1] + nums[l/2]) / 2.
        return nums[(l-1) / 2]
    def medianone(self, n1, nums):
        l = len(nums)
        if l % 2 == 0:
            a = [n1[0], nums[l/2 - 1], nums[l/2]]
            a.sort()
            return a[1]
        a = [n1[0], nums[l/2 - 1], nums[l/2], nums[l/2+1]]
        a.sort()
        return (a[1] + a[2]) / 2.
        
    def findMedianSortedArraysOddEven(self, nums1, nums2):
        t1 = self.findMedianSortedArraysEvenIndices(nums1[0:(len(nums1)-1)], nums2)
        #print t1
        if t1[1] < 0:
            #print nums1, nums2
            
            return min(nums1[int(math.ceil(t1[0]))], nums2[0])
            return nums1[len(nums1)-1]
        elif t1[1] > len(nums2)-1:
            return max(nums1[int(math.ceil(t1[0]))], nums2[len(nums2) - 1])
        a = [nums1[int(math.ceil(t1[0]))], nums2[int(math.floor(t1[1]))], nums2[int(math.ceil(t1[1]))]]
        a.sort()
        return a[1]
    def findMedianSortedArraysEvenIndices(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        p1 = int(math.ceil(math.log(l1, 2)))
        p2 = int(math.ceil(math.log(l2, 2)))
        i1 = l1 / 2 - .5
        i2 = l2 / 2 - .5
        p = min(p1, p2) - 1
        while True:
            #print p1, p2, i1, i2, p
            # Check if l1<u2 and l2<u1
            # If yes, done. Else it tells you which way to move
            if i1 > 0 and i2 < l2 - 1:
                a1 = nums1[int(math.floor(i1))]
                b2 = nums2[int(math.ceil(i2))]
                a1b2_good = a1 <= b2
            else:
                a1b2_good = True
            if i1 < l1 - 1 and i2 > 0:
                b1 = nums2[int(math.floor(i2))]
                a2 = nums1[int(math.ceil(i1))]
                b1a2_good = b1 <= a2
            else:
                b1a2_good = True
            
            #a1 = nums1[int(math.floor(i1))]
            #a2 = nums1[int(math.ceil(i1))]
            #b1 = nums2[int(math.floor(i2))]
            #b2 = nums2[int(math.ceil(i2))]
            move_dist = 2**p
            if a1b2_good and b1a2_good:
                #print "done", i1, i2, a1, a2, b1, b2
                if i1 > 0 and i2 > 0:
                    upperlower = max(a1, b1)
                elif i1 > 0:
                    upperlower = a1
                else:
                    upperlower = b1
                if i1 < l1 - 1 and i2 < l2 - 1:
                    lowerupper = min(a2,b2)
                elif i1 < l1 - 1:
                    lowerupper = a2
                else:
                    lowerupper = b2
                return [i1, i2] #(max(a1, b1) + min(a2, b2)) / 2.
            elif not a1b2_good: # move i1 down and i2 up
                move_dist = min(2**p, i1 + .5, l2 - i2 - .5)
                i1 -= move_dist
                i2 += move_dist
                #print i1, i2, 'aaa'
                pass
            elif not b1a2_good: # move i1 up and i2 down
                move_dist = min(2**p, i2 + .5, l1 - i1 - .5)
                i1 += move_dist
                i2 -= move_dist
                #print i1, i2, 'bbb'
                pass
            else:
                return "failed"
            under = i1 + i2
            over = l1+l2 - under
            p -= 1
            if p < -1:
                return "no good"
        return l1+l2
    def findMedianSortedArraysEven(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        p1 = int(math.ceil(math.log(l1, 2)))
        p2 = int(math.ceil(math.log(l2, 2)))
        i1 = l1 / 2 - .5
        i2 = l2 / 2 - .5
        if l2 % 2 != 0:
            i2 += 1
        p = min(p1, p2) - 1
        while True:
            #print p1, p2, i1, i2, p
            # Check if l1<u2 and l2<u1
            # If yes, done. Else it tells you which way to move
            if i1 > 0:
                a1 = nums1[int(math.floor(i1))]
            if i2 < l2 - 1:
                b2 = nums2[int(math.ceil(i2))]
            if i1 > 0 and i2 < l2 - 1:
                a1b2_good = a1 <= b2
            else:
                a1b2_good = True
            if i2 > 0:
                b1 = nums2[int(math.floor(i2))]
            if i1 < l1 - 1:
                a2 = nums1[int(math.ceil(i1))]
            if i1 < l1 - 1 and i2 > 0:
                b1a2_good = b1 <= a2
            else:
                b1a2_good = True
            
            #a1 = nums1[int(math.floor(i1))]
            #a2 = nums1[int(math.ceil(i1))]
            #b1 = nums2[int(math.floor(i2))]
            #b2 = nums2[int(math.ceil(i2))]
            move_dist = 2**p
            if a1b2_good and b1a2_good:
                #print "done", i1, i2, a1, a2, b1, b2
                if i1 > 0 and i2 > 0:
                    upperlower = max(a1, b1)
                elif i1 > 0:
                    upperlower = a1
                else:
                    upperlower = b1
                if i1 < l1 - 1 and i2 < l2 - 1:
                    lowerupper = min(a2,b2)
                elif i1 < l1 - 1:
                    lowerupper = a2
                else:
                    lowerupper = b2
                #print upperlower, lowerupper#, a1, a2, b1, b2
                return (upperlower + lowerupper) / 2.
                #return (max(a1, b1) + min(a2, b2)) / 2.
            elif not a1b2_good: # move i1 down and i2 up
                move_dist = min(2**p, i1 + .5, l2 - i2 - .5)
                i1 -= move_dist
                i2 += move_dist
                #print i1, i2, 'aaa'
                pass
            elif not b1a2_good: # move i1 up and i2 down
                move_dist = min(2**p, i2 + .5, l1 - i1 - .5)
                i1 += move_dist
                i2 -= move_dist
                #print i1, i2, 'bbb'
                pass
            else:
                return "failed"
            under = i1 + i2
            over = l1+l2 - under
            p -= 1
            if p < -1:
                return "no good"
        return l1+l2
sol = Solution()
print sol.findMedianSortedArrays([1,3, 5, 7],[2, 4, 6, 8])
print sol.findMedianSortedArrays([1,3, 4, 7],[2, 5, 6, 8])
print sol.findMedianSortedArrays([1,3, 4, 7],[12, 15, 16, 18])
print sol.findMedianSortedArrays([1,3],[2, 99, 100, 101])
print sol.findMedianSortedArrays([1,3,18],[2, 99, 100, 101])
print sol.findMedianSortedArrays([1,3,4,5,18],[12, 99, 100, 101])
print sol.findMedianSortedArrays([11,12, 99, 100, 101],[1,3,4,5])
print sol.findMedianSortedArrays([1,3],[2])
print sol.findMedianSortedArrays([3],[2, 4, 5, 6, 7])
print sol.findMedianSortedArrays([3, 8, 9],[2, 4, 5, 6, 7])
print sol.findMedianSortedArrays([],[1])
print sol.findMedianSortedArrays([1112],[])
print sol.findMedianSortedArrays([3, 5, 7, 8, 9],[12,14, 17, 232, 555])
print sol.findMedianSortedArrays([3, 4],[1, 2])
print sol.findMedianSortedArrays([3, 4],[1, 2, 5])
print sol.findMedianSortedArrays([4, 5],[1,2, 3, 6, 7])
print sol.findMedianSortedArrays([5, 6],[1,2, 3, 4, 7])

# Solves correctly but is super ugly
# Can remove Even and just get results from EvenIndices to save space
# Can cut other code stuff too