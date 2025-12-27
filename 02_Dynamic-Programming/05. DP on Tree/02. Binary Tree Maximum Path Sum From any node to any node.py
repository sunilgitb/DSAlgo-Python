# https://www.youtube.com/watch?v=Osz-Vwer6rw&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=48
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.res = float('-inf')  # Initialize to negative infinity
        
        def solve(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Get max path sums from left and right subtrees
            left = solve(node.left)
            right = solve(node.right)
            
            # Max path sum starting from current node going down to one child (or just node)
            temp = max(node.val + max(left, right), node.val)
            
            # Max path sum that passes through current node (including both children)
            through_node = node.val + left + right
            
            # Update global max
            self.res = max(self.res, through_node, node.val)  # Also consider single node
            
            return temp  # Return max gain if we include this node in path to parent
        
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
# Tree:     1
#         /   \
#        2     3
root1 = build_tree([1, 2, 3])
print(sol.maxPathSum(root1))  # Output: 6 (2 + 1 + 3)

# Example 2
# Tree:     -10
#          /   \
#         9     20
#              /  \
#             15    7
root2 = build_tree([-10, 9, 20, None, None, 15, 7])
print(sol.maxPathSum(root2))  # Output: 42 (15 + 20 + 7)

# Example 3
# Tree:     1
#          /
#         2
root3 = build_tree([1, 2])
print(sol.maxPathSum(root3))  # Output: 3 (1 + 2)

# Example 4 (negative values)
root4 = build_tree([-3])
print(sol.maxPathSum(root4))  # Output: -3 (single node)

# Example 5
# Tree:     10
#          /  \
#         2    10
#        / \     \
#       20  1     -5
root5 = build_tree([10, 2, 10, 20, 1, None, -5])
print(sol.maxPathSum(root5))  # Output: 40 (20 + 2 + 10 + 10)

# Example 6 (all positive)
root6 = build_tree([1, 2, 3, 4, 5, 6, 7])
print(sol.maxPathSum(root6))  # Output: 28 (4+2+1+3+5+6+7)