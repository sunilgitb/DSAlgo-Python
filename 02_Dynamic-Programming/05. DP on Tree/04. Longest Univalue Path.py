# https://leetcode.com/problems/longest-univalue-path/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def solve(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Get max univalue path lengths from left and right subtrees
            left_len = solve(node.left)
            right_len = solve(node.right)
            
            # Extend lengths only if values match
            if node.left and node.val == node.left.val:
                left_len += 1
            else:
                left_len = 0
                
            if node.right and node.val == node.right.val:
                right_len += 1
            else:
                right_len = 0
            
            # Update global max: longest path through current node
            self.res = max(self.res, left_len + right_len)
            
            # Return the max length from current node downward
            return max(left_len, right_len)
        
        solve(root)
        return self.res


# ---------------- Example Usage ----------------
# Helper function to build tree from list (level-order)
def build_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


sol = Solution()

# Example 1
# Tree:     5
#         /   \
#        4     5
#      /  \     \
#     1    1     5
root1 = build_tree([5, 4, 5, 1, 1, None, 5])
print(sol.longestUnivaluePath(root1))  # Output: 2

# Example 2
# Tree:     1
#         /   \
#        4     5
#      /  \     \
#     4    4     5
root2 = build_tree([1, 4, 5, 4, 4, None, 5])
print(sol.longestUnivaluePath(root2))  # Output: 2

# Example 3
root3 = build_tree([1])
print(sol.longestUnivaluePath(root3))  # Output: 0

# Example 4 (long chain of same value)
root4 = build_tree([1, 1, 1, 1, 1, 1, 1])
print(sol.longestUnivaluePath(root4))  # Output: 6

# Example 5 (all different values)
root5 = build_tree([1, 2, 3, 4, 5])
print(sol.longestUnivaluePath(root5))  # Output: 0

# Example 6 (skewed tree with same values)
root6 = build_tree([1, 1, None, 1, None, 1])
print(sol.longestUnivaluePath(root6))  # Output: 4