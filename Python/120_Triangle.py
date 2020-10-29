
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle)-2, -1, -1):
          #print(i) #
          for j in range(len(triangle[i])):
            triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        #print(triangle)
        return triangle[0][0]

sol = Solution()

print(sol.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]), 11)