class Solution:
    def partition(self, s: str):
      
      x = []
      print('partition', s, len(s))
      for i in range(1,len(s)):
        print('i is', i)
        a = s[:i]
        print('a is', a)
        if self.isPalindrome(a):
          print("palind", a)
          x2 = self.partition(s[i:])
          if len(x2) > 0:
            print("x2 is", x2)
        
      return x
    def isPalindrome(self, s):
      for i in range((len(s))//2):
        #print(i, s[i])
        if s[i] != s[len(s) - 1 - i]:
          return False
      return True

sol = Solution()

print(sol.partition("aab"))
#print(sol.partition("aabaa"))
#print(sol.isPalindrome("ababa"))
