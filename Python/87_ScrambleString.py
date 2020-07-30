class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # If equal, done
        if len(s1) != len(s2):
          return False
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
        del a1, a2
        # Now check recursively, the hard part
        for i in range(1, len(s1)):
          if self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:]):
            return True
          if self.isScramble(s1[0:i], s2[(len(s2)-i):]) and self.isScramble(s1[i:], s2[0:(len(s2)-i)]):
            return True
            
        
        return False
        
sol = Solution()

print(sol.isScramble("great", "rgeat"), True)
print(sol.isScramble("abcde", "caebd"), False)
print(sol.isScramble("a", "a"), True)
print(sol.isScramble("ba", "ab"), True)
print(sol.isScramble("ab", "ab"), True)
print(sol.isScramble("", ""), True)
print(sol.isScramble("aa", "a"), False)
print(sol.isScramble("ettztrgij", "irttgetzj"), False)
print(sol.isScramble("phlvandlvyupcq", "paplyvvdhnulcq"), False)
"phlvandlvyupcq"
"paplyvvdhnulcq"
