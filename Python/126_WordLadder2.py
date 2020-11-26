class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList) -> int:
      #def makeDict():
      d = {}
      for word in wordList:
        for i in range(len(word)):
          tword = word[0:i] + "_" + word[i+1:]
          d[tword] = d.get(tword, []) + [word]
        #return d
      #d = makeDict()
      allsolutions = []
      queue, visited = deque([(beginWord, 1, [beginWord])]), set()
      while queue:
        word, steps, ladder = queue.popleft()
        if word not in visited:
          visited.add(word)
          if word == endWord:
            allsolutions += [ladder] #return ladder
          for i in range(len(word)):
            tword = word[0:i] + "_" + word[i+1:]
            nextwords = d.get(tword, [])
            for nextword in nextwords:
              if nextword not in visited:
                queue.append((nextword, steps+1, ladder + [nextword]))
      return allsolutions
from collections import deque

sol = Solution()

print(sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 5)
print(sol.findLadders("hit", "dog", ["hot","dog"]), 0)

#dir(set())




