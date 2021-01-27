
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    def __repr__(self):
      s = "Node(" + str(self.val) + "," + (str(self.random.val) if self.random else "-") + ")"
      if self.next:
        s +=  " -> " + str(self.next) 
      return s

class Solution:
    def copyRandomList(self, head):
        if head is None: return None
        LL = []
        td = {}
        tmp = head
        i=0
        while tmp:
          LL.append((tmp, Node(tmp.val), i))
          td[tmp] = i
          tmp = tmp.next
          i += 1
        for i in range(len(LL)):
          nextnode = LL[i][0].next
          if nextnode:
            LL[i][1].next = LL[td[nextnode]][1]
          randnode = LL[i][0].random
          if randnode:
            LL[i][1].random = LL[td[randnode]][1]
        return LL[0][1]


sol = Solution()
n1 = Node(1)
n2 = Node(2)
n1.next = n2
n2.random = n1
print(n1)
print("sol 1", sol.copyRandomList(n1))
n1.random=n2
print('sol 2',n1, ":::", sol.copyRandomList(n1))


n0 = Node(7)
n1 = Node(13)
n2 = Node(11)
n3 = Node(10)
n4 = Node(0)
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n0.random = None
n1.random = n0
n2.random = n4
n3.random = n2
n4.random = n0
print('sol 3', n0, ':::', sol.copyRandomList(n0))

