
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    def __repr__(self):
      s = "Node(" + str(self.val) + ")"
      return s

class Solution:
    def copyRandomList(self, head):
        if head is None: return None
        newhead = Node(0)
        allnodes = {}
        allnodes2 = {}
        tmp = head
        while tmp:
          #print('tmp', tmp, tmp.val)
          allnodes[tmp.val] = (tmp.val, tmp.random.val if tmp.random else None)
          allnodes2[tmp.val] = Node(tmp.val)
          
          tmp = tmp.next
        #print(allnodes)
        #print(allnodes2)
        for key in allnodes2.keys():
          #print('key', key)
          rand = allnodes[key][1]
          if rand:
            allnodes2[key].random = allnodes2[rand]
        newhead = allnodes2[head.val]
        return newhead

sol = Solution()
n1 = Node(1)
n2 = Node(2)
n1.next = n2
n2.random = n1
print(sol.copyRandomList(n1))
