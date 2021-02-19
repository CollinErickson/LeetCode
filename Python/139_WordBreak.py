class Solution:
    alreadychecked = None
    def wordBreak(self, s, wordDict):
      self.alreadychecked = []
      wordSet = set(wordDict)
      wordLen = ([len(s) for s in wordSet])
      wordLen.sort()
      wordLen.reverse()
      return self.wordBreakInside(s, wordSet, wordLen)
    def wordBreakInside(self, s, wordSet, wordLen):
      #print("s", s)
      for l in wordLen:
        if l == len(s):
          if s in wordSet:
            return True
        if l < len(s):
          if len(s) - l not in self.alreadychecked:
            if s[0:l] in wordSet:
              if self.wordBreakInside(s[l:len(s)], wordSet, wordLen):
                return True
              self.alreadychecked.append(len(s) - l)
          else:
            pass #print('already checked', s[l:len(s)])
      return False

sol = Solution()
print(sol.wordBreak(s = "leetcode", wordDict = ["leet", "code"]), True)
print(sol.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]), True)
print(sol.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]), False)
print(sol.wordBreak(s = "c", wordDict = ["cats", "dog", "sand", "and", "cat"]), False)
print(sol.wordBreak(s = "catsandog", wordDict = []), False)
print(sol.wordBreak("aaaaaaa", ["aaaa","aaa"]), True)
#print(sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
#["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), False)

print(sol.wordBreak("abcd", ["a","abc","b","cd"]), True)
