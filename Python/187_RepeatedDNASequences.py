class Solution:
  def findRepeatedDnaSequences(self, s):
    if len(s) <= 10:
      return []
    d = {}
    for i in range(len(s)-10+1):
      # print(i)
      si = s[i:(i+10)]
      d[si] = d.get(si, 0) + 1
    dk = list(d.keys())
    # print('dk', dk)
    dv = list(d.values())
    # print(dk, dv)
    dk2 = [dk[i] for i in range(len(dk)) if dv[i] > 1]
    return dk2

sol = Solution()
print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"), ["AAAAACCCCC","CCCCCAAAAA"])
print(sol.findRepeatedDnaSequences("AAAAAAAAAAAAA"), ["AAAAAAAAAA"])
print(sol.findRepeatedDnaSequences("AAAAAAAAAA"), [])
print(sol.findRepeatedDnaSequences("AAAAAAAAAAA"), ["AAAAAAAAAA"])
# print(sol.findRepeatedDnaSequences(), )
# print(sol.findRepeatedDnaSequences(), )
# print(sol.findRepeatedDnaSequences(), )
