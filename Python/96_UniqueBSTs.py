class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==0:
          return 1
        if n == 1:
          return 1
        x = [0 for i in range(n+1)]
        x[0] = 1
        x[1] = 1
        for i in range(2, n+1):
          #print('i:', i)
          for j in range(i):
            #print('ij:', i, j, x[j], x[i-j-1])
            x[i] += x[j] * x[i-j-1]
        return x[n]

sol = Solution()
print(sol.numTrees(3), 5)
print(sol.numTrees(4), 14)
print(sol.numTrees(5), 42)
print(sol.numTrees(19), -1)
