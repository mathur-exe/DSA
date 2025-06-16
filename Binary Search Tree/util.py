#  %%
# This files contains the barebone functions required to work with BST
from Node import Node

def insert(root: Node, key):
    if root is None: return Node(key)
    if root.value == key: return root
    if root.value < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root
# %%
def inorder(root):
    # left - root - right
    if root is None: return
    inorder(root.left)
    print(f"{root.value} ->")
    inorder(root.right)

# %%
def search(root : Node, key):
    '''
    1. nodes in BST are in sorted order
    2. use Binary Search to find nodes in tree
    
    > print("Found" if search(r, 70) else "Nope") 
    '''
    if root is None or root.value == key: return root    
    if root.value < key: 
        return search(root.right, key)
    else:
        return search(root.left, key)
# %%
def delete(root : Node, key):
    '''
    There are 3 types of deletion
    1. Leaf Node in BST
    2. Node with single child in BST
    3. Node with 2 children in BST

    Example of 2 child subtree -> del(15)
        10
       /  \
      5    15
          /  \
        12    18
             /  \
           16   19
    '''
    if root is None or key is None: return None

    def find_min(node : Node):
        # finds node with smallest node in subtree
        while node.left:
            node = node.left
        return node

    if root.value < key: delete(root.right, key)
    elif root.value > key: delete(root.left, key)
    else:       # match condition
        # case 1: no left child
        if root.left is None: return root.right
        # case 2: no right child
        if root.right is None: return root.left

        # case 3: 2 child, replace with inorder
        successor = find_min(root.right)
        root.value = successor.value
        root.right = delete(root.right, successor.value)
    
    return root