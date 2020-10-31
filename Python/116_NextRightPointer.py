"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import queue
class Node(object):
     def __init__(self, val=0, left=None, right=None, next=None):
         self.val = val
         self.left = left
         self.right = right
         self.next = next
     def __repr__(self):
       s = str(self.val)
       if self.left is not None:
         s += "(" + str(self.left) + ")"
       if self.right is not None:
         s += "[" + str(self.right) + "]"
       return s
     def nexts(self):
       s = str(self.next.val) if self.next is not None else "#"
       q = queue.Queue()
       if self.left is not None:
           q.put(self.left)
           q.put(self.right)
       #print(dir(q))
       while q.qsize() > 0:
         #print('qget', q.qsize(), q.get(), q.qsize())
         #break
         x = q.get()
         #print('inq', x)
         s += str(x.next.val) if x.next is not None else "#"
         if x.left is not None:
             q.put(x.left)
             q.put(x.right)
       return s

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not (root is None or root.left is None):
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.right)
            self.connect(root.left)
        return root
[] is None
sol = Solution()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.left = n2
n1.right = n3

sol.connect(n1)
print(n1.nexts())


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

sol.connect(n1)
print(n1.nexts())
print(n2.next)
