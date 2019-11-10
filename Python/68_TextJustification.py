# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:31:58 2019

@author: cbe117
"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
        lines = []
        #linestart = 0
        curline = []
        lencurline = 0
        #for i in range(len(words)):
        #    if lencurline + len(words[i]) < maxWidth:
        #        pass
        for w in words:
            if lencurline + len(w) < maxWidth:
                curline.append(w)
                lencurline += len(w) + 1
            else:
                lines.append(curline)
                curline = [w]
                lencurline = len(w)
        lines.append(curline)
        
        # Now format within each line
        lines2 = []
        for line in lines:
            nspacestotal = maxwidth - sum([len(w) for w in line])
            if nspacestotal < len(line) - 1:
                print("FAILURE")
        return lines2

sol = Solution()
print(sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(
[
   "This    is    an",
   "example  of text",
   "justification.  "
])