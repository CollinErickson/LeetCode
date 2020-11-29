class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
      #def makeDict():
      d = {}
      for word in wordList:
        for i in range(len(word)):
          tword = word[0:i] + "_" + word[i+1:]
          d[tword] = d.get(tword, []) + [word]
        #return d
      #d = makeDict()
      
      queue, visited = deque([(beginWord, 1)]), set()
      while queue:
        word, steps = queue.popleft()
        if word not in visited:
          visited.add(word)
          if word == endWord:
            return steps
          for i in range(len(word)):
            tword = word[0:i] + "_" + word[i+1:]
            nextwords = d.get(tword, [])
            for nextword in nextwords:
              if nextword not in visited:
                queue.append((nextword, steps+1))
      return 0
from collections import deque

sol = Solution()

print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 5)
print(sol.ladderLength("hit", "dog", ["hot","dog"]), 0)

#dir(set())




