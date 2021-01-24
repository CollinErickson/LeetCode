class Solution:
    def candy(self, ratings):
      if len(ratings) <= 1:
        return len(ratings)
      x = [1 for r in ratings]
      for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
          x[i] = x[i-1] + 1
      for i in range(len(ratings)-1, 0, -1):
        if ratings[i-1] > ratings[i]:
          x[i-1] = max(x[i-1], x[i] + 1)
      return sum(x)
sol = Solution()
print(sol.candy([]), 0)
print(sol.candy([4]), 1)
print(sol.candy([1,2]), 3)
print(sol.candy([1,0,2]), 5)
print(sol.candy([1,2,2]), 4)
print(sol.candy([1,3,2,2,1]), 7)

