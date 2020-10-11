# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
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
    def sortedListToBST(self, head, bst=None):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
          return bst
        if
        bst = []
        return bst

sol = Solution()

n1 = ListNode(1)
print(sol.sortedListToBST(n1))
