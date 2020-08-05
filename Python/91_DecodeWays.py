class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        print('here', s)
        if len(s) == 0:
          return 0
        isvalid1 = s[0] != "0"
        if len(s) == 1:
          return 0 #isvalid1
        int2 = int(s[0:2])
        isvalid2 = int(int2 > 0 and int2 < 26 and len(s)>2)
        x = 1 + isvalid1 + isvalid2 + self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        return x
        

sol = Solution()
print(sol.numDecodings('12'), 2)
print(sol.numDecodings('226'), 3)
print(sol.numDecodings('30'), 0)
