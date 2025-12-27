from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Check if binary tree is symmetric around its center.
        A tree is symmetric if the left subtree is a mirror reflection of the right subtree.
        """
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # Both subtrees are empty
            if not left and not right:
                return True
            
            # One subtree is empty, other is not
            if not left or not right:
                return False
            
            # Check current nodes and recursively check mirrored pairs
            return (left.val == right.val and 
                    isMirror(left.left, right.right) and 
                    isMirror(left.right, right.left))
        
        # Empty tree is symmetric
        if not root:
            return True
        
        # Check if left and right subtrees are mirrors
        return isMirror(root.left, root.right)

# Example
print("Check if Binary Tree is Symmetric:")
print("\nSymmetric tree (example 1):")
print("""
        1
       / \\
      2   2
     / \\ / \\
    3  4 4  3
""")

# Build a symmetric tree
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)

solution = Solution()
result1 = solution.isSymmetric(root1)

print(f"\nIs the tree symmetric? {result1}")

print("\nComparison process:")
print("1. Compare root's left (2) and right (2): 2 == 2 ✓")
print("2. Compare left.left (3) with right.right (3): 3 == 3 ✓")
print("3. Compare left.right (4) with right.left (4): 4 == 4 ✓")
print("All comparisons pass → Tree is symmetric")

print("\n" + "="*50)
print("\nAsymmetric tree (example 2):")
print("""
        1
       / \\
      2   2
       \\   \\
        3    3
""")

# Build an asymmetric tree
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(3)

result2 = solution.isSymmetric(root2)
print(f"\nIs the tree symmetric? {result2}")

print("\nComparison process:")
print("1. Compare root's left (2) and right (2): 2 == 2 ✓")
print("2. Compare left.left (None) with right.right (3):")
print("   One is None, other is TreeNode(3) → Not symmetric ✗")
print("Tree is not symmetric")

print("\n" + "="*50)
print("\nSymmetric tree with single node (example 3):")
print("""
        1
""")

# Build single node tree
root3 = TreeNode(1)
result3 = solution.isSymmetric(root3)
print(f"\nIs the tree symmetric? {result3}")
print("Single node tree is always symmetric (trivially)")

print("\n" + "="*50)
print("\nAsymmetric tree (example 4):")
print("""
        1
       / \\
      2   2
     /   /
    3   3
""")

# Build another asymmetric tree
root4 = TreeNode(1)
root4.left = TreeNode(2)
root4.right = TreeNode(2)
root4.left.left = TreeNode(3)
root4.right.left = TreeNode(3)

result4 = solution.isSymmetric(root4)
print(f"\nIs the tree symmetric? {result4}")

print("\nComparison process:")
print("1. Compare root's left (2) and right (2): 2 == 2 ✓")
print("2. Compare left.left (3) with right.right (None):")
print("   One is TreeNode(3), other is None → Not symmetric ✗")