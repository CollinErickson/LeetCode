class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ls = len(s)
        lt = len(t)
        if len(s) < len(t):
          return 0
        if len(s) == len(t):
          return int(s == t)
        m = [[0 for j in range(len(t))] for i in range(len(s))]
        for i in range(len(s)):
          for j in range(min(i+1, len(t))):
            #print('ij are', i,j, s[0:(i+1)], t[0:(j+1)])
            if i == 0:
              m[i][j] = int(s[0:(i+1)] == t[0:(j+1)])
            elif j == 0:
              m[i][j] = m[i-1][j] + int(t[0] == s[i])
            else:
              m[i][j] = m[i-1][j]
              if s[i] == t[j]:
                m[i][j] += m[i-1][j-1]
        #print('m is', m)
        return m[ls-1][lt-1]

sol = Solution()

print(sol.numDistinct("r", "r"), 1)
print(sol.numDistinct("r", "rr"), 0)
print(sol.numDistinct("rr", "r"), 2)
print(sol.numDistinct("rabbbit", "rabbit"), 3)
print(sol.numDistinct("babgbag", "bag"), 5)
