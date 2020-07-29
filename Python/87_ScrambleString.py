class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # If equal, done
        if s1 == s2:
          return True
        # Check that they have same character frequencies
        a1 = [0 for i in range(26)]
        a2 = [0 for i in range(26)]
        for i in range(len(s1)):
          a1[ord(s1[i])-97] += 1
          a2[ord(s2[i])-97] += 1
        for i in range(len(s1)):
          if a1[i] != a2[i]:
            return False
        # Now check recursively, the hard part
        
        return False
        
sol = Solution()

print(sol.isScramble("great", "rgeat"), True)
print(sol.isScramble("abcde", "caebd"), False)
