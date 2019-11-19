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
    def deleteDuplicates(self, head, truehead =None, lastnode=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        print('dd', head.val)
        node = head
        if node.next is None:
            print('a')
            if truehead is None:
                return head
            return truehead
        if truehead is None:
            print('b')
            truehead = head
        if lastnode is not None and lastnode.val == node.val:
            print('c')
            lastnode.next=node.next
            node = lastnode
        return self.deleteDuplicates(head=node.next, truehead=truehead, lastnode=node)
sol = Solution()
n1 = ListNode(1)
s1 = sol.deleteDuplicates(n1)
t1 = s1
while t1 is not None:
    print('cc', t1.val)
    t1 = t1.next
#print(sol.deleteDuplicates(n1))
n2 = ListNode(1)
n1.next = n2
s1 = sol.deleteDuplicates(n1)
t1 = s1
while t1 is not None:
    print('cc', t1.val)
    t1 = t1.next
n3 = ListNode(2)
n2.next = n3
s1 = sol.deleteDuplicates(n1)
t1 = s1
while t1 is not None:
    print('cc', t1.val)
    t1 = t1.next
n4 = ListNode(3)
n3.next = n4
s1 = sol.deleteDuplicates(n1)
t1 = s1
while t1 is not None:
    print('cc', t1.val)
    t1 = t1.next
n5 = ListNode(3)
n4.next = n5
s1 = sol.deleteDuplicates(n1)
t1 = s1
while t1 is not None:
    print('cc', t1.val)
    t1 = t1.next
#print()


n1 = ListNode(1)
n2 = ListNode(1)
n1.next = n2
n3 = ListNode(2)
n2.next = n3


