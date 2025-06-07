class Node: 
    def __init__(self, v):
        self.left = None
        self.right = None
        self.val = v

def PreOrder(root):
    # Root-Left-Right
    
    if root is None: return

    print(f"{root.val=}")
    print(f"{PreOrder(root.left)=}")
    print(f"{PreOrder(root.right)=}")

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    PreOrder(root)