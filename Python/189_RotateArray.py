class Solution:
  def rotate(self, nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    km = k % len(nums)
    nums[:] = nums[(-km):] + nums[0:(-km)]
    return nums

sol = Solution()
print(sol.rotate(nums = [1,2,3,4,5,6,7], k = 1), [7,1,2,3,4,5,6])
print(sol.rotate(nums = [1,2,3,4,5,6,7], k = 3), [5,6,7,1,2,3,4])
print(sol.rotate(nums = [-1,-100,3,99], k = 2), [3,99,-1,-100])
print(sol.rotate([1,2], 3), [2,1])
# print(sol.rotate(), )
# print(sol.rotate(), )
