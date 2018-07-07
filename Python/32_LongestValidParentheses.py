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
        verbose=False
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
            if verbose:
                            print i, longest_valid,
            si = s[i]
            if q.empty():
                if verbose:
                            print "put on empty"
                q.put((si, i))
            else: # Queue is not empty
                if si == "(":
                    # ERROR HERE, can't just add them in middle of sequence
                    #  track when it was put in, then check that when taking out
                    if verbose:
                            print "put"
                    q.put(("(", i))
                    current_valid = 0
                else: # si == ")"
                    qget, iget = q.get()
                    if verbose:
                            print 'qget', qget, iget,
                    if qget == "(":
                        if verbose:
                            print "get match"
                        #current_valid += 2
                        #longest_valid = max(longest_valid, current_valid)
                        if q.empty():
                            #print longest_valid, i, "hereee"
                            longest_valid = max(longest_valid, i+1) #current_valid)
                        else: # q not empty, no match to ), so last
                            qlast, ilast = q.get()
                            longest_valid = max(longest_valid, i - ilast)
                            q.put((qlast, ilast))
                    else: # qget is ), end streak
                        # bad
                        if verbose:
                            print 'reset', i, iget
                        #if q.empty():
                        #    longest_valid = max(longest_valid, i+1) #current_valid)
                        #else: # q not empty, no match to ), so last
                        #qlast, ilast = q.get()
                        longest_valid = max(longest_valid, i - iget - 1)
                        #q.put((qlast, ilast))
                        q.put((qget, iget))
                        q.put((")", i))
                        #longest_valid = max(longest_valid, i - iget)
                        #longest_valid = max(longest_valid, i - 1 - iget)
                        current_valid = 0
                        #q = LifoQueue()
        if not q.empty():
            current_valid = len(s) - 1 - q.get()[1]
        longest_valid = max(longest_valid, current_valid)
        return longest_valid

sol = Solution()
print sol.longestValidParentheses("(()"), 2
print sol.longestValidParentheses("(())"), 4
print sol.longestValidParentheses(")()())"), 4
print sol.longestValidParentheses("(())()())))(((((())))()())()((("), 16
print sol.longestValidParentheses("()(()))"), 6
print sol.longestValidParentheses("()(()"), 2
print sol.longestValidParentheses("()(())"), 6
print sol.longestValidParentheses("((()()"), 4
print sol.longestValidParentheses("(()))))(()()()()((((()))()()))))))))))"), 24
#print sol.longestValidParentheses("(())))"), 4
