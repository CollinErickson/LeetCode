# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 22:19:49 2017

@author: cbe117
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l3 = None
        m1 = l1
        m2 = l2
        addone = 0
        while True:
            if l3 == None:
                tval = m1.val + m2.val
                if tval >= 10:
                    addone = 1
                    tval -= 10
                l3 = ListNode(tval)
                m3 = l3
            else:
                tval = m1.val + m2.val + addone
                addone = 0
                if tval >= 10:
                    addone = 1
                    tval -= 10
                m3_next = ListNode(tval)
                m3.next = m3_next
                m3 = m3.next
            m1 = m1.next
            m2 = m2.next
            #m3 = m3.next
            if m1 == None and m2 == None:
                if addone > 0:
                    m3.next = ListNode(addone)
                return l3
            if m1 == None:
                m1 = ListNode(0)
            if m2 == None:
                m2 = ListNode(0)
sol = Solution()
#print sol.addTwoNumbers([8,0,2,4,3], [9,5,6,4])
a1 = ListNode(5)
#a1.next = ListNode(8)
#a1.next.next = ListNode(3)
a2 = ListNode(5)
s1 =  sol.addTwoNumbers(a1, a2)
s2 =  sol.addTwoNumbers(a2, a1)
print s1.val
print s1.val, s1.next.val#, s1.next.next.val
#print s2.val, s2.next.val#, s1.next.next.val