class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = set()
        for i in range(2**len(nums)):
          strbin = str(bin(i))[2:]
          while len(strbin) < len(nums):
            strbin = '0' + strbin
          b = [j for j in strbin]
          #if len(s)
          #print('here', i, strbin, b)
          #c = [j for j in range(len(nums)) if j=='1']
          t = [nums[j] for j in range(len(nums)) if b[j]=='1' ]
          t.sort()
          t = tuple(t)
          #s += [t]
          s.add(t)
        return s


sol = Solution()
print(sol.subsetsWithDup([1,2,2]))
print(sol.subsetsWithDup([2,1,2]))
str(bin(11))[2:]
[j for j in str(bin(11))[2:]]

ts = set()

