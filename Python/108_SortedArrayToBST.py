# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
     def __repr__(self):
       s = str(self.val)
       if self.left is not None:
         s += "(" + str(self.left) + ")"
       if self.right is not None:
         s += "[" + str(self.right) + "]"
       return s

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
          return None
        if len(nums) == 1:
          return TreeNode(nums[0])
        head = TreeNode(nums[len(nums)//2])
        head.left  = self.sortedArrayToBST(nums[0:(len(nums)//2)])
        if len(nums) > 2:
          head.right = self.sortedArrayToBST(nums[(len(nums)//2+1):])
        return head        

sol = Solution()

print(sol.sortedArrayToBST([-10,-3,0,5,9]))

print(sol.sortedArrayToBST([-10,-3,0,5,9,11]))
print(sol.sortedArrayToBST([-10,-3,0,5,9,11,12]))
print(sol.sortedArrayToBST([]))
