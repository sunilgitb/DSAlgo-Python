from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Optimized O(N) approach
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root: 
                return True, 0  # (is_balanced, height)
            
            # Check left and right subtrees
            left_balanced, left_height = dfs(root.left)
            right_balanced, right_height = dfs(root.right)
            
            # Current node is balanced if:
            # 1. Both subtrees are balanced
            # 2. Height difference <= 1
            current_balanced = (abs(left_height - right_height) <= 1 and 
                              left_balanced and right_balanced)
            
            # Current height = 1 + max of subtree heights
            current_height = 1 + max(left_height, right_height)
            
            return current_balanced, current_height
        
        balanced, _ = dfs(root)
        return balanced

# Example
print("Check if Binary Tree is Balanced:")
print("\nTree structure:")
print("""
        3
       / \\
      9   20
         /  \\
        15   7
""")

# Build a balanced tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
result = solution.isBalanced(root)

print(f"\nIs the tree balanced? {result}")

print("\nHeight calculations:")
print("Node 9: height = 1")
print("Node 15: height = 1")
print("Node 7: height = 1")
print("Node 20: height = 2 (1 + max(1, 1))")
print("Node 3: height = 3 (1 + max(1, 2))")
print("\nHeight differences:")
print("At node 20: |1 - 1| = 0 ≤ 1 ✓")
print("At node 3: |1 - 2| = 1 ≤ 1 ✓")
print("All nodes satisfy balanced condition ✓")