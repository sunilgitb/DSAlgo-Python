from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True  # Direction flag
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Append level based on current direction
            if left_to_right:
                result.append(current_level)  # Left to right
            else:
                result.append(current_level[::-1])  # Right to left (reversed)
            
            # Toggle direction for next level
            left_to_right = not left_to_right
        
        return result

# Example
print("Binary Tree Zigzag Level Order Traversal:")
print("\nTree structure:")
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
result = solution.zigzagLevelOrder(root)

print(f"\nZigzag level order: {result}")

print("\nExplanation:")
print("Level 0 (depth 0): Left to right → [3]")
print("Level 1 (depth 1): Right to left → [20, 9] (reversed from [9, 20])")
print("Level 2 (depth 2): Left to right → [15, 7]")
print("\nTraversal order:")
print("1. Root level (0): 3 (left to right)")
print("2. Next level (1): 20 → 9 (right to left)") 
print("3. Next level (2): 15 → 7 (left to right)")
print("\nVisual zigzag path:")
print("""
    3 →       (LTR)
         ← 20 (RTL)
       ← 9    (RTL)
    15 →      (LTR)
        7 →   (LTR)
""")