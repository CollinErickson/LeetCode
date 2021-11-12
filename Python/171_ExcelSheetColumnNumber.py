class Solution:
  def titleToNumber(self, columnTitle):
    return 0 if len(columnTitle) == 0 else ((ord(columnTitle[-1])-64) + 26*self.titleToNumber(columnTitle[0:(len(columnTitle)-1)]))

sol = Solution()
print(sol.titleToNumber("A"), 1)
print(sol.titleToNumber("AB"), 28)
print(sol.titleToNumber("ZY"), 701)
print(sol.titleToNumber("FXSHRXW"), 2147483647)
# print(sol.titleToNumber(), )
