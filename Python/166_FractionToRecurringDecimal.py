class Solution:
  def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    if numerator > denominator:
      x = numerator // denominator
      numerator = numerator - x * denominator
    else:
      x = "0."
    if numerator == 0:
      return x
    # Has a leftover
    dic = {}
    decplace = 1
    #while True:
    #  
    return x

sol = Solution()
print(sol.fractionToDecimal(numerator = 1, denominator = 2), "0.5")
print(sol.fractionToDecimal(numerator = 2, denominator = 1), "2")
print(sol.fractionToDecimal(numerator = 2, denominator = 3), "0.(6)")
print(sol.fractionToDecimal(numerator = 4, denominator = 333), "0.(012)")
print(sol.fractionToDecimal(numerator = 1, denominator = 5), "0.2")
#print(sol.fractionToDecimal(), )
#print(sol.fractionToDecimal(), )
