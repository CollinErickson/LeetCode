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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
          return False
        if root.left is None and root.right is None:
          return sum == root.val
        if root.left is not None:
          if self.hasPathSum(root.left, sum - root.val):
            return True
        if root.right is not None:
          if self.hasPathSum(root.right, sum - root.val):
            return True
        return False

sol = Solution()

n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(8)
n4 = TreeNode(11)
#n5 = TreeNode(5)
n6 = TreeNode(13)
n7 = TreeNode(4)
n8 = TreeNode(7)
n9 = TreeNode(2)
n10 = TreeNode(1)


n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n6
n3.right = n7
n4.left = n8
n4.right = n9
n7.right = n10

print(n1, sol.hasPathSum(n1, 22), True)
print(n1, sol.hasPathSum(n1, 23), False)
print(n10, sol.hasPathSum(n10, 1), True)
print(n10, sol.hasPathSum(n10, 2), False)

