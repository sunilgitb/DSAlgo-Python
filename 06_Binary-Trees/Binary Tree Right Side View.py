from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            # The last element in the queue at each level is the rightmost node
            result.append(queue[-1].val)
            
            # Process all nodes at current level
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                
                # Add children for next level (left first, then right)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

# Example
print("Binary Tree Right Side View:")
print("\nTree structure:")
print("""
        1
       / \\
      2   3
       \\   \\
        5   4
""")

# Build the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

solution = Solution()
result = solution.rightSideView(root)

print(f"\nRight side view: {result}")

print("\nExplanation:")
print("Level 0 (depth 0): Rightmost node is 1")
print("Level 1 (depth 1): Rightmost node is 3")
print("Level 2 (depth 2): Rightmost node is 4")
print("Level 3 (depth 3): No nodes")
print("\nResult: [1, 3, 4]")

print("\nAlternative visualization:")
print("Stand to the right of the tree and look:")
print("""
    You see:    1
                 \
                  3
                   \
                    4
""")