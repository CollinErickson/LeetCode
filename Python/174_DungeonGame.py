class Solution:
  def calculateMinimumHP(self, dungeon):
    n = (len(dungeon))
    m = (len(dungeon[0]))
    x = [[None for j in range(m)] for i in range(n)]
    #print(x)
    for j in reversed(range(m)):
      for i in reversed(range(n)):
        #print(i, j, n, m)
        #if i==0 and j==0: print(i, j, n, m, x, dungeon[0][0])
        if i == n-1 and j == m-1:
          x[i][j] = max(1, -dungeon[i][j]+1)
        elif i == n-1:
          x[i][j] = max(1, -dungeon[i][j] + x[i][j+1])
        elif j == m-1:
          x[i][j] = max(1, -dungeon[i][j] + x[i+1][j])
        else:
          x[i][j] = max(1, min(-dungeon[i][j] + x[i+1][j], -dungeon[i][j] + x[i][j+1]))
    #print(x)
    return x[0][0]

sol = Solution()
print(sol.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]), 7)
print(sol.calculateMinimumHP([[0]]), 1)
#print(sol.calculateMinimumHP(), )
#print(sol.calculateMinimumHP(), )
#print(sol.calculateMinimumHP(), )
