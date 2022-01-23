class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    n = len(s)
    ds = {}
    for  i in range(n):
      di = ds.get(s[i], [])
      di.append(i)
      ds[s[i]] = di
    dt = {}
    for  i in range(n):
      di = dt.get(t[i], [])
      di.append(i)
      dt[t[i]] = di
    for k in ds.keys():
      inds = ds[k]
      t1 = t[inds[0]]
      if len(inds) > 1:
        for j in range(1, len(inds)):
          if t[inds[j]] != t1:
            return False
      if len(inds) != len(dt[t1]):
        return False
    return True

sol = Solution()
print(sol.isIsomorphic(s = "egg", t = "add"), True)
print(sol.isIsomorphic(s = "foo", t = "bar"), False)
print(sol.isIsomorphic(s = "paper", t = "title"), True)
print(sol.isIsomorphic('badc', 'baba'), False)
# print(sol.isIsomorphic(), )
