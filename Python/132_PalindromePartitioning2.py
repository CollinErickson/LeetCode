class Solution:
    def minCut(self, s):
      x = self.partition(s)
      lens = [len(i) for i in x]
      return min(lens) - 1
    def partition(self, s: str):
      
      x = []
      #print('partition', s, len(s))
      for i in range(1,len(s)):
        #print('i is', i)
        a = s[:i]
        #print('a is', a)
        if self.isPalindrome(a):
          #print("palind", a)
          x2 = self.partition(s[i:])
          if len(x2) > 0:
            #print("x2 is", x2)
            x += [[a] + x3 for x3 in x2]
      if self.isPalindrome(s):
        x += [[s]]
      return x
    def isPalindrome(self, s):
      for i in range((len(s))//2):
        #print(i, s[i])
        if s[i] != s[len(s) - 1 - i]:
          return False
      return True

sol = Solution()

print(sol.minCut("aab"), 1)
print(sol.minCut("aabaa"), 0)
print(sol.minCut("ababa"), 0)
print(sol.minCut("acbdafbag"), 8)
print(sol.minCut(""), 0)
