class Solution:
  def numIslands(self, grid):
    num = 0
    nexti, nextj = 0,0
    ni, nj = len(grid), len(grid[0])
    while nexti <= ni - 1 and nextj <= nj - 1:
      if grid[nexti][nextj] == "1":
        #print('found', nexti, nextj)
        # Found an island 
        grid[nexti][nextj] = '2'
        num += 1
        q = [(nexti+1, nextj), (nexti-1, nextj), (nexti, nextj+1), (nexti, nextj-1)]
        while len(q) > 0:
          p = q.pop()
          #print('p is', p)
          if p[0] >= 0 and p[0] <= ni-1 and p[1]>=0 and p[1] <= nj-1 and grid[p[0]][p[1]] == '1':
            grid[p[0]][p[1]] = '2'
            q += [(p[0]+1, p[1]), (p[0]-1, p[1]), (p[0], p[1]+1), (p[0], p[1]-1)]
            
      # Increment 
      nextj += 1
      if nextj >= nj:
        nexti, nextj = nexti+1, 0
    # Return num islands
    return num

sol = Solution()
print(sol.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]), 1)
print(sol.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]), 3)
# print(sol.numIslands(), )
# print(sol.numIslands(), )
