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
    def insertionSortList(self, head: ListNode) -> ListNode:
      if head is None or head.next is None:
        return head
      # At least two elements
      maxseen = head.val
      node = head.next
      prev = head
      while node:
        #print('in while loop', node, 'head', head, 'prev', prev)
        if node.val >= maxseen:
          maxseen = max(maxseen, node.val)
          prev = node
          node = node.next

        else:
          #print('doing the else', node, head, prev)
          nextnode = node.next
          # Separate the node out
          prev.next = node.next
          node.next = None
          # Put it in the right place
          if node.val <= head.val:
            #print('putting in front', node, head)
            node.next = head
            head = node
            
          else:
            a = head
            b = head.next
            while True:
              if node.val <= b.val:
                a.next = node
                node.next = b
                break
              else:
                a = b
                b = b.next
          # Get ready for next one
          #prev = prev
          node = nextnode
      return head

sol = Solution()
print(sol.insertionSortList(None))

n1 = ListNode(1)
print(sol.insertionSortList(n1), "--   1")

n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
print(sol.insertionSortList(n1), "//    1 -> 2")


n1 = ListNode(2)
n2 = ListNode(1)
n1.next = n2
print('starting', n1)
print(sol.insertionSortList(n1), "//    1 -> 2")


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3
print('starting', n1)
print(sol.insertionSortList(n1), "//    1 -> 2 -> 3")


n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(1)
n1.next = n2
n2.next = n3
print('starting', n1)
print(sol.insertionSortList(n1), "//    1 -> 2 -> 3")


n1 = ListNode(3)
n2 = ListNode(52)
n3 = ListNode(12)
n4 = ListNode(31)
n5 = ListNode(61)
n6 = ListNode(2)
n7 = ListNode(46)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
print('starting', n1)
print(sol.insertionSortList(n1), "//    1 -> 2 -> 3")
