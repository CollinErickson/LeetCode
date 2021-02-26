# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
         self.val = x
         self.next = None
   #def __repr__(self):
   #  s = self.val #"Node(" + str(self.val) + "," + (str(self.random.val) if self.random else "-") + ")"
   #    if self.next:
   #      s +=  " -> " + str(self.next) 
   #    return s

class Solution:
    def detectCycle(self, head):
      if head is None or head.next is None:
          return None
      node = head
      d = {}
      while node is not None:
         nh = node.__hash__()
         #print('nh', nh)
         if nh in d:
            return d[nh]
         d[nh] = node
         node = node.next
         
      return None
      
sol = Solution()
a1 = ListNode(3)
a2 = ListNode(2)
a3 = ListNode(0)
a4 = ListNode(4)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a2
print(sol.detectCycle(a1), a2)


a1 = ListNode(3)
a2 = ListNode(2)
a1.next = a2
a2.next = a1
print(sol.detectCycle(a1), a1)


a1 = ListNode(3)
a2 = ListNode(2)
a1.next = a2
print(sol.detectCycle(a1), None)


a1 = ListNode(3)
print(sol.detectCycle(a1), None)


a1 = ListNode(3)
a2 = ListNode(3)
a1.next = a2
print(sol.detectCycle(a1), None)
