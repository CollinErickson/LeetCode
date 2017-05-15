# -*- coding: utf-8 -*-
"""
Created on Sun May 14 19:22:05 2017

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
        if lenl > 2:
            return self.mergeKLists([self.mergeKLists(lists[0:(lenl/2)]), self.mergeKLists(lists[(lenl/2):lenl])])
        l0 = lists[0]
        l1 = lists[1]
        if l0 == None:
            return l1
        if l1 == None:
            return l0
        if l0.val < l1.val:
            r = l0
            rhead = l0
            l0 = l0.next
        else:
            r = l1
            rhead = l1
            l1 = l1.next
        #print "beginning True:"
        while True:
            #print l0, l1
            if l0 == None:
                r.next = l1
                break
            elif l1 == None:
                r.next = l0
                break
            if l0.val < l1.val:
                r.next = l0
                r = r.next
                l0 = l0.next
            else:
                r.next = l1
                r = r.next
                l1 = l1.next
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
l3 = ListNode(3.4)
l3.next = ListNode(4.5)
printll(sol.mergeKLists([l1, l2, l3]))