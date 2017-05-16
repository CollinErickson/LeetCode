# -*- coding: utf-8 -*-
"""
Created on Mon May 15 14:29:37 2017

@author: cbe117
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        a = head
        if a.next == None:
            return head
        b = head.next
        rhead = b
        #print 'rhead val is ', rhead.val
        a.next = b.next
        b.next = a
        #a = a.next
        while a.next != None:
            #print a.val,
            c = a.next
            if c.next == None:
                #print "break"
                break
            d = c.next
            #print a.val, c.val, d.val,
            a.next = d
            c.next = d.next
            d.next = c
            a = c
            #print a.val
        return rhead

sol = Solution()
print "\n", sol.swapPairs(None)
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(6)
l1.next.next.next.next.next.next = ListNode(7)
print
def printll(ll):
    if ll == None:
        return
    while ll != None:
        print ll.val,
        ll = ll.next
printll(sol.swapPairs(l1))
#l2 = ListNode(1)
#l2.next = ListNode(3)
#l2.next.next = ListNode(5)
#l2.next.next.next = ListNode(7)
#print "\ncombine two"
#printll(sol.mergeKLists([l1, l2]))
 