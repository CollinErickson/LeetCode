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
  q1 = QQ.LifoQueue()
  q2 = QQ.Queue()
  def zigzagLevelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root is None:
      return []
    a = [[root.val]]
    if root.left is not None:
      self.q1.put([root.left, 1])
    if root.right is not None:
      self.q1.put([root.right, 1])
    level = 1
    #self.q2 = 
    while not self.q1.empty() or not self.q2.empty():
      while not self.q1.empty():
        #print('starting level', level, a)
        n, lev = self.q1.get()
        #print('  got', n, lev)
        if len(a) <= lev:
          a.append([])
        #print('al', a, lev)
        a[lev] += [n.val]
        if n.left is not None:
          self.q2.put([n.left, lev+1])
        if n.right is not None:
          self.q2.put([n.right, lev+1])
      self.q1 = self.q2
      if level%2 == 0:
        self.q2 = QQ.LifoQueue()
      else:
        self.q2 = QQ.Queue()
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
