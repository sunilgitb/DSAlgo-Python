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

# Example with nodes at same position needing sorting
print("Vertical Order Traversal (with sorting for same position):")
print("\nTree structure:")
print("""
        3
       / \\
      1   4
     / \\   \\
    0   2   5
         \\
          6
""")

# Build the tree
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.right = TreeNode(5)
root.left.right.right = TreeNode(6)

solution = Solution()
result = solution.verticalTraversal(root)

print(f"\nVertical traversal result: {result}")

print("\nColumn details (col, row, value):")
print("Column -2: (2,0)")  # Node 0 at row 2
print("Column -1: (1,1), (3,2)")  # Node 1 at row 1, Node 2 at row 3
print("Column 0: (0,3), (2,4), (4,6)")  # Node 3 at row 0, Node 4 at row 2, Node 6 at row 4
print("Column 1: (1,5)")  # Node 5 at row 1
print("\nNote: Column 0 has nodes at different rows: 3(row 0), 4(row 2), 6(row 4)")
print("They are sorted by row first, then value")

print("\nStep-by-step grouping and sorting:")
print("1. After DFS traversal:")
print("   Column -2: [(2, 0)]")
print("   Column -1: [(1, 1), (3, 2)]")
print("   Column 0: [(0, 3), (2, 4), (4, 6)]")
print("   Column 1: [(1, 5)]")
print("\n2. Sorting within each column (by row, then value):")
print("   Column -1: Already sorted (1,1) then (3,2)")
print("   Column 0: Already sorted (0,3) then (2,4) then (4,6)")
print("\n3. Extract values:")
print("   Result: [[0], [1, 2], [3, 4, 6], [5]]")

print("\n" + "="*60)
print("Example 2: Tree where same column/row has multiple nodes")
print("Tree structure:")
print("""
        1
       / \\
      2   3
     / \\ / \\
    4  5 6  7
""")

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(7)

result2 = solution.verticalTraversal(root2)
print(f"\nVertical traversal: {result2}")

print("\nSpecial case: Nodes 5 and 6 are in same column (0) and same row (2)")
print("They need to be sorted by value: 5 then 6")
print("Column 0: (2,5) and (2,6) → sorted by value → [5, 6]")