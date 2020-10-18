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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        xx = self.hRL(root)
        #print('xx', xx)
        return not (xx is False)
    def hRL(self, root):
      if root is None:
        return (0,0)
      
      hR = self.hRL(root.right)
      hL = self.hRL(root.left)
      #print("h:", hR, hL)
      if hR is False or hL is False:
        return False
      if  max(hL + hR) - min(hL + hR) > 1:
        return False
      return (1 + min(hR + hL), 1 + max(hR + hL))
min(0,1)
sol = Solution()

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)

print(sol.isBalanced(n1), True)

n1.left = n2
print(sol.isBalanced(n1), True)

n2.left = n3
print(n1, sol.isBalanced(n1), False)

n2.right = n4
print(n1, sol.isBalanced(n1), False)

n1.right = n5
print(n1, sol.isBalanced(n1), True)
