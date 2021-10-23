class Solution:
  def maximumGap(self, nums):
    #print(nums)
    if len(nums) < 1.5:
      return 0
    if len(nums) == 2:
      return max(nums) - min(nums)
    n = len(nums)
    mn = min(nums)
    mx = max(nums)
    if mx - mn <= 1:
      return mx - mn
    # Make buckets
    numbuckets = n-1
    gap = int(math.ceil((mx - mn+1) / numbuckets))
    bmin = [None for i in range(numbuckets)]
    bmax = [None for i in range(numbuckets)]
    # Loop over nums, put in bucket
    for i in range(n):
      bucketi = (nums[i] - mn) // gap
      #print(' - ', i, numbuckets, gap, nums[i], bucketi, bmin, bmax)
      bmin[bucketi] = min(bmin[bucketi], nums[i]) if bmin[bucketi] is not None else nums[i]
      bmax[bucketi] = max(bmax[bucketi], nums[i]) if bmax[bucketi] is not None else nums[i]
    #print(bmin, bmax)
    out = bmax[0] - bmin[0]
    lastmax = bmax[0]
    for i in range(1, numbuckets):
      if bmin[i] is not None:
        out = max(out, bmin[i] - lastmax)
        lastmax = bmax[i]
      #out = min(out, bmin[i+1] - bmax[i]) if out is not None else (bmin[i+1] - bmax[i])
    return out
import math

sol = Solution()
print(sol.maximumGap([10]), 0)
print(sol.maximumGap([3,6,9,1]), 3)
print(sol.maximumGap([3,6,9,1,100]), 91)
print(sol.maximumGap([1, 10000000]), 9999999)
print(sol.maximumGap([100,3,2,1]), 97)
