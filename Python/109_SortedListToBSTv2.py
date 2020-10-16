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
    curnode = None
    def sortedListToBST(self, head, bst=None, leftdepth=0):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
          return None
        if head.next is None:
          return TreeNode(head.val)
        self.curnode = head
        n = 1
        node = head
        while node.next is not None:
          n += 1
          node = node.next
        #print('n is', n)
        return self.helper(n)
    def helper(self, n):
      #print('in helper', n)
      if n <= 0:
        return None
      if n==1:
        bst = TreeNode(self.curnode.val)
        self.curnode = self.curnode.next
        return bst
      nL = n-1 - (n-1) // 2
      nR = n - nL - 1
      assert nR>=0
      bstL = self.helper(nL)
      bst = TreeNode(self.curnode.val)
      self.curnode = self.curnode.next
      bstR = self.helper(nR)
      bst.left = bstL
      bst.right = bstR
      return bst


sol = Solution()


n1 = ListNode(1)
#print(n1)
#print('sol is', sol.sortedListToBST(n1), "1")

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

