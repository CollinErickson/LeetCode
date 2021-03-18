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
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        #print('start flatten', root)
        if root is None or (root.left is None and root.right is None):
            return
        if root.left is None:
            self.flatten(root.right)
            return
        if root.right is None:
            root.right = root.left
            root.left  = None
            self.flatten(root.right)
            return
        newright = root.left
        oldright = root.right
        self.flatten(oldright)
        self.flatten(newright)
        root.left = None
        root.right = None
        newrighttail = newright
        while newrighttail.right is not None:
            newrighttail = newrighttail.right
        #print('new/old', newright, newrighttail, oldright)
        newrighttail.right = oldright
        root.right = newright
        return

sol = Solution()


n1 = TreeNode(1)
n2 = TreeNode(2)
n1.left = n2
print("Before:", n1)
sol.flatten(n1)
print("After: ", n1)


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3
print("Before:", n1)
sol.flatten(n1)
print("After: ", n1)

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)
n10 = TreeNode(10)
n11 = TreeNode(11)


n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n6
n3.right = n7
n4.left = n8
n4.right = n9
n7.right = n10
n7.left = n11

print("Before:", n1)
sol.flatten(n1)
print("After: ", n1)
