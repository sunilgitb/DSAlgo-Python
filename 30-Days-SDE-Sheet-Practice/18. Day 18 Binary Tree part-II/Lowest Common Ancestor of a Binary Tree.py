# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left == None:
            return right
        if right == None:
            return left
        return root
    
# Time: O(N)
# Space: O(1)

# Example Usage:
# Constructing the binary tree:
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \ \
#      7   4 
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
p = root.left  # Node with value 5
q = root.right  # Node with value 1
solution = Solution()
lca = solution.lowestCommonAncestor(root, p, q)
print(f"The Lowest Common Ancestor of nodes {p.val} and {q.val} is: {lca.val}")

# Explanation:
# The function lowestCommonAncestor recursively traverses the binary tree to find the lowest common ancestor of
# two given nodes p and q. It checks if the current root is None or matches either p or q, in which case it returns the root.
# It then recursively searches the left and right subtrees for p and q. If both left and right calls return non-None values,
# it means p and q are found in different subtrees, so the current root is their lowest common ancestor. If only one side returns a non-None value,
# it means both p and q are located in that subtree, so it returns that value.
# Time: O(N)