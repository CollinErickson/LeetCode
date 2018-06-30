# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 16:46:32 2018

@author: cbe117
"""

class Solution2(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        nw = len(words)
        wl = len(words[0])
        dic = {}
        # First make dict of where each word starts
        for i in range(len(s)):
            for word in words:
                for j in range(wl):
                    if word[j] != s[i+j]:
                        break
                else: # All match
                    dic[word] += [i]
        # Then check through dicts
        pass
class Solution3(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        nw = len(words)
        if nw == 0:
            return []
        wl = len(words[0])
        #dic = {}
        lens = len(s)
        sols = []
        worddict=dict()
        for word in words:
            if word in worddict:
                worddict[word]+=1
            else:
                worddict[word]=1
        wordsleft = dict()
        # First make dict of where each word starts
        for i in range(lens):
            if i > lens - wl * nw:
                break
            #print i
            #print "at char", i
            #wordsleft = dict([(word, True) for word in words])
            for word in words:
                wordsleft[word] = worddict[word]
            for j in range(nw):
                #print "j", j
                nextword = s[(i+wl*j):(i+wl*j+wl)]
                #print "  checking ", j, "nextword is", nextword
                if nextword in wordsleft:
                #if wordsleft[nextword] > 0:
                    #if wordsleft[nextword] == True:
                    #    wordsleft[nextword] = False
                    if wordsleft[nextword] > 0:
                        wordsleft[nextword] -= 1
                    else:
                        break
                else:
                    break
            else:
                sols += [i]
        return sols
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        nw = len(words)
        if nw == 0:
            return []
        wl = len(words[0])
        lens = len(s)
        sols = []
        worddict=dict()
        worddict0=dict()
        for word in words:
            if word in worddict:
                worddict[word]+=1
                worddict0[word]+=1
            else:
                worddict[word]=1
                worddict0[word]=1
        #wordsleft = dict()
        # First make dict of where each word starts
        for k in range(wl):
            wordsinseq = 0
            for word in worddict:
                worddict[word] = worddict0[word]
            #print "k is", k, worddict
            i = k
            while i+wl <= lens:# - wl * nw:
                #print " i is", i, "wis is", wordsinseq, 'word is'#, worddict['word']
                #for j in range(nw):
                #nextword = s[(i+wl*j):(i+wl*j+wl)]
                nextword = s[i:(i+wl)]
                #print " nextword is", nextword, worddict[nextword]
                if nextword in worddict and worddict[nextword] > 0:
                    worddict[nextword] -= 1
                    wordsinseq += 1
                    if wordsinseq == nw:
                        #print "  sol for k, i", k, i
                        sols += [i - nw*wl+wl]
                        # Have to keep checking
                        wordsinseq -= 1
                        #print (i - nw*wl+wl), (i - nw*wl+wl*2)
                        worddict[s[(i - nw*wl+wl):(i - nw*wl+wl*2)]]+=1
                elif nextword in worddict: #soft restart, go back and find where word is used
                    #print " going back"
                    numgoback = worddict0[nextword] - worddict[nextword]
                    #print "    ", i-nw*wl+1
                    j = i - wl
                    while j >= 0:
                        #print "  j is ", j, worddict
                        oldword = s[j:(j+wl)]
                        if oldword == nextword:
                            numgoback -= 1
                            if numgoback == 0:
                                #i = j + wl
                                #worddict[nextword] += 1
                                # Clear words before it
                                kk = j - wl
                                while (i-kk)/wl <= wordsinseq:
                                    worddict[s[kk:(kk+wl)]]+=1
                                    kk -= wl
                                wordsinseq = (i-j) / wl
                                #print "  words in seq is ", wordsinseq
                                break
                        j -= wl
                    #print worddict
                else: #Need full restart
                    wordsinseq = 0
                    for word in words:
                        worddict[word] = worddict0[word]
                #print "changing", i, i+wl
                i += wl
        return sols
sol = Solution()
print sol.findSubstring("barfoothefoobarman", ["foo", "bar"]), [0,9]
print sol.findSubstring("foobar", ["oob"]), [1]
print sol.findSubstring("foobar", []), []
print sol.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]), [8]
print sol.findSubstring("aaaaaaaaaaaa",["a","a","a","a","a","a","a","a","a","a","a","a"]), [0]
print sol.findSubstring("aaa",["a","a","a"]), [0]
print sol.findSubstring("aaa",["a","a"]), [0,1]
print sol.findSubstring("ababababababababababababababababababababababababababa",["ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba"]), []
print sol.findSubstring("aaaaaa",["aaa","aaa"]), [0]
print sol.findSubstring("aaaaaa",["a","a"]), [0,1,2,3,4]
print sol.findSubstring("aaa",["a","b"]), []
