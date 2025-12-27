from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result

# Example
print("Binary Tree Level Order Traversal:")
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
result = solution.levelOrder(root)

print(f"\nLevel order traversal: {result}")

print("\nExplanation:")
print("Level 0: [3]              (root level)")
print("Level 1: [9, 20]          (children of root)")
print("Level 2: [15, 7]          (children of level 1 nodes)")
print("\nTraversal process:")
print("1. Start with root 3 → level 0: [3]")
print("2. Process level 0, add children 9 and 20 → level 1: [9, 20]")
print("3. Process level 1:")
print("   - Node 9 has no children")
print("   - Node 20 has children 15 and 7 → level 2: [15, 7]")
print("4. Result: [[3], [9, 20], [15, 7]]")