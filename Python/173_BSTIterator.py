# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
class BSTIterator:
    def __init__(self, root):
      if root is None:
        return
      self.stack = []
      def addtostack(x):
        if x is None:
          return
        if x.right is not None:
          addtostack(x.right)
        self.stack.append(x.val)
        if x.left is not None:
          addtostack(x.left)
        return
      addtostack(root)

    def next(self) -> int:
        return self.stack.pop()

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# This is inefficient since it uses 2^depth memory to 
# store all from start. Instead could just add left nodes
# to stack. When they get popped, then add their right nodes
# to stack.

root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)
# Your BSTIterator object will be instantiated and called as such:
obj = BSTIterator(root)
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
