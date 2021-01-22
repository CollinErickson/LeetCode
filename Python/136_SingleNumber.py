class Solution:
    def singleNumber(self, nums):
        d = dict()
        for x in nums:
          #print(x)
          if x in d:
            d[x] += 1
          else:
            d[x] = 1
        #print(d)
        for key in d:
          val = d[key]
          if val < 1.5:
            return key
        return False
sol = Solution()

print(sol.singleNumber([2,2,1]), 1)
print(sol.singleNumber([4,1,2,1,2]), 4)
print(sol.singleNumber([1]), 1)

