class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) <= 1:
          return len(nums)
        nums.sort()
        maxC = 1
        currC = 1
        lastnum = nums[0]
        for i in range(1, len(nums)):
          if nums[i] == lastnum + 1:
            currC += 1
            maxC = max(maxC, currC)
            lastnum = nums[i]
          elif nums[i] == lastnum:
            False
          else:
            currC = 1
            lastnum = nums[i]
        return maxC
        
sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]), 4)
print(sol.longestConsecutive([12]), 1)
print(sol.longestConsecutive([]), 0)
print(sol.longestConsecutive([1,0,1,0,2]), 3)
