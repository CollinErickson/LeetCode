import functools
class Solution:
  def largestNumber(self, nums):
    s = [str(i) for i in nums]
    #print("unsorted:", s)
    s.sort(reverse=False, key=functools.cmp_to_key(comp))
    #print("sorted:", s)
    x = "".join(s)
    return x


def comp(x,y):
  i=0
  while True:
    #print('comp i', i, x, y)
    if len(x) <= i and len(y) <= i:
      return 0
    #print('c1') #, x, y, 1 if y[i] > x[0] else -1)
    if len(x) <= i:
      #print('c1b', x, y, 1 if y[i] > x[0] else -1)
      return 1 if y[i] > x[0] else -1
    #print('c2')
    if len(y) <= i:
      return -1 if x[i] > y[0] else 1
    #print('c3', len(x), len(y), i)
    if x[i] < y[i]:
      return 1
    #print('c4')
    if x[i] > y[i]:
      return -1
    i += 1
  print("error")
  return

#print("comp", comp("4","2"))
#print("comp", comp("2","4"))
#print("comp", comp("0","0"))

sol = Solution()
# print(sol.largestNumber([3,30,34,5,9]), "9534330")
# print(sol.largestNumber([1]), "1")
# print(sol.largestNumber([10]), "10")
# print(sol.largestNumber([2,4,20,21,22,0,2]), "422221200")
# print(sol.largestNumber([2,4,0,2]), "4220")
# print(sol.largestNumber([7,5,8,3]), "8753")
# print(sol.largestNumber([5,7,3,5]), "7553")
# print(sol.largestNumber([3,30,34,5,9]), "9534330")
# print(sol.largestNumber([3, 30, 39]), "39330")
print(sol.largestNumber([432,43243]), "43243432")
# print(sol.largestNumber(), )
