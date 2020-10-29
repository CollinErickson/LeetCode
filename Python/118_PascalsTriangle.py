class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 0:
          return []
        #o.append([])
        if numRows == 1:
          return [[1]]
        o = [[1 for j in range(i+1)] for i in range(numRows)]
        #print('o is', o)
        for i in range(numRows - 1):
          #print(numRows, i, o)
          n = i + 2
          #a = [1] + [i + j for (i.j) in zip()]
          #a = [1 for j in range(n)]
          for j in range(1, n - 1):
            #print(n, j)
            o[i+1][j] = o[i][j-1] + o[i][j]
          #o[i+1] = a
        return o
sol = Solution()

print(sol.generate(0))
print(sol.generate(1))
print(sol.generate(2))
print(sol.generate(3))
print(sol.generate(5))
print(sol.generate(13))
