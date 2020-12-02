# Definition for a binary tree node.
class TreeNode:
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
class Solution:
    def sumNumbers(self, root: TreeNode, chain=0) -> int:
      if root is None:
        return 0
      if root.left is None and root.right is None:
        return chain*10 + root.val
      outsum = 0
      if root.left is not None:
        outsum += self.sumNumbers(root.left, chain=chain*10+root.val)
      if root.right is not None:
        outsum += self.sumNumbers(root.right, chain=chain*10+root.val)
      return outsum

sol = Solution()
print(sol.sumNumbers(None), 0)

e1 = TreeNode(3)
e2 = TreeNode(4)
e3 = TreeNode(5)
e1.left = e2
e1.right = e3
print(sol.sumNumbers(e3), 5)
print(sol.sumNumbers(e1), 69)
