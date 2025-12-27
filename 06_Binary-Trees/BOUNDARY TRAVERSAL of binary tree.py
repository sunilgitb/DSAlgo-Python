from typing import Optional, List

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def printBoundaryView(self, root: Optional[Node]) -> List[int]:
        
        def addLeftBoundary(root, res):
            """Add left boundary (excluding leaf nodes)."""
            if not root:
                return
            
            cur = root
            while cur:
                # Add if not leaf
                if cur.left or cur.right:
                    res.append(cur.data)
                
                # Move to left child, or right if left doesn't exist
                if cur.left:
                    cur = cur.left
                else:
                    cur = cur.right
        
        def addLeafNodes(root, res):
            """Add all leaf nodes (inorder traversal)."""
            if not root:
                return
            
            # If leaf node, add to result
            if not root.left and not root.right:
                res.append(root.data)
                return
            
            # Traverse left then right (inorder)
            addLeafNodes(root.left, res)
            addLeafNodes(root.right, res)
        
        def addRightBoundary(root, res):
            """Add right boundary in reverse order (excluding leaf nodes)."""
            if not root:
                return
            
            cur = root
            boundary = []
            while cur:
                # Add if not leaf
                if cur.left or cur.right:
                    boundary.append(cur.data)
                
                # Move to right child, or left if right doesn't exist
                if cur.right:
                    cur = cur.right
                else:
                    cur = cur.left
            
            # Add in reverse order (bottom to top)
            res.extend(boundary[::-1][1:])  # [1:] to exclude the root which is already added
        
        if not root:
            return []
        
        result = []
        
        # 1. Add root if it's not a leaf
        if root.left or root.right:
            result.append(root.data)
        
        # 2. Add left boundary (excluding leaves and root)
        addLeftBoundary(root.left, result)
        
        # 3. Add all leaf nodes
        addLeafNodes(root, result)
        
        # 4. Add right boundary in reverse (excluding leaves and root)
        addRightBoundary(root.right, result)
        
        return result

# Example
print("Boundary Traversal of Binary Tree:")
print("\nTree structure:")
print("""
        20
       /  \\
      8    22
     / \\     \\
    4   12    25
       /  \\
      10   14
""")

# Build the tree
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

solution = Solution()
result = solution.printBoundaryView(root)

print(f"\nBoundary traversal: {result}")

print("\nExplanation in order:")
print("1. Left boundary (top to bottom): 20 → 8 → 4")
print("2. Leaf nodes (left to right): 4, 10, 14, 25")
print("3. Right boundary (bottom to top): 25 → 22")
print("\nNote: Avoid duplicates:")
print("- Node 4 appears in both left boundary and leaves, but only once in result")
print("- Node 25 appears in both leaves and right boundary, but only once")
print("\nFinal sequence: 20, 8, 4, 10, 14, 25, 22")