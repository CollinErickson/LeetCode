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
    def generateTrees(self, n, addval=0):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        trees = []
        if n == 0:
          print("n==0 failure")
          return []
        if n == 1:
          return [TreeNode(1+addval)]
        for i  in range(1, n+1):
          lefttrees  = self.generateTrees(i-1, addval=addval) if i>1 else [None]
          righttrees = self.generateTrees(n - i, addval=addval+i) if i<n else [None]
          for Ltree in lefttrees:
            for Rtree in righttrees:
              #print(i,"LR", Ltree, Rtree, trees)
              newtree = TreeNode(i+addval)
              newtree.left = Ltree
              newtree.right = Rtree
              trees += [newtree]
        
        return trees

sol = Solution()

print(sol.generateTrees(1))
print(sol.generateTrees(2))
print(sol.generateTrees(3))
