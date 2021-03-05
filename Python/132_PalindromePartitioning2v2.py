class Solution:
    def minCut(self, s):
      n = len(s)
      ncuts = [i-1 for i in range(0, n+1)]
      # i is center of palindrome
      for i in range(0, n):
        # Odd length palindrome, work outward
        j = 0
        while i-j >= 0 and i+j < n and s[i-j] == s[i+j]:
          ncuts[i+j+1] = min(ncuts[i+j+1], 1+ncuts[i-j])
          j += 1
        # Even length palindrome, work outward
        j = 1
        while i-j+1 >= 0 and i+j < n and s[i-j+1] == s[i+j]:
          ncuts[i+j+1] = min(ncuts[i+j+1], 1+ncuts[i-j+1])
          j += 1
      return ncuts[n]

sol = Solution()

print(sol.minCut("aab"), 1)
print(sol.minCut("aabaa"), 0)
print(sol.minCut("ababa"), 0)
print(sol.minCut("acbdafbag"), 8)
print(sol.minCut("abbbba"), 0)
print(sol.minCut("abbbb"), 1)
