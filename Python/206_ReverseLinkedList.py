
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
      s = '' + str(self.val)
      if self.next:
        s += " -> " + str(self.next) + ""
      return s

class Solution:
    def reverseList(self, head):
      if head is None:
        return None
      q = []
      while head is not None:
        q.append(head)
        lasthead = head
        head = head.next
        lasthead.next = None
      head = q.pop()
      cur = head
      while len(q) > .5:
        cur.next = q.pop()
        cur = cur.next
      return head


sol = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
# n.next = n
# n1 = ListNode()
print(n1)

print(sol.reverseList(n1))


n1 = ListNode(1)
print(sol.reverseList(n1))


n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
print(sol.reverseList(n1))

