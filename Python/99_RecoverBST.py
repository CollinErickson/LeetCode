# Definition for a binary tree node.
#e1 = None
#e2 = None
#prevNode = None
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
    e1 = None
    e2 = None
    prevNode = None
    def recoverTree(self, root):
      cur, prev, drops = root, TreeNode(float('-inf')), []
      while cur:
        if cur.left:
          temp = cur.left
          while temp.right and temp.right != cur:
            temp = temp.right
          if not temp.right:
            temp.right, cur = cur, cur.left
            continue
          temp.right = None
        if cur.val < prev.val:
          drops.append((prev, cur))
        prev, cur = cur, cur.right
      drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val
    def inorderMorris(self, root):
      cur = root
      while cur:
        if cur.left:
          temp = cur.left
          while temp.right and temp.right != cur:
            temp = temp.right
          if not temp.right:
            temp.right, cur = cur, cur.left
            continue
          temp.right = None
        print(cur.val)
        cur = cur.right
    def recoverTreeOld(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.e1, self.e2, self.prevNode = None, None, None
        #print('in rc t')
        self.traverse(root)
        if self.e1 is None or self.e2 is None:
          print('failed', self.e1, self.e2)
          return
        #print('in rc t', self.e1, self.e2, self.e1.val, self.e2.val)
        tmp = self.e1.val
        #print('temp e2val', tmp, self.e2.val, self.e1.val)
        #print('before:', root)
        self.e1.val = self.e2.val
        #print('mid:', root)
        self.e2.val = tmp
        #print('after', self.e1.val, self.e2.val, root)
        return
    def traverse(self, node):
      #print('in traverse', node, self.prevNode)
      if node is None:
        return
      self.traverse(node.left)
      if self.prevNode is not None:
        if self.e1 is None and self.prevNode.val >= node.val:
          #print('e1 is ', self.prevNode.val, node.val)
          self.e1 = self.prevNode
        elif self.e1 is not None and self.prevNode.val >= node.val:
          #print('e2 is ', self.prevNode.val, node.val)
          self.e2 = node
      self.prevNode = node
      self.traverse(node.right)
      return

sol = Solution()

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
#print('ttt', t2.val)
#print('t21', print(t2))

t1.left = t3
t3.right = t2
print(t1)
sol.recoverTree(t1)
print(t1, "3(1[2])")


sol = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t3.left = t1
t3.right = t4
t4.left = t2
print(t3)
sol.recoverTree(t3)
print(t3, "2(1)[3[4]]")

