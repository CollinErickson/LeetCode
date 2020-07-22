class Solution(object):
  def maximalRectangle(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if len(matrix) <= 1 or len(matrix[0]) <= 1:
      return 0
    m = len(matrix)
    n = len(matrix[0])
    left = [0 for i in range(n)]
    right = [n for i in range(n)]
    height = [0 for i in range(n)]
    maxarea = 0
    for i in range(m):
      #print(i, left, right, height)
      cur_left = 0
      cur_right = n
      # Compute height
      for j in range(n):
        if matrix[i][j] == "1":
          height[j] += 1
        else:
          height[j] = 0
      # Computer left, go left to right
      for j in range(n):
        if matrix[i][j] == "1":
          left[j] = max(left[j], cur_left)
        else:
          left[j] = 0
          cur_left = j+1
      # Computer right, go right to left
      for j in range(n-1,-1, -1):
        if matrix[i][j] == "1":
          right[j] = min(right[j], cur_right)
        else:
          right[j] = n
          cur_right = j
      for j in range(n):
        #print((right[j]-left[j])*height[j])
        maxarea = max(maxarea, (right[j]-left[j])*height[j])
        
    return maxarea
      
sol = Solution()
print(sol.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]), 6)

import numpy as np
print(sol.maximalRectangle(
  [[np.random.choice(["0","1"]) for i in range(100)] for j in range(160)]
), "?")

print(sol.maximalRectangle([]), 0)

print(sol.maximalRectangle([["1"]]), 1)
print(sol.maximalRectangle([["1", "0"]]), 1)
print(sol.maximalRectangle([["1", "2"]]), 2)
