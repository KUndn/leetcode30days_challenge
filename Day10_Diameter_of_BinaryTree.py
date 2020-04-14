# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0 #edge case 
        
        def fn(node):
            if not node: return (0, 0)
            l1, d1 = fn(node.left)
            l2, d2 = fn(node.right)
            return 1 + max(l1, l2), max(d1, d2, l1+l2)
        
        return fn(root)[1]
