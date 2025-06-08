
from Tree import Node

# Finding the Height of the Tree
def height(root):
    if root is None: return -1

    left_T = height(root.left)
    right_T = height(root.right)

    return max(left_T, right_T) + 1

# Find Level of a Node in a Binary Tree
def node_level(root, key, level=0):
    if root is None: return 0
    if root.value == key: return level

    downlevel = node_level(root.left, key, level + 1)
    if downlevel != 0: return downlevel

    return node_level(root.right, key, level + 1)

# Finding the Size of the Entire Tree
def size_tree(root):
    if root is None: return 0
    left_T = size_tree(root.left)
    right_T = size_tree(root.right)

    return 1 + left_T + right_T
 
if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)

