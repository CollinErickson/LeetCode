# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
     def __repr__(self):
       s = '' + str(self.val)
       node = self.next
       while node is not None:
         s += " -> " + str(node.val)
         node = node.next
       return s

class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    if headA is None or headB is None:
      return None
    l1 = 0
    n = headA
    while n is not None:
      l1 += 1
      n = n.next
    l2 = 0
    n = headB
    while n is not None:
      l2 += 1
      n = n.next
    #print(l1, l2)
    a = headA
    b = headB
    if l1 > l2:
      for i in range(l1-l2):
        a = a.next
    elif l1 < l2:
      for i in range(l2-l1):
        b = b.next
    while a is not None:
      if a == b:
        return a
      a = a.next
      b = b.next
    #print(a, b)
    return None

sol = Solution()

a1 = ListNode(4)
a2 = ListNode(1)
a3 = ListNode(8)
a4 = ListNode(4)
a5 = ListNode(5)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(1)
b1.next = b2
b2.next = b3
b3.next = a3
print(a1, b1)
print(sol.getIntersectionNode(a1, b1))
