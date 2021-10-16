class Solution:
  def findMin(self, nums):
    l = len(nums)
    if l <= 1:
      return nums[0]
    if l <= 5:
      return min(nums)
    if nums[0] < nums[l-1]:
      return nums[0]
    # Find where array is flipped
    m = l//2
    x = nums[m]
    #print('m', m, x)
    if x > nums[0]:
      return self.findMin(nums[m:])
    elif x < nums[0]:
      return self.findMin(nums[0:(m+1)])
    else: # x == nums[0]
      return min(self.findMin(nums[0:(m+1)]), self.findMin(nums[m:]))

sol = Solution()
print(sol.findMin([3,4,5,1,2]), 1)
print(sol.findMin([4,5,6,7,0,1,2]), 0)
print(sol.findMin([11,13,15,17]), 11)
print(sol.findMin([11]), 11)
print(sol.findMin([11,13]), 11)
print(sol.findMin([13, 11]), 11)
print(sol.findMin([4,5,6,1,2,3]), 1)
