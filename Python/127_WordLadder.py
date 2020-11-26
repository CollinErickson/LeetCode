class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
      L = len(beginWord)
      wordSet = set(wordList)
      if endWord not in wordList:
        return 0
      allletters = {w for word in wordList for w in word}
      q = collections.deque([[beginWord, 1]])
      seenwords = set(beginWord)
      while q:
        w, l = q.popleft()
        #seenwords.add(w)
        if w == endWord:
          return l
        for tempword in wordList:
          if tempword not in seenwords and sum([tempword[i] == w[i] for i in range(L)]) == L-1:
              q.append([tempword, l+1])
              seenwords.add(tempword)
        #for i in range(len(w)):
        #  for letter in allletters:
        #    newWord = w[:i] + letter + w[(i+1):]
        #    if newWord in wordList and newWord not in seenwords:
        #      q.append([newWord, l+1])
        #      seenwords.add(w)
      return 0
import collections

sol = Solution()

print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 5)
print(sol.ladderLength("hit", "dog", ["hot","dog"]), 0)

#dir(set())




