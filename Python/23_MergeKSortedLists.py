# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:14:33 2017

@author: cbe117
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lenl = len(lists)
        if lenl == 0:
            return []
        if lenl == 1:
            return lists[0]
        finf = float('inf')
        nextvals = [finf for l in range(lenl)]
        for i in range(lenl):
            if lists[i] != None:
                nextvals[i] = lists[i].val
        mind = min(xrange(len(nextvals)), key=nextvals.__getitem__)
        if nextvals[mind] == finf:
            return None
        r = lists[mind]
        rhead = r
        if lists[mind].next == None:
            nextvals[mind] = float('inf')
        else:
            lists[mind] = lists[mind].next
            nextvals[mind] = lists[mind].val
        
        mind = min(xrange(len(nextvals)), key=nextvals.__getitem__)
        while nextvals[mind] < float('inf'):
            #print nextvals            
            r.next = lists[mind]
            r = r.next
            if lists[mind].next == None:
                nextvals[mind] = float('inf')
            else:
                lists[mind] = lists[mind].next
                nextvals[mind] = lists[mind].val
            
            mind = min(xrange(len(nextvals)), key=nextvals.__getitem__)
        r.next = None
        return rhead
sol = Solution()
print sol.mergeKLists([])
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(6)
def printll(ll):
    if ll == None:
        return
    while ll != None:
        print ll.val,
        ll = ll.next
printll(sol.mergeKLists([l1]))
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(5)
l2.next.next.next = ListNode(7)
print "\ncombine two"
printll(sol.mergeKLists([l1, l2]))
 