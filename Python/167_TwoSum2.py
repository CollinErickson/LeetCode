class Solution:
  def twoSum(self, numbers, target):
    l = 0
    r = len(numbers) - 1
    while l < r:
      if numbers[l] + numbers[r] == target:
        return [l+1, r+1]
      elif numbers[l] + numbers[r] > target:
        r -= 1
      elif numbers[l] + numbers[r] < target:
        l += 1
    return None

sol = Solution()
print(sol.twoSum(numbers = [2,7,11,15], target = 9), [1,2])
print(sol.twoSum(numbers = [2,3,4], target = 6), [1,3])
print(sol.twoSum(numbers = [-1,0], target = -1), [1,2])
print(sol.twoSum([5,25,75], 100), [2,3])
#print(sol.twoSum(), )
#print(sol.twoSum(), )
