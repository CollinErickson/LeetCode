class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
      wd = {}
      if endWord not in wordList:
        return 0
      curword=beginWord
      while True:
        if curword in wd:
          return 0
        dwords = []
        
        wd[curword] = dwords
        
        break
      return


sol = Solution()

print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 5)
