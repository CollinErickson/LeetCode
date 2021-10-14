class Solution:
  def maxProduct(self, nums):
    if len(nums) == 1:
      return nums[0]
    mpnz = []
    i = 0
    left = None
    nozeroyet = True
    while i < len(nums):
      if nums[i] == 0:
        if nozeroyet:
          nozeroyet = False
          mpnz.append(0)
        if left is None:
          pass
        else:
          #print()
          mpnz.append(self.maxProductNoZero(nums[left:i]))
          left = None
      else:
        if left is None:
          left = i
        else:
          pass
      i += 1
    if left is not None:
      mpnz.append(self.maxProductNoZero(nums[left:len(nums)]))
    #print('mpnz', mpnz)
    return max(mpnz)
  def maxProductNoZero(self, nums):
    # nums has no zeros in it
    #print('mpnz nums is', nums)
    if len(nums) == 1:
      return nums[0]
    # Count num negative
    negcount = 0
    for i in range(len(nums)):
      if nums[i] < 0:
        negcount += 1
    #print('negcount is', negcount)
    #if negcount >= len(nums):
    #  return max(nums)
    if negcount % 2 == 0:
      #print('even negs')
      out = 1
      for i in range(len(nums)):
        out *= nums[i]
      return out
    firstnegind = -1
    for i in range(len(nums)):
      if nums[i] < 0:
        firstnegind = i
        break
    if negcount == 1:
      return max([self.maxProductNoZero(nums[0:firstnegind]), self.maxProductNoZero(nums[(firstnegind+1):])])
    lastnegind = -1
    for i in range(len(nums)-1, -1, -1):
      if nums[i] < 0:
        lastnegind = i
        break
    #print('end', firstnegind, lastnegind)
    return max([self.maxProductNoZero(nums[0:lastnegind]), self.maxProductNoZero(nums[(firstnegind+1):])])

sol = Solution()
print(sol.maxProduct([2,3,-2,4]), 6)
print(sol.maxProduct([-2,0,-1]), 0)
print(sol.maxProduct([4]), 4)
print(sol.maxProduct([-4,1,-1]), 4)
print(sol.maxProduct([-4,-1,-1]), 4)
print(sol.maxProduct([-4,-1,2, -1]), 8)

