class Solution(object):
    def getRow(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        x = [1]
        for i in range(1, numRows + 1):
            x = [1] +  [i+j for (i,j) in zip(x[0:(len(x)-1)], x[1:len(x)])] + [1]
        return x
          
sol = Solution()

print(sol.getRow(0))
print(sol.getRow(1))
print(sol.getRow(2))
print(sol.getRow(3))
print(sol.getRow(5))
print(sol.getRow(13))
print(sol.getRow(40))
