from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderQueueVerbose(root):
    if not root:
        return []
    res = []
    q = deque([root])
    print(f"Initial queue: {[node.val for node in q]}")

    while q:
        level_size = len(q)
        level_vals = []
        print(f"\nProcessing level with {level_size} node(s)")
        for _ in range(level_size):
            node = q.popleft()
            print(f"Popped {node.val} from queue")
            level_vals.append(node.val)
            if node.left:
                q.append(node.left)
                print(f"Appended left child {node.left.val} to queue")
            if node.right:
                q.append(node.right)
                print(f"Appended right child {node.right.val} to queue")
            print(f"Current queue: {[n.val for n in q]}")
        res.append(level_vals)
        print(f"Completed level: {level_vals}")
        print(f"Result so far: {res}")
    return res

# Sample tree:
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4))
root.right = TreeNode(3, TreeNode(5), TreeNode(6))

level_order_verbose_result = levelOrderQueueVerbose(root)
level_order_verbose_result
