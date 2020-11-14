# Definition for a binary tree node.
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
  def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        h = self.help(root)
        return max(h[0], h[1])
  def help(self, root):
    if root is None:
      return (0,0)
    if root.left is None:
      L = (0,0)
    else:
      L = self.help(root.left)
    if root.right is None:
      R = (0,0)
    else:
      R = self.help(root.right)
    # p1 is tree that is only below
    p1 = max(L[1] + R[1] + root.val, L[0], R[0])
    # p2 is one sided
    p2 = root.val + max(L[1], R[1])
    return (p1, p2)
        
sol = Solution()

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3

print(sol.maxPathSum(n1), 6)




n1 = TreeNode(-10)
n2 = TreeNode(9)
n3 = TreeNode(20)
n6 = TreeNode(15)
n7 = TreeNode(7)
n1.left = n2
n1.right = n3
n3.left = n6
n3.right = n7

print(sol.maxPathSum(n1), 42)



n1 = TreeNode(-3)

print(sol.maxPathSum(n1), -3)

