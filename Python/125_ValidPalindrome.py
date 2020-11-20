class Solution:
    def isPalindrome(self, s: str) -> bool:
      s = s.lower()
      s = "".join([c for c in s if c.isalnum()])
      ls = len(s)
      for i in range(ls//2):
        if s[i] != s[ls-i-1]:
          return False
      return True

sol = Solution()
print(sol.isPalindrome("abc"), False)
print(sol.isPalindrome("abcba"), True)
print(sol.isPalindrome("ab"), False)
print(sol.isPalindrome("a"), True)
print(sol.isPalindrome(""), True)
print(sol.isPalindrome("abc12"), False)
print(sol.isPalindrome("abc121cba"), True)
print(sol.isPalindrome("A man, a plan, a canal: Panama"), True)
print(sol.isPalindrome("race a car"), False)


a="A man, a plan, a canal: Panama"
"".join([c for c in a.lower() if c.isalnum()])
