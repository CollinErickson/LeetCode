# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
     def __repr__(self):
       s = "(" + str(self.val)
       n = self.next
       if n is None:
         return s + ")"
       #print('s', s, n.val)
       while n is not None:
         s += " -> " + str(n.val)
         n = n.next
       return s + ")"
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
     def __repr__(self):
       s = str(self.val)
       if self.left is not None:
         s += "(" + str(self.left) + ")"
       if self.right is not None:
         s += "[" + str(self.right) + "]"
       return s
       
class Solution(object):
    def sortedListToBST(self, head, bst=None, leftdepth=0):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        #print("starting sltbst", head, bst, leftdepth)
        if head is None:
          return bst
        newbst = TreeNode(head.val)
        head = head.next
        #print('newbst is', newbst)
        if head is None:
          #print('return early', newbst)
          newbst.left = bst
          return newbst
        if bst is None:
          #print('bst is None', head, newbst)
          outbst = self.sortedListToBST(head = head, bst=newbst, leftdepth=1)
          return outbst
        newbst.left = bst
        listright = head
        nodestoputonright = leftdepth * (leftdepth + 1) // 2
        leftdepth += 1
        newhead = head
        lastofnodestoputonright = None
        #print('startling loop', newbst, nodestoputonright, listright)
        for i in range(nodestoputonright):
          #print('i', i)
          lastofnodestoputonright = newhead
          newhead = newhead.next
          if newhead is None:
            break
        else:
          lastofnodestoputonright.next = None
        #print('exited for', newbst, nodestoputonright, listright)
        newbst.right = self.sortedListToBST(head=listright, bst=None, leftdepth=0)
        fullbst =  self.sortedListToBST(head = newhead, bst=newbst, leftdepth=leftdepth)
        #bst = []
        #print('fullbst is', fullbst)
        return fullbst

sol = Solution()


n1 = ListNode(1)
#print(n1)
#print('sol is', sol.sortedListToBST(n1))

n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
#print(n1)
#print('sol is', sol.sortedListToBST(n1))


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3
#print(n1)
#print('sol is', sol.sortedListToBST(n1))


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
#print(n1)
#print('sol is', sol.sortedListToBST(n1))

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n8 = ListNode(8)
n9 = ListNode(9)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
print(n1)
print('sol is', sol.sortedListToBST(n1))

