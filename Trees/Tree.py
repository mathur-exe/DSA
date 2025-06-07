class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    # DFS implementations
    def dfs_preorder(self):
        result = []
        self._dfs_preorder_recursive(self.root, result)
        return result
    
    def _dfs_preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._dfs_preorder_recursive(node.left, result)
            self._dfs_preorder_recursive(node.right, result)
    
    def dfs_inorder(self):
        result = []
        self._dfs_inorder_recursive(self.root, result)
        return result
    
    def _dfs_inorder_recursive(self, node, result):
        if node:
            self._dfs_inorder_recursive(node.left, result)
            result.append(node.value)
            self._dfs_inorder_recursive(node.right, result)
    
    def dfs_postorder(self):
        result = []
        self._dfs_postorder_recursive(self.root, result)
        return result
    
    def _dfs_postorder_recursive(self, node, result):
        if node:
            self._dfs_postorder_recursive(node.left, result)
            self._dfs_postorder_recursive(node.right, result)
            result.append(node.value)
    
    # BFS implementation
    def bfs(self):
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return result

# Example usage
if __name__ == "__main__":
    tree = BinaryTree()
    values = [5, 3, 7, 1, 4, 6, 8]
    
    for value in values:
        tree.insert(value)
    
    print("DFS Preorder:", tree.dfs_preorder())
    print("DFS Inorder:", tree.dfs_inorder())
    print("DFS Postorder:", tree.dfs_postorder())
    print("BFS:", tree.bfs())