class Solution:
    def singleNumber(self, nums):
        y = 0
        for x in nums:
          y = y ^ x
        return y
sol = Solution()

print(sol.singleNumber([2,2,1]), 1)
print(sol.singleNumber([4,1,2,1,2]), 4)
print(sol.singleNumber([1]), 1)

