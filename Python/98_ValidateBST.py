# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def isValidBST(self, root, lessthan=None, greaterthan=None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
          return True
        if (lessthan is not None and root.val>=lessthan) or (greaterthan is not None and root.val<=greaterthan):
          return False
        if not self.isValidBST(root.left, lessthan=root.val, greaterthan=greaterthan):
          return False
        if not self.isValidBST(root.right, lessthan=lessthan, greaterthan=root.val):
          return False
        return True

sol = Solution()

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t2.left = t1
t2.right = t3

print(sol.isValidBST(t2), True)

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t2.left = t3
t2.right = t1

print(sol.isValidBST(t2), False)

print(None, True)
print(sol.isValidBST(t3), True)


t1 = TreeNode(1)
t1b = TreeNode(1)
t1.left = t1b
print(sol.isValidBST(t1), False)
