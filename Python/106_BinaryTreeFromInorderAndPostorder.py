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
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/221681/Don't-use-top-voted-Python-solution-for-interview-here-is-why.
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        map_inorder=  {}
        for i, val in enumerate(inorder):
            map_inorder[val] = i
        def recur(low, high):
            if low > high:
                return None
            x = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            x.right = recur(mid+1, high)
            x.left  = recur(low, mid-1)
            return x
            
        return recur(0, len(inorder)-1)
        
sol = Solution()

print(sol.buildTree([9,3,15,20,7], [9,15,7,20,3]), "3(9)[20(15)[7]]")
