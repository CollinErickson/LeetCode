class Solution:
  d1 = {}
  d2 = {}
  def canFinish(self, numCourses: int, prerequisites) -> bool:
    # Direct requirements
    self.d1 = {}
    for i in range(len(prerequisites)):
      e1 = self.d1.get(prerequisites[i][0], [])
      e1.append(prerequisites[i][1])
      self.d1[prerequisites[i][0]] = e1
    # print(self.d1)
    # Direct and indirect requirements
    self.d2 = {}
    for i in range(numCourses):
      # print('loop2', i)
      dep = self.getall(i, [])
      if type(dep) == bool:
        return False
      self.d2[i] = dep
    
    return True
  def getall(self, i, l):
    # print('in getall', i, l)
    if i in l:
      return False
    if i in self.d2:
      return self.d2[i]
    dep = []
    if i in self.d1:
      for j in self.d1[i]:
        if j in self.d2:
          dep.append(self.d2[j])
        else:
          depj = self.getall(j, l + [i])
          if type(depj) == bool:
            return False
          dep.append(depj)
    return dep

sol = Solution()
print(sol.canFinish(numCourses = 2, prerequisites = [[1,0]]), True)
print(sol.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]), False)
print(sol.canFinish(numCourses = 20, prerequisites = [[1,0],[2,1],[3,1]]), True)
# print(sol.canFinish(), )
# print(sol.canFinish(), )
# print(sol.canFinish(), )
