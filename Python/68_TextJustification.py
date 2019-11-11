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
            #print(curline, lencurline, w)
            if lencurline + len(w) <= maxWidth:
                curline.append(w)
                lencurline += len(w) + 1
            else: # start a new line
                lines.append(curline)
                curline = [w]
                lencurline = len(w) + 1
        lines.append(curline)
        
        # Now format within each line
        lines2 = []
        for iline, line in enumerate(lines):
            if iline < len(lines) - 1: # Not the last line
                nspacestotal = maxWidth - sum([len(w) for w in line])
                nbreaks = len(line) - 1
                spacesperbreak = nspacestotal // max(1, nbreaks)
                if nspacestotal < len(line) - 1:
                    print("FAILURE")
                l = ''
                if len(line) > 1:
                    for iw, w in enumerate(line):
                        l += (w)
                        if iw < len(line) - 1:
                            l += ''.join([' ' for i in range(spacesperbreak + (nspacestotal - nbreaks*spacesperbreak>iw))])
                else:
                    print(line, lines)
                    l = line[0] + ''.join([' ' for i in range(maxWidth - len(line[0]))])
                lines2.append(l)
            else: # Last line
                l = ' '.join(line)
                l += ''.join([' ' for i in range(maxWidth - len(l))])
                lines2.append(l)
        return lines2

sol = Solution()
print(sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(
[
   "This    is    an",
   "example  of text",
   "justification.  "
])
    
print(sol.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print([
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
])
    
print(sol.fullJustify(["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"], 20))
print([
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
])


print(sol.fullJustify(["Listen","to","many,","speak","to","a","few."], 6))
print(sol.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))
