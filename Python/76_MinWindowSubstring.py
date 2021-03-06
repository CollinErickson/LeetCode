class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == "":
          return True
        if s == "":
          return False
        L = 0
        R = 0
        d = {}
        for tt in s:
          d[tt] = 0
        tdict = {}
        for tt in t:
          if tt in tdict.keys():
            tdict[tt] += 1
          else:
            tdict[tt] = 1
        #print(tdict)
        def valid():
          #print('in valid', tdict, d)
          for k in tdict.keys():
            if k not in d.keys() or d[k] < tdict[k]:
              return False
          return True
        shortest = False
        while True:
          isvalid = valid()
          #print("LR", L, R, isvalid)
          if isvalid:
            #print('in if valid', R - L, R, L, (shortest))
            if  shortest is False or R-L <= len(shortest):
              #print('in the if, new shortest')
              shortest = s[L:R]
            #print('middle if')
            d[s[L]] -= 1
            L += 1
            #print('ending if valid')
          else:
            if R == len(s):
              break
            #print('in else', R, s, d)
            d[s[R]] += 1
            R += 1
          #print('checking break')
          #if R > len(s):
          #  break
        #print('check if', shortest, shortest is False)
        if shortest is False:
          #print("changing shortest")
          shortest = ""
        #print('ending', L, R, shortest, len(s))
        return shortest

sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))
print(sol.minWindow("ADOBECODEBANC", "AA"))
print(sol.minWindow("ADOBECODEBANC", "AAA"))
print(sol.minWindow("ADOBECODEBANC", "EC"))
print(sol.minWindow("ADOBECODEBANC", "ACC"))


S = "ADOBECODEBANC"
d = {"A": 1}
d[S[0]]
