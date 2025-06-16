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

    if root.value < key: root.right = delete(root.right, key)
    elif root.value > key: root.left = delete(root.left, key)
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

# %%
def find_floor(root: None, x : int):
    # Non-recursive fn to find floor for a key
    floor = -1
    while root is not None:
        if root.value == x: return root.value

        # pay attention to this for loop 
        # as choice of subtree depends on ceil/ floor
        if x < root.value: root = root.left
        else: 
            floor = root.value
            root = root.right
    return floor

# %%
def find_ceil(root: Node, key):
    ceil = -1
    while root is not None:
        if root.value == key: return root.value

        # pay attention to this for loop 
        # as choice of subtree depends on ceil/ floor
        if key > root.value: root = root.right
        else: 
            ceil = root.value
            root = root.left
    return ceil

# %%
def Successor(root : Node, tgt):
    '''
    Inorder Successor (ceil) -> min of right-subtree

    Steps
    - Start at root, initialize 'best' as None.
    - If current node's key == x, return key.
    - If node's key < x, record key as candidate and move right.
    - If node's key > x, move left.
    - Continue until reaching a leaf.
    - Return last recorded candidate (or None if not found).
    '''

    def find_min(node: Node):
        while node and node.left:
            node = node.left
        return node

    succ = None
    curr = root

    # ======= Logic for while loop ============
    # searching: min of right subtree
    # if tgt < curr.value --> tgt must be searched in left tree
    #                         as higher chances of finding closer val
    # elif: <common sense>
    # else: <code ... curr.right> --> find min in right subtree
    # =========================================
    while curr:
        if tgt < curr.value: 
            succ = curr
            curr = curr.left
        elif tgt > curr.value:
            curr = curr.right
        else:       # tgt is found
            if curr.right: return find_min(curr.right)
            break
    return succ

# %%
def predecessor(root : Node, tgt):
    '''
    Inorder Predecessor (floor) -> max of left-subtree

    Steps:
    - If node has left child → return max in left subtree.
    - Else, track candidate as you walk down:
        * If target > curr.key → candidate = curr; go right.
        * If target < curr.key → go left.
    '''

    def find_max(node: Node):
        while node and node.right: 
            node = node.right
        return node
    
    pred = None
    curr = root

    # ======= Logic for while loop ============
    # searching: max of left subtree
    # if tgt > curr.value --> tgt must be searched in right tree
    #                         as higher chances of finding closer val
    # elif: <common sense>
    # else: <code ... curr.left> --> find max in left subtree
    # =========================================
    while curr:
        if tgt > curr.value:
            pred = curr
            curr = curr.right
        elif tgt < curr.value:
            curr = curr.left
        else:       # tgt found
            if curr.left: return find_max(curr.left)
            break
    return pred