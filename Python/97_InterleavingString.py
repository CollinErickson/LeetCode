class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
          return False
        if len(s1) == 0:
          return s2==s3
        if len(s2) == 0:
          return s1==s3
        print(s1, s2, s3)
        tab = [[0 for i in range(len(s2))] for j in range(len(s1))]
        
        for i in range(len(s1)):
          for j in range(len(s2)):
            #print(i,j, len(s1), len(s2))
            if i==0 and j==0:
              tab[i][j] = True
            elif i==0:
              tab[i][j] = tab[i][j-1] and s2[j]==s3[j]
            elif j==0:
              tab[i][j] = tab[i-1][j] and s1[i]==s3[i]
            else:
              tab[i][j] = (tab[i][j-1] and s2[j]==s3[i+j]) or (tab[i-1][j] and s1[i]==s3[i+j])
        return tab[len(s1)-1][len(s2)-1]
    def slow_isInterleave(self, s1, s2, s3):
        if s3 == "":
          return s1 == "" and s2 == ""
        if s1 == "":
          return s2 == s3
        if s2 == "":
          return s1 == s3
        # All have len at least 1
        if s1[0] == s3[0] and s2[0] == s3[0]:
          return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
        if s1[0] == s3[0]:
          return self.isInterleave(s1[1:], s2, s3[1:])
        if s2[0] == s3[0]:
          return self.isInterleave(s1, s2[1:], s3[1:])
        return False

sol = Solution()
print(sol.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"), True)
print(sol.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"), False)
print(sol.isInterleave("a", "a", "aa"), True)
print(sol.isInterleave("a", "a", "a"), False)
print(sol.isInterleave("", "", ""), True)
print(sol.isInterleave("a", "", "a"), True)
print(sol.isInterleave(
  "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
"babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
"babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
), True)
