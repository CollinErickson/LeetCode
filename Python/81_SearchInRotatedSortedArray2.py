
class Solution(object):
    def search(self, nums, target, offset=0):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return nums[0] == target
        ind = self.binary_index(nums)
        print('ind is', ind, nums)
        if ind < 0: # already in order
            target_index = self.search_inside(nums=nums, target=target)
        elif target < nums[0]: # target in second half
            if target < nums[ind]: # lower than all in nums
                return False
            si = self.search_inside(nums=nums[ind:len(nums)], target=target)
            target_index = (ind + si) if si>=0 else -1
            
        else: # target in first half
            target_index = self.search_inside(nums=nums[0:ind], target=target)
            #print('h1')
        return target_index >= 0
    def search_inside(self, nums, target, offset=0):
        #print("search: ", nums, target, offset)
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
                return self.search_inside(nums[0:(lennums//2)], target, offset)
            else:
                return self.search_inside(nums[(lennums//2):lennums], target, offset+lennums/2)
        else:
            #print(target, nums, lennums, lennums // 2)
            if target >= nums[0] and target < nums[lennums // 2]:
                return self.search_inside(nums[0:(lennums//2)], target, offset)
            else:
                return self.search_inside(nums[(lennums//2):lennums], target, offset+lennums//2)
        return "error"
    def binary_index(self, nums):
        # find where split in nums is
        # [3,4,5,0,1,1] should return 3
        lennums = len(nums)
        if lennums == 0:
            return "error 0"
        if lennums == 1:
            return 0
        if lennums == 2:
            return -1 if nums[0]<=nums[1] else 1
        curindex = 0
        shiftright = lennums // 2
        shiftright = math.ceil(1.*3/2)
        while True:
            #print("w:", curindex, shiftright, nums)
            #if nums[curindex + shiftright] == nums[curindex]:
                #print('midequal')
            if nums[curindex + shiftright] == nums[0]:
                #print('need to check both')
                b1 = self.binary_index(nums[0:(curindex+shiftright)])
                b2 = self.binary_index(nums[(curindex+shiftright):len(nums)])
                return b1 if b1>=0 else b2
            elif nums[curindex + shiftright] > nums[0]:
                curindex += shiftright
            elif nums[curindex+1] < nums[curindex]:
                return curindex+1
            if nums[curindex - 1] >= nums[curindex]:
                #print('r:', curindex, shiftright)
                return curindex + shiftright
            shiftright = shiftright // 2
            #print('while:', curindex, shiftright, lennums)
            while curindex + shiftright >= lennums:
                shiftright = shiftright // 2
            if shiftright == 0:
                return -1 #curindex if nums[curindex]==target else -1
        return "failed2"
        
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
        if target < nums[lennums//2]:
            return self.binary(nums[0:(lennums//2)], target, offset)
        return self.binary(nums[(lennums//2):lennums], target, offset=offset + lennums//2)


sol = Solution()
#print(sol.search(nums = [2,5,6,0,0,1,2], target = 0), True)
if False:
    print(sol.binary_index(nums = [0,1]), -1)
    print(sol.binary_index(nums = [1,0]), 1)
    print(sol.binary_index(nums = [1,0, 1]), 1)
    print(sol.binary_index(nums = [2,5,6,0,0,1,2]), 3)
    print(sol.binary_index(nums = [2,5,6,6,9,0,0,1,2]), 5)
    print(sol.binary_index(nums = [2,5,6,6,9,10,0,0,1,2,3,3,4]), 6)
if True:
    print(sol.search(nums = [0,1], target=1), 1)
    print(sol.search(nums = [1,0], target=1), 0)
    print(sol.search(nums = [1,0, 1], target=1), 0)
    print(sol.search(nums = [2,5,6,0,0,1,2], target=1), 5)
    print(sol.search(nums = [2,5,6,6,9,0,0,1,2], target=1), 7)
    print(sol.search(nums = [2,5,6,6,9,10,0,0,1,2,3,3,4], target=1), 8)
    print(sol.search(nums = [2,5,6,0,0,1,2], target=0), 4)
    print(sol.search(nums = [2,5,6,0,0,1,2], target=4), False)
    print(sol.search(nums = [], target=5), False)
    print(sol.search(nums = [0], target=5), False)
    print(sol.search(nums = [5], target=5), True)
    print(sol.search(nums = [1,1,1,1,1,1,1,2,0], target=0), True)
    print(sol.search(nums = [1,2,0,1,1,1,1,1,1], target=0), True)
    print(sol.search(nums = [1,1], target=0), False)
    print(sol.search(nums = [3,1], target=0), False)
    print(sol.search(nums = [3,1], target=2), False)
    print(sol.search(nums = [1,1,3], target=1), True)


