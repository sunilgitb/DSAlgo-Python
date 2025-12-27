from typing import List, Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Dictionary to store nodes by their vertical column
        column_map = defaultdict(list)
        
        def dfs(node, col, row):
            if not node:
                return
            
            # Store node with its row and value
            column_map[col].append((row, node.val))
            
            # Traverse left (col-1) and right (col+1) with increased row
            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)
        
        dfs(root, 0, 0)
        
        # Sort columns from leftmost to rightmost
        result = []
        for col in sorted(column_map.keys()):
            # Sort nodes in same column by row, then by value
            nodes = column_map[col]
            nodes.sort()
            # Extract just the values in sorted order
            result.append([val for _, val in nodes])
        
        return result

# Example
print("Vertical Order Traversal of a Binary Tree:")
print("Tree structure:")
print("""
        3
       / \\
      9   20
         /  \\
        15   7
""")

# Build the tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
result = solution.verticalTraversal(root)

print(f"\nVertical traversal result: {result}")
print("\nExplanation:")
print("Column -1: [9] (left of root)")
print("Column 0: [3, 15] (root and its left child's left child)") 
print("Column 1: [20] (root's right child)")
print("Column 2: [7] (rightmost node)")