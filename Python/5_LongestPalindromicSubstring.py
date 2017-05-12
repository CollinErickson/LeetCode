# -*- coding: utf-8 -*-
"""
Created on Fri May 05 18:00:38 2017

@author: cbe117
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lens = len(s)
        long_len = 1
        long_ind = 1
        
        if lens == 1:
            return s
        # check odds first
        for i in range(1, lens - 1):
            #print i, range(1, 1+min(lens-i-1, i)), 1+min(lens-i-1, i), lens-i-1, lens
            for l in range(1, 1+min(lens-i-1, i)):
                #print i, l
                if s[i-l] != s[i+l]:
                    break
                if 2*l+1 > long_len:
                    long_len = 2*l + 1
                    long_ind = i
            if long_len > (lens-i)*2-1:
                #print "it's breaking", long_len, lens, i
                break
        # then check evens
        #print "Evens", long_len
        for i in range(0, lens-1):
            #print i, range(1, 2+min(lens-i-1, i)), 1+min(lens-i-1, i), lens-i-1, lens
            for l in range(1, 1+min(lens-i-1, i+1)):
                #print i, l
                if s[i-l+1] != s[i+l]:
                    break
                if 2*l > long_len:
                    #print 'newm', s[(long_ind-long_len+1):(long_ind+long_len+1)]
                    long_len = 2*l
                    long_ind = i
            if long_len > (lens-i-1)*2:
                break
        #print "odd", (long_ind-long_len/2), (long_ind+long_len/2+1)
        if long_len % 2 == 1:
            return s[(long_ind-long_len/2):(long_ind+long_len/2+1)]
        #print (long_ind-long_len+1),(long_ind+long_len+1)
        return s[(long_ind-long_len/2+1):(long_ind+long_len/2+1)]
sol = Solution()
print sol.longestPalindrome("babab")
print sol.longestPalindrome("ba")
print sol.longestPalindrome("bababb")
print sol.longestPalindrome("baab")
print sol.longestPalindrome("bca")
print sol.longestPalindrome("cbbd")
print sol.longestPalindrome("bbdefgh")
print sol.longestPalindrome("ccc")
print sol.longestPalindrome("cccc")
print sol.longestPalindrome("ababababa")
print sol.longestPalindrome("dddddddd")