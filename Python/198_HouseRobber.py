class Solution:
  def rob(self, nums):
    N = len(nums)
    if N <= 2:
      return max(nums)
    a = [0 for j in range(N)]
    a2 = nums[N-1]
    a1 = max(nums[N-1], nums[N-2])
    for i in range(N-3, -1, -1):
      # print(i, a, nums, a[i+1], nums[i]+a[i+2], nums[i], a[i+1])
      a0 = max(a1, nums[i] + a2)
      a1, a2 = a0, a1
    # print('a', a)
    return a0
  def robSlow(self, nums):
    N = len(nums)
    if N <= 2:
      return max(nums)
    a = [0 for j in range(N)]
    a[N - 1] = nums[N-1]
    a[N - 2] = max(nums[N-1], nums[N-2])
    for i in range(N-3, -1, -1):
      # print(i, a, nums, a[i+1], nums[i]+a[i+2], nums[i], a[i+1])
      a[i] = max(a[i+1], nums[i] + a[i+2])
    # print('a', a)
    return a[0]

sol = Solution()
print(sol.rob([1,2,3,1]), 4)
print(sol.rob([2,7,9,3,1]), 12)
print(sol.rob([2]), 2)
print(sol.rob([1,2]), 2)
print(sol.rob([2,1]), 2)
print(sol.rob([1,3,6]), 7)
print(sol.rob([1,6,3]), 6)
# print(sol.rob(), )
