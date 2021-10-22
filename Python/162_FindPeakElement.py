class Solution:
  def findPeakElement(self, nums):
    if len(nums) == 1:
      return 0
    if len(nums) == 2:
      return int(nums[0] < nums[1])
    # At least 3 elements
    mid = len(nums) // 2
    #print(nums, mid)
    if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
      return mid
    if nums[mid] > nums[mid-1]:
      return mid + self.findPeakElement(nums[mid:len(nums)])
    return self.findPeakElement(nums[0:mid])
    
  def findPeakElementLinear(self, nums):
    if len(nums) == 1:
      return 0
    if len(nums) == 2:
      if nums[0] > nums[1]:
        return 0
      elif nums[1] > nums[0]:
        return 1
      return None
    if nums[0] > nums[1]:
      return 0
    if nums[len(nums) - 1] > nums[len(nums) - 2]:
      return len(nums) - 1
    for i in range(1, len(nums)-1):
      if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        return i
    return None

sol = Solution()
print(sol.findPeakElement([1,2,3,1]), 2)
print(sol.findPeakElement([1,2,1,3,5,6,4]), 5)
print(sol.findPeakElement([1,2,3]), 2)
print(sol.findPeakElement([3,2,1]), 0)
