class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        iplace = 0
        isave = None
        isavenext = m
        j = 0
        x1 = nums1[0]
        x2 = nums2[0]
        while True:
          if x1 is None and x2 is None:
            break
          if x2 is None or x1 <= x2:
            if isave is None:
              # None are saved, just increase index
              iplace += 1
              x1 = nums[iplace]
            else:
              nums1[iplace] = x1
              iplace += 1
              
          else: # nums2 is less
            nums1[iplace] = nums2[j]
            j += 1
            if j < n:
              # Move nums1 into save spot
              if x1 is not None:
                
              nums1[iplace] = x2
              x2 = nums2[j]
            else:
              x2 = None
            
          break
        
        return nums1

sol = Solution()
print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))

