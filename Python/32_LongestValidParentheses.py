# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 17:28:45 2018

@author: cbe117
"""
from Queue import LifoQueue
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        #print s
        if len(s) <= 1:
            return 0
        #for i in range(len(s)-1):
        #    if s[i] == "(" and s[i+1] == ")":
        #        return 1 + self.longestValidParentheses(s[0:i] + s[(i+2):len(s)])
        current_valid = 0
        longest_valid = 0
        q = LifoQueue()
        for i in range(len(s)):
            #print i,
            si = s[i]
            if q.empty():
                #print "put on empty"
                q.put(si)
            else:
                if si == "(":
                    # ERROR HERE, can't just add them in middle of sequence
                    #  track when it was put in, then check that when taking out
                    #print "put"
                    q.put("(")
                else:
                    qget = q.get()
                    #print 'qget', qget
                    if qget == "(":
                        current_valid += 2
                    else:
                        # bad
                        #print 'reset'
                        longest_valid = max(longest_valid, current_valid)
                        current_valid = 0
                        #q = LifoQueue()
        longest_valid = max(longest_valid, current_valid)
        return longest_valid

sol = Solution()
print sol.longestValidParentheses("(()"), 2
print sol.longestValidParentheses("(())"), 4
print sol.longestValidParentheses(")()())"), 4
print sol.longestValidParentheses("(())()())))(((((())))()())()((("), 16
print sol.longestValidParentheses("()(()"), 2
