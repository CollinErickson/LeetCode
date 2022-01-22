class Solution:
  def compareVersion(self, version1: str, version2: str) -> int:
    #print("start", version1, version2)
    v1 = version1.split(".")
    v2 = version2.split(".")
    v1 = [int(x) for x in v1]
    v2 = [int(x) for x in v2]
    for i in range(max(len(v1), len(v2))):
      #print(i)
      if i >= len(v1) and v2[i] > 0:
        return -1
      if i >= len(v2) and v1[i] > 0:
        return 1
      if i < len(v1) and i < len(v2):
        if v2[i] > v1[i]:
          return -1
        if v2[i] < v1[i]:
          return 1
    return 0


sol = Solution()
print(sol.compareVersion(version1 = "1.01", version2 = "1.001"), 0)
print(sol.compareVersion(version1 = "1.0", version2 = "1.0.0"), 0)
print(sol.compareVersion(version1 = "1.0", version2 = "1.0.0.1"), -1)
print(sol.compareVersion(version1 = "0.1", version2 = "1.1"), -1)
print(sol.compareVersion(version1 = "1.0.1", version2 = "1"), 1)
print(sol.compareVersion(version1 = "7.5.2.4", version2 = "7.5.3"), -1)
#print(sol.compareVersion(), )
#print(sol.compareVersion(), )
