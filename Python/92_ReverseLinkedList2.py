# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
     def __repr__(self):
         node = self
         s = ''
         while node is not None:
             s += str(node.val) + '\t'
             node = node.next
         return s
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        node = head
        if m < 1:
            return 'error m < 1', m
        for i in range(m-1):
            print('p1', i)
            node = node.next
        tail1 = node
        node = node.next
        head2 = node
        tail2 = node
        for i in range(n-m):
            print('p2', i)
            nodelast = node
            node = node.next
            head2 = node
            head2.next = nodelast
        head3 = node
        tail1.next = head2
        tail2.next = head3
        
        return head

# Example:
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
#print(l1)
#print(l5)

sol = Solution()
print(sol.reverseBetween(l1, 2, 4))

