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
       if self.right is not None:
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
         if x.right is not None:
             q.put(x.right)
       return s

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        #print("Start:", root)
        #if root.val == 2:
          #print(5, root.next)
        if root is not None:
          if root.left is not None and root.right is not None:
            #print("LR", root)
            root.left.next = root.right
            if root.next:
                root.right.next = self.find_next(root.next) #root.next.left if root.next.left is not None else root.next.right
            
            #if root.val == 2:
            #  print("at 2:", root.next)
            self.connect(root.right)
            self.connect(root.left)
          elif root.left is not None: # Only has left
            #print("LL", root)
            if root.next:
              root.left.next = self.find_next(root.next) #root.next.left if root.next.left is not None else root.next.right
            self.connect(root.left)
          elif root.right is not None: # Only has right
            #print("RR", root)
            #print("-", root.next)
            if root.next:
              root.right.next = self.find_next(root.next) #root.next.left if root.next.left is not None else root.next.right
            self.connect(root.right)
        return root
    def find_next(self, root, down=None):
        #print("find", root)
        if root is None:
          return None
        #if down == 0:
        #  return root
        if root.left:
          return root.left #self.find_next(root=root.left)#, down=down-1)
        if root.right:
          return root.right #self.find_next(root=root.right)#, down=down-1)
        if root.next is None:
          return None
        #print("FAIL")
        return self.find_next(root.next) #, down=down)
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
#n3.left = n6
n3.right = n7
print('fn', n1, sol.find_next(n2))

sol.connect(n1)
print(n1.nexts(), "#3#57#")
print(n2.next)


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
#n3.left = n6
n3.right = n6
n4.left = n7
n6.right = n8
print('fn', n1, sol.find_next(n2))

print("===========")
sol.connect(n1)
print(n1.nexts(), "# 3# 56# 8#")
print(n5.next)
