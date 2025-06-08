from collections import deque
from Tree import Node
from InOrder import InOrder

def delete_node(root, key):
    '''
    1. Traverse tree in BFS while tracking:
       - The target node to delete (with value = val)
       - The deepest rightmost node (and its parent)
    2. If the target node is found:
       - Replace its value with the deepest node's value
       - Remove the deepest node from the tree using its parent
    3. If the target node isn't found, return the original tree.
    '''

    if root is None: return None

    q = deque([(root, None)])     # [root, None] -> keeps track of root node, and it's parent, 
                                # in absecence, i'll need to to do BFS again
    target = None
    last_node = None            # store: deepest right most (DRM) node 
    last_parent = None          # store: parent of DRM node

    # BFS for the node
    while q:
        curr, parent = q.popleft()
        # check if the node exist in the tree
        if curr.value == key: target = curr

        # updating last node and parent
        last_node, last_parent = curr, parent

        # Enqueqe children with parent info
        if curr.left: q.append((curr.left, curr))
        if curr.right: q.append((curr.right, curr))

    if target is None: return root

    # Overwrite target’s value and remove DRM
    target.value = last_node.value

    # If the tree had only one node, deletion makes it empty
    if last_parent is None: return None

    # Unlink last_node from its parent
    if last_parent.left is last_parent: last_parent.left = None
    else:last_parent.right = None

    return root

if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)

    print(f"Before Deletion of 6")
    InOrder(root)
    delete_node(root, key = 6)
    print("Post Deletion")
    InOrder(root)