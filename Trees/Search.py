from Tree import Node

def searchDFS(root, key):
    if root is None: return False

    if root.value == key: return True

    leftRes = searchDFS(root.left, key)
    rightRes = searchDFS(root.right, key)
    
    return leftRes or rightRes

if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)

    print(searchDFS(root, 0))