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
          if val < 2.5:
            return key
        return False
sol = Solution()

print(sol.singleNumber([2,2,3,2]), 3)
print(sol.singleNumber([0,1,0,1,0,1,99]), 99)
print(sol.singleNumber([1]), 1)

