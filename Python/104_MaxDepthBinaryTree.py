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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
          return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



sol = Solution()


s1 = TreeNode(3)
s2 = TreeNode(9)
s3 = TreeNode(20)
s4 = TreeNode(15)
s5 = TreeNode(7)
s1.left = s2
s1.right = s3
s3.left = s4
s3.right = s5
print(s1)
print(sol.maxDepth(s1), 3)
print(sol.maxDepth(s5), 1)
print(sol.maxDepth(s5.left), 0)


sol = Solution()

s1 = TreeNode(1)
s2 = TreeNode(2)
s3 = TreeNode(3)
s4 = TreeNode(4)
s5 = TreeNode(5)
s1.left = s2
s1.right = s3
s2.left = s4
s3.right = s5
print(s1)
print(sol.maxDepth(s1), 3)
