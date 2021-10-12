class Solution:
    def maxPoints(self, points):
      if len(points) <= 2:
        return len(points)
      
      out = 0
      for i in range(len(points)):
        d = {}
        overlap = 0
        curmax = 0
        for j in range(i+1, len(points)):
          dx = points[j][0] - points[i][0]
          dy = points[j][1] - points[i][1]
          if dx==0 and dy==0:
            overlap += 1
          gcd = self.gcd(dx, dy)
          dx //= gcd
          dy //= gcd
          if (dx, dy) in d:
            d[(dx, dy)] += 1
          else:
            d[(dx, dy)] = 1
          curmax = max(curmax, d[(dx, dy)])
        out = max(out, curmax + overlap + 1)
      return out
    def gcd(self, a, b):
      if b==0:
        return a
      return self.gcd(b, a%b)


sol = Solution()

print(sol.maxPoints([[1,1]]), 1)
print(sol.maxPoints([[1,1],[3,3]]), 2)
print(sol.maxPoints([[1,1],[2,2],[3,3]]), 3)
print(sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]), 4)
