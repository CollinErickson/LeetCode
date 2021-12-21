class Solution:
  def isHappy(self, n: int) -> bool:
    d = {}
    while True:
      n2 = sum([int(i) ** 2 for i in str(n)])
      # print(n, n2, d, n2 in d)
      if n2 == 1:
        return True
      if n2 in d:
        return False
      d[n2] = 1
      n = n2
    return

sol = Solution()
print(sol.isHappy(19), True)
print(sol.isHappy(2), False)
print(sol.isHappy(19887), False)
# print(sol.isHappy(), )
# print(sol.isHappy(), )
