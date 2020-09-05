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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #print(p, q)
        if p is None and q is None:
          return True
        if p is None or q is None:
          return False
        if p.val != q.val:
          return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return True

sol = Solution()

s1 = TreeNode(1)
s2 = TreeNode(2)
s3 = TreeNode(3)
s1.left = s2
s1.right = s3

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3

print(sol.isSameTree(s1, t1), True)

