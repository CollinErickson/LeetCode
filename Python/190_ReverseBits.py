class Solution:
  def reverseBits(self, n):
    print(n)
    n2 = bin(n)[2:]
    print(n2)
    # int(str(n)[::-1], 2)

sol = Solution()
print(sol.reverseBits(00000010100101000001111010011100))#, 964176192)
# print(sol.reverseBits(11111111111111111111111111111101), 3221225471)
# print(sol.reverseBits(), )
# print(sol.reverseBits(), )
# print(sol.reverseBits(), )
