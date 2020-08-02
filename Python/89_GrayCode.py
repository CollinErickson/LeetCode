class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n <= 0:
          return [0]
        if n == 1:
          return [0,1]
        x = self.grayCode2n(n)
        return [int(i, 2) for i in x]
    def grayCode2n(self, n):
      if n<=0:
        return ['0']
      if n==1:
        return ['0','1']
      oneless = self.grayCode2n(n-1)
      onelessreflected = list(reversed(oneless))
      a = ['0' + x for x in oneless]
      b = ['1' + x for x in onelessreflected]
      return a+b

sol = Solution()
print(sol.grayCode(0))
print(sol.grayCode(1))
print(sol.grayCode(2))
print(sol.grayCode(3))
print(sol.grayCode(4))
#print(sol.grayCode2n(3))
bin(3)
list(reversed([1,3,5,7]))
