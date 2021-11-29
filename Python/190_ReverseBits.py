class Solution:
  def reverseBits(self, n):
    # return 1
    # print(n)
    n2 = bin(n)[2:]
    # print(n2, len(n2))
    n3 = "".join(['0' for i in range(32-len(n2))]) + str(n2)
    # print(n3, len(n3))
    n4 = n3[::-1]
    # print(n4, len(n4))
    n5 = int(n4, 2)
    # print(n5)
    return n5
    # int(str(n)[::-1], 2)

sol = Solution()
# print(sol.reverseBits(0000101), 123444)
print(sol.reverseBits(43261596), 964176192)
print(sol.reverseBits(4294967293), 3221225471)
# print(sol.reverseBits(), )
# print(sol.reverseBits(), )
# print(sol.reverseBits(), )
