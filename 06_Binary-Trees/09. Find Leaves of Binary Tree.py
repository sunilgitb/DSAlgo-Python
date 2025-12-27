from typing import List, Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        height_dict = defaultdict(list)
        
        def tree_height(root):
            if not root: 
                return 0
            
            left_height = tree_height(root.left)
            right_height = tree_height(root.right)
            
            # Height of current node = 1 + max(height of subtrees)
            current_height = 1 + max(left_height, right_height)
            
            # Add node value to its corresponding height group
            height_dict[current_height].append(root.val)
            
            return current_height
        
        tree_height(root)
        
        # Return groups sorted by height (1 to max_height)
        result = []
        for height in sorted(height_dict.keys()):
            result.append(height_dict[height])
        
        return result

# Example
print("Find Leaves of Binary Tree:")
print("Tree structure:")
print("""
        1
       / \\
      2   3
     / \\
    4   5
""")

# Build the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = Solution()
result = solution.findLeaves(root)

print(f"\nLeaves grouped by height: {result}")
print("\nExplanation:")
print("Height 1 leaves: [4, 5, 3] (these are actual leaves)")
print("Height 2 leaves: [2] (becomes leaf after removing height 1 nodes)")
print("Height 3 leaves: [1] (becomes leaf after removing height 2 nodes)")
print("\nProcess:")
print("1. Remove leaves [4,5,3] → Tree becomes [1,2]")
print("2. Remove leaves [2] → Tree becomes [1]")
print("3. Remove leaves [1] → Tree becomes empty")