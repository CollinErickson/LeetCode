# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 21:42:18 2019

@author: cbe117
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
     def __repr__(self):
         r = str(self.val)
         m = self.next
         while m is not None:
             r += " => " + str(m.val)
             m = m.next
         return r

class Solution(object):
    def deleteDuplicates(self, head, realhead=None, prev_val=None, prev_node=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #print(head, head.next)
        if head is None:
            return realhead
        if realhead is None:
            realhead = head
        #if head.next is None:
        #    return realhead
        
        if prev_val is None:
                return self.deleteDuplicates(head=head.next, realhead=realhead, prev_val=head.val)
        # prev_val is not None, and head.next is not None
        if prev_node is not None and prev_node.val == head.val: # repeat val, so cut out node
            print('cutting out')
            prev_node.next=head.next
            head = prev_node.next
        else:
            prev_node = head
            prev_val = head.val
            head = head.next
        #head_next = None if prev_node.next
        return self.deleteDuplicates(head=head, 
                                     realhead=realhead, 
                                     prev_val=prev_val, prev_node=prev_node)

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(3)
n5 = ListNode(4)
n6 = ListNode(5)
n7 = ListNode(5)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n7

sol = Solution()
s1 = sol.deleteDuplicates(n1)
print(s1)
print(sol.deleteDuplicates(n7))
