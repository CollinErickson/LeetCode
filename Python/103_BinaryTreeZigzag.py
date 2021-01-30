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
import queue as QQ
class Solution(object):
  def zigzagLevelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root is None:
      return []
    a = [[root.val]]
    
    q1 = QQ.LifoQueue()
    q2 = QQ.LifoQueue()
    if root.left is not None:
      #print('L put in ', root.left.val)
      q1.put([root.left, 1])
    if root.right is not None:
      #print('R put in ', root.right.val)
      q1.put([root.right, 1])
    level = 1
    #q2 = 
    while not q1.empty() or not q2.empty():
      #print('starting level', level, a)
      while not q1.empty():
        n, lev = q1.get()
        #print('  got', n, lev)
        if len(a) <= lev:
          a.append([])
        #print('al', a, lev)
        a[lev] += [n.val]
        if lev%2 == 0:
          if n.left is not None:
            q2.put([n.left, lev+1])
          if n.right is not None:
            q2.put([n.right, lev+1])
        else:
          if n.right is not None:
            q2.put([n.right, lev+1])
          if n.left is not None:
            q2.put([n.left, lev+1])
      q1 = q2
      if level%2 == 0:
        q2 = QQ.LifoQueue()
      else:
        q2 = QQ.LifoQueue()
      level += 1
    
    return a




sol = Solution()


s1 = TreeNode(3)
s2 = TreeNode(9)
s3 = TreeNode(20)
s4 = TreeNode(15)
s5 = TreeNode(7)
s1.left = s2
s1.right = s3
s3.left = s4
s3.right = s5
print(s1)
print(sol.zigzagLevelOrder(s1), [[3],[20,9], [15,7]])


sol = Solution()

s1 = TreeNode(1)
s2 = TreeNode(2)
s3 = TreeNode(3)
s4 = TreeNode(4)
s5 = TreeNode(5)
s1.left = s2
s1.right = s3
s2.left = s4
s3.right = s5
print(s1)
print(sol.zigzagLevelOrder(s1), [[1],[3,2], [4,5]])
