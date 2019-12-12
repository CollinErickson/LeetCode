class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        lastkeepind = 0
        lastnum = None
        lastnumcount = 0
        keepcount = 0
        for num in nums:
            keep = True
            if num == lastnum:
                lastnumcount += 1
                if lastnumcount > 2:
                    keep = False
            else:
                lastnum = num
                lastnumcount = 1
            if keep:
                nums[lastkeepind] = num
                lastkeepind += 1
                keepcount += 1
            else:
                pass
            #print(num, lastnum, lastnumcount, keep)
        #print(lastkeepind)
        if lastkeepind < len(nums):
            nums = nums[0:lastkeepind]
        return nums #len(nums)
        
sol = Solution()
a1 = [1,1,1,2,2,3]
print(sol.removeDuplicates(a1), 5)
print(a1)

a1 = [1]
print(sol.removeDuplicates(a1), 1)
print(a1)
