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
        while n.next is not None:
            n = n.next
        n.next = head
        n = head
        for i in range(k):
            n = n.next
        n.next = None
        return newhead

