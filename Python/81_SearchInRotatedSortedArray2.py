class Solution(object):
    def search(self, nums, target, offset=0):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        
        #print "search: ", nums, target, offset
        lennums = len(nums)
        if lennums == 0:
            return -1
        if lennums == 1:
            if nums[0] == target:
                return 0 + offset
            else:
                return -1
            
        if nums[lennums // 2] < nums[0]:
            if target >= nums[0] or target < nums[lennums // 2]:
                return self.search(nums[0:(lennums/2)], target, offset)
            else:
                return self.binary(nums[(lennums/2):lennums], target, offset+lennums/2)
        else:
            if target >= nums[0] and target < nums[lennums / 2]:
                return self.binary(nums[0:(lennums/2)], target, offset)
            else:
                return self.search(nums[(lennums/2):lennums], target, offset+lennums/2)
        return "error"
    def binary(self, nums, target, offset=0):
        #print "binary: ", nums, target, offset
        # nums is sorted array
        lennums = len(nums)
        if lennums == 0:
            return "error 0"
        if lennums == 1:
            if target == nums[0]:
                return 0 + offset
            return -1
        if target < nums[lennums/2]:
            return self.binary(nums[0:(lennums/2)], target, offset)
        return self.binary(nums[(lennums/2):lennums], target, offset=offset + lennums/2)


sol = Solution()
print(sol.search(nums = [2,5,6,0,0,1,2], target = 0), True)