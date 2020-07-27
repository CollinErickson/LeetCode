# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        s = str(self.val)
        if self.next is None:
            return s + "\n"
        else:
            return s + " " + self.next.__repr__()
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        return head

sol = Solution()

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l22 = ListNode(2)

l1.next = l2

print('p1', (l1))

print("s1", sol.partition(l1, 3))
