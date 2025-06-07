class Node: 
    def __init__(self, v):
        self.left = None
        self.right = None
        self.val = v

def InOrder(root):
    # Left-Root-Right
    
    if root is None: return

    InOrder(root.left)              # Left
    print(f"{root.val=}")           # Root
    InOrder(root.right)             # Right

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    InOrder(root)