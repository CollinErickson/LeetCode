class Solution:
  def rangeBitwiseAnd(self, left: int, right: int) -> int:
    out = 0
    while left != right:
      left >>= 1
      right >>= 1
      out += 1
    return right << out

sol = Solution()
print(sol.rangeBitwiseAnd(left = 5, right = 7), 4)
print(sol.rangeBitwiseAnd(left = 0, right = 0), 0)
print(sol.rangeBitwiseAnd(left = 1, right = 2147483647), 0)
# print(sol.rangeBitwiseAnd(), )
# print(sol.rangeBitwiseAnd(), )
# print(sol.rangeBitwiseAnd(), )
