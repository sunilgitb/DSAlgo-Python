# https://leetcode.com/problems/diameter-of-binary-tree/
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
            if not root: return 0
            
            l = solve(root.left)
            r = solve(root.right)
            
            tmp = 1 + max(l, r)
            self.res = max(self.res, 1 + l + r)
            
            return tmp
        
        solve(root)
        return self.res - 1


# Example usage
# Definition for a binary tree node used in examples

if __name__ == "__main__":
    sol = Solution()

    # Example tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print("Diameter (edges):", sol.diameterOfBinaryTree(root))  # Expected: 3

    # Single node
    single = TreeNode(1)
    print("Single node diameter:", sol.diameterOfBinaryTree(single))  # Expected: 0