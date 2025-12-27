from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Find the lowest common ancestor of nodes p and q in binary tree.
        
        The LCA is the lowest (deepest) node that has both p and q as descendants
        (where a node can be a descendant of itself).
        """
        # Base cases
        if not root or root == p or root == q:
            return root
        
        # Search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right return non-null, current root is LCA
        if left and right:
            return root
        
        # Otherwise return the non-null child (if any)
        return left if left else right

# Example
print("Lowest Common Ancestor in Binary Tree:")
print("\nTree structure:")
print("""
        3
       / \\
      5   1
     / \\ / \\
    6  2 0  8
      / \\
     7   4
""")

# Build the tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Define nodes p and q
p = root.left      # Node 5
q = root.left.right.right  # Node 4

solution = Solution()
lca = solution.lowestCommonAncestor(root, p, q)

print(f"\nNode p: {p.val}")
print(f"Node q: {q.val}")
print(f"Lowest Common Ancestor: {lca.val}")

print("\nExplanation:")
print("1. Both p=5 and q=4 are in the left subtree of root 3")
print("2. From node 5 (p itself):")
print("   - q=4 is in the right subtree of 5")
print("   - So LCA is 5")
print("\nAlternative: If we search for nodes 5 and 1:")
print("   - 5 is in left subtree of 3")
print("   - 1 is in right subtree of 3")
print("   - So LCA would be 3")

print("\nAlgorithm logic:")
print("• If root is None or root is p or root is q → return root")
print("• Recursively search left and right subtrees")
print("• If both left and right return non-null → current root is LCA")
print("• Otherwise return whichever is non-null (or None if both null)")