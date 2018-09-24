# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 22:14:26 2018

@author: cbe117
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val) + "->" + self.next.__repr__()

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        l = 1
        n = head
        while n.next is not None:
            l += 1
            n = n.next
        n = head
        for i in range(k):
            n = n.next
        newhead = n
        print('newhead is', newhead)
        while n.next is not None:
            n = n.next
        print('n is', n)
        n.next = head
        for i in range(k):
            
            n = n.next
        n.next = None
        return newhead

sol = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print(sol.rotateRight(n1,1), "\n5->1->2->3->4->NULL")
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print(sol.rotateRight(n1,2), "\n4->5->1->2->3->NULL")