class Solution:
    partialwords = None
    def wordBreak(self, s, wordDict):
      self.partialwords = {0:[""]}
      wordSet = set(wordDict)
      wordSetByLen = {}
      for word in wordSet:
        wordLen = len(word)
        if wordLen in wordSetByLen:
          wordSetByLen[wordLen].add(word)
        else:
          wordSetByLen[wordLen] = set([word])
      wordLens = wordSetByLen.keys()
      for i in range(len(s)):
        if i in self.partialwords:
          for wordLen_i in wordLens:
            if i + wordLen_i <= len(s):
              sub_s = s[i:(i + wordLen_i)]
              if sub_s in wordSetByLen[wordLen_i]:
                newwords = []
                for partialword in self.partialwords[i]:
                  newwords.append(partialword + (" " if i>0 else "") + sub_s)
                if i + wordLen_i in self.partialwords:
                  self.partialwords[i + wordLen_i] += newwords
                else:
                  self.partialwords[i + wordLen_i] = newwords
      if len(s) in self.partialwords:
        return self.partialwords[len(s)]
      return []

sol = Solution()
print(sol.wordBreak(s = "leetcode", wordDict = ["leet", "code"]), ["leet code"])
print(sol.wordBreak(s = "catsanddog", wordDict = ["cat", "cats", "and", "sand", "dog"]), ["cats and dog","cat sand dog"])
print(sol.wordBreak(s = "pineapplepenapple", wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]), [
  "pine apple pen apple","pineapple pen apple","pine applepen apple"])
print(sol.wordBreak(s = "catsandog",wordDict = ["cats", "dog", "sand", "and", "cat"]), [])
#print(sol.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]), True)
#print(sol.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]), False)
#print(sol.wordBreak(s = "c", wordDict = ["cats", "dog", "sand", "and", "cat"]), False)
#print(sol.wordBreak(s = "catsandog", wordDict = []), False)
#print(sol.wordBreak("aaaaaaa", ["aaaa","aaa"]), True)
print(sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), [])

#print(sol.wordBreak("abcd", ["a","abc","b","cd"]), True)
