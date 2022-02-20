class Solution:
  def findOrder(self, numCourses: int, prerequisites):
    stack = list()
    visited = [False for i in range(numCourses)]
    adjacent = dict()
    for i in range(len(prerequisites)):
      adjacent[prerequisites[i][0]] = adjacent.get(prerequisites[i][0], []) + [prerequisites[i][1]]
    print('adj:', adjacent)
    def topsort(ind):
      # print('in topsort', ind)
      if not visited[ind]:
        visited[ind] = True
        for j in adjacent.get(ind, []):
          # print('call topsort on ', j)
          topsort(ind)
        stack.append(ind)
    minnotchecked = 0
    while minnotchecked < numCourses:
      print('in while', minnotchecked, visited, stack)
      if not visited[minnotchecked]:
        print('entering', minnotchecked)
        # Not visited yet
        topsort(minnotchecked)
      minnotchecked += 1
    return stack

sol = Solution()
print(sol.findOrder(numCourses = 2, prerequisites = [[1,0]]), [0,1])
print(sol.findOrder(numCourses = 2, prerequisites = [[0,1]]), [1,0])
# print(sol.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]), [0,2,1,3])
# print(sol.findOrder(numCourses = 1, prerequisites = []), [0])
# print(sol.findOrder(9, []), 'any order')
# print(sol.findOrder(), )
# print(sol.findOrder(), )
