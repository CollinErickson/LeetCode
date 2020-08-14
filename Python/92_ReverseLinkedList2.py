# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
     def __repr__(self):
         node = self
         s = ''
         while node is not None:
             #print(node.val)
             s += str(node.val) #+ ' => '
             if node.next is not None:
                 s += " => "
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
        if head.next is None:
            return head
        node = head
        #if m <= 1:
        #    return 'error m < 1', m
        for i in range(m-2):
            #print('p1', i)
            node = node.next
        if node is None or node.next is None:
            return head
        if m == 1:
            tail1 = None
        else:
            tail1 = node
            node = node.next
            tail1.next = None
        head2 = node
        tail2 = node
        node = node.next
        tail2.next = None
        if node is None:
            print("Failing with none node")
            tail1.next = head2
            return head1
        for i in range(n-m):
            #print('p2', node.val, i, head2)
            #nodelast = node
            #node = node.next
            #head2 = node
            #head2.next = nodelast
            nextnode = node.next
            newhead2 = node
            oldhead2 = head2
            head2 = newhead2
            head2.next = oldhead2
            node = nextnode
        #print('p3', head)
        head3 = node
        #print('p4', head2)
        
        if m == 1:
            head = head2
        else:
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
print(sol.reverseBetween(l1, 2, 4), [1,4,3,2,5])


l5 = ListNode(5)
print(sol.reverseBetween(l5, 1, 1), [5])

l4 = ListNode(4)
l5 = ListNode(5)
l4.next = l5
print(sol.reverseBetween(l4, 1, 1), [4,5])


l4 = ListNode(4)
l5 = ListNode(5)
l4.next = l5
print(sol.reverseBetween(l4, 1, 2), [5,4])
