# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 16:41:44 2018

@author: cbe117
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head
        prevnode = None
        curnode = head
        curnode0=None
        while True:
            #print "curnode val is ", curnode.val
            nodelist = [None for i in range(k)]
            for i in range(k):
                #print "1", i
                if curnode is not None:
                    #print 'lsa', i, k, nodelist
                    nodelist[i] = curnode
                    curnode = curnode.next
                else:
                    #print 'done'
                    #print curnode.val
                    # Don't need to change last group
                    return head
            #print 'curnode is', curnode
            nextnode = curnode
            for i in range(k):
                #print "2", i
                if curnode0 is None:
                    curnode0 = nodelist[k-1-i]
                    head = curnode0
                    #print "set head val to ", head.val
                else:
                    #print "setting next val to ", curnode0.next.val
                    curnode0.next = nodelist[k-1-i]
                    curnode0 = curnode0.next
            curnode0.next = nextnode
sol = Solution()
n = 8
lns = [ListNode(i) for i in range(n)]
for i in range(n-1):
    lns[i].next = lns[i+1]
s1 =sol.reverseKGroup(lns[0], 3)
print 'expect' ,1,0,3,2,4
while s1 is not None:
    print s1.val
    s1 = s1.next