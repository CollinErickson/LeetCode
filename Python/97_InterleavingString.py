class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
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
