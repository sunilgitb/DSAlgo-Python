from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Queue stores (node, index)
        # For root, index = 0 (or 1, but 0 works with the formula)
        queue = deque([(root, 0)])
        max_width = 0
        
        while queue:
            # Calculate width of current level
            # leftmost index = queue[0][1], rightmost = queue[-1][1]
            leftmost_index = queue[0][1]
            rightmost_index = queue[-1][1]
            current_width = rightmost_index - leftmost_index + 1
            max_width = max(max_width, current_width)
            
            # Process all nodes at current level
            level_size = len(queue)
            for _ in range(level_size):
                node, index = queue.popleft()
                
                # Assign indices to children
                # If we use 0-based indexing with root = 0:
                # left child = 2*i + 1, right child = 2*i + 2
                if node.left:
                    queue.append((node.left, 2 * index + 1))
                if node.right:
                    queue.append((node.right, 2 * index + 2))
        
        return max_width

# Example
print("Maximum Width of Binary Tree:")
print("\nTree structure:")
print("""
        1
       / \\
      3   2
     /     \\
    5       9
   /         \\
  6           7
""")

# Build the tree
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.right.right = TreeNode(9)
root.left.left.left = TreeNode(6)
root.right.right.right = TreeNode(7)

solution = Solution()
result = solution.widthOfBinaryTree(root)

print(f"\nMaximum width: {result}")

print("\nIndex assignment (0-based):")
print("Level 0: Node 1 → index 0")
print("Level 1: Node 3 → index 1 (2*0+1), Node 2 → index 2 (2*0+2)")
print("Level 2: Node 5 → index 3 (2*1+1), Node 9 → index 6 (2*2+2)")
print("Level 3: Node 6 → index 7 (2*3+1), Node 7 → index 14 (2*6+2)")

print("\nWidth calculation per level:")
print("Level 0: Only node 1 → width = 1")
print("Level 1: Nodes at indices 1 and 2 → width = 2-1+1 = 2")
print("Level 2: Nodes at indices 3 and 6 → width = 6-3+1 = 4")
print("Level 3: Nodes at indices 7 and 14 → width = 14-7+1 = 8")
print(f"Maximum width across all levels: {result}")

print("\nVisualization with indices:")
print("""
       0: 1
      /     \\
    1:3      2:2
    /          \\
  3:5          6:9
  /              \\
 7:6            14:7
""")