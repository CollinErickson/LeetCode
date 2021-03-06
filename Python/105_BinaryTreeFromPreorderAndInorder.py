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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
          i = inorder.index(preorder.pop(0))
          root = TreeNode(inorder[i])
          root.left = self.buildTree(preorder, inorder[0:i])
          root.right = self.buildTree(preorder, inorder[(i+1):])
          return root
        return None
        
sol = Solution()

print(sol.buildTree([3,9,20,15,7], [9,3,15,20,7]), "3(9)[20(15)[7]]")
