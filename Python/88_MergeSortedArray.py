class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
          if nums1[m-1] > nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
          else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
        if n > 0:
          nums1[:n] = nums2[:n]
        return nums1
    def mergefail(self):
        if m == 0:
          for i in range(n):
            nums1[i] = nums2[i]
          return nums1
        if n  == 0:
          return nums1
        iplace = 0
        isave = None
        isavenext = m
        j = 0
        x1 = nums1[0]
        x2 = nums2[0]
        while True:
          print(iplace, isave, isavenext, j, x1, x2, nums1)
          if x1 is None and x2 is None:
            break
          if x2 is None or (x1 is not None and x1 <= x2):
            if isave is None:
              # None are saved, just increase index
              iplace += 1
              if iplace >= m:
                x1 = None
              else:
                x1 = nums1[iplace]
            else: # Current x1 is saved in isave
              nums1[isave] = 0
              nums1[iplace] = x1
              iplace += 1
              #x1 = nums1[isave]
              isave += 1
              if isave >= m+n:
                isave = m
              if isave == isavenext:
                isave = None
                x1 = None
              else:
                x1 = nums1[isave]
              
          else: # nums2 is less
            print('in branch 2', j, nums2[j])
            #if isave is 
            nums1[iplace] = nums2[j]
            j += 1
            if j < n:
              print('in branch 2b')
              # Move nums1 into save spot
              if x1 is not None:
                if isave is None:
                  isave = isavenext
                nums1[isavenext] = x1
                isavenext += 1
                if isavenext >= m + n:
                  isavenext = m
              nums1[iplace] = x2
              x2 = nums2[j]
            else:
              x2 = None
            iplace += 1
          #break
        
        return nums1

sol = Solution()
print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(sol.merge([4,5,6,0,0,0], 3, [1,2,3], 3))
print(sol.merge([1,2,3], 3, [], 0))
print(sol.merge([0,0,0], 0, [1,2,3], 3))
print(sol.merge([2,0], 1, [1], 1))

