# -*- coding: utf-8 -*-
"""
Created on Tue May 09 13:47:45 2017

@author: cbe117
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None and l2==None:
            return None
        if l1==None:
            return l2
        if l2==None:
            return l1
        l3 = None
        if l1.val < l2.val:
            l3 = l1
            l1 = l1.next
        else:
            l3 = l2
            l2 = l2.next
        l0 = l3
        while True:
            #print l1.val, l2.val
            if l1 == None and l2 == None:
                break
            add_first = (l1!=None)
            if l1 != None and l2 != None:
                add_first = l1.val < l2.val
            if add_first:
                l3.next = l1
                l3 = l3.next
                l1 = l1.next
                #print "added first"#, l1.val, l2.val
            else: #if l2 == None:
                l3.next = l2
                l3 = l3.next
                l2 = l2.next
                #print "added second"#, l1.val, l2.val
        return l0

l1 = ListNode(1)
l1.next = ListNode(3)
l2 = ListNode(2)
l2.next = ListNode(5)
sol = Solution()
l3 = sol.mergeTwoLists(l1, l2)
while l3 != None:
    print l3.val
    l3 = l3.next