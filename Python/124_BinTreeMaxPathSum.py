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
    def rec(node):
      nonlocal ans
      if not node:
        return 0
      left = rec(node.left)
      right = rec(node.right)
      ans = max(ans, max(node.val, max(left, right)+node.val, left+right+node.val))
      return max(node.val, left+node.val, right+node.val)
    
    ans = -1001
    rec(root)
    return ans
  def maxPathSumBAD(self, root):
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
    if root.left is None and root.right is None:
      p1 = root.val
      p2 = root.val
    elif root.left is None and root.right is not None:
      R = self.help(root.right)
      p1 = max(R[1] + root.val, R[0], root.val)
      p2 = root.val + max(R[1], 0)
    elif root.left is not None and root.right is None:
      L = self.help(root.left)
      p1 = max(L[1] + root.val, L[0], root.val)
      p2 = root.val + max(L[1], 0)
    elif root.left is not None and root.right is not None:
      L = self.help(root.left)
      R = self.help(root.right)
      # p1 is tree that is only below
      p1 = max(L[1] + R[1] + root.val, L[1] + root.val, R[1] + root.val, L[0], R[0], root.val)
      # p2 is one sided
      p2 = root.val + max(L[1], R[1], 0)
    else:
      assert 1==0
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



n1 = TreeNode(-11)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3

print(sol.maxPathSum(n1), 3)

n1 = TreeNode(1)
n2 = TreeNode(-2)
n3 = TreeNode(-3)
n1.left = n2
n1.right = n3

print(sol.maxPathSum(n1), 1)


n1 = TreeNode(-1)
n2 = TreeNode(-2)
n3 = TreeNode(-3)
n1.left = n2
n1.right = n3

print(sol.maxPathSum(n1), -1)



n1 = TreeNode(-1)
n3 = TreeNode(9)
n6 = TreeNode(-6)
n7 = TreeNode(3)
n8 = TreeNode(-2)
n1.right = n3
n3.left = n6
n3.right = n7
n7.right = n8
#print(n1)
print(sol.maxPathSum(n1), 12)
print(sol.maxPathSum(n3), 12)
print(sol.maxPathSum(n7), 3)
