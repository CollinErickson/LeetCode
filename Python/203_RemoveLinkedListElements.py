
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
  def removeElements(self, head, val: int):
    if head is None:
      return head
    while head and head.val == val:
      head = head.next
    if head is None:
      return None
    prev = head
    cur = head.next
    while cur:
      if cur.val == val:
        cur = cur.next
        prev.next = cur
      else:
        prev = cur
        cur = cur.next
      if cur is None:
        break
    return head

sol = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(6)
n4 = ListNode(3)
n5 = ListNode(4)
n6 = ListNode(5)
n7 = ListNode(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
# n.next = n
# n1 = ListNode()
print(n1)

print(sol.removeElements(n1, 1))
print(sol.removeElements(n1, 6))


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(2)
n4 = ListNode(1)
n1.next = n2
n2.next = n3
n3.next = n4
print(sol.removeElements(n1, 2))
