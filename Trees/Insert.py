# %%
from collections import deque
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# %%
def insert_bfs(root, key):
    if root is None: return Node(key)
    q = deque([root])

    while q:
        temp = q.popleft()

        if temp.left is None:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)
            
    return root

# %%
def insert_dfs(root, key):
    '''
    There is problem with dfs based insertion
    It will do the very depth of the tree, and insert the nodes 
    even though there might be free spot up 
    '''
    if root is None: return Node(key)

    if root.left is None:
        root.left = Node(key)
    else: 
        insert_dfs(root.left, key)
    return root

# %%
if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

    from InOrder import InOrder

    print("Before Insert")
    InOrder(root)
    insert_bfs(root, key=6)
    print("After Insert")
    InOrder(root)