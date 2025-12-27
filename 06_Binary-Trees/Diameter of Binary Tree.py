from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def solve(root):
            if not root:
                return 0
            
            # Get heights of left and right subtrees
            left_height = solve(root.left)
            right_height = solve(root.right)
            
            # Height of current subtree = 1 + max(left, right)
            current_height = 1 + max(left_height, right_height)
            
            # Update global maximum diameter
            # Diameter through current node = left_height + right_height + 1 (for current node)
            # But we store total nodes in path for now, will subtract 1 later
            self.res = max(self.res, left_height + right_height + 1)
            
            return current_height
        
        solve(root)
        # Diameter is number of edges = number of nodes in path - 1
        return max(0, self.res - 1)

# Example
print("Diameter of Binary Tree:")
print("\nTree structure:")
print("""
        1
       / \\
      2   3
     / \\     
    4   5
   /
  6
""")

# Build the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)

solution = Solution()
result = solution.diameterOfBinaryTree(root)

print(f"\nDiameter (longest path length): {result}")

print("\nLongest path: [6 → 4 → 2 → 5] or [6 → 4 → 2 → 1 → 3]")
print("Path [6 → 4 → 2 → 5] has 4 nodes: 6, 4, 2, 5")
print("Number of edges = number of nodes - 1 = 3")

print("\nCalculation process (post-order traversal):")
print("Node 6: height = 1, diameter through node = 0 + 0 + 1 = 1")
print("Node 4: height = 2 (1 + max(1, 0)), diameter = 1 + 0 + 1 = 2")
print("Node 5: height = 1, diameter = 0 + 0 + 1 = 1")
print("Node 2: height = 3 (1 + max(2, 1)), diameter = 2 + 1 + 1 = 4 ← max so far")
print("Node 3: height = 1, diameter = 0 + 0 + 1 = 1")
print("Node 1: height = 4 (1 + max(3, 1)), diameter = 3 + 1 + 1 = 5")
print(f"\nMaximum nodes in path = {max(4, 5)} = 5")
print(f"Diameter (edges) = {max(4, 5)} - 1 = {result}")