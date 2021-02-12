# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    def __repr__(self):
        s = "N(" + str(self.val) + ": " + ",".join([str(n.val) for n in self.neighbors]) + ")"
        return s

from queue import Queue
class Solution:
    def cloneGraph(self, node):
        if node is None: return None
        #print('graph is', node, node)
        dict_old = {}
        dict_new = {}
        q = Queue()
        q.put(node)
        while q.qsize() > 0:
          n = q.get()
          #print('popped n:', n)
          if n.val in dict_old:
            pass
          else:
            dict_old[n.val] = n
            for nn in  n.neighbors:
              q.put(nn)
            dict_new[n.val] = Node(val=n.val)
        for key in dict_old:
            nold = dict_old[key]
            nnew = dict_new[key]
            for neighb in nold.neighbors:
                nnew.neighbors.append(dict_new[neighb.val])
        #print(dict_old)
        #print(dict_new)
        return dict_new[node.val]

sol = Solution()
n1 = Node(1)
print(sol.cloneGraph(n1))
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.neighbors = [n2, n4]
print(sol.cloneGraph(n1))
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]
print(sol.cloneGraph(n1))

