from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        self.res = root.val  # Initialize with root value
        
        def solve(root):
            if not root: 
                return 0
            
            # Get max path sum from left and right subtrees
            # If negative, we don't take them (max with 0)
            left_max = max(solve(root.left), 0)
            right_max = max(solve(root.right), 0)
            
            # Case 1: Path going through current node as "root" of the path
            # This path can include both children
            path_through_root = root.val + left_max + right_max
            
            # Case 2: Path that continues upward to parent
            # Can only include one child (max of left or right)
            path_to_parent = root.val + max(left_max, right_max)
            
            # Update global maximum
            self.res = max(self.res, path_through_root)
            
            # Return the maximum path sum that can be extended to parent
            return path_to_parent
        
        solve(root)
        return self.res

# Example
print("Binary Tree Maximum Path Sum:")
print("\nTree structure:")
print("""
        -10
       /   \\
      9     20
           /  \\
          15   7
""")

# Build the tree
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
result = solution.maxPathSum(root)

print(f"\nMaximum path sum: {result}")

print("\nExplanation:")
print("Possible paths and their sums:")
print("1. Path [15, 20, 7]: 15 + 20 + 7 = 42")
print("2. Path [9]: 9")
print("3. Path [-10, 9]: -10 + 9 = -1")
print("4. Path [-10, 20, 15]: -10 + 20 + 15 = 25")
print("5. Path [-10, 20, 7]: -10 + 20 + 7 = 17")
print("\nMaximum is path [15, 20, 7] with sum = 42")