# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 21:23:18 2019

@author: cbe117
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteDuplicates(self, head, truehead =None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        if node.next is None:
            if truehead is None:
                return head
            return truehead
        return self.deleteDuplicates(head=node.next, truehead=truehead)
sol = Solution()
n1 = ListNode(1)
print(sol.deleteDuplicates(n1))
n2 = ListNode(2)
print()