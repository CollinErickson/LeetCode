# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def rightSideView(self, root):
    view = []
    def tmp(node, depth):
      if node:
        if depth >= len(view):
          view.append(node.val)
        tmp(node.right, depth+1)
        tmp(node.left, depth+1)
    tmp(root, 0)
    return view

sol = Solution()
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n1.left = n2
n1.right = n3
n2.right = n5
n3.right = n4
print(sol.rightSideView(n1))
print(sol.rightSideView(None))
