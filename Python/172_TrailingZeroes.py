class Solution:
  def trailingZeroes(self, n: int) -> int:
    out = 0
    x = 5
    while x <= n:
      out += (n // x)
      x *= 5
    return out

sol = Solution()
print(sol.trailingZeroes(3), 0)
print(sol.trailingZeroes(5), 1)
print(sol.trailingZeroes(0), 0)
for i in range(31):
  print("    i:  ", i, "\t", sol.trailingZeroes(i))
print(sol.trailingZeroes(29), 6)
print(sol.trailingZeroes(41), 9)
print(sol.trailingZeroes(78), 18)

