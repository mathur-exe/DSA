from Tree import Node

def InOrder(root):
    # Left-Root-Right
    
    if root is None: return

    InOrder(root.left)              # Left
    print(f"{root.value=}")           # Root
    InOrder(root.right)             # Right

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    InOrder(root)