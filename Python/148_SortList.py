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
    def sortList(self, head: ListNode) -> ListNode:
      #print('starting', head)
      if head is None or head.next is None:
        return head
      if head.next.next is None:
        if head.val < head.next.val:
          return head
        n1 = head
        n2 = head.next
        n1.next = None
        n2.next = n1
        return n2
      if head.next.next.next is None:
        #print('fix length 3 now')
        n1 = head
        n2 = head.next
        n3 = n2.next
        n1.next = None
        head = n1
        tortoise = n2
      else:
        prehare = head
        hare = head.next
        tortoise = head
        pretortoise = None
        while hare.next is not None and hare.next.next is not None:
          prehare = hare.next
          hare = hare.next.next
          pretortoise = tortoise
          tortoise = tortoise.next
        #print('hare is', hare, 'tort is', tortoise)
        pretortoise.next = None
        #print('half 1 is', head, 'half 2 is', tortoise)
      
      #print('about to do c1,c2', head, tortoise)
      c1 = self.sortList(head)
      c2 = self.sortList(tortoise)
      c3 = self.merge(c1, c2)
      return c3
    def merge(self, c1, c2):
      if c1 is None:
        return c2
      if c2 is None:
        return c1
      if c1.val < c2.val:
        c3 = c1
        c1 = c1.next
        c3.next = None
      else:
        c3 = c2
        c2 = c2.next
        c3.next = None
      c4 = self.merge(c1, c2)
      c3.next = c4
      return c3

n1 = ListNode(4)
n2 = ListNode(2)
n3 = ListNode(1)
n4 = ListNode(3)
n1.next = n2
n2.next = n3
n3.next = n4
print(n1)

sol = Solution()
print('result is:', sol.sortList(n1))



h = ListNode(5)
t = h
import random
for i in range(10):
  t.next = ListNode(random.random())
  t = t.next
print('h is', h)
print(sol.sortList(h))
