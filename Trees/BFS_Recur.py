class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderDFS(root):
    res = []
    def dfs(node, depth):
        if not node:
            return
        # ensure there’s a list for this depth
        if depth == len(res):
            res.append([])
            print(f"{depth=} --> {res=}")  # after adding new level
        # record this node in its depth‐bucket
        res[depth].append(node.val)
        print(f"{depth=} --> {res=}")      # after adding node value
        # recurse to children, one level deeper
        dfs(node.left,  depth+1)
        dfs(node.right, depth+1)
    dfs(root, 0)
    return res

# Example: Build a sample binary tree:
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4))
root.right = TreeNode(3, TreeNode(5), TreeNode(6))

result = levelOrderDFS(root)
print("Final result:", result)
