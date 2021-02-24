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
    def hasCycle(self, head):
      if head is None or head.next is None:
          return False
      tortoise = head
      hare = head
      while tortoise.next and hare.next and hare.next.next:
        tortoise = tortoise.next
        hare = hare.next.next
        if hare == tortoise:
          return True
      return False

sol = Solution()
a1 = ListNode(3)
a2 = ListNode(2)
a3 = ListNode(0)
a4 = ListNode(4)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a2
print(sol.hasCycle(a1), True)


a1 = ListNode(3)
a2 = ListNode(2)
a1.next = a2
a2.next = a1
print(sol.hasCycle(a1), True)


a1 = ListNode(3)
a2 = ListNode(2)
a1.next = a2
print(sol.hasCycle(a1), False)


a1 = ListNode(3)
print(sol.hasCycle(a1), False)


a1 = ListNode(3)
a2 = ListNode(3)
a1.next = a2
print(sol.hasCycle(a1), False)
