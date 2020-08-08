class Solution(object):
    def numDecodings(self, s, include=0):
        """
        :type s: str
        :rtype: int
        """
        #print('here', s)
        if len(s) == 0:
          return include
        isvalid1 = int(s[0] != "0")
        if len(s) == 1:
          return isvalid1
        if s[0] == "0":
          nd1 = 0
        else:
          nd1 = self.numDecodings(s[1:],1)
        if nd1 == 0:
          isvalid1 = 0
        int2 = int(s[0:2])
        isvalid2 = int(int2 > 0 and int2 <= 26) # and len(s)>2)
        if isvalid2>.5:
          nd2 = self.numDecodings(s[2:],1)
        else:
          nd2 = 0
        #print('x', s, include, isvalid1, isvalid2, nd1, nd2)
        include=0
        x = include + isvalid1 + isvalid2 + nd1 + nd2
        x = nd1 + nd2
        return x
        

sol = Solution()
print(sol.numDecodings('12'), 2)
print(sol.numDecodings('226'), 3)
print(sol.numDecodings('30'), 0)
print(sol.numDecodings('3'), 1)
print(sol.numDecodings('0'), 0)
print(sol.numDecodings('11'), 2)
print(sol.numDecodings('10'), 1)
print(sol.numDecodings('91'), 1)
print(sol.numDecodings('111'), 3)
print(sol.numDecodings('01'), 0)
