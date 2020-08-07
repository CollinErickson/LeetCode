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
        if head is None:
            return head
        return self.partition2(None, None, None, None, head, x)
    def partition2(self, head1, head2, tail1, tail2, current,  x):
        if current is None:
            return "FAILED"
        if current.val < x:
            if tail1 is None:
                tail1 = current
                if head1 is None:
                    head1 = tail1
                newcurrent = current.next
                tail1.next = None
                if newcurrent is None: # Done
                    tail1.next = head2
                    return head1
                else:
                    return self.partition2(head1, head2, tail1, tail2, newcurrent, x)
            else: #tail1 is not None
                tail1.next = current
                tail1 = current
                newcurrent = tail1.next
                tail1.next = None
                if newcurrent is None: # Done
                    tail1.next = head2
                    return head1
                return self.partition2(head1, head2, tail1, tail2, newcurrent, x)
        else: #current.val >= x, put on tail2
            if tail2 is None:
                tail2 = current
                if head2 is None:
                    head2 = tail2
                newcurrent = current.next
                tail2.next = None
                if newcurrent is None: # Done
                    if head1 is None:
                        return head2
                    tail1.next = head2
                    return head1
                else:
                    return self.partition2(head1, head2, tail1, tail2, newcurrent, x)
            else: #tail2 is not None
                tail2.next = current
                tail2 = current
                newcurrent = tail2.next
                tail2.next = None
                if newcurrent is None: # Done
                    if head1 is None:
                        return head2
                    tail1.next = head2
                    return head1
                else:
                    return self.partition2(head1, head2, tail1, tail2, newcurrent, x)
                
                    

sol = Solution()

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l22 = ListNode(2)

l1.next = l4
l4.next = l3
l3.next = l2
l2.next = l5
l5.next = l22


print('p1', (l1))

print("s1", sol.partition(l1, 3))
