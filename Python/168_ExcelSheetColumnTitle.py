class Solution:
  def convertToTitle(self, columnNumber):
    xprev = 0
    x = 26
    i = 2
    while x < columnNumber:
      xprev = x
      x += 26**i
      i += 1
      if i>100: break
    nchar = i - 1
    c = [-1 for j in range(nchar)]
    diff = columnNumber - xprev - 1
    for j in range(nchar):
      c[j] = diff %26
      diff = diff // 26
    s = [chr(97+j) for j in c]
    s.reverse()
    s = ''.join(s).upper()
    #print(columnNumber, x, xprev, i)
    return s

sol = Solution()
print(sol.convertToTitle(1), "A")
print(sol.convertToTitle(2), "B")
print(sol.convertToTitle(27), "AA")
print(sol.convertToTitle(28), "AB")
print(sol.convertToTitle(701), "ZY")
print(sol.convertToTitle(2147483647), "FXSHRXW")
print(sol.convertToTitle(2**30), "?")
