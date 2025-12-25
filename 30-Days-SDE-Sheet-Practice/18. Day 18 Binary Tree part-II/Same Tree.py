# https://leetcode.com/problems/same-tree/

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base cases for recursion to check if both nodes are None 
        if not p and not q: 
            return True
        # If one of the nodes is None, trees are not the same
        if not p or not q: 
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Example usage:
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
solution = Solution()
print(solution.isSameTree(p, q))  # Output: True
