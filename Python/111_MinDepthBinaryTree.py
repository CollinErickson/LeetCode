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
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
          return 0
        if root.left is None and root.right is None:
          return 1
        if root.left is None:
          return 1 + self.minDepth(root.right)
        if root.right is None:
          return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

sol = Solution()

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)

print(None, sol.minDepth(None), 0)

print(n1, sol.minDepth(n1), 1)

n1.left = n2
print(n1, sol.minDepth(n1), 2)

n2.left = n4
print(n1, sol.minDepth(n1), 3)

n2.right = n5
print(n1, sol.minDepth(n1), 2)

n1.right = n3
print(n1, sol.minDepth(n1), 2)

n3.left = n6
print(n1, sol.minDepth(n1), 2)

n4.left = n7
print(n2, sol.minDepth(n2), 2)
print(n3, sol.minDepth(n3), 2)
print(n1, sol.minDepth(n1), 3)
