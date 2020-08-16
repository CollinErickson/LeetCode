# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        if root is None:
          return l
        if root.left is not None:
          l += self.inorderTraversal(root.left)
        l += [root.val]
        if root.right is not None:
          l += self.inorderTraversal(root.right)
        return l

sol = Solution()

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.right = n2
n2.left = n3

print(sol.inorderTraversal(n1), [1,3,2])
print(sol.inorderTraversal(None), [])
