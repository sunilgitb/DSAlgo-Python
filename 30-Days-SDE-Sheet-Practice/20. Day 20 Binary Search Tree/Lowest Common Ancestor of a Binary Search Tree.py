# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: 
            return 
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        return root


if __name__ == "__main__":
   
    # Build example BST:
    #        6
    #       / \
    #      2   8
    #     / \ / \
    #    0  4 7  9
    #      / \
    #     3  5
    n0 = TreeNode(0)
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n4.left = n3
    n4.right = n5
    n2 = TreeNode(2)
    n2.left = n0
    n2.right = n4
    n7 = TreeNode(7)
    n9 = TreeNode(9)
    n8 = TreeNode(8)
    n8.left = n7
    n8.right = n9
    root = TreeNode(6)
    root.left = n2
    root.right = n8

    sol = Solution()

    # Example 1: LCA of 2 and 8 -> 6
    lca1 = sol.lowestCommonAncestor(root, n2, n8)
    print(f"LCA of {n2.val} and {n8.val} ->", lca1.val if lca1 else None)

    # Example 2: LCA of 2 and 4 -> 2
    lca2 = sol.lowestCommonAncestor(root, n2, n4)
    print(f"LCA of {n2.val} and {n4.val} ->", lca2.val if lca2 else None)
