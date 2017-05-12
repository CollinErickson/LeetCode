# -*- coding: utf-8 -*-
"""
Created on Mon May 01 09:39:11 2017

@author: cbe117
"""

class Solution(object):
    def lengthOfLongestSubstring_wrong(self, s):
        """
        :type s: str
        :rtype: int
        """
        lens = len(s)
        if lens == 1:
            return 1
        for i in range(1, lens):
            for j in range(0, lens - i):
                print i,j, i+j, s[j], s[i+j]
                if s[j] == s[i+j]:
                    return i
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lens = len(s)
        if lens == 0:
            return 0
        if lens == 1:
            return 1
        for i in range(1, lens):
            if i == 1:
                dif = [s[j] == s[j+i] for j in range(lens-i)]
            else:
                dif = [(s[j] == s[j+i] or dif[j] or dif[j+1]) for j in range(lens-i)]
            if all(dif):
                return i
        return lens
    def lengthOfLongestSubstringRecursive(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(self.longestSubstring(s))
    def longestSubstringRecursive(self, s):
        #print s
        lens = len(s)
        if lens == 0 or lens == 1:
            return s
        t = s
        lent = len(t)
        t1 = t[0:(len(t)-1)]
        t2 = t[1:len(t)]
        print s, t1, t2
        ends_equal = t[0] == t[lent-1]#listt[0:(len(t)-1)] == listt[1:len(t)]
        #if False and ends_equal: # return func applied to first part of t
        #    return self.longestSubstring(t1)
        #else: # Check both sides of t
        u1 = self.longestSubstring(t1)
        u2 = self.longestSubstring(t2)
        if u1 == t1 and u2 == t2 and not ends_equal:
            return t
        if len(u1) >= len(u2):
            return u1
        else:
            return u2
sol = Solution()
print sol.lengthOfLongestSubstring("ababab")
print sol.lengthOfLongestSubstring("abcabcbb")
print sol.lengthOfLongestSubstring("bbbbb")
s3 = sol.lengthOfLongestSubstring("pwwkew")
print '-', s3
print sol.lengthOfLongestSubstring("tmmzuxt")
print sol.lengthOfLongestSubstring("aorjhguskzaahziwi")
print sol.lengthOfLongestSubstring("asdflkjpqwer")
print sol.lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnop")