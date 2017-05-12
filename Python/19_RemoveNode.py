# -*- coding: utf-8 -*-
"""
Created on Wed May 10 08:16:09 2017

@author: cbe117
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l=0
        node = head
        while node != None:
            l += 1
            node = node.next
        node = head
        #print l, n
        if l == n:
            return head.next
        
        for i in range(l-n - 1):
            #nodelast = node
            node = node.next
            #print nodelast.val, node.val, l
        node.next = node.next.next
        return head

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
l.next.next.next.next.next = ListNode(6)
l.next.next.next.next.next.next = ListNode(7)
l.next.next.next.next.next.next.next = ListNode(8)
sol = Solution()
sout = sol.removeNthFromEnd(l, 7)
while sout != None:
    print sout.val,
    sout = sout.next