class Solution(object):
  def maximalRectangle(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if len(matrix) == 1 or len(matrix[0]) == 1:
      return 0
    n = len(matrix)
    m = len(matrix[0])
    left = [0 for i in range(n)]
    right = [n for i in range(n)]
    height = [0 for i in range(n)]
    maxarea = 0
    for i in range(m):
      cur_left = 0
      cur_right = n
      # Compute height
      for j in range(n):
        pass
    return 1
      
sol = Solution()
print(sol.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]), 6)

import numpy as np
print(sol.maximalRectangle(
  [[np.random.choice(["0","1"]) for i in range(100)] for j in range(60)]
), 6)
