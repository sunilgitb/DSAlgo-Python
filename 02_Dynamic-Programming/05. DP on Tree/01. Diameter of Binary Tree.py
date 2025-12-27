# https://www.youtube.com/watch?v=zmPj_Ee3B8c&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=47
# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def solve(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_height = solve(node.left)
            right_height = solve(node.right)
            
            # Height of current subtree (max of left/right + 1)
            height = 1 + max(left_height, right_height)
            
            # Diameter through current node = left_height + right_height + 1
            diameter_through_node = left_height + right_height + 1
            
            # Update global max diameter
            self.res = max(self.res, diameter_through_node)
            
            # Return height to parent
            return height
        
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
#      /  \
#     4    5
root1 = build_tree([1, 2, 3, 4, 5])
print(sol.diameterOfBinaryTree(root1))  # Output: 4

# Example 2
# Tree:     1
#         /   \
#        2     3
#      /  \      \
#     4    5      6
root2 = build_tree([1, 2, 3, 4, 5, None, 6])
print(sol.diameterOfBinaryTree(root2))  # Output: 5

# Example 3 (single node)
root3 = build_tree([1])
print(sol.diameterOfBinaryTree(root3))  # Output: 0

# Example 4 (skewed tree)
root4 = build_tree([1, 2, None, 3, None, 4])
print(sol.diameterOfBinaryTree(root4))  # Output: 3

# Example 5
root5 = build_tree([4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2])
print(sol.diameterOfBinaryTree(root5))  # Output: 8