class Solution:
  def minSubArrayLen(self, target: int, nums) -> int:
    minlength = 0
    l = 0
    r = 0
    runsum = nums[0]
    while True:
      # print(l, r, runsum, minlength)
      if runsum >= target:
        if minlength < .5:
          minlength = r - l + 1
        else:
          minlength = min(minlength, r - l + 1)
          if minlength == 1:
            return 1
        # Move left since over target
        runsum -= nums[l]
        l += 1
      else:
        r += 1
        if r >= len(nums):
          break
        runsum += nums[r]
    return minlength

sol = Solution()
print(sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]), 2)
print(sol.minSubArrayLen(target = 4, nums = [1,4,4]), 1)
print(sol.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]), 0)
# print(sol.minSubArrayLen(), )
