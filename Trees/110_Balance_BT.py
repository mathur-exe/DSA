# ============================
# Leetcode: https://leetcode.com/problems/invert-binary-tree/
# ============================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        def check(root):
            if root is None: return 0
            left = check(root.left)
            if left == -1: return -1    # BT is not balanced
            right =  check(root.right)
            if right == -1: return -1   # BT is not balanced

            if abs(left - right) > 1: return -1

            return max(left, right) + 1
        
        return check(root) != -1