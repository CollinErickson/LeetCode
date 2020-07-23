class Solution(object):
  def maximalRectangle(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    biggest = 0
    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        for i2 in range(i+1,len(matrix)+1):
          #breakout1 = False
          # Check new values x[i2-1][]
          for j2 in range(j+1, len(matrix[0])+1):
            #if (i2-i) * (j2-j) <= biggest:
            #  #breakout1 = True
            #  continue #break
            #print(i,i2,j,j2)
            # Check that matrix[i:i2, j:j2] are all 1
            # Only check new j2, matrix[]
            breakout = False
            for iii in range(i,i2):
              for jjj in range(j,j2):
                #if i==1 and i2==3 and j==2 and j2==5:
                #  #print(i,i2,j,j2,iii,jjj, matrix[iii][jjj], biggest)
                if matrix[iii][jjj] == "0":
                  breakout = True
                  break
              if breakout:
                break
            else:
              #print('found valid', (i2-i) * (j2-j), (i2-i) , (j2-j))
              # Is valid
              if (i2-i) * (j2-j) > biggest:
                biggest = (i2-i) * (j2-j)
          #if breakout1:
          #  break
    return biggest
        
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
