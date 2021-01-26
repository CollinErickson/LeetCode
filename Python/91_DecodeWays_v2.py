class Solution:
    def numDecodings(self, s):
      n = len(s)
      if n == 0:
        return 0
      if n== 1:
        return int(s[0] != "0")
      if n == 2:
        return (s[0]!="0" and s[1]!="0") + (int(s) <= 26 and int(s) >= 10)
      x = [0 for i in range(n)]
      x[n-1] = s[n-1] != "0"
      for i in range(n-2, -1, -1):
        twoint = int(s[i:(i+2)])
        #print(s, 'i:', i, s[i:(i+2)], x)
        if i == n-2 and twoint <= 26 and twoint >= 10:
          x[i] += 1
        if i < n-2 and twoint <= 26 and twoint >= 10:
          x[i] += x[i+2]
        if s[i] != "0":
          x[i] += x[i+1]
      #print("final x is", x)
      return x[0]

sol = Solution()
print(sol.numDecodings('1'), 1)
print(sol.numDecodings('11'), 2)
print(sol.numDecodings('112'), 3)
print(sol.numDecodings('226'), 3)
print(sol.numDecodings('206'), 1)
print(sol.numDecodings('969'), 1)
print(sol.numDecodings('0'), 0)
print(sol.numDecodings('10'), 1)
print(sol.numDecodings('00'), 0)
print(sol.numDecodings('04'), 0)
print(sol.numDecodings('100'), 0)
print(sol.numDecodings('1000'), 0)
print(sol.numDecodings('001000'), 0)
