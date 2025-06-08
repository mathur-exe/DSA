# ============================
# Leetcode: https://leetcode.com/problems/invert-binary-tree/
# ============================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return root

        def PreOrder_DFS(node):
            if node is None: return
            PreOrder_DFS(node.left)
            PreOrder_DFS(node.right)
            node.left, node.right = node.right, node.left

            return node

        return PreOrder_DFS(root)
            

        