# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        have_null = False
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if not node:
                have_null = True
                continue
            
            if have_null:
                return False
            
            queue.append(node.left)
            queue.append(node.right)
        
        return True

# Test with one example
print("Example: [1,2,3,4,5,6]")
print("Tree structure:")
print("""
    1
   / \\
  2   3
 / \\  /
4   5 6
""")

# Build the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

solution = Solution()
result = solution.isCompleteTree(root)
print(f"Is complete binary tree? {result}")