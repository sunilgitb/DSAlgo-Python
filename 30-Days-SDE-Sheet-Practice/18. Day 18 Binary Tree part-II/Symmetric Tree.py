# https://leetcode.com/problems/symmetric-tree/

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def solve(l, r):
            if not l and not r: 
                return True
            if not l or not r:
                return False
            
            return l.val == r.val and solve(l.left, r.right) and solve(l.right, r.left)
        
        return solve(root.left, root.right)
    
# Time: O(N)
# Space: O(1)

# Example Usage:
sol = Solution()
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(3)
print(sol.isSymmetric(tree))  # Output: True
