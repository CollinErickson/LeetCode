class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Must have same length and same character frequency
        if len(s1) != len(s2) or sorted(s1)!=sorted(s2):
          return False
        # If equal, done
        if s1 == s2:
          return True
        # All with length 3 or less are scrambles, save time/depth
        if len(s1) < 3.5:
          return True
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
