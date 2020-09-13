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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
          return True
        if root.left is None and root.right is None:
          return True
        if root.left is None or root.right is None:
          return False
        if root.left.val != root.right.val:
          return False
        
        return self.isReverse(root.left, root.right)
    def isReverse(self, r1, r2):
      if r1 is None and r2 is None:
        return True
      if r1 is None or r2 is None:
        return False
      if r1.val != r2.val:
        return False
      return self.isReverse(r1.left, r2.right) and self.isReverse(r1.right, r2.left)

sol = Solution()

s1 = TreeNode(1)
s2 = TreeNode(2)
s3 = TreeNode(3)
s1.left = s2
s1.right = s3
print(sol.isSymmetric(s1), False)
print(sol.isSymmetric(s2), True)


s1 = TreeNode(1)
s2 = TreeNode(2)
s3 = TreeNode(2)
s1.left = s2
s1.right = s3
print(sol.isSymmetric(s1), True)
print(sol.isSymmetric(s2), True)
