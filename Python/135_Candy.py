class Solution:
    def candy(self, ratings):
        if len(ratings) <=1:
          return len(ratings)
        total = 1
        prev = 1
        slack = 0
        for i in range(1, len(ratings)):
          if ratings[i] > ratings[i-1]:
            # check for slack, if yes add to it
            curr = prev + 1
            total += curr
            prev = curr
          elif ratings[i] == ratings[i-1] or prev > 1:
            curr = 1
            total += curr
            prev = curr
          else: # Boost all previous (i has lower rating but previous got 1)
            # Use slack
            curr = 1
            total += curr + i
            prev = curr
        return total

sol = Solution()
print(sol.candy([]), 0)
print(sol.candy([4]), 1)
print(sol.candy([1,2]), 3)
print(sol.candy([1,0,2]), 5)
print(sol.candy([1,2,2]), 4)
print(sol.candy([1,3,2,2,1]), 7)

