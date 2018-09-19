# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 20:04:15 2018

@author: cbe117
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s.strip())==0: return 0
        return len(s.strip().split()[-1])
    
sol = Solution()
print(sol.lengthOfLastWord("hello world!"), 6)
print(sol.lengthOfLastWord("hello world"), 5)
print(sol.lengthOfLastWord("helloworld!"), 11)
print(sol.lengthOfLastWord(""), 0)
print(sol.lengthOfLastWord("   "), 0)
print(sol.lengthOfLastWord("   today is a good day"), 3)
print(sol.lengthOfLastWord("a   "), 1)

