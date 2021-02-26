# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
     def __repr__(self):
         s = str(self.val) #"Node(" + str(self.val) + "," + (str(self.random.val) if self.random else "-") + ")"
         if self.next:
           s +=  " -> " + str(self.next) 
         return s


class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
          return head
        # Find middle of list
        n1 = head
        n2 = head.next
        while n2.next and n2.next.next:
          n1 = n1.next
          n2 = n2.next.next
        
        # Reverse second half
        premiddle = n1
        node = n1.next
        while node.next:
          current = node.next
          node.next = current.next
          current.next = premiddle.next
          premiddle.next = current
          
        # Merge head and middle
        n3 = head
        n4 = premiddle.next
        while n3 != premiddle:
          premiddle.next = n4.next
          n4.next = n3.next
          n3.next = n4
          n3 = n4.next
          n4 = premiddle.next
        return head


sol = Solution()
print(sol.reorderList(None), None)

n1 = ListNode(1)
print(sol.reorderList(n1), "1")

n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
print(sol.reorderList(n1), "1 -> 2")


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3
print(sol.reorderList(n1), " // 1 -> 2 -> 3")


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
print(sol.reorderList(n1), " // 1 -> 4 -> 2 -> 3")

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print(sol.reorderList(n1), " // 1 -> 5 -> 2 -> 4 -> 3")
