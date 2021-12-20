class Solution:
  def countPrimes(self, n):
    if n <= 2:
      return 0
    x = [1 if i>1.5 else 0 for i in range(n)]
    # print(x)
    for i in range(2, int(math.ceil(math.sqrt(n)))):
      if x[i] > .5:
        j = 2*i
        while j < n:
          x[j] = 0
          j += i
    # print(x)
    return sum(x)

import math

sol = Solution()
print(sol.countPrimes(10), 4)
print(sol.countPrimes(0), 0)
print(sol.countPrimes(1), 0)
print(sol.countPrimes(7), 3)
print(sol.countPrimes(3), 1)
print(sol.countPrimes(5000000), 1)
